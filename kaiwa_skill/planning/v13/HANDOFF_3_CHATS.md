# Bàn giao V13 cho ba chat soạn shadowing

Mở ba chat Local trên cùng repo `D:/CODE/git/kaiwa_skill`. Mỗi chat điều phối ba sub `gpt-6.2-sol`, reasoning `high`. Một worker chỉ được ghi bản thảo trong thư mục chặng thuộc dải của mình. Điều phối của chính chat đó đọc duyệt và xuất JSON/checkpoint cho các mã thuộc chat. Dải dưới đây tính cả hai đầu. Mã xác định quyền ghi, thứ tự soạn lấy từ mảng `stages` của `kaiwa_skill/planning/v11/learner.json`, lọc `stage_kind == "topic"`. Có mã được chèn giữa lộ trình.

| Chat | Worker | Phần chính | Phần Trung sau khi hoàn thành cấp chính |
| --- | --- | --- | --- |
| Sơ | 1 | S-001–S-027 | T-099–T-104 |
| Sơ | 2 | S-028–S-054 | T-105–T-110 |
| Sơ | 3 | S-055–S-081 | T-111–T-115 |
| Trung | 1 | T-001–T-033 | |
| Trung | 2 | T-034–T-066 | |
| Trung | 3 | T-067–T-098 | |
| Thượng | 1 | H-001–H-022 | T-116–T-126 |
| Thượng | 2 | H-023–H-043 | T-127–T-137 |
| Thượng | 3 | H-044–H-064 | T-138–T-148 |

Tổng phạm vi Sơ 98, Trung 98, Thượng 97. Đã tính chín pilot vào đúng dải chủ sở hữu. Chat Sơ và Thượng chuyển ba worker sang phần Trung của mình sau khi toàn bộ cấp chính đã duyệt. Chat Trung giữ nguyên dải T-001–T-098. Mọi chat có thể khởi động song song.

## Lệnh làm việc chung cho cả ba chat

