# Biên bản bàn giao Minna N5–N4 · 25/11/2026

## Hai gói bàn giao

- [Gói Markdown cho admin Harumii](../exports/grammar-upload/minna-n5-n4-grammar-r2.zip) có 180 file đã biên tập, gồm 90 N5 và 90 N4. Chọn ZIP này trong **Biên soạn với AI** để xem diff trước khi áp dụng.
- [Gói preview 50 bài](../exports/harumii/minna-50-exercises-preview.zip) chứa thứ tự node theo từng bài, file từ vựng tham chiếu, bài giảng nguồn và bộ bài tập có đáp án, lời giải. Gói này phục vụ preview và gắn ID trước migration. Các UUID unit, template, session và URL phát media phải lấy từ môi trường Harumii đích. Các gói ZIP lẻ theo đợt là bản trung gian.

## Ngữ pháp và Renshuu B

Trang ngữ pháp của đủ 50 bài cung cấp 318 mục với công thức, nghĩa, cách dùng và 961 ví dụ Nhật–Việt có tham chiếu media. Các URL và khóa TTS cho biết cách nguồn tham chiếu bản đọc; 961 file audio chưa được tải và kiểm phát. Bảng từ Harumii có 2.229 mục. Preview đề xuất 97 nhóm theo thứ tự bản xuất, tối đa 30 từ mỗi nhóm. Các bài ngắn hoặc nhóm được chia đều có thể ít hơn 20 từ.

Mỗi mục có ID video ổn định, tiếp đến là node thực hành. Các nhóm dùng nhiều mẫu nằm sau mẫu cuối cần học. Video đang ở trạng thái lên kế hoạch. Ba kho bài tập cung cấp tổng cộng **1.738 câu**.

- 420 câu kiểm tra nhanh phủ cả 318 mẫu. Đã điều chỉnh 12 đề để phân định cách hiểu hoặc đáp án. Mỗi câu có ID lựa chọn đúng và lời giải tiếng Việt.
- 359 nhóm B có 359 bài luyện đại diện. Trong đó 100 câu chuyển thể trực tiếp từ drill và 259 câu luyện nhận diện dựa trên ví dụ Nhật–Việt của nhóm.
- Có thêm 959 bài luyện theo drill cụ thể. Tổng cộng 1.059 trong 1.471 drill gốc có biến thể làm được, gồm 17 đề được viết lại do bản gốc mơ hồ. 412 drill cần ảnh hoặc dữ kiện ngoài đề còn trong danh sách chờ. Tất cả khóa của biến thể được ghi là đáp án biên tập. Snapshot hiện tại chưa lưu trọn đáp án chính thức cho 1.471 drill. Biên bản khảo sát cũ của bài 39 ghi nhận 32 ID reveal, có một câu lưu chi tiết. [Độ phủ từng bài và từng nguyên nhân](renshuu-drill-round2.md).

Kiểm tra từ vựng sử dụng Sudachi để so sánh dạng từ trong đề và phương án với bản xuất của từng bài. Đã rút gọn ngữ cảnh ở bài 2 để học viên làm được câu これ mà chưa cần đọc 手に持っています. [Báo cáo có ID câu, bài xuất hiện từ và nghĩa để người biên tập tra lại](vocabulary-review.json). Kết quả nhận diện tự động còn phụ thuộc nghĩa của từ trong câu.

## Bài giảng Harumii

Đã kiểm toàn bộ 180 UUID, tên file và cấp độ so với bản xuất. 180 thành phần ZIP khớp byte với thư mục authored hiện hành, có 3.118 cặp H5 Nhật và H6 dịch Việt. Phần chuẩn hóa cấu trúc bảo toàn nội dung cũ. Những bài cần sửa nghĩa, cách chia hoặc hội thoại có chỉnh sửa riêng, mức độ biên tập khác nhau theo bài.

