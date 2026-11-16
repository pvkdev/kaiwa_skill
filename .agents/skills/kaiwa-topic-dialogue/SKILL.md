---
name: kaiwa-topic-dialogue
description: Biên soạn, sửa và nghiệm thu hội thoại mẫu V11 theo từng tình huống trong chặng topic V10, dùng Markdown Kaiwa, nguồn thực tế ở Nhật và chuyên đề liền trước.
---

# Hội thoại mẫu cho chặng topic

Mỗi tình huống V10 nhận một hội thoại có thể mở riêng, nghe toàn bộ, luyện từng câu và đổi vai. Sản phẩm của lượt này là nội dung nói. Bám UID, sự kiện, nhánh và trình tự V10. Các nghiệp vụ làm video, từ vựng, challenge và free talk có luồng riêng.

## Chuẩn bị cho từng chặng

1. Từ gốc repo chạy `py -X utf8 .agents/skills/kaiwa-topic-dialogue/scripts/dialogue.py S-011`, thay mã theo phân công. Đọc mục tiêu chặng, toàn bộ sự kiện, tình huống, quan hệ tiếp nối và phạm vi chặng liên quan. Nhìn trước các nhánh cạnh nhau. Ghi ngắn **ai cần nói gì, người kia biết gì, sau cuộc nói chuyện có gì thay đổi** cho từng cảnh.
2. Tra `kaiwa_skill/planning/catalog27/BOOK_GUIDE.md`, `source_index.jsonl` và `manifest.json`. Tìm bằng chức năng nói, quan hệ và cụm Nhật bên cạnh từ khóa chủ đề. Ví dụ tìm cả “hỏi lại”, 聞き返す và 乗り換え cho chặng tàu. Mở Markdown `book.md` hoặc chương thật trong `kaiwa_skill/knowledge`, đọc cả đoạn trước/sau và lời đáp. B01, role-play, Nama Chūkei, Nameraka, Shadowing và Speak Japanese đều là nguồn tham khảo cho hội thoại. Khi catalog có cờ cần rà, kiểm lại đoạn dùng. Lưu mã sách, tên thật, file, dải dòng và điểm đã dùng. Tra trên phạm vi đủ 27 sách qua chỉ mục, đọc sâu nguồn phù hợp từng chặng. Khi tìm không ra, ghi lại từ khóa và khoảng trống ở nhật ký rồi biên soạn từ các căn cứ còn lại.
3. Đọc bài của chuyên đề gần nhất **đã xuất hiện trước topic ở cùng cấp**. Mở `previous_lesson` và phần luyện V10 liên quan. Ưu tiên các ví dụ đã dẫn đúng `situation_uid` hiện tại trong `practice.json`. Cân nhắc lấy cách mở lời, xác nhận, sắc thái hay cách đáp của bài và phát triển thành cuộc thoại mới. Chỉ ghi `specialty_item_ids` khi cách dùng thực sự thể hiện trong lời thoại. Đầu cấp chưa có chuyên đề thì để mảng rỗng.
4. Điều tra thực tế trên internet theo chặng. Khi dựng cảnh ở ga, bệnh viện, nơi làm việc hay trước quầy dịch vụ, xác định câu nào phụ thuộc chính sách, địa phương, đơn vị, phí, giờ, điều kiện hoặc quyền lợi. Tra nguồn trực tiếp như nhà vận hành, thành phố, bộ ngành hay cơ sở cung cấp dịch vụ. Lưu URL trang cụ thể, ngày đọc, phạm vi áp dụng và dữ kiện đã kiểm. Có thể dùng trải nghiệm cộng đồng để tìm tình huống hoặc từ thường gặp. Đối chiếu thông tin thủ tục với cơ quan phụ trách. Dùng chung nguồn cho nhiều cảnh khi cùng dữ kiện. Khi chưa xác minh được một khẳng định, viết lời nhân vật hỏi nhân viên về trường hợp cụ thể hoặc ghi rõ chỗ chờ kiểm nếu bỏ dữ kiện sẽ sai mục tiêu. Chặng chỉ có giao tiếp xã hội có thể ghi nhận nguồn ngữ dụng trong sách đủ cho cảnh. Tên riêng, tiền và giờ dùng làm ví dụ phải nhất quán trong cùng sự kiện.

