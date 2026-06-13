# Research Notes: Chapter 10 — Add What's Missing

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `10-add-whats-missing_notes.md`
**Corresponding chapter:** `chapters/10-add-whats-missing.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Draft the chapters the Blueprint requires but the source book never had, seeded by existing pantry material and checked figures.

---

## A. Conceptual foundations

### Gap chapters carry higher risk
New chapters lack source-chapter provenance, so they need stronger notes, more explicit flags, and stricter fact-checking. The absence of inherited material is the main risk.

**Common misconception:** Students treat a new chapter as freer and therefore less in need of evidence.

**Worked example:** Compare flags in a converted chapter note and a new chapter note.

**Source(s):** Local: chapters/02-chapter-research.md
### Seed material is not a chapter
Pantry material like `ogilvy-ideas.md` can seed concepts, examples, and exercises, but it must be organized, sourced, and adapted to the signed audience.

**Common misconception:** Students paste seed material wholesale.

**Worked example:** Turn three seed bullets into a chapter section outline with sources and flags.

**Source(s):** Local: pantry/ogilvy-ideas.md
### Figures as checked artifacts
New material often needs new diagrams. A figure should have a purpose, source/claim discipline, alt text, and visual audit before it enters the manuscript.

**Common misconception:** Students create decorative figures that do not teach.

**Worked example:** Draft a figure spec and audit it against the chapter objective.

**Source(s):** Local: conductor/50-images/images.md; W3C WCAG: https://www.w3.org/TR/WCAG22/

---

## B. Domain examples and cases

### Headlines/hooks/CTAs
A composition textbook may teach rhetoric but not commercial response mechanisms; these are true gap chapters.

### Brand voice
Voice work can reuse writing pedagogy but needs modern AI workflow and guardrail material.

### Failure case: unsupported marketing folklore
New copywriting chapters can drift into practitioner clichés unless sources and examples are verified.

---

## C. Connections and dependencies

**Prerequisites (what reader must already know):**
- The signed Blueprint and chapter outline — this is the source of truth for the exercise.
- Basic repository navigation — the learner must be able to find `chapters/`, `pantry/`, build scripts, and sidecars.
- The AI1 gate idea — agent output becomes book material only after explicit human review.

**Unlocks (what this chapter makes possible):**
- Later chapters can operate on artifacts produced here rather than on chat memory.
- Verification can compare source, plan, draft, and output because each step leaves a file trail.
- The running Writing Guide conversion can proceed without losing provenance.

**Adjacent chapter connections:**
- Previous chapter: reinforces the prior artifact and gate.
- Next chapter: consumes the artifact produced here and makes the next operation possible.

---

## D. Current state of the field

**Settled:**
- new chapters require source gathering before drafting.

**Contested or emerging:**
- which classic advertising principles survive unchanged in AI-mediated feeds and search.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. FTC AI claims guidance — https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check
2. W3C WCAG 2.2 — accessibility requirements for figures/pages, https://www.w3.org/TR/WCAG22/
3. Local pantry/ogilvy-ideas.md and copied design figure library files.

**Recent developments (last 3 years):**
- generative AI has changed volume and sameness of copy, increasing the value of differentiation, voice, provenance, and human judgment.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck by drafting from memory; force notes-first.
- Use the analogy of adding a new wing to a building: it needs foundations, not just matching paint.
- Exercise: write a missing-chapter risk register before drafting.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_design-figure-architect.md`
- `_lib_design-figure-architect-prompt.md`
- `_lib_ai-prompt-engineering-textbook.md`

---

## G. Gaps and flags

- Verify all named advertising frameworks against primary or reputable secondary sources before final prose.
