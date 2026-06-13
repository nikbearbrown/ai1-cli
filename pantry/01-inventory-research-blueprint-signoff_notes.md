# Research Notes: Chapter 01 — Inventory, Research, Blueprint, Sign-Off

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `01-inventory-research-blueprint-signoff_notes.md`
**Corresponding chapter:** `chapters/01-inventory-research-blueprint-signoff.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Everything starts with the Blueprint, and the Blueprint starts with evidence: clone a finished book, inventory it, generate and run research, save the results to pantry, produce vision/architecture/chapter spec/risks, and log GATE 0 sign-off before touching the manuscript.

---

## A. Conceptual foundations

### Inventory before intervention
The chapter's first skill is descriptive discipline: list what exists before asking what it should become. In a conversion project, the inventory prevents the agent from optimizing a fantasy book. The inventory should capture chapter title, purpose, approximate length, assessment affordances, figures, source status, and obvious keep/cut/merge signals.

**Common misconception:** Students jump straight to a better TOC and lose evidence about the old manuscript.

**Worked example:** Inventory three chapters and write one neutral sentence about each before recommending any change.

**Source(s):** Local: conductor/00-blueprint/blueprint.md; Local: pantry/old-chapters/05-book-scaffold.md
### Research as a gate
A research pass is not decorative; it decides whether the plan is allowed to become a draft. Research prompts should be stored with outputs, so the plan can be audited later. The important habit is provenance: what came from the source book, what came from research, what is model knowledge, and what remains a flag.

**Common misconception:** A fluent plan is mistaken for an evidenced plan.

**Worked example:** Mark every claim in a one-page plan as source, research, model knowledge, or open flag.

**Source(s):** Local: conductor/10-research/research.md; OpenAI Codex docs: https://developers.openai.com/codex/
### Human sign-off
The book's constitutional move is that the human signs the plan. The agent may generate drafts and critiques, but the owner accepts the architecture. This creates accountability and makes later review possible: the manuscript is judged against what was signed, not against a moving preference.

**Common misconception:** Sign-off is treated as ceremony rather than a constraint on future work.

**Worked example:** Compare a later chapter to the signed spec and record whether the mismatch is a manuscript bug or a plan amendment.

**Source(s):** Local: CONDUCTOR.md; Local: STATUS.md

---

## B. Domain examples and cases

### Writing Guide to copywriting book
The running project uses a complete 24-chapter composition textbook as raw material, which makes the inventory concrete instead of simulated.

### Product requirements documents
Software teams use PRDs and design docs to separate decision-making from implementation; Blueprint plays the same role for a book.

### Failure case: silent drift
If the chapter count or audience changes without an amendment, later reviews cannot tell whether the draft is wrong or the plan changed.

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
- complex authoring workflows need explicit artifacts and review gates.

**Contested or emerging:**
- how much autonomy a writing agent should have before human review.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. OpenAI, Codex documentation — agentic coding/repository workflow context, https://developers.openai.com/codex/
2. Local AI1.md and CONDUCTOR.md — project constitution and phase gates.
3. Local conductor/00-blueprint/blueprint.md — Blueprint prompt and expected artifacts.

**Recent developments (last 3 years):**
- coding agents and writing agents increasingly operate on repositories, making file-based provenance more important than chat-based memory.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck because inventory feels slower than invention; require a two-column before/after table.
- Use the analogy of measuring a room before renovating it.
- Exercise: create a GATE 0 packet and have a peer reject one unsupported claim.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_education-tic-toc-v2.md`
- `_lib_ai-nbb-prompt-architecture-the-power-of-the-template-pattern.md`
- `_lib_ai-co-intelligence-living-and-working-with-ai.md`

---

## G. Gaps and flags

- Verify exact commands used to clone or obtain the Writing Guide in the final chapter draft.
