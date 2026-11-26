# Kế hoạch Minna 50 bài

Ngày 2026-11-25 đã lưu snapshot ngữ pháp của 50 bài và dựng danh mục 318 mục theo VNJPClub. Bài 39 có snapshot của cả bảy phần và gói ngữ pháp/thực hành revision 3. Dùng [quy trình crawl](CRAWL.md) để kiểm lại độ phủ từng phần, đáp án và tài liệu Harumii.

Gói bàn giao, số câu đã soạn, kiểm tra trên frontend và các phần còn chờ được ghi trong [biên bản chất lượng toàn khóa](../reports/minna-quality-review.md).

## Quyết định tổ chức

Tính từ gốc repo Git, thư mục biên soạn là `kaiwa_skill/minna-n5-n4/`. Các đường dẫn bên dưới tính từ thư mục biên soạn này.

Điểm vào của repo là `.agents/skills/minna-n5-n4/SKILL.md`. Quy trình và dữ liệu biên soạn nằm trong workspace Minna.

Các file đã tạo:

- `SKILL.md`: hướng dẫn thực thi.
- `references/`: nguồn đã khảo sát, kế hoạch, contract biên tập và đối chiếu app.
- `catalog/sources.json`: 50 bài × 8 trang ứng viên = 400 URL, không bao gồm trang từ vựng.
- `pilot/lesson-39.plan.json`: phạm vi, số lượng quan sát và mapping B dự kiến.
- `authored/lesson-39/grammar-practice.json` chứa 6 bài giảng và 34 câu ở trạng thái draft. `contracts/harumii-minna/v1/` chứa hợp đồng, JSON Schema. `scripts/` chứa công cụ khảo sát và đóng gói.
- `reports/`: kết quả chạy probe, không chứa toàn bộ nội dung bài học.

Tạo các thư mục sau khi bắt đầu biên soạn, không tạo trước các lesson rỗng:

```text
sources/lesson-39/       snapshot nguồn được phép sử dụng, hash, metadata
normalized/lesson-39/    dữ liệu parse trung lập, không sửa tay
authored/lesson-39/      bản biên soạn, mapping, exercise chuyển thể
media/                  manifest + file được lưu trữ phù hợp; tránh commit binary lớn
exports/harumii/         gói ZIP theo bài, phạm vi và revision để preview hoặc nhập
```

## Lộ trình học đề xuất

1. Video vocab nhóm 1 → node vocab nhóm 1 → video vocab nhóm 2 → node vocab nhóm 2… Chia nhóm 20–30 từ khi binding vocab thật, không tạo list từ mới từ VNJPCLUB.
2. Mỗi mẫu có một video độc lập, bài giảng chữ và ví dụ. Cấp ID video ngay lúc biên soạn và gắn URL khi quay xong.
3. Ngữ pháp 1 → B liên quan → ngữ pháp 2 → B liên quan… B dùng nhiều mẫu nằm sau khi đã giới thiệu đủ các mẫu ấy. Đây là thứ tự khuyến nghị, chưa thiết kế khóa tiến độ.
4. Shadowing Văn mẫu và A; có thể tách thành nhiều node để học vừa sức, không làm mất cấu trúc bảng/thay thế của A.
5. Luyện nghe tùy chọn.
6. Đọc ngắn và đọc dài, mỗi phần là một node tùy chọn.
7. Video hướng dẫn hội thoại → C1 → C2 → C3… → Kaiwa tổng hợp.
8. Kiểm tra cuối bài: các nhóm Mondai 1–6.

Ở bài 39 có sáu cặp video → thực hành. B5, B6, B7 và B8 cùng nằm sau video ので. Khi đến B8 người học đã biết Nで. Sau video 途中で có hai câu luyện thêm do AI soạn.

Node tắt được loại khỏi lộ trình đang hiển thị nhưng không xóa dataset/identity/progress. Không dùng node nghe/đọc đang tắt làm điều kiện bắt buộc để vào C, Kaiwa hay kiểm tra. Đề xuất mặc định tắt nghe/đọc trong chế độ gọn; giữ chúng trong chế độ đầy đủ.

## P0 — Discovery, hoàn thành một phần

- Đã trích 50 trang ngữ pháp từ hai mục lục VNJPClub. Sáu phần khác đã kiểm trên bài 39. Trạng thái từng trang nằm ở `reports/crawl-coverage.json`.
- Đã phân biệt trang hiện hành và link “bản cũ”. Không trộn hai phiên bản vào cùng lesson.
- Đã thấy HTTP shell, wrapper render JS, nội dung tải sau thao tác và audio theo đoạn.
- Đã xác minh đáp án, bản dịch và clip của 32/32 câu B, một lời giải quiz ngữ pháp và giải mã thử clip B1-1. Phần còn cần kiểm là đáp án Mondai, transcript nghe và mức phủ media của các phần còn lại.

## P1 — Pilot bài 39, checkpoint tiếp theo

