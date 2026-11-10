---
name: kaiwa-ingest
description: Điều phối markdown hóa PDF kaiwa, xem status, tiếp tục sau gián đoạn và nghiệm thu kho nguồn theo từng sách bằng các worker Sol/high.
---

# Điều phối ingest

Đọc `AGENTS.md`, `kaiwa_skill/core/WORKFLOW.md` và `kaiwa_skill/core/MARKDOWN.md` từ gốc repo. Công cụ: `python kaiwa_skill/tools/ingest.py --help`; đọc hướng dẫn CLI thực tế trước khi chạy, không đoán tham số.

## Trước khi chạy

1. Kiểm tra Git và nguồn; xác định pilot hay production. `bunpou_skill/` chỉ đọc. Nạp `kaiwa_skill/dispatch.json` làm cấu hình model, giới hạn song song và commit; đây là cấu hình coordinator đọc, không phải daemon tự chạy.
2. Xem status đã đối chiếu với file thật; không tin lịch sử chat hay chỉ số phần trăm cũ. Xử lý nguồn thay đổi trước khi tiếp tục.
3. Pilot: chọn 4–6 trang thực chất của một sách, có ít nhất hội thoại, giải thích/bảng/bài tập và một cặp trang liên tiếp. Mở trang để lựa chọn, không chỉ dựa tên sách. Có thể mở thêm trang để tìm mẫu, chỉ chuyển đổi phạm vi đã chọn.
4. Full: chỉ mở hàng đợi production khi pilot có báo cáo PASS lưu trên đĩa. Mỗi tác nhân nhận đúng một PDF và phạm vi còn lại. Mặc định hai worker đồng thời, không vượt slot khả dụng.

## Phân công

Dùng `collaboration.spawn_agent` với `model="gpt-6-sol"`, `reasoning_effort="high"`, `fork_turns="none"`. Đây là tên model cụ thể user yêu cầu (Sol, không tự đổi sang 6.1 Sol). Truyền prompt theo `kaiwa_skill/core/WORKER_PROMPT.md`, đường dẫn repo thực tế, book_id, trang và vị trí checkpoint. Không giao cùng sách cho hai worker. Worker không tự sinh thêm tác nhân.

Điều phối, sửa skill và QA cũng dùng `gpt-6-sol/high`. Model của phiên hiện tại không được đổi chỉ bằng lời nhắc; nếu cần dùng tác nhân đúng model.

## Giám sát và bàn giao

- Tiến độ đếm riêng bản nháp và trang verified; sách partial không phải sách completed.
- Worker checkpoint từng trang; lô 3–5 trang chỉ là kích thước công việc, không phải đơn vị lưu.
- Sau gián đoạn, kiểm tra tác nhân cũ đã dừng trước khi thu hồi quyền sở hữu; never chạy worker thay thế trong khi worker cũ còn ghi.
- Trước khi giao lại, reconcile/hash check; tác nhân mới mở lại trang dang dở, không viết lại các trang verified còn hợp lệ.
- Nghiệm thu pilot theo `kaiwa_skill/core/QUALITY.md`; chỉ sau đó đặt gate production. Nếu thiếu nội dung hoặc sai hệ thống, sửa skill bằng Sol/high và chạy lại phần liên quan.
- Kết thúc mỗi output: chạy validator/build, kiểm tra status, commit riêng theo `kaiwa_skill/core/VERSIONING.md`.
- Nếu phiên phải kết thúc, lưu danh sách sách đang làm, trang còn lại, lỗi và lệnh resume trong báo cáo bàn giao trên đĩa. Không báo đã hoàn thành toàn bộ nếu chưa đủ nguồn.
