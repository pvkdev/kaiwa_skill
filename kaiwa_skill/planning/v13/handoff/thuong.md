# V13 — Bàn giao chat Thượng

Hoàn tất ngày 19/11/2026. Lượt kiểm cuối lúc 12:32:28 JST đạt **97/97 checkpoint**, tổng **2.228 câu Nhật–Việt**; không có lỗi hoặc mã đang chờ.

## Kết quả

- Cấp Thượng: **64 chặng, 1.474 câu** (H-001–H-064).
- Phần phụ Trung: **33 chặng, 754 câu** (T-116–T-148).
- **94 chặng soạn mới**, **3 chặng dùng lại pilot còn phù hợp**: H-002, H-004, H-020. Các bản sản xuất đã xử lý ghi chú biên tập; snapshot pilot được giữ nguyên.
- Chặng mới, dùng lại và mọi lần sửa đều được root đọc duyệt trước khi xuất `shadowing.json` và `status.json`.

Đầu ra từng chặng nằm tại `kaiwa_skill/planning/v13/stages/<mã>/`, gồm `draft.json`, `shadowing.json`, `status.json`.

## Phân công đã hoàn tất

Dùng đúng ba sub `gpt-6.2-sol`, reasoning `high`, giữ nguyên ba sub qua hai pha. Root trực tiếp điều phối và nghiệm thu; không tạo sub điều phối khác.

- Sub 1: H-001–H-022 **496 câu**, sau đó T-116–T-126 **251 câu**; tổng **33 chặng / 747 câu** (30 mới, 3 dùng lại).
- Sub 2: H-023–H-043 **480 câu**, sau đó T-127–T-137 **254 câu**; tổng **32 chặng mới / 734 câu**.
- Sub 3: H-044–H-064 **498 câu**, sau đó T-138–T-148 **249 câu**; tổng **32 chặng mới / 747 câu**.

Hoàn tất và quét đủ 64 checkpoint Thượng trước khi giao phần Trung. Trong từng dải, thứ tự lấy từ `stages` của V11 `learner.json`, lọc topic. Phần Trung của sub 3 đã đi: T-146, T-138, T-139, T-140, T-141, T-147, T-148, T-142, T-143, T-144, T-145.

## Cách nghiệm thu

Trước mỗi chặng, worker chạy `py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/pilot.py brief <mã>`, đọc từ vựng V12 đã qua `reviewed_draft`, mọi hội thoại V11 và shadowing cũ. Mã chưa sẵn sàng được ghi chờ, làm mã sẵn sàng tiếp theo rồi quét lại. Các mã Trung ban đầu chưa đủ V12 đều đã được quay lại khi hợp lệ.

Nghiệm thu theo lô khoảng năm chặng/worker, lô cuối mỗi dải ngắn hơn. Root đọc toàn bộ Nhật–Việt, rà câu mở, nhịp luyện, vai người nói/nghe, sắc thái lời nhờ/nguyện vọng/xin phép, mức chắc chắn và việc câu có đứng riêng được không. Worker đọc lại riêng tiếng Nhật và tiếng Việt. Khi sang Trung, đã cân lại N3–N2 theo vị trí chặng, giảm câu dài và tầng kính ngữ; lời hỗ trợ khẩn cấp ưu tiên ngắn, trực tiếp, kính ngữ dịch vụ dùng đúng vai.

Xuất bằng `check` / `publish` / `checkpoint` với **`--target stages`**. Công cụ chung do chat Trung chuẩn bị; chat này không sửa skill, script, HTML, V11 hoặc V12.

Trong lúc làm, V12 đổi sau lần xuất ở H-014, H-022, H-032, H-055. Đúng chủ dải đã chạy lại brief, so từng trường, đọc lại câu và liên kết trước khi cập nhật pins. Nội dung brief dùng để soạn không đổi; bốn gói đã được root xuất lại và qua kiểm cuối. H-038 cũng đã được đối chiếu brief mới khi V12 đổi trong lúc soạn.

## Kiểm cuối và phần chờ

Lượt kiểm toàn phạm vi đã xác nhận cho cả 97 mã: trạng thái reviewed, V12 checkpoint hợp lệ, V11 có hội thoại đầy đủ, pins V11/V12/skill, hash bản thảo và gói xuất, số câu và nội dung node xuất khớp bản thảo. Sau lượt quét, kiểm lại hash hiện tại không phát hiện đầu vào đổi. Các cảnh báo dò mặt chữ từ vựng đều đã được đọc lại, là biến đổi tiểu từ hoặc đơn vị đếm hợp lệ.

- Chờ V12: **không có**.
- Chờ đọc V11: **không có**.
- Draft chưa duyệt hoặc checkpoint lệch: **không có**.
- Vướng nội dung cần tiếp quản: **không có**.

Chat Trung có thể lấy trực tiếp 97 checkpoint này để tổng hợp tiến độ chung. Không sửa `docs/index.html`, không push hoặc deploy trong lượt soạn này.
