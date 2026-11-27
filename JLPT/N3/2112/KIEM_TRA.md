# Kiểm tra bản lưu JLPT N3 tháng 12/2021

Kiểm tra ngày 27/11/2026 theo giờ Nhật Bản. Các liên kết tính từ thư mục này. Kết quả dựa trên hai file HTML và một file MP3 cục bộ.

**Kết luận**. Đủ đề, lời giải, transcript, mốc và tài nguyên nghe. Phụ lục phần đọc có 38 liên kết gãy, nhưng cả 38 mục vẫn giữ chữ Nhật và bản Việt. Hai HTML có lớp phủ khi lưu.

| Bản lưu | Đáp án và lời giải | Cặp Nhật–Việt | Script | Cặp mốc audio |
| --- | ---: | ---: | ---: | ---: |
| [Từ vựng, ngữ pháp, đọc hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (27_11_2026 23：56：48).html>) | 73/73 | 218 có chữ, 180 link đúng | — | — |
| [Nghe hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (27_11_2026 23：57：53).html>) | 28/28 | 177/177 dòng script | 28/28 | 28/28 |

- **Phần đọc.** Các mục mang nhãn dòng 181–218 trong phụ lục, ở dòng HTML 5014–5126, trỏ đến ID không còn trong file. Cả 38 mục còn chữ Nhật và bản Việt. Chữ Nhật của từng mục đối chiếu được với bảng hướng dẫn sử dụng thư viện thành phố Aoi ở dòng 3989. 180 mục còn lại khớp chữ Nhật, tooltip và liên kết.
- **Phần nghe.** Cả 177 cặp Nhật–Việt có link đúng và 28 đoạn chép nguyên văn khớp khung script. 28 cặp mốc khớp phụ lục, theo thứ tự và nằm trong thời lượng MP3. Mốc câu 1 là 199,75–261,11 giây, mốc câu 28 là 2559,30–2580,65 giây.
- **Audio và ảnh.** [JLPT-N3-2021-12.mp3](JLPT-N3-2021-12.mp3) dài **43:17,4**, khớp thời lượng ghi trong HTML. FFmpeg giải mã toàn bộ MP3 và cả tám ảnh PNG nhúng trong đề nghe. Khi nghe offline, mở MP3 riêng và tra mốc trong HTML.
- **Hiển thị offline.** Lớp phủ “Developer Tools đang mở” nằm ở dòng 5207 của phần đọc và dòng 3116 của phần nghe. Hai trang cũng lưu thuộc tính làm mờ, nên nội dung có thể bị che khi mở offline.

Đã rà nghĩa theo mẫu ở đầu, giữa và cuối mỗi phần. Kiểm mốc theo dữ liệu lưu, chưa nghe đối chiếu từng biên cắt. Repo chưa có bản độc lập cùng cấp và kỳ để đối chiếu.
