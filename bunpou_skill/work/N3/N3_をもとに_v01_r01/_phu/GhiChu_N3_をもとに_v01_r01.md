# Ghi chú biên tập – N3_をもとに_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜をもとに – Dựa trên… để tạo hoặc đánh giá…
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜をもとに – Dựa trên… để tạo hoặc đánh giá…
- Các dòng cấu trúc trong bài gốc: N＋をもとに／をもとにして; N1＋をもとにした＋N2.
- Gán thẻ cấu trúc cho từng cách dùng: Một cách dùng; thẻ1gộp に／にして nối hành động, thẻ2にした bổ nghĩa danh từ.
- Cách nói thường gặp: Không tách chương riêng.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Lấy điều có sẵn làm cơ sở sáng tạo hoặc đánh giá | 17 | 4 | 0 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu3 |
| 2 | 3.1 | 1 | Bài gốc câu4 |
| 3 | 3.1 | 2 | Bài gốc câu10 |
| 4 | 3.1 | 1 | Bài gốc câu13 |

## 2. Lỗi đã tự sửa trong bài gốc

- Dịch フィクション thành “viễn tưởng” quá hẹp → nên là “hư cấu”; câu12 không chọn.
- Bản dịch câu4 lặp “của của” → bỏ một từ.
- Câu17 dùng vốn thừa kế làm cơ sở kinh doanh: không giữ lời cấm tuyệt đối mọi thứ hữu hình; chỉ phân biệt với cách nói nguyên liệu trực tiếp.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 人のうわさだけをもとにして人を判断するのは良くない。 | Bài gốc câu3 |
| Chọn | このアイデアは君の話をもとにして考えたよ。 | Bài gốc câu4 |
| Chọn | 史実をもとにした作品を書き上げた。 | Bài gốc câu10 |
| Chọn | この映画は実際にあった事件をもとに作られた。 | Bài gốc câu13 |
| Lược | Câu1–2,5–9,11–12,14–17 | Chọn4câu phủ biến thể; tránh giải thích thêm các khẳng định lịch sử chưa cần thiết |

## 4. Quyết định đã tự đưa ra

- Kiểm tra chéo mở màn 7.2.0: Chuyện bạn đi lạc tạo chất liệu cho ý tưởng truyện mới đã nghĩ ra, khác sao chép nguyên xi. Bỏ đĩa sushi ở kết không có tiền đề trong mở.

- Một nghĩa lấy cơ sở; sáng tạo và đánh giá là hai bối cảnh của cùng quan hệ, không tách chương.
- Chọn4câu gốc, không thêm ví dụ mới; giữ 被動 ở câu13 trong bản dịch.
- Dùng Yuki, Vy và quán sushi như gợi ý, câu kết quay lại ý tưởng truyện tranh.

- Rà soát nhân vật toàn đợt: đổi tên gợi ý Yuki thành Như do trùng tên nhân vật chính đã dùng; giữ nghề, ngoại hình, tình huống và nhân vật phụ. Đổi đồng bộ Mở màn, Lời giảng và câu Kết; câu Nhật gốc giữ nguyên.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

- Rà soát mở màn 7.2.0: Có chuyện nguồn rõ ràng và phần sáng tạo phát triển thêm, đúng をもとに chứ không chép lại nguyên chuyện. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã đối chiếu từng câu được chọn với bài gốc; soát câu mẫu, câu kết, câu bẫy, bản dịch và cách chia.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
