# Rà độc lập V11 batch04 — 60 chặng

Đã rà đủ 60 chặng vừa biên soạn, gồm 1.012 hội thoại thuộc 238 sự kiện. Ba phiên gpt-6.2-sol/high mới, độc lập với phiên tác giả, phụ trách mỗi nhóm 20 chặng theo phân công trong RUN.json. Mốc trước sửa và hash đầu vào được ghim bằng baseline_commit.

- Nhóm Sơ kèm T-084–T-085: 365 cảnh; giữ 210, biên tập 155. Trong đó 153 cảnh đổi phần học viên đọc, 2 cảnh chỉ chỉnh hồ sơ nguồn.
- Nhóm T-064–T-083: 318 cảnh; giữ 210, biên tập 108.
- Nhóm H-064 và T-086–T-104: 329 cảnh; giữ 211, biên tập 118.

Tổng 381 cảnh được ghi fixed: 379 cảnh đổi lời thoại, bản Việt, vai hoặc bối cảnh; 2 cảnh chỉ sửa nguồn quản trị. 631 cảnh giữ nguyên. Số biên tập gồm cả làm rõ cách nói, không phải số lỗi nghiêm trọng. Nguồn dùng chung được cập nhật ở 5 chặng.

Các điểm sửa có ảnh hưởng việc học:

- Sửa chiều chênh lệch giờ Hà Nội–Tokyo và lịch nối tiếp trong T-069; sửa câu Việt đảo nghĩa “có người muốn nghe lại” ở T-071.
- Phân biệt ngày xuất hàng với ngày giao, giá thuê theo giờ, phí đã gồm thuế hay chưa, số đo và số trung bình; giữ điều kiện tương ứng với từng mức báo giá.
- Làm rõ ai có quyền duyệt, nghiệm thu thật hay còn chờ, giờ cập nhật dù chưa có kết quả, đầu mối thay và người chịu trách nhiệm gọi.
- Bổ sung xác nhận giữ chỗ khi cảnh sau cần dùng việc đã đặt; kiểm thông tin dịch vụ theo phạm vi Toyoko Inn, ANA, Haneda, Fukuoka, Koganeyu và nguồn địa phương.
- Sửa kính ngữ về hành động của chính mình, lời xin phép/từ chối và cách chốt bước tiếp. OJT phân biệt mã kiểu máy với số phiếu, người học nhắc lại đủ các mục và điều kiện trước khi làm.

Reviewer đọc riêng toàn bộ mạch Nhật và Việt, so vai/giới tính, mục tiêu và mức lịch sự, rồi đọc nối từng nhánh continues_from. Đoạn sách được dùng đã mở lại; khẳng định thực tế được đối chiếu nguồn chính thức đúng phạm vi. Với số liên hệ Fukuoka chưa xác minh cụ thể, cảnh hướng người học tìm đầu mối trên phiếu tình huống, không đưa số chưa được kiểm. Hồ sơ từng chặng ghi rõ mức nguồn thực sự đã đọc.

T-067 giữ điểm nối S015→S016 của V10. Reviewer đã đọc lại cả JA/VI: bối cảnh và lời nói nêu rõ lời mời Hinode Soft mới sau hai năm, nên không đảo trạng thái đã nhận offer trước. Quyết định và căn cứ được lưu trong RESEARCH cùng phiếu rà.

Cả 60 chặng qua review.py --check, đúng hash bản thảo, từng cảnh, nguồn sách và đầu vào đã ghi. Phiếu từng UID có lượt dẫn chứng và lý do giữ/sửa; từng sự kiện có ghi chú đọc nhánh. Không còn needs_fix/pending hoặc vấn đề mở được ghi nhận. Lịch sử tác giả được giữ trong hồ sơ hoặc qua commit đầu vào.

Điều phối kiểm toàn bộ diff và bằng chứng, đọc mẫu các cảnh giữ/sửa, rồi kiểm gói xuất. Đây không phải tuyên bố root đọc lại lần ba toàn bộ nội dung.

Lượt này thêm 4 lượt nói: 60 chặng có 4.560 lượt thay cho 4.556. Preview lũy kế hiện có 249 chặng topic, 5.032 hội thoại và 21.645 lượt nói; cả 249 chặng đã có hồ sơ rà độc lập còn khớp.

Export của 60 chặng khớp context_vi/speakers/turns của bản thảo. 189 bản thảo trước và phần lộ trình ngoài các hội thoại được giao giữ nguyên. JSON nhúng HTML khớp learner.json; docs/index.html trùng ROADMAP.html. Trình duyệt đã mở đủ 249 chặng ở chiều rộng 1.280 và 390 px, so đủ 5.032 cảnh/21.645 lượt, nhãn vai/giọng/Nhật/Việt; không phát hiện tràn ngang tại hai kích thước đó. Kiểm render không thay thế đánh giá ngôn ngữ.

Mở [preview](../../ROADMAP.html), [tiến độ](PROGRESS.json), [mốc đầu vào và kiểm chứng](RUN.json). Các báo cáo sản xuất ở batches/batch04 giữ nguyên như lịch sử.
