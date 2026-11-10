# Pilot handoff — Shigoto no Nihongo: Denwa Outai Kisohen

- Book ID: `shigoto-no-nihongo-denwa-outai-kisohen-dfdb0e2b61e0`
- Source (relative to `kaiwa_skill/`): `book/BJT/Shigoto_no_nihongo_Denwa_Outai_Kisohen.pdf`
- Source SHA-256: `dfdb0e2b61e0322252532c2a83a7c4c5d62269b45edb40ae61eb5e3c32b74711`
- Total: 162 physical PDF pages. Scan only; `pypdf` extraction returned no text for sampled pages.
- Pilot pages: physical p20–p23 (printed pages 18–21), four consecutive pages. p20 opens Unit 1 with a key sentence and multiple-choice vocabulary exercise; p21 has listening, monologue, and roleplay; p22 has answers/explanations and listening script; p23 continues the notes and has a vocabulary table. p19 is a divider page.
- Worker A (`pilot-sol-a`) completed and visually verified **p20–p21 only**. Corpus page files and renders: `kaiwa_skill/corpus/shigoto-no-nihongo-denwa-outai-kisohen-dfdb0e2b61e0/{pages,renders}/p0020.*` and `p0021.*`.
- Verified Markdown SHA-256 for resume comparison: p20 `425eb02c0072a2433371899a6ea60010cfc8ceeadff9b0ad0f9da24ea30ca72d`; p21 `812c10e6439165052bcae06f0af7f2a445e3321c9369e2b7e8ea1043453ba7e0`.
- Render SHA-256: p20 `c625feef91e542d8ea13448a5fda89598072d3968179e721ffdcf2e1df00ec1e`; p21 `ab299ee1b6a07fda30655da00e8b61cc7dddf42a606c89674968ff15ba4651ea`. Render scale 4 (about 288 DPI).
- Continuation: fresh worker checks `status`/`reconcile`, confirms p20–p21 hashes remain unchanged, claims the book with a new owner/token, renders and visually transcribes **p22–p23 only**, records drafts and real review evidence, verifies, rebuilds partial output, then releases. Open p21/p24 for boundary context as needed. The existing scratch previews of p22/p23 are *not* review or verification evidence.
- Runtime: Python bundled của Codex (tra đường dẫn bằng load_workspace_dependencies khi đổi máy); CLI: `python kaiwa_skill/tools/ingest.py --help` from repo root. Use `init/claim/render/record/evidence-template/verify/status/build/release` subcommand help. Persisted source paths are relative to `kaiwa_skill/`; corpus paths are relative to book directory.
- Review notes are in each page's `pages/p0020.json` and `p0021.json`. The source has no supplied audio; p21's three identical printed choices in listening question 1 remain identical in Markdown. No spoken distinction or answer was invented. Small circled exercise icon on p20 is not readable as a distinct numeral. No open text-loss issue was identified in p20–p21.
- During Worker A, the CLI validator gained a required page anchor and briefly invalidated both verified pages on `build`. Worker A added `<a id="p0020"></a>` and `<a id="p0021"></a>`, re-recorded, re-reviewed, and verified; final `build` included `[20,21]` with `complete: false`. This was a schema change, not a source transcription change.
- This is a partial pilot, not a complete book conversion or independent coordinator acceptance. Worker A made no Git commit.
