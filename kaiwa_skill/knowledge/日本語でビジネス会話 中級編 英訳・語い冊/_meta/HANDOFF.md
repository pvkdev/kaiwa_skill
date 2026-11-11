# Handoff — 日本語でビジネス会話 中級編〈英訳・語い冊〉

- **Trạng thái:** Đã clean toàn bộ phạm vi PDF vật lý **1–103** theo 21 chapter cố định: phần đầu và Lesson 1–20. `book.json.status` là `full`; 21 chapter đã checkpoint `author_checked`. Đây là tác giả tự đối chiếu, còn cần review độc lập và build/validate của root.
- **Đầu ra:** `chapters/00-bia-muc-luc.md` đến `chapters/20-bai-20-phong-van.md`, `_meta/units.jsonl` **145 unit**, `_meta/page-coverage.json` **103 trang** (102 `author_checked`, PDF103 `excluded_nonlearning`), `_meta/author-review-front.md` và `author-review-lesson1.md` đến `author-review-lesson20.md`.
- **Nguồn pin cố định:** `kaiwa_skill/source_snapshots/03-yuukibui-dd762e3fd201/9d94f2adf7585b0a/a875e0f7`; `book.json.source_markdown` trỏ vào snapshot, `source_pdf` giữ đường dẫn và hash gốc. Cache ảnh: `kaiwa_skill/.cache/clean/03-yuukibui-dd762e3fd201/p-NNN.png`.
- **Vai trò tập:** Đây là tập dịch tiếng Anh và từ vựng bổ trợ **英訳・語い冊**, không phải tập 本文冊. Hội thoại/biến thể chỉ có English được dịch Việt; không tự dựng câu Nhật. Giữ các từ/cụm Nhật thật trong bảng, mạch 20 Lesson theo TOC, số tham chiếu trang và mã bài.
- **Kiểm nội bộ cuối:** 21/21 file chapter, 145 unit ID duy nhất và đủ anchor chapter; mọi raw anchor nội dung PDF1–102 được map đúng một lần, không thừa/trùng; không thiếu trang coverage; mọi chapter checkpoint `author_checked`. PDF103 đã mở ảnh, raw chỉ ghi nhãn trang trắng và watermark, nên loại trừ với lý do/hashes trong coverage.
- **Điểm reviewer cần xem:** `_meta/editorial-log.md` ghi các lệch nguồn Lesson 12, 14, 15, 17, 19 và trang trắng PDF103. Đặc biệt đừng dùng tập này để tái dựng nguyên văn Nhật của tập 本文冊.
- **Bước tiếp theo của root:** build `book.md`/search rồi validate và review độc lập. Worker không tự build hoặc Git theo phân công.
