# Ghi chú biên tập – N3_uchi-ni

> File này chỉ dành cho người làm video. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜うちに – Trong lúc…, trước khi…
- Cấp độ: N3
- Phiên bản quy tắc: 1.0.0
- Ngày tạo: 2026-10-29
- Công cụ AI / model: Claude Code – claude-sonnet-5-5

## 1. Phân tích bài gốc

| Cách dùng | Ví dụ từ bài gốc | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- |
| 5.1 Tranh thủ làm trước khi trạng thái thay đổi | 3 | 1 | 4 |
| 5.2 Đang làm một việc thì có thay đổi tự nhiên xảy ra | 2 | 2 | 4 |
| **Tổng** | 5 | 3 | 8 |

## 2. Lỗi đã sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | 暗くならないうちに帰りましょう → "Hãy về trước khi trời tối" | "Chúng ta về trước khi trời tối nhé" | 〜ましょう là lời rủ cùng làm, "Hãy…" nghe như mệnh lệnh nên lệch sắc thái |
| 2 | 話しているうちに… → "Trong lúc nói chuyện, tôi đã thích cô ấy" | "Nói chuyện một hồi thì mình đã thích cô ấy" | Bản dịch gốc thiếu "thì", mất ý "đang làm một lúc rồi có thay đổi" của cách dùng ② |
| 3 | Dịch dùng "tôi" | "mình" | Đồng bộ xưng hô theo rule 02 (chỉ là chuẩn hóa văn phong, không phải lỗi nội dung) |

Ngoài ra: không phát hiện lỗi chính tả, lỗi cấu trúc (Aな đã có な, N đã có の) hay lỗi tiếng Nhật trong bài gốc. Bài gốc không có ví dụ cho dạng V る, nên dòng V る ở mục 4 dùng ví dụ ngắn tự viết (話すうちに).

## 3. Ví dụ [MỚI] đã thêm

| Mục | Câu Nhật | Lý do thêm |
| --- | --- | --- |
| 5.1 Ví dụ 4 | おばあちゃんが元気なうちに、温泉に連れていってあげたい。 | Cách dùng 1 chỉ có 3 ví dụ; minh họa dạng Aな + な + うちに |
| 5.2 Ví dụ 3 | 毎日練習しているうちに、お箸が上手に使えるようになった。 | Cách dùng 2 chỉ có 2 ví dụ; minh họa thay đổi dần dần (〜ようになる) |
| 5.2 Ví dụ 4 | 歩いているうちに、道に迷ってしまった。 | Cách dùng 2 chỉ có 2 ví dụ; thay đổi ngoài ý muốn |

## 4. Cần người biết tiếng Nhật duyệt

- [ ] Toàn bộ ví dụ [MỚI]
- [ ] Mục 4: các ví dụ ngắn tự viết cho dòng V る (話すうちに), V ない (忘れないうちに), Aな (元気なうちに)
- [ ] Mục 6: bẫy 〜間に (cách phân biệt sắc thái "tranh thủ" của うちに, đã dùng "thường" để tránh nói tuyệt đối) và bẫy うち = "nhà"
- [ ] Mục 7 Kết: 肉まんが温かいうちに食べたかった

## 5. Kết quả kiểm tra

- validate.py: ĐẠT – 0 cảnh báo (chạy lại theo quy tắc 1.2.0)
- Cảnh báo được giữ lại và lý do: Không có.

## 6. Khuyến nghị

- Tách tập: Không cần (tổng 8 ví dụ ≤ 24).
- Cập nhật theo quy tắc 1.2.0: đưa ví dụ cách dùng 1 về đúng thứ tự bài gốc; bỏ ví dụ [MỚI] dư 学生のうちに (cách dùng 1 chỉ cần bù 1 ví dụ cho đủ 4).
