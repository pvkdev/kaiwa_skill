# Hợp đồng gói JLPT 1.2.0

Trang nhập đề trong Harumi Development ở `/admin/jlpt-exams/import`. Xem định dạng thư mục, thao tác thêm/ghi đè và cơ chế thử lại trong [hướng dẫn migration](../../MIGRATION.md).

Đơn vị nhập là một đề, gồm cả phần viết và nghe của cùng cấp/kỳ. `exam-package.schema.json` mô tả một gói. `catalog.schema.json` liệt kê những gói trong một lần nhập toàn kho. Cả hai dùng JSON Schema 2020-12. `synthetic-draft.json` là fixture tự biên, có một đoạn dùng chung hai câu và vài chỗ cố ý bỏ trống để kiểm luồng bản nháp.

## Danh tính, thứ tự và nguồn

- `packageId` là UUID cấp một lần cho một đề. Lưu ID trong lần biên soạn đầu và tái dùng khi đổi tên thư mục, bổ sung script hoặc tải lại HTML. `revision` tăng khi đóng băng bản thay đổi. Mỗi đề có đúng một revision trong catalog. Hash SHA-256 tính trên **bytes file cuối**, kể cả xuống dòng. Không hash lại object sau khi đọc JSON.
- Bốn key Harumi là `mojigoi`, `bunpou`, `dokkai`, `choukai`. Mảng đi theo đúng đề. Giữ nguyên số mondai, nhóm đoạn đọc, số câu mỗi nhóm và nhãn lựa chọn, kể cả khi nhiều section đánh số lại. Dùng `structure.expectations` theo từng mondai, `timings` cho thời gian thi theo một hoặc nhiều section. Thời lượng MP3 là trường riêng. Loại đề `exam.kind` cần căn cứ từ nguồn.
- UUID của mondai, block, câu và media đi theo cùng nội dung qua các revision. Khi thêm câu, lấy lại ID của các câu cũ từ revision trước bằng locator và đối chiếu nội dung. Nếu locator đã đổi hoặc trùng, ghi issue để người biên soạn xác nhận. Không tự tạo bộ UUID mới mỗi lần đọc lại đề. Mỗi đề sở hữu các UUID riêng để cập nhật một đề an toàn trong pool dùng chung. Nhiều câu có thể cùng trỏ tới một file ảnh bằng hash.
- Mỗi HTML có `sources[]` riêng, chứa đường dẫn tương đối gốc `JLPT/` và SHA-256. Gắn `annotations.nodes[]` cho mọi node, với `locator` đủ mở lại đúng khối DOM hoặc dòng phụ lục. Bản dịch câu hỏi/lựa chọn đi vào `prompt.textVi`/`choices[].textVi`, bản dịch đoạn đọc vào `passage.viMd`. Giữ chữ gạch chân, dấu sao xếp từ, bảng và nhãn số chỉ lựa chọn. Không lấy đáp án dựa trên radio đã chọn. `annotations.answers` lưu đáp án nguồn, đáp án AI nếu có và quyết định cuối. Hai bằng chứng mâu thuẫn thì để `correctChoiceId: null`, ghi issue, chờ đối chiếu.
- Gói dùng đường dẫn tương đối từ gốc kho cho HTML và assets. `assets[].assetId` dùng `sha256:<hex>`, các trường ảnh tham chiếu `asset://<hex>`; bytes ở `assets/sha256/<hai-ký-tự-đầu>/<hex>.<ext>`. R2 có thể dùng cùng object key hoặc journal ánh xạ sang key thực do MediaUpload cấp. Chỉ chuyển URL phục vụ ổn định vào payload khi nhập. Presigned PUT URL hết hạn chỉ dùng để upload. Bản đóng gói chuyển máy phải mang các snapshot/asset mà bước kiểm local sẽ đọc.
- Mỗi lời giải cuối đi vào `question.explanation` dưới dạng Markdown tiếng Việt, các ghi chú chọn lọc vào `grammarNotes`/`vocabNotes`. Lưu `annotations.fields[]` cho nội dung biên tập, với UUID node, JSON Pointer tương đối với node và nguồn gốc. `origin=ai` là lời biên soạn của AI kể cả khi dựa trên giải thích VNJPClub. `origin=source` dành cho nội dung trực tiếp từ nguồn. Lưu ID nguồn, hash đầu vào, phiên bản skill/model nếu có và trạng thái review. Đủ căn cứ để đối chiếu nguồn gốc thì ghi vào `note` cụ thể tên trường HTML, dòng script hoặc vị trí ảnh.
- Nếu nêu bài ngữ pháp cụ thể, thêm `annotations.grammarRefs[]` gồm `questionId, catalog, entry, path, locator`. `path` tương đối với gốc repo `kaiwa_skill/` (thư mục cha của `JLPT/`), ví dụ `kaiwa_skill/reference/grammar/MINNA_01_50_GRAMMAR.json`, `locator` chỉ đúng hàng/mục/bài. Ghi tên chính xác của mẫu/bài vào `entry`. Không có kết quả khớp thì bỏ liên kết đó.
- `review.issues[]` có mã, mức độ, UUID đích và yêu cầu cụ thể. Ví dụ yêu cầu bổ sung script cho một nhóm nghe dùng chung ghi rõ cấp/kỳ/mondai/các câu và locator, tránh yêu cầu lại cùng tài liệu cho từng câu. Các file gốc và dữ liệu biên tập tách biệt.

