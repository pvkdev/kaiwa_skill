# Bàn giao chat Sơ — shadowing V13

Ngày làm việc: 2026-11-19 (Asia/Tokyo). Trạng thái: **hoàn tất phạm vi chat Sơ**.

Đường dẫn trong báo cáo tương đối từ gốc repo `D:/CODE/git/kaiwa_skill`.

## Kết quả nghiệm thu

- Đủ **98/98 chặng**, tổng **2.134 câu Nhật–Việt**; cả 98 checkpoint sản xuất hợp lệ ở lượt kiểm cuối.
- Cấp Sơ: **81 chặng / 1.740 câu**.
- Phần phụ Trung T-099–T-115: **17 chặng / 394 câu**.
- Soạn mới: **95 chặng / 2.068 câu**. Dùng lại ba pilot còn hợp lệ: **S-003 (20), S-011 (22), S-024 (24)**, tổng 66 câu.
- **Danh sách chờ V12: không có. Chặng chưa duyệt hoặc còn vướng biên tập: không có.**

Đúng ba sub `gpt-6.2-sol`, reasoning `high` đã được tạo và dùng lại khi chuyển sang Trung. Cấp Sơ được kiểm đủ 81/81 checkpoint trước khi giao bất kỳ phần Trung nào. Không tạo thêm sub.

## Phân công và số lượng đã duyệt

- Sub 1: S-001–S-027, 27 chặng / 601 câu; sau đó T-099–T-104, 6 chặng / 143 câu. Tổng **33 chặng / 744 câu**.
- Sub 2: S-028–S-054, 27 chặng / 552 câu; sau đó T-105–T-110, 6 chặng / 136 câu. Tổng **33 chặng / 688 câu**.
- Sub 3: S-055–S-081, 27 chặng / 587 câu; sau đó T-111–T-115, 5 chặng / 115 câu. Tổng **32 chặng / 702 câu**.

Thứ tự lấy từ mảng `stages` của `v11/learner.json`, chỉ lọc topic và dải quyền ghi. S-081 được làm sau S-056 và trước S-057. Nghiệm thu theo lô khoảng năm chặng/worker; lô cuối có thể ngắn hơn. Chặng đầu vào chưa khớp được tách vào danh sách chờ trong khi chặng sẵn sàng tiếp tục được duyệt.

## Đầu ra và kiểm tra

Mỗi mã có ba file trong `kaiwa_skill/planning/v13/stages/<mã>/`:

- `draft.json`: nhóm luyện, câu Nhật–Việt, vai, gender, terms/scenes/pattern và pins.
- `shadowing.json`: một node shadowing, mỗi mục đúng một người nói và một lượt Nhật–Việt.
- `status.json`: trạng thái reviewed, mã chặng, pins V11/V12/skill, hash draft và output, số câu và review_notes.

Worker chạy `pilot.py brief <mã>` trước từng chặng và chỉ soạn sau khi checkpoint V12 được xác nhận qua `reviewed_draft`, với mọi hội thoại V11 đọc được. Điều phối đọc duyệt hai ngôn ngữ, sửa điểm cần thiết rồi chạy `check`, `publish`, `checkpoint` với **`--target stages`**. Không dùng publish mặc định cho dữ liệu hàng loạt.

Lượt kiểm cuối xác nhận toàn bộ 98 checkpoint: code/state, checkpoint V12 hiện tại, input pins, hash bản thảo và gói xuất, nội dung gói khớp draft, ID câu không trùng và đủ Nhật–Việt/giọng. Tổng 2.134 mục gồm 907 giọng male và 1.227 giọng female. Hash vocabulary/status V12 được đối chiếu thêm sau khi quét để phát hiện nguồn đổi giữa lượt kiểm; không còn trường hợp như vậy ở lần chốt.

Công cụ dùng chung do chat Trung phụ trách. Điều phối chat Sơ đã chạy sáu kiểm thử trên thư mục tạm, đều đạt. SKILL.md, V11 và toàn bộ JSON snapshot pilot giữ nguyên hash so với đầu lượt. Chat Sơ chỉ đọc V11/V12; không sửa script dùng chung, HTML hoặc dữ liệu của dải khác.

## Rà lại khi nguồn V12 thay đổi

