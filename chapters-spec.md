<!--
    chapters-spec.md
    Blueprint Phase 3: Chapter Specifications.
-->

# AI1 CLI — Chapter Specifications

**Author:** Nik Bear Brown

*Phase 3 output from Blueprint. Drafted from book.md + outline.md (approved direction, 2026-06-12). Sidecar unverified until human sign-off. Outcomes live in architecture.md; this file gives each chapter's shape in compact form — full /c1 expansion happens at drafting.*

---

## Chapter Anatomy (every chapter)

Overview (1–3 pages: the artifact you're about to make, why the system works this way) → Exercises (the chapter's bulk; each ends with an openable artifact + a log/gate line) → Bridge (the question the next chapter answers). Apparatus per the assessment plan: exercises always; quiz + key terms generated, not hand-written.

## Chapter Specifications

**Ch 1 — Inventory, Research, Blueprint, Sign-Off**
*Capability:* run the evidence→plan→signature loop before touching content.
*Opening:* the reader's clone finishes; 24 chapters of someone else's book scroll past — "what should this become?"
*Blocks:* (1) inventory the book (list, gist, length per chapter); (2) write the research prompt with the agent — restructuring writing→copywriting + do classic direct-advertising principles (differentiator-first, features→benefits, attention-first — principles, never name-brand endorsement) survive AI-era copy?; (3) run research → `pantry/`; (4) Blueprint from inventory + research (incl. assessment plan); (5) review and sign — or refuse and revise — GATE 0, logged.
*Worked example:* one chapter's inventory row + one research finding → the Blueprint line it changed.
*Exercises:* the five blocks ARE the exercises; deliverable = pantry research file + signed (or refused-with-reasons) GATE 0 in STATUS.md.
*Bridge:* you signed a plan for a book that doesn't build under your name yet — Chapter 2 fixes that in ten minutes.

**Ch 2 — Rebuild the Book You Just Replanned**
*Capability:* end-to-end rebuild + ownership + governance.
*Opening:* change one sentence; `./build.sh`; your sentence in a real EPUB (the pebble).
*Blocks:* build mechanics in plain language; metadata.yaml identity (title/author/cover); Kindle Previewer path + no-device fallback; governance adoption via sync (AI1.md, CONDUCTOR.md, verify tooling arrive — reader performs the adoption).
*Worked example:* before/after metadata + the rebuilt cover page.
*Exercises:* sentence-change rebuild; full re-identification; sync + read what arrived; log the runs.
*Bridge:* it builds under your name — but it doesn't sound like anyone yet.

