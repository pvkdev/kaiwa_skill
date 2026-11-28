# Đưa kho đề vào bản fork Harumi

Tài liệu này lưu phương án ban đầu cho bản fork. Quyết định mới là sửa trực tiếp source Harumi, với trang riêng `/admin/jlpt-exams/import` và thư mục dữ liệu nằm trong repo kỹ năng. Để triển khai hoặc tiếp quản, dùng [kế hoạch hiện hành](ADMIN_JLPT_EXAMS.md), [hướng dẫn migration](MIGRATION.md) và [nhật ký pilot](reports/PILOT_2026-11-27.md).

Mục tiêu là chọn một catalog trên máy, bấm **Nhập kho JLPT** một lần, rồi mở đúng đề trong JLPT Pool và luyện được ở màn hình người học. Mỗi kỳ giữ một audio tổng. Nội dung, thứ tự và quan hệ dùng chung của `JlptMondai` theo đúng kỳ thi. Đây là kế hoạch phát triển cho bản fork local. Mã đã đối chiếu ở Harumi là commit `031fd10e`.

## Điểm nối hiện có

- `backend/src/Harumi.Exam/Features/ExamSetAuthoring/JlptExamSetSlices.cs` nhận `level/slug/name/contentJson`. `Extensions/EndpointExtensions.cs` đặt các route này dưới `/api/exam/admin` với quyền Admin. Khóa duy nhất hiện tại là cặp level và slug.
- `Services/JlptExamCompositionService.cs` tách bốn tab thành pool `JlptMondai` và bảng nối `JlptExamSetMondai` với `Paper/SortOrder`. Payload mỗi mondai giữ `instruction/instructionHtml/blocks`. Khi đọc, service dựng lại bốn tab. Gắn timeline vào root của JSON gửi theo đường lưu hiện tại sẽ làm mất timeline khi đọc lại. GET chi tiết có thể tự chuyển dữ liệu legacy khi đề chưa có links, vì vậy preview chỉ đọc cần một truy vấn riêng.
- `frontend/src/lib/exam/jlptExamModel.ts` có block chứa nhiều câu, passage, ảnh, audio, script JA/VI cấp block hoặc câu. Câu có `correctChoiceId`, `explanation`, `translationVi` và `grammarNotes`. Có thể giữ cơ chế chấm theo ID lựa chọn dù đề gốc hiển thị số.
- `JlptAudioEditor.tsx` đã có tìm audio qua RSS. `Harumi.Shared/Features/Rss/RssPodcastAudioResolver.cs` chọn item đầu tiên trùng title và trả URL enclosure. `AudioPlayer.tsx` hiện phát cả file, thanh seek dùng toàn thời lượng. `ExamPracticePage.tsx` dựng danh sách luyện từ `jlptPracticeMock.ts`. Những điểm này cần chỉnh để dùng dữ liệu đã import trong màn học.

## 1. Đọc catalog và dựng preview

Gắn thao tác vào màn JLPT Pool ở bản fork. Người dùng chọn thư mục chứa release. Trình duyệt chuyển danh mục file theo đường dẫn tương đối cho trình nhập. Đọc [schema catalog](contracts/v1/catalog.schema.json) và [schema từng đề](contracts/v1/exam-package.schema.json). Kiểm phiên bản, UUID ổn định, SHA-256 byte gốc, phạm vi đường dẫn, các ID tham chiếu và khóa trùng trước khi ghi. Chỉ đưa package thuộc catalog vào batch. Chỉ chuyển JSON đề và tài sản phục vụ app, HTML nguồn và khóa API vẫn ở máy biên soạn.

Preview hiển thị số đề sẽ tạo, cập nhật, bỏ qua, xung đột, số mondai/câu và media cần xử lý. Bấm nhập chạy lại cùng phép kiểm và xử lý toàn danh mục hợp lệ. Nêu rõ đề bị chặn và vị trí câu ở kết quả. Áp dụng chính sách draft/ready của contract, đặc biệt với script, bài giải và câu thiếu đáp án. Chỉ đưa đề được chọn cho người học vào danh sách luyện đã sẵn sàng.

## 2. Import một đề như một đơn vị