- T-102 từng bị chặn vì pin V12 thay đổi sau brief. Đã lấy brief mới, đọc mục 欠席 và metadata hiện tại, rà phần thẩm quyền/người vắng/điều kiện nghiệm thu cùng terms/scenes trước khi cập nhật pins và xuất lại. Câu 009 giữ nghĩa “tiếp theo”; câu 016/018 phân biệt bấm Lưu với lưu thành công.
- Lượt kiểm cuối phát hiện thêm S-051, S-065, S-067, S-068, S-076 và S-079 có đầu vào đổi sau lần xuất trước. Đã giao lại đúng worker sở hữu, chạy brief mới cho từng mã, đọc raw vocabulary hiện tại và rà lại toàn bộ bài.
- Với sáu mã S, brief cũ/mới trùng toàn bộ từ Nhật–nghĩa Việt, nhóm, hội thoại, vai và phần nội dung dùng để soạn; chỉ pins.v12 đổi. Cache cũ không có toàn bộ metadata V12 nên không kết luận diff byte chính xác của các trường ngoài brief. Điều phối đã đọc các mục hiện tại chứa 欠 và đối chiếu hash bằng cách khôi phục pin cũ trong bộ nhớ: nội dung draft ngoài pins giữ nguyên bản đã duyệt. Cả sáu mã đã xuất lại và kiểm checkpoint thành công.

Các trường hợp trên đã gỡ khỏi danh sách chờ. Khi nguồn đổi ở lượt sau, tiếp tục lấy brief và rà nội dung bị ảnh hưởng trước khi cập nhật pins; không coi chỉ có vocabulary.json hoặc một checkpoint cũ là đủ.

## Ghi chú sau khi tích hợp giọng

S-003-V13-009: nghe thử TTS để xác nhận 角 được đọc là かど trong ngữ cảnh chỉ đường. Đây là hạng mục nghe sau khi Harumii tích hợp giọng, không chặn nghiệm thu văn bản theo bàn giao. Snapshot pilot vẫn nguyên.

## Sổ chặng đã duyệt

- S-001: 22 câu.
- S-002: 21 câu.
- S-003: 20 câu — dùng lại pilot.
- S-004: 21 câu.
- S-005: 22 câu.
- S-006: 23 câu.
- S-007: 22 câu.
- S-008: 22 câu.
- S-009: 22 câu.
- S-010: 22 câu.
- S-011: 22 câu — dùng lại pilot.
- S-012: 24 câu.
- S-013: 24 câu.
- S-014: 23 câu.
- S-015: 24 câu.
- S-016: 22 câu.
- S-017: 21 câu.
- S-018: 22 câu.
- S-019: 22 câu.
- S-020: 21 câu.
- S-021: 22 câu.
- S-022: 22 câu.
- S-023: 22 câu.
- S-024: 24 câu — dùng lại pilot.
- S-025: 23 câu.
- S-026: 23 câu.
- S-027: 23 câu.
- S-028: 21 câu.
- S-029: 21 câu.
- S-030: 21 câu.
- S-031: 20 câu.
- S-032: 20 câu.
- S-033: 20 câu.
- S-034: 23 câu.
- S-035: 20 câu.
- S-036: 21 câu.
- S-037: 19 câu.
- S-038: 20 câu.
- S-039: 19 câu.
- S-040: 19 câu.
- S-041: 19 câu.
- S-042: 22 câu.
- S-043: 19 câu.
- S-044: 19 câu.
- S-045: 24 câu.
- S-046: 24 câu.
- S-047: 19 câu.
- S-048: 19 câu.
- S-049: 20 câu.
- S-050: 18 câu.
- S-051: 22 câu.
- S-052: 20 câu.
- S-053: 22 câu.
- S-054: 21 câu.
- S-055: 21 câu.
- S-056: 22 câu.
- S-081: 22 câu.
- S-057: 23 câu.
- S-058: 21 câu.
- S-059: 21 câu.
- S-060: 21 câu.
- S-061: 21 câu.
- S-062: 21 câu.
- S-063: 21 câu.
- S-064: 22 câu.
- S-065: 21 câu.
- S-066: 22 câu.
- S-067: 23 câu.
- S-068: 21 câu.
- S-069: 23 câu.
- S-070: 21 câu.
- S-071: 21 câu.
- S-072: 21 câu.
- S-073: 22 câu.
- S-074: 23 câu.
- S-075: 24 câu.
- S-076: 22 câu.
- S-077: 21 câu.
- S-078: 22 câu.
- S-079: 21 câu.
- S-080: 23 câu.
- T-099: 24 câu.
- T-100: 24 câu.
- T-101: 23 câu.
- T-102: 24 câu.
- T-103: 24 câu.
- T-104: 24 câu.
- T-105: 22 câu.
- T-106: 23 câu.
- T-107: 23 câu.
- T-108: 21 câu.
- T-109: 24 câu.
- T-110: 23 câu.
- T-111: 23 câu.
- T-112: 23 câu.
- T-113: 24 câu.
- T-114: 22 câu.
- T-115: 23 câu.
