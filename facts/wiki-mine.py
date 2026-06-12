#!/usr/bin/env python3
"""wiki-mine.py — deterministic Wikipedia miner (NO LLM, NO key).

From the enwiki pages-articles JSONL, for one topic category, produce:
  terms.json   — glossary: term, page, url, lead-sentence definition (inline links
                 kept as markdown), related in-topic terms, media (with direct
                 Commons URLs + a recreate strategy)
  graph.json   — concept graph: nodes (with in-degree) + in-topic edges
  preview.md   — a human-readable slice to send to a domain expert

  python wiki-mine.py <enwiki.jsonl> --topic physics --out-dir <dir> [--limit N]
"""
import argparse, hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import facts_store as fs   # the one shared fact store (lookup/record/consensus)

CAT  = re.compile(r'\[\[Category:([^\]|]+)', re.I)
LINK = re.compile(r'\[\[([^\]|:#]+)(?:\|([^\]]+))?\]\]')          # internal concept links
FILE = re.compile(r'\[\[(?:File|Image):([^|\]\n]+)', re.I)        # filename only (linear, no backtracking)
REF  = re.compile(r'<ref[^>]*>.*?</ref>|<ref[^>]*/>', re.S | re.I)
TMPL = re.compile(r'\{\{[^{}]*\}\}')

