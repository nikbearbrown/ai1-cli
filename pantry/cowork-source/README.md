# Cowork-source — staged seed for the restructured chapters

These 21 files are the **drafted chapter bodies from the older `ai1-cowork` draft**,
ported here and reframed for the Cowork app (CLI/terminal framing → Cowork desktop app)
with terminology aligned (Tic-TOC → Blueprint). They are **source material, not chapters.**
They live in `pantry/` (the book's source area), not in `chapters/`, so the book keeps its
restructured 13-chapter structure and does not carry two overlapping tables of contents.

Their prose becomes **overview-section seed material** for the restructured chapters, per
the mapping in `outline.md`. Fold them in when drafting Chapters 3–12; do not ship them
as standalone chapters.

Sidecars were moved alongside as `*.verified.json.bak` (renamed so `verify.py` does not
treat them as gated chapter artifacts).

## Mapping — source file → restructured target (from outline.md)

| Source (old draft) | Feeds restructured target |
|---|---|
| `01-what-ai-plus-one-is.md` | Introduction (what AI+1 is) |
| `02-chapter-01.md` | placeholder in the old draft (near-empty) — no target; keep for reference |
| `02-what-tic-toc-does.md` | Ch 10 (Blueprint) — also underpins Ch 1's Blueprint overview |
| `04-generating-your-tiktoc.md` | Ch 10 (Blueprint) — also Ch 1 |
| `03-domain-research.md` | Ch 11 (research / fact-check) |
| `06-research-pass.md` | Ch 11 (research / fact-check) |
| `05-book-scaffold.md` | Ch 1–2 overviews (scaffold/rebuild) |
| `07-chapter-writing.md` | Ch 8 (convert what survives) — writing |
| `08-the-human-rewrite.md` | Ch 8–9 (human rewrite / GATE 3) |
| `09-finishing-pass-and-figures.md` | Ch 9 (figures) |
| `11-creating-figures.md` | Ch 9 (figures) |
| `10-enrichment-for-ai.md` | Ch 4 (assessments / enrichment) |
| `13-enriched-layer.md` | Ch 4 (assessments / enrichment) |
| `15-glimmers.md` | Ch 4 (assessments / enrichment) |
| `16-spaced-repetition.md` | Ch 4 (flashcards / Anki) |
| `12-final-check-and-build.md` | Ch 1 (build-early win) and Ch 12 (ship) |
| `14-case-studies.md` | distributed into exercises across chapters |
| `17-canvas-course-export.md` | Ch 5 (export to Canvas) |
| `18-react-site.md` | appendix / Ch 12 pointer |
| `19-medhavy-lti.md` | Ch 12 (Medhavy export) / appendix |
| `20-ask-ai-everywhere.md` | appendix / Ch 12 pointer |

## Status

Chapters 3–12 of the restructured book are **not yet drafted** — that is the book's real
remaining Phase-2 work. Draft them from this seed + the copywriting running project
(writing-guide → copywriting), per each chapter's spec in `chapters-spec.md`. The old
generic-process prose seeds the "why it works this way" overviews; the exercises must be
authored around the running project, not lifted from the old draft.
