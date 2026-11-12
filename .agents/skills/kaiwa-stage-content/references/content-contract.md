# Dữ liệu nội dung chặng — bản nháp V3

Đây là hợp đồng biên soạn độc lập với engine app. Chỉ chốt giao diện import sau khi người dùng xem các chặng pilot. Không thêm field chấm điểm hoặc cơ chế học chỉ vì engine có thể hỗ trợ.

## Bộ dữ liệu một revision

```text
stage.json                tiêu đề, ID, node có thứ tự, nhóm sự kiện, nguồn
knowledge/<node_id>.md    nội dung giải thích, ví dụ và cách dùng
vocabulary/<node_id>.json danh sách từ
grammar/<node_id>.json    tên mẫu ngữ pháp và tham chiếu
situations/<node_id>.json hội thoại của một tình huống cụ thể
live/<node_id>.json       danh mục context cho một node Live AI
sources.json             sổ nguồn và quá trình đọc/áp dụng
editorial.md              phạm vi, độ bao phủ, quyết định, phần thiếu, lịch sử sửa
live-context.md          bản context đầy đủ do helper ghép từ các node, không sửa tay
```

`stage.json` là mục lục chính. JSON nội dung và Markdown kiến thức là bản gốc biên soạn; `live-context.md` là bản dẫn xuất. Không duy trì thêm bản MD hội thoại phải sửa đồng thời với JSON.

Ví dụ rút gọn cấu trúc, không phải một chặng đã biên soạn:

```json
{
  "schema_version": "3.0-draft",
  "stage_uid": "<UUID từ registry>",
  "display_code": "T-xx",
  "title": "Xin phép trong công việc",
  "level": "Trung",
  "scope": "Xin sử dụng nguồn lực chung và điều chỉnh khi chưa được phép",
  "nodes": [
    {"id":"k01","type":"knowledge","title":"Đề nghị và xác nhận phạm vi cho phép","path":"knowledge/k01.md"},
    {"id":"v01","type":"vocabulary","title":"Lịch và phòng họp","path":"vocabulary/v01.json"},
    {"id":"g01","type":"grammar","title":"Mẫu dùng trong cụm này","path":"grammar/g01.json"},
    {"id":"s01","type":"situation","title":"Được cho phép dùng phòng","path":"situations/s01.json"},
    {"id":"k02","type":"knowledge","title":"Đáp lại lời từ chối","path":"knowledge/k02.md"},
    {"id":"s02","type":"situation","title":"Phòng không trống: đổi phương án","path":"situations/s02.json"},
    {"id":"live01","type":"live_context","title":"Trò chuyện về chủ đề này","path":"live/live01.json"}
  ],
  "events": [{"id":"e01","title":"Xin dùng phòng họp","situation_ids":["s01","s02"]}],
  "retired_ids": [],
  "source_refs": ["src01"]
}
```

Không phải mọi chặng đều cần đúng bộ node như ví dụ. Một chặng có thể có nhiều node kiến thức/từ/ngữ pháp, một hoặc nhiều sự kiện; có đúng **một node Live AI**. Node ngữ pháp chỉ xuất hiện nếu hữu ích. Quan hệ `supports` hoặc `related_ids` là liên kết nội dung, không phải điều kiện mở khóa.

## Kiến thức Markdown

- Tiêu đề rõ; giải thích Việt có chiều sâu vừa đủ cho vấn đề, ví dụ Nhật kèm nghĩa Việt. Giải thích ai nói với ai, ý định, sắc thái, phản ứng và cách tiếp nối khi nguồn có chất liệu.
- Giữ những phần hay của sách: tổ chức lượt nói, phản hồi, lược âm, chiến lược lịch sự, văn hóa, lỗi dễ hiểu sai. Không ép mọi bài thành cùng một bộ heading, không giới hạn cứng số chữ.
- Ví dụ, gợi ý luyện nói, biến thể hội thoại của sách có ích thì chuyển thành nội dung học/nhánh nói thích hợp. Không bê bài viết, bài thi, đáp án kiểm tra vào app.
- Dẫn nguồn bằng ID trong sổ nguồn; không nhồi đường dẫn file, ghi chú OCR hoặc nhận xét kỹ thuật vào phần người học đọc.

## Một tình huống

```json
{
  "id": "s02",
  "event_id": "e01",
  "title": "Phòng không trống: đổi phương án",
  "setting": "Nhân viên hỏi người quản lý lịch phòng trước buổi họp nhóm.",
  "communication_goal": "Hiểu lý do chưa được phép và thống nhất phương án khác.",
  "relationship": "Đồng nghiệp; trao đổi lịch sự trong nội bộ",
  "outcome": "denied_then_alternative",
  "alternative_to": ["s01"],
  "speakers": [
    {"id":"A","role":"Người xin sử dụng phòng"},
    {"id":"B","role":"Người phụ trách lịch phòng"}
  ],
  "turns": [
    {"id":"s02-t01","speaker":"A","ja":"午後、この会議室を使ってもいいですか。","vi":"Chiều nay tôi dùng phòng họp này được không?"},
    {"id":"s02-t02","speaker":"B","ja":"すみません。午後は予約が入っているんです。","vi":"Xin lỗi, chiều nay phòng đã có người đặt rồi."},
    {"id":"s02-t03","speaker":"A","ja":"そうですか。では、別の部屋を確認してみます。","vi":"Vậy à. Thế để tôi kiểm tra phòng khác."}
  ],
  "knowledge_ids": ["k01","k02"],
  "vocabulary_ids": ["v01"],
  "grammar_ids": ["g01"],
  "source_refs": ["src01"],
  "authorship": "original_extension"
}
```

