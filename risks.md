<!--
    risks.md
    Blueprint Phase 4: Scope, Market, and Risk.
-->

# AI1 CLI — Scope, Market, and Risk

**Author:** Nik Bear Brown

*Phase 4 output from Blueprint. Drafted from book.md + outline.md (approved direction, 2026-06-12). Sidecar unverified until human sign-off.*

---

## Comparable Texts Analysis

Argued by category in vision.md (pandoc docs / prompt guides / self-publishing guides). [NEEDS HUMAN INPUT — three named titles with author/publisher/year for the proposal; category analysis suffices for design decisions but not for an acquisitions meeting.]

**Differentiation statements:**
- Unlike format-conversion documentation, which assumes you have a book, this book produces the book — plan, gates, facts, judgment — for readers whose real problem is everything before pandoc.
- Unlike prompt-engineering guides, which end at better output, this book ends at a shipped, checked, signed artifact — for readers who need to stand behind the result.
- Unlike self-publishing guides, which teach one storefront, this book teaches a production system whose exports (Kindle, Canvas, Medhavy) are interchangeable endpoints.

## Adoption Decision Tree (self-paced reader's version of syllabus fit)

Does the promise match a project I actually have? (running-project structure = yes for anyone with a book/course in them) · Can I do this with what I own? (chat-level skills + free tools — the two access risks are Kindle preview and Canvas account, both with in-chapter fallbacks) · Will I finish? (12 chapters, artifact per sitting, Part I in a weekend) · Do I trust it? (the book is produced by its own system; the trail is in the repo).

## Market Size Estimate

[NEEDS HUMAN INPUT — honest numbers require a decision about channel (KDP self-pub? course companion? both?). Directionally: the addressable reader is "people who write and chat with AI," which is large; the *reachable* reader via Substack/courses/NEU network is the real planning number, and only the author can estimate it.]

## Feature List with Priority Tags

| Feature | Tag | Producer |
|---|---|---|
| 12 chapters + intro + coda, exercise-first | ESSENTIAL | author + agent |
| writing-guide as downloadable input (public repo, stable) | ESSENTIAL | author (keep repo public + tagged) |
| In-chapter exercises with artifact + log deliverables | ESSENTIAL | author |
| Canvas `.imscc` of the book itself | IMPORTANT | repo tooling (Ch 5 process) |
| Generated quizzes + Anki deck | IMPORTANT | repo tooling (Ch 4 process) |
| Worked-solution exemplars (one/chapter) | VALUABLE | author, appendix |
| Editorial-review + audit prompt appendices | VALUABLE | already canonical in conductor/ |
| Video walkthroughs per chapter | ASPIRATIONAL | [NEEDS HUMAN INPUT — commit or cut] |

ESSENTIAL = 3 of 8 (37%) ✔ under the 40% rule.

**Minimum Viable Textbook:** chapters + exercises + a public writing-guide repo. That package alone is adoptable for the self-paced reader; everything else raises completion and course adoption.

## Out of Scope (the record of No)

| Item | Reason | Reopen condition |
|---|---|---|
| What Medhavy does | own book (book.md, 2026-06-12, author) | never in this book; cross-reference only |
| Prompt-engineering theory | category this book positions against | a chapter-level sidebar at most |
| KDP/storefront mechanics | platform-specific, fast-aging | second edition if readers demand |
| Toolchain internals / extending scripts | developer audience, not this reader | companion doc in `docs/` |
| Exam bank | self-paced primary context | course adoption at scale |
| Name-brand framing of advertising principles | author rule, 2026-06-12: principles cited as principles, tested as hypotheses; no endorsement-by-name | PERMANENTLY EXCLUDED |

**Coherence check:** the exclusions point at two other books (Medhavy book; a developer guide) — both already exist as intentions. ✔

## Adoption Risk Register

| Risk | Cat | L | I | Trigger | Mitigation | Contingency |
|---|---|---|---|---|---|---|
| Tool drift: CLI agents/platforms change faster than print | Timing | **H** | M | any agent UI change breaking a step | steps phrased as intents ("ask the agent to…"), platform specifics in boxed current-as-of notes; repo is updatable even when print isn't | errata file in repo; chapter steps point to repo for "current commands" |
| writing-guide availability/divergence | Production | M | **H** | repo moved, renamed, or restructured | tag a frozen release (e.g. `ai1-input-v1`) and have Ch 1 clone the tag | vendor a snapshot into a companion repo |
| Reader lacks Canvas/Kindle access | Content | M | M | free-account policy changes | fallbacks in-chapter; neither export is load-bearing for the arc | swap Ch 5 demo LMS; web EPUB reader |
| Ch 1 planning-first opener loses impatient readers | Structure | M | **H** | early-reader feedback / DNF at Ch 1 | Ch 1 is built as actions with a first-session artifact; Ch 2 promise stated up front | if testing confirms, swap Ch 1/Ch 2 order — logged as plan amendment, not drift |
| Agent variance: same exercise, different agent behavior | Content | **H** | M | reader's agent ignores a gate or invents steps | every exercise defines done by *artifact*, not by agent behavior; "what can go wrong" boxes | the variance itself is teachable — judgment sidebar pattern |
| Author bandwidth: 12 chapters + 2 hard ones | Production | M | **H** | drafting stalls after Part I | the system's own spine: chapters behind gates, drafted from this spec; hard chapters (8, 9) get scheduled first | [NEEDS HUMAN INPUT — timeline + whether volunteers/contributors are in play] |

## Top 3 Adoption Risks

**1. Tool drift.** The book teaches a living toolchain from dead trees. The mitigation is architectural, not editorial: the stable core is the loop (inventory → research → plan → sign → build → verify → ship), platform specifics are quarantined in boxed steps, and the repo — not the book — is the source of current commands. The book must say this about itself, in the introduction, as a feature.

**2. Ch 1 attrition.** Opening with planning is the right pedagogy and a real bounce risk. The chapter survives only if every block lands as an *action with an artifact* — the inventory table, the pantry research file, the signature. If early readers stall, the fallback (build-first, plan-second) is a logged plan amendment.

**3. Agent variance.** No two readers' agents will behave identically, and the book can't QA every model. Defining every exercise's "done" as an artifact the reader can open — never as "the agent will then say…" — is the only durable defense, and it happens to be the book's own thesis applied to itself.
