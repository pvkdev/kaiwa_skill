# Bàn giao sách シャドウイング 日本語を話そう 初・中級編

- Nguồn: `kaiwa_skill/book/Shadowing/シャドウイング 日本語を話そう初_中級.pdf`
- SHA-256 nguồn: `be075317cdcab1bad0245126bf7c4fe9bb066fcb714bc19aa841f5373b612869`
- Book ID: `book-be075317cdca`; 145 trang vật lý.
- Worker lượt này: `production-book13-sol`; claim `production-book13-sol-20261111` đã release sau checkpoint.
- Checkpoint sau p0087: **44 verified, 43 needs_review, 3 rendered (p0088–p0090), 55 pending (p0091–p0145), 0 draft, 0 invalid**. Trang tiếp theo là **p0088**; ảnh p0088–p0090 đã render nhưng chưa mở/đối chiếu/record.
- `reconcile` và `build` thành công, `build_current: true`. `book.md`, `search.jsonl`, `build.json` phản ánh 44 trang verified; `book_sha256: 6f0a248653ad39a8aaa2fcc7d66bc69014fe493f265b33c18fa5a98b99e79374`, `search_sha256: b58cab183f1d01ff8bed92469ea33470675c219f06a21ab91094409a9d4ee9e1`. `transcription_complete: false`, `acceptance: coordinator_review_required`.

## Cách làm và trạng thái review

Mỗi trang p0001–p0087 đã mở ảnh trang gốc riêng; crop khi cần để đối chiếu ảnh→Markdown và Markdown→ảnh, gồm văn bản, ruby, nhấn mạnh, bảng, nhãn vai, track, khoảng trống và ngắt trang. Bản nháp/evidence và ảnh render nằm trong `.cache/renders/book-be075317cdca/`; corpus chỉ chứa văn bản, không nhúng ảnh. Worker verified chỉ là checkpoint sản xuất; coordinator nghiệm thu độc lập.

Các trang `needs_review`: p0008, p0012, p0015–p0018, p0020, p0024 và các trang chẵn kế tiếp trong bài học, cùng p0045–p0046, p0065–p0066, p0083–p0086. Xem issue chính xác theo từng trang trong `manifest.json`; không nâng trạng thái chỉ vì đã có bản nháp.

- **Mẫu in cực nhỏ:** p0008, p0012, p0016, p0020 chứa cùng dạng trang mẫu thu nhỏ. Hội thoại và ba cột dịch không đủ rõ để chứng thực từng ký tự, kể cả sau render/crop lớn; phần văn bản, callout và bảng đọc được đã giữ trong draft. Đây là giới hạn kích thước của mẫu in nguồn, tách biệt với vấn đề tiếng Thái.
- **Tiếng Thái:** nhiều trang bản dịch/giới thiệu in rõ, có draft phần đọc được, nhưng worker không thể chứng thực toàn bộ ký tự, nguyên âm và dấu thanh. Cần người đọc tiếng Thái rà chính xác theo ảnh nguồn, đặc biệt p0015–p0018 và các trang bài học. Tesseract cài sẵn với model `tha`: chế độ `psm 6` toàn trang làm rơi nhiều dấu; `psm 7` trên crop từng dòng cho draft tốt hơn nhưng vẫn sai. Không gọi các trang này là PDF hỏng/mờ; không sửa theo suy đoán từ bản Nhật/Anh.
- **p0085:** ngoài review tiếng Thái, đoạn giới thiệu tiếng Nhật với ruby dày cần kiểm từng lần xuất hiện và phạm vi ruby chính xác. Draft đủ bốn ngôn ngữ đã có.
- **Source quirks:** p0065 lời giải tiếng Indonesia mục 6 và 7 trùng nhau ngay trong bản in; giữ nguyên. p0064 dòng cuối tiếng Việt in nhãn `B`; giữ nguyên. p0074 dòng Thai row 2 B đã crop xác nhận không có `นี่`. Một số từ Latin bị ngắt dòng với gạch nối trong nguồn; xem note tại trang trước khi chuẩn hóa.

## Tiếp tục

Claim mới, kiểm hash nguồn, mở p0088 trước khi record; tiếp tục từng trang đến p0145. Sau đó xử lý `needs_review` theo issue cụ thể, reconcile/build, rồi coordinator QA/acceptance. Không sửa `ROOT_AUDIT.json`, nguồn PDF, tools hoặc Git trong vai worker.
