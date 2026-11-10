# Mẫu giao việc cho Sol/high

Coordinator điền thông tin thực trước khi spawn. Output chỉ có text; cache render `.cache/renders/<book_id>/` được phép dùng tạm để đối chiếu, không commit hoặc nhúng vào Markdown:

> Làm việc tại REPO. Đọc AGENTS.md và .agents/skills/kaiwa-pdf-markdown/SKILL.md. Bạn là worker gpt-6-sol/high, chỉ phụ trách BOOK_ID, PDF SOURCE, trang PAGES. Đọc trạng thái hiện có trước khi làm. Claim với định danh WORKER_ID. Chỉ ghi corpus của sách và scratch riêng; không sửa skill, không commit. Mở ảnh từng trang và đối chiếu thật trước verify. Checkpoint từng trang. Nếu không đọc chắc, ghi issue và báo. Hoàn thành phạm vi thì release, báo đường dẫn output, trang đạt/còn lỗi và hướng dẫn tiếp tục. Không xử lý toàn file khi chỉ được giao pilot.

Tác nhân thay thế nhận thêm: vị trí manifest, trang đã verified, lý do bàn giao, lock đã giải phóng hay cần coordinator thu hồi. Không truyền đáp án mong muốn cho reviewer độc lập.

Nhắc worker kiểm header/footer và ranh giới bảng riêng từng trang, không truyền mẫu cố định sang trang khác. Vùng có vẻ thiếu trong ảnh toàn trang cần crop riêng trước khi xóa/bỏ; quan sát mâu thuẫn cần đối chứng và báo, không tự giả định nguyên nhân.
