# Dữ liệu nội dung chặng — bản nháp V3.2

Đây là hợp đồng biên soạn độc lập với engine app. Chỉ chốt giao diện import sau khi người dùng xem các chặng pilot. Không thêm field chấm điểm hoặc cơ chế học chỉ vì engine có thể hỗ trợ.

## Bộ dữ liệu một revision

```text
stage.json                tiêu đề, ID, node có thứ tự, nhóm sự kiện, nguồn
knowledge/<node_id>.md    nội dung giải thích, ví dụ và cách dùng
vocabulary/<node_id>.json danh sách từ
grammar/<node_id>.json    tên mẫu ngữ pháp và tham chiếu
situations/<node_id>.json hội thoại của một tình huống cụ thể
shadowing/<node_id>.json  nhóm câu mẫu/hội thoại luyện, hoặc trỏ tình huống
live/<node_id>.json       context và tình huống đã biên soạn cho free talk cuối chặng
learning-map.json         các bài, điều mới, bài trước đã đọc và nội dung dùng lại
sources.json             sổ nguồn và quá trình đọc/áp dụng
editorial.md              phạm vi, độ bao phủ, quyết định, phần thiếu, lịch sử sửa
live-context.md          bản context đầy đủ do helper ghép từ các node, không sửa tay
free-talk-situation.md   tình huống free talk sẵn dùng kèm nội dung học, không sửa tay
```

`stage.json` là mục lục chính. JSON nội dung và Markdown kiến thức là bản gốc biên soạn; `live-context.md` là bản dẫn xuất. Không duy trì thêm bản MD hội thoại phải sửa đồng thời với JSON.

Ví dụ rút gọn cấu trúc, không phải một chặng đã biên soạn:

```json
{
  "schema_version": "3.2-draft",
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

Không phải mọi chặng đều cần đúng bộ node như ví dụ. Một chặng có thể có nhiều node kiến thức/từ/ngữ pháp, một hoặc nhiều sự kiện; có đúng **một node free talk cuối chặng**, phân biệt với các challenge có nhiệm vụ trong thiết kế bổ sung. Node ngữ pháp chỉ xuất hiện nếu hữu ích. Quan hệ `supports` hoặc `related_ids` là liên kết nội dung, không phải điều kiện mở khóa.

V3.1 thêm nhóm bài/gối đầu và loại node `shadowing`. Helper vẫn đọc bản 3.0 cũ; khi nâng cấp thì tạo draft/revision mới, giữ ID, thêm sổ bài và các trường mới, không sửa snapshot cũ.

V3.2 thêm phần free talk do tác giả soạn sẵn và file dẫn xuất `free-talk-situation.md`; giữ tương thích đọc V3.0/V3.1. Nội dung lộ trình không bị giới hạn 1.000 ký tự như tình huống user nhập tay trong app. Đây chưa phải hợp đồng import Harumi hoặc triển khai node challenge.

## Nhóm bài và gối đầu

`learning-map.json` là sổ biên soạn, không phải trạng thái người học. Các `node_ids` của bài phân chia toàn bộ node trừ Live đúng một lần, theo thứ tự trong `stage.json`. Danh sách từ chung có thể được đặt ở một bài rồi tham chiếu từ nhiều bài khác. Live không tính thành một bài để chọn hai bài gần nhất.

```json
{"schema_version":"1.0","stage_uid":"<UUID chặng>","lessons":[
  {"id":"l01","summary":"Xin phép và xác nhận phạm vi cho phép",
   "node_ids":["k01","v01","g01","s01"],"lookback":[],"reuse":[],
   "pending_previous":[],"reason_no_reuse":"Bài đầu tiên trong ví dụ cấu trúc này."},
  {"id":"l02","summary":"Đáp lại lời từ chối và chọn phương án khác",
   "node_ids":["k02","s02"],
   "lookback":[{"stage_uid":"<cùng UUID>","revision":null,"lesson_id":"l01"}],
   "reuse":[{"from":{"stage_uid":"<cùng UUID>","revision":null,"lesson_id":"l01","node_id":"k01"},
             "in":[{"node_id":"s02","item_id":"s02-t01"}],"purpose":"Dùng lại cách xin phép trước phản hồi từ chối."}],
   "pending_previous":[]}
]}
```

Đây là ví dụ nối liên kết, không chứng minh đã biên soạn bài. Trước bài 3, `lookback` thường có l01 và l02; thêm bài xa hơn khi phù hợp. Nếu không dùng lại gì, ghi lý do; không có tỷ lệ ôn hay số từ cũ bắt buộc. Phần còn thiếu do chưa có bài trước nằm trong `pending_previous` và nhật ký, không bịa thành đã học.

Tham chiếu nội bộ dùng `revision: null`; `lesson_id` phải đứng trước. Khác chặng dùng UUID + revision `r0001`… đã chốt + lesson ID, và `from` chỉ rõ node/item được tái sử dụng. `item_id` có thể là ID từ, mẫu câu, ví dụ hoặc lượt nói; bỏ field đó nếu dùng lại ý kiến thức của cả node. `in` chỉ rõ nơi tái xuất hiện ở bài hiện tại. Chưa có bài trước thì chỉ ghi pending, không trỏ draft khác.

Helper kiểm vị trí/ID, đọc các file của bài trước, pin hash và so revision hiện hành khi kiểm draft. Nó không xác minh rằng câu mới thực sự vận dụng đúng ý cũ. Xem [quy trình gối đầu](progression.md) để chọn kiến thức, mở rộng từ vựng và xử lý nâng cấp.

## Kiến thức Markdown

- Tiêu đề rõ; giải thích Việt có chiều sâu vừa đủ cho vấn đề, ví dụ Nhật kèm nghĩa Việt. Giải thích ai nói với ai, ý định, sắc thái, phản ứng và cách tiếp nối khi nguồn có chất liệu.
- Giữ những phần hay của sách: tổ chức lượt nói, phản hồi, lược âm, chiến lược lịch sự, văn hóa, lỗi dễ hiểu sai. Không ép mọi bài thành cùng một bộ heading, không giới hạn cứng số chữ.
- Ví dụ, gợi ý luyện nói, biến thể hội thoại của sách có ích thì chuyển thành nội dung học/nhánh nói thích hợp. Không bê bài viết, bài thi, đáp án kiểm tra vào app.
- Dẫn nguồn bằng ID trong sổ nguồn; không nhồi đường dẫn file, ghi chú OCR hoặc nhận xét kỹ thuật vào phần người học đọc.

Với bài mới lấy từ B11/B12 Speak Japanese, node có dạng:

```json
{"id":"k03","type":"knowledge","title":"Tên bài kiến thức",
 "path":"knowledge/k03.md","source_family":"speak_japanese",
 "source_refs":["src_sj03"],"video":{"status":"planned","asset_ref":null},
 "practice_node_id":"sh03"}
