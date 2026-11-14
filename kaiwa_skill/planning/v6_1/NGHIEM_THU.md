# Nghiệm thu phân bổ nguồn V6.1

Đã hoàn tất 289/289 chặng theo ba hàng đợi độc lập, tuần tự. Model worker gpt-6-sol, reasoning high.

80 Sơ, 145 Trung, 64 Thượng. 33 cụm, 1.304 sự kiện và 5.914 tình huống giữ đúng từng hàng V5.

600 lượt bài Speak Japanese và 214 lượt pack độc lập. 246 đơn vị nguồn khác nhau. 814 bản Markdown cục bộ khớp byte với những dòng được chọn ở nguồn clean. Có manifest cho từng chặng và chỉ mục tra từ sách tới chặng.

## Kiểm tra hoàn tất

- Worker đọc trọn đơn vị được chọn, kiểm nguồn và check-one từng decision, tự rà cuối cấp. Root rà mẫu ý nghĩa, ranh giới và các quyết định rỗng.
- Build và verify toàn release. Từng hàng JSON sau khi bỏ đối tượng v6 bằng đúng hàng V5, bao gồm UID, sự kiện, tình huống, thứ tự và liên kết.
- Đối chiếu hash và byte của toàn bộ 814 file trích; số file thực bằng số file kê trong manifest. Các bản copy lỗi thời của lượt thử đã dọn.
- Mỗi bài Speak Japanese có placeholder video liền trước phần shadowing, mỗi pack độc lập một node; bài giảng chặng là placeholder.
- Preview mở offline ở chiều rộng390px, bộ lọc ba cấp, mở mẫu S-001/S-059/T-047/T-065/H-058/T-145, tiêu đề và nội dung nguồn. Những nhãn số nguồn giữ trong quản trị.

## Giới hạn và khoảng trống

Chín chặng đã tìm nhưng chưa chọn nguồn phù hợp: S-012, S-013, S-029, S-030, S-051, S-057, S-076, S-078, T-032. Các tình huống vẫn còn trong lộ trình; sổ tìm nguồn giải thích từng trường hợp.

B01 (5500) đã được xét ở các nhóm có liên quan, nhưng chưa có nhóm được chọn trong release. Đây là kết quả tuyển chọn, có thể tiếp tục bổ sung khi có đơn vị phù hợp. Cả chín sách kiến thức Speak Japanese đều đã có bài được chọn.

CD/track được đối chiếu từ nhãn và metadata nguồn clean. Chưa đối chiếu âm thanh thực tế. Một số phần Mensetsu còn needs_review được để chờ, xem considerations. Số đĩa chưa biết ghi null theo nguồn.

Các chủ đề thủ tục chuyên biệt (xe cộ, pháp lý, bạo lực/quấy rối, cứu trợ sau thiên tai, điều kiện hành chính) có phần chỉ tuyển được cách hỏi/xác nhận/giải thích. Các bài bổ trợ này chưa thay cho bài giảng thực tế hoặc dữ kiện hiện hành sẽ soạn sau.

## Lượt dùng theo sách

- B01: 0
- B05: 89
- B06: 69
- B07: 196
- B08: 194
- B11: 30
- B12: 48
- B13: 17
- B14: 1
- B18: 141
- B19: 11
- B20: 5
- B24: 11
- INTERVIEW: 2
