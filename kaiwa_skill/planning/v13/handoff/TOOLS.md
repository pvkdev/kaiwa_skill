# Công cụ V13 cho ba chat

Chat Trung đã bổ sung công cụ; giữ nguyên `SKILL.md` và snapshot `v13/pilot`.
Chạy từ gốc repo:

```powershell
py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/pilot.py brief T-001
py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/pilot.py check T-001 --target stages
py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/pilot.py publish T-001 --target stages --note "Điều phối đã đọc duyệt Nhật–Việt, vai và nhịp luyện."
py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/pilot.py checkpoint T-001 --target stages
py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/audit.py --scope all
```

`publish` chỉ dành cho điều phối sau lượt đọc nội dung. `check` và `checkpoint` không ghi file.
`checkpoint` kiểm mã, state reviewed, pins hiện tại (bao gồm checkpoint V12), hash draft,
hash gói xuất, số câu và nội dung gói xuất khớp phép chuyển từ draft. Nguồn hoặc draft
thay đổi trong lúc publish/checkpoint sẽ làm thao tác thất bại. Không có `--target`
thì vẫn dùng pilot, vì vậy luôn chỉ rõ `--target stages` với dữ liệu hàng loạt.

`audit.py` kiểm đủ 293 mã topic từ V11 theo thứ tự lộ trình, báo JSON trên stdout,
không ghi checkpoint hoặc nội dung. Có thể lọc `--scope so|trung|thuong` theo quyền sở hữu
trong bàn giao; `all` là mặc định. Chỉ tính câu từ checkpoint sản xuất hợp lệ.
Không coi pilot hoặc draft chưa duyệt là đã hoàn thành. Mã thiếu/chờ/lệch nguồn có lý do riêng.

Kiểm thử với bản sao pilot trong thư mục tạm:

```powershell
py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/test_pilot.py
```

Không ghi `docs/index.html` trong khi V12 đang dựng HTML. Preview V13 và báo cáo của từng
chat nằm riêng trong V13. Không push/deploy trong lượt này.

Preview có thể chọn riêng các mã đã duyệt để ba chat không ghi đè nhau, ví dụ:

```powershell
py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/preview.py --target stages --codes T-001 T-002 --output kaiwa_skill/planning/v13/handoff/trung-preview.html
```

Preview dùng lệnh checkpoint đầy đủ trước khi đưa một chặng vào trang. Luôn chỉ rõ
file `--output` riêng của chat; không chạy preview mặc định để ghi lại snapshot pilot.
