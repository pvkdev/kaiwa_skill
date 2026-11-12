# Thiết kế V3 — biên soạn nội dung chặng Kaiwa

Trạng thái: đã viết skill và hợp đồng dữ liệu nháp để dùng thử; chưa biên soạn hàng loạt 194 chặng. V3 thay phần thiết kế bài học trong V2 theo yêu cầu mới của người dùng. Giữ nguyên các danh sách V4.1 và V2 để đối chiếu lịch sử.

## Quyết định phạm vi

Skill tạo **nội dung**. App lo học từ vựng, phát audio, shadowing toàn tình huống, shadowing chia vai rồi đổi vai, Live AI. Không thiết kế điểm phát âm, đánh giá người học, bài kiểm tra, khóa bài, số buổi hay thời lượng bắt buộc. Người học chọn tự do.

Chặng có một chủ đề lớn, nhiều cụm sự kiện; trong đó xen kẽ kiến thức, danh sách từ, tên ngữ pháp và nhiều tình huống hội thoại. Không có công thức bảy bước áp cho mọi chặng. Mỗi cấp có thể quay lại cùng chủ đề, nhưng khác phạm vi việc cần làm, quan hệ và độ phức tạp của cuộc trao đổi.

## Nội dung của một chặng

- **Kiến thức:** Markdown dễ hiểu bằng tiếng Việt, ví dụ Nhật có nghĩa Việt. Giữ chiều sâu đặc trưng của sách: cách nói tự nhiên, phản hồi, cách triển khai câu chuyện, lịch sự, văn hóa, giải thích sắc thái. Không ép mọi bài vào một format hoặc giới hạn chữ.
- **Từ vựng:** một hoặc nhiều danh sách tùy phạm vi: cả chặng, một sự kiện, một cụm hoặc từng tình huống. Chỉ dữ liệu từ/đọc/nghĩa; app tự xây bài luyện.
- **Ngữ pháp:** tên mẫu cần dùng và tham chiếu Minna/bunpou, không viết lại cả kho bunpou. Có thể không có node riêng nếu không cần mẫu mới. Chưa có bài bunpou thì vẫn giữ tên và tham chiếu chờ bổ sung, không khóa học.
- **Tình huống:** bối cảnh, mục đích giao tiếp, hai vai và hội thoại Nhật–Việt từng lượt. Một dữ liệu dùng cho cả hai chế độ shadowing. Không tách R1/R2/R3, không tạo bài thi đóng vai.
- **Live AI:** đúng một node cho cả chặng. Có danh mục và bản xuất toàn bộ kiến thức, từ vựng, ngữ pháp, tình huống của chặng; thêm hướng mở rộng tùy chọn. Không thay context bằng bản tóm tắt quá ngắn. App quyết định cách nạp context và tương tác.

Ví dụ mạch nội dung **chỉ minh họa cấu trúc**: kiến thức xin phép → nhóm từ lịch/phòng → tên mẫu cần dùng → xin phòng và được đồng ý → kiến thức đáp lại khi bị từ chối → bị từ chối và tìm phòng khác → được dùng với điều kiện → xác nhận lại điều kiện → Live AI. Các sự kiện khác trong cùng topic tiếp tục có cụm riêng. Không bắt mọi topic đều có đúng các nhánh này.

## Tình huống phải rộng và có diễn biến

Cùng một sự kiện xin phép có thể tách thành được đồng ý, bị từ chối, được đồng ý có điều kiện, cần chờ người có quyền quyết định. Mỗi nhánh có hội thoại riêng xử lý hệ quả của phản hồi. Chỉ đổi tên người hoặc món ăn không đủ để tính thêm một tình huống.

Trước khi viết, tác giả dừng ở từng topic để tìm nguồn và suy nghĩ về trước/trong/sau sự kiện, vai và quan hệ, kết quả, hiểu nhầm, sửa lời và phương án khác. Không đặt chỉ tiêu 8–12 cho mọi chặng; cần đủ rộng cho chủ đề và ghi rõ góc còn thiếu. Chất lượng được đánh giá bằng nội dung đã viết và nguồn thực đọc, không bằng số node.

## Một lộ trình dùng chung 27 sách

Hạt giống V4.1 là danh sách định hướng. Chặng mới phải tra lại kho sách, không giới hạn trong vài token đã gắn. Quét chỉ mục 27 cuốn để tìm chất liệu, đọc sâu phần liên quan, phối hợp theo chức năng:

