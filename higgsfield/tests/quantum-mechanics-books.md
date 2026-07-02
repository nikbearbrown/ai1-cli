# Higgsfield Test Plan — Quantum Mechanics Books

The first tests for Higgsfield should run on the sibling quantum mechanics books in the Codex workspace.

## Test Corpus

Expected source directories:

- `/Users/nik/Documents/Codex/quantum-mechanics-vol1/chapters`
- `/Users/nik/Documents/Codex/quantum-mechanics-vol2/chapters`
- `/Users/nik/Documents/Codex/quantum-mechanics-vol3/chapters`
- `/Users/nik/Documents/Codex/quantum-mechanics-vol4/chapters`
- `/Users/nik/Documents/Codex/quantum-mechanics-vol5/chapters`
- `/Users/nik/Documents/Codex/quantum-mechanics-a-companion-guide/chapters`

## Test 1 — Single Chapter Scan

Input:

```text
/scan silent
/Users/nik/Documents/Codex/quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md
```

Expected behavior:

- proposes 3-6 candidates
- at least one strong candidate about zero-point energy or "cannot sit still"
- rejects at least one over-broad or derivation-heavy candidate
- every candidate has a source path, visual object, exclusions, and score
- every candidate has a production mode
- wave-fitting and energy-ladder candidates are classified as `Manim visualization`

Pass condition:

- no candidate tries to cover the entire infinite square well chapter
- no candidate requires normalization, orthonormality, and time evolution all in one video
- at least three strong candidates include a `Manim move`

## Test 2 — Advanced Chapter Scan

Input:

```text
/scan silent
/Users/nik/Documents/Codex/quantum-mechanics-vol3/chapters/04-the-wkb-approximation-and-tunneling.md
```

Expected behavior:

- separates tunneling intuition from WKB derivation
- flags derivation-heavy material as borderline or reject
- produces at least one candidate with a single visual object: barrier, fading wave, or turning point
- classifies WKB/tunneling candidates with moving wave/barrier geometry as `Manim visualization`

Pass condition:

- does not propose "Explain WKB approximation" as a strong one-minute topic

## Test 3 — Quantum Information Scan

Input:

```text
/scan silent
/Users/nik/Documents/Codex/quantum-mechanics-vol4/chapters/06-open-systems-and-lindblad.md
```

Expected behavior:

- identifies decoherence as a strong candidate
- distinguishes "open system" from "measurement problem"
- excludes master-equation derivation from first-pass videos

Pass condition:

- at least one candidate can be explained with one visual motion: a clean state becoming entangled with environment marks
- candidates that are mostly interpretation or philosophy are not forced into Manim

## Test 4 — Math Support Scan

Input:

```text
/scan silent
/Users/nik/Documents/Codex/quantum-mechanics-vol5/chapters/06-the-fourier-transform.md
```

Expected behavior:

- identifies Fourier transform as a visual transformation, not a formula dump
- proposes candidates around wave packet to momentum spectrum, Gaussian self-transform, and bandwidth/uncertainty
- rejects "derive the Fourier transform"

Pass condition:

- strong candidates have visual anchors and no more than 3 prerequisites
- transform-based candidates are classified as `Manim visualization`

## Test 5 — Series Deduplication

Input:

```text
/series silent
/Users/nik/Documents/Codex/quantum-mechanics-vol1/chapters
/Users/nik/Documents/Codex/quantum-mechanics-vol2/chapters
/Users/nik/Documents/Codex/quantum-mechanics-vol3/chapters
/Users/nik/Documents/Codex/quantum-mechanics-vol4/chapters
/Users/nik/Documents/Codex/quantum-mechanics-vol5/chapters
```

Expected behavior:

- returns a deduplicated list of candidate topics
- groups repeated motifs such as tunneling, uncertainty, spin, measurement, Fourier methods, and orbitals
- recommends a "Best First 10 Topics" list

Pass condition:

- does not list the same topic repeatedly under slightly different names
- preserves source references for each grouped topic

## Smoke-Test Expected Best First Topics

A good first series list should include topics close to:

- Why a particle in a box cannot sit still
- Why tunneling is not borrowing energy
- Why spin is not a tiny ball spinning
- Why electrons make stripes one dot at a time
- Why the electron in hydrogen is a cloud, not an orbit
- Why identical electrons cannot share the same state
- Why measuring one thing can erase what you knew about another
- Why a wave packet spreads
- Why a laser needs matching photons
- Why decoherence makes quantum behavior look classical

These are not required exact titles. They are calibration anchors.
