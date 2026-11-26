---
name: minna-n5-n4
description: Khảo sát nguồn VNJPCLUB, biên soạn dữ liệu Minna no Nihongo 50 bài N5–N4 trong kaiwa_skill và chuẩn bị gói migration sang Harumii. Dùng khi làm nguồn, ngữ pháp, Renshuu B, shadowing Văn mẫu/A, Renshuu C/Kaiwa hoặc contract dữ liệu Minna.
---

# Minna N5–N4: biên soạn trước, migration sau

Thư mục này là workspace biên tập được người dùng chỉ định. Tất cả dữ liệu Minna mới đặt ở đây; không sửa kho sách, vocab hoặc bunpou_skill. Chưa triển khai importer hay thay đổi app Harumi trong giai đoạn khảo sát.

## Bắt đầu

Nguồn quyết định mẫu và thứ tự trong từng bài là trang **ngữ pháp VNJPClub**. Tra [danh mục đã trích từ 50 trang](catalog/grammar-points.json) theo số bài rồi theo ID mục trong trang. Giữ cả các cách dùng cùng dạng bề mặt. Dữ liệu ngữ pháp Harumii dùng để đối chiếu nghĩa và ghép ID. Một bài giảng Harumii có thể dùng làm tài liệu cho nhiều node. Danh sách từ của từng bài lấy từ bản xuất Harumii.

Khi crawl hoặc cập nhật một bài, làm theo [quy trình chạy và kiểm độ phủ](references/CRAWL.md). Khi gặp bài giảng Harumii cần nâng cấp, dùng [skill biên tập ngữ pháp Harumii](../../.agents/skills/harumii-grammar-edit/SKILL.md) để chuẩn bị gói Markdown cho admin ngay trong đợt biên tập.

1. Đọc [kế hoạch triển khai](references/PLAN.md) để biết phạm vi và checkpoint.
2. Khi khảo sát/crawl, đọc [bằng chứng bài 39](references/SOURCE_AUDIT_39.md). Các selector và số lượng là quan sát của bài 39, không phải quy luật cho 50 bài.
3. Khi chuẩn hóa, đọc [hợp đồng biên tập dự thảo](references/DATA_CONTRACT.md).
4. Khi xuất sang app, đọc [đối chiếu Harumi](references/HARUMII_MAPPING.md), rồi xác minh lại code đích. Đây chưa phải wire contract được Harumii hỗ trợ.

## Phạm vi cố định từ yêu cầu

- Dùng danh sách từ vựng người biên soạn cung cấp để chọn từ khi viết bài tập. Các node học từ vựng tham chiếu dữ liệu hiện có trong Harumii và chia nhóm khoảng 20–30 từ. Bước crawl VNJPCLUB bỏ qua trang từ vựng.
- Lấy ngữ pháp, ví dụ Nhật–Việt, media, đáp án/lời giải nếu nguồn cung cấp; Renshuu B là ưu tiên cao nhất.
- Shadowing từ `luyen-doc`: chỉ Văn mẫu (`bunkei`) và luyện tập A. Không tự lấy thêm Ví dụ (`reibun`) hoặc tab kiểm tra.
- Hội thoại: giữ nhóm C, mẫu và biến thể; xếp C trước Kaiwa tổng hợp dù trang nguồn hiển thị Kaiwa trước.
- Nghe và đọc vẫn nằm trong dataset. Đề xuất node tùy chọn, mặc định tắt ở bản học gọn; đây là lựa chọn sản phẩm có thể đổi.
- `bai-tap`: chỉ bài đọc ngắn và câu hỏi gắn trực tiếp với bài đọc. `25-bai-doc-hieu`: bài đọc dài, dịch và câu hỏi trực tiếp; bỏ tab từ vựng và mở rộng.
- `kiem-tra`: chỉ **Mondai 1–6** theo số đề mục, không phải sáu khối kỹ năng của giao diện.
- Mỗi mẫu có một video riêng, bài giảng chữ và ví dụ trên cùng node. Ngay sau đó là một node thực hành tập hợp các nhóm B tương ứng. Nhóm cần hai mẫu được đặt khi cả hai đã học. Mẫu thiếu B được bổ sung bài AI mang nhãn luyện thêm.

## Quy trình

