# Chỉ preflight — 5500 câu giao tiếp tiếng Nhật trong sinh hoạt hàng ngày

**Trạng thái:** chuẩn bị bản đồ để clean sau này, không phải bản clean và không xác nhận corpus sẵn sàng. PDF có **136 trang vật lý**; manifest ingest hiện ghi **100 `verified`, 36 `needs_review`**. Các vùng bị che/cắt trong nguồn thuộc ingest; preflight này không sửa hoặc tự xác minh thay. Không init, không đổi scope, knowledge hay corpus.

## Nhan đề và ấn bản nhìn từ PDF

- Bìa PDF1, trang nhan đề PDF2 và colophon PDF136 đều in **`5500 câu giao tiếp tiếng Nhật trong sinh hoạt hàng ngày`**. Bìa/trang nhan đề còn in nhan đề Nhật `生活のために日本語会話文句 5500`; đây là dòng Nhật của chính bản sách, không suy từ tên file. Bìa ghi `Tri Thức Việt`, `Sato Toyoda (thực hiện CD)` và sách kèm CD/MP3. PDF2 in rõ **`(Tái bản lần 1)`**.
- Colophon PDF136 bên phải ghi **Nhà xuất bản Hồng Đức**, **ISBN 978-604-86-5757-4**, quyết định xuất bản ngày **16/05/2015**, in xong và nộp lưu chiểu **quý 3 năm 2015**. Đây là căn cứ ấn bản của PDF đang dùng; ngày tạo PDF 2017 trong metadata file không thay năm in của sách.
- Các ảnh **đã thực sự mở/đọc** trong preflight: PDF **1–7, 38, 66, 99, 112, 122, 127, 135–136**; xem thêm crop độ phân giải cao của mục lục PDF4 và colophon PDF136. Các trang khác chỉ được định vị theo mục lục hoặc raw chưa chốt, không được gọi là đã kiểm nội dung.

## Bản đồ cấu trúc và trang vật lý dự kiến

PDF là scan hai trang in trên một physical page. Từ PDF4 trở đi, trang PDF `n` thường có trang in `2n−2` bên trái, `2n−1` bên phải. **Các ranh giới panel dưới đây đã nhìn trực tiếp** ở PDF6, 38, 66, 99, 112, 122, 127, 136. Các chi tiết bên trong khoảng chưa mở ảnh vẫn là chỉ dẫn từ mục lục, cần rà khi clean full.

1. **Bìa/nhan đề/mục lục/lời đầu:** PDF1 là bìa trước và sau; PDF2 trang nhan đề; mục lục ở PDF3 bên phải, PDF4 cả hai panel và PDF5 bên trái (trang in 5–8); **Lời nói đầu** ở PDF5 bên phải–PDF6 bên trái (trang in 9–10). Lời đầu nêu cấu trúc mẫu câu cơ bản, đối thoại, cách diễn đạt tương tự/mở rộng và CD–MP3.
2. **CHƯƠNG I — BIỂU HIỆN CẢM XÚC CỦA BẢN THÂN:** từ **PDF6 bên phải / trang in 11** đến **PDF99 bên trái / in 196**. Bên trong có ba phần lớn, mỗi phần theo chủ đề nhỏ rồi kết bằng `Từ vựng quan trọng`:
   - **I. Thể hiện cảm xúc:** PDF6 bên phải–PDF38 bên trái, in **11–74**; 14 mục nhỏ từ `Vui vẻ` đến `Hờ hững, không quan tâm`, bảng từ vựng bắt đầu in **70** (khoảng PDF36). PDF6–7 cho thấy mẫu câu Nhật, romaji, nghĩa Việt, `Đối thoại`, `Diễn đạt tương tự` và câu mở rộng.
   - **II. Thể hiện nguyện vọng:** PDF38 bên phải–PDF66 bên trái, in **75–130**; 11 mục nhỏ từ `Yêu và ghét` đến `Thích và không thích`, bảng từ vựng bắt đầu in **127** (khoảng PDF64).
   - **III. Thể hiện ý kiến và quan điểm:** PDF66 bên phải–PDF99 bên trái, in **131–196**; mục nhỏ từ `Đặt câu hỏi` qua `Cho phép và ngăn cấm`/`Bày tỏ quan điểm`/`Không quyết đoán`, bảng từ vựng bắt đầu in **192** (khoảng PDF97). **Mục lục PDF4 có bất nhất thứ tự:** mục số 12 `Cho phép và ngăn cấm` ghi trang **190**, trong khi mục 13/14 ở panel tiếp ghi **184/187**. Giữ đây là điểm cần đối chiếu với ảnh trang học khi full, không sửa nhãn hay sắp lại theo suy đoán.
