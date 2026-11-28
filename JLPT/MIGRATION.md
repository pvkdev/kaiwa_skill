# Nhập kho đề JLPT vào Harumii dev

## Biên soạn và thử một kỳ với hợp đồng 1.3

Tại gốc kho `JLPT`, quy trình cho N3 tháng 12/2025 như sau. Bộ nguồn hiện hành gồm các thư mục cấp/kỳ, còn thư mục `packages` chỉ chứa những kỳ đã biên soạn. [Skill điều phối](.agents/skills/jlpt-exam-ingest/SKILL.md) và [checklist từng kỳ](reports/EXAM_CHECKLIST.md).

```powershell
py -3 -X utf8 .agents/skills/jlpt-exam-ingest/scripts/audit_sources.py --root . --out reports/source-gaps.json
py -3 -X utf8 tools/convert_singlefile.py --level N3 --period 2025-12 --inspect-layout
py -3 -X utf8 tools/convert_singlefile.py --level N3 --period 2025-12 --revision 1
py -3 -X utf8 tools/verify_capture.py packages/N3/2025-12/package.json
py -3 -X utf8 contracts/v1/validate_package.py packages/N3/2025-12/package.json --root .
py -3 -X utf8 tools/corpus_checklist.py
# Chạy skill jlpt-exam-review trên package cuối, ghi checkpoint rồi mới build.
py -3 -X utf8 tools/build_pilot_bundle.py --package packages/N3/2025-12/package.json
```

