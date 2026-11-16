# Yêu cầu V6.4 và V6.5 — ngày 16 tháng 11 năm 2026

V6.4 ẩn mềm toàn bộ bài/video/shadowing Speak Japanese của B05/B06/B07/B11/B12/B18/B19/B20/B24 trong 289 chặng topic. Giữ nội dung và nguồn gốc ở dữ liệu nội bộ, làm căn cứ V7. V6.3 là snapshot nguyên vẹn, không xóa nguồn.

V6.5 chỉ tuyển shadowing phù hợp topic từ B01/B08/B13/B14/INTERVIEW hiện có tại chặng. Tối đa một node shadowing tổng hợp, được phép không có node khi không có nội dung phù hợp. Không bắt dùng hết sách, không thêm hội thoại AI để bù. Câu/đoạn ngắn được lấy riêng, bỏ yêu cầu pack/CD. Khử trùng và sắp dễ tới khó, giữ ngữ cảnh, Nhật và Việt, phân loại single_sentence/dialogue, vai rõ và gender male/female phục vụ TTS. Giới tính phân giọng biên tập phải ghi editorial_cast nếu không có căn cứ nguồn.

Giữ kiến thức từ tất cả bài shadowing và Speak Japanese cũ bằng tham chiếu nội bộ có thể mở đầy đủ, kể cả nội dung bị bỏ khỏi bài luyện. UI chỉ hiện chuỗi shadowing, chưa hiện video giảng kiến thức shadowing. Video kiến thức chặng vẫn là placeholder. Tình huống/challenge/free talk giữ trạng thái khung, chưa soạn nội dung mới. Từ vựng topic hiện có tiếp tục giữ.

Lộ trình vẫn 289 UID, cấp, thứ tự, sự kiện, tình huống gốc. Chặng chuyên đề Speak Japanese V7 làm sau V6.5 theo lệnh riêng. Commit V6.4 trước khi publish V6.5, mỗi version có báo cáo riêng. Ba worker gpt-6-sol/high lần lượt Sơ/Trung/Thượng, root điều phối, QA và Git. Đầu ra learner và admin tách riêng; nguồn/CD/mã sách không xuất trên phần học. Nhân vật và phân giọng không suy diễn giới tính thật từ nghề nghiệp.

Quy ước dữ liệu decision chi tiết nằm trong .agents/skills/kaiwa-shadowing-curation/SKILL.md từ gốc repo. Giữ hash đầu vào để biết khi nào cần làm lại. Từng decision là checkpoint bền vững, status reviewed chỉ sau khi đọc nguồn và tự duyệt. Build/validation có thể chạy lại không nhân bản. Nguồn scan có lỗi chưa xác minh phải bỏ khỏi phần learner và ghi lý do.
