---
name: bunpou-video
description: Bộ sản xuất video ngữ pháp tiếng Nhật qua NotebookLM. Dùng khi người dùng dán bài giảng ngữ pháp (nhập vào source/), nói "chạy hàng đợi", "chạy hàng loạt", "làm video", "tạo kịch bản" hoặc gọi /bunpou-video.
---

# bunpou-video

Skill này chỉ là lối vào. **Nguồn quy tắc duy nhất** nằm ở thư mục gốc dự án: đọc `AGENTS.md`, rồi làm đúng `core/WORKFLOW.md`.

- **Dán bài giảng** → Chế độ A – Nhập nguồn: chép nguyên văn vào file tạm (nhiều bài: chèn dòng `---BÀI N2---` trước mỗi bài),
  chạy `python tools/nguon.py them <file tạm>`, xóa file tạm, báo các file đã thêm và số mẫu trong hàng đợi.
- **"chạy hàng đợi" / "chạy N2" / `/bunpou-video chạy`** → Chế độ B: `python tools/nguon.py hang-doi [--cap N2] [--so 10]`,
  rồi với **từng mẫu** làm Chế độ C:
  1. `python tools/nguon.py bat-dau <file nguồn>` → nhận `<ID>`, thư mục `work/<cấp>/<ID>/`, gợi ý nhân vật;
  2. làm `core/WORKFLOW.md` Bước 2 → 7, chỉ viết `KichBan_<ID>.md` và `_phu/GhiChu_<ID>.md`
     (áp dụng `core/rules/01`–`06`, `core/templates/`, ví dụ chuẩn `core/examples/N3_tokoro-ni-he-wo-de/`);
  3. `python tools/validate.py work/<cấp>/<ID>` đến khi ĐẠT (tự ghi trạng thái nguồn). Lỗi sau 3 vòng → ghi lại, sang mẫu kế tiếp.
  Cuối cùng `python tools/nguon.py trang-thai` và báo cáo bảng ngắn.

Chế độ tự quyết: không hỏi lại, không yêu cầu người dùng duyệt. Không sửa file trong `core/`, không sửa/xóa file trong `source/`,
không tự tạo hay đổi tên thư mục trong `work/`.
