# Chapter 1 — Inventory, Research, Blueprint, Sign-Off

Start by telling your agent to clone the book we'll be working on for the rest of this book:

```
git clone https://github.com/Humanitariansai/writing-guide.git
```

What arrives is a complete, finished textbook: **the Writing Guide**, a 24-chapter college composition and rhetoric text. Open `chapters/` and skim the titles — the literacy narrative, memoir, the profile ("telling a rich and compelling story"), proposal writing, evaluation and review, the analytical report, rhetorical analysis, position argument, the research process, the annotated bibliography, image analysis, multimodal writing, scripting for the public forum, portfolio reflection. It teaches a college student to write across the genres a first-year course demands. It builds with one command. It is fact-checked, illustrated, and done — and none of it is yours.

Here is what you and this book are going to do with it, over the next eleven chapters: **convert it into a copywriting book** — writing that exists to make a reader act. Chapters that serve a copywriter get transformed (the profile becomes a customer case study; the proposal becomes a pitch; rhetorical analysis becomes an ad teardown). Chapters that don't get cut, with logged reasons. Chapters copywriting needs that composition never taught — headlines, offers, landing pages, email, brand voice — get written. Along the way you'll add exercises and quizzes, generate flashcards, and export the result everywhere it needs to live: **Kindle** (a clean EPUB), **Canvas** (an importable course), and **Medhavy** (`.mdx`).

But none of that starts with editing. It starts with getting the **book map — the Blueprint — right.** A book is a few hundred decisions wearing a table of contents: who the reader is, what each chapter builds, what dies, what's missing, and which assessments the book owes its readers. Make those decisions mid-draft and they get made by momentum. Make them up front, against evidence, and every later edit has something to be checked against. That's this chapter, hands-on: inventory the book you just cloned, commission and run real research, have Blueprint draft the plan from that evidence, and then sign it — or refuse to, with reasons, which counts just as much.

The gate at the end of this chapter is called **GATE 0**, and it carries the rule that will follow you through this entire book: *the agent prepares; the human signs.* Your agent will do every step below with you — the listing, the research, the drafting of the plan. The one thing it cannot do, by the system's constitution, is approve the result. That signature is yours, it gets logged, and every chapter after this one will cite it.

## The exercise: six steps to a signed plan

Work with your agent. Each step produces an artifact you can open.

### Step 1 — Inventory the book you cloned

Ask your agent to read `chapters/` in your `writing-guide` clone and produce an inventory table: chapter number, title, what it actually teaches (one line, not the title restated), and approximate length. Read the table. Fix at least one row where the agent's one-liner misses the chapter's real point — you'll find one, and finding it is the lesson: *the inventory is a claim, and you just checked it.*

**Artifact:** the inventory table, saved in the repo.

### Step 2 — Write the research prompt

You're converting a book that teaches *writing* into a book that teaches *copywriting* — writing that exists to make a reader act. That conversion raises two genuine research questions, and you're going to commission the research rather than trust anyone's memory, including your agent's:

1. **Structure:** How do composition skills map to copywriting skills? Which of this book's 24 chapters have a copywriting counterpart (a profile becomes a case study; a proposal becomes a pitch; rhetorical analysis becomes an ad teardown), which have none, and what does a copywriting book need that a composition book never taught — headlines, offers, calls to action, landing pages, email, brand voice?
2. **Principles:** The classic principles of direct advertising — state the differentiator before writing a word, translate features into benefits, earn attention before asking for it — were formulated in a world of paid pages and scarce attention. **Do they still hold in an AI world**, where copy is generated in volume, feeds and search mediate attention, and your reader may be a recommendation algorithm before it's a person? Treat these as hypotheses to test, not doctrine to inherit — and cite them as principles, not as any famous name's endorsement.

Draft the prompt with your agent, then read it the way you read the inventory: would a stranger know exactly what questions to answer and what evidence to bring back? Sharpen it until yes.

**Artifact:** the research prompt.

### Step 3 — Run the research

Have your agent run it — web sources, with citations, dead links rejected. Demand the same discipline the system demands everywhere: every claim in the findings traces to a source you could click. If the agent asserts that "benefit-led copy outperforms feature-led copy," there had better be a study, a documented test, or an honest "practitioner consensus, evidence thin" label attached.

### Step 4 — Save it to the pantry

Research that lives in a chat scroll dies with the chat. Have the agent save the findings to `pantry/` — the repo's room for raw material — as a named file (e.g., `pantry/copywriting-conversion-research.md`). From now on, that file is citable: the Blueprint will reference it, Chapter 9 will draft from it, Chapter 11 will fact-check against it.

**Artifact:** the pantry file. Open it. Skim the sources. This is what "the trail" means.

### Step 5 — Blueprint

Now ask the agent to run **Blueprint** (the planning consultant in `conductor/00-blueprint/`) against two inputs: your inventory and your research. It will produce the new book's plan — vision (who the copywriting reader is, what the book argues), architecture (what each chapter builds, in what order, and the **assessment plan**: quizzes, exercises, flashcards, Canvas modules — each marked desired, needed, or out of scope), chapter spec, risks, and a proposed table of contents. With 24 inherited chapters, expect Blueprint's consolidation audit to fire — a course-adoptable book wants 12–14. Watch which chapters it proposes to cut, and notice whether you flinch. The flinch is information.

### Step 6 — Sign, or refuse

Read the plan. Not skim — read, with three questions: Is this reader someone I can picture? Does each chapter build something the research supports? Would I cut what it cuts? Then decide:

- **Approve:** tell your agent to record the sign-off — GATE 0 checked in `STATUS.md`, the plan's files marked verified with your name and the date. *The approval is logged.* That log line is the first entry in a trail that will, eleven chapters from now, let you defend every structural decision in your finished book.
- **Refuse:** just as valid. Name what's wrong, have Blueprint revise, read again. A refused gate with reasons is the system working; a reluctant signature is the system failing.

**Artifact:** the logged decision — either way.

## Worked example: one row, one finding, one plan line

From a real run of this chapter: the inventory row for writing-guide's Chapter 7 read *"Profile — telling a rich and compelling story: interview-based portrait of a person, emphasis on concrete detail."* The research's structure pass found that copywriting's nearest genre is the **customer case study** — same interview, same concrete detail, but organized around a transformation and ending in proof. The Blueprint line that resulted: *"Ch: Case Studies That Sell — converts writing-guide ch. 7; keeps interviewing and detail; adds outcome framing and a proof section; exercise: convert one profile into a case study with a verifiable result."* Inventory → evidence → plan, one line of each, all three citable. That's the loop, in miniature, that you just ran twenty-four times.

## What can go wrong

| Symptom | What it means | Fix |
|---|---|---|
| Agent starts rewriting chapters during Step 1 | it skipped the plan, like everyone wants to | stop it; point it at this chapter; inventory only |
| Research findings with no citations | fluent ≠ verified | send it back: every claim gets a source or a "consensus, evidence thin" label |
| Blueprint keeps all 24 chapters | consolidation audit didn't fire or was ignored | ask for it explicitly; a plan that cuts nothing decided nothing |
| You can't decide whether to sign | the plan is vague somewhere — find where | name the vague section; refusing with reasons beats signing with doubts |

## Bridge

You now own a signed plan for a book that doesn't build under your name yet. Chapter 2 fixes that in about ten minutes — you'll change one sentence, run one command, and watch a real EPUB come out with your change in it. Then you'll put your name on the cover.
