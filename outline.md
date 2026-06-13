<!--
    outline.md
    TABLE OF CONTENTS — your chapter-level planning document.

    This is NOT the auto-generated TOC that appears in the EPUB
    (pandoc handles that via --toc in build.sh). This file is YOUR
    working outline: chapter titles, one-line descriptions, and the
    order of arguments before you start drafting.

    Keep it in sync with the actual chapter files in chapters/.
    When the outline diverges from the drafts, update one or the other —
    don't let them drift.
-->

# AI1 CLI — Outline

**Author:** Nik Bear Brown

**Chapter shape (every chapter):** a short overview — what you're about to do and why the system works this way (1–3 pages) — then exercises, which are the chapter. Every exercise ends with an artifact you can open and a line in the trail (gate, sidecar, or log).

**The running project (one thread, whole book):** download the *Writing Guide* — a finished, fact-checked 24-chapter composition textbook — and remake it into a **copywriting book**: operate it, prune it, convert it, extend it, re-architect it with Blueprint, and ship it to Kindle, Canvas, and Medhavy. Everyone writes; no domain expertise required to play.

---

## Front Matter

- **Copyright**
- **Preface** — why this book exists, in the author's voice

## Introduction

What AI+1 is in two pages — one human plus agents, the human load-bearing — the three ways in (download a finished book / learn by doing right here / build from scratch), the running project, and how to read this book: do the exercises; the prose is just enough to know why.

## Chapters

> **AMENDMENT (2026-06-12, logged, not drift):** a new Chapter 2 — **Chapter Research** — is inserted after the Blueprint chapter, per author direction: Phase 1 of the spine (research every Blueprint chapter into pantry notes, human checks the flags) belongs in the running project before any operating or drafting. Chapters below renumber +1 from the old Ch 2 onward at the next outline revision; chapter count 12→13, still within range. The chapter file exists: `chapters/02-chapter-research.md`.

**Part I — Blueprint First, Then Operate**

1. **Inventory, Research, Blueprint, Sign-Off** — Everything starts with the Blueprint, and the Blueprint starts with evidence. The exercise, in order: **(a)** clone `writing-guide` and *list the current book* — all 24 chapters, what each teaches, approximate length; **(b)** *generate a research prompt* with the agent around two questions: how should a composition textbook be restructured into a copywriting book, and do the classic direct-advertising principles (differentiator before copy, features→benefits, earn attention first — referenced as principles, never as name-brand endorsement) still apply in an AI world of generated copy, feeds, and search; **(c)** *run the research*; **(d)** *save it to `pantry/`* — research is a citizen of the repo, not of the chat scroll; **(e)** run Blueprint against the inventory + research to produce the new book's plan: vision, architecture (including the **assessment plan**: which quizzes, exercises, flashcards, Canvas modules this book needs), chapter spec, risks; **(f)** the reader reviews and, if they approve, *the approval is logged* — GATE 0 signed in `STATUS.md`, their first signature, on a plan built from evidence they commissioned. Capability: the full loop — inventory → research → plan → human sign-off — before a single chapter is touched.
2. **Rebuild the Book You Just Replanned** — Change one sentence, run `./build.sh`, find it in the EPUB (the pebble: the whole factory, one sitting). Then new title, author, cover in `metadata.yaml`; a clean EPUB into Kindle Previewer; and `sync-to-book.sh` so the book gains AI1.md, CONDUCTOR.md, and verify tooling — writing-guide predates the constitution, so the reader performs the adoption. Capability: rebuild a real book end to end and put it under governance.
3. **Rewrite a Chapter in Another Voice** — Run a `voices/` rewrite (Socratic, Wonder, Sardonic…), diff against the original, judge which serves the *copywriting* reader the Blueprint named; originals stay untouched. Capability: direct AI rewriting and *judge* it.
4. **Generate the Assessments the Blueprint Promised** — Produce the study layer the Chapter 1 assessment plan called for — quizzes, practice exercises, an Anki deck; find the question generation got wrong. Capability: assessments as planned deliverables, audited instead of trusted.
5. **Export to Canvas** — `build-canvas.sh` → `.imscc`, import into a Canvas course, check module order against the signed Blueprint. Capability: turn a book into a course shell any LMS accepts.
6. **Facts: Check a Claim, Record It, Sign It** — Trace one claim to the fact dictionary, add a new sourced fact (`verified: false`), sign one as the human. Capability: the verified-artifact habit — recorded beats remembered.