# Hand-tuned aliases for topics where the CLI topic slug does not match
# Wikipedia category strings well. Match against page categories only.
TOPIC_ALIASES = {
 "physics": ["physics", "physical sciences", "thermodynamics", "electromagnetism",
             "electromagnetic", "quantum", "relativity", "optics", "astrophysics", "cosmology",
             "condensed matter",
             "nuclear physics", "statistical mechanic", "fluid dynamic",
             "classical mechanic", "particle physics"],
 "biology": ["biology", "biological", "life sciences", "cell biology", "genetics",
             "molecular biology", "ecology", "evolution", "physiology", "biochemistry",
             "microbiology", "anatomy", "botany", "zoology", "neuroscience"],
 "chemistry": ["chemistry", "chemical", "organic chemistry", "inorganic chemistry",
               "biochemistry", "physical chemistry", "analytical chemistry"],
 "branding": ["branding", "brand management", "brand equity", "brand identity",
              "brand architecture", "brand awareness", "brand valuation", "trademarks"],
 "marketing": ["marketing", "market research", "consumer behaviour", "consumer behavior",
               "market segmentation", "marketing strategy", "digital marketing",
               "marketing communications", "retailing", "sales"],
 "advertising": ["advertising", "advertisement", "ad campaigns", "advertising campaigns",
                 "advertising techniques", "advertising media", "promotion and marketing",
                 "public relations"],
 "copy_writing": ["copywriting", "copy writing", "advertising writing", "direct marketing",
                  "content marketing", "sales letters", "slogans"],
 "social_media": ["social media", "social networking", "online social networks",
                  "social media marketing", "social platforms", "internet culture"],
 "mathematics": ["mathematics", "mathematical", "math", "number theory", "topology",
                 "combinatorics", "discrete mathematics", "analysis", "probability"],
 "statistics": ["statistics", "statistical", "probability", "data analysis", "regression",
                "hypothesis testing", "estimation theory", "sampling", "bayesian"],
 "calculus": ["calculus", "differential calculus", "integral calculus", "multivariable calculus",
              "vector calculus", "differential equations", "mathematical analysis"],
 "algebra": ["algebra", "linear algebra", "abstract algebra", "commutative algebra",
             "group theory", "ring theory", "field theory", "algebraic"],
 "geometry": ["geometry", "geometric", "euclidean geometry", "non-euclidean geometry",
              "differential geometry", "algebraic geometry", "trigonometry"],
 "trigonometry": ["trigonometry", "trigonometric", "sine", "cosine", "tangent",
                  "triangles", "angle"],
 "astronomy": ["astronomy", "astronomical", "astrophysics", "cosmology", "planetary science",
               "stars", "galaxies", "solar system", "celestial mechanics"],
 "geology": ["geology", "geological", "earth sciences", "rocks", "minerals", "tectonics",
             "stratigraphy", "geomorphology", "volcanology", "seismology"],
 "meteorology": ["meteorology", "meteorological", "weather", "climate", "atmospheric sciences",
                 "atmospheric dynamics", "storms", "precipitation"],
 "oceanography": ["oceanography", "oceanographic", "marine science", "physical oceanography",
                  "chemical oceanography", "biological oceanography", "ocean currents",
                  "marine geology"],
 "environmental_science": ["environmental science", "environmental sciences", "environment",
                           "environmental studies", "environmental chemistry",
                           "environmental engineering", "conservation", "pollution",
                           "sustainability", "climate change"],
 "ecology": ["ecology", "ecological", "ecosystems", "biodiversity", "conservation biology",
             "population ecology", "community ecology", "biomes"],
 "anatomy": ["anatomy", "anatomical", "human anatomy", "comparative anatomy", "histology",
             "organ systems"],
 "physiology": ["physiology", "physiological", "human physiology", "animal physiology",
                "plant physiology", "neurophysiology", "exercise physiology"],
 "genetics": ["genetics", "genetic", "genomics", "heredity", "dna", "genes",
              "molecular genetics", "population genetics"],
 "microbiology": ["microbiology", "microbiological", "microorganisms", "bacteria", "bacteriology",
                  "virology", "mycology", "protists", "microbial"],
 "botany": ["botany", "botanical", "plants", "plant sciences", "plant taxonomy",
            "plant morphology", "plant physiology"],
 "zoology": ["zoology", "zoological", "animals", "animal taxonomy", "animal physiology",
             "invertebrates", "vertebrates", "mammalogy", "ornithology", "entomology"],
 "neuroscience": ["neuroscience", "neuroscientific", "neurobiology", "neurology", "brain",
                  "nervous system", "cognitive neuroscience", "neuroanatomy"],
 "psychology": ["psychology", "psychological", "cognitive science", "behavioral science",
                "behavioural science", "developmental psychology", "social psychology",
                "clinical psychology", "personality"],
 "sociology": ["sociology", "sociological", "society", "social science", "social theory",
               "social research", "social stratification", "demography"],
 "anthropology": ["anthropology", "anthropological", "cultural anthropology",
                  "social anthropology", "archaeology", "biological anthropology",
                  "ethnography"],
 "economics": ["economics", "economic", "economy", "econometrics", "political economy",
               "microeconomics", "macroeconomics", "finance"],
 "macroeconomics": ["macroeconomics", "macroeconomic", "monetary policy", "fiscal policy",
                    "inflation", "unemployment", "economic growth", "business cycle",
                    "national accounts"],
 "microeconomics": ["microeconomics", "microeconomic", "market structure", "game theory",
                    "consumer theory", "producer theory", "supply and demand",
                    "welfare economics"],
 "finance": ["finance", "financial", "investing", "investment", "corporate finance",
             "asset pricing", "banking", "capital markets", "risk management"],
 "accounting": ["accounting", "accountancy", "financial reporting", "auditing",
                "bookkeeping", "tax accounting", "management accounting"],
 "business": ["business", "commerce", "companies", "corporate", "organizational",
              "business models", "business strategy", "business terms"],
 "management": ["management", "organizational theory", "organisation theory",
                "strategic management", "operations management", "human resource management",
                "project management", "leadership"],
 "entrepreneurship": ["entrepreneurship", "entrepreneurial", "entrepreneurs", "startups",
                      "venture capital", "small business", "business incubators"],
 "political_science": ["political science", "politics", "political theory",
                       "comparative politics", "international relations", "public policy",
                       "public administration", "political philosophy"],
 "american_government": ["american government", "united states government",
                         "government of the united states", "u.s. government",
                         "us government", "united states congress", "presidency of the united states",
                         "united states federal law", "united states constitutional law"],
 "history": ["history", "historical", "historiography", "ancient history", "modern history",
             "social history", "political history", "military history"],
 "world_history": ["world history", "global history", "international history", "civilizations",
                   "ancient history", "medieval history", "early modern history",
                   "modern history"],
 "art_history": ["art history", "history of art", "art movements", "visual arts",
                 "paintings", "sculpture", "architecture", "artists", "iconography"],
 "philosophy": ["philosophy", "philosophical", "metaphysics", "epistemology", "ethics",
                "logic", "aesthetics", "philosophers"],
 "ethics": ["ethics", "ethical", "moral philosophy", "bioethics", "business ethics",
            "applied ethics", "normative ethics", "metaethics"],
 "logic": ["logic", "logical", "mathematical logic", "philosophical logic",
           "formal logic", "propositional calculus", "predicate logic"],
 "linguistics": ["linguistics", "linguistic", "language", "phonetics", "phonology",
                 "morphology", "syntax", "semantics", "pragmatics", "sociolinguistics"],
 "writing": ["writing", "rhetoric", "composition", "creative writing", "technical writing",
             "academic writing", "grammar", "style guides"],
 "literature": ["literature", "literary", "fiction", "poetry", "novels", "drama",
                "literary criticism", "literary theory", "genres"],
 "computer_science": ["computer science", "computing", "software engineering",
                      "theoretical computer science", "algorithms", "data structures",
                      "programming languages", "computer systems"],
 "programming": ["programming", "computer programming", "software development",
                 "programming languages", "programming constructs", "software engineering",
                 "coding"],
 "data_science": ["data science", "data analysis", "machine learning", "statistics",
                  "data mining", "big data", "databases", "visualization"],
 "artificial_intelligence": ["artificial intelligence", "machine learning", "deep learning",
                             "neural networks", "natural language processing",
                             "computer vision", "robotics", "expert systems"],
 "education": ["education", "educational", "pedagogy", "teaching", "learning",
               "curriculum", "educational psychology", "instructional design",
               "learning sciences"],
}


