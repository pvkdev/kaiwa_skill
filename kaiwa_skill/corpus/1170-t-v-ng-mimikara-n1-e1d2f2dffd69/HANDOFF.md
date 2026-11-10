# N1 production handoff

- Worker/claim: `production_book_03`, token `production_book_03_20261110_a7f2`.
- Source: `vocab/1170 TỪ VỰNG MIMIKARA N1.pdf`, 70 physical pages, SHA-256 `e1d2f2dffd69aadc03a195bd23564f29a481fbfd8bc43accf9715a9f16c38ba0`.
- Final checkpoint (2026-11-10 UTC): all pages 1–70 verified; no open `needs_review` issues; current build; claim released. Sequence check found exactly 1170 table rows, numbered 1.–1170. continuously. Coordinator accepted; see `REVIEW.md` and hash-bound `acceptance.json`.
- Scratch: `kaiwa_skill/.cache/production_book_03/` contains per-page TSV drafts, generated Markdown, crop images, evidence JSON and temporary scripts. Render cache: `kaiwa_skill/.cache/renders/1170-t-v-ng-mimikara-n1-e1d2f2dffd69/`.

## Visual review actually performed

Opened every full-page 150 DPI PNG for pages 1–70. For every page, separately opened top and bottom crops of the same PNG. Full-image and crop observations sometimes differed for the printed Shakespeare quote or Fanpage footer; the cause remains unresolved, so the crops were independently checked against the source. Rendered a 300 DPI middle-column crop for every page to inspect Vietnamese diacritics over the watermark. Checked all table rows, empty cells, printed boundaries, top/bottom blue `MINATO DORIMU` bars, watermark, quote and footer; compared each draft to the images before page-specific evidence and verify. Pages 61–70 also got enlarged Japanese-column crops; pages 67–70 got 300 DPI meaning-column crops for punctuation. The PDF has no useful text layer; transcription is manual from images.

Following coordinator findings, independently reopened enlarged 300 DPI Japanese columns on p39–41 and p54–56 and compared all 102 rows character by character, including trailing kana. Also reopened enlarged Vietnamese columns on p15–17 and p66–70 and compared all 120 rows for diacritics and punctuation. The discrepancies found were p55 row 923 and p67 row 1120, both corrected and reverified; p40 row 674 and p16 row 261 had already been corrected.

## Source oddities worth audit

- p4 row 58 Hán Việt `ÔI` confirmed by 300 DPI crop; p20 row 320 `ÁM KÌ`.
- p9 row 135 `をひずく` beside `築く`; p29 row 473 `をひきしめる` beside `引きずる`.
- p13 row 211 `PHẠP`; p16 row 261 meaning `Đanh đá` confirmed by coordinator crop from a 150 DPI PNG enlarged 1.5× and an independent 300 DPI Vietnamese-column crop (initial draft had `Danh đá`, corrected and reverified); p17 row 273 `k rõ ràng`.
- p22 row 360 `PHẢN ẢNH]`; p38 row 638 `XUNG KÍCH]`; p40 row 665 `SÚC TÍCH]`. Brackets are printed.
- p36 row 594 `ĐÃN`; p38 row 630 `THANH VIÊN`; p40 row 676 `SĨ QUẢI`.
- p40 row 674 `はあく/把握` confirmed by 300 DPI tight crop (initial draft omitted は, corrected and reverified).
- p51 row 853 meaning `khoông trách nhiệm, bông đùa`; p52 row 867 Hán Việt wraps `MÔ PHẠM ĐÍCH`; p53 row 890 wraps `THỦ TRÌ VÔ SA THÁI`.
- p55 row 923 prints `致命的な` (initial draft omitted な; corrected and reverified); row 931 `主催/CHỦ THÔI`.
- p61 row 1020 `折（り）`, row 1023 `vo ( gạo)`, row 1030 `が/をかまう`.
- p64 row 1068 `をなだめる/募る`, row 1074 `をはたる/謀る`; p64 row 1080 meaning ends with comma.
- p67 row 1120 meaning prints `quýnh lên` (initial draft had `quỳnh lên`; corrected and reverified); row 1122 prints `sự phát ban (trên mặt)`.
- p69 row 1153 meaning is printed with a blank line before a final `thực tế`; row 1159 two forms use a slash.
- p70 has ten final rows ending at 1170. A separate large logo follows the blue table band; the Fanpage footer is visible in a separate crop. The full-image and crop observations differed; the cause remains unresolved.

## Continuation

No pending conversion work. Any future correction requires a fresh claim, record/review, rebuild and coordinator acceptance. Preserve printed source oddities; investigate uncertainty with source crops before declaring a source error.
