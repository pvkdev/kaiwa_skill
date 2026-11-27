# Kiểm tra bản lưu JLPT N3 tháng 12/2018

Kiểm tra ngày 28/11/2026 theo giờ Nhật Bản. Các liên kết tính từ thư mục này. Đã rà hai HTML mới và một MP3 cục bộ, cùng bốn HTML đối chiếu trong `../old/1812/`.

**Kết luận**. Bộ hiện tại có đủ dữ liệu và tài nguyên, gồm MP3 đi kèm. Hai HTML lưu kèm lớp phủ và hiệu ứng làm mờ, có thể che nội dung khi mở offline.

| Bản lưu | Đáp án và lời giải | Cặp Nhật–Việt | Script | Cặp mốc audio |
| --- | ---: | ---: | ---: | ---: |
| [Từ vựng, ngữ pháp, đọc hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (28_11_2026 00：13：47).html>) | 74/74 | 269/269 | — | — |
| [Nghe hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (28_11_2026 00：15：26).html>) | 28/28 | 276/276, gồm 240 dòng script và 36 dòng đề | 28/28 | 28/28 |

- **Phụ lục.** Cả 545 cặp Nhật–Việt khớp với dòng Nhật và tooltip đã lưu, có liên kết về đúng vị trí. Cả 102 lời giải trong phụ lục khớp lời giải trong đề. Đã rà nghĩa theo mẫu ở đầu, giữa và cuối mỗi phần.
- **Đối chiếu bản cũ.** Các lựa chọn và đáp án đúng khớp cả hai lượt lưu ngày 26/11. So với lượt lưu lúc 13:21:58 và 13:26:58, cả 545 cặp Nhật–Việt, 102 lời giải, 28 cặp mốc và sáu ảnh đề nghe đều khớp. Lượt lưu lúc 11:33:52 và 11:36:56 còn ô dịch và script trống. Có 17 lời giải đã đổi chữ kể từ lượt lưu đó. [Biên bản lượt đầu](../old/1812/KIEM_TRA.md)
- **Script và mốc.** Cả 28 đoạn chép nguyên văn khớp khung script. Các mốc theo thứ tự, khớp giữa khung gốc và phụ lục, nằm trong thời lượng MP3. Câu 1 ghi 49,14–122,65 giây, câu 28 ghi 2411,65–2434,48 giây. Chưa nghe đối chiếu từng biên cắt.
- **Audio và ảnh.** [JLPT-N3-2018-12.mp3](JLPT-N3-2018-12.mp3) dài **40:57,8**, khớp thời lượng trong HTML. FFmpeg giải mã toàn bộ MP3 và sáu ảnh JPEG nhúng thành công. Phần đọc có một bảng HTML. Khi nghe offline, mở MP3 riêng và tra mốc trong HTML.
- **Hiển thị offline.** Lớp phủ “Developer Tools đang mở” nằm ở dòng 5450 của phần đọc và dòng 3428 của phần nghe. Hai trang lưu thuộc tính làm mờ. Bản nghe cũ lúc 13:26:58 không có dấu hiệu lớp phủ này trong HTML. Đánh giá hiển thị dựa trên mã đã lưu.
