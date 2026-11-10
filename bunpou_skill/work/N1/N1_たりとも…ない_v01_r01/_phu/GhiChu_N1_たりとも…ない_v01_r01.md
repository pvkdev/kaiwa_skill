# Ghi chú biên tập – N1_たりとも…ない_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜たりとも…ない – Dù chỉ một… cũng không
- Cấp độ: N1
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜たりとも…ない – Dù chỉ một… cũng không
- Các dòng cấu trúc trong bài gốc, chuẩn hóa và gán thẻ: 1: Số lượng tối thiểu ＋ たりとも ＋ phủ định.
- Các cách dùng và cách nói thường gặp: Dù một lượng nhỏ nhất cũng không.
- Bảng phủ được lập trước khi viết Kịch bản; chọn ví dụ theo thứ tự gốc trong từng chương, [MỚI] đặt cuối.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Dù một lượng nhỏ nhất cũng không | 4 | 4 | 0 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu 1 |
| 2 | 3.1 | 1 | Bài gốc câu 2 |
| 3 | 3.1 | 1 | Bài gốc câu 3 |
| 4 | 3.1 | 1 | Bài gốc câu 4 – sửa thiếu す |

## 2. Lỗi đã tự sửa trong bài gốc

- 聞き逃まい → 聞き逃すまい: 聞き逃す là động từ nhóm một, thêm まい vào dạng từ điển.
- “xe cộng” → “xe cộ”; chỉnh cách diễn đạt để giữ 一瞬 là một khoảnh khắc.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 試験まであとわずかだ。一日たりとも遊んではいられない。 | Bài gốc câu 1 |
| Chọn | 砂漠では一滴たりとも水を無駄にはできない。 | Bài gốc câu 2 |
| Chọn | 車の通りの多い所では、親は一瞬たりとも子どもの手を離さないように注意すべきだ。 | Bài gốc câu 3 |
| Chọn | 先生の言うことは一言たりとも聞き逃すまいと、新入生たちは真剣に話を聞いていた。 | Bài gốc câu 4 – sửa thiếu す |


## 4. Quyết định đã tự đưa ra

- Đổi Đức thành Tý, giữ học sinh, vest xám, mẹ và ga.
- Sửa tên người mẹ gợi ý Tuấn thành vai mẹ không tên, tránh xung đột giới/quan hệ.
- Bốn câu gốc đã đủ, không thêm ví dụ.
- Nhân vật Việt chỉ dùng một tên gọi ngắn, không thêm họ hoặc tên đệm theo yêu cầu người dùng.

- Rà soát mở màn 7.2.0: Thời gian thi sát giờ tạo căn cứ cho lượng tối thiểu một giây và phủ định không thể lãng phí; tránh bối cảnh trang phục không liên quan. Giữ nguyên câu Nhật, bản dịch và toàn bộ ví dụ; chỉ dẫn ngoại hình không liên quan được bỏ khỏi lời kể.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã đối chiếu 4 câu ví dụ với bài gốc, kiểm cách chia, nghĩa, thứ tự và phần tô màu; đã soát câu mẫu, bẫy và câu kết.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.

- Tự thẩm định mở màn 7.2.0: đã đối chiếu động cơ, diễn biến, sắc thái mẫu, phần giới thiệu và câu kết; lời kể tự nhiên khi đọc thành tiếng.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
