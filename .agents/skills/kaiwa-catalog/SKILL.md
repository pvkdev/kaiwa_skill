---
name: kaiwa-catalog
description: Lập chỉ mục metadata ngắn cho 27 sách kaiwa clean, tổng hợp topic và mục lục sách/chương để tìm ngược nội dung khi xây lộ trình; điều phối tối đa ba worker sol/high.
---

# Chỉ mục 27 sách kaiwa, tiết kiệm context

Đọc AGENTS.md. Nguồn chính là `kaiwa_skill/knowledge/`, không lấy memo web hoặc blueprint cũ làm taxonomy bắt buộc. Bước này chỉ tạo metadata, chưa biên soạn lộ trình/bài học, chưa phân tích ngữ nghĩa mọi câu. Không sửa sách clean/PDF/corpus/bunpou.

## Đầu ra

Thư mục `kaiwa_skill/planning/catalog27/`:

- `BOOK_GUIDE.md`: công dụng/thế mạnh/cách học/level sơ bộ của từng sách; toàn bộ chương và tóm tắt ngắn, có đường dẫn nguồn.
- `TOPICS_ALL.md`: hợp các topic do worker gán cho chương, sách và level; giữ topic trùng ở nhiều level.
- `SOURCE_LABELS.md`: tất cả nhãn mục/tình huống/biểu đạt có tên được trích cấu trúc, phân biệt với topic đã gán nhãn.
- `source_index.jsonl`: mục, hội thoại, câu/nhãn tình huống và vị trí nguồn để tìm ngược.
- `manifest.json`, `annotations/Bxx.json`: snapshot đường dẫn/hash và metadata ngắn; cho phép tiếp nối theo sách.

## Thực hiện

1. Chạy `py -B .agents/skills/kaiwa-catalog/scripts/catalog.py prepare --repo-root .`. Lệnh đọc cấu trúc toàn kho bằng máy, loại đúng ba tập từ vựng MINATO1160/MIMIKARA1170N1/MIMIKARA880N3, giữ cả các tập companion trong 27 sách. Packet chỉ có trích dẫn giới thiệu ngắn và tiêu đề/đầu mục chương; nằm trong cache, không phải bản tóm tắt toàn văn.
2. Root dùng `collaboration.spawn_agent`, `fork_turns="none"`, `model="gpt-6-sol"`, `reasoning_effort="high"`, tối đa ba worker. Mỗi worker nhận một lane trong manifest và đọc packet theo từng sách. Không truyền toàn lịch sử chat hoặc toàn sách cho worker. Nếu người dùng chỉ hỏi plan thì dừng ở chuẩn bị, không chạy queue.
3. Worker chỉ ghi `annotations/Bxx.json` thuộc lane mình. Đọc thêm đúng đoạn nguồn ngắn khi packet không đủ; tránh đọc lại cả sách. Không dùng Git. Theo [hợp đồng metadata](references/metadata.md). Ghi checkpoint ngay mỗi sách, bỏ qua annotation còn hợp lệ khi resume.
4. Root chạy `catalog.py build --repo-root .`. Builder kiểm 27 annotation, đủ chương, hash nguồn và tham chiếu; tạo mục lục/topic register bằng máy, không gọi AI viết lại báo cáo dài.
5. Root kiểm mẫu trên các dạng khác nhau: mini phrases có caption nhỏ, shadowing có đối thoại đánh số, roleplay có thẻ vai, sách business có tập phụ. Kiểm counts/links và các nhãn suy đoán. Sửa lỗi parser/metadata cụ thể rồi build lại. Chỉ root commit exact paths, không push.

## Giới hạn bắt buộc

- Ghi đúng mức đã làm: máy quét toàn văn/cấu trúc, AI đọc metadata/trích đoạn có mục tiêu. Không tuyên bố đã đọc hiểu từng câu của 27 sách.
- Không tạo tình huống mới để lấp chỉ mục. Đối thoại ít bối cảnh có thể giữ nhãn “đối thoại/câu” cùng đoạn nguồn ngắn.
- Level là nhãn nguồn và ước lượng khoảng cấp độ để tra cứu, không phải phân hạng cuối cùng từng câu. Không gán mọi nội dung theo bìa một cách tuyệt đối.
- Mỗi chương chỉ tóm tắt khoảng 8–18 từ tiếng Việt; mục đích sách tối đa khoảng 50 từ. Topic là cụm ngắn, không chép giải thích/hội thoại.
- Giữ `needs_review`/issues trong thông tin tra cứu, không mở lại toàn bộ PDF để QA lại. Audio chỉ dẫn tới inventory; không coi đã có file nghe.
- Số nhãn nguồn, số dòng index và số topic gộp là các phép đếm khác nhau. Topic gộp không được quảng bá là mọi khái niệm ngầm trong toàn corpus đã được phân tích.

Mẫu giao việc: “Đọc SKILL.md và references/metadata.md; lane N trong manifest. Dùng packet ở cache, mỗi lần một sách; hoàn thành annotation đúng schema cho toàn lane. Chỉ đọc bổ sung đoạn ngắn cần thiết. Không đọc toàn sách, không sửa nguồn/Git. Báo số sách/chương đã ghi và chỗ chưa rõ.”
