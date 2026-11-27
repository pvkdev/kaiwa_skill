# Kiểm tra bản lưu JLPT N3 tháng 12/2023

Kiểm tra ngày 27/11/2026 theo giờ Nhật Bản. Các liên kết tính từ thư mục này. Kết quả dựa trên dữ liệu cục bộ.

**Kết luận**. Đủ đề, lời giải, dữ liệu nghe và file offline. Phụ lục phần đọc có 22 liên kết gãy. Cả hai HTML có lớp phủ khi lưu.

| Bản lưu | Đáp án và lời giải | Cặp Nhật–Việt | Script | Cặp mốc audio |
| --- | ---: | ---: | ---: | ---: |
| [Từ vựng, ngữ pháp, đọc hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (27_11_2026 23：43：48).html>) | 73/73 | 145 có chữ, 123 link đúng | — | — |
| [Nghe hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (27_11_2026 23：44：50).html>) | 28/28 | 160/160 dòng script | 28/28 | 28/28 |

- **Phần đọc.** Mục 124–145 ở dòng HTML 4811–4875 dẫn tới các ID `jlpt-origin-124` đến `jlpt-origin-145` đã vắng mặt. Cả 22 mục vẫn có chữ Nhật và bản Việt trong phụ lục. Chữ Nhật của từng mục tìm được trong bảng thông tin của khu trượt tuyết Asayama ở dòng 3988. 123 mục còn lại khớp dòng gốc và tooltip.
- **Phần nghe.** Cả 160 cặp có link đúng. 28 đoạn chép nguyên văn khớp các khung script. Cả 28 mốc cắt khớp phụ lục, theo thứ tự và nằm trong thời lượng file. Mốc đầu là 187,49–260,98 giây và mốc cuối là 2487,34–2510,72 giây.
- **Audio và ảnh.** [JLPT-N3-2023-12.mp3](JLPT-N3-2023-12.mp3) dài **42:04,4**, khớp thời lượng ghi trong HTML. FFmpeg giải mã toàn bộ MP3 và cả sáu ảnh PNG nhúng thành công.
- **Hiển thị.** Lớp phủ “Developer Tools đang mở” được lưu trong HTML phần đọc ở dòng 4955 và phần nghe ở dòng 3046. Hai trang cũng lưu thuộc tính làm mờ, nên có thể bị che khi mở offline.

Đã rà nghĩa theo mẫu ở đầu, giữa và cuối mỗi phần. Kiểm mốc theo dữ liệu lưu, chưa nghe đối chiếu từng biên cắt. Repo chưa có bản độc lập cùng cấp và kỳ để đối chiếu.