## Bài đọc và script song ngữ

`1.2.0` thêm `annotations.sentencePairs` tùy chọn. Khoá là UUID hiện có của một media `kind: passage`, media `kind: audio` có script dùng chung, hoặc một question có `jlptListenScript`. Giá trị là mảng có thứ tự, mỗi hàng gồm `ja` là chuỗi khác trắng và `vi` là chuỗi khác trắng hoặc `null` khi chưa có bản dịch. Một script chung chỉ có một bộ hàng dù có hai câu hỏi. Xem ví dụ hình dạng trường dưới đây.

```json
{
  "sentencePairs": {
    "87eabb7a-4413-4cd2-bbb8-c6989d049961": [
      { "ja": "女：受付は二階です。", "vi": "Nữ: Quầy tiếp tân ở tầng hai." },
      { "ja": "男：ありがとうございます。", "vi": "Nam: Cảm ơn chị." }
    ]
  }
}
```

Giữ nguyên `passage.jaMd` hoặc `scriptJaMd` cho chế độ đọc nguyên bản, kể cả ký hiệu trống, bảng, nhãn người nói. Giao diện lấy bản Việt đầy đủ từ `passage.viMd`, `audio.scriptViMd` hoặc `jlptListenScript.scriptViMd`. Với node có hàng, trường này phải bằng chính xác `rows.filter(r => r.vi !== null).map(r => r.vi).join("\n")`. Bản song ngữ toàn đoạn dùng hai trường đầy đủ. Bảng Nhật–Việt dùng các hàng theo thứ tự đã biên soạn.

Liên kết một câu Nhật với đúng bản dịch qua DOM anchor/phụ lục cùng nguồn hoặc qua bản biên tập có hash. Nếu nguồn gộp nhiều câu vào một lượt lời, giữ chung lượt lời đến khi có người tách và rà nghĩa hai bên. Đối với biểu mẫu dùng chung và bảng giá, một hàng có thể chứa cả hàng bảng tương ứng bằng Markdown. Bản dịch tự soạn được đánh dấu `origin: ai` trên trường đích. `1.1.0` vẫn nhập được theo các trường nguyên đoạn cũ. Bổ sung hàng vào bản cũ cần tăng `schemaVersion` và `revision`, giữ nguyên toàn bộ UUID.

## Một audio cho một đề

