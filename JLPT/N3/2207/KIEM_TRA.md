# Kiểm tra bản lưu JLPT N3 tháng 07/2022

Kiểm tra ngày 27/11/2026 theo giờ Nhật Bản. Các liên kết tính từ thư mục này. Kết quả dựa trên hai file HTML và một file MP3 cục bộ.

**Kết luận**. Đủ đề, lời giải, transcript, mốc và tài nguyên nghe. Phụ lục phần đọc có 30 liên kết gãy, nhưng cả 30 mục vẫn giữ chữ Nhật và bản Việt. Hai HTML có lớp phủ khi lưu.

| Bản lưu | Đáp án và lời giải | Cặp Nhật–Việt | Script | Cặp mốc audio |
| --- | ---: | ---: | ---: | ---: |
| [Từ vựng, ngữ pháp, đọc hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (27_11_2026 23：54：18).html>) | 72/72 | 237 có chữ, 207 link đúng | — | — |
| [Nghe hiểu](<Thi thử JLPT N3 online, chọn kỳ thi và phần thi ｜ VNJPCLUB (27_11_2026 23：55：04).html>) | 28/28 | 178/178 dòng script | 28/28 | 28/28 |

- **Phần đọc.** Đề lưu liên tục từ câu 1 đến câu 72 và có đủ 72 đáp án đúng, lời giải. Trong phụ lục, 30 mục mang nhãn dòng 225–254 có liên kết về ID không còn trong HTML. Các mục này nằm ở dòng HTML 5006–5094. Cả 30 cặp đều còn nội dung và chữ Nhật đối chiếu được với bảng lớp guitar Nakamura ở dòng 3936. 207 mục còn lại khớp chữ Nhật, tooltip và liên kết.
- **Phần nghe.** Cả 178 cặp Nhật–Việt có link đúng. 28 đoạn chép nguyên văn khớp khung script. 28 cặp mốc trong phụ lục khớp dữ liệu trình phát, theo thứ tự và nằm trong thời lượng MP3. Mốc câu 1 là 121,94–178,77 giây, mốc câu 28 là 2301,33–2330,37 giây.
- **Audio và ảnh.** [JLPT-N3-2022-07.mp3](JLPT-N3-2022-07.mp3) dài **39:44,8**, khớp thời lượng ghi trong HTML nghe. FFmpeg giải mã toàn bộ MP3 và cả sáu ảnh PNG nhúng thành công. Khi nghe offline, mở MP3 riêng và tra mốc trong HTML.
- **Hiển thị.** Lớp phủ “Developer Tools đang mở” được lưu ở dòng 5168 của phần đọc và dòng 3118 của phần nghe. Hai trang cũng lưu thuộc tính làm mờ, nên nội dung có thể bị che khi mở offline.

Đã rà nghĩa theo mẫu ở đầu, giữa và cuối mỗi phần. Kiểm mốc theo dữ liệu lưu, chưa nghe đối chiếu từng biên cắt. Repo chưa có bản độc lập cùng cấp và kỳ để đối chiếu.
