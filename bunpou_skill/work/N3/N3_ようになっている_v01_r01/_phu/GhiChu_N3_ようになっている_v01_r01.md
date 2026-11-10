# Ghi chú biên tập – N3_ようになっている_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜ようになっている – Được thiết kế để…
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜ようになっている – Được thiết kế để…
- Các dòng cấu trúc trong bài gốc: Vる／Vない ＋ ようになっている
- Gán thẻ cấu trúc cho từng cách dùng: Một cách dùng; thẻ 1 khẳng định Vる, thẻ 2 phủ định Vない.
- Cách nói thường gặp: Không tách chương riêng.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Chức năng và cơ chế được thiết kế sẵn | 6 | 4 | 0 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu 1 |
| 2 | 3.1 | 2 | Bài gốc câu 2 |
| 3 | 3.1 | 1 | Bài gốc câu 3 |
| 4 | 3.1 | 2 | Bài gốc câu 6 |

## 2. Lỗi đã tự sửa trong bài gốc

- Câu 3 thiếu dấu kết câu → thêm 。; bản dịch “cái nửa” → “cửa” (lỗi chính tả).
- Bản dịch câu 2 “không bật lên” → “không thể mở” để khớp 開くことができない.
- Chuẩn hóa khoảng trắng thừa trong câu Nhật, không đổi từ.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | このドアは閉めると、カギがかかるようになっている。 | Bài gốc câu 1 |
| Chọn | この画面はパスワードを入力しないと、開くことができないようになっている。 | Bài gốc câu 2 |
| Chọn | このドアはだれかが近づくと、自動的に開くようになっている。 | Bài gốc câu 3 |
| Chọn | この自動販売機はレバーを押さないと、おつりが出ないようになっている。 | Bài gốc câu 6 |
| Lược | そのパソコンは、しばらく使わないと電源が切れるようになっている。 | Câu 4 cùng dạng khẳng định; dùng ý cho mở màn, không tính ví dụ |
| Lược | このストーブは大きく傾くと、自動的に火が消えるようになっている。 | Câu 5 cùng dạng cơ chế khẳng định |

## 4. Quyết định đã tự đưa ra

- Giữ một cách dùng đúng bài gốc, tách hai thẻ để phủ Vる và Vない.
- Dùng Suzuki và Đức trong lớp học theo gợi ý; câu kết quay về máy tính tự ngắt.
- Chọn 4 câu gốc, không thêm ví dụ mới; giải thích cơ chế bảo vệ ở dạng phủ định.

- Rà soát nhân vật toàn đợt: đổi tên gợi ý Suzuki thành Châu do trùng tên nhân vật chính đã dùng; giữ nghề, ngoại hình, tình huống và nhân vật phụ. Đổi đồng bộ Mở màn, Lời giảng và câu Kết; câu Nhật gốc giữ nguyên.

- Theo yêu cầu người dùng: nhân vật Việt chỉ dùng một tên gọi ngắn, thống nhất ở mở màn, lời dẫn, tình huống, câu kết và ghi chú; không thêm họ hoặc tên đệm để phân biệt giữa các bài.

- Rà soát mở màn 7.2.0: Dựa vào thiết lập tự tắt điện thực sự, tránh nhầm màn hình tối do ngủ thành máy đã tắt hoàn toàn của 電源が切れる. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã đối chiếu từng câu được chọn với bài gốc; soát câu mẫu, câu kết, câu bẫy, bản dịch và cách chia.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
