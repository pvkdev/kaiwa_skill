# Lưu đề và lời giải JLPT bằng SingleFile

[bookmarklets.html](bookmarklets.html) chứa các bookmarklet dùng trên trang thi thử VNJPCLUB. Các đường dẫn trong tài liệu này tính từ thư mục `JLPT/tools/`.

| Dấu trang | Chạy ở đâu | Tác dụng |
| --- | --- | --- |
| **Chọn đáp án 1** | Trang đang làm bài | Bấm lựa chọn đầu tiên của từng nhóm radio và báo số nhóm tìm thấy, số nhóm vừa thay đổi. |
| **Chuẩn bị lưu JLPT** | Trang đã có kết quả | Bật Dịch và Giải thích nếu khả dụng, mở script nghe, rê chuột qua các dòng và gom nội dung vào phụ lục cuối trang. |
| **Tải audio JLPT** | Trang phần thi nghe hoặc bản SingleFile có phụ lục | Lưu file nghe tổng từ nguồn audio đã có trên trang. |
| **Khôi phục CSS JLPT** | Tab VNJPCLUB thiếu CSS hoặc bản HTML đề thi lưu cục bộ | Chèn các stylesheet còn thiếu từ bản SingleFile cũ do bạn chọn. |

## Cài vào Chrome hoặc Edge

1. Mở `bookmarklets.html` từ bản sao repo trên máy. Bật thanh dấu trang bằng `Ctrl+Shift+B`.
2. Kéo các nút dấu trang cần dùng lên thanh dấu trang.
3. Nếu thao tác kéo không được, dùng nút **Sao chép URL** tương ứng. Tạo dấu trang mới, đặt tên như trên và dán cả chuỗi bắt đầu bằng `javascript:` vào ô URL của dấu trang. Nếu nút sao chép yêu cầu `Ctrl+C`, bấm tổ hợp phím khi ô URL đang được chọn.
4. Nếu đã cài **Chuẩn bị lưu JLPT** từ bản trước, thay URL của dấu trang cũ bằng URL mới.

## Thử khôi phục bố cục

1. Mở `bookmarklets.html`, tìm **Khôi phục bố cục khi trang mất CSS** và chọn một bản SingleFile trước đó có giao diện đầy đủ, chẳng hạn phần đọc ở `../N3/1812/`.
2. Khi trang báo đã đọc CSS, kéo **Khôi phục CSS JLPT** lên thanh dấu trang. Mở tab VNJPCLUB đang bị vỡ và bấm dấu trang đó. Hiệu lực chỉ trên tab hiện tại cho đến khi tải lại hoặc chuyển trang.
3. Thử **Dịch**, **Giải thích** hoặc **Script nghe hiểu**. Nếu bố cục đã trở lại mà nút vẫn đứng yên, trang cần tải được JavaScript gốc. Có thể đóng quảng cáo xen trang rồi quay lại URL sạch và tải lại bằng `Ctrl+Shift+R`.

Bookmarklet đọc CSS từ file đã chọn và giữ lại các khối có tên nhận diện được. Nó chỉ chèn stylesheet còn thiếu, dùng tài nguyên đã nhúng và không khởi tạo truy cập mạng để lấy CSS.

## Lưu một phần thi

1. Mở phần thi cần lưu. Nếu muốn điền nhanh đáp án mẫu, bấm **Chọn đáp án 1** khi đề đang mở. Bookmarklet này có thể thay lựa chọn đã điền. Nó ưu tiên input có tên bắt đầu bằng `answer[` và dùng các radio có tên trên trang làm dự phòng, nên hãy kiểm tra số câu báo về và các lựa chọn trước khi tự nộp bài.
2. Khi trang kết quả hiện ra, bấm **Chuẩn bị lưu JLPT**. Giữ tab mở và đợi **Đã rà xong**. Nút **Dừng thu thập** giữ lại phần đã lấy nếu cần dừng giữa chừng.
3. Kiểm tra **Nội dung đã mở để lưu offline** ở cuối trang. Mỗi dòng đề hoặc script đã rà có cặp **Nhật / Việt**, số câu, số dòng và lựa chọn nếu có. Liên kết **Về vị trí gốc** trỏ vào dòng tương ứng. Nếu thấy `[chưa lấy được]`, mở script hoặc rê chuột thủ công ở chỗ đó rồi bấm lại **Chuẩn bị lưu JLPT**. Lần chạy lại dùng các bản dịch đã thu được trên tab.
4. Bấm biểu tượng **SingleFile** sau khi kiểm tra phụ lục. Mở bản HTML vừa lưu và tìm **Nội dung đã mở để lưu offline** bằng `Ctrl+F`. Kiểm tra một vài cặp Nhật–Việt, lời giải và mốc audio nếu có. Nếu lưu cả đề và phần nghe, lặp lại trên từng trang kết quả.

