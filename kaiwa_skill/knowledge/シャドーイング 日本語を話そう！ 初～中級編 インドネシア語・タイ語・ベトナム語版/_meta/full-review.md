# Rà soát toàn sách — 2026-11-11

## Phạm vi và nguồn

- PDF gốc: `kaiwa_skill/book/Shadowing/シャドウイング 日本語を話そう初_中級.pdf`, SHA256 `be075317cdcab1bad0245126bf7c4fe9bb066fcb714bc19aa841f5373b612869`.
- Đã mở ảnh từng trang vật lý PDF 1–145 và ghi `_meta/pdf-pages/p0001.json` đến `p0145.json`; raw corpus chưa đầy đủ chỉ dùng để tra chữ, không làm xuất xứ chính.
- 8 chapter theo bìa/lời đầu, hướng dẫn, Unit 1–5 và trang xuất bản; 66 unit. PDF140 trắng; PDF141–145 là quảng cáo nhà xuất bản, đã loại có lý do tại page evidence. Bản dịch Indonesia/Thái lặp với cột Nhật–Việt đã được ghi excluded theo block; phần riêng có nghĩa ở cột Nhật/Việt được giữ.

## Kiểm nội dung

- So cấu trúc toàn 42 Section (Unit 1–5): 411 hội thoại, 950 lượt Nhật và 950 lượt Việt tương ứng. Giữ các hội thoại cố ý lặp, nhãn F/C/D in trên từng mục, thứ tự lượt, mẫu rút gọn trong guide và các phần 解説/コラム cuối Unit.
- Đối chiếu phần giới thiệu và hướng dẫn với ảnh PDF7–23: bảng 5 Unit, chỉ dẫn người học/giáo viên, ví dụ rút gọn và mã CD. Các mẫu Nhật trong guide đã có nghĩa Việt.
- Rà trực tiếp cột Nhật–Việt, đặc biệt so sánh, phủ định, quyết định đã chốt, yêu cầu cắt tóc, thời hạn/số ngày và nghĩa theo ngữ cảnh. Những chỗ bản Việt in sẵn sai rõ đã chỉnh và ghi `_meta/editorial-log.md`; không sửa câu Nhật nguồn hay tự dựng lời thoại. Hai dòng Việt tiếp dòng không lặp nhãn trên PDF110/116 đã ghép đúng lượt.
- Các dấu 💡 解説 trên trang dịch được nối về đúng mục giải thích và trang in. Giữ 42 nhãn track CD 02–43, số 0 đầu, vị trí Section/trang, script Nhật và cột Việt; audio thực tế chưa kiểm (`not_checked`). Không suy số đĩa hoặc track 01.
- Đã rà trang xuất bản PDF139, tên/ấn bản/ISBN/tác giả/dịch giả; không lấy quảng cáo cuối PDF làm học liệu.

## Trạng thái bàn giao

- Mọi trang và 8 chapter có checkpoint `author_checked`; `resume` không còn pending, draft, stale hay needs_review.
- Các bất nhất bản in đã xử lý bằng biên tập tiếng Việt được liệt kê trong editorial log. Không còn nguồn mờ/cắt chữ chưa giải quyết được ghi nhận trong phạm vi này.
- Báo cáo này là lượt tự rà của người biên tập; root tiếp tục QA độc lập và Git/release.
