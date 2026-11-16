# V11 — đợt 02

Tiếp đợt 01 theo lệnh chủ dự án, thêm 20 chặng topic mới mỗi level theo thứ tự V10. Danh sách cố định ở PLAN.json. Ba worker gpt-6-sol/high, mỗi người sở hữu một level; chat điều phối hiện dùng gpt-6.1-sol theo cấu hình hệ thống.

Mỗi chặng trong planning/v11/stages/<code> có dialogues.json, RESEARCH.md và status.json. Dữ liệu có tiếng Nhật–Việt riêng, hai vai và giới tính TTS, nguồn quản trị và checkpoint sau từng sự kiện. Đọc skill kaiwa-topic-dialogue và references/draft.md trước khi phục hồi.

Khi tiếp tục, so hash của bản thảo với status, giữ cảnh tự rà khớp hash, hoàn tất các UID còn thiếu trước khi chuyển chặng kế. Kiểm chặng hoàn chỉnh bằng dialogue.py --check. PROGRESS.json do điều phối cập nhật cho cả đợt. Trạng thái authored_self_reviewed ghi việc tự rà; lượt kiểm tra ngôn ngữ độc lập giữ pending theo luồng đã chốt.

Sau khi đủ 60 chặng, chạy từ gốc repo `py -X utf8 tools/roadmap_v11.py --batch batch02 --publish`. previous_batches trong PLAN.json liệt kê các đợt trước được ghép cùng. Preview sẽ gồm đợt 01, đợt 02 và chín pilot. Bản HTML/JSON nằm trong planning/v11, bản dùng cho GitHub Pages là docs/index.html.
