# Tiếp quản công việc clean

Snapshot hiện tại: **29/30 PDF, 4.364/4.597 trang đã release**. Dùng COORDINATOR.json và checkpoint thật để tiếp, không init/reset sách. User chọn `gpt-6-sol/high`; ba worker medium không resume.

Việc còn lại là cuốn **すぐに使える 日本語会話 超ミニフレーズ 発展210**, nguồn SHA `2fdf1586c2e2673f6b27b93fcf3c04c8584567fdd3c2258bcdd0033743de2b05`, 233 trang/16 chương. Keigo là writer duy nhất, đang build/validate; sho kiểm độc lập chỉ mục PDF226–231 (320 dòng); chu đã xong targeted QA16 cảnh cuối. Không release trước handoff + QA chỉ mục + root review.

Toàn210 đầu mục có926 cảnh sau phục hồi16 cảnh bị rơi. Báo cáo counts `.cache/root-live-qa/mini210-scene-coverage-independent.json` SHA `e007466b722c3463dff156867d355b649576f10d6b0a8be37ddd551e801595a0`. Báo cáo16cảnh `.cache/root-live-qa/mini210-restored-scenes-independent.json` SHA `3d233bdeef41af736d0e30c6337bc8e30a45c234114e3f623e4ab79a5fb21cf4`;4finding h141/144/147/180 đã sửa/readback. Giữ PDF75/207 vai A/A là source issue hẹp. Root đã mở30 trang nguồn:1–3,10–14,16–25,75,125,224–233; tail209/210 đã đọc output khớp5+6cảnh. Chỉ mục nguồn6trang đã mở; chờ reviewer đối chiếu320row. Audio210occurrences/198unique disc-track, reportfe3f28... nằm cache; filesnot_checked. Sauhandoff lưu các reportJSON vào _meta và lập coordinator-review, build/validate theo skill nếu nội dung thay đổi.

Onomatopoeia220 đã release `38c623b`, bookSHA `2896e5c247126d69cedaebcb8f9942dd63841458d21922135d0123be3d5d2d9b`; root37trang và các audit index/audio/15head độc lập đã lưu _meta. Mini200 release `e82b3b1`, audit counts995/995 bổ sung `746b475`; nội dung học không đổi.

Công cụ navigation `40eb2c2`,82fork+17direct PASS và2root regression PASS. Rebuild nav-only `617d903` cho125vàFeel180:370liên kết, chương/units/search/evidence/audio giữ nguyên. Bookhash mới và lịch sử trong _meta/coordinator-review.json + NAVIGATION_REBUILD.json. Không coi rebuild này là rà nghĩa mới.

Git dùng chung ingest: chỉ root commit exact paths bằng `--only`; không add., reset, push hoặc chạm PDF/corpus/claims/bunpou/production. Cache/renders không đưa vào knowledge. Chỉ MD/JSON/JSONL trong đầu ra. Dùng PowerShell, PYTHONUTF8=1, py -B, pymupdf as fitz; không cài PIL. Validator không chứng minh đủ nghĩa; phân biệt author_checked với independent QA.

Catalog helper root: kaiwa_skill/.cache/root-live-qa/sync_catalog.py --release BOOKDIR ACTUALCOMMIT. Guard review hash/errors0; không dùng literal HEAD. Cập nhật COORDINATOR/README/AUDIO_INDEX và STATUS/HANDOFF sau quyết định nghiệm thu. Kết thúc khi đủ30PDF/4597trang và các finding đã xử lý; không final ở mốc29.
