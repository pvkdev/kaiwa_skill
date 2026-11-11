# Kế hoạch skill fork kiến thức kaiwa

Ngày: 2026-11-11 (Asia/Tokyo). Phạm vi hiện tại: xây skill và chạy pilot để người dùng duyệt; chưa mở chạy toàn kho.

## Mục tiêu và ranh giới

Tạo tầng `kaiwa_skill/knowledge/` từ Markdown ingest đã có, đọc đối chiếu PDF gốc. Tầng này là bản biên soạn kiến thức tiếng Nhật với lời giải thích và bản dịch tiếng Việt, phục vụ tìm kiếm và xây lộ trình sau này. Đây không phải bản chép nguyên trang, cũng chưa phải chương trình học.

- PDF trong `book/`, `vocab/` và corpus ingest chỉ đọc. Các công việc ingest đang chạy tiếp tục độc lập.
- Tên thư mục lấy từ tên sách được đọc trên bìa/trang nhan đề, không lấy mã tải xuống hoặc tên file PDF. Lưu tên chính thức đầy đủ trong metadata; chỉ thay ký tự không hợp lệ với hệ điều hành khi cần và ghi lại cách thay.
- Giữ đầy đủ nội dung học và đặc trưng từng sách: kiến thức, ví dụ, hội thoại, bài tập, dữ kiện, đáp án nguồn, ghi chú, cột riêng, câu chuyện, văn hóa, phụ lục và quan hệ có ý nghĩa trong hình. Giữ thứ tự triển khai và chức năng bài tập. Chỉ gộp lớp dịch đa ngữ tương đương hoặc phần lặp do dàn trang đã xác nhận; không tóm tắt, tuyển chọn hay áp template bài học chung.
- Nội dung học chỉ dùng tiếng Nhật và tiếng Việt, ngoại trừ tên riêng/ký hiệu hoặc đối tượng ngôn ngữ thực sự đang được giảng. Bỏ ruby/furigana, romaji phụ trợ, bản dịch tiếng Trung và bản dịch ngoại ngữ dư. Giữ kanji Nhật.
- Dịch giải thích sang tiếng Việt; mỗi ví dụ và lượt thoại Nhật có bản dịch Việt tương ứng. Dùng tiếng Nhật để kiểm ý nghĩa; tiếng Anh là nguồn hỗ trợ, không mặc định đúng hơn bản Nhật.
- Loại header/footer, số trang và chỉ dẫn thuần dàn trang, mô tả tô màu, mô tả ảnh trang trí. Giữ tiêu đề học, tham chiếu bài tập, mã track cần cho thực hành và sự nhắc lại có chủ đích. Chuyển đủ dữ kiện học từ hình thành chữ, không làm mất đầu vào để giải bài.
- Không sáng tác ví dụ, đoán audio, tự thêm topic hoặc gán level. Phần chưa rõ đi vào hồ sơ cần kiểm tra, không lấp bằng suy đoán.

## Sản phẩm

Skill dùng trong repo: `.agents/skills/kaiwa-fork-knowledge/SKILL.md`; quy trình chi tiết/schema đặt ở references khi cần, checker read-only đặt trong scripts.

Mỗi sách có các file sau trong `kaiwa_skill/knowledge/<tên sách>/`:

- `chapters/*.md`: bản học sạch, chia theo cấu trúc sách, unit có ID ổn định.
- `book.md`: ghép đúng thứ tự từ chapters, không chỉnh riêng làm lệch chapter.
- `_meta/book.json`: tên sách, đường dẫn/hash nguồn, phạm vi pilot, danh sách chapters, trạng thái và hash sản phẩm.
- `_meta/units.jsonl`: nối từng unit với chương, trang PDF, trang raw và anchor nguồn; lưu tình trạng rà soát và vấn đề.
- `_meta/editorial-log.md`: quyết định giữ/bỏ/gộp, cách xử lý hình và sai khác phát hiện.
- `_meta/pilot-review.json`: đối chiếu thực tế của tác giả.
- `_meta/independent-review.md`: kiểm tra độc lập, phân biệt kiểm cấu trúc với kiểm nội dung và trang thực sự đã mở.

