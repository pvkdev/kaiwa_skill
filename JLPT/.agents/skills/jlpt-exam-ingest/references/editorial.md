# Lời giải sau khi nộp bài

## Khi HTML đã có lời giải

Đọc `.complete-answer` trong đúng `.q-item` của cùng kỳ và phần thi. Nếu ô trống, tra `#jlpt-singlefile-notes [data-key="answer-<id câu>"]` trong cùng file. Số câu có thể lặp ở phần viết và phần nghe. Chép nguyên lời giải vào `question.explanation`, giữ chữ Nhật, chữ Việt, số, dấu câu, thứ tự và ngắt đoạn có nghĩa. Bỏ nhãn giao diện của phụ lục. Giữ cả lời giải ngắn hoặc có cách trình bày khác các câu bên cạnh. Đánh dấu `origin=source`, ghi sourceId và locator. Nếu lời giải mâu thuẫn với đề hoặc khóa, giữ nguyên cả hai và mở issue có UUID để đối chiếu.

**Mốc đối chiếu khi kiểm preview.** N3 tháng 12/2025, phần viết, `#q-1` (西洋). Toàn bộ nội dung bên trong «Giải thích đáp án» của câu này là một đoạn:

> Từ đúng là 西洋 (せいよう) nghĩa là “phương Tây”. Các lựa chọn khác là đọc sai hoặc từ khác (vd. せいゆう = 声優).

So từng chữ với HTML. Nếu preview có thêm nhãn “Đáp án”, “Vì sao chọn”, “Vì sao loại” hoặc thêm diễn giải âm của từng kanji, kiểm revision/hash đang nhập và dữ liệu câu trong Harumi. Lời giải ngắn như nguồn đã là bản hoàn chỉnh.

## Khi HTML thiếu lời giải

Một dòng chỉ báo đáp án, trạng thái đang tải hoặc yêu cầu đăng nhập chưa đủ làm lời giải. Mở một lời giải **gốc** cùng dạng câu để tham khảo cách lập luận. Có thể dùng hai HTML của N3 tháng 12/2025 trong `N3/2512/`. Soạn bằng tiếng Việt với dữ kiện riêng của câu, dùng số đáp án theo thứ tự nguồn. Các ví dụ tra cứu:

- Phần viết `#q-1` (cách đọc) nêu từ, cách đọc và nghĩa trong câu. Chỉ đối chiếu một âm dễ nhầm nếu hữu ích.
- Phần viết `#q-37` (ngữ pháp) đặt mẫu trong cụm tiếng Nhật và giải nghĩa theo tình huống.
- Phần viết `#q-59` (đọc thông báo) chỉ ra điều kiện trong bài quyết định đáp án. Với bảng, dùng đúng dòng và cột liên quan.
- Phần nghe `#q-2` (việc cần làm trước) phân biệt việc được nhờ ngay với việc để sau bằng chi tiết trong hội thoại. Với câu dùng sơ đồ hoặc ảnh, kiểm cả nhãn trên ảnh và lời thoại.

Viết thành đoạn tự nhiên, thường có thể mở đầu bằng câu trả lời rồi nêu chi tiết quyết định. Chỉ phân tích lựa chọn gây nhầm khi việc đó giúp hiểu bài. Độ dài tùy câu. Ghi `origin=ai` và bằng chứng của đúng target. Nếu thiếu script, ảnh hoặc dữ kiện quyết định, giữ lời giải trống và báo đúng kỳ, phần, mondai, câu, UUID và hiện vật cần bổ sung. Ghi chú ngữ pháp có ích để riêng ở `grammarNotes`.

Phạm vi ngữ pháp tính từ thư mục cha của `JLPT/`. Với N3–N1, tra `bunpou_skill/source/<cấp>/_quan_ly.json` theo trường `mau` hoặc `ma`, mở đúng file ở trường `file`, đối chiếu cách dùng, ghi mã và đường dẫn thật. Với N5–N4, tra `kaiwa_skill/minna-n5-n4/catalog/grammar-points.json`, lưu cả số bài và `points[].id` vì ID một mình có thể lặp giữa các bài. Tra bài tương ứng nếu tiêu đề chưa đủ để phân biệt cách dùng. Ghi catalog theo phiên bản đang đọc. Nếu nguồn có mẫu nhưng tra chưa khớp, có thể giải thích ngay trong câu mà để trống liên kết. Một ghi chú biên tập không cấp ID bản ghi ngữ pháp ở DB Harumi.