3. **CHƯƠNG II — SINH HOẠT THƯỜNG NGÀY:** từ **PDF99 bên phải / in 197** đến **PDF136 bên trái / in 270**, chia bốn phần lớn:
   - **I. Vận động:** PDF99 bên phải–PDF112 bên trái, in **197–222**; 6 mục từ `Thức dậy` đến `Đi ngủ`, từ vựng in **220** (khoảng PDF111).
   - **II. Ẩm thực:** PDF112 bên phải–PDF122 bên trái, in **223–242**; 7 mục từ `Ăn cơm` đến `Thanh toán tiền`, từ vựng in **240** (PDF121).
   - **III. Liên lạc qua điện thoại:** PDF122 bên phải–PDF127 bên trái, in **243–252**; 4 mục từ `Gọi điện thoại` đến `Gọi nhầm số và phá rối điện thoại`, từ vựng in **252** (PDF127 trái).
   - **IV. Phương tiện vận chuyển:** PDF127 bên phải–PDF136 bên trái, in **253–270**; 6 mục từ `Xe buýt` đến `Tìm bãi đậu xe`, từ vựng in **268–270** (PDF135–136 trái). Ảnh PDF136 xác nhận danh sách từ vẫn tiếp đến trang in 270; không dừng ở dòng mục lục in 268.
4. **Colophon:** PDF136 bên phải; dữ liệu ấn bản, không phải bài luyện hoặc đáp án.

## Dữ liệu học cần giữ khi clean full

Ảnh PDF6–7, 38, 66, 99, 112, 122, 127, 135–136 cho thấy mỗi nhóm triển khai qua **chủ đề tiếng Việt → câu Nhật → romaji → nghĩa Việt**, kèm nhiều khối **`Đối thoại`**, **`Diễn đạt tương tự`** và bảng **`Từ vựng quan trọng`** có chữ Nhật, furigana/cách đọc và nghĩa Việt. Giữ thứ tự, lượt người nói, câu tương tự, ví dụ, mối liên hệ đến chủ đề và các bảng từ; chỉ phân loại romaji/furigana nào thực sự phụ trợ sau khi đối chiếu từng trang. Hình minh họa người nói/tình huống cần chuyển thành text nếu mang quan hệ bổ sung; hình chỉ trang trí có thể bỏ. Bìa nói có CD/MP3 nhưng chưa thấy mã track cụ thể trên những trang học đã mở; không tự gán track. Mục lục và mẫu trang đã xem **không cho thấy bài tập điền trống hay đáp án riêng**; chưa kết luận cho toàn bộ trang chưa mở.

## Chưa chốt và điều kiện tiếp tục

- Corpus 36 trang `needs_review`, nhiều ảnh có gáy đen che chữ (thấy rõ ngay ở PDF38 và 66). Cần nguồn/ingest xử lý trước khi root giao clean full; preflight không dùng raw partial để lấp chữ bị che.
- Bản đồ các tiểu mục giữa ranh giới lấy từ TOC, chưa phải xác nhận bằng ảnh từng trang. Thứ tự thực của mục 12–14 ở Chương I/III phải đối chiếu ảnh học; không theo TOC một cách máy móc.
- Khi scan chuyển `ready_for_fork`, **báo root trước**; chỉ sau phân công mới xác nhận chapter plan, init snapshot và clean. Không dùng nhan đề/tổng số câu trên bìa làm bằng chứng đã đếm đủ 5.500 câu.