1. Discovery: dùng trang gốc từng bài để lấy link thật. `catalog/sources.json` chỉ chứa URL ứng viên chưa xác minh. Ghi nhận thiếu trang, chuyển hướng, phiên bản giao diện và phần nằm ngoài phạm vi.
2. Acquisition: HTTP trước; nếu chỉ có shell hoặc wrapper cần JS, dùng DOM sau khi trình duyệt render bình thường. Không coi HTTP 200 là hoàn tất. Trang xác minh/đăng nhập/lỗi được ghi trạng thái, không lách hạn chế hay đoán endpoint riêng.
3. Extraction: giữ section/group/item ID, thứ tự, câu Nhật/Việt, ruby và quan hệ audio. Đáp án rỗng sau render là `pending`, không phải `absent`.
4. Reveal: dùng nút hiện đáp án/script của nguồn hoặc cơ chế công khai đã xác minh tương đương. Không chấm thử mọi phương án để suy đoán đáp án. Gắn đáp án theo item ID, không theo vị trí trả về.
5. Normalization: tách dữ liệu nguồn khỏi nội dung biên soạn/AI. Không tự bịa đáp án, timestamp, bản dịch hoặc lời giải rồi ghi là dữ liệu nguồn.
6. Authoring: ánh xạ B tới một hoặc nhiều ngữ pháp; người biên tập duyệt. Nhóm dùng nhiều mẫu được đặt sau mẫu cuối cần dùng. Không ép mỗi mẫu có đúng một nhóm B.
7. Validation: kiểm độ đầy đủ theo mục đã chọn, ghép Nhật–Việt, đáp án, ảnh, media và refs. Bài có ảnh không chuyển sang bài chữ nếu mất dữ kiện quyết định đáp án.
8. Export: xuất snapshot/revision riêng; preview diff và binding trước migration. Import không ghi đè tiến độ, video, media hay sửa tay của admin.

## Biên soạn và đóng gói

Ở trang sửa giáo trình từ vựng và ngữ pháp, chọn một trong năm template đã kiểm trong `CURRICULUM_MANUAL_TEMPLATE_PICKER` của Harumii. Dùng `manualQnA` cho một lựa chọn đúng; `manualFillInBlank` khi mục tiêu là tự chia dạng/điền trợ từ; `manualMultiSelect` khi người học cần nhận ra **tất cả** phát biểu đúng. Với `jlptReading`, mỗi đáp án phải suy được từ đoạn đọc. Với `jlptListening`, người học phải nghe được đúng audio chứa dữ kiện quyết định, giữ script cho phần đối chiếu sau khi làm. Chọn template theo thao tác cần luyện, không áp chỉ tiêu chia đều.

AI tự làm từng câu trước khi đánh dấu đáp án. Ghi ID đáp án đúng, toàn bộ tập ID đối với chọn nhiều, hoặc đáp án chấp nhận được theo từng ô. Viết lời giải tiếng Việt nêu dấu hiệu trong câu, bài đọc hay lượt thoại và vì sao lựa chọn dễ nhầm sai. Phân biệt đáp án chính thức đã reveal với đáp án AI của biến thể; lưu nguồn và mục tiêu ngữ pháp theo từng câu. Khi đổi thứ tự đáp án, tính lại chỉ số từ ID. Kiểm cả dữ liệu qua bộ nhập của editor, bộ lưu và bộ đọc của learner. Chọn JSON khi cần mang lời giải vào app; cột `correct` trong CSV dùng chỉ số từ 1 và mẫu CSV hiện tại không có cột lời giải.

Đồng thời rà **chính bài giảng N5–N4 đang có** được dùng làm tham chiếu. Khi có cách giảng mơ hồ, ví dụ sai, bản dịch lệch hoặc Markdown cũ, soạn bản nâng cấp cho cùng UUID theo [hợp đồng của admin](materials/grammar/HUONG-DAN-AI.md). Bảo toàn các cách dùng đúng và nội dung liên quan ngoài bài Minna đang luyện; bàn giao ZIP và diff ở bước duyệt.

Trước khi **viết mới hoặc sửa bài tập** của bài NN, đọc [danh sách từ vựng](materials/vocabulary/README.md) của đúng bài và tra [Markdown ngữ pháp](materials/grammar/README.md) theo mẫu đang luyện. Tìm file theo số bài hoặc đọc mục “Bài NN” trong tài liệu gộp. Danh sách chung N5/N4 chỉ giúp ước lượng độ khó. Chỉ coi một từ là từ của bài khi tài liệu có ghi bài tương ứng.

Ưu tiên từ của bài trong tình huống, câu hỏi và cả phương án nhiễu. Có thể dùng lại từ đã học ở các bài trước để câu tự nhiên. Nhận diện cả dạng chia và cách viết kana/kanji của cùng một từ. Với từ ngoài danh sách khiến người học khó trả lời, thay bằng từ quen hoặc thêm nghĩa ngắn nếu cần giữ tình huống. Khi rà lại, thử làm câu chỉ với vốn từ đã học và mẫu vừa dạy, rồi kiểm tra đáp án còn duy nhất sau khi thay từ. Với câu chuyển thể, sửa trên bản biên soạn để giữ được câu nguồn và liên kết audio gốc.

Mở [báo cáo đối chiếu từ của 50 bài](reports/vocabulary-review.json) hoặc chạy `py -X utf8 scripts/vocabulary_review.py --lesson 39` với SudachiPy 0.6.10 và SudachiDict-small 20250129. Báo cáo chỉ tới dòng trong bảng từ và ID câu có dùng từ dạy ở bài sau. Kiểm nghĩa trong ngữ cảnh trước khi chỉnh, đặc biệt với từ đồng âm, tên riêng và cách nói cố định. Chạy lại lệnh bỏ `--lesson` sau khi biên soạn để cập nhật báo cáo toàn khóa.

Nếu chưa có tài liệu theo bài, vẫn có thể soạn nháp từ ngữ cảnh nguồn. Khi bàn giao, ghi rõ bài nào còn chờ đối chiếu từ vựng hoặc ngữ pháp. Khi người dùng bổ sung tài liệu, đọc lại tài liệu trước khi chỉnh bản nháp.

