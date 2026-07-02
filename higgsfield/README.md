# Higgsfield

Higgsfield is a topic-discovery prompt system for short educational physics videos.

It adapts the useful part of CAJAL: disciplined scoping. CAJAL asks, "What figure is worth making, and what must it exclude?" Higgsfield asks, "What one-minute explainer topic is worth making, and what must it not try to cover?"

The first milestone is not video generation. The first milestone is a ranked list of possible topics from a book or chapter.

## Goal

Produce candidate topics for "One Minute Physics" style explainers and Manim visualizations:

- one idea per video
- visually explainable
- compressible to roughly 60 seconds
- grounded in source text
- not too broad
- not just a vocabulary definition
- not dependent on too much prerequisite machinery
- assigned to the right production mode

## Files

- `higgsfield.md` — the core command set and system prompt
- `topic-scan.prompt.md` — paste-ready prompt for scanning chapters/books
- `manim-visualization.prompt.md` — follow-up prompt for turning a Manim-suited candidate into an animation brief
- `tests/quantum-mechanics-books.md` — test plan for the quantum mechanics book series

## Output Shape

Higgsfield produces a topic inventory, not a script:

```markdown
## Candidate 01 — Why a particle in a box cannot sit still

- Source: quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md
- Production mode: Manim visualization
- Hook: The bottom of the box is not the lowest allowed motion.
- Core idea: Boundary conditions force curvature, and curvature costs kinetic energy.
- Visual object: standing wave trapped between two walls
- Manim move: compare
- 60-second fit: Strong
- Prerequisites: wave, boundary condition, energy
- Exclusions: no full derivation, no normalization, no Fourier expansion
- Score: 9/10
```

## Naming

The name is deliberately close to the physics use case: the "field" is the chapter text, and the output is where concepts acquire mass as candidate videos.
