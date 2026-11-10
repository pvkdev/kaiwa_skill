# CLAUDE.md

Mọi quy tắc của dự án nằm trong AGENTS.md. Đọc và tuân thủ toàn bộ:

@AGENTS.md

Ghi chú cho Claude Code:
- Skill của dự án: `.claude/skills/bunpou-video/SKILL.md` (gọi bằng `/bunpou-video`; dán bài giảng = nhập nguồn; "chạy hàng đợi" = sản xuất hàng loạt).
- Dùng TodoWrite/task list để theo dõi hàng đợi (mỗi mẫu một mục) và các bước của `core/WORKFLOW.md`.
- Hàng đợi dài: có thể giao mỗi mẫu cho một subagent (mỗi mẫu một thư mục riêng; `_quan_ly.json` có khóa ghi).
- Chạy `python tools/validate.py work/<cấp>/<ID>` trước khi báo hoàn thành (tự sinh file phụ, ghi trạng thái nguồn, cập nhật HuongDan.html).
