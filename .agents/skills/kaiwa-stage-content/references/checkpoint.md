# Checkpoint và revision

Chạy từ gốc repo bằng Python 3.10+. Lõi checkpoint dùng thư viện chuẩn; kiểm gói Harumii dùng thêm `jsonschema`. Helper không gọi model, không tiêu token để sinh nội dung. Một worker biên soạn một chặng tại một thời điểm. Không có điểm hay trạng thái hoàn thành của người học trong dữ liệu này.

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

`begin` trả đường dẫn draft V3.2 và tạo `learning-map.json` rỗng. Tác giả viết trực tiếp trong draft đó. Đây **không phải chặng đã hoàn thành**. `checkpoint` và `pause` cần chỉ dẫn tiếp theo đủ cụ thể cho người mới nhận việc, gồm bài/nhánh tiếp theo và nội dung cũ cần ôn. Nếu sổ nguồn/sổ bài đang viết dở hoặc hash chưa khớp, vẫn lưu với `source_warning`/`context_warning`; phải sửa trước khi chốt phần liên quan.

Lượt mới khai báo `harumii_export: harumii-stage.json`; chuẩn bị payload Exchange 1.0.0 theo [hướng dẫn xuất](harumii-exchange.md). `validate` kiểm gói app và ID/loại node/metadata khớp workspace; `finalize` còn yêu cầu revision gói bằng revision snapshot mới. Các challenge có thể được thêm ở gói app, nhưng không được làm mất ID node biên tập. Workspace legacy không có khai báo vẫn đọc được; muốn import feature mới thì nâng cấp draft, không bỏ khai báo chỉ để vượt kiểm tra. Sau khi chốt, dùng `kaiwa_exchange.py pack` từ file snapshot để tạo artifact có manifest; không lấy file preview sửa tay làm nguồn nhập.

`resume` yêu cầu draft không thay đổi từ lúc pause và các nguồn/spec/context đã pin còn khớp. Nếu có thay đổi, không reset: kiểm lý do rồi dùng recovery. Pin gồm registry, skill, các reference của skill, script và metadata khung nếu có; nguồn từ `sources.json`; context các bài trước từ `learning-map.json`, kèm con trỏ revision hiện hành và các file của bài đã tham khảo. Thay đổi phải đọc lại phần liên quan, ghi tái đối chiếu; không chỉ đổi hash hoặc revision để làm lệnh chạy qua.

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

V3.0 cũ vẫn đọc được. Nâng lên 3.1 trong draft mới: giữ ID, bổ sung nhóm bài/gối đầu, loại shadowing, metadata cặp kiến thức/video và nhãn từ mới/ôn; không sửa snapshot cũ. Khi bài trước được nâng cấp, con trỏ trong draft bài sau cần đọc lại và cập nhật. Dùng UID/lesson ID tìm các chặng phụ thuộc; không tự sửa hoặc tái sinh tất cả bài sau.

Nâng lên 3.2 trong draft mới: giữ ID, thêm `free_talk` do tác giả soạn cho node `live_context` ở cuối chặng; xuất cả `live-context.md` và `free-talk-situation.md`. Helper vẫn đọc 3.0/3.1 mà không tự sửa snapshot. Khi nâng cấp kiến thức, phải đọc lại phần tổng hợp free talk, sửa nếu cần rồi xuất lại; không chỉ ghép tài liệu mới vào một lời dẫn đã lỗi thời. File free talk không chịu giới hạn 1.000 ký tự của luồng user nhập tay.

Pilot rời có thể ghi `pending_previous` nếu bài trước chưa tồn tại. Helper giữ số pending trong kết quả validate và manifest revision (`continuity_pending`) thay vì tuyên bố đã nối xong. Đây là ghi chú biên tập; không có cổng người học.

## Bảo đảm và giới hạn

- Owner theo chặng ngăn helper mở hai lượt đồng thời. Guard tạo độc quyền bảo vệ các lần cập nhật metadata; mọi mutating command kiểm RUN hiện còn sở hữu chặng.
- Draft cũ và revisions không bị helper ghi đè. Revision mới được sao chép, băm, viết manifest trước khi đổi `current.json` bằng atomic replace. Bản snapshot dang dở không trở thành current; lần sau dùng số revision mới.
- `validate` kiểm node/file/ID, hai vai khi có hội thoại, Nhật–Việt, quan hệ sự kiện, cặp Speak Japanese liền nhau, anchor ví dụ, nhóm bài, liên kết ôn đúng bài trước, từ review có nguồn trước, Live có đủ node và free talk V3.2 có dữ liệu biên soạn/đứng cuối chặng. `finalize` ghép hai bản context; không tự viết phần tổng hợp. Không kiểm được tiếng Nhật tự nhiên, đã đọc thật, dịch đúng hoặc ví dụ thực hành đúng ý kiến thức. Người biên tập phải làm phần đó trước `--editor-reviewed`.
- Helper không khóa quyền sửa file bằng tay, không phải cơ chế bảo mật và không bảo đảm nhiều máy/ổ mạng. Không cho hai tiến trình dùng chung RUN/draft. Trước recovery phải dừng tiến trình cũ; không làm takeover giữa lúc người cũ vẫn viết.
- Atomic replace giảm metadata bị ghi nửa chừng; không thay thế backup/Git và không hứa chống mất dữ liệu do hỏng ổ đĩa. Checkpoint đều đặn, lưu handoff trước khi hết quota. Không thể cứu phần chưa từng được ghi xuống đĩa.