**Part II — Execute the Conversion**

7. **Cut to the Blueprint** — The signed plan says which of the 24 chapters serve a copywriter and which don't. Make the cuts; log every exclusion with its reason and owner (the Editorial Review's organization diagnosis is the evidence base). Capability: the power of No, executed against a plan rather than a mood.
8. **Convert What Survives** — Agent-assisted transformation of the keepers: profile → case study, proposal → pitch, evaluation → product review, rhetorical analysis → ad teardown; then the human rewrite and your first GATE 3 — the gate no agent may ever sign. Capability: re-purpose with the agent, own the result as the author.
9. **Add What's Missing** — Draft the chapters the Blueprint called for that composition never had (headlines, hooks and CTAs, landing pages, email sequences, brand voice — see `pantry/ogilvy-ideas.md` for the seed material); figures generated and passed through the visual audit. Capability: author new material *inside* the factory, illustrated and checked.

**Part III — Verify Against the Plan, Then Ship**

10. **The Manuscript Meets the Blueprint** — Run the Editorial Review and Blueprint's adoption-failure critique (`/g2`) against the converted book; compare what got built to what was signed at GATE 0; revise manuscript or plan — explicitly, with a changelog, never by silent drift. Capability: delivery vs. promise, judged with evidence.
11. **Fact-Check Old and New** — The inherited chapters carry the old book's claims; the new chapters carry yours. Research notes and fact-check both (Phases 1 + 4 in miniature); every claim sourced or cut. Capability: a full, checked manuscript with a trail.
12. **Ship Everywhere** — Final build: EPUB/Kindle, Canvas (`.imscc`), Medhavy (`.mdx`), and the assessments regenerated against the final text. The exercise covers *producing* the Medhavy export; what Medhavy can do with it — things Kindle and Canvas can't — is its own book, referenced here, not taught here. Capability: the honest run, completed — your book, checked, everywhere.

**Coda — From Scratch.** Two pages, not a chapter: everything in Parts I–III, minus the downloaded book — Blueprint from an empty starter is the same Phase 0 the reader already ran in Chapter 10. Pointer to the conductor spine and the Blueprint library.

## Back Matter

- **Acknowledgments**
- **About the Author**
- **Appendices** — the full prompt libraries the chapters invoke (Blueprint library, research pass, chapter writer, fact-check, enrichment generators, Canvas/imscc, react-site, Ask-AI). Existing appendix files 80–97 persist here.
- **References**

---

## Notes on Order

One project, three movements: plan-then-operate (I), transform (II), verify-and-ship (III) — each movement assumes only the artifacts the previous one produced, so the dependency chain is the project itself. **Everything starts with the Blueprint**: Chapter 1 is the plan and the sign-off, because that is the system's own rule and the reader should live it before touching a file — and because the assessment plan decided there gives Chapters 4, 5, and 12 their shopping list. The conversion *discussion* in Chapter 1 is where judgment enters first: the reader argues with Blueprint about what a copywriting book even is, and writing-guide's 24 inherited chapters guarantee the consolidation audit fires authentically, not as a staged demo. Chapter 2 then delivers the fast whole-task win (build, see your sentence) on the book they just replanned. In Part II, cutting (7) precedes converting (8) — you don't pay to convert what the plan already killed — and adding (9) follows so the reader knows the manuscript's voice before extending it. Part III closes the loop the way the constitution demands: the manuscript is verified *against the signed plan* (10), the claims against sources (11), and only then shipped (12). Chapter count is 12 (+ intro + coda), inside Blueprint's 12–14 target.

**Mapping from the previous draft chapters (00–20):** their prose becomes overview-section seed material — 01 (what AI+1 is) → Introduction; 02/04 (Blueprint) → Ch 10; 03/06 (research) → Ch 11; 05 (scaffold) → Ch 1–2 overviews; 07–08 (writing/rewrite) → Ch 8–9; 09/11 (figures) → Ch 9; 10/13/15/16 (enrichment, glimmers, spaced repetition) → Ch 4; 12 (final check/build) → Ch 1 and 12; 14 (case studies) → distributed into exercises; 17 (Canvas) → Ch 5; 18–20 (react site, LTI, Ask-AI) → appendices/Ch 12 pointers. Appendices 80–97 stay as the libraries.