- 5500 và các ngân hàng cách nói mở rộng phản hồi, bối cảnh và lựa chọn.
- Roleplay, business, kính ngữ cung cấp quan hệ, nhiệm vụ và tiến trình giao tiếp.
- Speak Japanese hỗ trợ mẫu/cấu trúc diễn đạt trong kiến thức và hội thoại.
- Shadowing hỗ trợ nhịp thoại, câu đáp, khẩu ngữ; mọi đoạn kaiwa của chặng đều luyện được bằng engine app.
- Nama Chuukei hỗ trợ nghe ý định, xác nhận, hỏi lại và phản hồi theo thông tin thực nghe được.
- Tượng thanh, quán ngữ, cảm xúc, rút gọn đi vào tình huống phù hợp như chất liệu ngôn ngữ.
- Memo web giúp phát hiện chủ đề/góc mới; mục lục không được coi là nguồn nguyên văn cho hội thoại.

Tận dụng tất cả sách trên toàn lộ trình, không nhét mọi sách vào mỗi chặng. Theo dõi đóng góp thật ở `sources.json`; phân biệt đã đọc, mới thấy chỉ mục, chuyển soạn và viết mở rộng. Ghi CD/track khi có bằng chứng nhưng không gắn audio cũ vào lời đã viết lại.

## Ngữ pháp N5–N4 / Minna

Đã lập [danh sách tên ngữ pháp 50 bài Minna sơ cấp](../../reference/grammar/MINNA_01_50_GRAMMAR.md), có JSON để tra theo bài. Dùng syllabus chính thức bản 2 và giáo án theo bài để đối chiếu tên mẫu. Không gọi đây là danh sách JLPT N5/N4 chính thức: JLPT không công bố danh mục ngữ pháp hiện hành theo cấp.

Tại lúc kiểm tra kho: bunpou có metadata N3/N2/N1, chưa có metadata bài N5/N4. Không ghi vào bunpou trong task này. Danh sách Minna là đầu vào để bổ sung bunpou sau; khi có bài thật mới gắn ID. Nhãn sơ/trung/thượng của chặng và nhãn JLPT không quy đổi một-một.

## Bền vững khi chạy dài và khi nâng cấp

Mỗi chặng dùng UUID trong registry. Mỗi node, tình huống và lượt nói giữ ID trong các lần sửa; mã S/T/H là mã hiển thị. Bản làm việc riêng từng lượt, có checkpoint ghi việc đã làm, việc tiếp theo, hash nội dung và nguồn tham chiếu. Một chặng chỉ có một lượt chủ sở hữu.

Pause lưu công việc. Resume kiểm hash để phát hiện thay đổi ngoài lượt; recovery tạo draft kế thừa riêng và giữ draft cũ. Revision đã chốt là snapshot không sửa tại chỗ; nâng cấp tạo lượt mới từ revision đó, sửa đúng phạm vi, tái xuất context, giữ lịch sử. Chỉ chuyển con trỏ `current.json` sau khi snapshot và kiểm tra cấu trúc thành công. Không cần một DB từ vựng toàn cục hay nhiều worker cùng ghi file nội dung chung.

Helper thực thi: `.agents/skills/kaiwa-stage-content/scripts/stage_work.py`. Cấu trúc chi tiết và giới hạn vận hành nằm trong [skill](../../../.agents/skills/kaiwa-stage-content/SKILL.md) và tài liệu checkpoint đi kèm. Kiểm tra của helper là kiểm tra biên tập/dữ liệu, không phải test trong app.

## Cách triển khai tiếp

1. Chọn ba chặng đại diện: một đời sống sơ cấp, một công việc trung cấp có nhánh từ chối/điều kiện, một thượng cấp có sắc thái và triển khai ý. Viết chậm, đủ sâu rồi người dùng xem chất lượng và độ tiện import.
2. Điều chỉnh hợp đồng dữ liệu sau pilot; không chốt cứng schema vì chưa biết đủ dạng nội dung thực tế.
3. Khi được giao chạy hàng loạt, làm từng chặng, checkpoint đều đặn. Tổng hợp độ bao phủ nguồn từ các revision đã chốt để tìm cuốn/góc còn ít được tận dụng.
4. Khi yêu cầu nâng cấp một chặng, đọc revision và sổ biên tập trước, bổ sung có mục tiêu; không tái sinh cả lộ trình.

Các vấn đề nguồn V4.1 đã phát hiện vẫn cần đối chiếu nội dung khi nhận chặng: token STAGE thiếu số bài, nhãn xin nghỉ gắn cảnh xin phòng, nguồn học thuật và nhãn y tế/chuyển nhà chưa chắc đúng. Skill không coi `fact_check` hoặc `kind: book` của hạt giống là chứng nhận ngữ nghĩa.
