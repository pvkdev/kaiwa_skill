# Handoff — 02-yuukibui-3e66906b7e05

- Nguồn (tương đối từ `kaiwa_skill/`): `book/BJT/02.日本語でビジネス会話 中級編 ー練習冊 YUUKIBUI.pdf`
- SHA-256 nguồn: `3e66906b7e052b1394bb246542ce5087b15570da4dcf2425d037e4d198a2440b`
- Số trang PDF vật lý: **148**. Đầu ra text only.
- Worker trước: `production_book_14_sol`, token `production_book_14_sol_20261111_0c52` (đã release).
- Worker lượt này: `production_book_14_root_cont2`, token `production_book_14_root_cont2_20261111_b45f` (đã release khi bàn giao).
- Sau `reconcile` và `build` lúc 2026-11-11 04:31 UTC: **23 verified** (`p0001`–`p0023`), **125 pending** (`p0024`–`p0148`), không rendered/draft/needs_review/invalid/issue. `book.md` và `search.jsonl` là bản **partial**; `build.json` ghi `complete: false`, `acceptance: coordinator_review_required`.
- Điểm tiếp theo: **p0024**. Trang này chưa render hay đọc ở lượt này; worker mới cần tự mở ảnh và crop để chép/đối chiếu.
- Build hiện tại: `book_sha256: 14c6cdf5c98ea192fabf1b2e9b81b6a6101bb573fd206f0d8ffc1a37bbbd9f6f`; `search_sha256: 95d27f1ec3cb5a094b23c9b46aac5de19c079988beaf4218ce4ff38aabe929cc`.

## Công việc đã kiểm

- `p0001`–`p0011` giữ nguyên hash và trạng thái verified của worker trước. `p0004` đã được root QA đóng sạch sau khi sửa đủ ruby và `口＝くち`; không làm lại. Ở `p0009`, `分＝ぷん` trong `30分`/`10分` và `家＝うち` đã được crop xác nhận trước đó.
- `p0012`–`p0023` mỗi trang đã mở ảnh full ở scale 2.5, crop từng vùng chữ nhỏ/glossary; chép vào Markdown và đọc lại ảnh → Markdown → ảnh. Mỗi trang có evidence JSON riêng trong hồ sơ corpus, gắn hash nguồn/render/Markdown và ghi vùng kiểm cụ thể. Từng trang đã checkpoint và verify bằng CLI; không có chỗ chưa rõ hoặc issue còn mở.
- `p0012`–`p0016`: hoàn tất 第二課 với bài 1–8, rồi hai trang 〈談話練習〉. Các mẫu đáp án in sẵn được giữ nguyên và gạch chân nguồn được mã hóa bằng `<u>`; prompt/ô trống chưa được giải. Bảng từ cuối trang đều kiểm hai cột. `p0015`–`p0016` giữ riêng vai A₁/B₁/A₂/B₂/A₃ và dữ kiện tương ứng.
- `p0017`–`p0023`: 第三課／依頼, bài 1–10 và hai trang 〈談話練習〉. Chú âm từng lần xuất hiện và đúng span được đối chiếu qua crop. `p0021` giữ cách viết nguồn `休けい` và `話し`. `p0023` crop riêng xác nhận `ピエール` có エ cỡ đầy đủ. Các chữ/vế trông không tự nhiên nhưng in như vậy trong nguồn được giữ nguyên; không tự sửa.
- Các trang có watermark `JLPT Mogi Yuuki Bui`, header/footer/trang in được kiểm riêng. Ảnh/crop chỉ ở `.cache/renders/02-yuukibui-3e66906b7e05/`, không thuộc output.

## Tiếp quản

1. Đọc `AGENTS.md`, `.agents/skills/kaiwa-pdf-markdown/SKILL.md`, core docs và CLI help. Kiểm claim rỗng; chạy `status`/`reconcile` đúng book ID và đối chiếu trạng thái 23 verified, 125 pending, 0 issue.
2. Claim bằng owner/token mới rồi bắt đầu **p0024**, không coi crop/lượt đọc trước là evidence của mình. Render full và crop vùng có ruby, bài tập, hội thoại, glossary, header/footer, hình mang nghĩa. Chuyển dữ kiện hình thành text có nhãn `(biên tập)`.
3. Ghi qua `record`, đọc ngược bản ghi với ảnh, lấy `evidence-template`, điền review thật và `verify` từng trang. Chữ mờ thật: giữ phần đọc được, issue localized và `needs_review`; không ép verified. Giữ dấu sao literal bằng `\*` nếu gặp.
4. Khi nghỉ: `reconcile`, `build`, cập nhật handoff, release claim; chỉ root dùng Git và sửa audit/roster.

Không có vấn đề đọc nguồn chưa giải quyết trong `p0001`–`p0023`.
