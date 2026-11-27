# Kiểm tra bản lưu JLPT N3 tháng 07/2019

Kiểm tra ngày 28/11/2026 theo giờ Nhật Bản. Các liên kết tính từ thư mục này. Kết quả dựa trên hai file HTML và một file MP3 cục bộ.

**Kết luận**. Bản lưu đủ dữ liệu để đọc và nghe lại. Form nghe thiếu nút chọn phương án 4 ở câu 13–15. Cả ba phương án 4 vẫn còn trong transcript. Hai HTML có lớp phủ khi lưu.

| Bản lưu | Đáp án xác định được | Lời giải | Cặp Nhật–Việt | Script | Cặp mốc audio |
| --- | ---: | ---: | ---: | ---: | ---: |
| [Từ vựng, ngữ pháp, đọc hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (28_11_2026 00：11：09).html>) | 74/74 | 74/74 | 185/185 | — | — |
| [Nghe hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (28_11_2026 00：11：43).html>) | 28/28 | 28/28 | 218/218, gồm 170 dòng script và 48 dòng đề | 28/28 | 28/28 |

- **Form nghe.** Câu 13–15, tức câu 1–3 của `問題3`, chỉ có ba nút chọn trong HTML. Phương án 4 còn trong script của từng câu ở các dòng HTML 1022, 1068 và 1114. Câu 13 vẫn đánh dấu đúng phương án 1. Với câu 14 và 15, form thiếu lựa chọn đúng nên công cụ chỉ đếm được 26/28 câu có nút đánh dấu. Dòng kết quả ở 1072 và 1118 đều ghi **đáp án đúng là 4**, khớp với lời giải và nội dung lựa chọn trong script.
- **Phụ lục.** Cả 403 cặp Nhật–Việt khớp dòng Nhật và tooltip đã lưu, có liên kết về đúng vị trí. Cả 102 lời giải trong phụ lục khớp lời giải trong đề. Đã rà nghĩa theo mẫu ở đầu, giữa và cuối mỗi phần.
- **Script và mốc.** Cả 28 đoạn chép nguyên văn khớp khung script. Cả 28 cặp mốc khớp phụ lục, theo thứ tự và nằm trong thời lượng MP3. Câu 1 ghi 58,74–121,14 giây, câu 28 ghi 2085,22–2108,29 giây. Chưa nghe đối chiếu từng biên cắt.
- **Audio và ảnh.** [JLPT-N3-2019-07.mp3](JLPT-N3-2019-07.mp3) dài **35:38**, khớp HTML. FFmpeg giải mã được toàn bộ MP3 và cả bốn ảnh PNG nhúng ở câu nghe 16–19. Phần đọc giữ hai bảng HTML. Khi nghe offline, mở MP3 riêng và tra mốc trong HTML.
- **Hiển thị offline.** Lớp phủ “Developer Tools đang mở” nằm ở dòng 5129 của phần đọc và dòng 3210 của phần nghe. Hai trang cũng lưu thuộc tính làm mờ.

Repo chưa có bản độc lập cùng cấp và kỳ để đối chiếu xem lỗi số lựa chọn xuất hiện từ trang hay từ lần lưu. Đánh giá hiển thị dựa trên mã HTML đã lưu.
