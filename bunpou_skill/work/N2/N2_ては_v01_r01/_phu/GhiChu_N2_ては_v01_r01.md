# Ghi chú biên tập – N2_ては_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜ては – Cứ… rồi lại…
- Cấp độ: N2
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜ては – Cứ… rồi lại…
- Các dòng cấu trúc trong bài gốc: Vて ＋ は ＋ B（lặp A→B）.
- Gán thẻ cấu trúc cho từng cách dùng: 3.1: 1.
- Cách nói thường gặp: không tách chương ngoài các cách dùng của bài gốc.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Hai việc nối nhau thành chuỗi lặp | 7 | 4 | 0 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu 1 |
| 2 | 3.1 | 1 | Bài gốc câu 2 |
| 3 | 3.1 | 1 | Bài gốc câu 3 |
| 4 | 3.1 | 1 | Bài gốc câu 7 |

## 2. Lỗi đã tự sửa trong bài gốc

Không phát hiện lỗi trong các câu được chọn.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 書いては消し、消しては書いているうちに、紙が破れた。 | Phủ cấu trúc 1; Hai việc nối nhau thành chuỗi lặp |
| Chọn | 東京は、降ってはやみの毎日で、はっきりしない天気が続く。 | Phủ cấu trúc 1; Hai việc nối nhau thành chuỗi lặp |
| Chọn | ABC出版社は、新しい本を出してはベストセラーになっている。 | Phủ cấu trúc 1; Hai việc nối nhau thành chuỗi lặp |
| Chọn | 留学のために貯金をしているのだが、なかなかたまらない。貯金通帳を見てはため息をつく毎日だ。 | Phủ cấu trúc 1; Hai việc nối nhau thành chuỗi lặp |
| Lược | 押しては引き、引いては押して、やっとその牛は歩き出した。 | Ưu tiên ví dụ điển hình và đủ dạng cấu trúc; không tăng số câu trùng dạng |
| Lược | ずっと苦しそうで、昨日から食べては吐いているんです。 | Ưu tiên ví dụ điển hình và đủ dạng cấu trúc; không tăng số câu trùng dạng |
| Lược | 彼女は毎年海外旅行に行っては、珍しい織物を買って帰ってくる。 | Ưu tiên ví dụ điển hình và đủ dạng cấu trúc; không tăng số câu trùng dạng |

## 4. Quyết định đã tự đưa ra

- Rà soát mở màn 7.2.0: Nêu rõ nhiều lượt đặt–hủy cùng một mục tiêu mua sắm, phù hợp 注文しては取り消している; bỏ quan hệ bà chủ nhà Hùng vô lý. Giữ nguyên câu Nhật và toàn bộ ví dụ; lời kể chỉ giữ chi tiết phục vụ ngữ pháp.

- QA trước sản xuất video: làm rõ cảnh và quan hệ nghĩa ở ví dụ 1, đưa phần Tình huống + Cách ghép đạt tối thiểu 60 từ; không thay câu Nhật gốc.

- Chọn1,2,3,7 để có động tác đối nhau, thời tiết, kết quả lặp và nếp phản ứng; không cần[MỚI].
- Không giữ khái quát mẫu chỉ có cặp động từ trái nghĩa; câu3,6,7 nguồn không như vậy.
- Tên An thay gợi ý trùng, giữ nghề, ngoại hình, bà Hùng và quán sushi.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

## 5. Kết quả kiểm tra

- Tự thẩm định mở màn 7.2.0: đã đối chiếu động cơ, diễn biến, sắc thái mẫu và câu Nhật kết; mở/kết nhất quán, đọc thành tiếng tự nhiên.

- Đọc chéo cuối toàn bộ: đã đối chiếu với bài gốc, kiểm nghĩa và cách chia, độ phủ từng dạng, câu Nhật tự viết, bản dịch, tô màu và phần lời Việt; các phát hiện đã xử lý.

- Tự thẩm định: đã soát từng câu Nhật, nghĩa Việt, dạng cấu trúc, tô màu và câu kết; chỉ giữ câu tự nhiên, chắc chắn đúng.
- validate.py: ĐẠT – 0 lỗi, 1 cảnh báo.
- Cảnh báo được giữ lại và lý do: ABC là tên nhà xuất bản giả định có sẵn trong câu gốc, không phải phiên âm cách đọc tiếng Nhật.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Kiểm tra chéo mở màn 7.2.0: Đặt, hủy rồi đặt lại nhiều lượt cùng gốc hành động đúng ては; Kết bỏ quán băng chuyền không có trong cảnh mới. Đã chỉnh tối thiểu lời kể để đồng bộ.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
