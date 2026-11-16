# Nghiệm thu V6.5

Ba worker Sol/high đã đọc, tuyển và tự duyệt lần lượt 80/145/64 chặng theo level. Root chạy validator toàn bộ 289 decision; không có file thiếu hoặc lỗi nguồn/schema. Kiểm nội dung chéo độc lập mười chặng S-001/S-003/S-011/S-023/S-034/S-050/H-019/H-023/H-047/H-052, cùng các mẫu bổ sung của root. Mỗi decision có lý do chọn/bỏ material, ghi chú và nguồn từng lượt để tiếp tục review.

Đã sửa nghĩa Việt cứng ở S-001/S-003, bỏ suy diễn buổi tối tại S-003 và hôm nay tại S-072, hoàn chỉnh câu trả lời ứng viên H-019 bằng các lượt liên tiếp trong nguồn. Hai câu B01 có cách diễn đạt Nhật chưa tự nhiên được loại; nội dung gốc vẫn truy được trong admin. Bản nguồn scan không mặc nhiên được xem là câu luyện đã đúng.

Đã đối chiếu 289 hàng với V6.3: UID, cấp, thứ tự, cụm, sự kiện, tình huống và tất cả trường ngoài v6 khớp. Mỗi chặng có đúng không hoặc một node shadowing, không còn node Speak Japanese/pack cũ trong learner. Mọi lượt có Nhật–Việt, speaker_id hợp lệ và giọng male/female. Mọi quote_ja và locator kiểm được với snapshot gốc; byte snapshot khớp manifest V6.3.

Preview mở bằng Chrome/Playwright, có ba tab, không lỗi JavaScript, không tràn ngang tại 320/390/1440px. Mở S-059 xem năm item theo vai; T-032 không hiện node shadowing. Mobile giữ font bài đọc 14px, desktop 16px. Không lộ anchor HTML hoặc nguồn B08 trên phần học. Payload learner không có source_refs hoặc gender_basis. Kiến thức/nguồn biên tập chỉ ở admin. Đã xem ảnh mobile sau render.

Chạy lại build qua tools/build_review_site.py cho cùng hash learner.json, chứng minh không nhân bản khi phục hồi. AUDIT.json ghi 289 checked, missing=[], errors=[]. TTS/audio chưa được sinh ở dự án này. 351 lượt phân vai có gender_basis=editorial_cast; giới tính giọng đọc này là quyết định biên tập khi nguồn không xác định. V7 dành lượt sau.
