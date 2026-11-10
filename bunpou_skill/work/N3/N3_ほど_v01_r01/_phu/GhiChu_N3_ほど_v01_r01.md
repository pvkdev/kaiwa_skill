# Ghi chú biên tập – N3_ほど_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜ほど – Càng… càng…; thường… hơn
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜ほど – Càng… càng…; thường… hơn
- Các dòng cấu trúc trong bài gốc: N ＋ ほど. Các ví dụ nguồn còn có Vる, Aい và Aなな ＋ ほど.
- Gán thẻ cấu trúc cho từng cách dùng: Nguồn thiếu các dạng đã xuất hiện trong ví dụ nên ghi đủ4 thẻ: N, V, Aい, Aな. Chọn3,4,7,8, mỗi thẻ1 ví dụ.
- Cách nói thường gặp (nếu có): Không tách chương riêng.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Mức đặc điểm tăng thì đặc điểm khác đổi theo | 9 | 4 | 0 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 4 | Bài gốc câu 3 |
| 2 | 3.1 | 1 | Bài gốc câu 4 |
| 3 | 3.1 | 2 | Bài gốc câu 7 |
| 4 | 3.1 | 3 | Bài gốc câu 8 |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | Chỉ ghi N ＋ ほど | Ghi thêm Vる／Aい／Aなな ＋ ほど | Ví dụ3,7,8 có các dạng này, không thể hướng dẫn tất cả nối như N. |
| 2 | たばこをよくする | たばこをよく吸う | Câu9 dùng động từ không tự nhiên; không chọn. |

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 家やアパートは、駅に近くて便利なほど高い。 | Phủ dạng cấu trúc và minh họa đúng nghĩa của chương. |
| Chọn | 真面目にがんばるひとほどストレスを抱え込みやすい。 | Phủ dạng cấu trúc và minh họa đúng nghĩa của chương. |
| Chọn | 彼女は成長するほどきれいになる。 | Phủ dạng cấu trúc và minh họa đúng nghĩa của chương. |
| Chọn | 結婚式のスピーチは短いほどいいと、よく言われます。 | Phủ dạng cấu trúc và minh họa đúng nghĩa của chương. |
| Lược | 若い人ほど朝寝坊を する。 | Đã có câu cùng dạng hoặc cùng ý; giữ số ví dụ gọn và đa dạng. |
| Lược | 太い人ほど病気になりやすい。 | Đã có câu cùng dạng hoặc cùng ý; giữ số ví dụ gọn và đa dạng. |
| Lược | 一般的に、若い患者ほど病気の進行も早い。 | Đã có câu cùng dạng hoặc cùng ý; giữ số ví dụ gọn và đa dạng. |
| Lược | 魚は新鮮なものほどおいしい。 | Đã có câu cùng dạng hoặc cùng ý; giữ số ví dụ gọn và đa dạng. |
| Lược | たばこ を よくする人ほど病気になりやすい。 | Đã có câu cùng dạng hoặc cùng ý; giữ số ví dụ gọn và đa dạng. |

## 4. Quyết định đã tự đưa ra

- Khoa đã dùng ở bài に決まっている, đổi sang Khang để tránh trùng; giữ vai câu cá và ngoại hình.
- Bổ sung thẻ cách nối bị nguồn lược nhưng đã có ví dụ, không thêm nghĩa mới.
- Không chọn các câu khái quát y tế vì có nhiều ngoại lệ và không cần để phủ cấu trúc.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

- Rà soát mở màn 7.2.0: Mức ít hành lý liên hệ trực tiếp mức thuận tiện di chuyển, có quan sát so sánh rõ; bỏ thùng cá vô cớ. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã soát 4 ví dụ, các câu mẫu, câu bẫy và câu kết; kiểm tra nguyên văn, nghĩa, cách nối và hai dòng tô màu.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.
- Cảnh báo được giữ lại và lý do: không có; đã nói rõ thẻ tính từ い.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
