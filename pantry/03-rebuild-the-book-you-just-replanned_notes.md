# Research Notes: Chapter 03 — Rebuild the Book You Just Replanned

**Source:** `outline.md` amended chapter list; `TIKTOC.md` not present in `ai1-cli`
**Notes file:** `03-rebuild-the-book-you-just-replanned_notes.md`
**Corresponding chapter:** `chapters/03-rebuild-the-book-you-just-replanned.md`
**Generated:** 2026-06-12

---

## Chapter summary (from outline.md)

Change one sentence, run the build, inspect the EPUB, update metadata, preview for Kindle, and sync AI1 governance files into the adopted book.

---

## A. Conceptual foundations

### The pebble build
A tiny visible edit proves the whole factory works: source markdown, build script, metadata, output path, and reader preview. The point is not the sentence; it is confidence that changes travel from source to artifact.

**Common misconception:** Students treat build success as abstract and never open the output.

**Worked example:** Change a harmless sentence, build, and find that exact sentence in the output EPUB.

**Source(s):** Pandoc Manual: https://pandoc.org/MANUAL.html; Local: build.sh
### Metadata as publishing surface
Title, author, rights, language, and cover are not afterthoughts. They are part of the book's identity in EPUB readers, Kindle workflows, LMS imports, and archives.

**Common misconception:** Metadata is edited only in visible front matter, leaving machine metadata stale.

**Worked example:** Change metadata.yaml, build, and inspect the EPUB metadata.

**Source(s):** Pandoc Manual: https://pandoc.org/MANUAL.html
### Adoption under governance
A legacy book becomes an AI1 book when it gains AI1.md, CONDUCTOR.md, verification sidecars, and repeatable scripts. The sync step is a governance migration, not file decoration.

**Common misconception:** Students copy prompts but skip verification tooling.

**Worked example:** Run sync-to-book on a disposable copy and list the files added.

**Source(s):** Local: scripts/sync-to-book.sh; Local: conductor/VERIFICATION.md

---

## B. Domain examples and cases

### EPUB smoke test
A one-sentence edit is the publishing equivalent of a unit test.

### Kindle Previewer inspection
Rendering problems often appear only after the EPUB is opened in a target reader.

### Failure case: stale outputs
Authors edit markdown but distribute an older EPUB because the output was never rebuilt and inspected.

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
- reproducible builds reduce publishing errors.

**Contested or emerging:**
- how strict AI1 should be about refusing builds when sidecars are unverified.
- How much autonomy to grant coding/writing agents before human checkpointing.
- How formal verification sidecars should be for small author-led projects.
- How to keep textbook pipelines humane while still enforcing enough structure to prevent drift.

**Key references:**
1. Pandoc User's Guide — EPUB and metadata behavior, https://pandoc.org/MANUAL.html
2. Local build.sh and metadata.yaml — project-specific build path.
3. Local scripts/sync-to-book.sh — adoption tooling.

**Recent developments (last 3 years):**
- agentic editing makes build verification more important because edits can touch many files quickly.
- Repository-aware coding agents have made multi-file book operations practical, but also easier to perform too quickly.
- AI governance expectations now emphasize provenance, human oversight, risk management, and disclosure for higher-stakes outputs.
- Courseware and book projects increasingly ship in multiple formats, making build verification a teaching problem as much as a technical one.

---

## E. Teaching considerations

**Where students get stuck:**
- Students get stuck when build output paths are unclear; require a screenshot or exact output filename.
- Use the analogy of a print proof.
- Exercise: intentionally break metadata, build, observe, then fix.

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

- Confirm the exact Kindle Previewer workflow on macOS before final prose.
