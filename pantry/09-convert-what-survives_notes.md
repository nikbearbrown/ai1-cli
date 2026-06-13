# Research Notes: Chapter 09 — Convert What Survives

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `09-convert-what-survives_notes.md`
**Corresponding chapter:** `chapters/09-convert-what-survives.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Transform retained source chapters into copywriting equivalents, then require human rewrite and GATE 3 ownership.

---

## A. Conceptual foundations

### Transformation mapping
Conversion is not summarization. Each source chapter gets mapped to its new rhetorical job: profile becomes case study, proposal becomes pitch, evaluation becomes product review, rhetorical analysis becomes ad teardown.

**Common misconception:** Students paraphrase the old chapter and call it converted.

**Worked example:** Write a source-to-target mapping for one chapter before generating any draft.

**Source(s):** Local: outline.md; Local: pantry/old-chapters/07-chapter-writing.md
### Preserve useful structure, change domain
A source chapter's pedagogical machinery may be valuable even when its examples change. The agent should preserve transferable scaffolds while replacing irrelevant domain content.

**Common misconception:** Students either copy too much or throw away everything.

**Worked example:** Highlight structure in one source chapter and replace only examples and assignments.

**Source(s):** Local: conductor/20-draft/draft.md
### Human rewrite gate
The generated conversion is not author-owned until the human rewrites, judges, and signs. GATE 3 protects the book from becoming an unexamined machine paraphrase.

**Common misconception:** Students mistake editing for accepting tracked changes.

**Worked example:** Record three substantive human choices made after generation.

**Source(s):** Local: conductor/30-human-rewrite/rewrite.md

---

## B. Domain examples and cases

### Proposal to sales page
A proposal's problem/solution logic transfers well into commercial offer structure.

### Evaluation to product review
Criteria-evidence-judgment becomes proof, comparison, and recommendation.

### Failure case: academic residue
A converted chapter keeps school-assignment language that no longer serves a copywriting reader.

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
- domain transfer requires preserving learning structure while changing examples and outcomes.

**Contested or emerging:**
- how much old prose can survive before the book feels patched rather than reauthored.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Local conductor/20-draft/draft.md.
2. Local conductor/30-human-rewrite/rewrite.md.
3. OpenAI Codex docs — repository editing context, https://developers.openai.com/codex/

**Recent developments (last 3 years):**
- AI makes bulk conversion easy, so the scarce skill is human taste and ownership.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck because they cannot distinguish structure from subject matter.
- Use the analogy of changing a building's tenant without demolishing the load-bearing walls.
- Exercise: convert an assignment prompt into a commercial deliverable prompt.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_ai-claude-code-the-definitive-guide-to-agentic-development.md`
- `_lib_ai-co-intelligence-living-and-working-with-ai.md`

---

## G. Gaps and flags

- Need concrete source-to-target mapping table from the signed Blueprint before drafting examples.
