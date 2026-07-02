<!--
    architecture.md
    Blueprint Phase 2: Learning Architecture.
-->

# AI1 CLI — Learning Architecture

**Author:** Nik Bear Brown

*Phase 2 output from Blueprint. Drafted from book.md + outline.md (approved direction, 2026-06-12). Sidecar unverified until human sign-off.*

---

## Learning Outcomes (per chapter, Bloom's level labeled)

**Intro** — (Understand) Explain AI+1's labor split — agent executes, human signs — and name the three ways into the system.

**Ch 1 — Inventory, Research, Blueprint, Sign-Off**
1. (Analyze) Inventory an existing 24-chapter book: what each chapter teaches, for whom.
2. (Create) Generate and run a research prompt on restructuring writing→copywriting and on whether classic direct-advertising principles survive an AI world; save findings to `pantry/`.
3. (Evaluate) Review a Blueprint built from that evidence and sign — or refuse to sign — GATE 0, logging the decision.

**Ch 2 — Rebuild the Book You Just Replanned**
1. (Apply) Rebuild a real book end-to-end (`./build.sh`) and locate an edit in the EPUB.
2. (Apply) Re-identify the book (title, author, cover) and produce a Kindle-ready file.
3. (Understand) Explain what governance adoption (sync) added and why downstream copies are read-only.

**Ch 3 — Rewrite a Chapter in Another Voice**
1. (Apply) Produce a voice rewrite without touching the original.
2. (Evaluate) Judge, with cited passages, which voice serves the Blueprint's named reader.

**Ch 4 — Generate the Assessments the Blueprint Promised**
1. (Apply) Generate quizzes, exercises, and an Anki deck from chapters.
2. (Analyze) Find and document at least one generated question that fails its outcome — and say why.

**Ch 5 — Export to Canvas**
1. (Apply) Build and import an `.imscc`; verify module order against the signed plan.

**Ch 6 — Facts**
1. (Apply) Trace a claim to the fact dictionary; add a sourced fact with `verified: false`.
2. (Evaluate) Sign one fact as a human, and state what the signature does and doesn't warrant.

**Ch 7 — Cut to the Blueprint**
1. (Evaluate) Execute deletions against the signed plan, logging each exclusion with reason and owner.

**Ch 8 — Convert What Survives**
1. (Create) Transform surviving chapters to copywriting genres (profile→case study, proposal→pitch, analysis→ad teardown) with the agent.
2. (Evaluate) Perform the human rewrite and sign GATE 3 — articulating what made the draft not-yet-theirs.

**Ch 9 — Add What's Missing**
1. (Create) Draft net-new chapters the plan calls for (headlines/hooks/CTAs, landing pages, email, brand voice) from research, not model memory.
2. (Apply) Produce figures that pass the visual audit.

**Ch 10 — The Manuscript Meets the Blueprint**
1. (Evaluate) Run Editorial Review + adoption-failure critique; reconcile manuscript and plan explicitly with a changelog.

**Ch 11 — Fact-Check Old and New**
1. (Analyze) Distinguish inherited claims from new ones; source or cut every checkable claim.

**Ch 12 — Ship Everywhere**
1. (Apply) Produce final EPUB/Kindle, Canvas `.imscc`, Medhavy `.mdx`, and regenerated assessments.
2. (Evaluate) Walk the provenance chain of the finished book and defend one gate decision in it.

**Ch 13 — From Book to Video** *(capstone; extension)*
1. (Apply) Turn one finished, signed chapter into a previewed narrated lecture spine with Unreal Reels (pool → sign the plan → narrate/preview).
2. (Evaluate) Run the fidelity pass against the source chapter, resolve every flag, and sign the lecture — stating what the signature warrants (faithful to a verified source, not true from scratch).

## Outcome Map

