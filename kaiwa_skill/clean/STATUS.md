# Clean hàng loạt — đang điều phối

Kế hoạch hiện hành: [DIRECT_PLAN.md](DIRECT_PLAN.md). Raw đầy đủ tiếp tục clean; PDF chưa chạy đi thẳng knowledge sau pilot. Kiểm kê đổi luồng: 9 nguồn raw ready, 7 raw dở/có vấn đề nguồn, 14 PDF chưa ingest. Các số này là snapshot; kiểm lại manifest/claim khi giao việc.

Người dùng yêu cầu một sub điều phối và ba worker, tất cả `gpt-6-sol/high`; runtime chỉ cho ba sub active cùng root nên luân phiên vai. Root giữ lượt điều phối, QA và Git; chưa hoàn thành catalog30 PDF.

## Đã có bản đọc và rà độc lập

Bảy nguồn đầu có501 trang PDF, đã build/validate và rà ảnh/raw/clean toàn phạm vi bởi tác nhân khác tác giả hoặc kết hợp reviewer/root. Mỗi sách có hồ sơ chỉ rõ những phần được rà và sửa sau review; không đồng nghĩa mọi nhận xét trong bản in đã được xác minh ngoài sách.

- 日本語生中継 初中級編1:91 trang,13 chương,253 unit; bản Việt đã làm rõ vai và giữ nhánh lựa chọn.
- 日本語生中継 中～上級編:89 trang,11 chương,122 unit; Bài8 kết thúc PDF87.
- Bảng880 từ N3:47 trang; đủ880 dòng. Bốn gloss English được dịch Việt có log; năm cụm nghĩa nguồn còn cần xác minh ở360/543/632/636/682.
- MINATO checklist1160 từ:8 trang; thiếu STT460/có1161 đúng nguồn, không tự thêm cách đọc/nghĩa.
- Kính ngữ 基本表現85:93 trang,9 chương,116 unit;164 đáp án Nhật có Việt đã được root QA. PDF thiếu trang in106–107/bài14;15 unit còn vấn đề nguồn.
- Bảng1170 từ N1:70 trang; STT1132 khôi phụcきっちり（と） theo ảnh, khác raw có log. Hai nghĩa nguồn1159/1165 còn needs_review.
- 日本語でビジネス会話 中級編〈英訳・語い冊〉:103 trang,21 phần,145 unit; thoại English-only dịch Việt, không dựng Japanese. Các chênh lệch nguồn được giữ riêng.

Pilot 基本文型88 chỉ PDF7–12:4 chapter,9 unit; đã khôi phục CD01–03/trang mở PART1/mạch hội thoại trước giải thích/MEMO. Root mở lại đủ6 ảnh và rà bản sửa; vẫn pilot_partial, không gọi full sách.

## Đang chạy

- `/root/knowledge_coordinator`: đã bàn giao contract/công cụ PDF-native; 8 test mới và30 test cũ PASS. Đang idle để ba worker chạy.
- `/root/clean_keigo`: pilot Wakaru đã được root kiểm/sửa và ghi PASS theo hash, vẫn chỉ PDF1/17/18/23/149/152 +PDF9 chứng cứ CD. Đã giao full direct mới cuốn なめらか日本語会話 (tên/ấn bản chờ worker xác minh bìa),163 trang, không tạo raw.
- `/root/clean_namachuukei_sho`: tiếp clean roleplay trung cấp140 trang từ checkpoint PDF1–85, đang Unit5; bổ sung CD/audio inventory.
- `/root/clean_namachuukei_chu`: 本文冊 kinh doanh138 trang đã author-check PDF1–35; đang tiếp từ PDF36. Không làm lại.

Review roleplay trước khi đổi luồng chỉ mới mở một số trang phần đầu, chưa xác nhận chapter độc lập. Nghiệm thu tương lai phải dựa hash/output hiện tại, không dùng trạng thái cũ làm bằng chứng.

Pilot trực tiếp đã giữ45key lựa chọn,21câu Drill và65mảnh đáp án ôn có Việt; đã sửa bản Việt từng lượt bài tập và hai nghĩa/cách viết. Báo cáo `_meta/pilot-independent-review.json` trong thư mục Wakaru. Các bản toàn sách vẫn cần checkpoint/QA riêng; không suy full acceptance từ PASS pilot.

Bản đọc: [knowledge/README.md](../knowledge/README.md). Ownership và hàng đợi: [COORDINATOR.json](COORDINATOR.json). Tiếp quản: [HANDOFF.md](HANDOFF.md). Phiên bị đóng sẽ dừng tính toán; checkpoint/snapshot hỗ trợ mở lại từ chỗ đã lưu, không có daemon nền.
