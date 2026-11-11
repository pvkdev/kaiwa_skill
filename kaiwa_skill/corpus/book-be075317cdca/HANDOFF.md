# Bàn giao sách シャドウイング 日本語を話そう 初・中級編

- Nguồn: `kaiwa_skill/book/Shadowing/シャドウイング 日本語を話そう初_中級.pdf`
- SHA-256 nguồn: `be075317cdcab1bad0245126bf7c4fe9bb066fcb714bc19aa841f5373b612869`
- Book ID: `book-be075317cdca`; 145 trang vật lý.
- Worker lượt này: `production_book_13_root_cont2`; claim `production_book_13_root_cont2_20261111` đã release sau checkpoint.
- Checkpoint sau p0116: **56 verified, 60 needs_review, 29 pending (p0117–p0145), 0 rendered, 0 draft, 0 invalid**. Trang tiếp theo là **p0117** (Unit 5 section 3, phần tiếp theo tiếng Nhật). Mỗi p0088–p0116 đã render, mở toàn trang, crop chữ/ruby nhỏ, record và checkpoint.
- `reconcile` và `build` thành công sau p0116. `book.md`, `search.jsonl`, `build.json` phản ánh 56 trang verified; `book_sha256: 3d8f2a92bef60bc0340734de193ab6bc51ea526b9f89e9e9dfb22edbcffc5e06`, `search_sha256: 38443f2bdcd10974c01d096db2b6420c875892b8c4b752b2dace900b9f50d7eb`. `transcription_complete: false`, `acceptance: coordinator_review_required`.

## Cách làm và trạng thái review

Mỗi trang p0001–p0116 đã mở ảnh trang gốc riêng; crop khi cần để đối chiếu ảnh→Markdown và Markdown→ảnh, gồm văn bản, ruby, nhấn mạnh, bảng, nhãn vai, track, khoảng trống và ngắt trang. Bản nháp/evidence và ảnh render nằm trong `.cache/renders/book-be075317cdca/`; corpus chỉ chứa văn bản, không nhúng ảnh. Worker verified chỉ là checkpoint sản xuất; coordinator nghiệm thu độc lập.

Các trang `needs_review`: p0008, p0012, p0015–p0018, p0020, p0024 và các trang chẵn kế tiếp trong bài học, cùng p0045–p0046, p0065–p0066, p0083–p0086. Xem issue chính xác theo từng trang trong `manifest.json`; không nâng trạng thái chỉ vì đã có bản nháp.

- **Mẫu in cực nhỏ:** p0008, p0012, p0016, p0020 chứa cùng dạng trang mẫu thu nhỏ. Hội thoại và ba cột dịch không đủ rõ để chứng thực từng ký tự, kể cả sau render/crop lớn; phần văn bản, callout và bảng đọc được đã giữ trong draft. Đây là giới hạn kích thước của mẫu in nguồn, tách biệt với vấn đề tiếng Thái.
- **Tiếng Thái:** nhiều trang bản dịch/giới thiệu in rõ, có draft phần đọc được, nhưng worker không thể chứng thực toàn bộ ký tự, nguyên âm và dấu thanh. Cần người đọc tiếng Thái rà chính xác theo ảnh nguồn, đặc biệt p0015–p0018 và các trang bài học. Tesseract cài sẵn với model `tha`: chế độ `psm 6` toàn trang làm rơi nhiều dấu; `psm 7` trên crop từng dòng cho draft tốt hơn nhưng vẫn sai. Không gọi các trang này là PDF hỏng/mờ; không sửa theo suy đoán từ bản Nhật/Anh.
- **p0085:** ruby tiếng Nhật đã rà lại từng lần xuất hiện theo crop nguồn scale 6, loại ruby thừa; root đối chiếu xác nhận 32 mục đúng nguồn. Trang vẫn `needs_review` riêng tiếng Thái; không nâng trạng thái vì review ruby.
- **Source quirks:** p0065 lời giải tiếng Indonesia mục 6 và 7 trùng nhau ngay trong bản in; giữ nguyên. p0064 dòng cuối tiếng Việt in nhãn `B`; giữ nguyên. p0074 dòng Thai row 2 B đã crop xác nhận không có `นี่`. Một số từ Latin bị ngắt dòng với gạch nối trong nguồn; xem note tại trang trước khi chuẩn hóa.
- **Lượt p0088–p0116:** các trang tiếng Nhật p0089, p0091, p0093, p0095, p0097, p0099, p0101, p0107, p0109, p0111, p0113, p0115 đã `verified`. p0103–p0104 là trang giải thích đa ngữ, p0105 là Column 2, p0106 là đầu Unit 5; tất cả đã có draft text đầy đủ và `needs_review` chỉ ở chữ Thái nhỏ. Các trang bản dịch chẵn p0088–p0102 và p0108–p0116 cũng có draft đầy đủ, `needs_review` có issue cụ thể trong `manifest.json`. p0104 có banner nhà phân phối được chép. p0110 mục 10 và p0116 mục 7: cột Việt thiếu nhãn vai ở câu cuối ngay trong bản in, nên để câu không nhãn và ghi chú biên tập. p0108 mục 5: Indonesia “mengopy-” bị ngắt dòng trước “nya”, đã nối thành “mengopynya”, issue yêu cầu QA xét gạch nối. Không diễn giải khác bản Nhật hay tự giải bài.

## Tiếp tục

Claim mới, kiểm hash nguồn, mở p0117 trước khi record; tiếp tục từng trang đến p0145. Sau đó xử lý `needs_review` theo issue cụ thể, reconcile/build, rồi coordinator QA/acceptance. Không sửa `ROOT_AUDIT.json`, nguồn PDF, tools hoặc Git trong vai worker. Khi handoff, root đang giữ QA/Git và có thể tạo worker mới sau khi claim hiện tại release.
