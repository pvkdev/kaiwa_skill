# Thiết kế V3.1 — biên soạn chặng có gối đầu và bài shadowing

Trạng thái: cập nhật skill và hợp đồng nháp theo feedback về gối đầu, Speak Japanese và bài shadowing; chưa chạy pilot hoặc biên soạn hàng loạt. V3.1 tiếp tục thay phần thiết kế bài học V2, giữ khung 194 chặng V4.1 đã sửa nguồn. Tên file giữ V3 để các liên kết cũ vẫn dùng được.

## Quyết định phạm vi

Skill tạo **nội dung**. App lo học từ vựng, phát audio, shadowing toàn tình huống, shadowing chia vai rồi đổi vai, Live AI. Không thiết kế điểm phát âm, đánh giá người học, bài kiểm tra, khóa bài, số buổi hay thời lượng bắt buộc. Người học chọn tự do.

Chặng có một chủ đề lớn, nhiều cụm sự kiện; trong đó xen kẽ kiến thức, danh sách từ, tên ngữ pháp và nhiều tình huống hội thoại. Không có công thức bảy bước áp cho mọi chặng. Mỗi cấp có thể quay lại cùng chủ đề, nhưng khác phạm vi việc cần làm, quan hệ và độ phức tạp của cuộc trao đổi.

## Bài sau gối đầu bài trước

Một bài là nhóm node cùng mục đích. Một bài Speak Japanese gồm phần kiến thức dành cho video và shadowing ví dụ đi ngay sau; từ/ngữ pháp chuẩn bị có thể đặt trước cặp. Thứ tự bài theo các node trong chặng và thứ tự chặng V4.1, xuyên qua cả ba level.

Trước bài 3, skill đọc lại bài 1/2; trước các bài tiếp, bắt đầu từ hai bài gần nhất và tìm thêm bài cũ liên quan. Từ nội dung đã có, chọn kiến thức, từ/cách nói và ngữ pháp hợp cảnh để dùng trong ví dụ, hội thoại và danh sách từ mới. Không bắt nhồi mọi điều cũ vào mỗi bài; không giả vờ mẫu/từ chưa được biên soạn là đã học. Phần mới của mỗi bài vẫn rõ.

`learning-map.json` ghi tóm tắt điều mới, các bài trước đã tham khảo, phần thực sự được dùng lại và vị trí tái xuất hiện. Ví dụ: bài 1 giới thiệu từ món ăn, bài 2 cách nhận xét; bài 3 xin gợi ý món sử dụng lại một số tên món và cách nhận xét trong một trao đổi mới. Đây là minh họa nguyên tắc, chưa phải ba bài đã biên soạn. Các ví dụ Speak Japanese cũng áp dụng như vậy.

Nếu pilot rời hoặc bài trước chưa có, ghi pending và tiếp phần có thể làm; không bịa lịch sử. Khi nâng cấp bài cũ, giữ ID, tìm các tham chiếu ở bài sau để xem lại đúng phần ảnh hưởng. Quan hệ này là ghi chép của tác giả, không là khóa truy cập hay yêu cầu người học phải học đủ bài trước.

## Nội dung của một chặng

- **Kiến thức:** Markdown dễ hiểu bằng tiếng Việt, ví dụ Nhật có nghĩa Việt. Giữ chiều sâu đặc trưng của sách: cách nói tự nhiên, phản hồi, cách triển khai câu chuyện, lịch sự, văn hóa, giải thích sắc thái. Không ép mọi bài vào một format hoặc giới hạn chữ.
- **Từ vựng:** một hoặc nhiều danh sách theo chặng/bài/cụm tình huống, đủ các nhóm từ cần thiết của miền chủ đề chứ không chỉ từ trong đoạn thoại. Ví dụ ăn uống gồm món, nguyên liệu, đồ uống, vị, khẩu phần, thao tác theo phạm vi chặng. Đánh dấu mới/ôn; từ ôn dẫn về item đã học và được dùng lại trong câu/hội thoại mới. App tự xây bài luyện.
- **Ngữ pháp:** tên mẫu cần dùng và tham chiếu Minna/bunpou, không viết lại cả kho bunpou. Có thể không có node riêng nếu không cần mẫu mới. Chưa có bài bunpou thì vẫn giữ tên và tham chiếu chờ bổ sung, không khóa học.
- **Tình huống:** bối cảnh, mục đích giao tiếp, hai vai và hội thoại Nhật–Việt từng lượt. Một dữ liệu dùng cho cả hai chế độ shadowing. Không tách R1/R2/R3, không tạo bài thi đóng vai.
- **Shadowing:** node bài luyện gồm câu mẫu, hội thoại mini hoặc tham chiếu tình huống có sẵn. Câu đơn không cần bịa hai vai; giữ nhóm có chủ đề/mục đích rõ. Node này đưa các nguồn luyện nói thành nội dung luyện thực tế.
- **Live AI:** đúng một node cho cả chặng. Có danh mục và bản xuất toàn bộ kiến thức, từ vựng, ngữ pháp, tình huống của chặng; thêm hướng mở rộng tùy chọn. Không thay context bằng bản tóm tắt quá ngắn. App quyết định cách nạp context và tương tác.

