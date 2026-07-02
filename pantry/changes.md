# Change Log

One line per edit, newest at the bottom:
`YYYY-MM-DD · file · what changed · reason`

---

2026-07-01 · chapters/13-from-book-to-video.md · added Chapter 13 (capstone) explaining Unreal Reels — turning a finished book into video · author direction; a shipped book is raw material for video, taught as an extension of the same gated discipline
2026-07-01 · outline.md · added "Beyond the Book" → Ch 13 + amendment note; chapter count 12→13 (13→14 w/ Ch-2 insertion), within 12–14 target · reflect the new chapter, logged not drift
2026-07-01 · chapters-spec.md · added Ch 13 spec (capstone/extension) · sync spec with outline
2026-07-01 · architecture.md · added Ch 13 learning outcomes + outcome-map row · sync outcomes with outline
2026-07-01 · chapters/13-from-book-to-video.md.verified.json · stubbed sidecar (verified:false) · new artifact awaits human sign-off per P2
2026-07-01 · chapters/{01-what-ai-plus-one-is … 20-ask-ai-everywhere}.md (21 files) · ported the drafted chapter bodies from ai1-cowork into ai1-cli, reframed for the Cowork app (CLI/terminal framing → Cowork desktop app; agent does the typing) and terminology aligned (Tic-TOC → Blueprint) · author direction: fill ai1-cli's missing drafted chapters from the older cowork draft; each got a stubbed verified:false sidecar
2026-07-01 · KNOWN ISSUE (needs author decision) · ai1-cli/chapters now holds TWO structures at once — the current restructured set (00-introduction, 01-inventory-research-blueprint-signoff, 02-chapter-research, 13-from-book-to-video) AND the ported old-draft set (01-what-ai-plus-one-is … 20-ask-ai-everywhere). Duplicate chapter numbers (two 01s, three 02s, two 13s); build.sh globs *.md alphabetically so the EPUB would interleave them. outline.md/chapters-spec.md/architecture.md still describe only the restructured 13-chapter book. Reconcile before GATE 0.
2026-07-01 · RESOLVED (author chose: keep restructured 13-ch structure, fold ported chapters in as source) · moved all 21 ported chapters out of chapters/ into pantry/cowork-source/ (sidecars → *.verified.json.bak so verify.py ignores them); added pantry/cowork-source/README.md keying each source file to its restructured target per the outline mapping. chapters/ is coherent again: Intro, Ch 1, Ch 2, Ch 13, appendices 80–97. Chapters 3–12 remain to be drafted (Phase 2) from the staged seed + the copywriting running project.
2026-07-01 · outline.md · added amendment note recording the pantry staging + that Ch 3–12 are still to be drafted · reflect the fold-in decision, logged not drift
2026-07-01 · voices/teardown/VOICE.md · created the Teardown voice (v3.2, formerly "Feynman × MKBHD") — intellectual-honesty + design-critic register with a command set (/essay /nart /write /bookmap) and the /done finishing pass (adds subtitle + exercises if missing, seeds visual-suggestion HTML comments) · author direction
2026-07-01 · voices/README.md + STATUS.md · registered the Teardown voice in the voices menu + voice checklist · keep the menu in sync with the new voice
2026-07-01 · voices/feynman-mkbhd → voices/teardown · renamed the voice to "Teardown" (single-word register name matching Wonder/Sardonic/Pragmatist); kept a "formerly Feynman × MKBHD" note · author direction
