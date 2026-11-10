# Ghi chú biên tập – N3_反面_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜反面 – Nhưng mặt khác lại…
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜反面 – Nhưng mặt khác lại…
- Các dòng cấu trúc trong bài gốc: Thể thường＋反面; Aな＋な／である＋反面; N＋である＋反面.
- Gán thẻ cấu trúc cho từng cách dùng: Một nghĩa hai mặt; thẻ1V,2Aい,3Aなな／である,4Nである.
- Cách nói thường gặp: Không tách chương riêng.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Hai mặt trái ngược của cùng sự vật, sự việc | 15 | 4 | 0 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu1 |
| 2 | 3.1 | 3 | Bài gốc câu2 |
| 3 | 3.1 | 2 | Bài gốc câu3 |
| 4 | 3.1 | 4 | Bài gốc câu11 |

## 2. Lỗi đã tự sửa trong bài gốc

- Câu8 “cấp trước” → “cấp dưới” theo 目下; câu không chọn.
- Câu11 伯父 dịch “chú” → “bác trai”; không xác định bên nội hay ngoại nếu câu không nói.
- Không dạy mặt tốt bắt buộc đứng trước; câu6 nguồn đưa bất tiện trước ưu điểm.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | この薬はよく効く反面、副作用も強い。 | Bài gốc câu1 |
| Chọn | フェースブックは便利な反面、トラブルも多い。 | Bài gốc câu2 |
| Chọn | この部屋は日当たりがいい反面、夏はかなり暑い。 | Bài gốc câu3 |
| Chọn | 伯父は頑固者である反面、涙も脆い性格だ。 | Bài gốc câu11 |
| Lược | Câu4–10,12–15 | Chọn4câu phủV/Aい/Aな/N, giữ đa dạng đồvật, dịchvụ, chỗở, conngười |

## 4. Quyết định đã tự đưa ra

- Một cách dùng hai mặt, không thêm nghĩa đối chiếu người này với người khác.
- Bốn câu gốc đủ phủthẻ, không thêm mới; giữ Facebook đúng cách viết gốc trong câu Nhật.
- Dùng Sakura và Vy ở quán sushi; các nhận xét về thuốc và dịch vụ là ví dụ hư cấu để học câu.

- Rà soát nhân vật toàn đợt: đổi tên gợi ý Sakura thành Anh do trùng tên nhân vật chính đã dùng; giữ nghề, ngoại hình, tình huống và nhân vật phụ. Đổi đồng bộ Mở màn, Lời giảng và câu Kết; câu Nhật gốc giữ nguyên.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

- Chốt QA: bỏ lời nhắc ví dụ gốc khỏi lời giảng, giữ giải thích về cách dùng thực tế.

- Rà soát mở màn 7.2.0: Mặt trái cụ thể là dễ ăn quá nhiều, trực tiếp khớp 食べすぎやすい; không lấy phân tâm thay cho ý câu kết. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã đối chiếu từng câu được chọn với bài gốc; soát câu mẫu, câu kết, câu bẫy, bản dịch và cách chia.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
