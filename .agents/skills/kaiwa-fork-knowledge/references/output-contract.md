# Hợp đồng đầu ra cho mọi fork

## Nội dung và file

Mỗi sách có thư mục `kaiwa_skill/knowledge/<tên sách hợp lệ trên Windows>/`, chứa `chapters/*.md`, `book.md` và `_meta/`. Chapter là nguồn nội dung học sạch; `book.md` được build từ chapters theo thứ tự trong metadata, không sửa trực tiếp. Bản partial phải có phạm vi rõ trong `_meta/book.json`, không để người đọc hiểu là đã xử lý toàn sách.

Mỗi đơn vị nội dung có anchor HTML và `unit_id` ổn định. Không đặt ID dựa vào cấp độ/topic tự suy. Phần hội thoại/ví dụ Nhật và bản Việt dùng `**JP:**` rồi `**VI:**` liền nhau về thứ tự, có dòng trống ngăn hai paragraph để Markdown hiển thị rõ; từng lượt hội thoại dùng `**A (JP):**` / `**A (VI):**`, `**B (JP):**` / `**B (VI):**` theo đúng vai nguồn. Phần giải thích thuần Việt không cần tạo cặp giả. Giữ cấu trúc thực có của sách, không ép mọi sách vào bốn chapter của pilot.

`_meta/book.json` ghi title thật từ bìa/trang nhan đề, `source_pdf` và `source_markdown` dạng `{ "path": "...", "sha256": "..." }`, `scope.pdf_pages` là danh sách số trang PDF vật lý 1-based, `scope.chapters` là danh sách chapter paths theo đúng thứ tự build, và `status` cho biết partial/full. `source_pdf.path` và `source_markdown.path` tính từ **gốc repo**; chapter paths tính từ **thư mục sách**. Tên thư mục đã sanitize không được thay thế title thật trong metadata. Nếu nguồn PDF/corpus đổi hash, phải đối chiếu lại phần liên quan trước khi xác nhận.

`_meta/units.jsonl` có một dòng JSON cho mỗi unit. Các trường tối thiểu: `unit_id`, `chapter`, `heading`, `source`, `review_status`, `issues`. Mỗi phần tử `source` có `pdf_page` (số vật lý), `raw_page` (đường dẫn Markdown trang tương đối **gốc repo**) và `raw_anchors` (mảng anchor đúng trong file trang đó). Ghi đủ trang/khối raw thực dùng, không ghi nguồn chỉ vì nằm gần nội dung. Trạng thái author tự đối chiếu không đồng nghĩa reviewer độc lập đã xác nhận. Chỗ không chắc ghi `issues` và hồ sơ biên tập, không giấu bằng cách đánh dấu verified.

Hồ sơ biên tập/review ở `_meta/`: ghi quyết định lọc, dịch, sửa sai raw từ PDF và vùng/anchor đã đối chiếu; phân biệt lỗi raw/OCR với mâu thuẫn thật ngay trong PDF. Reviewer độc lập ghi kết quả riêng. Tên file chi tiết có thể theo kế hoạch từng sách.

Sau khi chapters, `_meta/book.json` và `_meta/units.jsonl` sẵn sàng, chạy `py .agents/skills/kaiwa-fork-knowledge/scripts/build_fork.py <thư mục sách>` rồi `py .agents/skills/kaiwa-fork-knowledge/scripts/validate_fork.py <thư mục sách> --repo-root <gốc repo>` (hoặc Python tương đương). Builder tạo `book.md`, `_meta/search.jsonl`, ghi hash chapter/units/book/search, số unit và phép hạ cấp heading vào `book.build`; nó không nâng trạng thái review. Validator kiểm cấu trúc, cặp JP/VI và dấu hiệu sót; cảnh báo của nó cần đọc và xử lý bằng đối chiếu PDF, không tự xóa tiếng Nhật Kanji vì có ký tự Han.
