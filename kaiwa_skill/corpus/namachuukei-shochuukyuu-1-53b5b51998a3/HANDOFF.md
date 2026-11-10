# Bàn giao sách 日本語生中継 初中級編 1

- Nguồn: `kaiwa_skill/book/Shadowing/Namachuukei Shochuukyuu 1.pdf`
- SHA-256 nguồn: `53b5b51998a3d426fcdbd24e3fe029ed62823255a3de9a431caf50fc33e703d8`
- Book ID: `namachuukei-shochuukyuu-1-53b5b51998a3`
- Số trang vật lý: 91
- Worker ban đầu: `production_book_05`; worker tiếp tục và hoàn tất: `production_book_05_resume`
- Claim worker tiếp tục: `pb05resume-20261110-53b5` (đã release sau build)
- Trạng thái cuối: **91/91 verified, 0 pending, 0 rendered, 0 draft, 0 needs_review, 0 invalid**. `transcription_complete: true`; vẫn cần coordinator nghiệm thu độc lập.
- `book.md`, `search.jsonl` và `build.json` đã tạo từ toàn bộ trang verified. SHA-256 `book.md`: `7e62283e6447591d63b40ab4d9dc3958f36b2917426c837d26351ca5a1990d26`; `search.jsonl`: `a155bc462d4c6eac4b6f9b2fab0170a1c4460bd5daf13dd3cdd5779d939fe5e3`.

## Phương pháp và checkpoint

PDF scan không có text layer hữu ích. OCR chỉ dùng làm bản nháp; trước mỗi lần verify, worker mở ảnh render trang gốc, crop phần chữ/ruby nhỏ, đối chiếu ảnh→Markdown và Markdown→ảnh. Review evidence từng trang ràng buộc SHA nguồn, render và Markdown, ghi reviewer cùng thời điểm. Bản nháp nằm ở `scratch/`, checkpoint trang ở `pages/`; ảnh crop chỉ là cache hỗ trợ kiểm tra. Các trang cũ đã verified giữ nguyên, ngoại trừ lỗi cụ thể phát hiện khi QA rồi record/reverify.

`WORKER_REVIEW.md` ghi đợt rà mở rộng p0024–p0040 và p0041–p0055, gồm từng trang đã xem, correction và hash sau rà. `COORDINATOR_AUDIT.json` do coordinator quản lý riêng; worker không sửa. Coordinator đã lấy mẫu độc lập nhiều trang từ p0001 tới cuối sách, báo các sai khác cụ thể; toàn bộ correction nhận được đến lúc build đã mở nguồn, sửa và reverify. Các trường hợp gần cuối gồm p0069–p0071 (quan hệ panel/ruby), p0074 (heading biên tập), p0078 (span 何), p0083 và p0085 (ruby tự thêm), p0087 (span 水), p0090 (`TAC 日本語学舎`). p0091 đã đọc toàn colophon và crop tiêu đề, tên, thông tin xuất bản, bản quyền, ISBN, dòng cuối trước verify.

Lưu các quirk nguồn, không chuẩn hóa: p0009 chú giải Trung ghi `a~f` dù bài `a~e` và tiếng Bồ có `A pessoa ques esta falando`; p0089 in `くろしお版` trong thân bài. Nhãn hoặc mô tả do biên tập đã đánh dấu rõ. Chưa có issue mở tại thời điểm bàn giao.

## Việc tiếp theo

Coordinator kiểm chéo nghiệm thu, kiểm `status`/`build_current` và commit trong phạm vi được giao. Worker này không commit hay sửa nguồn PDF/skill.