1. Với layout mới, đối chiếu số, lời dẫn, block đầu tiên của từng phần rồi lưu mapping của đúng SHA nguồn vào `written-layout.json` cạnh HTML hoặc truyền `--layout`. Với gói đã biên tập, dùng `--output-root` trỏ sang staging, so thay đổi và tăng revision đã nhập trước khi thay gói canonical.
2. Dán RSS ở ô **B4** của [sổ audio](JLPT_AUDIO.xlsx), lưu, đóng Excel rồi chạy `.\tools\sync_exam_audio.ps1`. Kiểm tra kết quả từng dòng. Công cụ đặt enclosure vào gói; sau đó chạy lại checklist, validate, review và build để có thư mục upload theo hash mới. Nếu đang chờ feed, có thể dùng MP3 local để preview. Khi nhận nguồn bổ sung cho nghe, dùng [skill nghe](.agents/skills/jlpt-listening/SKILL.md).
3. Sau mỗi lần tạo/sửa gói, chạy [skill rà gói](.agents/skills/jlpt-exam-review/SKILL.md) trước khi build: đối chiếu từng UUID với nguồn, ghi checkpoint đúng revision/SHA-256 bytes và mọi vấn đề còn mở. Bản draft có khóa chấm được xem trước trên dev; chưa rà hết thì không duyệt. Chọn **thư mục mới mà lệnh build in ra** ở [trang import](http://localhost:3000/admin/jlpt-exams/import). Bỏ `--package` để đóng cả kho. Đăng nhập admin, xem preview, chọn các đề, nhập rồi mở trang xem. Phần biên tập còn thiếu hiện trong checklist trang sửa. Khi duyệt phát hành dùng validator với `--release` trên cùng revision/hash và `tools/build_catalog.py`.
4. Để kiểm sau migration, đối chiếu số câu, ảnh, khóa và nhóm dùng chung với nguồn. Mở phần nghe, thử mốc đầu/giữa/cuối trên cùng file, kiểm một câu có cue riêng và một nhóm dùng chung nếu kỳ có. Nộp bài, thử JA để tra từ, VI cho bản dịch đầy đủ và chạm câu trong JAVI. Với mobile, thử nút tiến/lùi bên phải footer, nút nộp ở header, quay lại sau reload ở chế độ bấm giờ.

Các bước còn lại bên dưới mô tả API và năm gói 1.1/1.2 đã dùng trong pilot năm 2018.

## Nhập ngay

1. Đăng nhập tài khoản quản trị và mở [Nhập thư mục đề](http://localhost:3000/admin/jlpt-exams/import).
2. Chọn cả thư mục `D:\CODE\git\kaiwa_skill\JLPT\pilot-upload\edb3be1a64cd54c8`. Bên trong có `catalog.json`, `packages/` và `assets/`. Đây là 5 gói revision 2 của N1, N2, N3 với 517 câu. Để thử riêng N2 tháng 12/2018 kèm MP3, chọn `pilot-upload/d27c45cb520a25cb`.
3. Đợi kiểm tra hash và xem trạng thái từng đề. Giữ các đề cần nhập được đánh dấu, bấm **Nhập**. Khi tất cả đề đã chọn thành công, trình duyệt mở đề đầu tiên. Nếu có lỗi giữa chừng, các đề đã thành công có liên kết mở riêng. Sửa lỗi và kiểm tra lại các đề còn lại.
4. [Thư viện đề](http://localhost:3000/admin/jlpt-exams) liệt kê các đề đã nhập. Mỗi đề có trang làm bài và trang chỉnh sửa. Bản mới ở trạng thái nháp. Có thể nộp khi còn câu trống qua hộp xác nhận để xem kết quả, nhấn hiện bản dịch, mở giải thích và tra từ. Điểm tổng hợp là số câu đúng, sai và bỏ trống. Lượt xem thử lưu trong tab trình duyệt.
5. Với đề nghe, ở trang sửa dán URL tệp audio tổng hoặc URL enclosure của tập podcast. URL phải phát được trực tiếp trong trình phát audio của trình duyệt. Đổi nơi lưu cùng bản ghi vẫn dùng thời lượng đã xác minh của master. Khi thay bản thu khác, cập nhật master, thời lượng và timeline trong repo rồi nhập revision mới. Mốc trong dữ liệu dùng mili giây tính từ đầu tệp. Chọn phần nghe, mondai và câu. Nhập trực tiếp hoặc lấy vị trí đang phát. Khi nghe lại câu, ưu tiên mốc câu, tiếp theo là đoạn dùng chung, rồi mốc mondai. Nút phát từ đầu dùng toàn bộ master.
6. Trong trang chỉnh sửa đề, lưu thay đổi rồi mở **Furigana** cạnh nút lưu. Chọn **Tạo lại furigana cho đề này** hoặc **Tạo lại furigana cho toàn bộ đề**. Phạm vi toàn bộ bao gồm cả các cấp độ đang ẩn bởi bộ lọc. Giữ tab mở trong lúc chạy. Từng đề được tính lại bằng Kuroshiro và Sudachi rồi lưu trong một lần có kiểm tra phiên bản. Nếu một đề lỗi, bản đã lưu của đề đó còn nguyên và màn hình cho biết đề cần chạy lại.

## Chuẩn bị từ SingleFile

Chạy PowerShell tại `D:\CODE\git\kaiwa_skill\JLPT`. Cần Python 3.11+, jsonschema 4.x và ffprobe khi đo tệp nghe. [Skill biên soạn](.agents/skills/jlpt-exam-ingest/SKILL.md) quy định đối chiếu khóa đáp án, biên tập nguồn thiếu và ghi checkpoint.

```powershell
py -3 .agents/skills/jlpt-exam-ingest/scripts/audit_sources.py --root . --out reports/source-gaps.json
py -3 tools/convert_singlefile.py --level N2 --period 2018-12 --output-root "$env:TEMP/jlpt-n2-staging"
py -3 contracts/v1/validate_package.py packages/N2/2018-12/package.json --root .
py -3 tools/build_pilot_bundle.py
py -3 tools/build_pilot_bundle.py --package packages/N2/2018-12/package.json
```

Dùng `--output-root <thư-mục-staging>` cho converter khi đối chiếu thay đổi trên gói đã biên tập. Giữ UUID cũ khi có thay đổi số thứ tự. Bổ sung nguồn, lời giải, bản dịch trong kho này, chứng minh nội dung thay đổi và tăng revision trước khi đóng gói. Chạy [review](.agents/skills/jlpt-exam-review/SKILL.md) trên bản cuối sau mỗi lần chỉnh/gộp. Bản sửa trực tiếp trên app chỉ ở DB dev. Đồng bộ chỉnh sửa có giá trị về kho trước lần nhập sau. Gói phát hành đã duyệt dùng `tools/build_catalog.py`. Pilot chấp nhận bản nháp có đáp án đã xác minh.

## Hợp đồng trao đổi và lưu trữ

- [Hợp đồng dữ liệu](contracts/v1/CONTRACT.md), [schema gói](contracts/v1/exam-package.schema.json) và [schema catalog](contracts/v1/catalog.schema.json) là định nghĩa cho repo dữ liệu. Importer đọc được 1.1.0, 1.2.0 và 1.3.0. [Thiết kế và nhật ký kiểm thử](ADMIN_JLPT_EXAMS.md).
- Catalog liệt kê `packageId, revision, path, sha256`. Mã SHA-256 tính trên byte thực. Mỗi gói chứa `exam, structure, sources, assets, content, annotations, review, masterAudio`. Gói chỉ mang JSON và media được tham chiếu. HTML, report, checkpoint và thông tin xác thực nằm ở kho local.
- Thứ tự lịch sử nằm ở `content.{mojigoi,bunpou,dokkai,choukai}.mondais[].blocks[]`. Các bảng/ảnh thuộc bài, khóa `correctChoiceId`, số câu nguồn và các UUID được bảo toàn. `annotations.sentencePairs[id]` là dãy `{ja,vi}`. Khóa là ID media cho bài đọc/script chung, ID câu hỏi cho script riêng. Bản dịch toàn bài ghép các hàng có tiếng Việt theo thứ tự, dùng dấu xuống dòng. Gói 1.3 tách lượt nói có nhiều câu thành các cặp riêng trước khi duyệt. `vi:null` biểu thị thiếu dịch. Với gói 1.1 chưa có đối chiếu, dùng bản dịch cả đoạn hiện có.
- `annotations.audioSegments[]` ghi `mondaiId, questionIds, role, startMs, endMs`; điểm cuối loại trừ, null biểu thị mở đến cuối. Nhiều câu có thể trỏ tới cùng cuộc thoại. Audio và ảnh đóng gói theo SHA trong `assets/sha256`. Upload dev phục vụ media cùng origin, có HTTP Range. Muốn di chuyển môi trường cần mang theo DB và thư mục media (`%LOCALAPPDATA%\Harumi\jlpt-pilot-media` hoặc `JLPT_PILOT_MEDIA_DIR`), hoặc đóng gói và nhập lại. Khi tích hợp R2 sau này, dùng asset SHA làm khóa ánh xạ để thay URL ở importer.
- DB giữ `JlptExamSet`, `JlptMondai` và bảng liên kết hiện có. Metadata import đặt trong `JlptExamSet.ContentJson.importMetadata` gồm biên nhận, ghi chú review, URL master, timeline, số câu nguồn và cặp câu. Một package tương ứng một transaction. Không cần EF migration riêng cho tính năng.

## Kiểm tra API và xử lý xung đột

- Dev frontend mặc định mở ở localhost:3000, API ở localhost:5000. Từ repo Harumi, `docker compose up -d --build --no-deps api` cập nhật API khi các dependency đã chạy. Các API kho đề yêu cầu Development và quyền Admin. Swagger/Postman dùng bearer của phiên admin dev.
- `POST /api/exam/admin/jlpt-package-import` nhận `packageJson` là **nguyên chuỗi UTF-8 của tệp**, `sha256`, `assetUrls` (digest → URL media dev), `preview` và tùy chọn `overwrite, expectedVersion`. Gửi `preview:true` trước, upload media qua `PUT /api/jlpt-pilot-media/<digest>.<ext>`, sau đó gửi `preview:false`. Trả `status=created|updated|unchanged` cùng ID, level, slug, revision, version. Khi ghi đè dùng version của **lần preview với overwrite**.
- Cùng package và revision đã nhập sạch trả `unchanged`. Bản nguồn mới hơn cập nhật theo UUID. Bản có thay đổi tay trên DB hoặc cùng revision nhưng khác bytes yêu cầu chủ động bật **Cho phép ghi đè**. Preview sẽ chạy lại. Importer từ chối bản cũ hơn, xung đột slug/UUID, mondai dùng bởi đề khác hoặc bản loại bỏ ID câu/mondai đang tham chiếu. Nếu nhận 409 do có người sửa sau preview, kiểm tra lại trước khi ghi. Tạo lại riêng furigana trên đề sạch vẫn cho phép retry import bình thường.
- `GET /api/exam/admin/jlpt-exams` trả danh sách gói đã nhập. `GET /api/exam/admin/jlpt-exams/{id}` trả `id, name, level, slug, revision, version, content, importMetadata`. `PUT` cùng URL nhận `{expectedVersion,content,name?,masterAudioUrl?,audioSegments?,sentencePairs?}`. Body chứa đầy đủ content với cấu trúc và UUID của bản GET. Sửa sai âm/sai vị trí hoặc sai cấu trúc trả 400. Bản đã đổi sau lần đọc trả 409.
- Source app ở `frontend/src/components/admin/jlpt-exams`, `frontend/src/lib/exam/jlpt{PilotImport,WorkspaceApi,BlockEnrich}.ts`, `backend/src/Harumi.Exam/Features/ImportJlptPackage`. Khi đổi schema, cập nhật bản nhúng trong backend và so SHA. Kiểm thử frontend bằng `node node_modules/vitest/vitest.mjs run jlpt` ở thư mục frontend; backend bằng `dotnet test backend/tests/Harumi.Exam.Tests/Harumi.Exam.Tests.csproj`. Để chạy test dữ liệu thật, đặt `HARUMI_JLPT_TEST_POSTGRES` đến DB test, `HARUMI_JLPT_TEST_BUNDLE` đến thư mục upload, `HARUMI_JLPT_TEST_QUESTION_COUNT=517`.
