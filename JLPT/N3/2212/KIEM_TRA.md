# Kiểm tra bản lưu JLPT N3 tháng 12/2022

Kiểm tra ngày 27/11/2026 theo giờ Nhật Bản. Các liên kết tính từ thư mục này. Kết quả dựa trên hai file HTML và một file MP3 cục bộ.

**Kết luận**. Bộ `2212` đủ dữ liệu đề và tài nguyên nghe. Hai HTML lưu kèm lớp phủ và hiệu ứng làm mờ, có thể ảnh hưởng khi mở offline.

| Bản lưu | Đáp án và lời giải | Cặp Nhật–Việt | Script | Cặp mốc audio |
| --- | ---: | ---: | ---: | ---: |
| [Từ vựng, ngữ pháp, đọc hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (27_11_2026 23：50：22).html>) | 73/73 | 146/146 | — | — |
| [Nghe hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (27_11_2026 23：51：56).html>) | 28/28 | 168/168 dòng script | 28/28 | 28/28 |

- **Phụ lục.** Cả 314 cặp Nhật–Việt khớp chữ Nhật và tooltip đã lưu, có liên kết về đúng dòng. Cả 101 lời giải trong phụ lục đều khớp lời giải trong đề. Đã rà nghĩa theo mẫu ở đầu, giữa và cuối mỗi phần.
- **Script và mốc.** Cả 28 đoạn chép nguyên văn khớp khung script gốc. Các mốc đầu–cuối theo thứ tự, khớp giữa khung gốc và phụ lục, nằm trong thời lượng MP3. Mốc đầu là 118,98–186,41 giây, mốc cuối là 2159,06–2183,91 giây. Chưa nghe đối chiếu từng biên cắt.
- **Audio và ảnh.** [JLPT-N3-2022-12.mp3](JLPT-N3-2022-12.mp3) dài **36:31,5**, khớp thời lượng ghi trong HTML. FFmpeg giải mã toàn bộ MP3 và ảnh PNG nhúng ở câu nghe 3, dòng HTML 426. Phần đọc có hai bảng HTML. HTML nghe chỉ ghi nguồn và mốc, nên khi dùng offline cần giữ MP3 đi kèm.
- **Hiển thị offline.** Lớp phủ “Developer Tools đang mở” nằm ở dòng 4975 của HTML phần đọc và dòng 3067 của HTML phần nghe. Cả hai trang lưu thuộc tính làm mờ. Đánh giá hiển thị dựa trên mã đã lưu.

Repo chưa có bản độc lập cùng cấp và kỳ để đối chiếu.