def topic_pattern(topic):
    aliases = TOPIC_ALIASES.get(topic, [topic.replace("_", " ")])
    parts = []
    for alias in aliases:
        words = [re.escape(w) for w in re.split(r'[\s_-]+', alias.strip()) if w]
        if not words:
            continue
        parts.append(r'[\s_-]+'.join(words) + r's?')
    return r'(?<![A-Za-z0-9])(' + '|'.join(parts) + r')(?![A-Za-z0-9])'


# Default exclusions drop works/media/pop-culture noise from concept-oriented
# slices. Some humanities topics intentionally mine those categories.
DEFAULT_EXCLUDE = (
    r'bestiar|manuscript|\bbooks?\b|literature|novels?|fiction|mytholog|folklore|'
    r'popular culture|films?|television|paintings?|drawings?|illustrations?|'
    r'sculptures?|poems?|songs?|albums?|video games?|comics?'
)
TOPIC_EXCLUDE = {
    "art_history": r'popular culture|films?|television|songs?|albums?|video games?|comics?',
    "literature": r'popular culture|films?|television|paintings?|drawings?|'
                  r'illustrations?|sculptures?|songs?|albums?|video games?|comics?',
    "writing": r'popular culture|films?|television|paintings?|drawings?|'
               r'illustrations?|sculptures?|songs?|albums?|video games?|comics?',
}
# A real definition has a copula near the start; otherwise the lead didn't parse cleanly.
DEF_OK = re.compile(r'\b(is|are|was|were|refers to|describes|denotes|consists? of)\b', re.I)


def plain(d):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', d) if d else d


def strip_templates(s):
    for _ in range(6):                # cap passes — avoid pathological loops on huge articles
        new = TMPL.sub('', s)
        if new == s:
            break
        s = new
    return s


def commons_url(fn):
    fn = fn.strip().replace(' ', '_')
    h = hashlib.md5(fn.encode()).hexdigest()
    return f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{fn}"


def media_strategy(fn, caption):
    low = (fn + ' ' + caption).lower()
    if fn.lower().endswith('.svg'):
        return ("diagram", "redraw-svg")          # facts in visual form → our own SVG
    if any(k in low for k in ('plot', 'chart', 'graph of', 'curve', 'spectrum', 'histogram')):
        return ("chart", "d3-from-data")
    if fn.lower().endswith(('.jpg', '.jpeg')):
        return ("photo", "use-if-free-else-omit")  # never AI-fake a real specific photo
    return ("image", "review")


def wiki_url(target):
    target = target.strip().replace(' ', '_')
    return "https://en.wikipedia.org/wiki/" + (target[:1].upper() + target[1:])   # MediaWiki capitalizes the first letter


def link_to_md(m):
    tgt = m.group(1).strip(); disp = (m.group(2) or tgt).strip()
    return f"[{disp}]({wiki_url(tgt)})"


def lead_sentence(text):
    t = strip_templates(REF.sub('', text[:6000]))  # lead is at the top; bound the work
    m = re.search(r"'''.+?'''", t)                 # the bolded subject
    if not m:
        return None
    seg = t[m.start():]
    ms = re.search(r'\.\s', seg)
    lead = seg[:ms.end()] if ms else seg[:400]
    lead = re.sub(r"'''|''", '', lead)             # remove bold/italic marks
    lead = LINK.sub(link_to_md, lead)              # [[x|y]] -> [y](url)
    return re.sub(r'\s+', ' ', lead).strip()


def term_of(title):
    return re.sub(r'\s*\(.*?\)$', '', title).strip()


