# Ghi chú biên tập – N3_向け_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜向け – Hướng đến, được làm dành cho…
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜向け – Hướng đến, được làm dành cho…
- Các dòng cấu trúc trong bài gốc: N＋向けに＋V／câu; N＋向けだ; N1＋向けの＋N2.
- Gán thẻ cấu trúc cho từng cách dùng: Một nghĩa chỉ đối tượng nhắm tới; thẻ1向けに,2向けだ,3向けの.
- Cách nói thường gặp: Không tách chương riêng.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Đối tượng mà sản phẩm hoặc hoạt động hướng tới | 18 | 4 | 0 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 3 | Bài gốc câu1 |
| 2 | 3.1 | 3 | Bài gốc câu3 |
| 3 | 3.1 | 2 | Bài gốc câu11 |
| 4 | 3.1 | 1 | Bài gốc câu12 |

## 2. Lỗi đã tự sửa trong bài gốc

- Bản dịch câu10 “hơn to hơn” → “to hơn”; câu không chọn.
- Không giữ khẳng định chỉ đi với danh từ người; nguồn có 海外, 輸出 nên giải thích thêm đúng phạm vi.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | この会社では、子どもむけのテレビ番組を作っている。 | Bài gốc câu1 |
| Chọn | 小学生向けの辞書は字が大きくて読みやすい。 | Bài gốc câu3 |
| Chọn | この説明書は外国人向けだが、日本人が読んでもとてもおもしろく、ためになる。 | Bài gốc câu11 |
| Chọn | これは若いお母さん向けに書かれた本です。 | Bài gốc câu12 |
| Lược | Câu2,4–10,13–18; vídụ so sánh nângcao | Đủ4câu phủに／の／だ, không thêm ví dụmới; phần向き và用đưa vào bẫy/lưuý |

## 4. Quyết định đã tự đưa ra

- Một nghĩa hướng đối tượng; hình thức bổ nghĩa và vị ngữ không tách cách dùng.
- Chọn4câu gốc, giữむけ ở câu1theo bản gốc.
- Giữ Quân, Phương và quán sushi theo gợi ý; món trong mở màn chỉ để giới thiệu hình ảnh thực đơn.

- Rà soát nhân vật toàn đợt: đổi tên gợi ý Quân thành Khoa do trùng tên nhân vật chính đã dùng; giữ nghề, ngoại hình, tình huống và nhân vật phụ. Đổi đồng bộ Mở màn, Lời giảng và câu Kết; câu Nhật gốc giữ nguyên.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

- Rà soát trước sản xuất ngày 2026-11-04: Bỏ lời nhắc biên tập về câu gốc khỏi kịch bản, thay bằng giải thích phục vụ trực tiếp người học; giữ câu Nhật.

- Rà soát mở màn 7.2.0: Có lựa chọn thiết kế ảnh lớn và phần ăn hướng trẻ em từ đầu, phân biệt 向け với phù hợp tình cờ. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định trước sản xuất ngày 2026-11-04: đã soát 4 ví dụ (0 [MỚI]), 3 thẻ cấu trúc, câu mẫu, bẫy và câu kết; đối chiếu nghĩa, cách ghép, thứ tự, bảng phủ, tên gọi và sự tự nhiên. Những câu Nhật được giữ lại không bị viết lại.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.
- Cảnh báo được giữ lại và lý do: Không có.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