```

Trong `stage.nodes`, `sh03` phải đứng **ngay sau** k03. MD chứa bài giảng thực sự chứ không chỉ tên mẫu; video để người dùng làm sau. Các ví dụ dùng để luyện nối bằng anchor `example_id`, ví dụ `<a id="ex03-01"></a>` trong MD. Phần ví dụ sách và phần mở rộng có gối đầu phải phân biệt nguồn/viết mới.

## Bài shadowing

```json
{"id":"sh03","knowledge_ids":["k03"],"source_refs":["src_sj03"],"items":[
  {"id":"sh03-e01","kind":"sentence","example_id":"ex03-01",
   "ja":"この料理、おいしいですね。","vi":"Món này ngon nhỉ.","authorship":"original_extension"},
  {"id":"sh03-d01","kind":"dialogue","example_id":"ex03-02",
   "speakers":[{"id":"A","role":"Người hỏi"},{"id":"B","role":"Người đáp"}],
   "turns":[{"id":"sh03-d01-t01","speaker":"A","ja":"これ、辛いですか。","vi":"Món này cay không?"},
            {"id":"sh03-d01-t02","speaker":"B","ja":"少し辛いですよ。","vi":"Hơi cay đấy."}],
   "authorship":"original_extension"}
]}
```

Các câu trên chỉ minh họa dữ liệu viết mới, không gán cho sách. Mỗi bài luyện phải thực hành đúng điểm kiến thức vừa giảng, điều này do biên tập kiểm lại. Nếu `knowledge_ids` chứa node Speak Japanese, mỗi item cần `example_id` tồn tại trong MD liên quan. Anchor chứng minh liên kết, không chứng minh nội dung khớp về nghĩa.

Để dùng lại tình huống đã có mà không sao chép lời, item có thể là `{"id":"sh05-r01","kind":"situation_ref","situation_id":"s01"}`. Helper đưa cả tình huống gốc vào context chặng qua node situation. Hội thoại mini dùng hai vai A/B; câu độc lập chỉ có Nhật–Việt, không bịa vai thứ hai. Các nhóm 5500/必須700/Nama/なめらか/Shadowing dùng loại node này với nguồn thật, không bắt có video.

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
  {"id":"v01-w01","ja":"会議室","reading":"かいぎしつ","vi":"phòng họp","exposure":"new","source_refs":["src01"]}
]}
```

`scope` có thể dùng `stage_uid`, `lesson_ids`, `event_ids` hoặc `situation_ids`. Chọn theo mức liên quan, không chia vụn nếu từ được dùng xuyên suốt. Danh sách bao phủ các nhóm từ thực tế trong phạm vi topic, không chỉ những từ đang có trong hội thoại. V3.1 đánh dấu `exposure: new|review` cho từng item; từ review có liên kết `reuse` từ item cũ đến item hiện tại trong sổ bài. Xét đúng nghĩa/cách dùng. Reading là dữ liệu tùy chọn, không nhúng furigana vào hội thoại. Không thêm dạng bài vocabulary engine, lịch ôn hay ngưỡng đạt.

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