def url_of(title):
    return "https://en.wikipedia.org/wiki/" + title.replace(' ', '_')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jsonl")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--limit", type=int, help="scan only the first N lines (sampling)")
    args = ap.parse_args()

    allow = re.compile(topic_pattern(args.topic), re.I)
    exclude = re.compile(TOPIC_EXCLUDE.get(args.topic, DEFAULT_EXCLUDE), re.I)

    arts = {}
    for i, line in enumerate(open(args.jsonl, encoding="utf-8")):
        if args.limit and i >= args.limit:
            break
        try:
            r = json.loads(line)
        except Exception:
            continue
        t = r["text"]
        if '#redirect' in t[:300].lower():
            continue
        cats = [c.strip() for c in CAT.findall(t)]
        if not any(allow.search(c) for c in cats):
            continue
        if any(exclude.search(c) for c in cats):     # works/culture noise, unless topic-relevant
            continue
        title = r["title"]
        media = []
        seen_files = set()
        for fn in FILE.findall(t):
            fn = fn.strip()
            if fn in seen_files:
                continue
            seen_files.add(fn)
            typ, strat = media_strategy(fn, "")
            media.append({"file": fn, "commons_url": commons_url(fn), "type": typ, "strategy": strat})
        d = lead_sentence(t)
        if d and not DEF_OK.search(plain(d)[:140]):   # garbled lead → no usable definition
            d = None
        arts[title] = {
            "term": term_of(title), "page": title, "url": url_of(title),
            "definition": d,
            "categories": [c for c in cats if allow.search(c)][:6],
            "_targets": [d.strip() for d, _ in LINK.findall(t)],
            "media": media[:6],
        }

    nodes = set(arts)
    indeg = {n: 0 for n in nodes}
    edges = []
    for src, a in arts.items():
        seen = set()
        for tgt in a["_targets"]:
            if tgt in nodes and tgt != src and tgt not in seen:
                seen.add(tgt); indeg[tgt] += 1; edges.append([src, tgt])
    for src, a in arts.items():
        a["related"] = [term_of(x) for x in dict.fromkeys(a["_targets"]) if x in nodes and x != src][:8]
        del a["_targets"]

    os.makedirs(args.out_dir, exist_ok=True)
    terms = sorted(arts.values(), key=lambda x: x["term"].lower())
    json.dump(terms, open(os.path.join(args.out_dir, "terms.json"), "w"), indent=2, ensure_ascii=False)
    graph = {"nodes": [{"term": term_of(n), "page": n, "url": url_of(n), "in_degree": indeg[n]} for n in nodes],
             "edges": edges}
    json.dump(graph, open(os.path.join(args.out_dir, "graph.json"), "w"), indent=2, ensure_ascii=False)

    # facts.json — each definition is a citable Wikipedia fact (deterministic; source=wikipedia,
    # tier=solid). Single-source = "unverified" candidates that gain votes when merged with
    # OpenStax/PubMed/expert evidence via the shared store.
    sources = fs.load_sources()
    tier, _ = fs.source_meta("wikipedia", sources)
    facts = []
    for a in terms:
        if not a["definition"]:
            continue
        text_plain = plain(a["definition"])             # strip md links for the canonical/verbatim
        cit = {"source": "wikipedia", "publisher": "wikimedia", "book": None,
               "repo": None, "module": a["page"], "url": a["url"]}
        ex = {"canonical": text_plain, "verbatim": text_plain, "domain": [args.topic],
              "stable": True, "category": "DEFINITION"}
        fs.merge_fact(facts, fs.make_fact(ex, cit, tier, sources), sources)
    fs.save_facts(facts, os.path.join(args.out_dir, "facts.json"))

    # preview.md — for a domain expert
    foundational = sorted(nodes, key=lambda n: -indeg[n])[:20]
    media_n = sum(len(a["media"]) for a in arts.values())
    with open(os.path.join(args.out_dir, "preview.md"), "w", encoding="utf-8") as f:
        f.write(f"# {args.topic.title()} — Wikipedia knowledge slice (for expert review)\n\n")
        f.write(f"Auto-extracted, deterministically (no AI), from the English Wikipedia dump"
                f"{' (sample of first %d pages)' % args.limit if args.limit else ''}.\n"
                f"**{len(nodes)} terms · {len(edges)} concept links · {media_n} media refs.** "
                f"Please flag anything wrong — definitions are Wikipedia's lead sentences, verbatim.\n\n")
        f.write("## Most-connected concepts (a prerequisite/foundation signal)\n\n")
        for n in foundational:
            f.write(f"- **{term_of(n)}** — linked by {indeg[n]} other {args.topic} pages · {url_of(n)}\n")
        f.write("\n## Glossary sample (alphabetical, first 30)\n\n")
        for a in terms[:30]:
            d = a["definition"] or "*(no lead sentence parsed)*"
            f.write(f"### {a['term']}\n{d}\n\n")
            f.write(f"- page: {a['url']}\n")
            if a["related"]:
                f.write(f"- related: {', '.join(a['related'][:6])}\n")
            if a["media"]:
                f.write(f"- media: {len(a['media'])} (e.g. `{a['media'][0]['file']}` → {a['media'][0]['strategy']})\n")
            f.write("\n")
    print(f"{args.topic}: {len(nodes)} terms, {len(edges)} edges, {media_n} media, {len(facts)} facts → {args.out_dir}/")


if __name__ == "__main__":
    main()