## Viết theo nhánh và theo người học

Viết từng sự kiện. Chọn đúng hai vai trong số những người có thể tham gia sự kiện đó. Với sự kiện chuyển đầu mối, chuyển lời qua một vai hoặc đặt cuộc gặp tiếp theo ở tình huống tiếp nối đã có. Ghi bối cảnh Việt đủ để người mở riêng biết mình đang ở đâu, nói với ai và muốn đạt điều gì. Nếu đã xin ở cảnh trước, cảnh sau có thể mở bằng câu trả lời đang chờ. Nhánh bị từ chối phải cho người học cơ hội đáp, hỏi điều kiện hoặc chọn phương án khác. Cảnh thiếu thông tin nên có lượt hỏi đúng chi tiết, rồi dùng được câu trả lời. Giữ cách kết thúc phù hợp kết quả thật của từng cảnh.

- **Sơ.** Ưu tiên câu ngắn, một ý chính, đủ thông tin để người kia trả lời. Có thể tập nghe một câu lịch sự cố định từ nhân viên trong khi lời người học vẫn vừa sức.
- **Trung.** Luyện trình bày hoàn cảnh, kiểm lại điều kiện và thương lượng bước tiếp. Lời đáp phải tác động tới câu kế của người học.
- **Thượng.** Luyện nhận ý ngầm, xử lý quan hệ trong–ngoài, thuyết phục và sửa hiểu lầm. Độ khó có thể nằm ngay ở lựa chọn giữa hai câu ngắn. Với kính ngữ hãy xác định chủ thể hành động, người nghe, người được nhắc tới.

Để dự trù pilot có thể bắt đầu quanh 4–8 lượt ở Sơ, 6–10 ở Trung, 6–12 ở Thượng. Điều chỉnh theo mục tiêu; một trao đổi khẩn cấp có thể kết thúc sau vài lời. Tách lượt theo đơn vị nói mà người học có thể nhắc hoặc thu âm tự nhiên. Đọc nối A–B cả đoạn và thử đứng ở **cả hai vai**. Đổi vai luyện là phát lại cùng kịch bản. Kiểm nhịp ngắt, cách xưng hô và câu cuối. Tránh lặp nguyên câu mở/kết ở mọi nhánh chỉ để đủ lượt. Cụm cố định được phép lặp khi người Nhật thực sự sẽ nói như vậy.

Dịch Việt theo ý, mức lịch sự và quan hệ. Đọc nguyên bản Việt một lần độc lập. Bỏ văn viết, xưng hô mơ hồ, dịch sát chữ làm lệch ý hoặc biến lời lưỡng lự thành cam kết. Tiếng Nhật dành cho hiển thị/TTS, giữ kanji tự nhiên. Mỗi câu nói có hai chuỗi riêng `ja`, `vi`. Nguồn, mã nội bộ và tên level nằm trong dữ liệu quản trị.

Gán `speaker_id` theo người thực sự nói từng lượt. Khi một nhân vật nói hai lượt liên tiếp, cả hai lượt giữ cùng vai. Nếu dùng script để đóng gói bản thảo, giữ vai đã biên tập cùng câu thay vì suy ra vai từ vị trí chẵn/lẻ. Trong lượt rà đổi vai, đối chiếu từng câu với tên vai và giới tính được xuất cho TTS.

Khi đọc lại, kiểm tra những gì mỗi người thực sự biết tại lượt đang nói. “Đã chuyển tài liệu” chỉ xác nhận việc chuyển; cần có thông tin người nhận đã xem trước khi suy ra họ đã đọc. Trong cuộc thoại có chuyển lời hoặc đổi quan hệ nội bộ–đối ngoại, rà kính ngữ của cả hai nhân vật. Nếu cảnh hỏi giá, lịch hoặc điều kiện, cho người học nhận đủ câu trả lời để thực hiện bước của cảnh đó. Có thể dùng mức giá hay giờ giả định được ghi rõ trong bối cảnh. Cảnh đang chờ trả lời cần chốt đầu mối hoặc cách hỏi lại. Giữ địa bàn và dịch vụ thực tế trong bối cảnh để học viên hiểu phạm vi của lời nhân viên.

## Dữ liệu, checkpoint và nghiệm thu

