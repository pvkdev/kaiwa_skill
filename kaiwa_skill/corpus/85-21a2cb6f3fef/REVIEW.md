# Nghiệm thu 外国人のための日本語敬語の使い方 基本表現85

**ACCEPTED** — 2026-11-10T17:00:22.066778+00:00. Reviewer: gpt-6-astra/high, coordinator `/root/production_resume`. Skill 0.2.3.

Nguồn: `book/Kaiwa/外国人のための日本語敬語の使い方-基本表現85.pdf` (tương đối từ kaiwa_skill/), SHA-256 `21a2cb6f3fefc783cec4267c8ee2e4fec1391c13f4fc28e5435b7f99b09170c6`, 93 trang PDF. Các đường dẫn bằng chứng bên dưới tương đối từ corpus này.

## Phạm vi và bằng chứng

Worker Sol/high mở ảnh từng trang, đối chiếu hai chiều và lưu93 checkpoint verified. Coordinator đã độc lập mở ảnh nguồn và đọc toàn bộ Markdown **93/93 trang vật lý**, mở crop cho chữ nhỏ, ruby, dấu gạch, romaji, bảng và minh họa có nghĩa. Bao phủ bìa/trang trắng, lời đầu/mục lục/hướng dẫn, mọi thẻ ngữ pháp/đầu cuối unit, hội thoại song ngữ và romaji, bài tập/đáp án, bảng biến đổi/tra cứu, chỉ mục và colophon. Hash từng trang/ảnh và phạm vi cụ thể trong `COORDINATOR_AUDIT.json`; không còn hash QA cũ hoặc finding chưa xử lý. `WORKER_REVIEW.md` ghi phương pháp và lượt sửa của worker.

Status độc lập cuối:93verified,0issue,build_current=true,claim=null. Nguồn được hash lại; mọi Markdown khớp checkpoint, build và QA ledger. Sản phẩm text-only `book.md`/`search.jsonl` khớp marker hiện hành. Không coi validator/hash là bằng chứng thay việc đọc ảnh.

## Sửa đổi và mở rộng kiểm tra

Sau lỗi ruby occurrence/span tái diễn, đã mở rộng đến toàn bộ sách: bỏ ruby tự thêm, giữ lần có in, tách span xuống dòng; sửa kana nhỏ/âm cuối như分＝ぷん,話＝はなし và２人＝ふたり. Kiểm riêng header/nhãn, mọi công thức và các dấu gạch xóa ます/する/ない/た; ghi rõ nhãn biên tập. So từng dòng romaji/Anh, giữ cách viết bất thường nguồn và phục hồi chữ hoa, macron, khoảng trắng cùng dấu nối cuối dòng. P91 giữ vị trí nhãn cột lệch nghĩa theo bản in. P92 kiểm mọi mục/số trang/ruby của bốn cột. P93 phục hồi 『』ngoài nhan đề, 「」bên trong và dấu gạch dài. Mỗi sửa đổi record/reverify/rebuild và coordinator đọc lại. Các false positive bị crop bác bỏ được giữ trong lịch sử, không sửa nguồn đúng để phù hợp suy đoán.

## Giới hạn nguồn và quyết định

**PDF được cung cấp thiếu trang in106–107**: hai trang vật lý liên tiếp54→55 hiển thị104–105/item13/audio58 rồi108–109/item15/audio60. Chỉ mục p92 vẫn dẫn mục存じる（思う）đến106. Đã giữ đúng những gì nguồn chứa, không dựng lại item14. P87 bên phải là divider không in số trang giữa172 và174. Nghiệm thu93/93 ở đây là toàn bộ **trang vật lý hiện có**, không chứng nhận PDF đủ mọi trang của ấn bản giấy.

Không còn sai khác đã biết sau lượt độc lập toàn93trang; vẫn không cam kết tuyệt đối không có lỗi đọc/chép ẩn. Chấp nhận build hiện tại; `acceptance.json` ràng buộc nguồn/build/trang/sản phẩm/báo cáo/sổQA. Marker máy vẫn ghi coordinator_review_required theo thiết kế; quyết định này nằm riêng. Thay đổi nội dung phải review/build/acceptance mới. Ảnh/crop chỉ ở cache tạm, không thuộc output/Git.
