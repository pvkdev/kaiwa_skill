# HANDOFF — Shigoto no Nihongo: Bijinesu Manaa Hen

- Book ID: `shigoto-no-nihongo-bijinesu-manaa-hen-0e3d5e9467fa`
- Source: `book/BJT/Shigoto_no_nihongo_Bijinesu_Manaa_hen.pdf` (136 physical pages)
- Source SHA-256: `0e3d5e9467fafaef97acda677080aa1bb6f9b849aa20e5993172ee6b0864d7a6`
- Output mode: `text_only`; rendered images are review cache only.
- Current checkpoint after reconcile/build: 106 verified, 6 needs_review, 24 pending, 0 draft/rendered/invalid. `build_current: true`; output is partial/INCOMPLETE.
- **Next independent page: PDF p0113**. Continuation worker cont4 opened p113 only to check the English m continuation from p112; no p113 transcription/checkpoint exists. Claim with a new unique owner/token before mutation. Do not reuse any prior token, including `book10-cont4-20261111-93d65b`.

## Completed coverage

PDF p0002, p0004–p0019, p0021–p0022, p0024–p0026, p0028–p0068, p0070–p0112 are verified with page-specific render/Markdown hashes and evidence. PDF p0001, p0003, p0020, p0023, p0027, p0069 are locally `needs_review` as below. No pages after PDF p0112 have been transcribed. The p0006 miniature matches full-size PDF pp0030–0031; p0007 miniature matches pp0034–0035. Their guide pages contain explicit source crossrefs and were verified after comparison. PDF p0040 is the six-panel ③ 返事の仕方 comic; p0041 contains its points c–e and 語尾の大切さ. All p0036–p0055 are verified. The continuation worker added PDF p0042–p0055 (14 pages), opening each full source page and direct 6x crops; PDF p0055 also used direct 8x heading/comic and tight panel6 crops. No new source issue arose in this batch.

## Source review items

- p0001: lower cover blurb is physically clipped at the left PDF edge. Visible suffixes are recorded; missing characters were not guessed. Direct high-resolution crops inspected. Author is `釜渕優子`.
- p0003: publisher logo/text at bottom remains too faint to certify after high-resolution and contrast inspection. Other visible text, including `釜渕優子`, recorded.
- p0020: Chinese answer ③ has one ambiguous glyph before `用` in `而不是?用手夹包`; direct 8x crop cannot certify strokes. Placeholder remains in draft Markdown.
- p0023: faint handwritten Japanese line above six-panel comic remains unreadable after high-resolution/contrast inspection. Rest of page recorded.
- p0027: Chinese female answer ② has unreadable glyph before `鸡窝` in heading and prose after direct 8x and threshold crops. Placeholder remains in draft Markdown.

- p0069: handwritten subtitle above character labels has missing strokes in the middle. Inspected full2x, direct6x, direct8x original and 4x-contrast tight crops; kept readable prefix/suffix with local marker. Six comic panels, signature `Nguyễn Sĩ Tú`, Chinese g and English continuation/g are transcribed. No inferred repair.

These six issues are source-local and do not block p0073 onward. If genuinely resolved from source, record corrected Markdown, obtain fresh hash-bound evidence, and verify; otherwise preserve `needs_review`. Do not infer text from context.

## Runtime and continuation

Python: `C:/Program Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-1104-2876-0_26.1104.2876.0_x64__3k8sg7r9htsxt/dependencies/python/python.exe`

Run from repo root `D:/CODE/git/kaiwa_skill` with `kaiwa_skill/tools/ingest.py`. Review source render and tight crops for each page, then record/verify with actual comparison. Scratch crops/evidence for the first worker remain under `.cache/renders/<book_id>/scratch-production_book_10_sol-*`; continuation scratch uses `scratch-cont-*` in the same temporary cache. Use your own scratch prefix. Continue `p0113` through `p0136`, then reconcile/build and release your new claim. The latest continuation worker owner `production_book_10_sol_cont3` releases its claim after this handoff.


## Continuation checkpoint — PDF p0042–p0055

- Completed in this batch: all 14 physical pages p0042–p0055 verified with per-page hash-bound evidence; 50 verified total, five older source-local needs_review, 81 pending p0056–p0136. Reconcile/build passed; no draft/rendered/invalid state remains. This is partial/INCOMPLETE and is not book acceptance.
- Current partial `book.md` SHA-256: `10b56eadaff74f8474bb31dba86a6606f4acc4151ef74043a9ab831789229198`; `search.jsonl`: `03f649f41eb1b1469069dee1cb084971f268fd87d4894b8613db12561a0bbab7`.
- Source oddities retained: p0043 shows deliberately wrong honorific examples and `お〜なる`; p0044 has a truly blank table row after 来る. P0047 Japanese says `俺的には`, while the English explanation prints `僕的には`. P0053 point k prints `さまざま種類` without な. These were read from the source rather than repaired.
- Continuations checked: English③ p0046 ends `It's a`, continues `trendy word...` on p0047; Chinese/English① at the bottom of p0052 continue at the top of the translations on p0053. Text remains within each physical page, with editorial cross-page notes.
- P0055 faint subtitle `〜びっくりする着信音！？〜` read using direct 8x original and contrast crops. All sound-effect syllables, dialogue/thought bubbles and meaning-bearing illustration relations are recorded. No placeholder/issue remains there.
- Next page p0056 has not been rendered or read by this worker. Seven accepted books, other active books and source PDFs were untouched. No Git stage/commit performed.