Thêm vertical slice hành động trong `Harumi.Exam` dưới quyền Admin. Cả batch gọi cùng handler cho từng đề. Đề xuất lưu metadata import riêng gắn với `JlptExamSet.Id` gồm định danh package, revision, checksum nguồn, fingerprint dữ liệu app ở lần import cuối và siêu dữ liệu cần cho màn học. Lưu `masterAudio`, quan hệ thời gian và thứ tự lịch sử theo hợp đồng vào metadata cấp đề, đọc qua DTO chi tiết riêng. Gói đầy đủ cùng nguồn gốc bài giải, tham chiếu ngữ pháp và báo cáo thiếu nằm trong kho dữ liệu. Giữ nguyên model pool và quan hệ tham chiếu hiện hành.

1. Nhận dạng bằng `packageId` qua mapping ổn định. Giữ ID mondai, block, media, câu và choice qua các bản sửa. Trùng slug với đề nhập tay, trùng UUID với pool khác nguồn, revision thấp hơn, hay cùng revision nhưng checksum khác đều trả kết quả xung đột. Cùng revision/hash chỉ bỏ qua sau khi kiểm fingerprint target.
2. So sánh fingerprint nội dung hiện tại với lần import cuối, gồm cấu trúc, thứ tự, đáp án, nội dung và timeline. Nếu admin đã sửa trong app, đưa diff theo đề/mondai và để nguyên bản đang dùng. Mondai có liên kết sang đề khác cần báo tất cả đề bị ảnh hưởng trước khi đổi nội dung. Hai gói trùng số mondai nhưng khác kỳ vẫn có ID riêng.
3. Dùng composition và section resolver hiện có cho phần chung. Truyền tường minh `section`, số mondai và thứ tự trong tab theo gói để xử lý kỳ thi đổi cấu trúc. Trước khi gọi service phải xác thực ID, quyền sở hữu và toàn bộ payload. Đường split hiện thay links và có thể cập nhật trực tiếp mondai dùng chung theo GUID. So sánh loại bỏ/thay thế các ID đã có dữ liệu học, yêu cầu xử lý rõ với thay đổi phá vỡ tham chiếu.
4. Dùng transaction Postgres cho upsert đề, mondai, thứ tự links và metadata. Khóa theo package và kiểm lại revision sau khi lấy khóa, kể cả tình huống hai request tạo mới. Tôn trọng unique index `(ExamSetId, Paper, SortOrder)` khi đổi thứ tự. Một đề lỗi rollback riêng. Các đề thành công có biên nhận trong DB để lần chạy sau tiếp tục, kể cả khi trình duyệt mất kết nối ngay sau commit. Không dùng một EF migration chứa toàn bộ câu hỏi.
5. Đọc lại đề đã assemble và metadata theo ID. So với gói sau ánh xạ bằng số lượng, thứ tự, đáp án, nội dung, quan hệ ảnh/passage, audio và mốc thời gian. Báo riêng trạng thái đã commit nhưng đọc lại không khớp để lần chạy kế tiếp đối soát an toàn.

## 3. Media và phát từng đoạn

Ảnh dùng bytes local theo hash, importer ánh xạ sang đường dẫn dev hoặc khóa R2. Dùng cơ chế presigned PUT của Shared khi chạy với R2. Do `RequestMediaUploadUrlSlice` hiện sinh khóa ngẫu nhiên và `ConfirmMediaUploadedSlice` đang ghi bảng thử nghiệm, cần lưu mapping hash–objectKey bền vững và xác minh object trước khi liên kết. Upload trước transaction DB, tái sử dụng phần upload đã xác minh khi retry. Trình nhập local chỉ liên hệ đích media đã cấu hình cho môi trường.

Với audio, giữ một bản master và trục millisecond từ đầu bản đó. Nếu chạy local hoàn toàn, phục vụ MP3 từ đường dẫn dev cho trình duyệt seek được. Khi chủ kho đã đưa đúng bản thu lên Spotify và có RSS, dùng GUID của episode trong feed để tra enclosure có thể phát trực tiếp. Tiêu đề giúp tìm ứng viên khi đăng ký episode. Nếu có nhiều ứng viên, yêu cầu chủ kho chọn binding một lần. URL trang Spotify chỉ giúp người dùng mở trang episode. Lưu định danh episode riêng với URL phát để cập nhật enclosure khi URL đổi. Kiểm thời lượng thực, khả năng seek trên trình duyệt và so vài mốc đầu/giữa/cuối với master. Một bản thu có intro/quảng cáo hoặc bị cắt khác cần đánh dấu xác minh lại timeline.

