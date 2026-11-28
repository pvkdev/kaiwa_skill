# Hợp đồng gói JLPT 1.3.0

Trang nhập đề trong Harumi Development ở `/admin/jlpt-exams/import`. Xem định dạng thư mục, thao tác thêm/ghi đè và cơ chế thử lại trong [hướng dẫn migration](../../MIGRATION.md).

Đơn vị nhập là một đề, gồm cả phần viết và nghe của cùng cấp/kỳ. `exam-package.schema.json` mô tả một gói. `catalog.schema.json` liệt kê những gói trong một lần nhập toàn kho. Cả hai dùng JSON Schema 2020-12. `synthetic-draft.json` là fixture tự biên, có một đoạn dùng chung hai câu và vài chỗ cố ý bỏ trống để kiểm luồng bản nháp.

## Quy ước cho bản 1.3

- Danh tính biên soạn là `(exam.level, exam.slug)`, ví dụ `N3` và `2025/12`. Cấp hợp lệ từ N5 đến N1. Năm, tháng là số và phải khớp slug. Thư mục dùng `packages/N3/2025-12/`. Harumi giữ `2025/12` trong `importMetadata.periodSlug` và lưu `2025-12` ở cột slug cho các route nhận một đoạn URL. Khi nâng gói cũ, giữ nguyên packageId và mọi UUID, tăng revision. Importer đọc cả 1.1 và 1.2 theo slug cũ.
- Đề gốc gồm HTML bất biến, file đính kèm và hash. Phần phát cho người học lưu chính chữ Nhật, thứ tự, nhóm, hình, bảng và khóa gốc. Ruby là lớp hiển thị riêng của Harumi. Lời giải biên tập, dịch, furigana và STT đều có nguồn gốc riêng. Nếu bản gốc tự mâu thuẫn, giữ nguyên văn, ghi issue có UUID, locator và yêu cầu đối chiếu. Một bản chụp có thể đầy đủ file nhưng vẫn còn lỗi nội dung.
- `review.status=approved` hiển thị **Hoàn thành**. `draft` hoặc `needs_review` hiển thị **Còn thiếu**. Đây là trạng thái biên soạn của revision nhập. `IsPublished` quản lý việc xuất bản riêng. Mỗi issue có mã, mức độ, UUID đích (null cho cả đề), mô tả và vị trí có thể tìm lại. Checklist theo repo tổng hợp nguồn hiện hành, số mục có/cần, UUID, câu, dòng và người xử lý. Chạy lại sau khi cập nhật nguồn, RSS hoặc package. [Chi tiết checklist](../../reports/exam-checklist.json)
- `annotations.sentencePairs` bắt buộc có ở 1.3. Với bản hoàn thành, từng câu Nhật có bản Việt tương ứng theo thứ tự. Bảng có thể giữ đơn vị hàng/ô và nhãn. JA hiển thị nguyên bản và cho tra từ. VI lấy bản Việt đã ghép. Trong JAVI, chạm câu Nhật để hiện nghĩa tương ứng. Bản nháp có thể có `vi:null`. Bản cũ chỉ có dịch nguyên đoạn vẫn hiển thị được ở VI.
- Đối với phần nghe, dùng một master. Bản hoàn thành cần enclosure RSS, script Nhật, bản dịch và đủ cặp start/end cho từng mondai cùng các câu. Hai câu hỏi cùng một hội thoại có thể dùng chung một cue `shared`. Lưu mốc riêng nếu có bằng chứng riêng. Với đề chỉ có phần viết theo nguồn, ghi bằng chứng phạm vi tại hồ sơ kỳ và để phần nghe rỗng. Điểm kết thúc của đoạn là mốc loại trừ.
- Khi trộn mondai từ nhiều đề, lấy `practiceSource` qua `GET /api/exam/admin/jlpt-mondais/{id}`. Câu hỏi kế thừa group từ `JlptMondai.Section` và giữ nguyên block cùng tư liệu. `practiceSource.examId` xác định đề gốc, `masterAudioUrl` xác định track nghe. `audioSegments`, `sentencePairs`, `questionLabels` chỉ chứa mốc và UUID của mondai được hỏi. Quan hệ trong DB qua `JlptExamSetMondai` giữ được nguồn khi ghép nhiều đề. Sửa master/cue trong đề rồi đọc lại mondai sẽ dùng dữ liệu mới. Mondai soạn tay có thể nhận `practiceSource:null`.
- `structure.timings[].seconds` là thời gian thi cho các `sectionKeys` nêu rõ, có nguồn. Khi không biết thời gian thi, giữ mảng rỗng. `masterAudio.durationMs` chỉ mô tả độ dài bản ghi. [Quy trình STT](../../.agents/skills/jlpt-listening/SKILL.md) và [binding RSS](../../tools/AUDIO_RSS.md).

