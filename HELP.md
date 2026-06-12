# Help — Talking to This Book

Welcome. **This repository *is* a book** — one you build and make your own by
talking to a CLI agent (Cowork, Claude Code, or Codex). You describe what you
want in plain language; the agent finds the right file, does the work, and tells
you what happened.

**You don't need to be technical.** No terminal, no editing files, no API keys —
if you can use email and chat with Claude on a website, you can build this book.
The agent does the typing, the commands, and the building for you. (The only key
that ever comes up is an optional one for spoken audio on flashcards — and even
then you just paste it into the chat — or add it privately, see `KEYS.md`.)

Everything is self-contained in this repo.

---

## Just say what you want

You don't need commands — talk to the agent. Examples:

**Build something to hand out**
- *"Build the book"* → an EPUB you can read or publish (`./build.sh` → `output/`)
- *"Build a Canvas course"* → an `.imscc` you import into Canvas/Moodle/Blackboard
- *"Make an Anki flashcard deck"* → a `.apkg` for spaced-repetition study
- *"Make chapter quizzes"* or *"practice exercises"* → ready-to-use study materials

**Rewrite the book in a different voice** (a copy; the original is untouched)
- Wonder · Generic (OpenStax-style) · Socratic · Sardonic · Narrative · Pragmatist
- e.g. *"Rewrite Chapter 3 in the Socratic voice"*

**Work with facts**
- *"Build a fact dictionary from this source"* → `facts/`
- *"Fact-check the book"* → checks claims, writes a report

**Drive the build pipeline**
- *"What phase are we in?"* → the agent reads `STATUS.md`
- *"Start the next phase"* / *"How do I start?"* → the agent follows `CONDUCTOR.md`

---

## The three ways to begin

1. **Download a finished book** — clone a complete, fact-checked AI+1 book from
   GitHub and make it yours: rewrite it in your voice, swap in your subject, rebuild.
2. **Learn by doing** — stay right here: try the examples above, build the EPUB,
   make a flashcard deck. Small exercises that teach you the system.
3. **Build from scratch** — plan a new book with **Blueprint**, then draft,
   fact-check, and illustrate it phase by phase.

Not sure? Just say *"what should I do first?"* and the agent will walk you through it.

---

## What's in the repo (you rarely need this)

| Folder / file | What it is |
|---|---|
| `chapters/` | the book — the markdown the agent edits |
| `CONDUCTOR.md` | the build spine the agent follows |
| `STATUS.md` | which phase is active, what's been signed off |
| `conductor/` | the instructions (prompts) for each phase + the editions menu |
| `voices/` | alternate-voice rewrites of the book |
| `facts/` | the fact dictionary + the tools that build and check it |
| `scripts/` | the runnable code the agent calls |
| `images/`, `output/` | figures, and built files (EPUB, Canvas, Anki) |

For the full guide, open `HOW-TO-USE.md`. To go deeper on the build pipeline,
`CONDUCTOR.md`.

**Ready?** Tell the agent what you'd like to do.
