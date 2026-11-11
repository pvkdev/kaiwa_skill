# Rà toàn sách — 2026-11-11

## Phạm vi và nguồn

- PDF nguồn: 225 trang vật lý, SHA-256 `2ec8b7129cb8dff63a414edaef504898954b77762512c2eaa29bfea42e36ef2a`. Đã mở ảnh từng trang và có evidence `p0001.json` đến `p0225.json`; hash ảnh cache và PDF khớp toàn bộ.
- Chapterplan giữ nguyên 12 chương: front, 序章, tám chương nội dung, bảng 丁寧表現早見表, colophon. Không giảm scope để build.
- 223 trang `author_checked`, hai trang 178–179 `needs_review` cho cùng một mâu thuẫn biểu tượng vai nguồn ở Unit 1 Chương 6. Không có trang draft/pending. 11 chương checked, Chương 6 needs_review hẹp.

## Bảo toàn nội dung

- Kiểm 92 Unit thực in với 723 ý luyện có ô □ và 723 mẫu Nhật–Việt tương ứng; số lượng dựa trên item thực, không lấy nhan đề “700” làm số dòng. Giữ lượt khách, biến thể dấu `/`, gợi đầu câu, chú từ và mẹo phục vụ ở vị trí nguồn.
- Kiểm đầu/cuối mọi chương, trang ranh giới, bảng từ/câu cuối Chương 1–8 và bảng kính ngữ trang 219–223. Bảng cuối giữ 43 hàng 尊敬語, 28 hàng 謙譲語, các cặp cách nói khác, nhóm về người khác/bản thân và mọi tổ hợp お～/ご～ cùng ví dụ và nghĩa.
- Rà cặp đồng chữ khác cách đọc ở bảng cuối: 明日, 明後日, 昨日, 一昨日, 一昨年 và 私 đều giữ cách đọc của hai cột. Các cách đọc này là dữ kiện học; furigana phụ trợ bên trên ví dụ không đưa vào bản học.
- Kiểm hướng dẫn CD giữ trình tự English → khoảng dừng tự nói tiếng Nhật → giọng Nhật để đối chiếu. `_meta/audio.json` ghi 92 nhãn track thật in (CD-1 / 2–47, CD-2 / 1–46), mapping Unit/trang/block; không suy nội dung cho CD-1 / 1. Hai CD và tính năng tải âm thanh có bằng chứng bìa; URL/mã tải riêng không thấy ở cuối PDF; actual files `not_checked`.
- Rà các bất nhất đã xử lý: English “toilet” tại PDF98 trái với トレイ/torē và ngữ cảnh khay, danh sách アパレル①～③ ở PDF99 trái sáu Unit thực, tham chiếu “p.115” ở PDF131 không khớp vị trí bài được trỏ. Giữ vấn đề nguồn trong editorial log, không sửa Nhật in theo lớp English.

## Kiểm tra kỹ thuật

- `direct_progress.py build`: 12 chapters, 127 units, `status=full`, `completion_status=source_issues_unresolved`.
- `direct_progress.py validate --allow-source-issues`: 0 lỗi, 4 warning cùng một vấn đề PDF178–179 (hai page + hai unit references).
- Resume: không stale/rebase, không draft/pending; chỉ còn p178–179 và `chapters/07-ch6-sonota.md` ở `needs_review` do biểu tượng nguồn. Bản học ghi đúng câu Nhật và không gán lại vai theo suy đoán.