## Danh tính, thứ tự và nguồn

- `packageId` là UUID cấp một lần cho một đề. Lưu ID trong lần biên soạn đầu và tái dùng khi đổi tên thư mục, bổ sung script hoặc tải lại HTML. `revision` tăng khi đóng băng bản thay đổi. Mỗi đề có đúng một revision trong catalog. Hash SHA-256 tính trên **bytes file cuối**, kể cả xuống dòng. Không hash lại object sau khi đọc JSON.
- Bốn key Harumi là `mojigoi`, `bunpou`, `dokkai`, `choukai`. Mảng đi theo đúng đề. Giữ nguyên số mondai, nhóm đoạn đọc, số câu mỗi nhóm và nhãn lựa chọn, kể cả khi nhiều section đánh số lại. Dùng `structure.expectations` theo từng mondai, `timings` cho thời gian thi theo một hoặc nhiều section. Thời lượng MP3 là trường riêng. Loại đề `exam.kind` cần căn cứ từ nguồn.
- UUID của mondai, block, câu và media đi theo cùng nội dung qua các revision. Khi thêm câu, lấy lại ID của các câu cũ từ revision trước bằng locator và đối chiếu nội dung. Nếu locator đã đổi hoặc trùng, ghi issue để người biên soạn xác nhận. Không tự tạo bộ UUID mới mỗi lần đọc lại đề. Mỗi đề sở hữu các UUID riêng để cập nhật một đề an toàn trong pool dùng chung. Nhiều câu có thể cùng trỏ tới một file ảnh bằng hash.
- Mỗi HTML có `sources[]` riêng, chứa đường dẫn tương đối gốc `JLPT/` và SHA-256. Gắn `annotations.nodes[]` cho mọi node, với `locator` đủ mở lại đúng khối DOM hoặc dòng phụ lục. Bản dịch câu hỏi/lựa chọn đi vào `prompt.textVi`/`choices[].textVi`, bản dịch đoạn đọc vào `passage.viMd`. Giữ chữ gạch chân, dấu sao xếp từ, bảng và nhãn số chỉ lựa chọn. Không lấy đáp án dựa trên radio đã chọn. `annotations.answers` lưu đáp án nguồn, đáp án AI nếu có và quyết định cuối. Hai bằng chứng mâu thuẫn thì để `correctChoiceId: null`, ghi issue, chờ đối chiếu.
- Gói dùng đường dẫn tương đối từ gốc kho cho HTML và assets. `assets[].assetId` dùng `sha256:<hex>`, các trường ảnh tham chiếu `asset://<hex>`; bytes ở `assets/sha256/<hai-ký-tự-đầu>/<hex>.<ext>`. R2 có thể dùng cùng object key hoặc journal ánh xạ sang key thực do MediaUpload cấp. Chỉ chuyển URL phục vụ ổn định vào payload khi nhập. Presigned PUT URL hết hạn chỉ dùng để upload. Bản đóng gói chuyển máy phải mang các snapshot/asset mà bước kiểm local sẽ đọc.
- Mỗi lời giải cuối đi vào `question.explanation` dưới dạng Markdown tiếng Việt, các ghi chú chọn lọc vào `grammarNotes`/`vocabNotes`. Lưu `annotations.fields[]` cho nội dung biên tập, với UUID node, JSON Pointer tương đối với node và nguồn gốc. Khi HTML hoặc phụ lục đúng câu có lời giải, lưu nguyên văn và ngắt đoạn của nguồn, ghi `origin=source` cùng sourceId/locator. Bản biên tập cũ chỉ được dùng cho câu thiếu lời giải nguồn. Khi thiếu, AI dùng bằng chứng của chính câu và lối giải thích VNJPClub cùng dạng, ghi `origin=ai`. Chỉ có khóa đáp án thì cần thêm căn cứ để soạn. Mâu thuẫn với khóa được ghi riêng trong review. Quy tắc này dùng cấu trúc gói hiện hành. Lưu ID nguồn, hash đầu vào, phiên bản skill/model nếu có và trạng thái review. Đủ căn cứ để đối chiếu nguồn gốc thì ghi vào `note` cụ thể tên trường HTML, dòng script hoặc vị trí ảnh.
- Nếu nêu bài ngữ pháp cụ thể, thêm `annotations.grammarRefs[]` gồm `questionId, catalog, entry, path, locator`. `path` tương đối với gốc repo `kaiwa_skill/` (thư mục cha của `JLPT/`), ví dụ `kaiwa_skill/reference/grammar/MINNA_01_50_GRAMMAR.json`, `locator` chỉ đúng hàng/mục/bài. Ghi tên chính xác của mẫu/bài vào `entry`. Không có kết quả khớp thì bỏ liên kết đó.
- `review.issues[]` có mã, mức độ, UUID đích và yêu cầu cụ thể. Ví dụ yêu cầu bổ sung script cho một nhóm nghe dùng chung ghi rõ cấp/kỳ/mondai/các câu và locator, tránh yêu cầu lại cùng tài liệu cho từng câu. Các file gốc và dữ liệu biên tập tách biệt.

