# Handoff — 02-yuukibui-3e66906b7e05

- Nguồn (tương đối từ `kaiwa_skill/`): `book/BJT/02.日本語でビジネス会話 中級編 ー練習冊 YUUKIBUI.pdf`
- SHA-256 nguồn: `3e66906b7e052b1394bb246542ce5087b15570da4dcf2425d037e4d198a2440b`
- Số trang PDF vật lý: **148**. Đầu ra text only.
- Worker đã làm: `production_book_14_sol`, token `production_book_14_sol_20261111_0c52` (đã release khi bàn giao).
- Trạng thái sau `reconcile` và `build`: **11 verified** (`p0001`–`p0011`), **1 rendered** (`p0012`), **136 pending** (`p0013`–`p0148`), không draft/needs_review/invalid/issue. `book.md` và `search.jsonl` là bản **partial**, `build.json` ghi `complete: false`.
- Điểm tiếp theo: **p0012**. Trang đã được render và mở toàn ảnh ở scale 2.5, nhưng **chưa** chép, crop hay review; worker kế tiếp phải tự mở lại ảnh, crop, chép và đối chiếu. Đây là trang in 5, mở đầu `第二課　わからない日本語を聞く`, có bài 1–2 và hai cột glossary. Sau đó tiếp tục p0013–p0148 theo thứ tự.

## Công việc đã kiểm

- `p0001` bìa, `p0002` trang tên sách, `p0003` copyright: đã mở ảnh full, crop watermark/logo/dấu thư viện/imprint. Watermark là **`JLPT Mogi Yuuki Bui`**; bản nháp ban đầu nhầm `Nogi`, đã sửa và reverify.
- `p0004` ghi chú `学習者へ`: bản nháp đầu chưa đủ ruby, đã quay lại đọc ba crop phóng lớn, bổ sung theo thứ tự từng lần xuất hiện và reverify. Root QA phát hiện thêm `口＝くち` tại `十分口ならし`; đã sửa, record lại, reverify. Hai đề mục có gạch chân được giữ bằng `<u>`; chữ thân bài không có bằng chứng đủ để thêm bold.
- `p0005` bản hướng dẫn tiếng Anh; `p0006`–`p0007` mục lục. Mục `第十五課　問い合わせ` ở p0007 **không có số trang riêng** trong nguồn, nhưng dòng `談話練習` phía dưới có trang 98.
- `p0008`–`p0011` là toàn bộ bài 1: các mẫu và câu trả lời **in sẵn** được chép, gạch chân nguồn giữ lại; các prompt bài tập chỉ chép dữ kiện, không tự giải. Mỗi trang đã mở full và crop riêng vùng bài 1/bài 2/glossary để kiểm số thứ tự, cặp vế, ruby và tiếng Anh. Ở p0009, `分＝ぷん` của `30分` và `10分` được xác nhận qua crop sát; `家＝うち` ở bài 4 dòng (6) cũng được crop kiểm lại.
- Mỗi trang verified có JSON evidence riêng gắn hash nguồn/render/Markdown và ghi vùng đối chiếu. Lần sửa cuối p0004 đã làm review cũ hết hiệu lực rồi verify lại. `build.json` sau build có `book_sha256: 1149603618147ea1bf2fdb7be96a091d11e03c7e0ee2f95adaf48eead880a05e`, `search_sha256: f87938ef5cff8aaf9699362a7fd24379674e43ebf85e4ffbb535f6e8f56b8ebb`.

## Tiếp quản

1. Đọc `AGENTS.md`, `.agents/skills/kaiwa-pdf-markdown/SKILL.md`, core docs và CLI help như quy định.
2. Kiểm claim đã rỗng; chạy `status`/`reconcile` với đúng book ID. Nếu p0012 còn rendered, claim token mới và tiếp p0012; không coi ảnh đã mở bởi worker trước là evidence của mình.
3. Render/crop từng trang, ghi qua `record`, verify bằng evidence thật. Giữ chú âm đúng span/lần xuất hiện; glossary cuối trang luôn kiểm đủ hai cột, dấu sao chú thích literal nếu gặp phải escape `\*`.
4. Checkpoint từng trang. Khi nghỉ, `reconcile`, `build`, cập nhật handoff và release; chỉ root dùng Git và sửa audit/roster.

Cache ảnh tạm ở `kaiwa_skill/.cache/renders/02-yuukibui-3e66906b7e05/`, không thuộc output hay commit. Không có vấn đề đọc nguồn chưa giải quyết trong p0001–p0011.
