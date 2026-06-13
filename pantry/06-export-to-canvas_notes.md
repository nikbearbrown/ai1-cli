# Research Notes: Chapter 06 — Export to Canvas

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `06-export-to-canvas_notes.md`
**Corresponding chapter:** `chapters/06-export-to-canvas.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Build an IMS Common Cartridge, import it into Canvas, and check module order against the signed Blueprint.

---

## A. Conceptual foundations

### IMSCC as portability artifact
An `.imscc` package is a course-transfer artifact based on Common Cartridge conventions. It is not just a zip file; it encodes resources and organization so an LMS can import modules.

**Common misconception:** Students expect a course export to behave like a folder copy.

**Worked example:** Build an IMSCC and list its manifest/resources before importing.

**Source(s):** IMS Common Cartridge: https://www.imsglobal.org/cc/index.html; Local: build-imscc-standard.py
### Canvas import is verification
The import step checks whether the course shell actually appears in the target LMS as intended. Module order, page titles, links, and assessments need human inspection.

**Common misconception:** Students stop at successful file creation.

**Worked example:** Import into a test shell and compare module order to outline.md.

**Source(s):** Canvas Community guide: https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-content-from-Common-Cartridge-into-Canvas/ta-p/913
### Blueprint alignment
A course shell should reflect the signed chapter and assessment plan. If Canvas order differs from the plan, the fix is either the export script or a logged plan amendment.

**Common misconception:** Students reorganize in Canvas silently and leave the repository stale.

**Worked example:** Create a module-order checklist and record pass/fail per module.

**Source(s):** Local: outline.md; Local: build-canvas.sh

---

## B. Domain examples and cases

### Common Cartridge import
Canvas can import Common Cartridge packages into a course shell, making IMSCC a useful delivery format.

### Module order smoke test
The simplest course QA is whether modules appear in the order the book promises.

### Failure case: broken internal links
Markdown links that work locally may fail once packaged into an LMS resource tree.

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
- LMS exports need target-platform inspection.

**Contested or emerging:**
- how much LMS-specific customization belongs in a generic book repo.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. 1EdTech IMS Common Cartridge — https://www.imsglobal.org/cc/index.html
2. Canvas import guide — https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-import-content-from-Common-Cartridge-into-Canvas/ta-p/913
3. Local build-canvas.sh and build-imscc-standard.py.

**Recent developments (last 3 years):**
- course packages increasingly include interactive and AI-supported resources, making manifest discipline more important.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck treating LMS export as magic; make them inspect the manifest.
- Use the analogy of packing a moving box with labels.
- Exercise: import, screenshot/list module order, and file one issue.

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
- `_lib_education-tic-toc-v2.md`

---

## G. Gaps and flags

- Confirm current Canvas UI wording before screenshots or step-by-step instructions.