## Continuation checkpoint — PDF p0056–p0072 (production_book_10_sol_cont2)

- Batch coverage: 17 physical pages; 16 verified (p0056–p0068 and p0070–p0072), p0069 needs_review for the faded subtitle only. Current total: 66 verified, 6 needs_review, 64 pending p0073–p0136; 0 draft/rendered/invalid. Reconcile and partial build passed, `build_current: true`. This is WIP/INCOMPLETE, not acceptance.
- Current `book.md` SHA-256: `0a6d1525f0927ea588e06754631f86b4b8329a7378dec2f35124e6d7001279e2`; `search.jsonl`: `976dffe212ff3662f36464d3cb2706cb32142b16444f975a223c56c5805e2864`.
- Every new page was opened as full2x source image and direct6x upper/lower crops, then read back against Markdown. Extra tight crops: p56 Chinese (`切掉电源`, corrected from draft misread); p58 Chinese; p64 Chinese (`签、证护照`, source oddity retained); p67 direct8x original/contrast subtitle `〜もしも遅刻したら〜`; p69 direct8x subtitle/contrast and watermark. Cache/scratch only under `.cache/renders/<book_id>/scratch-cont2*`; no image output in corpus.
- Other source oddities retained: p57 English labels the second paragraph `e.` rather than Japanese/Chinese `d.`; p58 Chinese② prints `注意不要不影响他人`; p65 Chinese `发表看法` corrected during reverse review. English line-end hyphens retained, including con-veyance/per-sonal/man-ner/of-ficial/cas-es/permis-sion/impres-sion/fa-vor/de-pending. P70 has one actual ruby occurrence `尋＝たず` in m, no inferred ruby added elsewhere.
- Cross-page joins verified: p64 English h ends `hurry back`, continues p65 `to the office as soon as possible.`; p68 English f ends `docu-`, continues p69 `ments, or taking memos.`. Translations b for p63 are printed on p62; g for p68 is printed on p69; p/q for p70 are printed on p71. Content kept on its physical source page.
- P72 is truly blank with no printed number/title/text/meaning-bearing image; full image and direct6x crops inspected twice. Described as editorial blank-page note.
- Next pending independent page is p0073. Earlier source issues p1/p3/p20/p23/p27 unchanged. Seven accepted books, other active books, tools/skills and source PDFs untouched; no Git stage/commit. Claim owner `production_book_10_sol_cont2` releases token `production_book_10_sol_cont2_20261111_c42b` after this handoff.



## Continuation checkpoint — PDF p0073–p0092 (production_book_10_sol_cont3)

- Batch coverage: all 20 physical pages p0073–p0092 verified with individual source/render/Markdown hashes and concrete evidence. Current total: 86 verified, six older needs_review (p1/p3/p20/p23/p27/p69), 44 pending p0093–p0136; zero draft/rendered/invalid and zero validation errors. Reconcile/build passed; `build_current: true`. This is WIP/INCOMPLETE, not acceptance.
- Current `book.md` SHA-256: `4766c0456745f7e0a239ed57a5b856fc3385cf9d6ebbc1f33d4f6ec2932a68ad`; `search.jsonl`: `665fe5a58a24d432c14a63d70f4e4a349eaff600be144afe705366bdf51e1590`; `build.json`: `ba54a160d24939ffcb651417890841f9d8f6405d23e708da0d6b707142ff5476`.
- Every page opened full2x and direct6x upper/lower (p73 uses its title crop). Extra direct8x crops for comics p78/p84/p90, p83 faded subtitle original/contrast, each odd page inactive edge tabs, p80 Chinese a, p81 Chinese f, p88 sound/Chinese and p89 name. Source p83 subtitle reads `〜日本茶の正しい出し方〜`. All images/crops/scratch are ignored cache only, prefix `scratch-cont3-*`.
- Inactive right tabs on odd pages p75/p77/p79/p81/p83/p85/p87/p89/p91 read individually and recorded as `第一章 日本の一般マナー／第二章 日本のビジネスマナー／確認問題`. P75 was freshly reverified after adding inactive tabs. Source typography/wording preserved: p74 answer says `名刺をもらった後の移動`, whereas p78 heading says `名刺をもらった後の行動`; p81 Japanese c label uses a colon. P83 Chinese i says `不要垫茶托` despite JP/EN distinction; p87 Chinese a prints `不附和`.
- Final reverse review p88 used direct12x tight CN crops: sound phrase is source `卡叽卡机`, with final 木-radical `机`, not repeated `叽`. Corrected initial draft, re-recorded/reverified p88 and rebuilt. P88 comic has `ゲフッ`, prose `ゲップ`. No unresolved source issue arose in this batch.
- Furigana occurs only where printed: p78 quoted `道明寺＝どうみょうじ` in panel3; p83 `茶碗＝ちゃわん`; p85 `経＝た`; p86 `箸＝はし`; p87 `椀＝わん`; p88 `噛＝か`; p89 `完璧＝かんぺき`. No inferred readings on repeated names/words.
- Cross-page join checked: English m at p76 ends `ac-`, p77 starts `cept his with your left.`. Kept split on source physical pages with editorial join notes. All other sentences in this batch end on their page; p92 starts Unit14 quiz and has no prose continuing to p93.
- Next independent pending page: PDF p0093. Source SHA remains `0e3d5e9467fafaef97acda677080aa1bb6f9b849aa20e5993172ee6b0864d7a6`. Claim `production_book_10_sol_cont3` / `book10-cont3-20261111-73c41f` is released after this handoff. Earlier six source issues, other books, source PDFs, tools/skills and global production files untouched. No Git stage/commit.


