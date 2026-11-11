# Rà soát toàn sách — 2026-11-11

**Phạm vi:** PDF1–138 theo kế hoạch cố định trong `book.json`; 22/22 chapter `author_checked`, 128 unit. 135 trang có nội dung được chuyển; PDF3 là thông tin xuất bản đã lưu trong metadata; PDF136 và PDF138 trắng ngoài watermark scan. Không có trang pending. Từng ảnh đã mở, hash ảnh và hash raw của 138 trang khớp hồ sơ coverage. Toàn bộ 420 raw anchor của các unit tồn tại trong trang snapshot được trỏ tới; mỗi unit có đúng một anchor trong chapter.

**Mạch sách:** Mở đầu/hướng dẫn, 20 bài theo thứ tự in, rồi lời bạt. Bài tập giữ khung, chỗ trống và các lượt Nhật in sẵn; bản Việt đi theo câu/lượt, không tự điền đáp án. Hội thoại bị ngắt qua trang được nối rõ ở Bài 17 và Bài 18. Các bảng/lược đồ địa danh, họ tên, cơ cấu công ty và Nội các được đưa sang chữ với quan hệ nhánh. Rà các chapter không còn dòng furigana phụ trợ, romaji hoặc nhãn biên tập của raw.

**Audio:** `audio.json` kiểm inventory PDF1–138. PDF6 chỉ khuyên dùng băng cho `談話練習` ở tập `練習冊`; không thấy nhãn số CD/track, kịch bản nghe, đáp án nghe hoặc địa chỉ tải trong `本文冊`. `actual_files_status=not_checked`; không tự tạo track hay lời thoại.

**Kiểm cấu trúc:** `clean_progress.py resume` trả 22 completed, 0 draft/pending/stale/snapshot_errors, `scope_changed=false`. `validate_fork.py` sau sửa nhãn và số blank còn 6 lỗi: 2 lỗi build chưa chạy (thiếu build hashes và `book.md`) và 4 lỗi anchor trong `book.md` của snapshot (xem drift bên dưới); không còn cảnh báo chapter.

**Drift nguồn live sau snapshot:** `resume` báo `needs_rebase` cho `corpus/book.md`, `manifest.json`, `build.json`. So sánh trực tiếp cho thấy `book.md` live chỉ thêm bốn anchor `p0011-b001`, `p0012-b001`, `p0013-b001`, `p0014-b001` và dòng trống. `manifest.json` chỉ đổi `updated_at`. `build.json` đổi thời gian sinh, hash `book.md`, hash trang 11–14 và hash search tương ứng. Không thấy đổi chữ học. Các trang snapshot `pages/p0011–p0014.md` đã có bốn anchor trên, nên trỏ nguồn ở `units.jsonl` hợp lệ trên trang snapshot; validator đọc `book.md` snapshot nên báo thiếu bốn anchor. Giữ nguyên snapshot và provenance, chờ root ghi nhận/cân nhắc source drift trước build/QA.

**Sửa QA trong lượt:** Bài 13 thống nhất nhãn chú thích JP/VI; Bài 14 giữ đúng hai blank của nhánh lời nhắn có hai cách diễn đạt; Bài 18 giữ cả nhãn Nhật của ngữ cảnh gọi khách. Đã refresh checkpoint ba bài.
