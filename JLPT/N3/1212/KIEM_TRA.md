# Kiểm tra bản lưu JLPT N3 tháng 12/2012

Kiểm tra ngày 28/11/2026 theo giờ Nhật Bản. Các liên kết tính từ thư mục này. Kết quả dựa trên hai HTML và một MP3 cục bộ.

**Kết luận**. Đủ đề, bản dịch, lời giải và tài nguyên nghe. MP3 có hơn 10 phút âm lượng thấp sau mốc câu cuối. Hai HTML lưu kèm lớp phủ và hiệu ứng làm mờ.

| Bản lưu | Đáp án và lời giải | Cặp Nhật–Việt | Script | Cặp mốc audio |
| --- | ---: | ---: | ---: | ---: |
| [Từ vựng, ngữ pháp, đọc hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (28_11_2026 00：52：16).html>) | 74/74 | 253/253 | — | — |
| [Nghe hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (28_11_2026 00：53：03).html>) | 28/28 | 268/268, gồm 228 dòng script và 40 dòng đề | 28/28 | 28/28 |

- **Phụ lục.** Cả 521 cặp Nhật–Việt khớp dòng Nhật và tooltip đã lưu, có liên kết đúng. Cả 102 lời giải trong phụ lục khớp lời giải trong đề. Phần đọc giữ một bảng HTML.
- **Script và mốc.** Cả 28 đoạn chép nguyên văn khớp khung script. Mốc theo thứ tự, khớp phụ lục và nằm trong thời lượng MP3. Câu 1 ghi 123,97–189,64 giây và câu 28 ghi 2141,40–2164,88 giây. FFmpeg đo phần sau mốc cuối có khoảng 608,3 giây liên tục dưới ngưỡng −45 dB.
- **Audio và ảnh.** [JLPT-N3-2012-12.mp3](JLPT-N3-2012-12.mp3) dài **46:13,2**, khớp HTML. FFmpeg giải mã toàn bộ MP3 và sáu ảnh JPEG nhúng thành công. Khi nghe offline, mở MP3 riêng và tra mốc trong HTML.
- **Hiển thị.** Lớp phủ “Developer Tools đang mở” nằm ở dòng 5443 của phần đọc và dòng 3404 của phần nghe. Hai trang lưu thuộc tính làm mờ.

Đã rà nghĩa theo mẫu ở đầu, giữa và cuối mỗi phần. Chưa nghe đối chiếu từng biên cắt. Repo chưa có bản độc lập cùng cấp và kỳ để đối chiếu.
