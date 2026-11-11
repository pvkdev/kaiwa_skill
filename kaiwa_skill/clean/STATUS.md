# Clean hàng loạt — đang chạy

Điều phối bắt đầu ngày 2026-11-11 (JST), theo yêu cầu giữ chat hoạt động và dùng đúng ba worker `gpt-6-sol/high`. Toàn kho hiện có 30 PDF; chỉ nhận sách đã có ingest đủ điều kiện và ghim phiên bản nguồn trước khi biên soạn.

- **日本語生中継 初中級編 1**: lô đầu đã biên soạn PDF5–10; hai chương hướng dẫn được tác giả kiểm, Bài1 đang nháp. Worker tiếp PDF11–16 để hoàn tất Bài1.
- **日本語生中継 中～上級編**: lô đầu đã biên soạn PDF9–13; Bài1 đang nháp. Worker tiếp PDF14–18; phần hướng dẫn PDF4–8 vẫn còn trong kế hoạch.
- **日本語敬語の使い方 基本表現85**: lô đầu biên soạn PDF3,5,6,7,8,10; hai chương đầu được tác giả kiểm, §1 đang nháp. Worker tiếp PDF11–15.

Đây là trạng thái theo checkpoint tác giả, chưa phải nghiệm thu toàn sách. Root đang kiểm mẫu ảnh nguồn và bản clean. Không có sách nào trong đợt hàng loạt được tuyên bố hoàn tất ở thời điểm này.

Trạng thái máy và phân công: [COORDINATOR.json](COORDINATOR.json). Tiến độ chính xác từng sách nằm ở `_meta/clean-state.json`, `_meta/page-coverage.json` và hồ sơ biên tập của sách. Nếu chat bị ngắt, đọc các file đó và xác nhận worker cũ đã dừng trước khi tiếp quản.

Giữ toàn bộ mạch kiến thức và đặc trưng sách, kể cả bài tập, dữ kiện, đáp án nguồn, ghi chú và mã track cần cho thực hành. Nội dung học trong `knowledge/`; snapshot raw nằm riêng trong `source_snapshots/`. Worker không dùng Git hoặc sửa nguồn ingest.
