# Mong muốn của chủ dự án trước khi dựng Kaiwa V6

Ghi ngày 14 tháng 11 năm 2026, trước khi sửa skill và chạy pilot. Đây là mốc đối chiếu yêu cầu. Các quyết định phân bổ cụ thể sẽ được lưu riêng để sau này có thể đổi một chặng mà vẫn xem được ý định ban đầu.

## Mục đích và đường học

“Bạn chỉ giỏi kaiwa khi bạn nói đủ nhiều”. Người Việt mở Harumii để luyện nghe, nói, phát âm và phản xạ trong đời sống ở Nhật, trong quan hệ cá nhân và công việc. Kết hợp nhiều giáo trình thành một lộ trình tự học. Ưu tiên chất lượng, độ sâu, tiếng Nhật tự nhiên, tiếng Việt dễ hiểu và khả năng vận dụng thực tế. Người học có quyền tự chọn bài. App đã có engine từ vựng, phát âm, đổi vai và Live AI. Dự án chuẩn bị lộ trình, nội dung và gói dữ liệu dễ migration. Đánh giá nội bộ dành cho tác giả, không thêm bài thi, chấm điểm hay cổng mở khóa cho người học.

Giữ V5 với 289 chặng, 80 Sơ, 145 Trung, 64 Thượng, 33 cụm, 1.304 sự kiện, 5.914 tình huống. Giữ UID, tiêu đề, thứ tự, cấp độ, sự kiện, diễn biến, kết quả, cuộc nói tiếp theo và các liên kết. Cùng một topic có thể quay lại ở cấp khác khi quan hệ, cách nói hoặc nhiệm vụ khác. Tập trung hội thoại. Giấy tờ là đối tượng trao đổi khi phù hợp. Mục lục web và memo bổ trợ cho kho sách. Nguồn ngoài và ví dụ AI viết mới là thành phần thực sự của dự án, có xuất xứ rõ ràng.

## Thứ tự một chặng

1. Xem các nhóm từ vựng theo topic. Phạm vi đủ rộng để người học tự nói về hoàn cảnh của mình, gồm từ dùng trong challenge và free talk. Ví dụ thực phẩm có món, đồ uống, rau, củ, trái cây, vị và cách chế biến. Có thể chia nhóm theo tình huống. Dùng từ điển cho động từ và dạng cơ bản cho tính từ. Khi soạn nội dung chỉ xuất danh sách từ Nhật cho engine. Hội thoại giúp rà từ còn thiếu và gợi lại từ cũ.
2. Xem video kiến thức Speak Japanese khi chọn được bài phù hợp.
3. Shadowing đúng ví dụ của bài đó ngay sau video. Có nhiều bài thì xếp thành nhiều cặp độc lập theo mạch học.
4. Luyện các pack shadowing độc lập phù hợp với topic. Một pack thành một node riêng.
5. Xem video kiến thức tổng hợp chuẩn bị cho toàn bộ tình huống của chặng. Giảng cách đối ứng, trình tự nói, nghe ra ý gì, ngữ pháp cần dùng, ví dụ Nhật–Việt, mẹo và dữ kiện thực tế. Ngữ pháp được giải thích ngắn ngay chỗ dùng, tên chuẩn Minna/bunpou và JLPT có thể lưu cho admin. Bản đọc và tài liệu tạo video NotebookLM dùng chung nội dung. Thiết kế chi tiết hai skill bài giảng Speak Japanese và bài giảng chặng sẽ bàn sau.
6. Thực hành các tình huống đa dạng. Mỗi tình huống có hội thoại hai vai, bản dịch Việt và hai chế độ app hỗ trợ (shadowing toàn tình huống và đổi vai). Kiến thức, từ và ngữ pháp bài trước có thể gối đầu tự nhiên khi viết ví dụ mới.
7. Một hoặc nhiều challenge Live AI. Mỗi challenge là một cuộc trao đổi duy nhất với một vai, một bối cảnh và nhóm nhiệm vụ cụ thể có thể kết hợp nhiều tình huống đã học. Có brief/gợi ý cho người học và tình huống riêng cho AI, không có menu chọn nhánh trong challenge. Thiết kế nhiệm vụ sau khi đã soạn xong các tình huống.
8. Một free Kaiwa cuối chặng, có context tổng hợp để AI trò chuyện tự do, mở rộng theo người học. Giới hạn 1.000 ký tự của ô user nhập không áp dụng cho context biên soạn sẵn.

## Tuyển và tái dùng nguồn

