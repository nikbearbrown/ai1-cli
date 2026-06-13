# Research Notes: Chapter 12 — Fact-Check Old and New

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `12-fact-check-old-and-new_notes.md`
**Corresponding chapter:** `chapters/12-fact-check-old-and-new.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Research notes and fact-check both inherited and new claims so every claim is sourced or cut.

---

## A. Conceptual foundations

### Inherited claims are not automatically safe
A source chapter may have been fact-checked for its original purpose, but conversion changes context. Claims need to be re-evaluated when they are moved, reframed, or used to support a new argument.

**Common misconception:** Students assume old text is safe because it came from a finished book.

**Worked example:** Pick one inherited claim and check whether the new chapter uses it for the same purpose.

**Source(s):** Local: conductor/40-factcheck/factcheck.md
### New claims need stronger sourcing
New chapters and AI-era updates often involve fast-moving policy, platform, or regulatory material. Primary sources should be preferred for law, standards, and official guidance.

**Common misconception:** Students cite blog summaries for regulator claims.

**Worked example:** Replace one secondary source with a primary regulator or standards page.

**Source(s):** NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework; FTC: https://www.ftc.gov/business-guidance
### Cutting is a fact-check outcome
The fact-checker is not required to save every claim. Unsupported, unnecessary, or overbroad claims should be narrowed or removed.

**Common misconception:** Students treat every failed check as a search problem.

**Worked example:** Cut one unsupported claim and explain why the chapter improves.

**Source(s):** Local: conductor/40-factcheck/factcheck.md

---

## B. Domain examples and cases

### FTC reviews rule
Claims about endorsements/reviews require exact FTC rule or guidance.

### AI governance
NIST, Copyright Office, W3C, and Google policy links must be restored before governance prose is drafted.

### Failure case: adjacent source
A source about AI generally may not support a specific claim about classroom or publishing practice.

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
- primary sources are preferred for legal, medical, regulatory, and standards claims.

**Contested or emerging:**
- whether common marketing frameworks require primary historical attribution or can be taught as practitioner heuristics.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. FTC consumer reviews/testimonials rule resources — https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers
2. U.S. Copyright Office AI resources — https://www.copyright.gov/ai/
3. W3C WCAG 2.2 — https://www.w3.org/TR/WCAG22/

**Recent developments (last 3 years):**
- AI policy, copyright, disclosure, and review rules have changed quickly since 2023.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck because fact-checking seems punitive; frame it as strengthening claims.
- Use the analogy of tightening bolts before a bridge opens.
- Exercise: classify ten claims as sourced, source-needed, too broad, or cut.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_ai-gigo.md`
- `_lib_business-data-ism-the-revolution-transforming-decision-making-consumer-behavior-and-al.md`

---

## G. Gaps and flags

- Require live link verification for all regulator/standards URLs before manuscript sign-off.
