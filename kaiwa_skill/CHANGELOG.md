# Changelog

## 0.2.0 — 2026-11-10

- Theo yêu cầu người dùng, corpus và bài luyện kaiwa chỉ có text; hình mang nghĩa được diễn đạt bằng văn bản có nhãn biên tập.
- Ảnh render chỉ là cache phục vụ đối chiếu PDF. Giữ hồ sơ hash bằng text, cho phép dọn cache sau xác nhận và tạo lại khi cần.
- Chuyển pilot hiện có sang chế độ text-only; bỏ PNG khỏi cây Git hiện tại, giữ lịch sử commit cũ.

## 0.1.2 — 2026-11-10

- Sau rà soát pilot, chuẩn hóa nhãn biên tập cho chữ trong hình, tiêu đề lề và tiêu đề nối trang; phân biệt rõ phần thêm để tổ chức Markdown với nguyên văn sách.

## 0.1.1 — 2026-11-10

- Chỉ mục giữ ngữ cảnh unit/trang cho từng khối nội dung.
- Hash tài sản liên kết được ràng buộc vào hồ sơ đối chiếu và bản build; sửa crop làm mất hiệu lực xác nhận cũ.
- Bổ sung kiểm thử tương thích hồ sơ trang chỉ có chữ và phục hồi sau thay đổi asset.

## 0.1.0 — 2026-11-10

- Hai skill điều phối và xử lý từng sách, Astra/high xây dựng và Sol/high chuyển đổi.
- Quy trình đối chiếu từng trang, trạng thái bền vững, phục hồi và kiểm tra hash.
- Markdown bảo toàn nguyên văn, nguồn truy ngược, pilot trước production và commit riêng từng output.
