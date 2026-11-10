# HANDOFF — 5500 câu giao tiếp tiếng Nhật trong sinh hoạt hàng ngày

- Source: `book/Kaiwa/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hàng ngày.pdf` (136 physical PDF pages).
- Source SHA-256: `c8933782539c7bbe8ac755f2278bb7a6d7cf0d9165843c9ef14a198993b1825a`.
- Output mode: text only.
- Status after `build`: **28 verified, 13 needs_review, 95 pending**; `build_current=true`.
- Next page: **physical PDF p42**; pending interval **p42–p136**.
- Verified physical PDF pages: p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p17, p18, p19, p20, p21, p23, p28, p29, p30, p35, p36, p37, p38, p39.
- Partial output: `book.md`, `search.jsonl`, `build.json` in this book corpus directory; each page has `pages/pNNNN.md` and `.json`.
- Claim owner before release: `production_book_09_sol_resume`; claim token `production_book_09_sol_resume_20261111_0d8a34c9`. This claim must be released at handoff.

## Source issues requiring a better scan

- PDF p1: Contact block is intrinsically blurred; partial labels/website retained but individual addresses and email illegible. Requires better source before verification.
- PDF p16: Printed p30 item 2 at binding edge: Japanese after visible 話さないで and roman after visible hanasanai de are physically obscured/cut off in PDF scan, confirmed at 5x render; local [không đọc được] marks preserve uncertainty. Other text viewed full plus four crops.
- PDF p22: Printed p42 item 10 first Japanese, roman, and Vietnamese lines run into binding edge; final characters of each are obscured in source at 4x render/crop. Partial transcription has local unreadable markers. Requires better source before verification; other regions of pp42-43 read at 4x.
- PDF p24: Printed p46 item 16 expanded expression: ends of Japanese, roman and Vietnamese lines are obscured at the binding edge at 4x render. Partial text and local unreadable markers recorded; better source required for verification. Rest of pp46-47 opened full and quadrants.
- PDF p25: Printed p48 item 7 Japanese, roman, and Vietnamese lines extend into binding edge with final characters obscured. Partial draft marks these spans unreadable. Full spread and quadrant crops inspected at 4x; better source required before verification.
- PDF p26: Printed p50 dialogue and item 13 run into binding edge. Japanese/roman/Vietnamese endings of dialogue and roman/Vietnamese of item 13 are partly obscured at 4x; partial text marked unreadable. Better source required; other regions of pp50-51 opened full and in quadrants.
- PDF p27: Printed p52 item 7 Vietnamese and item 10 Japanese/roman lines extend into binding edge; final characters obscured at 4x. Partial draft marks these unreadable spans. Full spread and quadrant crops inspected; better source required before verification.
- PDF p31: Printed p60 several roman lines in continuation dialogue and section 12 item 1/alternative run into black binding edge. Their ends cannot be read in 4x full/crops. Partial draft marks unreadable spans; better source required. Remaining p60 and p61 opened full and quadrant crops.
- PDF p32: Printed p62 item 8 Japanese, roman and Vietnamese first lines enter black binding edge; end characters unreadable at 4x. Partial draft has local unreadable markers. Full spread and four quadrant crops reviewed; needs a better source before verification.
- PDF p33: Printed p64 item 13 expanded expression roman ending/punctuation enters black binding edge after kakemasu and cannot be distinguished at 4x crop. Draft marks local unreadable span. Other text on pp64-65 opened full and four crops; better source required for verification.
- PDF p34: Printed p66 item 2 expanded Vietnamese, item 3 Japanese/roman, and item 5 Japanese endings are physically obscured at black binding edge in 4x image and crops. Draft marks each local unreadable span; better source required. Remaining pp66-67 opened full and quadrants.
- PDF p40: Printed p78 item 15 Japanese/roman endings, item 19 roman ending, and item 20 Japanese/roman endings extend into black binding edge and cannot be read at 4x full/crops. Partial draft marks local unreadable spans; better source required. Other regions of pp78-79 inspected full and in quadrants.
- PDF p41: Printed p80 item 6 roman punctuation and item 9 Japanese/roman ends meet black binding edge and cannot be distinguished in 4x full/crops. Partial draft marks these local spans; better source required. Remaining pp80-81 inspected full and in quadrants.

## Resume instructions

- Recover/claim using `kaiwa_skill/tools/ingest.py`; reconcile and check source hash before writing.
- Continue at physical PDF p42, then each pending page through p136. The 13 `needs_review` pages already have local partial drafts and issue records. Do not infer text behind the black binding edge.
- Render each page and inspect the full spread plus quadrant crops; compare transcription to image in both directions, including Japanese, romanization, Vietnamese, headings, page numbers and printed furigana occurrence/span. Verify with page evidence only when completely readable; otherwise record partial text with local unreadable markers and `needs_review`.
- Images and scratch drafts for p18–p41 are under `kaiwa_skill/.cache/renders/<book_id>/`; these are temporary reference files.
- Build partial at checkpoints, and run final build/reconcile/quality checks after all pages are processed. No Git operation was performed by this worker.
