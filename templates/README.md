# templates/

Source-only. Lives in ai1-cli and is never synced to a book.

`seed/` holds the blank per-book files that `scripts/sync-to-book.sh` copies into
a book when they are missing (the SEED list in `../SOURCE-MANIFEST.md`). Paths
under `seed/` mirror the book root: `seed/facts/facts.json` seeds
`facts/facts.json`.

ai1-cli is itself a book, so its own root copies of these files (`book.md`,
`vision.md`, `STATUS.md`, `metadata.yaml`, …) carry the AI1 CLI book's values.
They are never the seed source. To change what a new book starts with, edit the
template here. Every SEED entry in the manifest needs a file here; the sync
warns and skips any that is missing.

Placeholders a new book fills in: `[BOOK TITLE]`, `[YYYY]`, `[YYYY-MM-DD]`,
`<book-slug>`, the `name` in `package.json`, and every `[NEEDS HUMAN INPUT]` in
`book.md`. Blueprint (Phase 0) writes the other planning files.