Một trình phát cho đề, đổi khoảng phát theo lựa chọn. Đổi ms sang giây tại biên HTMLMediaElement. Khi metadata sẵn sàng thì seek đến đầu đoạn. Trong luyện riêng, giới hạn seek, phát lại và tự dừng ở cuối khoảng. Khi làm toàn phần nghe thì phát master liên tục. Ưu tiên đoạn riêng của câu, sau đó đoạn dùng chung được gắn với câu, kế tiếp là đoạn mondai đã xác minh. Nếu chỉ có master, hiển thị nút nghe toàn đề. Một đoạn có hai câu dùng cùng ID tham chiếu/quan hệ theo contract. Chuyển câu đang phát phải gỡ callback cũ. Đặt riêng phần kiểm khoảng và phạm vi điều khiển để các màn dùng AudioPlayer cũ tiếp tục phát cả file.

## 4. Đưa vào luồng ôn thực tế

Nối màn đề theo kỳ và luyện theo mondai của bản fork với truy vấn thật từ Exam, giữ thứ tự ổn định và ID khi làm bài. Trả prompt, options, passage, ảnh và đoạn phát trong lượt làm bài. Dùng đề đã nộp để trả đáp án đúng, bản dịch, script và bài giải Markdown. Mẫu ngữ pháp đã đối chiếu hiện qua `grammarNotes`; hiển thị được ghi chú ngay cả khi app chưa có liên kết đến bản ghi ngữ pháp. Mọi truy vấn khác domain sau này dùng interface/event theo thiết kế. Giữ biên tập cục bộ và tiếp tục hỗ trợ dữ liệu cũ có audio riêng. Bổ sung vào editor trường audio/timeline cấp đề qua DTO, hoặc dùng cập nhật metadata riêng để lưu một thay đổi văn bản không làm rỗng mốc đã nhập.

## Checkpoint trên bản fork

1. **Swagger/Postman ở dev** — nạp fixture theo catalog vào DB mới, rồi đọc lại qua `GET /api/exam/admin/jlpt-exam-sets/by-slug/{level}/{slug}` và DTO chứa timeline. Kiểm lại khi import lần hai, sửa một câu rồi tăng revision, trùng slug, sửa tay trong app, lỗi ghi giữa một đề, ngắt kết nối sau commit và hai lượt import đồng thời. Số đề/mondai/links phải khớp trước và sau retry.
2. **Trình duyệt admin** — lấy N2 tháng 12/2018 làm pilot với MP3 tổng. Kiểm số câu/đáp án, mở hai câu dùng cùng đoạn, sửa một lời giải rồi lưu, đóng và mở lại để thấy audio và timeline còn đủ. Với N3 tháng 12 kiểm sáu ảnh phần nghe và bảng lịch ở hai câu đọc cuối. Đổi thứ tự hai mondai trên fixture để kiểm link và số gốc.
3. **Trình duyệt người học** — vào danh sách đề thật, chọn kỳ và làm một mondai tới kết quả. Kiểm seek/replay/auto-stop ở đầu, giữa, cuối file và hai câu chung đoạn. Với N1 chỉ có đáp án, xem trạng thái thiếu từ admin, làm thử phần đủ dữ liệu theo chính sách release. Kiểm cả đề legacy và một fixture N5/N4 trước khi công bố hỗ trợ cả năm cấp. QA bản phát RSS trên đúng enclosure sau khi chủ kho cung cấp feed.

Ưu tiên triển khai trên fork theo thứ tự preview và import một đề → import cả catalog và retry → phát theo mốc ở editor → màn người học đọc đề thật. Pilot kết thúc khi một lần nhập cho phép làm, nộp và đọc lại đúng một bài thật ngay trong app.
