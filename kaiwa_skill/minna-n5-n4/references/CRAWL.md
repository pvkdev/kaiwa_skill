# Crawl và biên soạn lộ trình Minna 1–50

Chạy từ `kaiwa_skill/minna-n5-n4/` trong repo. Công cụ trình duyệt dùng Python 3.10+, Playwright và Microsoft Edge đã cài. Cài gói Python bằng `py -m pip install playwright` trong môi trường dùng để crawl. Có thể dùng Chromium của Playwright với `py -m playwright install chromium` và `--browser chromium`.

## Crawl theo bài

```powershell
py -X utf8 scripts/crawl_minna.py --family grammar
py -X utf8 scripts/course_coverage.py --require grammar
py -X utf8 scripts/grammar_index.py
py -X utf8 scripts/crawl_minna.py --family all
pwsh -NoProfile -File scripts/crawl_b_answers.ps1 -Start 1 -End 50
py -X utf8 scripts/course_coverage.py --require b-answers
py -X utf8 scripts/course_coverage.py --require all
```

Hai chỉ mục ngữ pháp N5/N4 của VNJPClub cung cấp link cho bài 1–50. Các phần khác lấy link từ trang gốc của bài. Trình duyệt để trang render rồi ghi lại các section liên quan, ID, ruby, nút phát và bảng track vào `sources/lesson-NN/<phần>/<hash>.json`; một snapshot là một lần quan sát. `reports/crawl-coverage.json` ghi trạng thái và con trỏ snapshot mới nhất. Các đường dẫn snapshot tính từ workspace Minna. Để tái kiểm ở máy khác, mang theo thư mục `sources/` hoặc chạy crawl lại trên máy đích.

Dùng `--start 39 --end 39` để xử lý một bài, hoặc chạy lại lệnh cũ để tiếp tục phần thiếu. Khi nguồn đổi, dùng thêm `--refresh` trên khoảng bài cần cập nhật. Mỗi thời điểm chạy một tiến trình ghi coverage. So sánh danh mục cũ và mới theo cặp (số bài, ID nguồn), phát hiện đổi tên, đổi thứ tự, thêm/bớt mục. Đối chiếu cả nội dung snapshot cho những mục cùng ID. Trang thiếu link, đổi layout hoặc bị xác minh phải được ghi nhận để kiểm lại. Đối với layout mới, mở trang bình thường, xác minh nhóm thực tế, rồi sửa bộ trích và chạy lại bài đó.

`course_coverage.py --lesson 39` chỉ ra đúng file từ vựng, số từ và trạng thái từng phần. `--require all` kiểm 7 snapshot cho mỗi bài và hash của từng file. Trạng thái `captured` chứng minh đã lưu nội dung render ban đầu. Đáp án, media, biên tập và duyệt sư phạm được kiểm riêng. `grammar_index.py` chỉ xuất danh mục khi có đủ 50 bài, bỏ cách đọc ruby khỏi tiêu đề và giữ ID cùng thứ tự nguồn.

## Từ snapshot đến nội dung học

Trong lượt kiểm ngày 2026-11-25, chức năng reveal bài 39 từng trả đủ 32 ID ở phiên khảo sát trước. Lần chạy script tải đầy đủ ở phiên này gặp trang “Xác nhận truy cập”. Script dừng ở bước mở trang. Khi nguồn cho truy cập bình thường, chạy lại lệnh để lưu phần đáp án còn thiếu. Biên bản cũ có metadata và một câu mẫu; bộ kiểm chỉ đếm đáp án thực sự lưu cạnh snapshot hiện tại.

- **Ngữ pháp và B.** Dùng danh mục VNJPClub làm khung. Với từng mục, lưu ID, câu Nhật, dịch Việt, ví dụ, audio hoặc track + clip. Với B, script đáp án phía trên chỉ reveal các ID đã thấy, lưu cạnh snapshot dưới tên `<hash>.answers.json` và tiếp tục từ ID còn thiếu. Đọc `answer`, `reveal_html` (dịch/clip) và `explanation_html` theo ID. Kiểm riêng lời giải và quiz nhanh. Nếu lời giải nguồn trống, biên soạn lời giải Việt có nhãn AI. Đặt nhóm B sau mẫu cuối cùng cần dùng. Nhóm hình được viết lại thành tình huống chữ có đủ dữ kiện; câu chưa có nhóm B được bổ sung luyện thêm. Giữ ID câu/biến thể khi sửa.
- **Shadowing.** Chọn Văn mẫu và A. Gắn câu, bản dịch, track, khoảng đầu/cuối theo ID dòng. Mẫu bảng A cần giữ cả phần cố định và các vị trí thay thế.
- **Hội thoại.** Giữ các lượt nói, người nói, mẫu C và biến thể theo cụm. Khi biên tập, xếp video hướng dẫn → C → Kaiwa tổng hợp.
- **Nghe và đọc theo dạng JLPT.** Mỗi cụm có ID, đề dẫn chung, passage hoặc track/clip, transcript Nhật và dịch Việt nếu có. Mỗi câu giữ thứ tự, ID nguồn, lời hỏi, lựa chọn, đáp án nguồn, giải thích và tham chiếu về đúng passage/track. Đọc ngắn chỉ chọn section đọc và câu hỏi liên quan. Đọc dài lấy bài và tab câu hỏi. Loại ví dụ mẫu khỏi số câu chấm điểm. Mở “Script & dịch” hay “Đáp án” đúng item khi nội dung tải muộn. Đối chiếu đáp án bằng ID, phát thử clip; để trạng thái chờ nếu chưa xác minh được. Lưu dữ liệu học trung lập ở `normalized/lesson-NN/` và biến thể ở `authored/lesson-NN/`. Khi Harumii chốt bộ đọc cho nghe/đọc, kiểm bằng fixture rồi mới xuất payload theo hợp đồng app.
- **Kiểm tra.** Chọn theo số Mondai 1–6 trong tiêu đề, giữ loại bài, đề, đáp án và lời giải. Với bài thiếu một Mondai, ghi rõ số thiếu và bằng chứng từ trang.
- **Media.** Quan sát trong section và cấu hình media liên quan. Ghép track theo khóa, clip theo mốc và câu. Khi cần lưu file, kiểm loại nội dung, độ dài, hash và khả năng phát; nhiều clip có thể dùng chung một file. Bản ghi TTS cục bộ, track nguồn và media chưa xác minh có trạng thái riêng. Giữ nguyên liên kết của bản nguồn khi đổi câu và dùng media khớp lời mới.

## Rà từng bài trước khi duyệt

Mở đúng file từ vựng Harumii theo số sau chữ “Bài”. Tra cả 2 cấp trong `materials/grammar/` theo ý nghĩa và cấu trúc cho từng điểm nguồn. Đối chiếu từng nhóm B, đánh giá đề đã đủ dữ kiện, đáp án duy nhất và lời giải khớp câu mới. Lưu những quyết định cần truy lại trong `authored/lesson-NN/review.md`, gồm nguồn, ID đối chiếu Harumii, bài đã sửa, lý do và phần còn chờ. Nếu sửa bản đã đóng gói, tăng revision, build và verify lại. Ví dụ ở [bài 39](../authored/lesson-39/review.md).

Khi bàn giao, báo riêng số bài có snapshot, đáp án theo ID, media đã kiểm và bài đã duyệt. Với các node tùy chọn như nghe/đọc, trình bày rõ số cụm hoặc câu còn thiếu transcript, đáp án hoặc audio. Chốt toàn khóa sau khi từng bài 1–50 có biên bản theo phạm vi yêu cầu.
