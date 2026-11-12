# Checkpoint và revision

Chạy từ gốc repo bằng Python 3.10+. Helper chỉ dùng thư viện chuẩn, không gọi model, không tiêu token để sinh nội dung. Một worker biên soạn một chặng tại một thời điểm. Không có điểm hay trạng thái hoàn thành của người học trong dữ liệu này.

## Lệnh

Trong PowerShell, thay UID và RUN bằng giá trị thật. UID lấy từ registry; RUN là UUID helper trả về.

```powershell
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py begin --stage UID
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py status --stage UID --run RUN
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py checkpoint --stage UID --run RUN --note 'Đã đọc phần nguồn và viết xong cụm đầu' --next 'Đọc nguồn cho nhánh bị từ chối rồi viết s02'
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py pause --stage UID --run RUN --note 'Dừng sau cụm đầu' --next 'Tiếp nhánh từ chối; xem editorial.md'
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py resume --stage UID --run RUN
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py validate --stage UID --run RUN
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py finalize --stage UID --run RUN --editor-reviewed --note 'Đã đọc lại nội dung, xác minh nguồn dùng và ghi các giới hạn trong editorial.md'
```

`begin` trả đường dẫn draft. Tác giả viết trực tiếp trong draft đó. Khởi tạo chỉ tạo mục lục rỗng và nhật ký, **không phải một chặng đã hoàn thành**. `checkpoint` và `pause` cần chỉ dẫn tiếp theo đủ cụ thể cho người mới nhận việc. Nếu sổ nguồn đang viết dở hoặc hash nguồn chưa khớp, vẫn lưu công việc với `source_warning`; chưa được chốt revision.

`resume` yêu cầu draft không thay đổi từ lúc pause và các nguồn/spec đã pin còn khớp. Nếu có thay đổi, không xóa hoặc reset: kiểm lý do rồi dùng recovery. Registry, skill, hợp đồng dữ liệu và script được pin nếu nằm trong repo; nguồn đã dùng được pin từ `sources.json`. Thay đổi một nguồn cần đọc lại phần liên quan, cập nhật vị trí/hash và ghi rõ việc tái đối chiếu; không chỉ đổi hash để làm lệnh chạy qua.

## Sau hết quota, tắt máy hoặc tiến trình bị ngắt

1. Đọc `status` và `next_action`, draft, checkpoint mới nhất. Byte đã ghi xuống file vẫn còn dù chưa checkpoint; phần còn trong context chưa ghi đĩa không thể tự khôi phục.
2. Xác nhận worker cũ đã dừng. Không đoán worker chết chỉ vì chạy lâu.
3. Nhận lại bằng lệnh dưới; bản cũ được giữ nguyên, lượt cũ chuyển `superseded`, lượt mới có draft riêng và RUN mới. Hash khác checkpoint là việc phải kiểm, không tự bỏ phần khác.

```powershell
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py recover --stage UID --run RUN --ack-stopped --next 'Kiểm phần viết dở rồi tiếp cụm thứ hai'
```

Nếu tiến trình chết đúng lúc helper đang ghi metadata, có thể còn `.mutation.lock`. Chỉ khi đã dừng worker cũ mới thêm `--clear-stale-guard`. Không tự xóa lock chỉ để chạy tiếp nhanh. Recovery từ lượt đã chốt không cần thiết; dùng begin nâng cấp. Nếu con trỏ current đã được chốt nhưng ghi trạng thái lượt bị ngắt ngay sau đó, recovery đối chiếu hash revision rồi hoàn tất trạng thái, không chốt lặp.

File draft có JSON viết dở vẫn được giữ trong recovery; phải sửa để parse được trước validate/finalize. Dùng ghi file tạm rồi rename khi thay một JSON lớn để giảm khả năng file dở dang.

## Nâng cấp

```powershell
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/stage_work.py begin --stage UID --from-current --next 'Bổ sung nhánh có điều kiện; giữ các ID đang dùng'
```

Lệnh sao chép revision hiện tại vào draft mới sau khi đối chiếu manifest. Giữ ID đối tượng cũ, thêm ID cho đối tượng mới. Nếu bỏ node, thêm `{id, reason, replacement_ids}` vào `retired_ids`; không dùng lại ID cho cảnh khác. Tác giả ghi diff về nghĩa/nội dung trong `editorial.md`, sửa các liên kết và danh sách context. Helper không tự quyết định một đối tượng còn cùng nghĩa hay không.

## Bảo đảm và giới hạn

- Owner theo chặng ngăn helper mở hai lượt đồng thời. Guard tạo độc quyền bảo vệ các lần cập nhật metadata; mọi mutating command kiểm RUN hiện còn sở hữu chặng.
- Draft cũ và revisions không bị helper ghi đè. Revision mới được sao chép, băm, viết manifest trước khi đổi `current.json` bằng atomic replace. Bản snapshot dang dở không trở thành current; lần sau dùng số revision mới.
- `validate` kiểm node/file/ID, hai vai, nghĩa từng lượt, quan hệ sự kiện, danh sách nguồn và context đủ node. Không kiểm được tiếng Nhật tự nhiên, việc đã đọc thật, nghĩa bản dịch hoặc độ rộng tình huống. Người biên tập phải làm phần đó trước `--editor-reviewed`.
- Helper không khóa quyền sửa file bằng tay, không phải cơ chế bảo mật và không bảo đảm nhiều máy/ổ mạng. Không cho hai tiến trình dùng chung RUN/draft. Trước recovery phải dừng tiến trình cũ; không làm takeover giữa lúc người cũ vẫn viết.
- Atomic replace giảm metadata bị ghi nửa chừng; không thay thế backup/Git và không hứa chống mất dữ liệu do hỏng ổ đĩa. Checkpoint đều đặn, lưu handoff trước khi hết quota. Không thể cứu phần chưa từng được ghi xuống đĩa.
