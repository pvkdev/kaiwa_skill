# Ghi chú biên tập – N3_tokoro-ni-he-wo-de-v2

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜ところに／へ／を／で – Đúng lúc…, trong lúc… thì…, vừa… thì…
- Cấp độ: N3
- Phiên bản quy tắc: 1.4.0
- Ngày tạo: 2026-10-29
- Công cụ AI / model: Claude Code – claude-opus-5-5

## 1. Phân tích bài gốc

| Cách dùng | Ví dụ bài gốc | Đã dùng | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 5.1 ところに／ところへ – đang dở dang thì có người/việc ập tới | 8 | 8 | 0 | 8 |
| 5.2 ところを – đang làm thì bị bắt gặp, bị tóm | 7 | 7 | 0 | 7 |
| 5.3 ところで – vừa chạm mốc thì chuyện tiếp theo xảy ra | 4 | 4 | 0 | 4 |
| **Tổng** | 19 | 19 | 0 | 19 |

Dạng kết hợp: V る／ている／た + ところ, Aい + ところ, Aな + な + ところ, N + の + ところ.

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | 妹 dịch là "chị" (ところを, ví dụ 5) | "em gái" | 妹 = em gái; chị gái là 姉 |
| 2 | "B thường cảm trở A" | "cản trở" | Lỗi chính tả |
| 3 | Aい／Aな + ところ | Aな + な + ところ | Tính từ đuôi な cần な khi bổ nghĩa danh từ |
| 4 | "Goị lại" | "Gọi lại" | Lỗi chính tả (chỉ trong phần giải thích bài gốc) |
| 5 | Thiếu dấu 。 ở 手伝って (ところに／へ, ví dụ 1), 見られた (ところを, ví dụ 2), 閉まった (ところで, ví dụ 2) | Thêm 。 | Thiếu dấu câu Nhật |

## 3. Ví dụ [MỚI] và ví dụ bị lược

Không có (mọi cách dùng có 4–10 ví dụ bài gốc).

## 4. Quyết định đã tự đưa ra

- ID: `output/N3_tokoro-ni-he-wo-de/` đã tồn tại → dùng `N3_tokoro-ni-he-wo-de-v2` (không ghi đè); bài giảng thô lưu ở `input/N3_tokoro-ni-he-wo-de-v2.md`.
- Nghĩa ngắn: giữ "đúng lúc…, trong lúc… thì…" của bài gốc, đổi "sau khi…" thành "vừa… thì…" vì ところで nhấn vào khoảnh khắc ngay tại mốc, "sau khi" quá rộng. Bản dịch các ví dụ ところで cũng dùng "vừa… thì…".
- Dấu hiệu nhận biết 5.1: không đưa 行く (bài gốc có nêu) vì cách nói này ít gặp; chỉ giữ các động từ chắc chắn: 来る、帰ってくる、入ってくる、電話がかかってくる、通りかかる.
- Ví dụ 8 của 5.1 (悪いところに来たなあ): giữ chủ ngữ "anh" theo bản dịch gốc, dựng cảnh Tanaka nói với anh họ.
- Bảng mục 4: tự viết 大事なところで, お休みのところを vì bài gốc không có ví dụ dạng Aな và N の; các dòng còn lại trích từ ví dụ bài gốc.
- Mục 6 (N3: 2 bẫy, ưu tiên gần nghĩa): chọn 〜ところです cuối câu (gần nghĩa, bài gốc khuyên tham khảo) và 〜たところで + vế sau tiêu cực (giống hệt hình thức cách dùng 3). Bỏ khoảng trắng thừa trong câu Nhật bài gốc (không tính là lỗi).

## 5. Kết quả kiểm tra

- Tự thẩm định: đã soát 9 câu/cụm tiếng Nhật tự viết (bảng mục 4: 2 cụm; bẫy: 2 câu; đố nhanh: 3 câu; kết: 2 câu; cùng toàn bộ 19 dòng Cách đọc và bản dịch), không phải thay câu nào. Đố nhanh mỗi câu chỉ có 1 đáp án hợp lý.
- validate.py: ĐẠT – 0 cảnh báo
- Cảnh báo được giữ lại và lý do: Không có.
