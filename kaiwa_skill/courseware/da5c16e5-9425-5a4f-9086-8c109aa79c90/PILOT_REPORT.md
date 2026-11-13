# Pilot S-011 — Tàu điện & xe buýt

Revision r0001 đã chốt để người dùng đọc thử; chưa tự chạy hàng loạt.

- [Đọc toàn chặng theo thứ tự học](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0001/stage-preview.md)
- [Ví dụ challenge — phần user](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0001/challenge-c02-transfer.learner.md)
- [Cùng challenge — phần AI](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0001/challenge-c02-transfer.ai.md)
- [Context free talk đã tạo sẵn](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0001/free-talk-situation.md)
- [Canonical JSON để migration](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0001/stage.json)
- [Nghiệm thu và quyết định biên tập](revisions/r0001/content/editorial.md)
- [Nguồn đã dùng và vị trí đã đọc](revisions/r0001/content/sources.json)

## Kết quả

5 bài kiến thức, trong đó có một cặp Speak Japanese → shadowing ngay sau; 5 nhóm shadowing, 15/15 tình huống thuộc 3 sự kiện V5, 112 lượt hội thoại Nhật–Việt; 3 challenge với 6 variant và một free talk cuối chặng. Có 132 đơn vị câu Nhật–Việt, 78 mục từ qua 3 list (71 từ khác nhau) và 7 mẫu ngữ pháp có level + tên.

Quét chỉ mục đủ 27 sách, đọc sâu các phần được chọn của 5 sách B01/B08/B11/B14/B27, Minna và hai nguồn chính thức. Chuyển soạn kiến thức/cách luyện, viết mới hội thoại và các nhánh, không chép lại toàn sách. Không dùng 100% nguồn làm KPI.

## Những gì đã thử thật

- Canonical source sinh workspace/MD và gói output; không soạn nội dung hai lần.
- Pause/resume trên chính pilot, giữ nguyên file/source/spec pins.
- Recovery JSON viết dở và nâng revision được thử trên fixture, không phá pilot.
- Kiểm đúng 15 situation UID của V5, schema, liên kết, nhánh, Nhật–Việt, hash snapshot và artifact.
- Self-review toàn bộ nội dung; đã sửa nhãn từ ôn sai, giản hóa câu và xử lý một mâu thuẫn mạng buýt giả định. Không nhận đã có reviewer bản ngữ hoặc đã chạy Live/TTS.

## Giới hạn cần biết

Pilot bắt đầu ở chặng S-011 trong khi chặng trước chưa biên soạn. Gối đầu trong 5 bài đã có, nhưng giữ một pending_previous xuyên chặng, chưa tuyên bố nối xong toàn lộ trình. Bản này là pilot để bạn đánh giá nội dung/độ dày, không phải nghiệm thu hiệu quả với người học thật.

Lộ trình/giá/thời gian giả định có nhãn rõ. Thông tin lên xuống xe theo tuyến được đối chiếu [Kyoto City Bus](https://www2.city.kyoto.lg.jp/kotsu/webguide/en/bus/howtoride_bus.html); nhu cầu phối hợp hỗ trợ được đối chiếu [JR East](https://www.jreast.co.jp/en/equipment/equipment_1/wheelchair/). Không hứa đây là hành trình hoặc dịch vụ thật.

## Tiếp tục hoặc nâng cấp

Đọc `AGENTS.md`, skill và `references/run-and-resume.md`. Trạng thái gốc tại `current.json` và `runs/`; bảng tổng hợp tại `../STATUS.md` là dẫn xuất. Pilot đã finalized, không resume/recover để viết đè. Khi có yêu cầu sửa: `stage_work.py begin --stage da5c16e5-9425-5a4f-9086-8c109aa79c90 --from-current`; giữ ID, sửa canonical source, sync/validate/review rồi chốt r0002. Nếu một lượt nâng cấp dở bị ngắt, dùng quy trình pause/recovery như hướng dẫn. Không cần lịch sử chat còn nguyên.

## Token và quy mô

Canonical JSON có 75205 ký tự, gồm dữ liệu học và cấu trúc. Đây không phải số token bill. Công cụ local không có telemetry quota của Codex/Claude và không suy phần trăm quota từ số chữ. Phần chuẩn bị tool/skill và lượt biên soạn thực là hai khối công việc khác nhau; các chặng tiếp theo tái sử dụng tool, nhưng vẫn cần đọc nguồn, viết và review. Các bản MD/context được script sinh, không gọi thêm model.