- Cả 27 sách clean đều dùng để tra cứu hội thoại, tình huống, ví dụ, lời giảng và context. Nama Chūkei (B25–B27) và Nameraka (B09) đặc biệt hữu ích. Chỉ giới hạn nguồn cho các node shadowing lấy trực tiếp từ sách. Ba cuốn từ vựng riêng chỉ để tham chiếu.
- Speak Japanese gồm B05, B06, B07, B08, B11, B12, B18, B19, B20, B24. Chín cuốn ngoài B08 dùng cho các cặp bài kiến thức và shadowing ví dụ của bài. Giữ mạch, độ sâu, cách dùng và ví dụ nguyên gốc. B08 必須700 dùng cho shadowing theo topic. B05 接客…決まり文句700 là cuốn khác.
- Nguồn shadowing độc lập gồm B01 (5500, chọn nhóm cùng mục đích), B08 (必須700), B13 và B14. Thêm sách phỏng vấn 就職・アルバイト・進学面接編 khi đủ căn cứ về đơn vị bài và pack. Có ba hướng riêng là baito, tuyển sinh và tuyển dụng.
- Topic, tình huống, vai và việc người học cần nói quyết định tập ứng viên trước. Sau đó đọc toàn bài/pack để xét độ vừa sức. B07/B11 gợi ý từ cuối Sơ đến đầu Trung, B06/B12 từ cuối Trung lên Thượng. Các sách mọi cấp xét từng bài. Dải trên chỉ để tham khảo; thứ tự trong sách cũng không quyết định thứ tự chặng.
- Một chặng có thể có nhiều bài Speak Japanese **và** nhiều pack shadowing. Chủ động tìm thêm những bài bổ sung được cách nói hoặc vai mới. Ưu tiên khai thác phong phú bộ Speak Japanese. Cùng một bài hoặc pack có thể dùng lại trọn vẹn ở Sơ, Trung, Thượng nếu phù hợp. Có thể dẫn ôn khi đáng làm, không ép một nguồn chỉ có một chặng chính. Không đặt KPI phải dùng hết tài nguyên hoặc bắt chặng nào cũng có pack.
- Một pack audio nguyên vẹn nằm trong một node, giữ mọi track và lượt đúng thứ tự và nguyên văn tiếng Nhật để tra được CD. Khi một vài câu hợp mà trọn pack lệch topic, tìm pack khác. Câu AI viết mới hoặc chuyển soạn ghi khác câu trích nguyên văn. Nguồn sách không có file nghe đã kiểm thì chỉ ghi dấu CD/track thật sự có bằng chứng.
- Metadata admin có mã nguồn, mã và **tên sách đầy đủ**, bài/chương, anchor hoặc trang, pack, CD/track nếu biết, lý do gán và các tình huống liên quan. Lưu lại khi một nguồn được dùng ở nhiều cấp. Có chỉ mục ngược từ sách tới chặng và trạng thái đã xem/chưa xem. Tên sách, mã Bxx, CD và tên cấp không xuất hiện trong lời bài, bản dịch hay gợi ý người học. Câu Nhật có nghĩa Việt và không cần furigana.
- Nghiên cứu ngoài và AI có thể bổ sung tình huống và lời giảng sau này. Kiểm thông tin nhạy theo địa phương/thời điểm, phân biệt căn cứ nguồn với tình huống giả định. Phạm vi hiện tại là phân bổ nguồn có thật vào V5.

## Điểm dừng và phiên bản

V6.0 gồm hai skill (điều phối lộ trình, phân bổ bài/pack), cập nhật điểm vào skill nội dung, khung nguyên V5 và pilot có thể mở xem. Ghi rõ đã duyệt nguồn không đồng nghĩa đã sản xuất bài giảng, video, hội thoại hay challenge. Các chặng ngoài pilot hiển thị chưa phân bổ. Giữ sáu pilot cũ để đối chiếu. Dữ liệu chuẩn có thể sinh lại bản đọc, preview và chỉ mục. Có checkpoint theo chặng/đơn vị, kiểm được trùng và hỗ trợ thay một quyết định có lịch sử.

**Dừng sau khi pilot chạy và kiểm thành công để chủ dự án xem.** V6.1 dành cho đợt gán Speak Japanese và shadowing toàn lộ trình, với chat chính điều phối ba sub Sol/high sau lệnh riêng. Số lượng nguồn đã đọc và số chưa xét phải được báo trung thực. Lượt V6.0 không phát hành V6.1 hay tự chuyển toàn hệ thống sản xuất sang bản pilot.