## Bài đọc và script song ngữ

`1.2.0` thêm `annotations.sentencePairs` tùy chọn. Khoá là UUID hiện có của một media `kind: passage`, media `kind: audio` có script dùng chung, hoặc một question có `jlptListenScript`. Giá trị là mảng có thứ tự, mỗi hàng gồm `ja` là chuỗi khác trắng và `vi` là chuỗi khác trắng hoặc `null` khi chưa có bản dịch. Một script chung chỉ có một bộ hàng dù có hai câu hỏi. Xem ví dụ hình dạng trường dưới đây.

```json
{
  "sentencePairs": {
    "87eabb7a-4413-4cd2-bbb8-c6989d049961": [
      { "ja": "女：受付は二階です。", "vi": "**Nữ**: Quầy tiếp tân ở tầng hai." },
      { "ja": "階段を使ってください。", "vi": "Xin hãy đi cầu thang bộ." },
      { "ja": "男：ありがとうございます。", "vi": "**Nam**: Cảm ơn chị." }
    ]
  }
}
```

### Bố cục song ngữ và nhãn nhân vật (quy ước biên tập 1.3)

Ví dụ trên tương ứng hai dòng nguồn: `女：受付は二階です。階段を使ってください。` rồi `男：ありがとうございます。`. Ba hàng dữ liệu tạo hai lượt lời ở cả JA và VI. Giữ nguyên dấu, nội dung và xuống dòng trong `jaMd`/`scriptJaMd`. Mỗi `ja` là câu trích từ đó, bao gồm nhãn người nói nếu có. Ở đầu lượt thoại, đặt **chỉ tên hoặc vai** của nhân vật trong cặp dấu `**` ở đầu `vi`, theo mẫu `**Nhân viên**: Xin mời.`. Dấu hai chấm nằm ngoài phần đậm. Đó là tín hiệu để Harumi cũng in đậm nhãn tương ứng trước `:` hoặc `：` ở bản Nhật. Chỉ dùng khi xác định được người nói từ nguồn. Giờ, URL, nhãn bảng và lời dẫn giữ định dạng riêng.

Một hàng phục vụ một câu tra dịch. Mỗi ngôn ngữ giữ bố cục theo đoạn nguồn, gồm tiêu đề, dòng trống, lượt nói, danh sách, bảng và chú thích. Câu tiếp theo của cùng lượt không lặp lại tên. Ở bảng, giữ hàng phân cách, số cột, ô trống và thứ tự ô trong bản Việt. `viMd`/`scriptViMd` lưu đúng phép nối các `vi` khác null bằng `\n` theo hợp đồng nhập. Khi hiển thị, Harumi lấy ranh giới đoạn và lượt lời từ vị trí các hàng trong JA. Bằng chứng HTML và UUID được giữ nguyên; chỉnh cặp câu trong gói đã nhập cần tăng revision.

Giữ nguyên `passage.jaMd` hoặc `scriptJaMd` cho chế độ đọc nguyên bản, kể cả ký hiệu trống, bảng, nhãn người nói. Giao diện lấy bản Việt đầy đủ từ `passage.viMd`, `audio.scriptViMd` hoặc `jlptListenScript.scriptViMd`. Với node có hàng, trường này phải bằng chính xác `rows.filter(r => r.vi !== null).map(r => r.vi).join("\n")`. Trong JAVI, ánh xạ từng hàng vào đúng vị trí trong bài Nhật để người học chạm xem bản dịch.