Đọc [hợp đồng bản thảo](references/draft.md) khi tạo hoặc sửa file. Mỗi chặng có một worker sở hữu. Lưu bản thảo và tiến độ sau từng sự kiện, ghi UID đã soạn, UID đã rà, dấu vân tay của đầu vào, điều còn nghi ngờ và việc tiếp theo. Ghi vào file tạm rồi thay thế nguyên tử. Khi phục hồi, mở lại file, so đầu vào, giữ phần đã duyệt và rà lại các cảnh phụ thuộc đoạn nguồn vừa đổi. Lệnh `--check` dùng cho chặng đã soạn đủ.

### Ba lượt rà trước khi duyệt hội thoại

1. **Đúng việc, đúng vai.** Mở riêng từng cảnh. Từ tên cảnh và nhánh, xác định người học cần làm gì. Chỉ đúng lượt họ tự làm việc ấy và lượt người kia đáp. Rồi đọc cảnh tiền nhiệm theo `continues_from`. Nếu cảnh trước đã làm xong việc đích, hoặc người đối diện nói thay, điều chỉnh điểm kết của cảnh trước và điểm mở của cảnh sau. Ví dụ, cảnh đầu có thể xác lập rằng chưa hỏi ý kiến Tổng vụ. Ở cảnh kế, chính người học đề nghị hoãn quyết định để đi hỏi. Bối cảnh chỉ cung cấp điều nhân vật đã biết.
2. **Đúng mạch, đúng nghĩa.** Đọc liền câu hỏi và câu đáp bằng tiếng Nhật, rồi đọc riêng bản Việt như một cuộc nói chuyện. Đối chiếu các từ nhỏ có thể đổi quyết định: tiền và giờ có tính cả mốc hay không, ai được phép làm, khi nào, phủ định, độ chắc chắn và tình trạng phê duyệt. Nếu nhân vật hỏi nghĩa một từ, giữ từ đang hỏi trong lời dịch để lượt đáp giải thích. Sau mỗi lần sửa, đọc lại lượt trước, lượt sau và cảnh tiếp nối dùng thông tin vừa đổi. Với dữ kiện thực tế, giữ đúng điều kiện và phạm vi của nguồn.
3. **Nói được cả hai vai, phân biệt được các nhánh.** Nhập vai người nhận và tự trả lời: nghe câu này, tôi hiểu điều gì vừa được đồng ý, ai sẽ làm gì tiếp? So cách hiểu ấy với ý định của người nói trong cả Nhật và Việt. Chẳng hạn, khi khách hoãn mua, lời đáp của cửa hàng cần cho khách hiểu họ có thể quay lại hỏi tiếp. Đổi vai, nói thử cả đoạn ở độ dài vừa sức rồi đọc liền các cảnh cùng sự kiện. Giữ những câu cố định dùng tự nhiên. Khi một câu hỏi chỉ lặp lại điều vừa được trả lời, cho người học hỏi tiếp chi tiết còn thiếu. Số lượt hay tần suất một từ là tín hiệu để mở cảnh đọc lại.

Trong hồ sơ nội bộ của chặng, ghi một dòng cho mỗi UID cảnh đã rà, gồm vai/lượt làm việc đích, kết quả và điểm đáng lưu ý sau khi đối chiếu hai ngôn ngữ và tập đổi vai. Nếu một bước còn vướng, ghi UID lượt cần sửa và giữ cảnh ở `needs_fix`. Gắn trạng thái duyệt với đúng bản văn đã đọc theo [hợp đồng bản thảo](references/draft.md). Với cảnh y tế, pháp lý, bạo lực hay quyền lợi, rà từng khẳng định có thể tác động quyết định ngoài đời.

Điều phối mở HTML chứa đúng JSON pilot và thử đi theo thứ tự tình huống trên PC/mobile, kiểm cả hai vai, `ja` và `vi`, và việc ẩn metadata nguồn. Sửa một lượt rồi dựng lại để kiểm ID ổn định. Khi chỉnh sau nghiệm thu, giữ UID của cảnh/lượt còn cùng nghĩa, thêm ID mới cho lượt mới, cập nhật nhật ký và kiểm lại. Ba pilot kết thúc bằng preview riêng, báo cáo QA và số liệu thực đo để người dùng quyết định bước hàng loạt.