## Continuation checkpoint — PDF p0093–p0112 (production_book_10_sol_cont4)

- Batch coverage: all 20 physical pages p0093–p0112 verified with individual source/render/Markdown hashes and concrete evidence. Current total: 106 verified, six older needs_review (p1/p3/p20/p23/p27/p69), 24 pending p0113–p0136; zero draft/rendered/invalid and zero validation errors. Reconcile/build passed; `build_current: true`. This is WIP/INCOMPLETE, not acceptance.
- Current `book.md` SHA-256: `5afcb92bd147d4eff535f5304f8079ba6493feca136f2a77dd79636d814bd18f`; `search.jsonl`: `026ce007925e0ccb17e43e6bad3799bdc5fde4c6d2ef8d4c430561e89dcd7112`; `build.json`: `86be7cdecaf0668740e920a69da07eb3eee47a5dc857a197cb700183453a9dd1`.
- Every page opened full2x plus direct6x top/bottom; every odd-page edge opened as a separate crop. Extra direct8x crops: p99 Chinese and bubbles; p101 subtitle/comic; p102 Chinese; p105 template; p110 Chinese; p111 subtitle/labels/comic/tight thought; p113 English join only. Images/scratch exist only in ignored cache with `scratch-cont4-*` prefix. No image assets in corpus.
- **Source printed-page gap:** physical PDF p0105 has printed folio103; physical p0106 has printed folio106. Printed104–105 are absent from this PDF at this transition, so the template explanations for Unit16 are missing from the source. Physical IDs and actual folios were retained; no missing text or synthetic pages created. Coordinator independently confirmed this source gap. This book must not be represented as a complete reproduction of missing printed pages even if all136 physical pages eventually pass.
- Seating exercises p93–96 and answer diagrams p97 are text-only descriptions preserving doors/windows/table/chair positions, empty boxes or printed ranking numbers, driver exclusion, train motion/facing directions and elevator arrow positions. No exercise was solved beyond the source answer page. P105 includes all email UI labels, nine arrow references and actual template strings; attachment filename is literal text, not an image link.
- Source oddities retained: p97 Japanese `後は窓際`; p99 Chinese `将寒暄礼后电话中所听事情`; p101 caller `MDT`/`七田` vs response/memo `NTD`/`イチダ`/`市田`; p103 sample memo spells `MTDセキュリティ` and `シチダ`; p102 Chinese `一边` in k; p110 Chinese e body begins `司安排工作时` without 上. No repair inferred. Faint subtitles read as p101 `〜取り次ぎって難しい〜`, p111 `〜コピー取ってきて〜`.
- Exact ruby in this batch: p102 sidebar `綴＝つづ`; p104 first answer option `宛先＝あてさき` only. Parenthetical numerical readings in p101/p102 are source parentheses. P111 劉 labels/bubbles have no ruby; none invented.
- Cross-page relations checked: f/g translations p96, Japanese p97; a–c translations p98, Japanese p99; i/j translations p101, Japanese p100; m translation p103, Japanese p102; a–d translations p106, Japanese p107; f/g translations p111, Japanese p110. English m p112 ends `no blank`, continues p113 `pages are mixed in.`. P113 was opened full2x and tight8x only for this join and remains pending/untranscribed; next worker must process all of p113.
- Source SHA unchanged: `0e3d5e9467fafaef97acda677080aa1bb6f9b849aa20e5993172ee6b0864d7a6`. Next independent page p0113. Earlier six source issues, other books, source PDFs, tools/skills and global production files untouched. No Git/stage/commit. Owner `production_book_10_sol_cont4` releases token `book10-cont4-20261111-93d65b` after this handoff.
