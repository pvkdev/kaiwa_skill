# Ghi chú biên tập – N2_次第_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜次第 – ngay khi A xong thì làm B
- Cấp độ: N2
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜次第 – ngay khi A xong thì làm B
- Các dòng cấu trúc trong bài gốc: V bỏ ます＋次第. Câu gốc 6 còn có danh từ hành động 終了＋次第.
- Gán thẻ cấu trúc cho từng cách dùng: Một nghĩa thời điểm tương lai. Thẻ 1 thân Vます; thẻ 2 danh từ hành động trong tổ hợp 終了次第. Không nhập với N次第だ nghĩa tùy thuộc hay Vた次第だ nghĩa giải thích.
- Cách nói thường gặp: Không tách chương riêng.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Làm ngay khi đủ mốc | 10 | 4 | 0 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Ví dụ gốc 1 |
| 2 | 3.1 | 1 | Ví dụ gốc 3 |
| 3 | 3.1 | 1 | Ví dụ gốc 5 |
| 4 | 3.1 | 2 | Ví dụ gốc 6, bỏ khoảng trắng thừa trước に |

## 2. Lỗi đã tự sửa trong bài gốc

- Câu gốc 6 ロビー に có khoảng trắng thừa; chuẩn hóa ロビーに, không đổi nội dung.
- Công thức nguồn chỉ ghi V bỏ ます nhưng câu 6 dùng 終了次第; ghi nhận danh từ hành động trong chính câu gốc để không bỏ sót dạng thực tế.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 全員集まり次第、出発します。 | Ví dụ gốc 1 |
| Chọn | 部屋の準備ができ次第、会議を始めます。 | Ví dụ gốc 3 |
| Chọn | 成田空港に着き次第、電話します。 | Ví dụ gốc 5 |
| Chọn | 式が終了次第、ロビーに集合してください。 | Ví dụ gốc 6, bỏ khoảng trắng thừa trước に |
| Lược | Ví dụ gốc 2, 4, 7–10 | Cùng nghĩa mốc tương lai; bốn cảnh đã phủ nhóm động từ, hoàn tất chuẩn bị, tới nơi và danh từ hành động. Đối thoại 10 có cách đọc chen chữ nên không chọn. |

## 4. Quyết định đã tự đưa ra

- Rà soát mở màn 7.2.0: Tới Narita là mốc còn phải chờ, gọi điện là hành động chủ định thực hiện ngay sau đó; đúng 着き次第、電話します. Giữ nguyên câu Nhật và toàn bộ ví dụ; lời kể chỉ giữ chi tiết phục vụ ngữ pháp.

- Gợi ý Nam trùng: chọn Kiên, giữ văn phòng mới, áo mưa, giày, mẹ Haruka và tiệm giặt là.
- Không thêm nghĩa tùy thuộc: thuộc các bài 次第だ／次第で khác.
- Bốn ví dụ gốc đủ; không cần câu mới.
- Không tuyệt đối hóa rằng A phải là động tác có người cố ý: 準備ができる hay thông tin đi vào cũng có thể làm mốc chờ, chủ định nằm rõ ở hành động B.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

## 5. Kết quả kiểm tra

- Tự thẩm định mở màn 7.2.0: đã đối chiếu động cơ, diễn biến, sắc thái mẫu và câu Nhật kết; mở/kết nhất quán, đọc thành tiếng tự nhiên.

- Đọc chéo cuối toàn bộ: đã đối chiếu với bài gốc, kiểm nghĩa và cách chia, độ phủ từng dạng, câu Nhật tự viết, bản dịch, tô màu và phần lời Việt; các phát hiện đã xử lý.

- Tự thẩm định: đã đối chiếu từng câu được chọn với bài gốc; soát câu mẫu, câu kết, câu bẫy, bản dịch và cách chia.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.

- Kiểm tra chéo mở màn 7.2.0: Lời hẹn gắn trực tiếp mốc tới sân bay với cuộc gọi chủ động. Sửa lý do không hẹn giờ từ xong thủ tục sang giờ đến có thể đổi để không đặt hai mốc khác nhau. Đã sửa liên kết lời kể/câu kết ở phần tiếng Việt; giữ nguyên câu Nhật, bản dịch, cấu trúc và ví dụ.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