## Audio và giới hạn của bản lưu

1. Trên trang phần thi nghe, bấm **Tải audio JLPT**. Nếu chưa thấy nguồn audio, bấm phát trình nghe chính một lần rồi thử lại.
2. Với nguồn cùng trang, trình duyệt tải trực tiếp file tổng. Nếu nguồn mở trong tab mới, dùng **Ctrl+S** hoặc nút **Tải xuống** của trình phát trong tab đó.
3. Để file audio cạnh bản HTML. Lấy các mốc bắt đầu và kết thúc từ phụ lục khi cần tra đoạn tương ứng.

- Khi trang cung cấp dữ liệu, phụ lục giữ nguồn audio, thời lượng, mốc bắt đầu hoặc kết thúc, đoạn `#t=` và cue phụ đề. Giá trị đi cùng tên thuộc tính hoặc đơn vị gốc. Trình phát trong script được ghi cùng số câu và số dòng khi xác định được dòng tương ứng.
- Số **Mục thông tin audio** là số vị trí có dữ liệu đọc được, có thể gồm cả thời lượng của trình phát tổng. Muốn xác nhận hai đoạn dùng chung file, đối chiếu phần nguồn trước `#t=` và so sánh mốc của từng đoạn. Một dòng `Đồng hồ hiển thị` ghi đúng giá trị trên trình phát tại thời điểm thu.
- Bookmarklet đọc nội dung trên trang và gọi thao tác bấm, rê chuột. Trang có thể tải thêm dữ liệu khi nhận các thao tác này. Lời giải bị khóa, transcript chưa tải hoặc tooltip không phản hồi có thể xuất hiện dưới dạng mục thiếu. URL hoặc mốc audio trong phụ lục chỉ phục vụ tra cứu. Khả năng phát offline phụ thuộc vào việc bản lưu có chứa file audio.

## Ghi chú đối chiếu

Trong các bản SingleFile kiểm tra cục bộ, bốn phần nghe có nút **Script nghe hiểu** và tất cả khung chứa transcript đều trống. Các trình phát chính hiển thị thời lượng trong bảng. Nguồn audio và mốc riêng theo câu vẫn cần đối chiếu khi script đã mở.

| Bản nghe | Ô có transcript | Thời lượng trình phát chính |
| --- | --- | --- |
| N3 2017-12 | 0/28 | 37:44 |
| N3 2018-07 | 0/28 | 37:50 |
| N3 2018-12 | 0/28 | 40:57 |
| N2 2018-12 | 0/29 | 39:29 |

Bản N2 2018-12 mới trong `../N2/1812_1/` lưu đủ 29 script và 29 khoảng audio. Đoạn cuối phục vụ câu 29 và 30. Phần nghe có 253 cặp Nhật–Việt trong script và 44 cặp của đề. Phần từ vựng, ngữ pháp và đọc hiểu có 337 cặp. Cả hai phần có đủ lời giải và đáp án theo bản nguồn.

Trang cài đặt lưu nguyên mã **Chọn đáp án 1** đã cung cấp. Bookmarklet **Chuẩn bị lưu JLPT** đã được kiểm thử cục bộ với tooltip tạm thời, lời giải bị khóa và mốc cắt dùng chung một file audio. Kết quả trên VNJPCLUB thực tế cần được đối chiếu từ phụ lục sau khi chạy.