Đoạn trên chỉ minh họa schema và là nội dung viết mới; không gán nó cho sách. Khi biên soạn thật cần hội thoại khép kín tự nhiên, đủ cho diễn biến đó. Không giới hạn ba lượt. `authorship`: `source_adaptation` khi đã đọc chất liệu cụ thể và chuyển soạn, `original_extension` khi tự mở rộng. Tên topic trùng sách không đủ để gọi hội thoại là source adaptation.

Hai vai phải thực sự có lời nói. Sự kiện nhiều người được chia thành những cuộc trao đổi hai vai; không giả vờ lời dẫn là vai thứ hai. Một tình huống có một diễn biến/kết quả rõ. Phê duyệt và từ chối có thể cùng mở đầu nhưng cần hai hội thoại riêng, thay đổi cách xử lý sau phản hồi. Tình huống nối tiếp thời gian dùng `follows`; nhánh thay thế dùng `alternative_to`, không nhầm hai quan hệ.

## Từ vựng và ngữ pháp

```json
{"id":"v01","scope":{"event_ids":["e01"]},"items":[
  {"id":"v01-w01","ja":"会議室","reading":"かいぎしつ","vi":"phòng họp","source_refs":["src01"]}
]}
```

`scope` có thể dùng `stage_uid`, `event_ids` hoặc `situation_ids`. Chọn theo mức liên quan, không chia vụn nếu từ được dùng xuyên suốt. Reading là dữ liệu tùy chọn, không nhúng furigana vào hội thoại. Không thêm dạng bài vocabulary engine, lịch ôn hay ngưỡng đạt.

```json
{"id":"g01","items":[
  {"id":"g01-p01","name_ja":"〜てもいいですか","name_vi":"Xin phép",
   "reference":{"kind":"minna","lesson":15,"edition":"2"},
   "bunpou_id":null,"link_status":"pending_bunpou"}
]}
```

Chỉ cần tên và tham chiếu. Nếu có metadata bunpou phù hợp thì dùng ID/path thật; nếu chưa có thì giữ tên, không bịa ID và không khóa nội dung. Không tự nhân một ngữ pháp thành ba mức JLPT. Minna bài 1–25/26–50 là hai phần sơ cấp, không phải ranh giới JLPT được cơ quan khảo thí xác nhận.

## Nguồn

`sources.json` có `scan` gồm 27 mục `{book_id, status, note}`; status là `index_only` hoặc `read`. `entries` là các chất liệu được dùng thật:

```json
{"id":"src01","kind":"book","book_id":"B02",
 "path":"kaiwa_skill/knowledge/<thư-mục>/<file>.md",
 "locator":{"heading":"<heading đã kiểm>","lines":[100,140]},
 "sha256":"<hash file>","read_status":"read",
 "used_for":["s01","k01"],"contribution":"Cách xin phép sử dụng phòng; không chứng minh nội dung xin nghỉ."}
```

Đường dẫn tính từ repo. Giữ hash file nguồn lúc đọc; line/heading giúp tìm lại, không phải lời khẳng định nguyên văn. Memo dùng `kind: memo`, đúng số bài, `read_status: index_only`; web đọc toàn phần dùng `kind: web`, URL/ngày truy cập. Chất liệu tự mở rộng ghi `kind: original`, căn cứ và giới hạn. Có thể dẫn một nguồn hỗ trợ chức năng giao tiếp mà vẫn ghi hội thoại là viết mới. Không biến memo hoặc nguồn ngân hàng ngôn ngữ thành chứng cứ cho cả tình huống cụ thể.

Lưu thông tin audio biết được dưới `audio_evidence`: sách/ấn bản, nhãn CD/track, vị trí bằng chứng, URL nếu đã thấy; `availability: unknown|inventory_only|file_verified`. Không gán audio gốc cho hội thoại đã viết lại.

## Node Live AI

```json
{"id":"live01","context_node_ids":["k01","v01","g01","s01","k02","s02"],
 "overview_vi":"Phạm vi giao tiếp của chặng", "optional_extensions":["Các nguồn lực chung khác trong văn phòng"],
 "context_export":"live-context.md"}
```

Danh sách phải bao gồm mọi node còn lại của chặng. Helper ghép nguyên nội dung các node đó theo thứ tự, giữ toàn bộ hội thoại/từ/ngữ pháp, thêm bối cảnh chặng và sổ nguồn để app có thể lấy context. Không tạo đề kiểm tra, rubric, máy trạng thái AI hoặc bắt AI chỉ được hỏi một tập câu. App quyết định cách nạp/lọc context và cách người học mở rộng free talk.
