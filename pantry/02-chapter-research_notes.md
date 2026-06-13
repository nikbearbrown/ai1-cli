# Research Notes: Chapter 02 — Chapter Research

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `02-chapter-research_notes.md`
**Corresponding chapter:** `chapters/02-chapter-research.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Research every signed-Blueprint chapter before drafting any chapter. Produce one notes file per chapter, scan the shared markdown library, copy relevant `_lib_` material into pantry, and triage flags before prose begins.

---

## A. Conceptual foundations

### Notes are pre-prose
The research note is a contract, not a miniature chapter. It gathers concepts, examples, dependencies, field status, teaching considerations, sources, and flags. Its success is measured by whether an author can draft from it while still seeing what must be verified.

**Common misconception:** Students write polished paragraphs and bury uncertainty.

**Worked example:** Rewrite a paragraph-like note into bullets tagged source, case, misconception, and flag.

**Source(s):** Local: conductor/10-research/research.md; Local: chapters/83-appendix-research-pass.md
### Library before web
Owned material is searched before external research because it may already contain voice, figures, examples, and reusable explanations. Copying with `_lib_` preserves provenance and makes the pantry auditable.

**Common misconception:** Students either ignore owned material or paste it without provenance.

**Worked example:** Scan ten library filenames and classify each as relevant, possibly relevant, or unrelated.

**Source(s):** Local: MD library; Local: pantry/README.md
### Flagging is success
A good research pass exposes weak places. New chapters should have more flags than converted chapters because they lack a source-chapter safety net. An empty flag list is suspicious unless the chapter is narrow and heavily sourced.

**Common misconception:** Learners think flags mean the research failed.

**Worked example:** Compare a converted chapter note and a new chapter note; explain why the new one should carry more risk.

**Source(s):** Local: books/writing-guide/pantry/08-awareness-frameworks_notes.md

---

## B. Domain examples and cases

### Bear's Copywriting Book run
The writing-guide pantry contains 16 research notes and 12 `_lib_` files, with flags concentrated in new chapters.

### Regulatory chapter
AI governance notes are useful only if NIST/FTC/Copyright/W3C links survive into the draft.

### Failure case: fabricated certainty
If every claim has a neat citation after a limited-access run, the research probably invented or over-smoothed sources.

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
- source tracking is essential for factual authoring.

**Contested or emerging:**
- whether LLM-generated research notes can be trusted without independent verification.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Local chapters/02-chapter-research.md — current chapter text.
2. NIST AI RMF — provenance/governance context, https://www.nist.gov/itl/ai-risk-management-framework
3. OpenAI Codex docs — repository-based agent workflow, https://developers.openai.com/codex/

**Recent developments (last 3 years):**
- institutions are moving toward AI provenance and disclosure policies, increasing the value of saved prompts and notes.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck distinguishing research from drafting; enforce a no-polished-prose rule.
- Use a claims-file analogy: notes are the drawer of evidence before the essay.
- Exercise: audit a notes file and find the three claims that should block drafting.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_ai-prompt-engineering-textbook.md`
- `_lib_ai-nbb-prompt-architecture-the-power-of-the-template-pattern.md`
- `_lib_ai-gigo.md`

---

## G. Gaps and flags

- The current sidecar for this chapter is still `verified: false`; sign only after source review.
