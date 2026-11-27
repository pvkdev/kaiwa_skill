# Từ SingleFile đến một kho JLPT nhập được vào Harumi

Trạng thái sau triển khai pilot ngày 27/11/2026 nằm trong [nhật ký kiểm thử](reports/PILOT_2026-11-27.md). Để nạp dữ liệu ngay, làm theo [hướng dẫn migration](MIGRATION.md).

Thư mục làm việc là `JLPT/` trong repo `kaiwa_skill`. Người sưu tầm lưu một HTML kết quả cho phần viết, một HTML cho phần nghe và một bản audio tổng khi có. AI chịu trách nhiệm từ lúc nhận nguồn đến lúc giao gói dữ liệu đã rà. Mục tiêu ở bản fork là chọn kho một lần, nhập toàn bộ các đề đã sẵn sàng và mở một đề để làm, chấm, nghe lại, xem lời giải. Các kỳ có thể đổi cấu trúc, số phương án, cách đánh số và số câu cho mỗi đoạn.

## Trình tự giao hàng

1. **Nhận nguồn và trả phiếu thiếu.** Giữ cách đặt file hiện tại `N1/` đến `N5/`; tên thư mục là gợi ý tìm file. Đọc kỳ và phần thi trên bản lưu. Mỗi lần bổ sung HTML hoặc transcript, chạy audit và đối chiếu checklist cũ. Giao người sưu tầm danh sách có thể hành động theo kỳ/mondai/câu, gồm script Nhật hoặc MP3 còn thiếu. Thiếu giải thích nguồn tạo việc cho AI. Thiếu dịch mà nguyên văn còn đầy đủ cũng do AI xử lý.
2. **Biên soạn trọn một kỳ N2 tháng 12/2018.** Đây là pilot có đủ hai HTML, một MP3 và ví dụ hai câu nghe chung. Tách bài đọc, câu hỏi và ảnh vào đúng block; lập ID theo hợp đồng, giữ thứ tự hiển thị và đáp án. Biên tập từng lời giải bằng tiếng Việt, đối chiếu với nguồn Nhật. Kết quả là `packages/N2/2018-12/package.json`, file gốc theo checksum, các ảnh/MP3 phục vụ app dưới `assets/sha256/` và danh sách thiếu nếu phát hiện thêm. Đối chiếu **73 câu viết + 30 câu nghe**, cùng mốc và script của cặp 29–30. Duyệt chất lượng biên tập trước khi đưa vào catalog.
3. **Đưa pilot qua fork local.** Dùng [kế hoạch Harumi](HARUMI_IMPORT_PLAN.md) để triển khai từng slice. (a) Đọc catalog, kiểm và preview. (b) Nhập gói dưới một transaction cho mỗi đề, mapping và media dùng lại theo hash. (c) Mở lại trong pool, phát master theo khoảng, chấm và xem giải thích từ dữ liệu thật. Kiểm nhập lại và phục hồi sau lỗi trước khi nhân rộng. Asset local có thể phục vụ từ dev ngay. Khi dùng R2 cho ảnh hoặc RSS cho audio, ánh xạ lúc import để hồ sơ biên tập vẫn di chuyển được giữa máy.
4. **Mở rộng theo kỳ.** Root giao một kỳ/sub, giao QA độc lập các đoạn chung hoặc câu có mâu thuẫn. Làm tiếp hai kỳ N3 để kiểm ảnh và bảng thông tin; N2 tháng 7 để kiểm luồng bổ sung script; N1 tháng 12 để kiểm luồng tự soạn toàn bộ giải thích. Bổ sung N4 và N5 khi nhận file, chạy một kỳ mỗi cấp trước khi áp dụng hàng loạt. Đo cấu trúc từ từng đề, không suy ra số câu từ mẫu 2018.
5. **Phát hành kho local.** Root kiểm toàn bộ gói đã duyệt, chạy `py -3 tools/build_catalog.py` từ `JLPT/`. Lệnh dựng `catalog.json` gồm đường dẫn gói, revision và checksum. Gói nào đang chờ nguồn được liệt kê khi bỏ qua; catalog được thay nguyên tử sau khi validator kiểm thành công. Trong fork, một lần nhập xử lý toàn danh mục. Revision mới của một kỳ phải giữ liên kết ổn định với đề, mondai và câu để không làm hỏng lượt luyện đã lưu.

## Lưu gì ở đâu

- `N*/…` và file bổ sung của người dùng là chứng cứ gốc. Đặt script bổ sung cạnh bộ đề, có tên thể hiện phần nghe, mondai và câu, ví dụ `N2/1807/supplements/choukai-m01-q01-q03.md`. Trong file ghi rõ đoạn nào thuộc câu nào, người nói nếu biết và nguồn của script. Bổ sung này được worker đăng ký vào `sources` trong gói; báo cáo kiểm HTML vẫn phản ánh đúng những gì bản HTML tự chứa.
- `work/evidence/<sha256>/` là bản đọc cho tác nhân, tạo lại từ nguồn được. `reports/source-gaps.json` là kiểm kê tự động theo HTML. Vấn đề đã được người dùng bổ sung hoặc còn chờ xác minh được ghi tại `review.issues` của từng package và đối chiếu trước khi gửi lại phiếu thiếu.
- `packages/<level>/<YYYY-MM>/package.json`, `assets/sha256/` và `catalog.json` là dữ liệu để đóng gói. Nếu một kỳ có nhiều bộ độc lập, dùng thêm định danh biến thể trong tên thư mục cùng cấp và trong slug. Giữ định danh khi người dùng thay file chụp tốt hơn. Cấu trúc gói, quy tắc phiên bản, mapping và lệnh kiểm nằm trong [hợp đồng](contracts/v1/CONTRACT.md).
- [Skill biên soạn](.agents/skills/jlpt-exam-ingest/SKILL.md) chứa hướng dẫn tác nhân, mẫu lời giải đã đối chiếu với đề thật, cách gắn ngữ pháp, script, đoạn nghe và cách giao sub. Mở Codex tại thư mục `JLPT/` để dùng skill theo repo. Ví dụ: “Dùng $jlpt-exam-ingest xử lý bộ N2 tháng 12/2018 đến gói có thể nhập ở local.”

## Mốc nghiệm thu

**Dữ liệu.** So số câu, khóa đáp án, bài đọc dùng chung, thứ tự, chữ gạch chân, ảnh và script với HTML. Kiểm nghĩa tiếng Việt và bằng chứng giải thích theo từng câu. Không để furigana tự động lộ đáp án bài đọc chữ. Mọi mốc đều tham chiếu đúng một bản audio đã định danh. Câu có nguồn chưa đủ vẫn nằm trong kho biên soạn.

**Fork.** Nạp catalog lần đầu, mở ở pool rồi làm một bài N2 trên màn học. Phát lại chính xác đoạn chung câu 29–30, chấm đáp án và mở bài giải. Nhập lần hai giữ nguyên số đề/câu và ID. Thay một lời giải, tăng revision rồi nhập lại chỉ cập nhật đúng kỳ. Sửa tay cùng câu trong app, thử import lại để thấy báo xung đột. Làm hỏng một checksum trong fixture và ngắt sau khi upload trước commit để kiểm khả năng retry.

**Tiến độ khi lập kế hoạch.** Đã xây skill, công cụ đọc SingleFile, báo cáo kiểm nguồn và hợp đồng kiểm bằng máy. Đã kiểm trên các ảnh chụp hiện có và fixture tổng hợp. Gói biên tập đầy đủ của pilot, chỉnh mã bản fork và bài test import vào DB là ba đầu việc triển khai tiếp theo.
