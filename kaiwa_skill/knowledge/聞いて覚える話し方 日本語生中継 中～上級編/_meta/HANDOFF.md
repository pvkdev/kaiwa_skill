# Handoff — 日本語生中継 中～上級編

## Đã làm

- Scope full PDF vật lý 1–89, 11 chương cố định trong book.json. Không rút scope để build.
- Snapshot nguồn hoàn tất trong `kaiwa_skill/source_snapshots/namachuukei-chuujoukyuu-f08dd9302ee6/ecd29c28d4eb0df1/8e433a00`; đường dẫn file bên trong snapshot giữ nguyên repo-relative path gốc.
- Đã mở ảnh, đối chiếu raw và clean PDF 1–3 vào `chapters/00-bia-muc-luc.md` (2 unit), PDF 4–8 vào `chapters/01-huong-dan-su-dung.md` (7 unit). Cả hai chapter đã checkpoint `author_checked`; chưa review độc lập.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 9–18 vào `chapters/02-bai-1-dengon.md`. Toàn bộ 13 unit/10 trang của Bài 1 đã được tác giả rà lại và checkpoint `author_checked`; chưa có review độc lập.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 19–28 vào `chapters/03-bai-2-kanyuu.md`. Toàn bộ 14 unit/10 trang của Bài 2 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai2.md` để kiểm kê.
- Đã mở ảnh, đối chiếu raw và clean đủ PDF 29–38 vào `chapters/04-bai-3-kyoka.md`. Toàn bộ 14 unit/10 trang của Bài 3 đã được tác giả rà lại và checkpoint `author_checked`; xem `_meta/author-review-bai3.md` để kiểm kê.
- `_meta/units.jsonl`, `_meta/page-coverage.json`, `_meta/editorial-log.md` đã lưu provenance, hashes ảnh/raw và vấn đề nguồn.
- Chưa chạy builder toàn sách vì 6 trong 11 chương còn thiếu.

## Bước tiếp theo

1. Chạy `clean_progress.py resume` và kiểm snapshot/ledger trước khi sửa chương.
2. Tiếp tục **Bài 4 từ PDF 39**, rồi lần lượt các bài 5–8 và hậu ký theo chapter plan, cập nhật coverage từng trang, không thay scope.

## Vấn đề cần giữ

- PDF 9 in ①～⑥ nhưng chỉ có năm lời nhắn và năm dòng trả lời; clean dùng năm và có log giải thích.
- PDF 12 không in track riêng cho 問い4 tại bảng 問題3; không tự suy.
- Không có audio transcript hoặc đáp án bài nghe trong phạm vi đã clean; không tự tạo.