- Bài ～いい giữ năm cách dùng, chỉnh câu Nhật hỏng và dịch lại theo ngữ cảnh. Bài ～と言いました sửa câu dịch nhầm chuyến công tác Tokyo thành cuộc họp và chuyển chú thích Việt ra ngoài H5. Bài ～たらどうですか được tách từng lượt đối thoại.
- Bản N5 làm rõ だけ dùng được trong câu phủ định, phân biệt với しか cần vị ngữ phủ định. Bảng biến đổi động từ được giữ làm quy tắc. Bài vĩ tố tổng hợp vẫn có nhận định về giới tính và văn phong từ bản gốc, cần người biên tập đọc trong tình huống sử dụng trước khi áp dụng. [Biên bản N5](grammar-upgrade-2026-11-25-N5-final.md).
- Các báo cáo theo đợt lưu trạng thái ở thời điểm tạo. Gói tổng hợp r2 đã bao gồm các bài sau đó được xử lý và các sửa cuối khi rà chéo. [Lịch sử biên tập N4 và các đợt chuẩn hóa](grammar-upgrade-2026-11-25.md).

## Nội dung ngoài ngữ pháp

- Bài 1 và 39 đã chuẩn hóa tổng cộng 44 dòng shadowing Văn mẫu/A, cùng 99 lượt của C/Kaiwa. Có cặp Nhật–Việt, thông tin người nói khi nguồn cung cấp và tham chiếu đoạn audio theo dòng. Các biến thể C được xếp trước Kaiwa.
- Bài 39 có bài đọc ngắn về kimono và bài dài về Manjirō, với 7 câu JLPT Reading đã ghi căn cứ theo đoạn. Phần kiểm tra có 29 câu đủ Mondai 1–6. [Kiểm tra 29 câu và sửa câu 28 có hai cách hiểu](grammar-upgrade-assessment-39.md).
- Bài 1 và 39 có hai bài nghe mới, tổng cộng 4 câu, cùng script và MP3 tiếng Nhật đã giải mã bằng FFmpeg. Cần upload hai MP3 và gắn URL Harumii để học viên phát được. Gói có riêng một đoạn nghe mẫu để thử năm template. [Bản ghi, thời lượng và mã kiểm MP3](listening-supplemental-01-39.md).
- Số bài có snapshot là 2/50 cho từng phần shadowing, hội thoại, nghe và 1/50 cho từng phần đọc ngắn, đọc dài, kiểm tra. VNJPClub yêu cầu xác minh truy cập ở bước đọc ngắn của bài 1. Crawler đã lưu checkpoint theo từng phần để chạy tiếp khi nguồn cho truy cập. [Trạng thái từng bài](crawl-coverage.json).

## Kiểm migration

Đối chiếu checkout Harumii `031fd10e` ở editor giáo trình từ vựng và ngữ pháp. Năm template là chọn một, điền chỗ trống, chọn nhiều, đọc JLPT, nghe JLPT. Đường dán JSON của editor tạo ID lựa chọn mới ở mẫu chọn một/chọn nhiều nên có thể làm sai khóa. Gói dùng dữ liệu storage đã kiểm qua bộ lưu và bộ đọc của Harumii. Mẫu điền xuất marker `(...)` đúng theo mapper của phiên bản này. [Cấu trúc payload, binding và cách chạy lại](../references/TEMPLATES.md).

Bản nguồn cache đặt tại `sources/`; dữ liệu chuẩn hóa ở `normalized/`; đầu vào để sửa ở `authored/`; gói sinh ra ở `exports/`. Hai thư mục `sources/` và `exports/` nằm trong Git ignore của repo. Khi chuyển sang máy khác, mang theo snapshot hoặc bản lưu có checksum nếu cần tái tạo dữ liệu. Toàn bộ công việc trong đợt này diễn ra cục bộ, chưa upload lên Harumii.

Lần build cuối đạt 162/162 kiểm thử frontend và 5/5 kiểm thử Python. Đã mở lại cả hai ZIP, kiểm tập tin, SHA-256 và thứ tự các node. Số node dự kiến là 1.230, tính cả video, các node tùy chọn và phần chờ thu thập. Mã SHA-256 của ZIP ngữ pháp r2 là `c5dd0e65bece402ba840b84080da59715eb87a2c4af49a9ce5adc3831f2cd631`. Mã của ZIP preview là `5475b5d75a07f457807e297590c48bf353866a554663400f591392211da4e168`.