Liên kết một câu Nhật với đúng bản dịch qua DOM anchor/phụ lục cùng nguồn hoặc qua bản biên tập có hash. Nếu nguồn gộp nhiều câu vào một lượt lời, lưu bằng chứng gộp trong HTML, sau đó tách và rà nghĩa hai bên trước khi duyệt 1.3. Đối với biểu mẫu dùng chung và bảng giá, một hàng có thể chứa cả hàng bảng tương ứng bằng Markdown. Bản dịch tự soạn được đánh dấu `origin: ai` trên trường đích. `1.1.0` vẫn nhập được theo các trường nguyên đoạn cũ. Bổ sung hàng vào bản cũ cần tăng `schemaVersion` và `revision`, giữ nguyên toàn bộ UUID.

## Một audio cho một đề

`masterAudio` là bản thu duy nhất của kỳ thi. Giá trị `null` dùng khi chưa biết bản thu. Có thể lưu mốc đã trích từ HTML vào bản nháp ngay cả khi đang đợi MP3, bằng object có `assetId: null`, `rss: null`, `durationMs` đã biết hoặc null. Khi có file, gắn `assetId` của audio tổng. Nếu dùng RSS, ghi cả `feedUrl`, `episodeGuid` và `enclosureUrl` HTTPS của cùng bản thu. Nếu cả hai tồn tại, `rss` là nguồn phát online và asset là bản tham chiếu local. URL trang episode hoặc trang trình phát không phải enclosure. Một số nguồn có thể phát bản khác hoặc chèn intro/quảng cáo; thử seek trước khi xác nhận cùng timeline. Khi đổi master, đối chiếu lại toàn bộ mốc với đúng phiên bản.

`annotations.audioSegments[]` ghi mốc trên đồng hồ **toàn file**, đơn vị mili giây. `startMs` bao gồm, `endMs` loại trừ. `endMs: null` khi chỉ có bằng chứng cho điểm bắt đầu; khi phát phải để người học chủ động dừng hoặc phát tiếp theo kiểu phát cả đề. `sourceId` và `locator` dẫn đến dữ liệu timing có thể đối chiếu. Nếu không rõ đó là đồng hồ cục bộ của player con hay thời điểm toàn file, lưu issue và giữ mốc ở ghi chú nguồn cho tới khi xác minh. Không cộng dồn thời lượng player con để dựng timeline. Vai trò:

- `mondai` có `mondaiId` và `questionIds: []`, dùng cho “Nghe từ mondai này”. Khi suy biên từ nhóm cue đầy đủ, ghi rõ cách xác định và kiểm tra cả hướng dẫn đầu mondai; một tập cue chưa đủ chỉ chứng minh được phạm vi các câu có cue.
- `question` có đúng một UUID câu. `shared` có nhiều UUID trong cùng mondai cho một đoạn chung, có thể chồng với khoảng của mondai. Câu không có cue riêng có thể dùng đoạn chung, rồi mốc mondai, cuối cùng là player cả đề.
- `intro`/`example` gắn vào mondai chứa nó, danh sách câu rỗng. Mốc giới hạn trên là `durationMs` khi biết. Bản ghi đoạn chứa **tham chiếu**, không cần xuất MP3 cắt. Shared script JA/VI nằm trong một media audio ở block chung. Script riêng từng câu có thể đặt vào `jlptListenScript`.

## Ánh xạ tới Harumi

`exam` ánh xạ vào `JlptExamSet`. Mỗi phần tử `content.<section>.mondais` ánh xạ một `JlptMondai`; `section/paper, mondaiNumber, label` là metadata và `instruction, blocks` vào `ContentJson`. `JlptExamSetMondai` nối đề–mondai theo thứ tự mảng của từng section. Adapter ánh xạ `asset://` sang URL ảnh sử dụng được. Câu chỉ có đáp án số vẫn giữ đúng 3 hoặc 4 lựa chọn theo nguồn; ID a/b/c/d áp theo thứ tự, giữ nhãn nguồn riêng. Một block dùng chung một `choiceCount`; khi số lựa chọn khác nhau, tách block và giữ liên kết tới media chung. So sánh vòng xuất–nhập toàn bộ ID, số thứ tự, đoạn đọc, bảng, ảnh và Markdown.

