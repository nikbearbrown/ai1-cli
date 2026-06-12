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

---

## Front Matter

- **Copyright**
- **Preface** — why this book exists, in the author's voice

## Introduction

What AI+1 is in two pages — one human plus agents, the human load-bearing — the three ways in (download a finished book / learn by doing right here / build from scratch), and how to read this book: do the exercises; the prose is just enough to know why.

## Chapters

**Part I — Make a Book Yours**

1. **Download a Book and Change One Sentence** — Clone a finished, fact-checked AI+1 book (the cancer-biology textbook), edit one sentence, run `./build.sh`, open the EPUB. Capability: rebuild a real book end to end and see your change in it. *(The pebble: the whole factory, first sitting.)*
2. **Retitle It, Re-Cover It, Make It Build for Kindle** — `metadata.yaml`, title/author, a cover image, a clean EPUB into Kindle Previewer or a device. Capability: own the book's identity and ship the file Kindle accepts.
3. **Rewrite a Chapter in Another Voice** — Run a `voices/` rewrite (Socratic, Wonder, Sardonic…), diff it against the original, decide which serves the reader. Capability: direct AI rewriting and *judge* it — the original stays untouched.
4. **Generate the Study Layer** — Quizzes, practice exercises, an Anki deck from the chapters; find the question generation got wrong. Capability: produce learning assets and audit them instead of trusting them.
5. **Export to Canvas** — `build-canvas.sh` → `.imscc`, import into a Canvas course, check module order against the book's BLUEPRINT.md. Capability: turn a book into a course shell any LMS accepts.
6. **Facts: Check a Claim, Record It, Sign It** — Trace one claim to `facts/facts.json`, add a new sourced fact (`verified: false`), sign one as the human. Capability: the verified-artifact habit — recorded beats remembered.

**Part II — Change the Substance**

7. **Swap In Your Subject** — Replace one chapter of the downloaded book with a chapter on something you know, drafted by the agent from your notes. Capability: author *inside* the factory.
8. **The Human Rewrite** — Take the agent's draft and make it sound like you; sign your first GATE 3 — the gate no agent may ever sign. Capability: the irreducible part, experienced.
9. **Figures That Pass Audit** — Generate an SVG figure, render PNG, run `svg-visual-audit`, fix what it flags. Capability: illustrated chapters with a clean audit, not just pictures.

**Part III — Build From Scratch**

10. **Blueprint Your Book** — Run Blueprint (Phase 0) on your own idea: vision, architecture, chapter spec, risks, outline; sign GATE 0. Capability: a defensible plan instead of a topic list.
11. **Research, Then Draft, Then Rewrite** — Phases 1–3: research notes before drafting, chapters from research not model memory, your rewrite behind GATEs 1–3. Capability: a full draft with a trail.
12. **Fact-Check, Finish, Ship Everywhere** — Phases 4–6, then every export: EPUB/Kindle, Canvas (`.imscc`), Medhavy (`.mdx`), and the study layer. The exercise covers *producing* the Medhavy export; what Medhavy can do with it — things Kindle and Canvas can't — is its own book, referenced here, not taught here. Capability: the honest run, completed — your book, checked, everywhere.

## Back Matter

- **Acknowledgments**
- **About the Author**
- **Appendices** — the full prompt libraries the chapters invoke (Blueprint library, research pass, chapter writer, fact-check, enrichment generators, Canvas/imscc, react-site, Ask-AI). Existing appendix files 80–97 persist here.
- **References**

---

## Notes on Order

Part I is strictly easiest-win-first: Chapter 1 is deliberately the whole system in one sitting (Merrill's whole-task principle — the pebble in the pond), and every Part I chapter works on a *finished* book so nothing the reader does can fail for lack of content. Facts (6) closes Part I because by then the reader has shipped enough artifacts to feel why "recorded beats remembered" matters. Part II crosses from operating to authoring; the human rewrite (8) must follow authoring-with-an-agent (7) so the reader has a draft worth owning, and precedes figures (9) because audits make more sense once you've signed something. Part III is the spine in order — it cannot be reordered; the gates enforce it. Chapter count is 12 (+ intro), inside Blueprint's 12–14 target for a semester course; each Part I chapter is one sitting, Part III chapters span multiple sessions by design.

**Mapping from the previous draft chapters (00–20):** their prose becomes overview-section seed material — 01 (what AI+1 is) → Introduction; 02/04 (Blueprint) → Ch 10; 03/06 (research) → Ch 11; 05 (scaffold) → Ch 1–2 overviews; 07–08 (writing/rewrite) → Ch 7–8; 09/11 (figures) → Ch 9; 10/13/15/16 (enrichment, glimmers, spaced repetition) → Ch 4; 12 (final check/build) → Ch 1 and 12; 14 (case studies) → distributed into exercises; 17 (Canvas) → Ch 5; 18–20 (react site, LTI, Ask-AI) → appendices/Ch 12 pointers. Appendices 80–97 stay as the libraries.
