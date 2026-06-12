# CLAUDE.md

This repository is built phase-by-phase through a gated pipeline.

**If the user types `help` (or seems new / asks "what can I do?"), read
`HELP.md` and present it** — it's the friendly, non-technical orientation for
someone who just opened this repo and wants to talk to the book.

**Assume the user is non-technical** (email + chatting with Claude on a website —
nothing more). Never ask them to open a terminal, edit a file, run a command, or
obtain an API key. *You* run the scripts, edit the files, and build the outputs
for them, then report in plain language. Default to **agent mode**: you are the
model, so the LLM steps need no API key.

**If a key is ever genuinely required** (e.g. ElevenLabs audio), use the **secure
path** so the key never passes through chat: create `.env` from `.env.example` if
missing, **open it** for the user (e.g. `open .env`), have them paste the key on
its line and save, then confirm it's set with a non-echoing check
(`grep -q '^ELEVENLABS_API_KEY=.\+' .env`). **Never print, echo, log, or repeat a
key back, and never commit `.env`.** Only offer the paste-in-chat shortcut if they
prefer convenience, and warn once that it sends the key through the chat. See
`KEYS.md` and `MODES.md`.

**Read `AI1.md` first — it is the source of truth for the AI+1 system.** It
authorizes `CONDUCTOR.md` as the build spine; read that next, then `STATUS.md`
to see which phase is active and which gates are signed.

Do not start a phase until the previous phase's gate is signed off in
`STATUS.md`. Phase prompts live in `conductor/`; runnable scripts live in
`scripts/`. GATE 3 (Human Rewrite) is human-only — never sign it yourself.

**Before generating any artifact, check it isn't already verified:** run
`python scripts/verify.py check <artifact>`. If verified (exit 0), use the
existing file — do not regenerate. If not, generate it, run
`python scripts/verify.py stub <artifact> --phase <phase>`, and STOP for human
sign-off. Only a human runs `verify.py sign`. See `conductor/VERIFICATION.md`.

Everything else you need is in `CONDUCTOR.md`.
