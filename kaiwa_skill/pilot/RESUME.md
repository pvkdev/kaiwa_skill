# Pilot resume test — Shigoto no Nihongo: Denwa Outai Kisohen

- Book ID: `shigoto-no-nihongo-denwa-outai-kisohen-dfdb0e2b61e0`
- Source SHA-256: `dfdb0e2b61e0322252532c2a83a7c4c5d62269b45edb40ae61eb5e3c32b74711`
- Sequence: `pilot-sol-a` verified physical PDF pages 20–21 and released its claim; fresh worker `pilot-sol-b` read the handoff, checked read-only status, claimed the same book, reconciled it, then rendered, transcribed, visually reviewed, and verified **only pages 22–23**. It built a partial book from all four verified pages and released its claim.
- This was a clean, sequential worker handoff. It did **not** simulate a killed process or an interrupted write.

## Earlier verified files remained unchanged

| File | Before SHA-256 (handoff) | After SHA-256 | Result |
| --- | --- | --- | --- |
| `pages/p0020.md` | `425eb02c0072a2433371899a6ea60010cfc8ceeadff9b0ad0f9da24ea30ca72d` | `425eb02c0072a2433371899a6ea60010cfc8ceeadff9b0ad0f9da24ea30ca72d` | unchanged, verified |
| `pages/p0021.md` | `812c10e6439165052bcae06f0af7f2a445e3321c9369e2b7e8ea1043453ba7e0` | `812c10e6439165052bcae06f0af7f2a445e3321c9369e2b7e8ea1043453ba7e0` | unchanged, verified |
| `renders/p0020.png` | `c625feef91e542d8ea13448a5fda89598072d3968179e721ffdcf2e1df00ec1e` | `c625feef91e542d8ea13448a5fda89598072d3968179e721ffdcf2e1df00ec1e` | unchanged |
| `renders/p0021.png` | `ab299ee1b6a07fda30655da00e8b61cc7dddf42a606c89674968ff15ba4651ea` | `ab299ee1b6a07fda30655da00e8b61cc7dddf42a606c89674968ff15ba4651ea` | unchanged |

Paths in the table are relative to `kaiwa_skill/corpus/shigoto-no-nihongo-denwa-outai-kisohen-dfdb0e2b61e0/`.

## Outcome

- Pages 22–23 were opened at render scale 4 (about 288 DPI); enlarged crops were also inspected. Their page checkpoints contain review evidence with specific regions and source comparisons.
- The generated `build.json` includes verified physical pages `[20, 21, 22, 23]`. The book has 162 pages, so `complete: false` and `transcription_complete: false` are correct. No page outside the four-page pilot was processed.
- Final status after release: four verified, 158 pending, zero issues, no claim, `build_current: true`.
- Independent coordinator/Astra review and the separate simulated-crash tests remain outside this clean handoff observation.

## Later QA edit (after the handoff test)

On 2026-11-10, the independent full-page review found the source transcription faithful and requested clearer editorial labels under `core/MARKDOWN.md` v0.1.2. Worker `pilot-sol-b-qa` changed only the four editorial labels on p20, p21, and p23, reopened those source renders, recorded new drafts and review evidence, reverified the three pages, rebuilt, and released the claim. No source-language transcription or render changed. The table above deliberately retains the hashes measured **at the time of the clean handoff test**; these later Markdown changes do not retroactively invalidate that observation.

Current verified Markdown SHA-256 after the later QA edit:

- `pages/p0020.md`: `01b92c723296d439beee964bc4e2e30041b4b5fbc5e9c893b02680abdee6b0ea`
- `pages/p0021.md`: `ae20fdde838ed0f164eba2141ba0fcbfcd5c7c30b1324a50eae4b37943b3269c`
- `pages/p0022.md`: `6f5fb4bbe051a3b1dd028baca742bc7be2e4c00b5615da034a3ac46b46bee486` (unchanged)
- `pages/p0023.md`: `95bd3f6b27ee710ab3bda92b3e24336548f29a5e7fe8a397dfe8cd158a7c7924`