Đường dẫn nguồn trong `book.json` tính từ gốc repo. Đường dẫn chapter tính từ thư mục sách. Phạm vi partial/pilot nằm trong metadata và file hướng dẫn duyệt, không biến thành header lặp trong nội dung học.

## Pilot đã chọn

Sách: `わかる！話せる！日本語会話 基本文型88` — tên xác nhận trên bìa PDF1.

Nguồn: `kaiwa_skill/corpus/669041168-4f47df1cc97a/book.md` và `kaiwa_skill/book/Kaiwa/669041168-日本語会話-基本文型８８.pdf`.

1. `chapters/00-mo-dau.md`: chương mở đầu, năm mục kiến thức, PDF7–9, trang in 12–16; không lấy trang mở PART1 ở nửa phải PDF9.
2. `chapters/01-ne.md`: PART1 bài 1, `～ね`, PDF10, trang in 18–19.
3. `chapters/02-yo.md`: PART1 bài 2, `～よ`, PDF11, trang in 20–21.
4. `chapters/03-yone.md`: PART1 bài 3, `～よね`, PDF12, trang in 22–23; kiểm biên với PDF13 trước khi chốt.

Corpus hiện tự ghi INCOMPLETE, PDF28 cần review. Pilot không bao gồm trang đó; không tuyên bố sách đã hoàn tất.

## Điều phối đúng ba sub

1. **Skill author:** thiết kế và viết skill/schema. Không viết nội dung pilot hoặc dùng Git.
2. **Pilot author:** đọc PDF và raw; viết bốn chapter cùng provenance/hồ sơ biên tập. Một tác giả sở hữu phần fork của PDF này.
3. **Validator và QA:** viết checker; sau khi tác giả hoàn tất, dùng skill để kiểm tra độc lập nội dung và đối chiếu một phạm vi nguồn được ghi rõ. Báo lỗi cho tác giả sửa, không ghi đua chapter.

Root trực tiếp chốt hợp đồng, kiểm nguồn và bản dịch, ghép book/index, rà diff và commit local tách skill với output. Ba sub dùng `gpt-6-sol/high` theo AGENTS.md; không mở thêm sub. Root không thay model của phiên đang chạy.

## Tiêu chí nghiệm thu pilot

- Đã mở ảnh mọi trang PDF dùng để biên soạn; vùng chữ nhỏ/quan hệ mơ hồ được kiểm đủ rõ. Script không thay việc đọc trang.
- Không còn rác dàn trang, ruby, mô tả ảnh hoặc bản dịch ngoại ngữ dư trong chapters/book.
- Từng phần nguồn có vị trí tương ứng trong bản clean, gồm phần riêng của sách, bài tập, đáp án và ghi chú. Mạch bài và chức năng bài tập được giữ; việc gộp hoặc bỏ chỉ áp dụng phần rác/lớp dịch trùng và có căn cứ.
- Mỗi câu/lượt thoại Nhật có bản dịch Việt; bản dịch giữ tình thái, vai nói và ý nghĩa ngữ cảnh.
- Mỗi unit có nguồn kiểm tra được; mọi vấn đề chưa giải quyết được công bố.
- Checker qua các kiểm cấu trúc và kiểm âm tính có ý nghĩa. Kết quả checker không được gọi là chứng nhận ngữ nghĩa.
- PDF/raw không bị sửa; file ảnh/cache không nằm trong output hoặc commit.
- Người dùng nhận được bản gộp dễ đọc và các chapter để duyệt trước khi quyết định nhân rộng.

## Sau khi người dùng duyệt

Điều chỉnh quy tắc từ phản hồi pilot, rồi mới áp dụng theo từng sách. Mỗi sách mới xác nhận tên, phạm vi, nguồn và giữ checkpoint từng chương. Chỉ dùng các fork đã qua rà soát làm nền tổng hợp topic/tình huống và thiết kế lộ trình; vẫn liên kết được về corpus/PDF.
