# V6.1 đang phân bổ nguồn

Chủ dự án cho lệnh chạy ngày 14 tháng 11 năm 2026, mỗi sub sở hữu một cấp, đi tuần tự theo thứ tự chặng. Điều phối root, ba worker gpt-6-sol/high. Giữ 289 chặng và toàn bộ cấu trúc V5.

- v61_so dùng QUEUE_so.json, 80 chặng.
- v61_trung dùng QUEUE_trung.json, 145 chặng.
- v61_thuong dùng QUEUE_thuong.json, 64 chặng.

Ba pilot S-059, T-012, H-050 được kế thừa. Trong từng queue, kiểm file decisions tồn tại bằng check-one trước khi bỏ qua. Một file đã validate là một checkpoint. Khi khôi phục, xác nhận worker cũ đã dừng, tiếp chặng đầu chưa có quyết định hợp lệ. Không bỏ qua chặng giữa queue mà không ghi lý do.

Mỗi shell dùng $env:KAIWA_ROADMAP_DIR='D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v6_1'. Điều phối chạy tools/roadmap_v6.py build và verify để sinh các MD nguồn, manifest từng chặng, bản đọc cấp, HTML và tra sách. STATUS.json phản ánh thời điểm lần build gần nhất. Số chặng đang làm xem trực tiếp thư mục decisions hoặc checkpoint riêng của worker.

Nguồn và nội dung V5 chỉ đọc. Chưa viết bài giảng, hội thoại mới, challenge. Tên bài gốc và prefix đánh số nội bộ được lưu riêng. App preview bỏ prefix khi hiển thị. Giữ đủ bài/pack và các track. Một nguồn được tái dùng trong nhiều chặng hoặc cấp khi có ích.

Sau đủ 289 quyết định, kiểm toàn bộ bằng chứng/hashes, ranh giới pack đồng nhất, tiêu đề, các trường hợp rỗng, bản JSON đúng nguyên V5, và đọc preview. Commit quyết định và bản xuất riêng với skill. Chỉ phát hành con trỏ sau nghiệm thu.
