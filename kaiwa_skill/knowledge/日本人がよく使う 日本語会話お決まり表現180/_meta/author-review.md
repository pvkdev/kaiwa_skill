# Author review — toàn bộ PDF 1–209

- Đã mở ảnh từng trang vật lý PDF1–209 và đối chiếu nội dung đã viết với sách. Mỗi trang có evidence và checkpoint hiện hành; không còn pending, draft hoặc stale.
- Giữ đủ 180 đầu mục số 1–180, 180 cặp Listen & Speak 1/2 (mục 178 phần 2 là lời phát biểu một người), 50 cột Useful One-word Expressions và các chú từ chân trang. Cột 29 ở PDF129 in nhãn số 3, cột tại PDF161 in số 36; giữ nhãn nguồn, có ghi nhận trong editorial log.
- Bảng tra tiếng Anh PDF200–204 giữ 212 khóa tra (43/40/42/42/45 theo trang), mỗi khóa có biểu thức Nhật, nghĩa Việt và trang in. Bảng tra tiếng Nhật PDF205–207 giữ đủ 180 biểu thức và trang in, theo thứ tự tra chữ Latin của sách.
- Hậu sách PDF208–209 giữ thông tin tác giả, người tham gia, mốc in, ISBN và hai câu ví dụ Nhật–Việt trên bìa sau. Audio inventory ghi icon CD 1–90 theo trang và block, thông tin ấn bản/ISBN, CD và lời dẫn tải in trên bìa; file nghe thực tế chưa kiểm. Cuối sách không thấy URL hoặc mã tải riêng.
- Hai vấn đề nguồn còn mở: PDF53/mục34 và PDF168/mục149 đều in vai A/A trong hội thoại Nhật nhưng A/B ở cột Anh. Câu Nhật và phần Việt đã giữ, vai chưa tự sửa; page, unit và chapter liên quan có `needs_review`. PDF103/mục84 có lỗi cột Anh nhưng lượt Nhật rõ, đã ghi editorial correction và kiểm lại.
- Build full tạo 31 chapter, 200 unit; `validate --allow-source-issues` báo 0 lỗi, 4 cảnh báo tương ứng hai vấn đề nguồn ở page và unit. Chế độ strict không được tuyên bố đạt khi hai vấn đề chưa giải quyết.

Đây là self-audit của tác giả bản clean; root kiểm độc lập theo các trang mẫu và sẽ QA cuối/Git riêng.

## Bổ sung của root sau handoff

Số212 khóa English ở self-audit phía trên đã được thay thế sau khi root mở lại toàn ảnh200–204: nguồn có218 khóa, theo trang43/43/42/45/45. Root khôi phục sáu khóa bị OCR bỏ và sửa một khoảng trắng trong Bottlenecked; mọi khóa nối đúng180 đầu mục và trang đã in. Japanese index vẫn180 mục. Đây là sửa của root, không phải xác nhận tác giả đã đếm218 trong lượt đầu. Root checkpoint/build/validate lại sau sửa; hai vấn đề vai nguồn53/168 vẫn giữ.
