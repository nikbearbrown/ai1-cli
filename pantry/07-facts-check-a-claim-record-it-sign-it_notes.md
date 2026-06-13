# Research Notes: Chapter 07 — Facts: Check a Claim, Record It, Sign It

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `07-facts-check-a-claim-record-it-sign-it_notes.md`
**Corresponding chapter:** `chapters/07-facts-check-a-claim-record-it-sign-it.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Trace one claim to the fact dictionary, add a sourced fact with `verified: false`, and have the human sign one verified claim.

---

## A. Conceptual foundations

### Fact dictionary as memory
A fact store makes claims reusable and inspectable. Instead of re-checking or re-inventing a claim in every chapter, the project records text, source, status, and signer.

**Common misconception:** Students cite sources in prose only and lose structured verification.

**Worked example:** Add one fact with source URL and status false, then reference it in a draft note.

**Source(s):** Local: facts/facts.json; Local: facts/facts_store.py
### Verified is a human status
The system may collect evidence, but verification belongs to an accountable human or defined review rule. The status should mean something operationally: unsigned facts cannot be treated as settled.

**Common misconception:** Students mark a fact verified because the URL exists.

**Worked example:** Compare source text to claim text and decide whether the claim is narrower, broader, or exact.

**Source(s):** Local: conductor/VERIFICATION.md
### Claim granularity
Facts should be small enough to verify. A paragraph with three empirical claims is three facts, not one. Good granularity makes errors cheaper to fix.

**Common misconception:** Students store broad summaries that cannot be checked precisely.

**Worked example:** Split a complex paragraph into atomic fact candidates.

**Source(s):** Local: facts/README.md

---

## B. Domain examples and cases

### Regulatory citation
A claim about FTC rules must record the exact FTC page or rule text, not a memory of enforcement.

### Definition fact
A standard definition can be sourced once and reused across chapters.

### Failure case: source mismatch
A URL can be real while failing to support the exact claim being made.

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
- claim-level provenance improves auditability.

**Contested or emerging:**
- when two independent secondary sources are enough versus requiring a primary source.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Local facts/FACTCHECKER-INTEGRATION.md.
2. FTC AI claims guidance — https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check
3. NIST AI RMF — https://www.nist.gov/itl/ai-risk-management-framework

**Recent developments (last 3 years):**
- AI-generated prose increases the need for explicit verification trails.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck because fact-checking feels like proofreading; teach it as claim/source alignment.
- Use a courtroom evidence analogy.
- Exercise: reject one source because it is adjacent but not supporting.

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

- Decide whether this chapter should require command-line use of facts.py or allow manual JSON editing.
