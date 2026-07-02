# BLUEPRINT.md — AI1 CLI

**Author:** Nik Bear Brown
**Status:** Synthesized from planning files + chapters in silent mode (Blueprint /scaffold). Review before use.

---

## Concept
This book teaches making books by talking to a CLI agent — the AI+1 system, one human plus AI agents with the human as the load-bearing author who signs every decision that matters. It is learned through one continuous hands-on project: download a finished, fact-checked 24-chapter writing guide and remake it into a copywriting book, behind gates, with every step leaving a trail.

**Target course / reader:** A non-technical author, teacher, or student comfortable with email and chatting with an AI — nothing more — who has a book in them (or a course that needs one). Primary context: self-paced individual use (one author, a CLI agent, a free weekend per Part); secondarily a workshop or half-semester course module on AI-assisted authorship (12 chapters ≈ 12 sessions).

## Three-Act Arc
From architecture.md:
- **Act One — Establish (Intro–Ch 6):** the inciting question — what should this book become, and how do I run the factory that makes it? By the end the reader has a signed plan and full command of the operating surface (build, voice, assessments, Canvas, facts).
- **Act Two — Build (Ch 7–9):** the hard middle — judgment under load. Cutting, converting, authoring; GATE 3 is the act's emotional center, the moment the book becomes theirs.
- **Act Three — Apply (Ch 10–12):** integration — the manuscript is held against the plan, the claims against sources, and the book ships everywhere.

Arc statement: takes the reader from *chatting with an AI* to *shipping a checked, multi-format book they signed*, by first making them sign a plan built from evidence, then remake a real book against that plan, then prove the result honest and ship it. (Ch 13 is a capstone extension beyond the three-act arc.)

## Chapter-by-Chapter
| # | Chapter | Capability built (DO) |
|---|---------|----------------------|
| Intro | Introduction | Explain AI+1's labor split (agent executes, human signs) and name the three ways into the system. |
| 1 | Inventory, Research, Blueprint, Sign-Off | Run the evidence→plan→signature loop — inventory a 24-chapter book, generate and run research to the pantry, sign or refuse GATE 0 — before touching content. |
| 2 | Chapter Research | Research every Blueprint chapter into pantry notes and check the flags before drafting any chapter (Phase 1 of the spine). *(Drafted as Ch 2; per the logged amendment this research chapter shifts operating chapters +1.)* |
| 3 | Rewrite a Chapter in Another Voice | Produce a voice rewrite without touching the original and judge, with cited passages, which voice serves the Blueprint's reader. *(outlined; not drafted)* |
| 4 | Generate the Assessments the Blueprint Promised | Generate quizzes, exercises, and an Anki deck from chapters, then find and document a generated question that fails its outcome. *(outlined; not drafted)* |
| 5 | Export to Canvas | Build and import an `.imscc` and verify module order against the signed plan. *(outlined; not drafted)* |
| 6 | Facts: Check a Claim, Record It, Sign It | Trace a claim to the fact dictionary, add a sourced fact (`verified: false`), and sign one fact as the human. *(outlined; not drafted)* |
| 7 | Cut to the Blueprint | Execute deletions against the signed plan, logging each exclusion with reason and owner. *(outlined; not drafted)* |
| 8 | Convert What Survives | Transform surviving chapters to copywriting genres with the agent, perform the human rewrite, and sign GATE 3. *(outlined; not drafted)* |
| 9 | Add What's Missing | Draft net-new copywriting chapters from research (not model memory) and produce figures that pass the visual audit. *(outlined; not drafted)* |
| 10 | The Manuscript Meets the Blueprint | Run Editorial Review + adoption-failure critique and reconcile manuscript and plan explicitly with a changelog. *(outlined; not drafted)* |
| 11 | Fact-Check Old and New | Distinguish inherited from new claims and source or cut every checkable claim. *(outlined; not drafted)* |
| 12 | Ship Everywhere | Produce final EPUB/Kindle, Canvas `.imscc`, Medhavy `.mdx`, and regenerated assessments, then walk the provenance chain. *(outlined; not drafted)* |
| 13 | From Book to Video | Turn one finished, signed chapter into a previewed narrated lecture spine with Unreal Reels, run the fidelity pass, and sign the lecture. *(capstone / extension)* |

*Note: the drafted `chapters/` currently holds Intro, Ch 1, Ch 2 (Chapter Research), Ch 13, and appendices 80–97. Chapters 3–12 are outlined but not yet drafted. Numbering above follows outline.md; per the 2026-06-12 amendment the inserted research chapter renumbers later chapters at the next outline revision. [INFERRED] mapping of outline titles to the not-yet-renumbered slots.*

## Prerequisites
From vision.md / architecture.md: chatting with an AI agent (Yes); installing a CLI agent — Cowork/Claude Code/Codex (Probably; handled in the Introduction setup box); `git clone` one command (Probably; exact line given in Ch 1); Markdown literacy (Probably; taught by exposure in Ch 2). Hard "No" ratings — Kindle Previewer/device access (fallback resolved inside Ch 2 — [NEEDS HUMAN INPUT: preferred fallback, web EPUB reader?]) and Canvas access (free Canvas teacher account, viability to confirm). Fewer than 3 hard No ratings after treatment → no foundations chapter; front-loaded via the Introduction.

## Positioning (one line)
Unlike prompt guides, which teach you to ask better, this book teaches you to *ship* — for readers who need a finished, checked book they can sign their name to.
