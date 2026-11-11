# Điều phối clean — tiếp tục từ đây

Root đang điều phối toàn catalog30 PDF, chỉ clean nguồn ready. Người dùng yêu cầu giữ lượt sống và đúng ba worker gpt-6-sol/high. Không kết thúc chỉ vì đã khởi chạy hoặc bàn giao một sách. Không tạo goal/automation nền. Đóng ứng dụng dừng tính toán; checkpoint hỗ trợ mở lại, không phải daemon.

Repo: `D:/CODE/git/kaiwa_skill`. Đọc AGENTS.md, `.agents/skills/kaiwa-fork-knowledge/SKILL.md`, COORDINATOR.json và STATUS.md. Worker hiện tại:

- `/root/clean_namachuukei_sho`: N1 1170 từ, full70 trang; đang phần cuối. N3 và N2 đã bàn giao/build/commit.
- `/root/clean_namachuukei_chu`: 英訳・語い冊 kinh doanh, full103 trang; checkpoint từng bài và tự tiếp tục. Sau Bài10 đang Bài11.
- `/root/clean_keigo`: đã bàn giao Keigo đủ93 trang; đang independent QA toàn sách Sho, review từ đầu, hiện qua Bài5. Không sửa Sho khi worker còn sở hữu.

Đã release phạm vi PDF: Sho91p(commit87c18d1), Chu89p(0314647), N3 47p(fedfb5f), MINATO checklist8p(19da433), Keigo93p(8e939e7). Root review theo mẫu, không gán review toàn sách. Sho đang thêm independent review; cần rebuild/validate/commit khi bàn giao nếu có sửa nội dung. Keigo15 units needs_review; thiếu bài14/trang in106–107 do chính PDF, không dựng lại.

Dùng `py -B`, môi trường PYTHONUTF8=1. PATH `python` là Store alias. clean_progress.py scan/resume/checkpoint, build_fork.py, validate_fork.py nằm trong scripts của skill. Version0.3.5,26tests đạt; parser chấp nhận vai nói Nhật dịch/phiên âm ở lượt Việt, không xác minh ngữ nghĩa vai.

Chờ nguồn ingest sẵn sàng; quét lại sau sách/bàn giao. Nếu không còn nguồn mới, giao worker QA độc lập sách người khác thay vì nhận nguồn chưa đủ điều kiện. Chỉ một worker ghi mỗi sách; root không sửa sách đang được worker sở hữu. Nguồn và snapshot bất biến; không đổi hash để che thay đổi. Chương cũ hợp lệ giữ nguyên khi resume.

Git chia sẻ index với ingest ở chat khác. Chỉ root Git, exact-path `git commit --only -- <book> <snapshot>`, file mới dùng `git add -N` đúng path. Không git add., không reset lịch sử, không push. Kiểm commit thực sự chỉ chứa path được giao. Source snapshot byte-for-byte ở ngoài knowledge; chỉ.md/.json/.jsonl, ảnh ignoredcache.

Điểm tiếp theo: nghiệm thu N1, tiếp tục business, nhận Sho independent QA; scan nguồn mới và giao ngay trong phạm vi đã được ủy quyền. Cập nhật ownership/checkpoint vào COORDINATOR.json. Nếu thực sự bị ngắt, xác nhận worker cũ dừng trước khi nhận lại sách; đọc ledger và resume, không khởi tạo lại/xóa tiến độ.