1. Đọc `AGENTS.md` và `.agents/skills/kaiwa-topic-shadowing/SKILL.md`. Trước khi giao từng chặng, chạy từ gốc repo `py -B -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/pilot.py brief <mã>`. Chỉ soạn khi lệnh thành công và brief có nhóm từ V12 cùng hội thoại V11 của chặng. Lệnh gọi `reviewed_draft` để kiểm checkpoint V12 và hash. Chỉ có thư mục, `vocabulary.json`, hay thấy từ trên HTML đều chưa đủ. Nếu thiếu/đang ghi/checkpoint lệch thì ghi mã và lý do vào danh sách chờ của chính chat, chuyển tới mã sẵn sàng tiếp theo. Quét lại danh sách chờ theo thứ tự lộ trình sau mỗi lô và trước khi kết thúc. Khi chỉ còn chặng chờ, kiểm lại trong khi V12 đang tiến triển. Nếu nguồn bị kẹt, báo đúng mã và lý do để tiếp quản. Tuyệt đối chỉ đọc V11 và V12.
2. Đầu ra hàng loạt ở `kaiwa_skill/planning/v13/stages/<mã>/`. Worker lưu `draft.json` nguyên tử và giữ `pins` của brief đã dùng. Chỉ điều phối được gọi publish sau lượt rà nội dung. Phiên bản script lúc bàn giao chỉ hỗ trợ đường dẫn pilot. Riêng chat Trung chuẩn bị chế độ `--target stages` cho `check` và `publish`, giữ `pilot` là mặc định và dùng nguyên logic của `pilot.py`. Thêm một thao tác chỉ đọc để kiểm checkpoint V13 theo code, trạng thái reviewed, input pins, hash bản thảo và hash gói xuất. Kiểm thử bằng bản sao/thư mục tạm. Giữ nguyên SKILL.md trong đợt này để pins giữa chín worker nhất quán. Sơ/Thượng có thể bắt đầu lấy brief và viết vào `stages` ngay. Nếu công cụ chung chưa sẵn sàng, giữ draft để điều phối duyệt sau. Không gọi `publish` mặc định trên dữ liệu hàng loạt.
3. Khi tiếp tục sau gián đoạn, bỏ qua chặng có checkpoint sản xuất đã duyệt và còn khớp đầy đủ. Nếu đã có draft, kiểm pins và tiếp tục từ phần hợp lệ. Nếu nguồn đổi, đọc lại phần đổi, rà các câu bị ảnh hưởng rồi mới cập nhật pins. Với chín pilot có sẵn (S-003, S-011, S-024, T-002, T-008, T-044, H-002, H-004, H-020), chủ dải kiểm lại pins và review_notes. Nếu còn phù hợp, dùng lại draft, xử lý ghi chú biên tập ở bản sản xuất và xuất checkpoint mới. Giữ nguyên snapshot pilot. Hạng mục nghe TTS có thể giữ thành ghi chú sau khi tích hợp giọng.
4. Mỗi chặng có một bài shadowing gồm các câu nói độc lập, mỗi câu có một vai, giọng TTS `male` hoặc `female`, trường `ja` và `vi` riêng. Soạn dựa trên từ vựng V12, các tình huống và toàn bộ hội thoại V11. Shadowing giáo trình là nguồn tham khảo. Bắt đầu bằng câu dễ nhắc theo, rồi luyện lại mẫu ở hoàn cảnh hoặc dụng ý khác. Cân độ khó theo vị trí trong cấp. Thường 18–24 câu, linh hoạt theo lượng điều thực sự đáng luyện. Áp dụng hai lượt đọc Nhật và Việt trong skill.
5. Điều phối duyệt theo lô nhỏ khoảng 5 chặng/worker. Kiểm đặc biệt câu mở đầu, độ lặp sát nhau, cách nói hợp vai, nguyện vọng/đề nghị/xin phép trong bản Việt. Sửa lỗi ở chặng thuộc mình rồi kiểm lại. Trước khi xuất, xác nhận V12 hiện vẫn được duyệt và pins còn khớp. Báo số chặng mới, dùng lại, chờ V12, còn vướng và số câu. Khi xong phạm vi, mỗi chat lưu một báo cáo riêng tại `kaiwa_skill/planning/v13/handoff/{so,trung,thuong}.md` tương ứng. Các worker không sửa skill, script, HTML, báo cáo chung hoặc Git. Các chat V13 không sửa `docs/index.html` trong khi V12 cũng đang dựng trang đó. Chỉ chat Trung phụ trách tổng hợp tiến độ từ checkpoint của cả ba chat khi đã đủ đầu ra. Việc push/deploy nằm ngoài lượt soạn này.

## Ba prompt để dán

### Chat Sơ

Mở repo Local D:/CODE/git/kaiwa_skill. Thực hiện đúng hợp đồng kaiwa_skill/planning/v13/HANDOFF_3_CHATS.md, phần chat Sơ. Chat chính điều phối ba sub gpt-6.2-sol/high. Chạy các chặng Sơ trước, khi xong dùng lại ba sub phụ Trung theo đúng dải đã giao. Trước từng chặng phải chạy brief kiểm checkpoint từ vựng V12. Lưu tiến độ từng chặng và nghiệm thu theo lô cho đến khi hoàn tất phạm vi.

### Chat Trung

Mở repo Local D:/CODE/git/kaiwa_skill. Thực hiện đúng hợp đồng kaiwa_skill/planning/v13/HANDOFF_3_CHATS.md, phần chat Trung. Chat chính điều phối ba sub gpt-6.2-sol/high cho T-001–T-098 và tự chuẩn bị công cụ xuất/kiểm checkpoint vào stages dùng chung như mục 2. Trước từng chặng bắt buộc chạy brief kiểm checkpoint V12. Nghiệm thu theo lô. Dải T-099–T-148 đã thuộc Sơ và Thượng. Cuối đợt tổng hợp tiến độ toàn bộ qua checkpoint.

### Chat Thượng

Mở repo Local D:/CODE/git/kaiwa_skill. Thực hiện đúng hợp đồng kaiwa_skill/planning/v13/HANDOFF_3_CHATS.md, phần chat Thượng. Chat chính điều phối ba sub gpt-6.2-sol/high. Chạy các chặng Thượng trước, khi xong dùng lại ba sub phụ Trung theo đúng dải đã giao. Trước từng chặng phải chạy brief kiểm checkpoint từ vựng V12. Lưu tiến độ từng chặng và nghiệm thu theo lô cho đến khi hoàn tất phạm vi.
