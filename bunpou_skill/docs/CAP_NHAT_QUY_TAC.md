# Hướng dẫn cập nhật quy tắc

Dành cho người dùng và cho AI khi người dùng yêu cầu "cập nhật quy tắc".

## 1. Muốn đổi gì thì sửa file nào

| Muốn đổi | Sửa file |
| --- | --- |
| Thứ tự / số phần của bài giảng | `core/templates/KichBan.template.md`, `guide.md`, `tools/validate.py` (H2_FIXED_*), ví dụ chuẩn |
| Cách trình bày màn hình video (2 dòng Nhật / Việt, ngắt dòng, tô màu, hình minh họa) | `guide.md`, `core/templates/TuyChinh.template.txt` |
| Giọng giảng, xưng hô, độ hài, độ dài | `core/rules/02_giong-van.md`, `guide.md` |
| Cách trình bày ví dụ (nhãn, câu dẫn dịch) | `core/rules/03_vi-du.md`, `tools/validate.py` (LABELS, TRANSLATION_LEADS), template, ví dụ chuẩn |
| Số ví dụ cả bài | `core/rules/01_noi-dung.md`, `core/rules/05_cap-do.md`, `tools/validate.py` (MIN/MAX_TOTAL_EXAMPLES) |
| Quy tắc độ chính xác | `core/rules/01_noi-dung.md` |
| Quy tắc chữ Nhật, cách đọc | `core/rules/04_tieng-nhat.md` |
| Hồ sơ cấp độ N5–N1 | `core/rules/05_cap-do.md` |
| Dàn nhân vật | `core/rules/06_nhan-vat.md` |
| Prompt dán vào NotebookLM | `core/templates/TuyChinh.template.txt` |
| Trang làm video (các bước, giao diện, nút copy, tìm kiếm) | `HuongDan.html` (gốc dự án) |
| Dữ liệu sinh tự động (meta, TuyChinh, data.js, work/_index.js) | `tools/build_data.py` |
| Ngôn ngữ, định dạng, kiểu hình ảnh của series | `series.json` |
| Từ bị cấm | `core/rules/02_giong-van.md` + `tools/validate.py` (FORBIDDEN_PHRASES) |

## 2. Các bước bắt buộc sau khi sửa

1. Sửa (các) file ở bảng trên. Giữ nguyên tắc: **một quy tắc chỉ ghi ở một nơi**; file khác chỉ tham chiếu.
2. Nếu đổi định dạng: cập nhật **ví dụ chuẩn** `core/examples/N3_tokoro-ni-he-wo-de/` cho khớp.
3. Nếu sửa `guide.md`: nhắc người dùng xóa nguồn guide cũ trong notebook NotebookLM và tải lại `guide.md`.
4. Tăng `VERSION`:
   - `MAJOR` (2.0.0): đổi định dạng đầu ra (tiêu đề, nhãn, tên file) – đầu ra cũ không còn đạt validate.
   - `MINOR` (1.1.0): thêm/đổi quy tắc nội dung, giọng văn.
   - `PATCH` (1.0.1): sửa câu chữ, lỗi nhỏ.
5. Ghi `CHANGELOG.md`.
6. Chạy:
   ```bash
   python tools/validate.py core/examples/N3_tokoro-ni-he-wo-de
   python tools/build_bundle.py
   python tools/build_data.py
   ```
   Ví dụ chuẩn phải ĐẠT. Bundle phải được tạo lại. Dữ liệu HuongDan.html dựng lại (guide, series mới).
7. Nếu sửa `SKILL.md`: sửa cả 2 bản `.claude/skills/…` và `.agents/skills/…` cho giống nhau.

## 3. Mẫu yêu cầu gửi AI

```text
Cập nhật quy tắc:
- <điều muốn đổi 1>
- <điều muốn đổi 2>
Làm theo docs/CAP_NHAT_QUY_TAC.md.
```