Ví dụ mạch nội dung **chỉ minh họa cấu trúc**: kiến thức xin phép → nhóm từ lịch/phòng → tên mẫu cần dùng → xin phòng và được đồng ý → kiến thức đáp lại khi bị từ chối → bị từ chối và tìm phòng khác → được dùng với điều kiện → xác nhận lại điều kiện → Live AI. Các sự kiện khác trong cùng topic tiếp tục có cụm riêng. Không bắt mọi topic đều có đúng các nhánh này.

## Tình huống phải rộng và có diễn biến

Cùng một sự kiện xin phép có thể tách thành được đồng ý, bị từ chối, được đồng ý có điều kiện, cần chờ người có quyền quyết định. Mỗi nhánh có hội thoại riêng xử lý hệ quả của phản hồi. Chỉ đổi tên người hoặc món ăn không đủ để tính thêm một tình huống.

Trước khi viết, tác giả dừng ở từng topic để tìm nguồn và suy nghĩ về trước/trong/sau sự kiện, vai và quan hệ, kết quả, hiểu nhầm, sửa lời và phương án khác. Không đặt chỉ tiêu 8–12 cho mọi chặng; cần đủ rộng cho chủ đề và ghi rõ góc còn thiếu. Chất lượng được đánh giá bằng nội dung đã viết và nguồn thực đọc, không bằng số node.

## Một lộ trình dùng chung 27 sách

Hạt giống V4.1 là danh sách định hướng. Chặng mới phải tra lại kho sách, không giới hạn trong vài token đã gắn. Quét chỉ mục 27 cuốn để tìm chất liệu, đọc sâu phần liên quan, phối hợp theo chức năng:

- 5500 và các ngân hàng cách nói mở rộng phản hồi, bối cảnh và lựa chọn.
- Roleplay, business, kính ngữ cung cấp quan hệ, nhiệm vụ và tiến trình giao tiếp.
- **B11/B12 Speak Japanese:** bài kiến thức MD đầy đủ để người dùng làm video; node kế tiếp là shadowing các ví dụ/hội thoại tương ứng. Có liên kết example ID giữa MD và bài luyện. Mẫu mới + ôn chọn lọc bài trước; phân bổ đến nhiều topic phù hợp, không dồn cả sách vào vài pool nguồn cũ. Hiện chưa tạo video.
- **B01 5500:** nhóm các câu/đối đáp theo mục đích giao tiếp thành shadowing.
- **B08 必須700:** nhóm theo topic/chức năng thành shadowing; ngoại lệ với cách đóng gói video kiến thức của Speak Japanese.
- **B09 なめらか, B13/B14 Shadowing:** câu/đoạn mẫu phù hợp thành bài luyện shadowing, giữ sắc thái và nhịp thoại.
- **B25–B27 Nama Chuukei:** hội thoại/câu mẫu thành bài shadowing có bối cảnh, giữ lợi ích nghe ý định, xác nhận và hỏi lại; không chỉ lưu ở ngân hàng nguồn.
- Tượng thanh, quán ngữ, cảm xúc, rút gọn đi vào tình huống phù hợp như chất liệu ngôn ngữ.
- Memo web giúp phát hiện chủ đề/góc mới; mục lục không được coi là nguồn nguyên văn cho hội thoại.

