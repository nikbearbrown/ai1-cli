# Research Notes: Chapter 11 — The Manuscript Meets the Blueprint

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `11-the-manuscript-meets-the-blueprint_notes.md`
**Corresponding chapter:** `chapters/11-the-manuscript-meets-the-blueprint.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Run editorial review and adoption-failure critique against the converted book, compare manuscript to signed plan, and revise either manuscript or plan explicitly.

---

## A. Conceptual foundations

### Delivery versus promise
This chapter asks whether the manuscript built what the Blueprint promised. The key move is comparison, not taste: audience, structure, assessments, risk mitigations, and chapter purposes are checked against the signed plan.

**Common misconception:** Students review the manuscript as if no plan exists.

**Worked example:** Create a two-column plan/delivery audit for three chapters.

**Source(s):** Local: conductor/editor/editor.md; Local: outline.md
### Adoption-failure critique
A book can be correct and still fail adoption because readers cannot enter it, teachers cannot assign it, chapters are uneven, or workflows are too brittle. The critique asks how the book will fail in real use.

**Common misconception:** Students focus on sentence polish while ignoring adoption risks.

**Worked example:** Name three reasons a target instructor would not use the book.

**Source(s):** Local: conductor/00-blueprint/blueprint-library.md
### Logged amendment
If the plan was wrong, amend it. If the manuscript missed, revise it. Silent drift destroys the value of gates.

**Common misconception:** Students hide plan changes inside prose edits.

**Worked example:** Write one amendment with date, reason, owner, and affected chapters.

**Source(s):** Local: outline.md amendment example

---

## B. Domain examples and cases

### Chapter 2 insertion
The existing outline amendment is a model of explicit plan change.

### Cancer textbook organization audit
Earlier audit logic showed how uneven chapters can signal a need to restructure into larger parts.

### Failure case: beautiful wrong book
A polished manuscript can fail because it no longer matches the promised audience or course use.

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
- editorial review should evaluate structure, pedagogy, consistency, and reader experience.

**Contested or emerging:**
- whether the plan or manuscript should win when evidence emerges mid-build.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Local conductor/editor/editor.md — textbook audit prompt.
2. Local conductor/00-blueprint/blueprint.md and blueprint-library.md.
3. Local outline.md — amendment practice.

**Recent developments (last 3 years):**
- agent-built manuscripts can drift quickly, increasing the need for formal comparison gates.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck because critique feels personal; route every finding to the plan.
- Use a contract delivery analogy.
- Exercise: choose one mismatch and decide: revise text, amend plan, or cut.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_business-flawless-consulting-4th-edition.md`

---

## G. Gaps and flags

- Need `/g2` adoption-failure critique source/prompt name verified before final chapter names it.
