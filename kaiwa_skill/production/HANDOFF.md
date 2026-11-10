# Production — tiếp tục toàn bộ hàng đợi

Người dùng đã yêu cầu chuyển đổi tất cả PDF. Gate pilot PASS nằm tại `kaiwa_skill/pilot/REVIEW.md`; skill 0.2.0, output chỉ text. Danh sách nguồn và phân công chuẩn: `roster.json`; bản dễ đọc: `ROSTER.txt`. Đường dẫn nguồn trong roster tương đối từ `kaiwa_skill/`; đường dẫn corpus tương đối từ repo.

Điều phối `gpt-6-astra/high`; chỉ hai worker `gpt-6-sol/high` cùng lúc, mỗi worker đúng một PDF. Chạy các lệnh từ gốc repo hiện tại. Root chat không dùng Git; coordinator chịu trách nhiệm commit tuần tự theo sách. Không sửa `bunpou_skill/` hoặc PDF nguồn.

## Tiếp tục

1. Kiểm tra tác nhân đang sống trước khi giao lại sách. Một claim không tự hết hạn. Không thu hồi khi worker cũ vẫn đang ghi.
2. Đọc `AGENTS.md`, hai skill ingest/worker, core docs, `tools/USAGE.md`, rồi chạy `status-all`. Roster là snapshot; cần refresh số đếm/hash từ file thật.
3. Dùng `python kaiwa_skill/production/refresh_roster.py` để cập nhật roster. Script chỉ đọc trạng thái corpus và ghi snapshot; không chạy worker, không xác nhận nội dung.
4. Tiếp tục sách có `worker_state: running` sau khi xác nhận worker còn sống, hoặc xử lý claim cũ/reconcile đúng CLI khi đã dừng. Đọc `corpus/BOOK_ID/HANDOFF.md` nếu có.
5. Lấy sách queued nhỏ nhất theo `queue_order` khi có slot trống. Spawn `gpt-6-sol`, `reasoning_effort=high`, `fork_turns=none`; prompt yêu cầu mở ảnh thật từng trang, mọi ngôn ngữ/bảng/ghi chú/bìa/trắng, checkpoint từng trang, text only. Ghi agent ID thực bằng `refresh_roster.py --assign BOOK_ID AGENT_ID`.
6. Worker chỉ gọi trang verified sau xem ảnh và đối chiếu. Không dùng OCR/text layer làm chứng cứ đã xem ảnh. Những chỗ không đọc được phải `needs_review`, không đoán. Tiếp tục sách độc lập khi một sách cần xử lý lỗi.
7. Khi worker hoàn thành và release: chạy build/status, kiểm tất cả trang lỗi và chọn mẫu theo bố cục/đầu-cuối unit. Ghi báo cáo nghiệm thu với hash, phạm vi mẫu và giới hạn. Chỉ nhận sách khi verified bằng toàn bộ trang, không lỗi, build hiện tại và kiểm mẫu đạt. Coverage máy không phải nghiệm thu.
8. Commit cụ thể từng output đã nghiệm thu; không stage ảnh cache/lock/scratch. Handoff dài hạn chỉ commit `WIP`, ghi rõ số trang thực và phần chưa hoàn tất. Không push.

Python cần có `pypdfium2`, `Pillow` và `pypdf`. Xác định runtime Python của môi trường hiện tại; có thể dùng runtime bundled của Codex. Không giả định đường dẫn cài đặt giữa các máy hoặc các phiên bản.

## Trạng thái đầu đợt

Inventory/status đọc lại ngày 2026-11-10: 30 PDF, 4597 trang vật lý; 4 verified ở pilot điện thoại, 4593 chưa verified. Không suy ra tiến độ hiện tại từ các số đầu đợt này; đọc roster mới hoặc CLI.

- Roster commit: `390dc38`.
- Snapshot assignments + công cụ refresh: `d34ee95`.
- Slot 1 bắt đầu `1160-t-v-ng-mimikara-n2-6d226fd8769f` (8 trang).
- Slot 2 bắt đầu `880-t-v-ng-mimikara-n3-minato-b3140fae78af` (47 trang).

Không có daemon hoặc tiến trình nền được bảo đảm tiếp tục sau khi toàn bộ tác nhân dừng. Tệp này bảo toàn quyền tiếp tục và hàng đợi, không chứng minh công việc đang chạy.
