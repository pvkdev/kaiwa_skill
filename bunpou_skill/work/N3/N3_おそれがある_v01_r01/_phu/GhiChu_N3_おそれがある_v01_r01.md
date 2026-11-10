# Ghi chú biên tập – N3_おそれがある_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜おそれがある – Sợ rằng…, có nguy cơ… (chuyện không hay sẽ xảy ra)
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Claude Code – claude-sonnet-5-5

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜おそれがある – Sợ rằng…, có nguy cơ… (chuyện xấu sẽ xảy ra)
- Các dòng cấu trúc trong bài gốc: Động từ thể từ điển + 恐れがある; Danh từ + の + 恐れがある.
- Chỉ có MỘT cách dùng: tiêu đề `## 3.1 Cách dùng: …` không đánh số. Thẻ 1 (V thể từ điển), thẻ 2 (N の). Chuẩn hóa ký hiệu thành `V（thể từ điển） ＋ おそれがある` và `N ＋ の ＋ おそれがある`; viết おそれ bằng kana theo tên mẫu, chú thích kanji 恐れ ở Sắc thái.
- Ý ② (văn viết, dùng trong bản tin, thời sự…) và ③ (cách nói tương tự 危険がある、不安がある) của bài gốc: ② đưa vào Khi nào dùng / Dấu hiệu nhận biết; ③ không tách thành cách dùng, không đưa vào Kịch bản (không cần, tránh lan man).
- Cách nói thường gặp: không có.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 おそれがある | 15 | 6 | 0 | 6 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu 1 (V る: 倒れる) |
| 2 | 3.1 | 2 | Bài gốc câu 2 (N の: 台風) |
| 3 | 3.1 | 2 | Bài gốc câu 3 (N の: 倒産) |
| 4 | 3.1 | 1 | Bài gốc câu 5 (V る: 手遅れになる) |
| 5 | 3.1 | 1 | Bài gốc câu 8 (V てしまう, chữ 恐れ) |
| 6 | 3.1 | 1 | Bài gốc câu 14 (V bị động, ことから) |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | Động từ thể từ điển + 恐れがある | V（thể từ điển） ＋ おそれがある | Chuẩn hóa ký hiệu và thuật ngữ sang ký hiệu V, N (không phải lỗi thật) |
| 2 | 説滅のおそれがある (câu 12, không được chọn) | 絶滅のおそれがある | Sai chữ Hán; câu không được chọn nên không xuất hiện trong Kịch bản |
| 3 | 医師に指示に従って (câu 10, không được chọn) | 医師の指示に従って | Sai trợ từ; câu không được chọn |
| 4 | 「đếm nay」 (câu 7, không được chọn) | đêm nay | Sai chính tả tiếng Việt; câu không được chọn |
| 5 | 「この テレビドラマ は」 (câu 4, không được chọn) | このテレビドラマは | Khoảng trắng thừa, không phải lỗi thật |

Các câu được chọn (1, 2, 3, 5, 8, 14) không phát hiện lỗi; chỉ chỉnh câu Việt cho tự nhiên (vd "xin hãy chú ý" → "mọi người hãy chú ý nhé", "nhóm chụp hình" → "nhóm quay phim").

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 大きい地震が来たら、この建物は倒れるおそれがある。 | Điển hình, V る, thiên tai |
| Chọn | 明日は台風のおそれがあるので、注意してください。 | Phủ dạng N の; lời cảnh báo kèm lời dặn |
| Chọn | こんな赤字が続くと、この会社は倒産のおそれがある。 | Dạng N の; sắc thái công việc |
| Chọn | 早く手術しないと、手遅れになるおそれがある。 | V る; ngữ cảnh y tế, điều kiện ないと |
| Chọn | この液体は危険だ。間違って飲み込むと、死んでしまう恐れがある。 | Phủ chữ 恐れ, dạng V てしまう |
| Chọn | 親鳥に気づかれるおそれがあることから、撮影チームはそれ以上巣に近づくことをあきらめた。 | V bị động, văn viết, nối ことから |
| Lược | câu 4 (ドラマ…影響), 6 (タバコ…肺がん), 7 (津波), 9 (噴火), 10 (副作用), 11 (台風は上陸する), 12 (絶滅), 13 (話すと…問題), 15 (ハリケーン…恐れが出てきた) | Trùng ý/trùng dạng với câu đã chọn; câu 10, 12 có lỗi chữ/trợ từ; câu 15 dùng おそれが出てくる (ngoài cấu trúc bài gốc); câu 6 vế trước rời rạc |

## 4. Quyết định đã tự đưa ra

- Bài chỉ có một cách dùng: mục 3.1 không đánh số, lời giảng chỉ nói "cách dùng"/"mẫu".
- Viết tên mẫu bằng kana おそれ như tiêu đề bài gốc; các ví dụ giữ nguyên chữ kana hay kanji (恐れ) như bài gốc.
- Nhân vật theo gợi ý: Daichi (y tá, mua sắm online), phụ Wei (sếp), ga tàu giờ cao điểm; không đổi gợi ý.
- Bẫy 1 (gần nghĩa): おそれがある vs かもしれない; Bẫy 2 (giống hình thức): 恐れ入ります. Cả hai là cách nói chắc chắn.
- Câu mẫu, 2 câu "Người Nhật thường nói" và câu Kết tự viết (thông báo thời tiết, cảnh báo bảo mật); đều là câu quen thuộc, dùng おそれ trong ngữ cảnh văn viết.
- Không tách ý ③ của bài gốc (危険がある、不安がある) thành nội dung vì không phải cách dùng và không cần cho người học ở cấp N3.
- Đặt Kết dùng おそれがあります (lịch sự) để bám tình huống thông báo của loa ga ở mở màn.

- Rà soát trước sản xuất ngày 2026-11-04: Bổ sung lời giảng cụ thể cho ví dụ 3, bảo đảm tình huống và cách ghép đủ ít nhất 60 từ tiếng Việt khi bỏ câu Nhật; giữ nguyên câu Nhật và nghĩa đã chọn.

- Rà soát mở màn 7.2.0: Thông báo trang trọng về nguy cơ tàu chậm chưa thành sự thật dẫn đúng おそれがある; loại bỏ thùng hàng và trang phục không liên quan. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định trước sản xuất ngày 2026-11-04: đã soát 6 ví dụ (0 [MỚI]), 2 thẻ cấu trúc, câu mẫu, bẫy và câu kết; đối chiếu nghĩa, cách ghép, thứ tự, bảng phủ, tên gọi và sự tự nhiên. Những câu Nhật được giữ lại không bị viết lại.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.
- Cảnh báo được giữ lại và lý do: Không có.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