**Ch 3 — Rewrite a Chapter in Another Voice**
*Capability:* direct and judge AI rewriting; originals untouched.
*Blocks:* voices/ mechanics; diff reading; judgment memo (which voice serves the plan's reader — cite passages).
*Exercises:* two voices on one chapter; a 200-word judgment with quotes; log.
*Bridge:* voice is chosen — now the plan's promised assessments.

**Ch 4 — Generate the Assessments the Blueprint Promised**
*Capability:* produce and audit generated assessments.
*Blocks:* quizzes, practice exercises, Anki from chapters; the audit: find the generated question that fails its outcome.
*Worked example:* one bad generated question, dissected (tests recall when outcome says Apply).
*Exercises:* generate per the Ch 1 assessment plan; document one failure; log.
*Bridge:* assessments exist — now put the whole thing where students live.

**Ch 5 — Export to Canvas**
*Capability:* book → `.imscc` → imported course.
*Blocks:* build-canvas; import into free Canvas teacher account; module order vs. the signed plan.
*Exercises:* full export-import; one module-order discrepancy found or confirmed absent; log.
*Bridge:* the course shell exists — but whose claims are in it?

**Ch 6 — Facts: Check a Claim, Record It, Sign It**
*Capability:* the verified-artifact habit on facts.
*Blocks:* facts.json tour; trace one claim; add one sourced fact (`verified: false`); the human signature and its scope.
*Worked example:* one fact entry, full schema, before/after signature.
*Exercises:* trace, add, sign one; refuse to sign one (with reason); log.
*Bridge:* Part I closes — you can operate everything. Now the plan starts cutting.

**Ch 7 — Cut to the Blueprint**
*Capability:* scope execution with an audit trail.
*Opening:* the signed plan vs. 24 inherited chapters — the gap is the to-do list.
*Blocks:* Editorial Review's organization diagnosis as evidence; the exclusion log (what, why, who, reopen condition); performing deletions.
*Exercises:* cut per plan; log every exclusion; one deliberate disagreement with the plan, resolved explicitly (plan amended or cut made) — never silent.
*Bridge:* what survives must change genre.

**Ch 8 — Convert What Survives** *(hard chapter — see below)*
*Capability:* agent-assisted genre transformation + the human rewrite.
*Blocks:* conversion maps (profile→case study, proposal→pitch, evaluation→product review, rhetorical analysis→ad teardown); directing transformation; the human rewrite; GATE 3 — the signature no agent may give.
*Worked example:* one passage three ways — original, agent conversion, human rewrite — with what changed and why.
*Exercises:* convert two chapters; rewrite one until it's yours; sign GATE 3; log.
*Bridge:* the old book is converted — the new book has holes the plan already named.

**Ch 9 — Add What's Missing** *(hard chapter)*
*Capability:* authoring net-new material in-system.
*Blocks:* drafting from research not memory (`pantry/` is the source; see `pantry/ogilvy-ideas.md` usage rule — principles as hypotheses, no name-brand endorsement); candidate new chapters: headlines/hooks/CTAs, landing pages, email sequences, brand voice; figures + visual audit.
*Exercises:* draft one new chapter from pantry research; one figure passing audit; log.
*Bridge:* the manuscript is whole — does it match what you signed?

**Ch 10 — The Manuscript Meets the Blueprint**
*Capability:* delivery-vs-promise verification.
*Blocks:* Editorial Review (reader's report); adoption-failure critique; reconciliation — amend manuscript or amend plan, with changelog; never drift.
*Worked example:* one divergence, both resolution paths costed.
*Exercises:* full review; reconcile every divergence explicitly; log/changelog.
*Bridge:* the structure is honest — now the sentences must be.

**Ch 11 — Fact-Check Old and New**
*Capability:* claim-level verification at manuscript scale.
*Blocks:* inherited vs. new claims; research notes for new chapters; fact-check pass; source-or-cut discipline.
*Exercises:* fact-check the converted book; report; every flagged claim resolved; log.
*Bridge:* checked and signed — ship it.

**Ch 12 — Ship Everywhere**
*Capability:* the honest run completed; all exports.
*Blocks:* final build; EPUB/Kindle; Canvas; Medhavy `.mdx` (export only — capabilities are its own book); assessments regenerated; the provenance walk — defend one gate decision.
*Exercises:* all four exports; provenance walk written up; final log entry.
*Bridge:* the book is shipped — now let it speak.

**Ch 13 — From Book to Video** *(capstone; extension)*
*Capability:* extend a finished, signed book into video without losing its authority.
*Blocks:* Unreal Reels as AI+1's sibling (the two laws — audio is the master clock; the human signs every gate — and `beat_sheet.json` as the spine, mirroring `facts.json`); the three forms (lecture / explainer / reels-promo) over one engine; the lecture pipeline in three stages (pool → sign the plan → narrate/preview); fidelity downstream of a GATE-4 chapter (a fidelity check, not a fact-check from scratch); the render gate the agent may never sign; a lecture as a first-class AI+1 artifact (its own sign-off sidecar). Referenced, not bundled — like Medhavy.
*Worked example:* one shipped chapter → a previewed lecture spine → a clean fidelity report → a signed lecture.
*Exercises:* pick a chapter and choose its video form; build and preview a lecture spine; run the fidelity pass, resolve every flag, sign the lecture.
*Bridge (coda):* same loop, empty starter — your book this time.

## Case Study Strategy

One running case (writing-guide→copywriting) carries the book — deliberate exception to domain-rotation, because continuity *is* the pedagogy. Escalation: Act One cases have clear answers (does it build?), Act Two require judgment (what dies?), Act Three have no single right answer (plan vs. manuscript). At least one failure case is built-in: Ch 4's bad generated question and Ch 10's divergences are *engineered to exist*.

## Contested Claims Audit

"Classic direct-advertising principles still apply in an AI world" — **deliberately contested**: Ch 1 frames it as a research question, not a claim; the book reports what the reader's research finds. "Gates produce better books than open-loop generation" — the book's thesis; argued, with the flood as evidence, acknowledged as position. AI-tool specifics (agent names, platform limits) — emerging/perishable; see aging audit.

## Coverage Gaps (named, accepted)

No prompt-engineering theory; no KDP/storefront mechanics beyond producing the file; no Medhavy capabilities (own book); no toolchain internals (docs/). Acknowledge the first two in the preface.

## Hard Chapters

**Ch 8** — hardest to write: must show transformation quality, not assert it; the three-way worked example is load-bearing; risk = mush if the example is weak. Ideal author: someone who has actually rewritten agent prose in anger. **Ch 9** — second: net-new copywriting content must be good *copywriting*, not just good process; leans on pantry research quality. **Ch 1** — riskiest pedagogically (planning as opener); mitigation already in architecture.md.

## Aging Risk Audit

High: platform constraints (Canvas import flow, Kindle Previewer, agent CLIs) — isolate in boxed "current as of" steps; the loop (inventory→research→plan→sign) is the stable core. Medium: the copywriting research findings (AI-era copy norms shift) — but the *method* of re-asking is the lesson, so aging is survivable by design. Low: gates, sidecars, facts — the system's own concepts.
