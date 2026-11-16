# V11 — đợt 01

Chủ dự án cho chạy ngày 16-11-2026, tối đa 20 chặng mới mỗi level theo thứ tự lộ trình. Đợt này gồm 60 chặng topic và 1.222 tình huống. Chín pilot đã có được giữ riêng và ghép vào preview cùng đợt mới.

Ba worker gpt-6-sol/high mỗi người sở hữu một level. Runtime chat điều phối hiện là gpt-6.1-sol. Danh sách cố định và hash đầu vào ở PLAN.json. Worker tự rà theo skill V11 trước khi bàn giao. Lượt kiểm tra ngôn ngữ độc lập toàn bộ đợt được để sau sản xuất theo quyết định của chủ dự án.

## Tiếp tục khi gián đoạn

Mở PLAN.json, đọc status.json và dialogues.json trong planning/v11/stages/<code>. Đối chiếu hash bản thảo, UID cảnh với brief V10 và trạng thái của từng sự kiện. Hoàn tất chặng đang dở trước khi chuyển chặng kế trong cùng level. Mỗi chặng chỉ một worker ghi. File chặng đã xong phải qua dialogue.py --check.

Đọc lại skill .agents/skills/kaiwa-topic-dialogue/SKILL.md và references/draft.md trước khi tiếp tục. Giữ các cảnh tự rà đúng hash, tiếp các UID chưa có. Nếu sửa lời thoại thì đọc lại nhánh chịu ảnh hưởng và cập nhật checkpoint. Source metadata phải dẫn đúng tài liệu đã mở.

## Dựng và xem kết quả

Từ gốc repo, chạy `py -X utf8 tools/roadmap_v11.py --batch batch01 --publish` sau khi đủ 60 chặng. Lệnh kiểm mọi đầu vào của đợt, ghép với chín pilot và giữ toàn bộ nền V10. learner.json, ROADMAP.html và BUILD.json nằm ở planning/v11. docs/index.html là bản HTML dùng cho GitHub Pages. Bản pilot giữ trong thư mục pilot.

Tiến độ thực tế được điều phối cập nhật trong PROGRESS.json. Chỉ gọi hoàn tất sản xuất khi có đủ 60 chặng hợp lệ và đã dựng/đối chiếu preview. Trạng thái chờ rà độc lập được giữ rõ trong hồ sơ.