Khi gặp ảnh bắt buộc, lời giải thiếu, câu mơ hồ hoặc kiểu tương tác Harumii chưa đọc được, tạo ngay biến thể có thể làm độc lập. Ghi `source_item_id`, kiểu chuyển thể, đáp án và lời giải tiếng Việt. Với mục bị thiếu dữ kiện, soạn tình huống tương đương và đánh dấu bài mới. Thu âm mới khi câu Nhật đã đổi. Bài nguồn phù hợp với renderer có thể dùng nguyên bản kèm lời giải AI ở trường riêng. [Hợp đồng migration và cách đóng gói](contracts/harumii-minna/v1/CONTRACT.md).

## Công cụ hiện có

Để tạo lại [thứ tự video và bài luyện cho 50 bài](catalog/grammar-practice-order.json), chạy các lệnh dưới đây sau khi có snapshot ngữ pháp. Bước chuẩn hóa dùng `beautifulsoup4`. Mỗi mục nguồn giữ ngữ pháp, ví dụ, tham chiếu media và câu hỏi gốc. Khi nguồn thay đổi, so lại câu hỏi và lựa chọn trước khi cập nhật `authored/quick-checks/source-revisions.json`.

```powershell
py -X utf8 scripts/normalize_grammar.py
py -X utf8 scripts/normalize_speaking_reading.py
py -X utf8 scripts/quick_checks.py
py -X utf8 scripts/renshuu_author.py
py -X utf8 scripts/renshuu_drill_round2.py
py -X utf8 scripts/grammar_practice_order.py
```

Đọc [cách xuất sang năm template và giới hạn của editor](references/TEMPLATES.md) trước khi chuyển bài tập cho Harumii. Dùng [bộ câu có đáp án và lời giải](authored/quick-checks) theo ID câu và [bộ Renshuu B](authored/renshuu) theo ID nhóm. Mỗi video có ID riêng. Thứ tự của bài dùng mẫu đã dạy muộn nhất trong nhóm B. Với bài 39, gói pilot có thêm chín nhóm thực hành.

Khi nguồn đổi thứ tự điểm ngữ pháp, tra [sổ ID video](catalog/grammar-video-ids.json) để giữ nguyên liên kết với media và tiến độ. Khi nguồn thêm một điểm thực sự mới, cấp số video chưa dùng của bài. Khi nguồn đổi ID cho cùng một điểm, đối chiếu nội dung và chuyển khóa nguồn sang ID video đã có. Giữ số video đã nghỉ để tránh dùng lại.

Chạy `pwsh -NoProfile -File scripts/build_exercise_release.ps1` để xuất toàn bộ câu đã biên tập, kiểm đáp án và đóng gói `exports/harumii/minna-50-exercises-preview.zip`. ZIP chứa 50 bài theo đúng thứ tự, dữ liệu bài tập native, manifest checksum và bản nghe mẫu cục bộ. Gói Markdown cho admin ngữ pháp dùng quy trình riêng theo hợp đồng bài giảng.

Xem [biên bản bàn giao](reports/minna-quality-review.md) để lấy đúng ZIP ngữ pháp dùng cho admin, ZIP lộ trình dùng để preview và danh sách dữ liệu nguồn còn thiếu.

Chạy từ thư mục skill:

```powershell
py scripts/build_catalog.py
pwsh -NoProfile -File scripts/probe_source.ps1 -Lesson 39
pwsh -NoProfile -File scripts/audit_b39.ps1
py -X utf8 scripts/harumii_package.py build authored/lesson-39/grammar-practice.json
py -X utf8 scripts/harumii_package.py verify exports/harumii/lesson-39/grammar_practice/r0003.zip
```

- `build_catalog.py`: tạo/cập nhật metadata ứng viên cho 50 bài; giữ nguyên trạng thái đã ghi trong catalog, không truy cập mạng.
- `probe_source.ps1` dùng PowerShell 7 để khảo sát tối đa 8 URL/bài. Biên bản trong `reports/` phân biệt yêu cầu render, xác minh truy cập và lỗi HTTP. Script dừng khi host yêu cầu xác minh hoặc giới hạn tần suất.
- `audit_b39.ps1` dùng chức năng hiện đáp án của trang ngữ pháp cho 32 ID đã quan sát. [Kết quả chạy và ví dụ câu B1-1](reports/lesson-39-renshuu-b.json).
- `pilot/lesson-39.plan.json`: bản kế hoạch dựa trên quan sát, **không phải một bài đã biên soạn xong**.
- [Bản biên soạn bài 39](authored/lesson-39/grammar-practice.json) chứa sáu cặp node video và thực hành. Hai lệnh Python cuối đóng gói và kiểm lại bản biên soạn, cần thư viện `jsonschema` 4.x.

Khi báo cáo, phân biệt: link dự kiến / đã thấy trên nguồn / đã tải / đã parse / đã duyệt / đã xuất / đã import. Không gọi manifest 50 bài là “đã crawl 50 bài”.
