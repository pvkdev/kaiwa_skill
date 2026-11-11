# Clean hàng loạt — điều phối đang hoạt động

Root giữ lượt điều phối và đúng ba worker `gpt-6-sol/high`. Ingest và clean chạy ở thư mục riêng; chỉ nhận sách có nguồn sẵn sàng.

Đã build bản đọc toàn phạm vi PDF đầu vào và kiểm cấu trúc không lỗi/cảnh báo (501 trang trong bảy nguồn):

- 日本語生中継 初中級編1: 91 trang, 13 chương, 253 unit; đã rà độc lập toàn bộ ảnh/raw/clean.
- 日本語生中継 中～上級編: 89 trang, 11 chương, 122 unit; đã rà độc lập toàn bộ ảnh/raw/clean.
- TỔNG HỢP880 TỪ VỰNG MIMIKARA N3: 47 trang, đủ880 dòng; giữ cách đọc và Hán Việt.
- Danh sách1160 từ vựng MINATO DORIMU: 8 trang, đủ1160 mục; nguồn thiếu số460 và có1161, không tự sửa.
- 外国人のための日本語敬語の使い方 基本表現85: 93 trang, 9 chương, 116 unit; 15 unit còn vấn đề nguồn. PDF gốc thiếu trang in106–107/bài14; không tự phục dựng.
- TỔNG HỢP1170 TỪ VỰNG MIMIKARA N1: 70 trang, đủ1170 dòng; 306 ô Kanji và 328 ô Hán Việt trống được giữ nguyên. Hai unit có nghĩa nguồn đáng ngờ giữ needs_review.

Root review ảnh theo mẫu, kiểm toàn bộ dữ liệu bảng bằng script; mỗi sách ghi rõ giới hạn ở `_meta/coordinator-review.md`. Không gọi mọi bản dịch đã kiểm độc lập toàn bộ. Trạng thái full nghĩa là đủ PDF được cung cấp, không đảm bảo PDF vốn có đủ mọi trang của sách in hoặc có CD/kịch bản riêng.

- 日本語でビジネス会話 中級編〈英訳・語い冊〉: 103 trang, 21 phần, 145 unit; hội thoại chỉ có English trong tập được dịch Việt, không tạo thêm lời Nhật.

Đang chạy tiếp:

- `/root/clean_namachuukei_sho`: independent QA toàn sách kính ngữ 基本表現85.
- `/root/clean_namachuukei_chu`: rà và khôi phục phần học/track của pilot 基本文型88, chỉ PDF7–12.
- `/root/clean_keigo`: independent QA toàn bảng880 từ N3.

Trạng thái máy và ownership: [COORDINATOR.json](COORDINATOR.json). Hướng dẫn tiếp quản: [HANDOFF.md](HANDOFF.md). Checkpoint từng sách ở `_meta/clean-state.json`; nguồn ghim ở `source_snapshots/`, ngoài knowledge. Sau gián đoạn, xác nhận worker cũ dừng rồi chạy clean_progress.py resume, không xóa tiến độ hoặc init lại.