1. Snapshot DOM trước và sau mở tab/nút nội dung, ghi fetch time, final URL, sha256 và phiên bản parser. Xác minh quy tắc truy cập/robots hiện hành khi thực hiện crawl tự động; dừng host khi bị chặn/rate limit. Lưu tình trạng quyền dùng lại media/content trong provenance phục vụ xuất bản.
2. Parse 6 ngữ pháp, 13 ví dụ có nút nghe và 32 item B. Gắn 6 câu kiểm tra nhanh vào ngữ pháp như nội dung bổ trợ riêng; không tính chúng vào B hay Mondai cuối bài.
3. Dùng biên bản reveal 32 câu B làm chuẩn. Kiểm thêm một câu Mondai và một mục nghe từ đúng trang, sau đó đối chiếu theo item ID. Mục thiếu lời giải nguồn có thể bổ sung lời giải biên tập với xuất xứ riêng.
4. Parse 3 câu Văn mẫu và 15 câu A (6/2/7 theo ba bảng). Loại 15 câu Ví dụ trong tab chung và 10 câu kiểm tra của trang này.
5. Parse C: 3 nhóm, 12 câu/nhóm; giữ ranh giới mẫu/biến thể và speaker, không nối thành hội thoại 36 câu. Kaiwa riêng gồm 12 câu theo phân đoạn nguồn; số câu không nhất thiết bằng số lượt nói.
6. Parse nghe: 4 nhóm/11 mục làm bài; ví dụ mẫu giữ riêng. Giữ transcript và bản dịch khi lấy được.
7. Bài đọc ngắn tại `#mx-p7`: 3 đoạn, 4 câu hỏi trực tiếp. Bài đọc dài: 11 đoạn, 9 câu hỏi; bỏ glossary và mở rộng.
8. Parse Mondai 1–6. Inventory hiện tại của bài 39 là 29 câu, lần lượt 5/5/5/5/5/4. Ghi nhận sai biệt nếu nguồn cập nhật.
9. Duyệt mapping B và chuyển thể nhóm ảnh; kiểm nguồn audio, độ dài, timestamp, Nhật–Việt.
10. Tạo lesson canonical và bản xem trước; chỉ khóa schema v1 sau khi pilot vượt kiểm tra nội dung.

Điều kiện hoàn thành P1: mỗi mục trong scope có dữ liệu hoặc lý do chưa lấy được; toàn bộ node bật được phải có nội dung đã duyệt; câu chấm tự động có đáp án hợp lệ; không có media/refs trỏ nhầm; mapping B có người duyệt. Pending không được biến thành “đầy đủ”.

## P2 — Kiểm tra tính khái quát

Thử bài 1, 2, 25, 26 và 50 trước khi chạy 1–50. Đó là lựa chọn kiểm tra ranh giới, không phải khẳng định chúng có cùng DOM với bài 39. Kiểm bảng A, tranh B, số người nói, trang không có bài đọc, link cũ/mới và chữ không có ruby.

Mỗi family có adapter riêng: grammar, reading/shadowing, conversation, listening, exercises-short-reading, topic25 và test. Nếu không nhận diện family/version, ghi `unsupported_layout`, không âm thầm áp regex bài 39.

## P3 — Crawl có thể chạy tiếp

- Discovery từ các link nguồn; URL sinh theo mẫu chỉ dùng làm ứng viên cần kiểm chứng.
- Một request đang chạy/host, khoảng nghỉ khởi điểm 2 giây; thực hiện giới hạn chặt hơn nếu nguồn yêu cầu. Không mở hàng trăm tab.
- GET idempotent có timeout, tối đa ba lần thử cho lỗi mạng/5xx; 429 tôn trọng Retry-After và tạm dừng host; 403/challenge/login không retry dồn dập.
- Ledger mỗi resource: URL, final URL, status, content type, attempts, timestamp UTC, sha256, parser version, error code.
- Cache snapshot và asset theo hash. Resume chỉ phần thiếu/hỏng/thay đổi; không lặp tải audio chung cho từng câu.
- Không lưu cookie/token/nonce vào gói xuất; không gọi API tạo TTS hàng loạt chỉ để “thu hoạch audio”.
- Lưu phần đã parse vào staging theo lesson rồi commit file atomically. Không sửa đè phần authored khi crawl lại.
- Báo coverage theo từng family/lesson và từng trường: text, translation, answer, explanation, media, alignment, review. Không dùng một cờ `done` cho tất cả.

## P4 — Biên soạn

Ưu tiên ngữ pháp/B → shadowing → C/Kaiwa → Mondai 1–6 → nghe/đọc. Acquisition có thể giữ cả scope, còn ưu tiên biên soạn tập trung phần chính.

B không ảnh: giữ bài sắp xếp có thẻ nhiễu, điền từ, đổi dạng hoặc chọn đáp án tùy mục tiêu. Không mặc định chuyển mọi câu thành MCQ. B có ảnh: mô tả thành tình huống chữ đủ dữ kiện, soạn phương án nhiễu và lời giải mới; người biên tập duyệt tính đúng/đơn nghĩa. Không dùng OCR để bịa dữ kiện không có trong tranh. Không chuyển thể được thì giữ `image_required` và không bật node ấy.

Mỗi phần AI soạn có `derived_from`, phiên bản prompt/model khi dùng, trạng thái review và đáp án riêng. Giữ nguyên bản nguồn để đối chiếu. Lời giải nguồn, lời giải AI và lời giải biên tập viên là ba nguồn xuất xứ khác nhau.

## P5 — Adapter và migration

Khóa contract sau pilot; viết adapter theo code Harumi hiện tại, preview diff/binding trước commit. Gói xuất có version, stable IDs, checksums và media manifest. Import từng lesson có transaction/idempotency, retry không nhân bản, rollback revision mà không xóa tiến độ. Chỉ triển khai các bước này trong task migration tiếp theo.

Không coi các JSON import JLPT hiện có hoặc contract Kaiwa curriculum trước đây là importer Minna đã sẵn sàng. Xem `HARUMII_MAPPING.md`.
