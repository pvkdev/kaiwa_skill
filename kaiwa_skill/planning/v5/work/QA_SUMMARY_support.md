# Bàn giao QA — owner `support`

Ngày 2026-11-13. Đã ghi đủ **85/85** chặng được giao trong `support_assignment.json`, tổng **1.562** tình huống nói, tại `work/stages/<stage_key>.json`. Mỗi file có mục tiêu, trọng tâm kiến thức, họ sự kiện, vai, nhánh, đường nối hậu sự kiện và ranh giới chặng. Không viết hội thoại/bài học, không bài test/điểm/gate. Các tình huống mới giữ `origin: ai_authored`; không quy chúng cho sách từ heading hoặc lookup.

## Mở sâu sau bản đầu

- `T-51` lên 30 cảnh: nhập học/chuyển trường; ensoku, undoukai, kyuushoku, đồ cần mang; quan hệ bạn bè và trao đổi khi con thấy bị bỏ ngoài nhóm mà không tự kết luận bắt nạt.
- `V5P-065` lên 33 cảnh: đón trễ/đổi người đón chưa được xác nhận; bé ốm hoặc ngã giữa buổi; cơ sở đóng đột ngột; nhu cầu ăn uống riêng và trao đổi sau thử.
- `T-48` lên 25 cảnh: chọn nơi sinh/lớp chuẩn bị, người đi cùng, ngày sinh khác kế hoạch. `T-50` thêm cuộc tìm đúng đầu mối hỗ trợ.
- `V5P-086` lên 28 cảnh: cuộc xin nghỉ với sếp, lời giữ lại, lời đồn, HR/offboarding, gọi hỏi giấy công ty chưa giao, bàn giao và xử lý áp lực qua đầu mối phù hợp. `H-09` và `H-55` mỗi chặng 24 cảnh để phủ người nhà/chuyên viên hiểu khác nhau và việc cộng đồng phát sinh sau họp.
- Tách thêm hậu sự kiện/đầu mối nhiều bước cho `S-34`, `V5P-025/027/030/032/033/049/057/058/059/060/062/068/072/093/094`, cùng các chặng y tế, nghề, thiên tai và gia đình còn rộng. Các cảnh nối tiếp dùng ID cũ đã viết trước đó, không đổi UID/order.

## Lỗi đã sửa và kiểm tra

- Đã sửa 18 `continues_from` tự trỏ trong `V5P-065/068/072/093/094/086`. Quét cả 85 file: mọi đường nối chỉ trỏ ID đã xuất hiện trước trong cùng chặng, không có self/future link.
- Tiêu đề cảnh `V5P-084/S004` trùng nguyên văn `S-07/S015` đã đổi thành tên cụ thể cho cuộc offer, giữ nguyên ID. Không sửa file của owner khác.
- `py -B -X utf8 tools/roadmap_v5.py validate --partial` sau sửa: `valid=true`, `warnings=0`, `duplicate_title_groups=0`, `possible_nonoral_tasks=0` (lúc chạy: 277/289 chặng có file, 12 còn chờ owner khác). Đây là kiểm cấu trúc; chất lượng biên tập vẫn cần root đọc.
- Đọc chéo các cặp S-44↔V5P-025, S-34↔V5P-057–062, T-51↔H-55, T-01↔V5P-018/020, S-42↔V5P-033/034, S-32↔T-49/V5P-096/086. Ranh giới mục tiêu nói hợp lý. **Cần root kiểm sau khi H-10 có file:** T-01 của owner daily đã có năm cảnh gia hạn/đổi điều kiện; H-10 nên giữ thương lượng, trách nhiệm và tranh chấp sâu thay vì dạy mới cùng việc hỏi gia hạn.

## Giới hạn nguồn

- `support_web_sources.json`: 21 nguồn chính thức, mỗi nguồn có `read_status` thực tế (**8 `opened`, 13 `search_excerpt`**). W01 và W03 có trích đoạn tìm kiếm nhưng mở trang trực tiếp bị HTTP 403. Nguồn này giúp xác định đầu mối và phạm vi giao tiếp, không chứng minh điều kiện/chi phí/quyền lợi từng trường hợp hoặc câu Nhật cụ thể.
- Bản clean sách đã đọc chọn: B08 Unit 11–14, 29; B05 chương khẩn cấp Unit 1–6; B02 một phần Scene 29–30, 35; B01 đầu chương điện thoại. Chưa đối chiếu ảnh PDF ở lượt V5 này. B05 là vai nhân viên cơ sở, không phải mẫu người gọi 119; B08 câu về thẻ cư trú không chứng minh đúng quầy Nyukan. Trước khi viết bài chuyên môn cần đọc sâu đúng đoạn, thêm nguồn y tế/pháp lý/địa phương hiện hành, và ghi vai nguồn chính xác.
- Các stage nghề trong assignment có tham khảo `work_research.md` **chỉ đọc** để tìm ranh giới, nhưng worker support chưa tự mở sách/web sơ cấp của nhóm work. Vì vậy không gắn `work:Wxx` hoặc B09/B16 vào `source_refs` các stage nghề; tình huống vẫn là AI biên soạn.
