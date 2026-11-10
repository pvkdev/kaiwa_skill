# Ghi chú biên tập – {{ID}}

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: {{MAU}} – {{NGHIA}}
- Cấp độ: {{CAP_DO}}
- Phiên bản quy tắc: {{VERSION}}
- Ngày tạo: {{YYYY-MM-DD}}
- Công cụ AI / model: {{vd Claude Code – claude-sonnet / Codex – gpt-…}}

<!-- 4 dòng Cấp độ / Phiên bản quy tắc / Ngày tạo / Công cụ AI là BẮT BUỘC: công cụ đọc chúng để sinh meta. -->

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: {{…}}
- Các dòng cấu trúc trong bài gốc: {{…}}
- Gán thẻ cấu trúc cho từng cách dùng (gộp dòng nào, cách dùng nào "giống cách dùng n"): {{…}}
- Cách nói thường gặp (nếu có): {{…}}

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| {{3.1 …}} | {{n}} | {{k}} | {{m}} | {{k+m}} |

### Bảng phủ ví dụ

<!-- BẮT BUỘC: mỗi ví dụ của Kịch bản một dòng. "Phần" = chương 3.x chứa ví dụ. "Cấu trúc" = số thẻ "Cấu trúc n" ví dụ dùng
     (nhiều số thì cách bằng dấu phẩy; ví dụ của chương Cách nói thường gặp ghi –).
     validate.py dùng bảng này để kiểm: mỗi cách dùng 4–6 ví dụ, mọi thẻ cấu trúc có ít nhất 1 ví dụ. -->

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | {{n}} | {{Bài gốc câu k / MỚI – lý do}} |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | {{…}} | {{…}} | {{…}} |

(Không có lỗi → ghi "Không phát hiện lỗi.")

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| {{Chọn / Lược / MỚI}} | {{…}} | {{điển hình, phủ dạng V/A/N, sắc thái khác… / trùng ý, khó dựng tình huống… / bù cho đủ}} |

## 4. Quyết định đã tự đưa ra

- {{vd: chọn bẫy …; …}}

## 5. Kết quả kiểm tra

- Tự thẩm định: {{số câu Nhật đã soát; số câu đã thay vì không chắc}}
- validate.py: {{ĐẠT / kiểm thủ công}} – {{số cảnh báo}} cảnh báo
- Cảnh báo được giữ lại và lý do: {{…}}
