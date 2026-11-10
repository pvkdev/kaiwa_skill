# Ghi chú biên tập – N2_上（で）_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜上で／上では – Xét riêng về mặt…, theo…
- Cấp độ: N2
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜上で／上では – Xét riêng về mặt…, theo…
- Các dòng cấu trúc trong bài gốc: Nの上で／Nの上では; bổ nghĩa Nの上でのN／Nの上のN.
- Gán thẻ cấu trúc cho từng cách dùng: Một nghĩa khía cạnh/phạm vi/cơ sở thể hiện; thẻ 1 vị ngữ, 2 上でのN, 3 上のN. 上 ở đây là うえ có の trước, không là hậu tố じょう.
- Cách nói thường gặp: Không tách chương riêng.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Giới hạn nhận xét trong một phương diện hoặc phạm vi | 8 | 5 | 0 | 5 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 2 | Bài gốc1 |
| 2 | 3.1 | 1 | Bài gốc2 |
| 3 | 3.1 | 1 | Bài gốc5 |
| 4 | 3.1 | 1 | Bài gốc6 |
| 5 | 3.1 | 3 | Bài gốc7 |

## 2. Lỗi đã tự sửa trong bài gốc

Không phát hiện lỗi trong các câu chọn. Giữ doanh thu 売り上げ khác lợi nhuận 利益, giữ sắc thái có vẻ ở そう.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 彼とは仕事の上での付き合いしかない。 | Bài gốc1 |
| Chọn | 地図の上では近そうに見えたが、実際に歩いてみると遠かった。 | Bài gốc2 |
| Chọn | 理論の上では一日で終わる計算だが、実際にはもっと時間がかかりそうだ。 | Bài gốc5 |
| Chọn | 数字の上では売り上げが伸びているが、利益はほとんど増えていない。 | Bài gốc6 |
| Chọn | 彼女とは仕事の上の付き合いだけで、私生活については何も知らない。 | Bài gốc7 |
| Lược | Câu 3–4, 8 | Năm lượt có 4 ý khác vì 1/7 cùng quan hệ công việc, giữ cặp để phủ 上での/上の; 2/5/6 bổ sung 3 tình huống khác đủ tối thiểu 4 ý |

## 4. Quyết định đã tự đưa ra

- Rà soát mở màn 7.2.0: Khoanh nhận xét gần trong phương diện bản đồ, đối chiếu đường đi thực tế để không nhầm thành vị trí nằm trên bản đồ. Giữ nguyên câu Nhật và toàn bộ ví dụ; lời kể chỉ giữ chi tiết phục vụ ngữ pháp.

- Một nghĩa phương diện, không tách bản đồ và lý thuyết thành cách dùng riêng.
- Không gộp với bài 上で Vた/Vる hoặc bài N上じょう.
- Tiêu đề viết 上で／上では thay ngoặc 上（で） để tránh nhìn thành chú giải cách đọc.
- Nam trùng, dùng Khang, giữ nghề/ngoại hình/bé Kobayashi/quán sushi.

- Đọc chéo đã đưa lịch sử sửa nguồn và quyết định chọn ví dụ ra khỏi lời giảng; Kịch bản giữ diễn giải ngữ pháp tự đủ, phần biên tập nằm ở ghi chú.

- Đã rà khoảng trắng tiếng Việt và ký tự biên tập lạc trên bản hiện tại; giữ nguyên câu Nhật, nhãn, công thức và số ví dụ.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

## 5. Kết quả kiểm tra

- Tự thẩm định mở màn 7.2.0: đã đối chiếu động cơ, diễn biến, sắc thái mẫu và câu Nhật kết; mở/kết nhất quán, đọc thành tiếng tự nhiên.

- Đọc chéo cuối toàn bộ: đã đối chiếu với bài gốc, kiểm nghĩa và cách chia, độ phủ từng dạng, câu Nhật tự viết, bản dịch, tô màu và phần lời Việt; các phát hiện đã xử lý.

- Tự thẩm định: đã đối chiếu từng câu được chọn với bài gốc; soát câu mẫu, câu kết, câu bẫy, bản dịch và cách chia.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
