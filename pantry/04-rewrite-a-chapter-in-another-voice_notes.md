# Research Notes: Chapter 04 — Rewrite a Chapter in Another Voice

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `04-rewrite-a-chapter-in-another-voice_notes.md`
**Corresponding chapter:** `chapters/04-rewrite-a-chapter-in-another-voice.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Run a voice rewrite, diff it against the original, judge which version serves the copywriting reader, and preserve originals.

---

## A. Conceptual foundations

### Voice is a design constraint
A voice file is not a vibe prompt; it is an operational specification for diction, pacing, examples, stance, and reader relationship. Rewriting in voice tests whether style serves the signed audience.

**Common misconception:** Students equate voice with decorative adjectives.

**Worked example:** Rewrite one paragraph in Socratic and pragmatic voices, then name what each helps or harms.

**Source(s):** Local: voices/*/VOICE.md
### Diff as judgment surface
The diff turns rewriting from taste into evidence. Students can see additions, deletions, softened claims, lost examples, and tone changes. The human judges the diff, not the agent's confidence.

**Common misconception:** Students read only the rewritten version and forget what changed.

**Worked example:** Mark three diff hunks as better, worse, or neutral for the target reader.

**Source(s):** Git documentation: https://git-scm.com/docs/git-diff
### Preserve source integrity
Original chapters are evidence. Rewrites should happen in a new file, branch, or staged artifact so the source remains available for comparison and rollback.

**Common misconception:** Students overwrite the original and cannot audit the transformation.

**Worked example:** Create a voice rewrite file and show a clean diff against the source.

**Source(s):** Local: conductor/30-human-rewrite/rewrite.md

---

## B. Domain examples and cases

### Socratic vs pragmatic rewrite
A Socratic version may increase reflection while a pragmatic version may better serve a procedural chapter.

### Brand voice adaptation
The same factual content can be made formal, warm, sardonic, or wonder-driven without changing claims.

### Failure case: style erases claims
A lively rewrite may drop caveats or sources; the diff reveals the loss.

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
- style transfer requires human evaluation for audience fit.

**Contested or emerging:**
- whether voice libraries should be stable templates or chapter-specific adaptive prompts.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Local conductor/30-human-rewrite/rewrite.md — rewrite gate.
2. Mollick, Co-Intelligence — human/AI collaboration framing in copied library file.
3. Git diff documentation — https://git-scm.com/docs/git-diff

**Recent developments (last 3 years):**
- LLMs make large-scale style rewriting cheap, raising the risk of unreviewed homogenization.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck because they argue taste; make them cite the signed audience.
- Use the analogy of trying on eyeglasses: each lens reveals and distorts.
- Exercise: score a rewrite on clarity, fidelity, audience fit, and source preservation.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_ai-co-intelligence-living-and-working-with-ai.md`
- `_lib_ai-claude-cowork-capabilities.md`

---

## G. Gaps and flags

- Decide whether final chapter uses existing `voices/` only or asks reader to author a new voice.
