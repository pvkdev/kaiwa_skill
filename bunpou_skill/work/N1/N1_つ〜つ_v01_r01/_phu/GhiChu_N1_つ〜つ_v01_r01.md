# Ghi chú biên tập – N1_つ〜つ_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜つ〜つ – Khi thì… khi thì…; qua lại
- Cấp độ: N1
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜つ〜つ – Khi thì… khi thì…; qua lại
- Các dòng cấu trúc trong bài gốc, chuẩn hóa và gán thẻ: 1: Vます bỏ ます ＋ つ ＋ Vます bỏ ます ＋ つ.
- Các cách dùng và cách nói thường gặp: Hai hành động đan xen qua lại.
- Bảng phủ được lập trước khi viết Kịch bản; chọn ví dụ theo thứ tự gốc trong từng chương, [MỚI] đặt cuối.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Hai hành động đan xen qua lại | 6 | 6 | 0 | 6 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu 1 |
| 2 | 3.1 | 1 | Bài gốc câu 3 – sửa 待ち thành 持ち |
| 3 | 3.1 | 1 | Bài gốc câu 4 |
| 4 | 3.1 | 1 | Bài gốc câu 6 |
| 5 | 3.1 | 1 | Bài gốc câu 8 |
| 6 | 3.1 | 1 | Bài gốc câu 9 |

## 2. Lỗi đã tự sửa trong bài gốc

- 待ちつ持たれつ → 持ちつ持たれつ: quán ngữ hỗ trợ qua lại dùng 持つ, không phải 待つ.
- Câu 10 lược: 待ちつ待たれつ/間係 có lỗi; nội dung được giữ bằng câu 3 đã sửa, tránh nhân đôi quán ngữ.
- “chéc tạc chén thù” → diễn đạt rõ rót mời qua lại.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 彼に会おうか会うまいかと悩んで、家の前を行きつ戻りつしていた。 | Bài gốc câu 1 |
| Chọn | お互い持ちつ持たれつで、助け合いましょう。 | Bài gốc câu 3 – sửa 待ち thành 持ち |
| Chọn | 初詣の神社はものすごい人出で、押しつ押されつ、やっとのことで境内まで辿り着いた。 | Bài gốc câu 4 |
| Chọn | 久しぶりに友人と差しつ差されつ酒を飲んで何時間もしゃべった。 | Bài gốc câu 6 |
| Chọn | あの試合は抜きつ抜かれつの良いものだった。 | Bài gốc câu 8 |
| Chọn | 今夜の月は雲間から見えつ隠れつしている。 | Bài gốc câu 9 |
| Lược | 彼女に事実を言おうか言うまいか、廊下を行きつ戻りつ考えた。 | Ngoài tập chọn; ưu tiên dạng khác và tình huống không trùng |
| Lược | ラッシュアワーの時間なので、バス内は乗客で押しつ押されつしている。 | Ngoài tập chọn; ưu tiên dạng khác và tình huống không trùng |
| Lược | 今日はゆっくり二人で、差しつ差されつ朝まで飲みましょう。 | Ngoài tập chọn; ưu tiên dạng khác và tình huống không trùng |
| Lược | 待ちつ待たれつの間係だ。 | Ngoài tập chọn; ưu tiên dạng khác và tình huống không trùng |

## 4. Quyết định đã tự đưa ra

- Đổi Đức sang Nhân, giữ họa sĩ, vest xám, ga và bạn cũ.
- Nhóm câu 1/2, 4/5, 6/7 gần trùng; câu 10 sau sửa trở về cùng quán ngữ với câu 3, không tăng số lượng.
- Chọn sáu cặp/tình huống khác nhau, không thêm ví dụ.
- Nhân vật Việt chỉ dùng một tên gọi ngắn, không thêm họ hoặc tên đệm theo yêu cầu người dùng.

- Rà soát mở màn 7.2.0: Lo quên bút và sợ lỡ tàu tạo hai lực kéo khiến nhân vật thực sự đi đi lại lại trước ga, khớp 行きつ戻りつ và Kết tìm thấy bút. Giữ nguyên câu Nhật, bản dịch và toàn bộ ví dụ; chỉ dẫn ngoại hình không liên quan được bỏ khỏi lời kể.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã đối chiếu 6 câu ví dụ với bài gốc, kiểm cách chia, nghĩa, thứ tự và phần tô màu; đã soát câu mẫu, bẫy và câu kết.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.

- Tự thẩm định mở màn 7.2.0: đã đối chiếu động cơ, diễn biến, sắc thái mẫu, phần giới thiệu và câu kết; lời kể tự nhiên khi đọc thành tiếng.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
