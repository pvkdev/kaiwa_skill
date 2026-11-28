# Kiểm tra bản lưu JLPT N2 ngày 28/11/2026

Đã rà 8 HTML và 4 MP3 của các kỳ 07/2024, 12/2024, 07/2025 và 12/2025 theo skill `jlpt-singlefile-check`. Các bản trong `old/` thuộc kỳ 2018 nên không có bản độc lập cùng kỳ để đối chiếu. Kiểm tra dựa trên các file cục bộ và giờ Nhật Bản.

**Kết luận.** Cả bốn bộ dùng được làm nguồn biên soạn. Phần viết giữ đủ dữ liệu tiếng Nhật trong phạm vi DOM đã kiểm để giao AI dịch. Phần nghe có script, bản dịch, lời giải và MP3 tương ứng. Cả tám HTML lưu kèm lớp phủ toàn màn hình và `filter:blur(6px)` trên `body`, nên bản lưu nguyên trạng có thể bị che khi mở trực tiếp.

## File đã rà

- **07/2024** · [HTML viết](<2407/Thi thử JLPT N2 bằng đề thi các năm ｜ VNJPCLUB (28_11_2026 10：46：36).html>) · [HTML nghe](<2407/Thi thử JLPT N2 bằng đề thi các năm ｜ VNJPCLUB (28_11_2026 10：44：46).html>) · [MP3](2407/JLPT-N2-2024-07.mp3). Đề viết có 2 bảng. Phụ lục viết có 0/53 mục có bản dịch và còn 28 dòng dịch trong tooltip của tài liệu cuối đề. Đề nghe có 209/209 cặp Nhật–Việt. MP3 dài 48:05,600.
- **12/2024** · [HTML viết](<2412/Thi thử JLPT N2 bằng đề thi các năm ｜ VNJPCLUB (28_11_2026 10：46：15).html>) · [HTML nghe](<2412/Thi thử JLPT N2 bằng đề thi các năm ｜ VNJPCLUB (28_11_2026 10：41：24).html>) · [MP3](2412/JLPT-N2-2024-12.mp3). Đề viết có 3 bảng. Phụ lục viết có 0/65 mục có bản dịch và còn 30 dòng dịch trong tooltip của tài liệu cuối đề. Đề nghe có 199/199 cặp Nhật–Việt và 1 ảnh PNG ở `#q-2`. MP3 dài 48:22,900.
- **07/2025** · [HTML viết](<2507/Thi thử JLPT N2 bằng đề thi các năm ｜ VNJPCLUB (28_11_2026 10：45：58).html>) · [HTML nghe](<2507/Thi thử JLPT N2 bằng đề thi các năm ｜ VNJPCLUB (28_11_2026 10：38：50).html>) · [MP3](2507/JLPT-N2-2025-07.mp3). Đề viết có 2 bảng. Phụ lục viết có 0/40 mục có bản dịch và còn 29 dòng dịch trong tooltip của tài liệu cuối đề. Đề nghe có 208/208 cặp Nhật–Việt. MP3 dài 48:00,201.
- **12/2025** · [HTML viết](<2512/Thi thử JLPT N2 bằng đề thi các năm ｜ VNJPCLUB (28_11_2026 10：45：31).html>) · [HTML nghe](<2512/Thi thử JLPT N2 bằng đề thi các năm ｜ VNJPCLUB (28_11_2026 10：36：33).html>) · [MP3](2512/JLPT-N2-2025-12.mp3). Đề viết có 2 bảng. Phụ lục viết có 0/83 mục có bản dịch và còn 35 dòng dịch trong tooltip của tài liệu cuối đề. Đề nghe có 206/206 cặp Nhật–Việt và 1 ảnh PNG ở `#q-2`. MP3 dài 51:22,840.

## Phần từ vựng, ngữ pháp và đọc hiểu

- Mỗi kỳ có 71/71 câu theo thứ tự `#q-1` đến `#q-71`. Cả 71 câu có thân câu, bốn lựa chọn có nội dung và khóa `.choice-correct` khớp `.result-line`. DOM đề lưu 71/71 lời giải ở `.complete-answer`. Phụ lục viết chưa thu lời giải nên cả bốn file có 0/71 ở phụ lục.
- Mỗi kỳ giữ 12/12 khối `.passage-content` không rỗng, gồm bài điền khuyết và các đoạn đọc, cùng một tài liệu tra cứu riêng ở `.vnjp-dokkai-thongtindich` sau câu 71. Tài liệu đó thuộc `問題 14`, dùng cho câu 70–71. Các bảng còn nội dung tiếng Nhật dưới dạng HTML.
- Người sưu tầm đã chủ động dừng thu bản dịch phần viết để dùng AI dịch sau. Phụ lục có 241 mục bản dịch dang dở, đều rỗng phần Việt. Các tooltip có nội dung chỉ nằm trong tài liệu tra cứu cuối đề.
- **Cả bốn kỳ, `問題 9`.** Hướng dẫn ghi phạm vi `[48]–[52]`. Đoạn văn và câu hỏi thực tế có bốn ô `[48]–[51]`. Câu `#q-52` có đoạn và câu hỏi riêng ở `問題 10`.
- **12/2025, `#q-37`–`#q-42`.** Khối ở dòng 2129 hiển thị lại tiêu đề `問題 6` và hướng dẫn chọn cách dùng từ. Sáu câu trong khối là điền khuyết ngữ pháp, nằm giữa `問題 7` và `問題 8`. Cần rà khi ánh xạ nhóm để tránh gộp vào Mondai 6 của phần từ vựng.

## Phần nghe và tài nguyên offline

- Mỗi kỳ có 30/30 câu, 30/30 khóa khớp giữa hai vị trí trong HTML và 30/30 lời giải khớp giữa đề và phụ lục. Có 29/29 khung script có nội dung và khớp bản chép trong phụ lục sau khi bỏ furigana, điều khiển và tooltip. `#q-29` và `#q-30` dùng chung khung cuối đặt ở `#q-30`, có cả hai câu hỏi trong script.
- Cả 822 cặp Nhật–Việt trong bốn đề nghe có nội dung và khớp tooltip gốc theo script kiểm tra. Đã đọc mẫu bản dịch ở đầu, giữa và cuối phần nghe của mỗi kỳ. Đã đọc mẫu lời giải phần viết ở các câu 1, 38 và 71. Phạm vi rà nghĩa là các mẫu này.
- Cả 29/29 mốc đầu–cuối của mỗi kỳ khớp giữa đề và phụ lục, theo thứ tự, trong thời lượng MP3. FFmpeg giải mã hết 4 MP3 và 2 PNG nhúng. Các bản viết không có ảnh đề riêng. HTML nghe lưu URL audio ngoài và mốc, nên giữ MP3 cạnh HTML để mở riêng khi dùng offline.
- CSS nền `generate-style-css` còn trong cả tám file. Lớp phủ `#vnjp-devtools-overlay` lưu ở các dòng 3354 và 4609 (07/2024, nghe và viết), 3313 và 4695 (12/2024), 3350 và 4603 (07/2025), 3340 và 4746 (12/2025). Thuộc tính làm mờ nằm ở dòng 51 trong cả tám file.

Đã kiểm cấu trúc, số lượng, dữ liệu hiển thị trong DOM và khả năng giải mã tài nguyên. Chưa nghe đối chiếu từng biên cắt, chạy HTML trong trình duyệt hoặc đối chiếu câu chữ với một nguồn độc lập. HTML và MP3 được giữ nguyên.