| Ch | Highest Bloom's | Assessable? | Maps to course need? |
|---|---|---|---|
| 1 | Evaluate | Y (signed/refused gate + logged reason) | planning & judgment |
| 2 | Apply | Y (EPUB artifact) | toolchain operation |
| 3 | Evaluate | Y (judgment memo w/ citations) | AI-output judgment |
| 4 | Analyze | Y (flawed-question find) | assessment literacy |
| 5 | Apply | Y (imported course) | LMS delivery |
| 6 | Evaluate | Y (signed fact) | verification habit |
| 7 | Evaluate | Y (exclusion log) | scope judgment |
| 8 | Evaluate | Y (GATE 3 signature) | authorship |
| 9 | Create | Y (new chapters + clean audit) | authoring in-system |
| 10 | Evaluate | Y (reconciliation changelog) | delivery vs. promise |
| 11 | Analyze | Y (fact-check report) | accuracy |
| 12 | Evaluate | Y (provenance walk) | integration |
| 13 | Evaluate | Y (signed lecture + clean fidelity report) | extend the book into video |

No comprehension-only chapters; every chapter has Apply or above. ✔

## Sequencing Model and Justification

**Primary model: Problem → Solution, executed as whole-task-first (Merrill).** The learner profile is project-driven non-technical readers: they stay when each session ends in an artifact and leave during theory. So the plan (the problem "what book should this be?") comes first as a *task*, not a lecture; every subsequent chapter is a solution to a need the project has already created. Spiral elements: gates recur (GATE 0 in Ch 1, GATE 3 in Ch 8, gate-vs-manuscript in Ch 10), each return escalating from *signing a plan* → *signing prose as yours* → *holding a build accountable to a signature*.

**Where the model most likely breaks:** Chapter 1 — a planning chapter as the opener risks "when do I get to build?" Mitigation: the chapter is built as actions (inventory, research, sign) with the explicit promise that Chapter 2 builds in the first ten minutes; and Chapter 1's research step gives the first artifact (the pantry file) within the first session.

**Transition chapter:** Ch 7 — the pivot from operating (I) to authoring (II). The student must cross knowing: how to run builds, what the signed plan says, and how to log a decision.

## Three-Act Learning Arc

**Act One — Establish (Intro–Ch 6):** the inciting question — *what should this book become, and how do I run the factory that makes it?* By the end the reader has a signed plan and full command of the operating surface (build, voice, assessments, Canvas, facts).

**Act Two — Build (Ch 7–9):** the hard middle — judgment under load. Cutting, converting, authoring; GATE 3 is the act's emotional center: the moment the book becomes theirs.

**Act Three — Apply (Ch 10–12):** integration — the manuscript is held against the plan, the claims against sources, and the book ships everywhere. The reader produces the thing the book promised on page one.

**Arc statement:** This book takes the reader from *chatting with an AI* to *shipping a checked, multi-format book they signed*, by first making them sign a plan built from evidence, then making them remake a real book against that plan, then making them prove the result honest and ship it.

**Transition tests:** I→II — can the reader run any build and cite the signed plan? II→III — does a converted manuscript exist with GATE 3 signed?

## Prerequisite Dependency Map

| Ch | Depends on |
|---|---|
| 1 | Intro setup |
| 2 | 1 (the plan exists; identity changes follow it) |
| 3–6 | 2 (a building book) |
| 7 | 1 (the plan), 6 (logging habit) |
| 8 | 7 (the keepers list) |
| 9 | 8 (manuscript voice learned) + 1 (plan's gap list) |
| 10 | 9 + 1 (manuscript vs. signed plan) |
| 11 | 10 (stable manuscript) |
| 12 | 11 (checked manuscript) |

No chapter depends on a later one. ✔ Load-bearing: Ch 1 (everything cites the plan) and Ch 2 (everything runs builds) — flag both for extra polish.

## Front-Loading Decisions

CLI-agent setup → Introduction setup box (not a chapter). Markdown → taught by exposure in Ch 2. Kindle/Canvas access fallbacks → resolved inside Ch 2/Ch 5 exercises, not front-loaded. No Chapter 0 needed.

## Assessment Plan

From vision.md's assessment requirements: **needed** — in-chapter exercises (every chapter; artifact + RUN/STATUS log line is the submission) and Canvas modules (the book ships as its own `.imscc`); **desired** — chapter quizzes and key-term Anki deck (both generated by the repo's own tools as the Ch 4 exercise, then regenerated at Ch 12), worked solutions (one exemplar per chapter, in an appendix); **out of scope** — exam bank. Chapters 4 and 12 are where the assessment plan is *exercised*; every chapter is where it is *fulfilled*.
