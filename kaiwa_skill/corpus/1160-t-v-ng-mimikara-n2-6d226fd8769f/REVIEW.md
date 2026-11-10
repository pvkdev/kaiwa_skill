# Nghiệm thu production — ACCEPTED

- Ngày: 2026-11-10; coordinator `gpt-6-astra/high`, worker `gpt-6-sol/high` (`production_book_01`).
- Nguồn: `vocab/1160 TỪ VỰNG MIMIKARA N2.pdf` (tương đối từ `kaiwa_skill/`); SHA-256 `6d226fd8769f2e248518d8d32e542002738a13160e14a4ea90aaf102a67eab6d`.
- Phạm vi: đủ 8 trang vật lý. Worker mở và đối chiếu toàn bộ; coordinator ban đầu chọn p1, p3, p7, p8, sau đó mở rộng sang cả p2, p4, p5, p6 vì phát hiện vấn đề cấu trúc bảng và quan sát header chưa thống nhất.
- Quy tắc hiện tại: skill 0.2.1, commit `9e3d08c`. Thay đổi làm rõ kiểm header/footer và ranh giới bảng; CLI/schema không đổi.

## Đối chiếu và sửa lỗi xác nhận được

Coordinator đã mở ảnh cả tám trang và đọc đối chiếu toàn bộ Markdown: các cặp số–từ Nhật, bảng năm cặp cột, bảng cuối hai cặp cột, vị trí nhóm KATAKANA, chữ đậm ở mục 799, các từ xuống dòng và lời kết Nhật/Việt. Các ranh giới đáng ngờ được kiểm thêm bằng crop riêng từ cache nguồn.

- p2: dải MINATO giữa trang phải nằm sau hàng 170, trước 171; bản đầu chia sau 171.
- p4: dải giữa phải nằm sau 534, trước 535; bản đầu chia sau 532.
- p6: dải giữa phải nằm sau 901, trước 902; bản đầu chia sau 902.
- p7: chuyển cách trình bày theo cột sang hai bảng theo hàng, giữ dải giữa sau 1064/1101/1138/472/509 và nhóm KATAKANA ở cặp cột thứ tư.

Các trạng thái verified ban đầu đã không phát hiện những lỗi ranh giới này. Nội dung số–từ không đổi. Worker record và verify lại phần sửa; coordinator đọc lại bản cuối và xác nhận các ranh giới đúng. Không dùng trạng thái máy làm bằng chứng duy nhất về độ đúng.

## Nhận định đã rút về header

Quan sát ảnh toàn trang ban đầu khiến coordinator và worker nhận định một số trang thiếu khẩu hiệu/logo. Nhận định này đã được rút: crop riêng p4 từ chính cache cho thấy rõ cả khẩu hiệu và logo. Crop vùng khẩu hiệu `(100,70,1000,180)` trên ảnh 1224×1584 của cả tám trang có cùng SHA-256 pixel `0d58835c778c50b50c7c0d5193a4b1e14c35b5a5b6b68afcbd024e638739bf19`; worker còn kiểm crop 300 DPI trực tiếp từ PDF. Fresh render p4 ở cùng scale có hash bằng cache hiện hữu. Nguyên nhân quan sát ảnh toàn trang và crop không khớp chưa được xác định; không kết luận lỗi PDF hoặc lỗi công cụ.

Khẩu hiệu/logo thực có trên cả tám trang. Những chỉnh sửa nháp tạm bỏ header đã được khôi phục trước build cuối; không coi header ban đầu là lỗi thêm nội dung. Hash Markdown p1, p3, p5, p8 giữ nguyên so với bản bàn giao đầu. Evidence cuối ghi việc đối chứng và sửa thực tế; không che các lần nháp bị sửa sai.

## Chi tiết nguồn được bảo toàn

- p3 in số 459 rồi 511; nhóm 461–510 xuất hiện ở p7. Không chèn số 460 hoặc tự đánh số lại.
- p4 in `便` ở cả 592 và 593; p2 in `面倒さい` ở 235. Giữ đúng nguồn, không sửa theo từ chuẩn.
- p8 có ô đỏ `1161 パス`; tổng dữ liệu có 1160 mục đánh số 1–1161 trừ 460.
- Footer p8 là `今回こそ絶対合格してやるぜえええええええ`, có bảy chữ `え` sau `ぜ`; crop riêng đã được đọc. Giữ ba dòng chữ ký tiếng Việt/Latin.

## Quyết định và ràng buộc

Status cuối đọc lại: 8 verified / 8 trang, không issue/error, claim đã release, `build_current: true`. `book.md` và `search.jsonl` do CLI build từ tám trang đã xác nhận; đầu ra chỉ Markdown/JSON/JSONL, không ảnh. Coordinator chấp nhận phiên bản này; `acceptance.json` gắn quyết định với source/page/output hashes và SHA-256 của build marker. Build marker vẫn giữ trường máy `coordinator_review_required`; quyết định độc lập nằm trong báo cáo và acceptance, không sửa metadata để làm như công cụ tự nghiệm thu.

Đây là nghiệm thu toàn bộ một PDF, không phải toàn bộ kho. Rà soát bằng AI có thể bỏ sót; không suy ra tỷ lệ chính xác số học. Cache/crop chỉ phục vụ đọc, không nằm trong commit output.
