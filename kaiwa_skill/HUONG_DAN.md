# Vận hành kho nguồn kaiwa

Mở Codex tại gốc repo (thư mục có AGENTS.md, bunpou_skill và kaiwa_skill). Skill được lưu trong `.agents/skills/` ở gốc repo. Mọi thao tác PDF dùng thư mục con kaiwa_skill.

## Các yêu cầu có thể gửi cho coordinator

- “Dùng $kaiwa-ingest xem status toàn bộ kho, số trang nháp, số trang đã đối chiếu và lỗi còn lại.”
- “Dùng $kaiwa-ingest tiếp tục sách BOOK_ID từ checkpoint; worker Sol/high.”
- “Dùng $kaiwa-ingest chạy pilot theo phạm vi đã chọn, kiểm tra bằng Astra/high rồi commit output pilot.”
- “Dùng $kaiwa-ingest chạy toàn bộ hàng đợi với hai worker Sol/high, mỗi worker một sách; commit từng sách nghiệm thu.”

Coordinator đọc dispatch.json và chọn model trong lệnh tạo tác nhân. File cấu hình không tự khởi động tác nhân. Đóng ứng dụng/phiên làm việc có thể ngừng xử lý; các checkpoint vẫn nằm trên đĩa và được dùng khi yêu cầu tiếp tục.

## Đọc kết quả

- `corpus/catalog.json`: kiểm kê nguồn, số trang và dấu vân tay PDF.
- `corpus/<book_id>/manifest.json`: định danh sách và checkpoint tổng hợp.
- `corpus/<book_id>/pages/pNNNN.md`: nội dung một trang PDF.
- JSON cùng trang: trạng thái, hash và hồ sơ đối chiếu.
- `book.md`: bản ghép các trang đã xác nhận; nhãn INCOMPLETE khi chưa đủ sách.
- `search.jsonl`: nội dung và nguồn cho công cụ truy xuất; không phải chỉ mục embeddings.
- `build.json`: dấu vân tay bản ghép/chỉ mục; phải kiểm tra còn current trước khi dùng downstream.
- `pilot/REVIEW.md`: kết quả đánh giá pilot, lỗi, sửa đổi và phạm vi được kiểm tra.

Đọc `tools/USAGE.md` để chạy CLI và khôi phục quyền sở hữu bị bỏ lại. Không tự xóa lock khi tác nhân cũ còn hoạt động. Một trang chỉ verified sau khi đọc ảnh và đối chiếu; số lượng verified không đại diện cho đánh giá độc lập toàn sách.

## Phiên bản

Skill và output có commit riêng. Commit ở máy này; không tự push remote. Các file đã lưu nhưng chưa commit vẫn có thể resume trên máy hiện tại; commit dùng cho lịch sử và phục hồi qua Git. Nguồn PDF và bunpou chỉ đọc.

Giai đoạn này bảo toàn nguồn sách. Topic, level, tình huống mới, lộ trình học và dữ liệu app sẽ được xây bằng quy trình sau, dùng nguồn đã nghiệm thu.

Đầu ra chỉ có text (Markdown, JSON, JSONL). Ảnh PDF chỉ được render tạm để AI đọc và đối chiếu, không nằm trong corpus bàn giao hoặc commit. Có thể xóa cache mà vẫn sử dụng và tìm kiếm text đã verified; khi cần kiểm tra lại, render từ PDF gốc. Các bài luyện kaiwa về sau cũng diễn đạt bối cảnh, vai và tình huống bằng text.
