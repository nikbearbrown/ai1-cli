<!--
    vision.md
    Blueprint Phase 1: Vision and Positioning.
-->

# AI1 CLI — Vision

**Author:** Nik Bear Brown

*Phase 1 output from Blueprint. Drafted from book.md + outline.md (approved direction, 2026-06-12). Sidecar unverified until human sign-off.*

---

## Book Concept Summary

This book teaches **making books by talking to a CLI agent** to **non-technical authors, teachers, and students**, by **one continuous hands-on project — downloading a finished, fact-checked writing guide and remaking it into a copywriting book, behind gates, with every step leaving a trail** — filling the gap left by pandoc manuals (conversion without system), prompt-engineering books (prompting without product), and self-publishing guides (platforms without method). It succeeds if the reader can **take a book from Blueprint to signed gates to exports on Kindle, Canvas, and Medhavy — and then do it again with their own book from scratch.**

## Book Type and Deployment Specification

**Book type:** Course textbook (primary) with practitioner-handbook traits — chapters are sequential and gated like a course, but each Part I chapter is also re-enterable as a task reference.

**Primary adoption context:** self-paced individual use (an author with a CLI agent and a free weekend per Part); secondarily, a workshop or half-semester course module on AI-assisted authorship — 12 chapters ≈ 12 sessions.

**Secondary adoption context:** teams adopting the AI+1 system who need an onboarding text; instructors evaluating Medhavy/Canvas pipelines.

**Explicitly NOT designed for:** readers wanting prompt-engineering theory; developers extending the toolchain (that's `docs/`-level material); anyone seeking what Medhavy does (its own book, see book.md Out of Scope).

**How the TOC signals the type:** chapter titles are capability statements with one running project visible in the sequence; a faculty member can read the 12 titles as a syllabus.

**ASSESSMENT REQUIREMENTS** (per the Blueprint assessment rule):

| Assessment | Status | Notes |
|---|---|---|
| In-chapter exercises | **needed** — they ARE the book | every chapter; artifact + log entry per exercise |
| Chapter quizzes | desired | generated via `build-quizzes.py` — the book should eat its own dogfood |
| Flashcards/Anki | desired | key terms of the system (gate, sidecar, spine, Blueprint…) via `build-anki.py` |
| Canvas modules | **needed** | the book ships as an `.imscc` built by its own Chapter 5 process |
| Worked solutions | desired | per-exercise "what good looks like" — one exemplar per chapter |
| Exam bank | out of scope | self-paced primary context doesn't need it; revisit if course adoption materializes |

## Learner Profile

**Primary reader:** a person who writes — teacher, subject expert, working writer — comfortable with email and chatting with an AI, nothing more. They have a book in them (or a course that needs one) and no path that doesn't involve either learning a toolchain or paying someone.

**Prior knowledge (reliable):** using a chat AI; basic file/folder concepts; what a Kindle book and an LMS are.

**Prior misconceptions:** that AI writes finished books (it drafts; judgment ships them); that "the AI said so" is verification; that more generation is progress.

**Capability gap this book closes:** from "I can chat with an AI" to "I can operate a gated book-production system and sign my name to its outputs."

**Motivation type:** professional/project-driven — they want the artifact. Chapter openings therefore lead with the artifact, not the concept.

## Prerequisite Map

| Prerequisite | Safe to assume? | Treatment |
|---|---|---|
| Chatting with an AI agent | Yes | — |
| Installing a CLI agent (Cowork/Claude Code/Codex) | Probably | Introduction includes a "get set up" box; agent does the rest |
| git clone (one command) | Probably | Chapter 1 gives the exact line; agent can run it |
| Kindle Previewer / device access | No | Chapter 2 offers Previewer path + "no device" fallback — [NEEDS HUMAN INPUT: preferred fallback — web EPUB reader?] |
| Canvas access | No | Chapter 5 uses free Canvas teacher account — confirm this remains viable |
| Markdown literacy | Probably | taught by exposure in Chapter 2; never lectured |

Fewer than 3 hard "No" ratings after treatments → no foundations chapter needed; front-load via the Introduction's setup box.

## Central Argument

This book argues that **AI made book-production cheap but left judgment scarce, so the way to make a real book with AI is a gated system where the human signs every decision that matters** — which means that **anyone who writes can now produce a publishable, fact-checked, multi-format book without becoming technical**, and this matters because **the alternative is the flood: fluent, unchecked, unowned AI books that no one stands behind.**

## Field Positioning

| Existing category | What it does | What this book does instead |
|---|---|---|
| Pandoc/static-site documentation | converts formats | builds *books* — planning, gates, facts, judgment; conversion is one exercise |
| Prompt-engineering guides | better asking | a *system* in which prompts are recipes with gates and logs; the prompt is never the product |
| Self-publishing guides (KDP etc.) | platform mechanics | platform-agnostic production; Kindle/Canvas/Medhavy are exports, not the method |

**Positioning statement:** Unlike prompt guides, which teach you to ask better, this book teaches you to *ship* — for readers who need a finished, checked book they can sign their name to.

[NEEDS HUMAN INPUT — named comparable titles: the table argues by category; the publisher proposal will need 3 specific competing titles with authors/years.]
