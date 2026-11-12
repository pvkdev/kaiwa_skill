# Chỉ mục metadata 27 sách

[Topic tổng hợp](TOPICS_ALL.md) · [Mục lục sách/chương](BOOK_GUIDE.md) · [Nhãn nguồn chi tiết](SOURCE_LABELS.md)

27 sách; 486 chương/phần theo bản clean; 539 nhãn topic gộp; 22,110 vị trí index. Ba tập từ vựng chỉ để tham chiếu, ghi trong manifest.

Đã quét cấu trúc toàn văn bằng script và bổ sung metadata bằng ba worker sol/high. Không phải đợt đọc sâu toàn corpus, không khẳng định đã khai phá mọi tình huống ngầm. Level còn sơ bộ; audio là inventory, chưa xác nhận file thực.

Tra cứu: tìm nhãn trong TOPICS_ALL/SOURCE_LABELS hoặc dùng rg trên source_index.jsonl. Dòng index cho book_id/chapter_id/line/anchor; manifest giải chapter_id ra đường dẫn. Một số nhãn được rút gọn còn105ký tự; nội dung đầy đủ vẫn ở nguồn. Khi biên soạn, mở đúng chương và tìm toàn văn trong knowledge để lấy kiến thức đầy đủ, gồm cả từ nằm ngoài nhãn.

Packet ở snapshot prepare hiện tại: 126,754 ký tự JSON theo serializer; đây không phải số token hoặc phần trăm quota. [Ghi nhận lượt chạy](RUN_SUMMARY.json) tách packet lúc giao việc và snapshot có thể bổ sung sau QA. Hash nguồn được kiểm trước build.
