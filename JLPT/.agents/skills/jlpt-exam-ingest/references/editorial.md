# Lời giải người học đọc sau khi làm bài

Viết bằng tiếng Việt. Cho người học thấy lựa chọn nào đúng, dấu hiệu nào trong tiếng Nhật quyết định đáp án và họ có thể tự nhận ra dấu hiệu ấy ở đâu. Giữ nguyên thứ tự đáp án và câu hỏi. Chép văn bản Nhật từ đề hoặc script; tách phần dịch khỏi phần giải thích. Lời giải VNJPClub được giữ trong bằng chứng, tác nhân kiểm và viết lại sau khi tự giải câu. Nếu có căn cứ cho thấy khóa nguồn sai, ghi khóa nguồn, đáp án đề nghị, vị trí bằng chứng rồi chuyển QA; không tự sửa khóa.

## Format biên tập

- **Đáp án.** Ghi số theo đề và nội dung chọn. Với các đáp án chỉ có số, thêm lời đáp khi có nguồn xác định chính xác lời tương ứng.
- **Vì sao chọn.** Trích vừa đủ một từ, vế câu, ô bảng hoặc lượt thoại có giá trị phân biệt. Giải nghĩa tiếng Việt rồi nối dữ kiện với đúng yêu cầu đề. Với câu đọc thái độ tác giả, phân biệt lời người được trích và kết luận của tác giả. Với câu nghe hỏi việc làm *đầu tiên*, nêu ai làm, trình tự và điều kiện thay đổi quyết định.
- **Vì sao loại.** Nêu điểm sai của từng phương án khi có sự khác biệt đáng học. Có thể gộp phương án trùng, chỉ rõ các số đã gộp. Với câu sắp xếp, cho chuỗi hoàn chỉnh và vị trí ★. Với câu từ vựng, chỉ rõ âm, chữ, kết hợp từ hoặc sắc thái gây nhầm. Với đề nghe chỉ hiện số, thiếu lời các phương án thì chỉ loại với bằng chứng thực sự có.
- **Ngữ pháp liên quan** là phần tùy câu. Chọn mẫu có vai trò trong cách hiểu hoặc cách loại phương án, dẫn đúng cụm trong đề và giải nghĩa ở chính ngữ cảnh đó. Lưu ghi chú ngữ pháp riêng theo mapping hợp đồng; UI có thể hiển thị ngay sau phần giải. Không nhồi danh mục cùng cấp vào mọi câu.

Phạm vi ngữ pháp tính từ thư mục cha của `JLPT/`. Với N3–N1, tra `bunpou_skill/source/<cấp>/_quan_ly.json` theo trường `mau` hoặc `ma`, mở đúng file ở trường `file`, đối chiếu cách dùng, ghi mã và đường dẫn thật. Với N5–N4, tra `kaiwa_skill/minna-n5-n4/catalog/grammar-points.json`, lưu cả số bài và `points[].id` vì ID một mình có thể lặp giữa các bài. Tra bài tương ứng nếu tiêu đề chưa đủ để phân biệt cách dùng. Ghi catalog theo phiên bản đang đọc. Nếu nguồn có mẫu nhưng tra chưa khớp, có thể giải thích ngay trong câu mà để trống liên kết. Một ghi chú biên tập không cấp ID bản ghi ngữ pháp ở DB Harumi.

## Ví dụ đã đối chiếu với bản N3 tháng 12/2018

Nguồn phần viết `8ee1351a9921d5c15d29aff63562ec3ff31f3491e11c03eaaef7e628468b5ffc`, vị trí `#q-1`. Câu hỏi kiểm tra cách đọc phần gạch chân trong 息子は来年【卒業】します。 Bản lưu có furigana và có hai lựa chọn trùng nhau. Nội dung người học có thể đọc sau khi trả lời:

> **Đáp án 2 · そつぎょう.** 「卒業します」 nghĩa là “tốt nghiệp”. Trong từ này, 卒 đọc là そつ và 業 đọc là ぎょう. Cả câu nghĩa là “Con trai tôi sẽ tốt nghiệp vào năm sau”.
>
> **Vì sao loại.** Phương án 1 và 4 đều ghi さつぎょう, sai âm đầu của 卒. Phương án 3 ghi そつきょう, đọc 業 thành きょう thay vì ぎょう.

Không cần gắn mẫu ngữ pháp cho ví dụ này. Giữ nguyên hai lựa chọn trùng như nguồn và ghi vào ghi chú biên tập. Bản dịch trong lời giải không được hiện bên cạnh câu hỏi trước khi chấm nếu nó tiết lộ đáp án.

## Khi thiếu

Thiếu lời giải nguồn nhưng đủ đề, lựa chọn, đáp án và căn cứ → AI tự soạn, ghi provenance là phần AI biên tập. Thiếu script làm thay đổi khả năng chứng minh câu nghe → giữ đề, khóa và lời giải nguồn nếu có; ghi chính xác kỳ, mondai, câu (cả số hiển thị và ID trong HTML), file, đoạn nếu biết, và yêu cầu “cần nguyên văn Nhật của đoạn này”. Script do người dùng bổ sung vẫn cần đối chiếu người nói và câu hỏi. Khi một đoạn phục vụ nhiều câu, gửi một yêu cầu cho cả nhóm. Thiếu bản dịch Việt nhưng có đủ nguyên văn Nhật → AI có thể dịch, đánh dấu nguồn bản dịch. Không dùng khóa trắc nghiệm để suy ngược lời thoại.
