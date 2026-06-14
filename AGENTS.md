<!-- GENERATED FILE — do not edit by hand.
     Source: instructions/ (_shared/ modules + project file) · manifest: instructions/manifest.yml
     Rebuild: node scripts/build-instructions.mjs   ·   Promote: --promote
     Hand edits are overwritten on the next build. -->

# Agent Instructions

## Governance

This repository is built phase-by-phase through a gated pipeline.

**Read `AI1.md` first — it is the source of truth for the AI+1 system** (one human plus AI agents making books neither could make alone). It authorizes `CONDUCTOR.md` as the build spine; read that next, then `STATUS.md` to see which phase is active and which gates are signed. If any file conflicts with `AI1.md`, `AI1.md` governs and the conflict is a bug — report it to the human and record it.

## `help`

If the user types `help` (or seems new, or asks "what can I do?"), **read `HELP.md` and present it** — the friendly, non-technical orientation for someone who just opened this repo and wants to talk to the book. For the full briefing on the two build paths and how the agent works, see `HOW-TO-USE.md`.

## The human is non-technical; the agent does the typing (P5)

Assume the user is non-technical — email and chatting with the agent on a website, nothing more. **Never ask them to open a terminal, edit a file, run a command, or obtain an API key.** *You* run the scripts, edit the files, and build the outputs, then report in plain language. Default to **agent mode**: you are the model, so the LLM steps need no API key.

## Secure key path (P5)

If a key is ever genuinely required (e.g. ElevenLabs audio), use the **secure path** so the key never passes through chat: create `.env` from `.env.example` if missing, **open it** for the user (e.g. `open .env`), have them paste the key on its line and save, then confirm it's set with a non-echoing check (`grep -q '^ELEVENLABS_API_KEY=.\+' .env`). **Never print, echo, log, or repeat a key back, and never commit `.env`.** Only offer the paste-in-chat shortcut if they prefer convenience, and warn once that it sends the key through the chat. See `KEYS.md` and `MODES.md`.

## Phase gates, in order (P1, P3)

Work one phase at a time, in order — do not skip a gate. Do not start a phase until the previous phase's gate is signed off in `STATUS.md`. Phase instructions live in `conductor/<phase>/`; executable code lives in `scripts/`. **GATE 3 (Human Rewrite) is human-only — never sign it yourself**, and never sign anything you cannot honestly attest.

## Generation is the fallback, not the default (P2)

**Before generating any artifact, check it isn't already verified:** run `python scripts/verify.py check <artifact>`. If verified (exit 0), **use the existing file — do not regenerate.** If unverified, stop and say so. If absent, generate it, run `python scripts/verify.py stub <artifact> --phase <phase>`, and **STOP** for human sign-off. Only a human runs `python scripts/verify.py sign`. The sidecar (`<name>.verified.json`) is the artifact's passport. See `conductor/VERIFICATION.md`.

## Leave a trail (P7)

Research notes, fact-check reports, audit output, and `.verified.json` sidecars are artifacts — **commit them, do not discard.** Never delete a hand-made artifact or a sidecar; the only safe removals are rebuildable outputs (`output/`, `__pycache__/`, `*.pyc`). When unsure, stop and ask the human — a wrong autonomous phase is expensive to unwind.

## AI1 CLI

This repo writes books with the **AI+1** method — one human plus AI agents making a book neither could make alone. The agent executes (research, drafting, fact-lookup, figures, builds, audits); the **+1**, the human, does what cannot be delegated: deciding what the book *is*, rewriting it until it carries their voice, and signing every gate. The seven-phase spine runs Blueprint → Research → Draft → Human Rewrite → Fact Check → Images → Check Images, with optional `conductor/editions/` and `voices/` after the spine.

Everything operational lives in `CONDUCTOR.md` (the spine), `STATUS.md` (current phase + gate state), `MODES.md` / `KEYS.md` (agent mode and the secure key path), and `SOURCE-MANIFEST.md` (what syncs downstream).
