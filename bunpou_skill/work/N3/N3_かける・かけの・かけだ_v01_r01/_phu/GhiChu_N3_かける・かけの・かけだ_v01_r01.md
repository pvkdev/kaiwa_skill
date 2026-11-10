# Ghi chú biên tập – N3_かける・かけの・かけだ_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜かける／かけの／かけだ – Đang… dở, làm giữa chừng, chưa xong
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Claude Code – claude-sonnet-5-5

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜かける／かけの／かけだ – Đang… dở, làm giữa chừng, chưa xong
- Các dòng cấu trúc trong bài gốc: V~~ます~~ + かける; V~~ます~~ + かけの + Danh từ; V~~ます~~ + かけだ (~~ます~~ = bỏ ます).
- Chỉ có MỘT cách dùng (hành động dở dang) → `## 3.1 Cách dùng: …` không số. Ba dòng cấu trúc giữ thành 3 thẻ riêng (thẻ 1 かける, thẻ 2 かけの ＋ N, thẻ 3 かけだ), ghi theo ký hiệu `V（bỏ ます） ＋ …`.
- Ý ② bài gốc (かけの đi trước danh từ): đưa vào Sắc thái và Giải thích thẻ 2, không tách thành cách dùng riêng.
- Cách nói thường gặp: không có.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 dở dang | 20 (câu 1 và 8 trùng nhau → 19 ý) | 6 | 0 | 6 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 3 | Bài gốc câu 1 (かけだ; câu 8 trùng nguyên văn) |
| 2 | 3.1 | 1 | Bài gốc câu 2 (入りかけた, thể quá khứ) |
| 3 | 3.1 | 1 | Bài gốc câu 3 (言いかけて, dừng có chủ ý) |
| 4 | 3.1 | 2 | Bài gốc câu 5 (食べかけの＋N) |
| 5 | 3.1 | 1 | Bài gốc câu 10 (死にかけていた, nghĩa thoi thóp) |
| 6 | 3.1 | 2 | Bài gốc câu 14 (作りかけの＋N) |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | 母に食べかけのりんご を捨てられてしまった。 (câu 5) | 母に食べかけのりんごを捨てられてしまった。 | Khoảng trắng thừa trước を (câu được chọn) |
| 2 | 「V~~ます~~ + かける」 | V（bỏ ます） ＋ かける | Chuẩn hóa ký hiệu gạch ngang thành chữ "bỏ ます" |
| 3 | 堀の宿題はまたやりかけだ。 (câu 17, không chọn) | 堀の宿題はまだやりかけだ。 | Nghi sai chữ: bản dịch là "vẫn còn", phải là まだ; câu không được chọn |
| 4 | 「trờ thành」, 「bán kem」, 「ăn ở vốn đã nguội」 (câu 7, 13, 15, không chọn) | trở thành, bánh kem, ăn dở vốn đã nguội | Lỗi chính tả tiếng Việt; câu không được chọn |
| 5 | Câu 1 và câu 8 trùng nguyên văn | tính là một câu | Trùng lặp trong bài gốc |

Câu 20 có khoảng trắng thừa 「、 ゴメンね」, không chọn. Câu 3 bản dịch gốc "đang định nói yêu anh ấy" đã chỉnh cho tự nhiên ở câu Việt.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | この本はまだ読みかけだ。 | Dạng かけだ, điển hình |
| Chọn | お風呂に入りかけたときに、電話が鳴った。 | Dạng かける, quá khứ, bị gián đoạn |
| Chọn | 彼のことが好きだと言いかけてやめた。 | Dạng かける, dừng có chủ ý |
| Chọn | 母に食べかけのりんごを捨てられてしまった。 | Dạng かけの ＋ N, bị động |
| Chọn | その猫は飢えてほとんど死にかけていたが、世話をしたら奇跡的に命を取り戻した。 | Dạng かける với động từ chỉ trạng thái 死ぬ, sắc thái khác |
| Chọn | 母は作りかけの料理を置いて、電話に出た。 | Dạng かけの ＋ N, dễ dựng tình huống |
| Lược | câu 4, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20 | Trùng ý/dạng với câu đã chọn (vd câu 8 trùng câu 1); câu 17 nghi lỗi まだ/また; câu 11, 16 gần ý với câu 10 |

## 4. Quyết định đã tự đưa ra

- Bài chỉ có một cách dùng: mục 3.1 không đánh số, lời giảng chỉ nói "cách dùng" / "mẫu".
- Nhân vật theo gợi ý: Kobayashi (họa sĩ truyện tranh chạy deadline, hay quên đồ), phụ Trang (cô giáo), nhà ga nửa đêm; mở màn và Kết cùng dùng bánh mì ăn dở.
- Bản dịch câu 2 theo bài gốc "chuẩn bị tắm" được viết lại là "vừa mới bước vào bồn tắm" để khớp 入りかけた (việc mới bắt đầu, chưa trọn); không thêm kiến thức ngoài bài gốc.
- Ví dụ 死にかけていた giảng theo hướng "dở dang giữa còn và mất" (thoi thóp), không tách thành cách dùng "sắp…" vì bài gốc chỉ có một ý dở dang.
- Bẫy 1 (gần nghĩa): 〜きる ý ngược; Bẫy 2 (giống hình thức): かける động từ riêng (鍵をかける). Cả hai chắc chắn đúng.
- Câu mẫu メールを書きかけて…, 2 câu người Nhật thường nói (食べかけでごめんね／書きかけのメール) và câu Kết 食べかけのパン tự viết, đều là câu quen thuộc.

- Rà soát trước sản xuất ngày 2026-11-04: Bổ sung lời giảng cụ thể cho ví dụ 1, 2, 4, bảo đảm tình huống và cách ghép đủ ít nhất 60 từ tiếng Việt khi bỏ câu Nhật; giữ nguyên câu Nhật và nghĩa đã chọn.

- Rà soát mở màn 7.2.0: Việc ăn đã bắt đầu rồi bị gián đoạn tạo đồ vật ăn dở; quên trên ghế khớp nguyên văn câu Nhật kết. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định trước sản xuất ngày 2026-11-04: đã soát 6 ví dụ (0 [MỚI]), 3 thẻ cấu trúc, câu mẫu, bẫy và câu kết; đối chiếu nghĩa, cách ghép, thứ tự, bảng phủ, tên gọi và sự tự nhiên. Những câu Nhật được giữ lại không bị viết lại.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.
- Cảnh báo được giữ lại và lý do: Không có.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