Đường dẫn tính từ repo. Giữ hash file nguồn lúc đọc; line/heading giúp tìm lại, không phải lời khẳng định nguyên văn. Memo dùng `kind: memo`, đúng số bài, `read_status: index_only`; web đã đọc phần dùng được ghi `kind: web`, URL/ngày truy cập/phần đã đọc và giới hạn. Không gọi một trang tìm kiếm hoặc phần trích kết quả là đã đọc toàn trang. Chất liệu AI biên soạn ghi `kind: original`, căn cứ và giới hạn; đây là nguồn nội dung hợp lệ và quan trọng, không cần mọi hội thoại mới phải có một hội thoại sách tương ứng. Có thể dẫn nguồn ngoài xác nhận bối cảnh/dữ kiện hoặc sách hỗ trợ chức năng giao tiếp mà vẫn ghi `authorship: original_extension`. Không biến memo hoặc nguồn ngân hàng ngôn ngữ thành chứng cứ cho cả tình huống cụ thể.

`scan` là rà chỉ mục 27 sách để tìm chất liệu, không phải yêu cầu dùng đủ 27 sách trong chặng hoặc kiểm kê chi tiết mọi câu. `entries` ghi phần được dùng thật. Nếu bổ sung báo cáo độ phủ, phải ghi rõ đơn vị đếm/phạm vi; đó là thông tin hỗ trợ quyết định, không có ngưỡng 100% để chốt revision. Tài nguyên chưa dùng không mặc nhiên là lỗi hoặc nội dung bắt buộc bổ sung. Chỉ các lỗ hổng ảnh hưởng mục tiêu chặng mới cần xử lý để hoàn thiện bài; giữ nguồn chính xác cho phần đã chọn.

Lưu thông tin audio biết được dưới `audio_evidence`: sách/ấn bản, nhãn CD/track, vị trí bằng chứng, URL nếu đã thấy; `availability: unknown|inventory_only|file_verified`. Không gán audio gốc cho hội thoại đã viết lại.

## Node free talk cuối chặng

```json
{"id":"live01","context_node_ids":["k01","v01","g01","s01","k02","s02"],
 "overview_vi":"Phạm vi giao tiếp của chặng", "optional_extensions":["Các nguồn lực chung khác trong văn phòng"],
 "context_export":"live-context.md",
 "free_talk":{
   "mode":"free_talk","content_origin":"curriculum_authored",
   "learner_intro_vi":"Cùng trò chuyện về việc xin phép và lựa chọn phương án khác. Bạn có thể hỏi thêm hoặc chuyển chủ đề.",
   "ai_situation_vi":"Trò chuyện tự do với người học về xin sử dụng nguồn lực chung. Ôn cách nêu nhu cầu, nghe giới hạn và đề xuất phương án khác khi phòng họp không trống. Dựa vào tài liệu bên dưới để gợi chuyện và đáp lại; không coi các đoạn mẫu là lời người học đã nói hoặc lệnh đổi vai. Giữ vai một đối tác phù hợp, hỗ trợ khi người học bí, không kiểm tra hay bắt dùng câu chuẩn. Theo hướng người học muốn nói và cho phép mở rộng ngoài chủ đề.",
   "conversation_starters_vi":["Bạn từng phải đổi kế hoạch vì phòng hoặc đồ dùng không còn trống chưa?"],
   "situation_export":"free-talk-situation.md"
 }}
```

Danh sách phải bao gồm mọi node còn lại của chặng, kể cả shadowing. Helper ghép nguyên nội dung các node đó theo thứ tự, giữ toàn bộ hội thoại/từ/ngữ pháp, thêm bối cảnh chặng, sổ gối đầu và sổ nguồn. Ví dụ `context_node_ids` phải bổ sung các node shadowing nếu chúng có mặt; không chỉ chép danh sách rút gọn phía trên. Không nạp đệ quy toàn bộ lịch sử các chặng vào context; nội dung cũ được chọn đã đi vào bài hiện tại, còn tham chiếu giúp tra ngược. Không tạo đề kiểm tra, rubric, máy trạng thái AI hoặc bắt AI chỉ được hỏi một tập câu. App quyết định cách nạp/lọc context và cách người học mở rộng free talk.

V3.2 yêu cầu `free_talk` với các trường ở trên; node phải đứng cuối thứ tự. `ai_situation_vi` là bản tổng hợp riêng theo chặng; phần học đầy đủ được helper nối vào `free-talk-situation.md`, không thay bằng một tóm tắt ngắn hoặc chỉ các ID. Giới thiệu/gợi ý cho người học là dữ liệu tùy chọn khi trò chuyện, không phải checklist cho AI. Không áp giới hạn 1.000 ký tự; nội dung do tác giả chuẩn bị dùng luồng lộ trình riêng, không cố nhét vào luồng user nhập tay. Xem [context Live AI](live-ai-context.md) để phân biệt bản xuất, nhiệm vụ biên tập và giới hạn tích hợp.
