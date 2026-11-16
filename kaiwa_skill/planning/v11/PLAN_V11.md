# V11 · Hội thoại để luyện nói trong từng tình huống

## Phạm vi đã kiểm trên V10

Lộ trình hiện có 365 chặng. V11 bổ sung hội thoại cho **6.004 tình huống thuộc 293 chặng topic**. Sơ có 81 chặng với 1.433 tình huống, Trung có 148 chặng với 3.039 tình huống, Thượng có 64 chặng với 1.532 tình huống. 72 chuyên đề với 322 bài là học liệu người soạn có thể dùng để gối đầu. Giữ UID và thứ tự học hiện tại để mỗi hội thoại gắn đúng vào tình huống mà người học chọn.

## Đơn vị sản xuất

1. **Đọc theo chặng.** Đọc hết các sự kiện và nhánh trước khi viết. Với mỗi cảnh, chốt người nói, quan hệ, việc cần giải quyết, chi tiết người học phải nghe và kết quả cần đạt. So các cảnh sát nhau để lời thoại bộc lộ được sự khác nhau.
2. **Tìm chất liệu.** Dùng chỉ mục 27 sách để tìm theo ngữ cảnh và hành vi giao tiếp. Mở đoạn Markdown gốc để xem người ta dẫn vào câu nói thế nào và đối phương trả lời ra sao. Tra bài và ví dụ đã học ở chuyên đề ngay trước. Chọn chi tiết có thể dùng tự nhiên. Ghi căn cứ một lần rồi dùng lại cho các nhánh trong cùng sự kiện.
3. **Kiểm thực tế.** Câu nào phụ thuộc quy định, dịch vụ hay địa phương thì đối chiếu trang của đơn vị chịu trách nhiệm, ghi rõ địa bàn và ngày tra. Ví dụ, ở quầy gửi hàng cần phân biệt điều nhân viên được quyền xác nhận với điều khách phải hỏi lại. Với cảnh có rủi ro, reviewer mở nguồn và kiểm lại từng khẳng định ảnh hưởng đến hành động của người học.
4. **Viết và đọc thành tiếng theo sự kiện.** Dùng tiếng Nhật người trong hai vai thực sự sẽ nói, chọn độ dài vừa với hơi nói và trình độ. Dịch riêng từng lượt, rồi đọc lại cả đoạn tiếng Việt để sửa xưng hô, hàm ý và những câu dịch đúng chữ nhưng khó hiểu. AI có thể viết mới lượt hỏi, đáp và diễn tiến, ghi rõ ở tầng quản trị phần trích, phần chuyển soạn và phần viết mới.
5. **Lưu và rà.** Một người viết sở hữu một chặng tại một thời điểm. Mỗi sự kiện có checkpoint riêng. Reviewer thứ hai đọc từng cuộc thoại trong bối cảnh và đối chiếu các nhánh gần nhau. Trả về đúng UID cảnh/lượt cần sửa. Lưu phiên bản nguồn để khi sửa nguồn hoặc phục hồi sau gián đoạn chỉ cần rà lại phần bị ảnh hưởng.
6. **Dựng preview từ JSON.** Nối bằng UID vào đúng tình huống V10. Mỗi lượt có hai trường `ja`, `vi` và tham chiếu vai có `gender: male | female`. Preview và bản xuất dùng chung dữ liệu người học. Mã sách, nguồn, ghi chú biên tập và lịch sử thay đổi nằm ở phần quản trị. [Hợp đồng bản thảo và bản xuất](../../../.agents/skills/kaiwa-topic-dialogue/references/draft.md)

## Pilot đề xuất khi có lệnh

- **S-011 · Tàu điện & xe buýt** — 15 tình huống. Kiểm tra người mới có thể hỏi, nghe và xác nhận đúng thông tin không. Đọc kỹ những cảnh khác nhau giữa các tuyến, giữa lời nhân viên và lời khách. Chuyên đề gần trước là `sj-so-03`.
- **T-044 · Gửi bưu kiện cá nhân và hỏi hàng quốc tế** — 25 tình huống. Kiểm tra cách hỏi điều kiện, đổi phương án và chốt bước tiếp theo. Đặc biệt rà điều kiện của từng dịch vụ và tránh để người học hiểu một ví dụ thành quy định chung. Chuyên đề gần trước là `sj-trung-11`.
- **H-004 · Kính ngữ đối ngoại & chuyển lời xã giao** — 15 tình huống. Kiểm tra đúng vai trong–ngoài, chủ thể của hành động và sắc thái tiếng Việt khi giới thiệu, chuyển lời, nhận lời hoặc khước từ. Chuyên đề gần trước là `sj-thuong-01`.

Ba pilot thử tổng cộng **55 hội thoại**. Khi được duyệt chạy, cho mỗi người soạn phụ trách một cấp. Điều phối kiểm tra độc lập nội dung cả ba chặng và đối chiếu kết quả trên HTML. Bàn giao bản thảo theo chặng, preview, nhật ký nguồn, danh sách lỗi đã sửa và những điểm còn cần chủ dự án quyết định.

## Quyết định trước khi nhân rộng

- Kiểm đủ 55 UID theo thứ tự, đúng hai vai và giọng TTS, đủ hai ngôn ngữ, liên kết nguồn và bài chuyên đề có thật. Đọc lại cả 55 đoạn từ đầu tới cuối. Chỉ chấp nhận cảnh khi người học luyện được việc nêu trong tiêu đề và kết quả đúng nhánh. Các lỗi sai vai, sai nghĩa, sai dữ kiện và trùng kịch bản phải được sửa và đọc lại.
- Thử đổi vai, hiển thị Nhật–Việt trên PC/mobile và sửa một cảnh rồi dựng lại. Thử dừng sau một sự kiện và tiếp tục từ checkpoint. Đối chiếu UID, nội dung đã duyệt và số cảnh để phát hiện mất hoặc nhân đôi dữ liệu.
- Đo riêng thời gian tra cứu, soạn và review ở mỗi cấp. Ghi token thực nếu công cụ cung cấp. Ước lượng lượt hàng loạt theo số cảnh từng cấp và độ phức tạp nguồn, nêu độ bất định vì mới đo một chặng mỗi cấp. Dùng kết quả pilot để điều chỉnh skill và chốt hợp đồng xuất.
- Sau khi người dùng duyệt pilot, chạy từng chặng theo thứ tự trong mỗi cấp. Đo tiến độ bằng số tình huống đã qua review. Trước phát hành, kiểm toàn bộ 6.004 UID, trùng kịch bản xuyên chặng, dữ kiện dùng lại ở nhiều nơi và đường đi từ preview tới từng cảnh. Giữ bản V10 để đối chiếu.

[Skill soạn và nghiệm thu hội thoại V11](../../../.agents/skills/kaiwa-topic-dialogue/SKILL.md)
