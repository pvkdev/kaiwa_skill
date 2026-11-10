# Ghi chú biên tập – N3_こと・ないこと_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜こと／ないこと – Hãy…, Phải… / Không được…
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Claude Code – claude-sonnet-5-5

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜こと／ないこと – Hãy…, Phải… / Không được…
- Các dòng cấu trúc trong bài gốc: Vる／Vない + こと (một dòng).
- Gán thẻ cấu trúc: bài gốc chỉ có 1 cách dùng (①②③ cùng nghĩa: chỉ thị ở cuối câu, dùng trong quy tắc/thông báo, văn bản). Tách dòng gốc thành 2 thẻ để phủ dạng: Cấu trúc 1 Vる ＋ こと, Cấu trúc 2 Vない ＋ こと.
- Ý ④ (こととする) không tách thành cách dùng riêng, đưa vào Sắc thái và Lưu ý.
- Cách nói thường gặp: không có.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 ra lệnh, nhắc nhở quy tắc | 17 (15 câu cùng mẫu + 2 câu ことだ) | 6 | 0 | 6 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu 1 (V る) |
| 2 | 3.1 | 1 | Bài gốc câu 4 (V る) |
| 3 | 3.1 | 2 | Bài gốc câu 6 (V ない) |
| 4 | 3.1 | 2 | Bài gốc câu 7 (V ない) |
| 5 | 3.1 | 1 | Bài gốc câu 11 (V る) |
| 6 | 3.1 | 2 | Bài gốc câu 14 (V ない) |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | 15 日 | 15日 | Khoảng trắng thừa trong câu Nhật |

(Ngoài ra không phát hiện lỗi dịch hay ngữ pháp trong các câu đã chọn.)

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | レポートは10日までに提出すること。 | V る điển hình, thông báo của trường |
| Chọn | 15日はお弁当を持ってくること。 | V る, thầy cô dặn cả lớp |
| Chọn | 病気でも、会議には必ず出席すること。 | V る, bối cảnh công sở, có 〜でも |
| Chọn | 明日は赤鉛筆を忘れないこと。 | V ない, nhắc nhở |
| Chọn | 体育館には土足で入らないこと。 | V ない, biển cảnh báo |
| Chọn | 授業中は携帯電話を使わないこと。 | V ない, nội quy lớp |
| Lược | câu 2, 3, 5, 8, 10, 12, 13, 15 | Trùng dạng/ý với câu đã chọn (câu 5 xem mục 4) |
| Lược | câu 9 (集合のこと) | Dạng N ＋ のこと không nằm trong cấu trúc bài gốc (chỉ có Vる／Vない), không thêm thẻ mới |
| Lược | câu 16, 17 (ことだ) | Là mẫu 〜ことだ (lời khuyên), không phải 〜こと mệnh lệnh; đưa ngắn gọn vào mục Bẫy 1 |

## 4. Quyết định đã tự đưa ra

- Chỉ có một cách dùng nên chương ghi `## 3.1 Cách dùng: …` không đánh số, lời giảng không nói "cách dùng 1".
- Câu 16, 17 của bài gốc là 〜ことだ (lời khuyên) – không đưa vào ví dụ; viết thành Bẫy 1 với câu tự viết 風邪を引きたくなければ、早く寝ることだ。 (câu quen thuộc, chắc chắn đúng).
- Câu 5 (có 「（とする）」 trong ngoặc) không chọn để tránh ký hiệu ngoặc trên màn hình; ý こととする được nêu bằng lời ở Sắc thái và Lưu ý.
- Bẫy 2 chọn 〜ないでください (gần nghĩa) – điểm khác biệt chắc chắn: lời nhờ lịch sự nói trực tiếp so với văn bản cứng.
- Câu mẫu 廊下を走らないこと。, hai câu "Người Nhật thường nói" (ごみは持ち帰ること。／遅刻しないこと。) và câu Kết 取った皿は戻さないこと。 là câu tự viết, đều là câu nội quy quen thuộc.
- Nhân vật theo gợi ý: Sơn (họa sĩ truyện tranh), Takeshi, nhà hàng sushi băng chuyền; các ví dụ dùng nhân vật khác nhau.
- Tô màu chọn こと (phần đứng sát động từ); Tô màu Việt chọn cụm "phải…"/"không được…" tương ứng.

- Rà soát trước sản xuất ngày 2026-11-04: Bổ sung lời giảng cụ thể cho ví dụ 4, bảo đảm tình huống và cách ghép đủ ít nhất 60 từ tiếng Việt khi bỏ câu Nhật; giữ nguyên câu Nhật và nghĩa đã chọn.

- Rà soát trước sản xuất ngày 2026-11-04: Xếp câu nguồn 6, 7 trước câu 11 theo thứ tự nguồn, không nhóm lại theo khẳng định/phủ định; giữ nguyên câu Nhật và cập nhật bảng phủ.

- Rà soát mở màn 7.2.0: Hành động định trả đĩa làm nội quy cần xuất hiện đúng lúc; tránh lý do chạy hạn và ngoại hình không liên quan. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định trước sản xuất ngày 2026-11-04: đã soát 6 ví dụ (0 [MỚI]), 2 thẻ cấu trúc, câu mẫu, bẫy và câu kết; đối chiếu nghĩa, cách ghép, thứ tự, bảng phủ, tên gọi và sự tự nhiên. Những câu Nhật được giữ lại không bị viết lại.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.
- Cảnh báo được giữ lại và lý do: Không có.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