`JlptExamCompositionService` hiện chỉ giữ instruction/instructionHtml/blocks khi split; assemble tạo lại đúng bốn tab. Importer lưu master, mốc và metadata theo ID đề. Editor và API đọc lại những trường này. Chỉ dán JSON gói vào endpoint cũ sẽ mất phần ngoài content. Tham chiếu R2/RSS thuộc tài nguyên phát, không chuyển raw SingleFile hoặc thông tin chạy model lên app. Trước khi tạo/sửa, đối chiếu package→exam và quyền sở hữu mondai để ngăn ghi nhầm lên đề dùng chung. Đụng slug/UUID không thuộc cùng gói phải trả conflict. Gói sửa chỉ cập nhật snapshot mình sở hữu; phát hiện sửa tay ở đích bằng fingerprint. Nếu có shared mondai với đề khác, xử lý xung đột hoặc tạo bản sở hữu riêng có mapping ổn định.

Catalog chứa `schemaVersion, packages[]`; mỗi entry có `packageId, revision, path, sha256`. Luồng nhập kiểm **tất cả** entry và asset trước khi ghi. Cùng ID/revision và hash đã commit là no-op; cùng revision khác hash hoặc revision lùi là conflict. Revision tăng cập nhật cùng exam. Mỗi đề có transaction và nhật ký tiến độ riêng để chạy lại sau lỗi; không xóa đề chỉ vì một gói vắng mặt trong catalog.

## Chạy kiểm tra

Từ thư mục `JLPT/`, dùng Python 3.11+ có thư viện `jsonschema` 4.x. Lệnh đầu phải PASS; fixture draft có lỗi biên tập có chủ đích nên lệnh thêm `--release` phải trả mã lỗi.

```powershell
py -3 contracts/v1/validate_package.py contracts/v1/synthetic-draft.json --root .
py -3 contracts/v1/validate_package.py contracts/v1/synthetic-draft.json --root . --release
```

Với một gói hoặc catalog đã đóng băng, thay đối số đầu bằng đường dẫn JSON thật. Validator kiểm schema, path/hash/size, khóa và liên kết nguồn, nội dung, phân đoạn, căn chỉnh mốc với thời lượng, đáp án, số câu khai báo và UUID trùng. `--release` kiểm thêm nguồn phát nghe, script riêng hoặc script chung trong block, lời giải đã có provenance, đáp án đã giải quyết, review toàn gói và lỗi đang mở. Validator chưa đọc hiểu đề, xác nhận dịch/ngữ pháp, kiểm HTTPS seek, so sánh với phiên bản cũ/DB, hay đo bản MP3 thực tế; các bước QA và importer dev đảm nhiệm những phần này. Byte hash của các nguồn cho phép đối chiếu lại đúng dữ liệu đã dùng.

## Hai phép kiểm ngoài schema

1. **Độ phủ so với nguồn**. Expectations đối chiếu hai phần của cùng một gói. Chúng không phát hiện một mondai mà người xuất đã bỏ quên ở cả hai phần. Trước khi duyệt, đối chiếu kiểm kê HTML **độc lập** với toàn bộ `annotations.nodes`: danh sách ID câu theo từng file/phần, số và thứ tự lựa chọn, đáp án, số đoạn đọc/script/ảnh, script dùng chung và các bảng đứng ở khối kế bên. Chênh lệch được ghi theo sourceId/locator. Tạo mã vấn đề cho các capture thiếu hẳn phần nghe hoặc phần viết.
2. **Bản sửa AI đến muộn**. Lưu đúng bytes đầu vào của lượt giao việc, gồm câu/đáp án/đoạn dẫn, nguồn giải thích và các tham chiếu ngữ pháp dùng cho lượt đó. `annotations.fields[].inputSha256` là SHA-256 của bytes đầu vào này. Khi nhận patch, so base revision, hash bytes đầu vào đã giao so với input hiện hành và giá trị cũ ở trường đích; lệch thì không áp patch, làm lại với đầu vào mới. Validator gói chỉ xác nhận hash nguồn/assets trên đĩa và sự hiện diện của thông tin lượt AI. Không thể dựng lại hash một prompt cũ từ riêng Markdown đã biên tập.

## Chuyển bản nháp cũ từ 1.0.0

Gói `1.0.0` ở kho thử `D:/JLPT` dùng cùng envelope bốn tab, nhưng `annotations.audioSegments` từng gắn với từng asset. Khi nâng sang `1.1.0`, giữ nguyên ID và lưu snapshot cũ; chọn đúng master, mở rộng bộ tham chiếu cue theo mondai/câu, kiểm lại đơn vị và timebase, rồi validate. Nếu chỉ có thời gian tương đối trên clip, giữ dữ liệu cũ để đối chiếu và yêu cầu mốc master. Gói chỉ có văn bản đặt `masterAudio: null`. Với hợp đồng đóng field, mọi lần thay đổi version cần adapter biết version cụ thể.

