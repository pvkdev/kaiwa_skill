# V11 — đợt 03

Thêm 20 chặng topic chưa soạn ở mỗi level theo thứ tự V10, tổng 60 chặng và 1.312 tình huống. PLAN.json cố định phân công. Thứ tự S-081 theo vị trí hiện có trong lộ trình. Ba worker gpt-6-sol/high, mỗi người một level. Chat điều phối dùng gpt-6.1-sol theo cấu hình hệ thống.

Mỗi chặng nằm trong `planning/v11/stages/<code>` với dialogues.json, RESEARCH.md và status.json. Đọc skill kaiwa-topic-dialogue và references/draft.md trước khi viết hoặc phục hồi. Lưu checkpoint theo sự kiện, giữ các UID đã tự rà và có hash khớp, tiếp các UID còn thiếu. PROGRESS.json do điều phối cập nhật sau kiểm tra bản trên đĩa.

Nhật–Việt được viết ở hai trường riêng, hai vai có gender cho TTS. Nguồn sách và nguồn thực tế nằm ở phần quản trị. Người soạn đọc từng cảnh riêng rồi theo các nhánh, đối chiếu vai, thời điểm, quyền quyết định và bản Việt. Dữ kiện y tế, khẩn cấp, quyền lợi và thủ tục cần nguồn chính thức đúng phạm vi. authored_self_reviewed ghi nhận vòng tự rà. Lượt biên tập độc lập của 60 chặng mới giữ pending.

Khi đủ phạm vi, chạy từ gốc repo `py -X utf8 tools/roadmap_v11.py --batch batch03 --publish`. Bộ dựng ghép cả ba đợt và chín pilot, tạo 189 chặng topic có hội thoại trong preview lũy kế. Lịch sử rà độc lập của 129 chặng trước được kiểm theo hồ sơ hiện có. HTML/JSON ở planning/v11, bản Pages ở docs/index.html.
