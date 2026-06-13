# Research Notes: Chapter 13 — Ship Everywhere

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `13-ship-everywhere_notes.md`
**Corresponding chapter:** `chapters/13-ship-everywhere.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Produce final EPUB/Kindle, Canvas IMSCC, Medhavy/MDX, and regenerated assessments against the final text.

---

## A. Conceptual foundations

### Final text is the assessment source
Assessments must be regenerated or checked against the final manuscript, not against drafts. Otherwise quizzes test content that moved, changed, or disappeared.

**Common misconception:** Students build study materials once and forget to refresh them.

**Worked example:** Change a chapter heading and trace whether related quiz/card references still work.

**Source(s):** Local: build-quizzes.py; Local: build-anki.py
### Multi-format shipping
EPUB, Canvas, and MDX have different affordances and failure modes. Shipping everywhere means validating each target format, not assuming one build proves all.

**Common misconception:** Students treat formats as interchangeable exports.

**Worked example:** Create a release checklist with one inspection per format.

**Source(s):** Pandoc: https://pandoc.org/MANUAL.html; IMS CC: https://www.imsglobal.org/cc/index.html
### Release trail
The final run should leave outputs, checks, sidecar states, and a changelog. A release without a trail cannot be audited or reproduced.

**Common misconception:** Students announce completion without recording what was built.

**Worked example:** Write a release note listing artifact names, build date, and verification status.

**Source(s):** Local: conductor/VERIFICATION.md; Local: STATUS.md

---

## B. Domain examples and cases

### EPUB plus Canvas
A book can render well in EPUB while importing poorly to LMS; both must be inspected.

### Medhavy pointer
The outline correctly treats Medhavy capabilities as a referenced separate book, not a hidden chapter.

### Failure case: stale quiz deck
An Anki deck generated before final edits may teach removed terminology.

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
- release workflows need target-specific QA.

**Contested or emerging:**
- how many formats a small authoring project should support before maintenance cost dominates.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Pandoc User's Guide — https://pandoc.org/MANUAL.html
2. 1EdTech Common Cartridge — https://www.imsglobal.org/cc/index.html
3. Local build.sh, build-site.sh, build-canvas.sh, build-react-site.py.

**Recent developments (last 3 years):**
- MDX/static-site publishing and LMS imports make books increasingly multi-surface products.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck calling the first successful build done; require format-specific evidence.
- Use the analogy of opening night on multiple stages.
- Exercise: complete a release checklist and mark one residual risk.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_education-humanitarians-ai-course-template.md`

---

## G. Gaps and flags

- Verify current Medhavy export expectations before writing detailed instructions.
