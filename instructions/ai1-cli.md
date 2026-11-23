## AI1 CLI

This repo writes books with the **AI+1** method — one human plus AI agents making a book neither could make alone. The agent executes (research, drafting, fact-lookup, figures, builds, audits); the **+1**, the human, does what cannot be delegated: deciding what the book *is*, rewriting it until it carries their voice, and signing every gate. The seven-phase spine runs Blueprint → Research → Draft → Human Rewrite → Fact Check → Images → Check Images, with optional `conductor/editions/` and `voices/` after the spine.

For an author-requested consolidated textbook, read the
[private pre-review procedure](conductor/consolidated-textbook.md) and use its
isolated draft-proof route. Do not edit production artifacts or gate status,
publish, import to an LMS, or disclose private source material from that route.

Everything operational lives in `CONDUCTOR.md` (the spine), `STATUS.md` (current phase + gate state), `MODES.md` / `KEYS.md` (agent mode and the secure key path), and `SOURCE-MANIFEST.md` (what syncs downstream).
