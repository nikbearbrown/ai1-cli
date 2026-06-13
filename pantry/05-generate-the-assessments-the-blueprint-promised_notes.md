# Research Notes: Chapter 05 — Generate the Assessments the Blueprint Promised

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `05-generate-the-assessments-the-blueprint-promised_notes.md`
**Corresponding chapter:** `chapters/05-generate-the-assessments-the-blueprint-promised.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Use the Chapter 1 assessment plan to generate quizzes, exercises, and Anki cards, then audit what question generation got wrong.

---

## A. Conceptual foundations

### Assessment follows objectives
Questions should test the capabilities promised in the Blueprint, not merely recall chapter vocabulary. The assessment plan is the shopping list, and generation is fulfillment.

**Common misconception:** Students generate generic quizzes because they ignore learning outcomes.

**Worked example:** Turn one chapter capability into one recall question, one application task, and one critique task.

**Source(s):** Local: build-quizzes.py; Local: build-exercises.py
### Item quality audit
Generated items often fail by ambiguity, answer leakage, unsupported distractors, or testing facts the chapter never taught. The audit is part of the chapter, not an optional polish pass.

**Common misconception:** Students trust plausible multiple-choice questions.

**Worked example:** Identify the flaw in five generated questions and rewrite them.

**Source(s):** Local: conductor/editions/chapter-quizzes.md
### Spaced repetition as a separate layer
Anki cards are useful for durable recall, but they are not substitutes for exercises that build judgment. Good cards are atomic, answerable, and tied to source text.

**Common misconception:** Students put essay-sized answers on flashcards.

**Worked example:** Split one overloaded card into three atomic cards.

**Source(s):** Local: scripts/extract-cards.py; Local: conductor/editions/flashcards-anki.md

---

## B. Domain examples and cases

### Blueprint-to-quiz trace
A quiz item should point back to a chapter objective or it is curricular noise.

### Anki deck build
The APKG output is an inspectable artifact, not just a promise of study support.

### Failure case: unsupported distractor
A wrong answer that is only wrong by author intent teaches confusion.

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
- assessment should align with learning outcomes.

**Contested or emerging:**
- how much generated assessment content can be accepted without psychometric review.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Local build-quizzes.py, build-exercises.py, build-anki.py.
2. Local conductor/editions/* assessment prompts.
3. IMS Common Cartridge context for LMS packaging: https://www.imsglobal.org/cc/index.html

**Recent developments (last 3 years):**
- LLM-generated quizzes are common, but quality control remains the limiting factor.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck writing recall-only items; require Bloom-level labels.
- Use the analogy of a lock and key: the objective is the lock, the item is the key.
- Exercise: reject at least 30 percent of generated items and explain why.

**Analogies and framings that work:**
- Factory, trail, and gate metaphors work because the book treats each stage as a visible artifact rather than invisible intention.
- The running project should stay concrete: every exercise should end with a file, output, diff, sign-off, or logged decision.

**Exercises that build the target skill:**
- Produce the chapter artifact, inspect it, and write a one-line trail entry.
- Pair-review the artifact against the signed Blueprint.
- Mark one thing the agent did well and one thing the human must still own.

---

## F. Relevant library files

- `_lib_education-teaching-for-deeper-learning-tools-to-engage-students-in-meaning-making.md`
- `_lib_education-humanitarians-ai-course-template.md`

---

## G. Gaps and flags

- Verify whether generated quizzes should be included in EPUB, Canvas only, or both.
