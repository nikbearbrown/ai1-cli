# Research Notes: Chapter 08 — Cut to the Blueprint

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `08-cut-to-the-blueprint_notes.md`
**Corresponding chapter:** `chapters/08-cut-to-the-blueprint.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Use the signed plan to prune inherited chapters, log every exclusion with reason and owner, and avoid paying to convert material the plan has already killed.

---

## A. Conceptual foundations

### Cutting is authorship
Pruning is not merely deletion; it is the act of making the new book coherent. Every kept chapter consumes reader attention, build space, assessment effort, and verification cost.

**Common misconception:** Students feel guilty cutting usable prose.

**Worked example:** Classify each source chapter as keep, cut, merge, or appendix with one reason.

**Source(s):** Local: conductor/editor/editor.md
### Logged exclusions
A cut should leave a trace: what was removed, why, who approved it, and whether anything was moved to pantry. This prevents future agents from reintroducing rejected material.

**Common misconception:** Students delete silently and lose rationale.

**Worked example:** Write three exclusion log entries and one merge entry.

**Source(s):** Local: pantry/changes.md
### Evidence-based organization
The signed Blueprint and editorial review should drive cuts, not current mood. If a cut contradicts the plan, amend the plan first.

**Common misconception:** Students use the Blueprint only when convenient.

**Worked example:** Compare proposed cuts to the Chapter 1 plan and mark conflicts.

**Source(s):** Local: outline.md; Local: conductor/editor/editor.md

---

## B. Domain examples and cases

### Composition to copywriting
Some writing-guide chapters transfer cleanly, some merge, and some distract from the new audience.

### Thin/long chapter audit
Uneven chapter length can signal consolidation or splitting needs.

### Failure case: zombie chapter
Unlogged cuts reappear when a later agent scans old files and assumes they are still active.

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
- coherent textbooks need deliberate scope control.

**Contested or emerging:**
- whether useful-but-off-scope material belongs in appendices, pantry, or a separate book.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Local conductor/editor/editor.md — editorial review and organization audit.
2. Local pantry/changes.md — change log seed.
3. Local outline.md — signed plan source.

**Recent developments (last 3 years):**
- repository-based authoring makes deletion recoverable, so rationale matters more than preservation anxiety.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck by valuing effort already spent; use the sunk-cost framing.
- Use the analogy of editing a film: good scenes can be cut from the wrong movie.
- Exercise: defend one painful cut to a peer using only the Blueprint.

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

- Need the actual converted-book Blueprint packet to name concrete source chapters in final prose.
