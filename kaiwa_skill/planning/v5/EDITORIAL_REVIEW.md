# Nghiệm thu V5 — 13/11/2026

**Phạm vi đã làm: lộ trình và bản thiết kế tình huống nói cho 289 chặng.** Chưa phải 5.914 hội thoại Nhật–Việt hoàn chỉnh hoặc bài kiến thức/từ vựng/ngữ pháp đã viết xong.

## Quy mô và định hướng

- 80 Sơ, 145 Trung, 64 Thượng; 33 cụm; 1.304 họ sự kiện, 5.914 tình huống nói; 2.602 liên kết tiếp nối.
- 185 UID cũ giữ nguyên, 9 chặng tổng hợp/quá rộng phân lại nội dung, 104 chặng mới. Đủ 194 mã cũ có đích trong MIGRATION_V4_1.
- Chặng có 12–41 tình huống tùy phạm vi; số lượng không chứng minh chất lượng hoặc đủ mọi việc ngoài đời.
- Cả 27 sách vẫn là nền tra cứu. Nguồn ngoài và AI biên soạn là thành phần thiết yếu, không bị chặn vì thiếu hội thoại sách tương ứng. Mọi tình huống mới đều ghi AI biên soạn; nguồn sách/web tách riêng theo vai trò.

## Các phần đã đọc và cải thiện

Ba worker Sol/high biên soạn từng chặng trong assignment, đọc lại cấu trúc và các phạm vi liên quan. Root đọc chọn các cảnh/nhánh, kiểm ranh giới giữa cấp độ và vai, rồi ghép. Có đọc chéo độc lập các cặp quầy Sơ–Trung, nhờ giúp–cuộc gọi chuyên biệt, trường học–PTA, nhà ở–sửa/chuyển, ngân hàng và nghỉ việc.

- T-22: 35 cảnh vai người dự, nhiều dịp 忘年会/新年会/歓迎会/送別会/祝賀会/昇進/打ち上げ. V5P-118: 40 cảnh 幹事; H-46: 41 cảnh MC; T-23: 31 cảnh phụ trách du lịch công ty. Các key là đầu mối cũ; mã hiển thị mới xem registry.
- T-35 được mở từ hai việc xin phép khá hẹp thành 7 họ sự kiện/38 cảnh, có từ chối/có điều kiện/chờ và cuộc nói sau đó.
- T-51 có 30 cảnh gồm nhập/chuyển trường, sự kiện, đồ dùng/bữa ăn và quan hệ bạn bè. V5P-065 có 33 cảnh gồm đón trễ, người khác đón, bé ốm/ngã, cơ sở đóng và nhu cầu ăn riêng.
- T-48 có 25 cảnh; V5P-086 có 28 cảnh gồm HR và việc sau khi chốt nghỉ, tách lời chào H-30. Các lời hỏi chuyên môn không thành tư vấn y tế/pháp lý.
- H-10 được sửa để khác T-01: đối chiếu cách hiểu/căn cứ, thương lượng gói điều kiện và nêu phần còn bất đồng; không tự chuyển từ từ chối sang đã giải quyết.
- Root thêm 11 họ sự kiện/61 cảnh cho khoảng trống cụ thể: xe đêm, gọi hỗ trợ tài khoản, cơ sở cộng đồng, diễn tập, quyền chọn thông tin với recruiter, hybrid, gói làm đẹp, PTA, trao đổi y tế riêng tư, hobby shop và studio ảnh. Hai tiêu đề chung được viết rõ mục tiêu khác nhau, giữ ID.

## Kiểm bằng máy và kiểm bản xem

- Đủ 289 file, đúng UID/chủ sở hữu; event/case ID và con trỏ hợp lệ, nhánh nằm trong tập được định nghĩa.
- Các nhánh nối tiếp chỉ trỏ tình huống có trước, không self-loop hoặc vòng lặp. Đã phát hiện và sửa self-loop trong một batch mở rộng trước khi công bố.
- Không còn tiêu đề trùng nguyên văn sau chuẩn hóa; không phát hiện nhiệm vụ viết email/điền form/CV/báo cáo trong các title tình huống. Đây là kiểm tìm dấu hiệu, có kiểm biên tập bổ sung; không phải bộ chứng minh mọi câu đều hoàn hảo.
- JSONL, registry, các cụm và mã hiển thị dựng từ cùng manifest. Hash V4.1 khớp, nguồn PDF/knowledge/bunpou không bị sửa.
- 14 kiểm tra hồi quy của helper nội dung đạt, gồm đọc registry V5 mới và giữ phiên bản lộ trình được pin cho draft.
- HTML chạy smoke cho tìm không dấu, lọc cấp, tra mã cũ và hiển thị chặng có nhiều cảnh; đã render bằng Chrome headless và xem ảnh desktop. Ảnh chỉ ở cache, không là tài liệu bàn giao.

## Giới hạn cần giữ đúng khi đi tiếp

Root không đọc lại toàn văn 27 PDF hoặc tự đọc mọi cảnh trong lượt này. Nguồn web có mức đọc khác nhau; ledger ghi opened/search_excerpt/index_only và phần không kiểm được. Dữ kiện thủ tục/điều kiện/chi phí/y tế/an toàn cần kiểm lại đúng cơ sở và thời điểm khi soạn bài. Lời kể cộng đồng gợi nhu cầu, không là thống kê phổ biến.

Không gán audio sách cho lời thoại mới. Không tuyên bố dùng hết sách hoặc bao phủ vô hạn. Tình huống có thể ôn cùng một kỹ năng ở cấp khác; zero title duplicates không đồng nghĩa không có phần gần nghĩa cần biên tập tiếp khi viết bài.

## Tiếp tục và sửa theo ID

Đọc SCHEMA_V5 và DESIGN_AND_MIGRATION. Sửa đúng file `work/stages/<key>.json`, giữ UID/ID cũ, thêm ID mới cho cảnh mới. Kiểm liên kết, render lại rồi nghiệm thu phần thay đổi; không sinh lại 289 chặng để sửa một chặng. BUILD_STATE là đầu mối tiếp tục; skill nội dung có checkpoint/revision riêng khi bắt đầu viết bài.