`masterAudio` là bản thu duy nhất của kỳ thi. Giá trị `null` dùng khi chưa biết bản thu. Có thể lưu mốc đã trích từ HTML vào bản nháp ngay cả khi đang đợi MP3, bằng object có `assetId: null`, `rss: null`, `durationMs` đã biết hoặc null. Khi có file, gắn `assetId` của audio tổng. Nếu dùng RSS, ghi cả `feedUrl`, `episodeGuid` và `enclosureUrl` HTTPS của cùng bản thu. Nếu cả hai tồn tại, `rss` là nguồn phát online và asset là bản tham chiếu local. URL trang episode hoặc trang trình phát không phải enclosure. Một số nguồn có thể phát bản khác hoặc chèn intro/quảng cáo; thử seek trước khi xác nhận cùng timeline. Khi đổi master, đối chiếu lại toàn bộ mốc với đúng phiên bản.

`annotations.audioSegments[]` ghi mốc trên đồng hồ **toàn file**, đơn vị mili giây. `startMs` bao gồm, `endMs` loại trừ. `endMs: null` khi chỉ có bằng chứng cho điểm bắt đầu; khi phát phải để người học chủ động dừng hoặc phát tiếp theo kiểu phát cả đề. `sourceId` và `locator` dẫn đến dữ liệu timing có thể đối chiếu. Nếu không rõ đó là đồng hồ cục bộ của player con hay thời điểm toàn file, lưu issue và giữ mốc ở ghi chú nguồn cho tới khi xác minh. Không cộng dồn thời lượng player con để dựng timeline. Vai trò:

- `mondai` có `mondaiId` và `questionIds: []`, dùng cho “Nghe từ mondai này”. Khi suy biên từ nhóm cue đầy đủ, ghi rõ cách xác định và kiểm tra cả hướng dẫn đầu mondai; một tập cue chưa đủ chỉ chứng minh được phạm vi các câu có cue.
- `question` có đúng một UUID câu. `shared` có nhiều UUID trong cùng mondai cho một đoạn chung, có thể chồng với khoảng của mondai. Câu không có cue riêng có thể dùng đoạn chung, rồi mốc mondai, cuối cùng là player cả đề.
- `intro`/`example` gắn vào mondai chứa nó, danh sách câu rỗng. Mốc giới hạn trên là `durationMs` khi biết. Bản ghi đoạn chứa **tham chiếu**, không cần xuất MP3 cắt. Shared script JA/VI nằm trong một media audio ở block chung. Script riêng từng câu có thể đặt vào `jlptListenScript`.

## Ánh xạ tới Harumi

`exam` ánh xạ vào `JlptExamSet`. Mỗi phần tử `content.<section>.mondais` ánh xạ một `JlptMondai`; `section/paper, mondaiNumber, label` là metadata và `instruction, blocks` vào `ContentJson`. `JlptExamSetMondai` nối đề–mondai theo thứ tự mảng của từng section. Adapter ánh xạ `asset://` sang URL ảnh sử dụng được. Câu chỉ có đáp án số vẫn giữ đúng 3 hoặc 4 lựa chọn theo nguồn; ID a/b/c/d áp theo thứ tự, giữ nhãn nguồn riêng. Một block dùng chung một `choiceCount`; khi số lựa chọn khác nhau, tách block và giữ liên kết tới media chung. So sánh vòng xuất–nhập toàn bộ ID, số thứ tự, đoạn đọc, bảng, ảnh và Markdown.

`JlptExamCompositionService` hiện chỉ giữ instruction/instructionHtml/blocks khi split; assemble tạo lại đúng bốn tab. Adapter mới cần lưu master, mốc và metadata import theo ID đề, đọc lại chúng qua API và giữ được khi dùng editor. Chỉ dán JSON gói vào endpoint cũ sẽ mất phần ngoài content. Tham chiếu R2/RSS thuộc tài nguyên phát, không chuyển raw SingleFile hoặc thông tin chạy model lên app. Trước khi tạo/sửa, đối chiếu package→exam và quyền sở hữu mondai để ngăn ghi nhầm lên đề dùng chung. Đụng slug/UUID không thuộc cùng gói phải trả conflict. Gói sửa chỉ cập nhật snapshot mình sở hữu; phát hiện sửa tay ở đích bằng fingerprint. Nếu có shared mondai với đề khác, xử lý xung đột hoặc tạo bản sở hữu riêng có mapping ổn định.

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

