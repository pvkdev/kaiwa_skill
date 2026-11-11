# Rà soát toàn sách — 2026-11-11

Phạm vi PDF vật lý 1–152 đã được mở ảnh và đối chiếu với phần học tương ứng: bìa, hướng dẫn, 10 bài ở 本冊, trang cuối 本冊, bìa và mục lục 別冊, toàn bộ script, 単語表, 解答 và bìa sau. Các trang giấy chỉ có thông tin xuất bản được ghi rõ ở page evidence; chữ viết tay trên bản scan không được chép thành đáp án in. Mọi trang có evidence với SHA-256 ảnh render và PDF gốc.

Sau lượt viết đầu, rà riêng chức năng bài tập trong cả 10 bài PDF12–91: chỉ dẫn, từng lượt Nhật in, lựa chọn, ô trống, vị trí bản Việt sau đề. Bài 3–10 được phục hồi các bản Việt từng lượt/lựa chọn từng bị tóm; Bài 1–2 đã có bản Việt đủ cho các vùng tương ứng. Đối chiếu ảnh thêm tại PDF28, 35, 36, 43, 44, 51, 52, 59, 60, 67, 68, 75, 76, 83, 84, 91; PDF44 có một lỗi chép cấu trúc lựa chọn đã sửa. Đáp án PDF142–151 nằm riêng sau các hoạt động, không dùng để điền đề. Rà nghĩa các mảnh đáp án theo câu đề, sửa PDF142/146/148/150; các mã và cụm Nhật in giữ nguyên.

Audio inventory ghi CD 2枚 và các mã in thực tế, đối chiếu với bài/hoạt động/trang; tệp nghe chưa kiểm. Không dựng thêm lời audio chưa in. Bảng 単語表 giữ cách đọc là dữ liệu học, khác furigana phụ trên ví dụ.

Hai bất nhất của bản in vẫn là `needs_review` hẹp: PDF83 ghi chọn a〜e nhưng chỉ có phương án a–d; PDF119 in hai nhãn B liên tiếp trong một đoạn script. Page/unit/chapter liên quan có issue khớp; toàn bộ trang và chương khác đã author_checked. Chúng không được tự sửa hay suy ra đáp án/vai bị thiếu.

Build full scope tạo 26 chapter/227 unit. Kiểm định `--allow-source-issues` có 0 lỗi và 13 cảnh báo: bốn cảnh báo là hai issue nguồn lặp ở page/unit; chín cảnh báo ô trống là giới hạn so sánh dòng của validator. Đã đọc lại ngữ cảnh của cả chín: sáu cảnh báo tại chỉ dẫn `CDを聞いて、＿＿に書いてください`/câu điểm nghe, trong đó ô trống chỉ ký hiệu vị trí điền, bản Việt chỉ dẫn giữ ý chứ không lặp hình dạng ký hiệu; ba cảnh báo còn lại do ô đề nằm ở các dòng câu/bảng sau chỉ dẫn. Các câu và bảng bài tập vẫn giữ ô theo ảnh; không sửa số ô để giảm cảnh báo.