Tận dụng tất cả sách trên toàn lộ trình, không nhét mọi sách vào mỗi chặng. Theo dõi đóng góp thật ở `sources.json`; phân biệt đã đọc, mới thấy chỉ mục, chuyển soạn và viết mở rộng. Ghi CD/track khi có bằng chứng nhưng không gắn audio cũ vào lời đã viết lại.

## Ngữ pháp N5–N4 / Minna

Đã lập [danh sách tên ngữ pháp 50 bài Minna sơ cấp](../../reference/grammar/MINNA_01_50_GRAMMAR.md), có JSON để tra theo bài. Dùng syllabus chính thức bản 2 và giáo án theo bài để đối chiếu tên mẫu. Không gọi đây là danh sách JLPT N5/N4 chính thức: JLPT không công bố danh mục ngữ pháp hiện hành theo cấp.

Tại lúc kiểm tra kho: bunpou có metadata N3/N2/N1, chưa có metadata bài N5/N4. Không ghi vào bunpou trong task này. Danh sách Minna là đầu vào để bổ sung bunpou sau; khi có bài thật mới gắn ID. Nhãn sơ/trung/thượng của chặng và nhãn JLPT không quy đổi một-một.

## Bền vững khi chạy dài và khi nâng cấp

Mỗi chặng dùng UUID trong registry. Mỗi node, tình huống và lượt nói giữ ID trong các lần sửa; mã S/T/H là mã hiển thị. Bản làm việc riêng từng lượt, có checkpoint ghi việc đã làm, việc tiếp theo, hash nội dung và nguồn tham chiếu. Một chặng chỉ có một lượt chủ sở hữu.

Pause lưu công việc. Resume kiểm hash để phát hiện thay đổi ngoài lượt; recovery tạo draft kế thừa riêng và giữ draft cũ. Revision đã chốt là snapshot không sửa tại chỗ; nâng cấp tạo lượt mới từ revision đó, sửa đúng phạm vi, tái xuất context, giữ lịch sử. Chỉ chuyển con trỏ `current.json` sau khi snapshot và kiểm tra cấu trúc thành công. Không cần một DB từ vựng toàn cục hay nhiều worker cùng ghi file nội dung chung.

V3.1 pin thêm sổ bài và file nội dung của các bài trước đã tham khảo. Nếu chặng trước đổi revision trong lúc draft nối tiếp đang làm, cần xem lại liên kết ôn trước khi chốt. Các phần chưa nối được có ghi `continuity_pending` trong manifest; chưa có dữ liệu không được báo là đã hoàn thành gối đầu.

Helper thực thi: `.agents/skills/kaiwa-stage-content/scripts/stage_work.py`. Cấu trúc chi tiết và giới hạn vận hành nằm trong [skill](../../../.agents/skills/kaiwa-stage-content/SKILL.md) và tài liệu checkpoint đi kèm. Kiểm tra của helper là kiểm tra biên tập/dữ liệu, không phải test trong app.

## Cách triển khai tiếp

1. Chọn ba chặng đại diện: một đời sống sơ cấp, một công việc trung cấp có nhánh từ chối/điều kiện, một thượng cấp có sắc thái và triển khai ý. Viết chậm, đủ sâu rồi người dùng xem chất lượng và độ tiện import.
2. Điều chỉnh hợp đồng dữ liệu sau pilot; không chốt cứng schema vì chưa biết đủ dạng nội dung thực tế.
3. Khi được giao chạy hàng loạt, làm từng chặng, checkpoint đều đặn. Tổng hợp độ bao phủ nguồn từ các revision đã chốt để tìm cuốn/góc còn ít được tận dụng.
4. Khi yêu cầu nâng cấp một chặng, đọc revision và sổ biên tập trước, bổ sung có mục tiêu; không tái sinh cả lộ trình.

V4.1 đã có [gói sửa nguồn và thống kê](V4_1_SOURCE_FIXES.md); khi nhận chặng vẫn phải đọc phần nguồn dùng thật. Token pool hiện có chỉ là nơi bắt đầu tìm, không giới hạn nơi được đưa Speak Japanese/nguồn shadowing vào. Khung topic, 194 UID và thứ tự không cần đổi cho feedback này; cần đổi cách bố trí bài **bên trong** chặng và nối các bài với nhau. Skill không coi `fact_check` hoặc `kind: book` của hạt giống là chứng nhận ngữ nghĩa.
