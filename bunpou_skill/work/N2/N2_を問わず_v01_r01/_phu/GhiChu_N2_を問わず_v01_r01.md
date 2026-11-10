# Ghi chú biên tập – N2_を問わず_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜を問わず – Bất kể…, không phân biệt…
- Cấp độ: N2
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜を問わず – Bất kể…, không phân biệt…
- Các dòng cấu trúc trong bài gốc: N＋を問わず; chú ý có Nは問わず. N là tiêu chí phân loại, thang mức, cặp đối lập.
- Gán thẻ cấu trúc cho từng cách dùng: Một nghĩa không lấy tiêu chí A để phân biệt B; thẻ 1 を問わず, 2 は問わず nhấn tiêu chí.
- Cách nói thường gặp: Không tách chương riêng.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Không phân biệt theo một tiêu chí | 23 | 4 | 1 | 5 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc1 |
| 2 | 3.1 | 1 | Bài gốc4 |
| 3 | 3.1 | 1 | Bài gốc6 |
| 4 | 3.1 | 1 | Bài gốc21 sửa bản dịch sai コート |
| 5 | 3.1 | 2 | MỚI – phủ biến thể は問わず được nêu nhưng thiếu ví dụ |

## 2. Lỗi đã tự sửa trong bài gốc

- Câu 21 オールウェザーコート là sân thi đấu mọi thời tiết, trong cảnh này コート không phải áo khoác; bỏ chú giải tiếng Anh sai “coat”.
- Câu 22 文化財 là di sản văn hóa, không phải tài nguyên văn hóa, câu không chọn.
- Mẫu không chỉ trường hợp “có hay không”; còn mọi mức và mọi loại của tiêu chí.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | このスポーツセンターは、年齢を問わず、どなたでも利用できます。 | Bài gốc1 |
| Chọn | 彼らは昼夜を問わず、作業を続けた。 | Bài gốc4 |
| Chọn | 値段の高い安いを問わず、とにかく、いいものを買いたい。 | Bài gốc6 |
| Chọn | オールウェザーコートでは、天候を問わずいつでも試合ができる。 | Bài gốc21 sửa bản dịch sai コート |
| MỚI | 経験は問わず、意欲のある人を募集します。 | MỚI – phủ biến thể は問わず được nêu nhưng thiếu ví dụ |
| Lược | Câu 2–3, 5, 7–20, 22–23 | Bốn câu gốc đa dạng tiêu chí, 1 mới chỉ phủ Nは問わず |

## 4. Quyết định đã tự đưa ra

- Rà soát mở màn 7.2.0: Nỗi lo tuổi tác được giải bằng phạm vi mọi tuổi; không tự suy rằng ngoài tuổi thì không còn điều kiện nào. Giữ nguyên câu Nhật và toàn bộ ví dụ; lời kể chỉ giữ chi tiết phục vụ ngữ pháp.

- Giữ một nghĩa tiêu chí không xét, không tách tuổi/quốc tịch/thời tiết thành cách dùng.
- Nは問わず là thẻ riêng để không bỏ dạng nguồn nêu, thêm đúng 1 câu.
- Nam trùng, dùng Tâm, giữ nghề/ngoại hình/Wei/ga đêm.

- Đã rà khoảng trắng tiếng Việt và ký tự biên tập lạc trên bản hiện tại; giữ nguyên câu Nhật, nhãn, công thức và số ví dụ.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

## 5. Kết quả kiểm tra

- Tự thẩm định mở màn 7.2.0: đã đối chiếu động cơ, diễn biến, sắc thái mẫu và câu Nhật kết; mở/kết nhất quán, đọc thành tiếng tự nhiên.

- Đọc chéo cuối toàn bộ: đã đối chiếu với bài gốc, kiểm nghĩa và cách chia, độ phủ từng dạng, câu Nhật tự viết, bản dịch, tô màu và phần lời Việt; các phát hiện đã xử lý.

- Tự thẩm định: đã đối chiếu từng câu được chọn với bài gốc; soát câu mẫu, câu kết, câu bẫy, bản dịch và cách chia.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
