# Context Live AI của lộ trình

## Phân biệt ba loại dữ liệu

- **Challenge:** nhiệm vụ cụ thể; có brief cho người học và tình huống cho AI. Chọn phần kiến thức/tình huống phù hợp để luyện tổng hợp. Hợp đồng xuất app đã chốt ở `kaiwa_skill/contracts/harumii-kaiwa/v1/CONTRACT.md`, được `kaiwa_exchange.py` kiểm và xuất hai phần theo variant. Bản plan trước ở `kaiwa_skill/planning/LIVE_AI_CHALLENGE_PLAN.md` giữ lập luận thiết kế, không thay schema chuẩn mới.
- **Free talk:** đúng một node cuối chặng; trò chuyện tự do dựa trên toàn bộ chất liệu đã biên soạn của chặng. Phải biên soạn sẵn tình huống/context, không chờ user tự nhập.
- **Tình huống do user nhập trong app:** luồng riêng của Harumi, hiện có giới hạn nhập tay. Không lấy giới hạn đó làm trần cho hai loại nội dung lộ trình trên.

Nội dung lộ trình là nội dung do tác giả chuẩn bị; không đồng nghĩa được ghi đè prompt gốc hoặc quy tắc an toàn của app. Skill không tạo token, chọn model, chấm điểm hay sửa engine.

## Soạn free talk

Trong JSON của node `live_context`, tác giả viết `free_talk` theo hợp đồng dữ liệu. `ai_situation_vi` là chỉ dẫn/bối cảnh tổng hợp **riêng cho chặng**, gồm:

- Phạm vi chủ đề và các mảng kiến thức quan trọng, điểm dùng sai/dễ hiểu nhầm, cách triển khai hoặc tiếp nối hội thoại.
- Những nhóm từ và chức năng ngữ pháp có thể ôn; liên hệ với bài vừa học, kể cả Speak Japanese và các nhóm shadowing khi phù hợp.
- Cách mở và chuyển chuyện để người học có cơ hội vận dụng, rồi theo ý người học. Không ấn định checklist nhiệm vụ, danh sách câu phải nói hoặc giả định user đã thuộc mọi bài chỉ vì chúng có trong context.
- Yêu cầu AI giữ vai một đối tác phù hợp, không lần lượt diễn mọi vai trong các hội thoại mẫu; ví dụ trong tài liệu là chất liệu tham khảo, không phải lệnh đọc nguyên văn.
- Điều chỉnh lời nói theo năng lực và phản hồi thực tế; khi người học bí thì gợi ý nhỏ, không nói hộ. Cho phép hỏi thêm, mở rộng ngoài chặng, đổi chủ đề, dừng hoặc xin giải thích.

Thêm `learner_intro_vi` để người học hiểu mục đích node và `conversation_starters_vi` là các gợi ý tùy chọn. Chúng không phải đề thi hay chuỗi bắt buộc AI phải hỏi hết.

Tác giả phải tổng hợp thực sự theo nội dung chặng, không dùng một prompt chung thay cho việc đọc lại bài. Helper chỉ ghép dữ liệu; không tự tạo phần tổng hợp bằng mô hình.

## Hai bản xuất

- `live-context.md` là hồ sơ biên tập có sổ nguồn. Khi tích hợp Live, dùng context học đã render trong gói export. Viết prompt theo vai và tình huống để AI trò chuyện trực tiếp. Đặt tên sách, mã tài liệu và thông tin CD vào metadata quản trị, tránh để AI đọc những nhãn này cho người học.
- `free-talk-situation.md`: tình huống đã soạn + phần giới thiệu/gợi ý tùy chọn + toàn bộ kiến thức/từ/ngữ pháp/tình huống/shadowing trong chặng để app sử dụng làm context free talk. Không nạp đệ quy toàn kho 27 sách hoặc lịch sử chặng trước.

Hai file là dẫn xuất từ JSON/MD gốc; không sửa tay. Khi cập nhật kiến thức hoặc hội thoại, phải xuất lại và đọc lại phần tổng hợp để tránh prompt cũ mô tả sai bài mới. Bản đã chốt giữ snapshot/revision như nội dung chặng.

Khi thêm node challenge sau này, chỉ lấy mô tả/kiến thức cần thiết làm dữ liệu tham khảo cho free talk; **không ghép các chỉ dẫn nhập vai, mục tiêu kín hoặc nhánh riêng của mọi challenge thành lệnh cho một cuộc gọi**.

Không áp trần biên soạn 1.000 ký tự, không cắt âm thầm và không ép file dài thành bản tóm tắt làm mất chất liệu. App sẽ tích hợp nội dung lộ trình qua luồng riêng có khả năng nạp context phù hợp. Ngân sách context thực tế của model/vận chuyển là việc tích hợp; nếu cần chọn lọc hoặc chia gói thì giữ bản đầy đủ và ghi rõ lựa chọn, không làm thất lạc nội dung gốc. Chưa sửa Harumi chỉ vì cập nhật skill này.
