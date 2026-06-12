# AGENTS.md

This repository is built phase-by-phase through a gated pipeline.

**If the user types `help` (or is new / asks what they can do), read and present
`HELP.md`** — the non-technical orientation for someone who just opened this repo.

**Assume the user is non-technical.** Never require a terminal, a file edit, a
command, or an API key from them — *you* do all of it and report in plain
language. Default to **agent mode** (you are the model; no key needed). If a key
is ever required, use the **secure path** (the key never passes through chat):
create `.env` from the template, open it for them to paste & save, then confirm
with a non-echoing check — never print, echo, or commit a key. See `KEYS.md` and `MODES.md`.

**Read `AI1.md` first — it is the source of truth for the AI+1 system.**
It authorizes `CONDUCTOR.md` as the build spine for the phase sequence,
prompts, and gates. Then read `STATUS.md` for the current phase and gate state.

Rules for any agent (Cowork, Claude Code, Codex, or other):
- Work one phase at a time, in order. Do not skip a gate.
- Phase instructions: `conductor/<phase>/`. Executable code: `scripts/`.
- GATE 3 (Human Rewrite) requires a human signature — never sign it.
- Commit artifacts (research notes, fact-check reports, audit logs).
- **Verified artifacts:** before generating any artifact, run
  `python scripts/verify.py check <artifact>`. If verified, use it — do not
  regenerate. If not, generate, run `verify.py stub <artifact> --phase <phase>`,
  and STOP. Only a human runs `verify.py sign`. See `conductor/VERIFICATION.md`.

See `CONDUCTOR.md` for the full spine and `conductor/editions/` for optional
post-spine editions.
