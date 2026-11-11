# Handoff — 日本語生中継 中～上級編

## Đã làm

- Scope full PDF vật lý 1–89, 11 chương cố định trong book.json. Không rút scope để build.
- Snapshot nguồn hoàn tất trong `kaiwa_skill/source_snapshots/namachuukei-chuujoukyuu-f08dd9302ee6/ecd29c28d4eb0df1/8e433a00`; đường dẫn file bên trong snapshot giữ nguyên repo-relative path gốc.
- Đã mở ảnh, đối chiếu raw và clean PDF 1–3 vào `chapters/00-bia-muc-luc.md` (2 unit), PDF 4–8 vào `chapters/01-huong-dan-su-dung.md` (7 unit). Cả hai chapter đã checkpoint `author_checked`; chưa review độc lập.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 9–18 vào `chapters/02-bai-1-dengon.md`. Toàn bộ 13 unit/10 trang của Bài 1 đã được tác giả rà lại và checkpoint `author_checked`; chưa có review độc lập.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 19–28 vào `chapters/03-bai-2-kanyuu.md`. Toàn bộ 14 unit/10 trang của Bài 2 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai2.md` để kiểm kê.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 29–38 vào `chapters/04-bai-3-kyoka.md`. Toàn bộ 14 unit/10 trang của Bài 3 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai3.md` để kiểm kê.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 39–48 vào `chapters/05-bai-4-jouhou.md`. Toàn bộ 14 unit/10 trang của Bài 4 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai4.md` để kiểm kê.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 49–58 vào `chapters/06-bai-5-irai-shiji.md`. Toàn bộ 15 unit/10 trang của Bài 5 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai5.md` để kiểm kê.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 59–68 vào `chapters/07-bai-6-monku.md`. Toàn bộ 13 unit/10 trang của Bài 6 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai6.md` để kiểm kê.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 69–78 vào `chapters/08-bai-7-teian.md`. Toàn bộ 12 unit/10 trang của Bài 7 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai7.md` để kiểm kê.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 79–87 vào `chapters/09-bai-8-kansou.md`. Toàn bộ 13 unit/9 trang của Bài 8 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai8.md` để kiểm kê.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 88–89 vào `chapters/10-atogaki.md`. Toàn bộ 5 unit/2 trang hậu ký đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-atogaki.md` để kiểm kê.
- `_meta/units.jsonl`, `_meta/page-coverage.json`, `_meta/editorial-log.md` đã lưu provenance, hashes ảnh/raw và vấn đề nguồn.
- Toàn bộ 11 chương/89 trang đã clean và checkpoint `author_checked`; chờ root QA/build.
- Tự kiểm toàn sách: 122 unit có anchor và thứ tự khớp chapter; mọi raw anchor nội dung PDF1–89 gắn đúng một lần (thiếu 0, lặp 0, sai 0); 11 dải trang khớp chapter plan; 89 raw hash và 89 ảnh hash đúng; `clean_progress.py resume` không có draft/pending/stale/needs_rebase/snapshot error và scope không đổi. `validate_fork.py` hiện chỉ báo thiếu `book.md` và build hashes vì root chưa build, không báo lỗi nội dung chapter/metadata.

## Bước tiếp theo

1. Root chạy kiểm tra cấu trúc, provenance và review độc lập theo hồ sơ từng chương.
2. Khi QA đạt, root chạy builder toàn sách theo scope 89 trang đã khóa.

## Vấn đề cần giữ

- PDF 9 in ①～⑥ nhưng chỉ có năm lời nhắn và năm dòng trả lời; clean dùng năm và có log giải thích.
- PDF 12 không in track riêng cho 問い4 tại bảng 問題3; không tự suy.
- Không có audio transcript hoặc đáp án bài nghe trong phạm vi đã clean; không tự tạo.
