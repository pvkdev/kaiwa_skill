# Tổng kết nghiệm thu shadowing V13 — 293 topic

Đã đối chiếu đủ **293/293 mã topic** của `v11/learner.json`, theo thứ tự lộ trình.
Tổng **6.502 câu Nhật–Việt**. Không còn mã thiếu, chờ, checkpoint lỗi hoặc mã ngoài danh mục.
Đường dẫn trong báo cáo tương đối từ gốc repo `D:/CODE/git/kaiwa_skill`.

## Theo chat sở hữu

- Chat Sơ: 98 chặng / 2.134 câu; 81 Sơ và T-099–T-115.
- Chat Trung: 98 chặng / 2.140 câu; T-001–T-098.
- Chat Thượng: 97 chặng / 2.228 câu; 64 Thượng và T-116–T-148.

## Theo cấp lộ trình

- Sơ: 81 chặng / 1.740 câu.
- Trung: 148 chặng / 3.288 câu.
- Thượng: 64 chặng / 1.474 câu.

## Căn cứ chốt

Mỗi mã đã qua kiểm `checkpoint --target stages`: mã/state reviewed, V12 hiện được duyệt,
pins V11/V12/skill, hash draft/hash output, số câu, nội dung output khớp phép chuyển từ draft.
Mỗi mục có một người nói, một lượt Nhật–Việt và giọng male/female. Không tính pilot hoặc draft chưa duyệt.
Các điều phối đã đọc duyệt nội dung trong phạm vi của mình theo bàn giao.

Lượt chốt kiểm trước và sau toàn bộ 1.470 file đầu vào/đầu ra/checkpoint: không file nào đổi.
SHA-256 snapshot: `e91609e91b419f7a8891f30fa7d9ee73d72c61275b38a6822f475bef626b1aaa`.
Thời điểm hoàn tất kiểm (UTC): `2026-11-19T03:34:54.337990+00:00`.
Dữ liệu kiểm đầy đủ: [all-checkpoints.json](all-checkpoints.json).

## Dữ liệu và công cụ

- Dùng đúng ba worker gpt-6.2-sol/high trong mỗi chat, giữ đúng dải và thứ tự learner.
- 284 chặng mới, 9 chặng dùng lại pilot sau rà; giữ nguyên snapshot pilot để đối chiếu.
- Đối chiếu baseline `21b4ef97`: SKILL.md, V11 learner, toàn bộ pilot/preview và PILOT_REPORT.md giữ nguyên.
- Công cụ check/publish có `--target stages`, pilot vẫn mặc định; checkpoint/audit chỉ đọc.
- Tám kiểm thử trên bản sao/thư mục tạm đạt; công cụ commit `97ddd578`.
- Phần Trung 98 chặng đã commit riêng `be341fdb`; preview riêng V13, không sửa HTML chung.
- V11/V12 và SKILL.md không bị các chat V13 sửa. Không push/deploy trong lượt này.

Bàn giao từng chat: [Sơ](so.md), [Trung](trung.md), [Thượng](thuong.md).
[Preview Trung 98 chặng](trung-preview.html).

S-003-V13-009 cần nghe lại cách TTS đọc 角 sau tích hợp giọng; đây là ghi chú audio sau nghiệm thu văn bản,
không phải mã đang vướng checkpoint. Chưa nghiệm thu audio TTS trong đợt biên soạn này.
