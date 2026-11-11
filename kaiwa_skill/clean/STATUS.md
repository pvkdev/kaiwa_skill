# Clean hàng loạt — đang điều phối

Đúng ba worker `gpt-6-sol/high`. Root giữ lượt điều phối, kiểm nguồn mới, QA và Git; chưa kết thúc phạm vi toàn catalog30 PDF.

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

- `/root/clean_namachuukei_sho`: full clean cuốn 中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―,140 trang; đã checkpoint phần mở đầu và Unit1 (PDF1–40), đang Unit2; plan10 phần.
- `/root/clean_namachuukei_chu`: full clean 本文冊 kinh doanh138 trang; source đã ready và snapshot/plan22 phần đã init.
- `/root/clean_keigo`: preflight shadowing sơ–trung cấp145 trang; full88/5500/business manners/telephone đã có map riêng, chưa clean khi raw chưa ready.

Bản đọc: [knowledge/README.md](../knowledge/README.md). Ownership và hàng đợi: [COORDINATOR.json](COORDINATOR.json). Tiếp quản: [HANDOFF.md](HANDOFF.md). Phiên bị đóng sẽ dừng tính toán; checkpoint/snapshot hỗ trợ mở lại từ chỗ đã lưu, không có daemon nền.
