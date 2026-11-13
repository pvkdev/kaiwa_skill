# Gối đầu, Speak Japanese và bài shadowing

## “Bài” và trí nhớ của lộ trình

Một chặng có nhiều bài. Một bài là nhóm node có cùng mục đích học, khai báo bằng `lessons[].id` trong `learning-map.json` và tham chiếu qua `lesson_id`; không thêm một loại màn hình bắt buộc cho app. Ví dụ một bài Speak Japanese gồm node kiến thức dành cho video và node shadowing theo ngay sau, có thể được chuẩn bị từ vựng/ngữ pháp trước cặp đó. ID bài/node giữ nguyên khi sửa; không lấy số thứ tự làm danh tính.

Khi tạo hội thoại hoặc ví dụ mới, **cân nhắc** dùng kiến thức Speak Japanese, từ vựng và ngữ pháp đã xuất hiện nếu chúng hợp ngữ cảnh. Hai bài gần nhất là gợi ý tra cứu thuận tiện, không phải danh sách buộc phải đọc/áp dụng cho mọi bài. Có thể tìm xa hơn trong lộ trình hiện hành; không ép một nội dung cũ vào lời thoại để có “gối đầu”.

Khi cần tra bài cũ, dùng thứ tự node/sổ bài và `current.json`. Nội dung chưa tồn tại không được gọi là đã học. Nếu bài cũ chưa có, vẫn soạn được bài mới; không tự tạo một món nợ “phải nối đủ hai bài trước”. Khi chuyển soạn ví dụ Speak Japanese, cũng cân nhắc ứng dụng kiến thức cũ như với hội thoại khác.

Không nạp lại cả lịch sử lộ trình. Khi chọn dùng nguồn cũ thì mở phần thực định dùng. Có thể ghi ngắn:

- Điều mới của bài, tóm tắt trong `summary`.
- Những bài trước đã tham khảo (`lookback`).
- Nội dung nào được dùng lại, từ bài/node/item nào, xuất hiện ở đâu trong bài mới và để làm gì (`reuse`). Tham khảo một bài không có nghĩa đã dùng lại toàn bộ bài đó.

Ưu tiên kiến thức vừa học và nội dung cũ phù hợp ngữ cảnh: từ về món ăn có thể trở lại trong đặt bàn, hỏi thành phần, đổi món; cách chia sẻ cảm nhận đã học có thể đi vào ví dụ mới về ăn uống. Có thể quay lại xa hơn để ôn, không ép đưa mọi từ/mẫu của hai bài trước vào cuộc thoại mới. Giữ mục tiêu mới rõ ràng và độ khó hợp cấp.

`lookback`, `reuse` và `review_links` là ghi chú tùy chọn, không KPI, không điều kiện chốt bài và không cần giải trình việc không tái sử dụng. Không tạo link cho từng từ chỉ vì nó xuất hiện lại. Nếu ghi liên kết cụ thể thì nó phải có thật. Ưu tiên ghi theo nhóm kiến thức khi có ích; gói app có thể để `review_links: []`, không xuất sổ biên tập thành luật học.

Chỉ nội dung **đã tồn tại và đã đọc** mới được ghi là ôn lại. Cần dùng mẫu chưa giới thiệu thì bổ sung hỗ trợ/giải thích thích hợp hoặc ghi là chất liệu mới; không giả vờ nó đã học vì có trong sách nguồn. Chọn đoạn sách hợp cấp; không làm sai sắc thái hay xóa mất điểm hay của ví dụ chỉ để ép nó khớp danh sách ngữ pháp.

Nếu chưa có bài trước, không bịa tham chiếu hoặc tuyên bố đã ôn. Có thể ghi chú để cân nhắc khi nâng cấp sau; không bắt `pending_previous` hoặc coi đó là công việc bắt buộc còn thiếu.

## Speak Japanese: kiến thức → shadowing

Hai sách hiện có là B11 **基本文型88** và B12 **発展文型125**. Đọc trọn bài/mục được chọn. Giữ mạch bài nguồn, các chức năng, đối chiếu thân mật/lịch sự, hội thoại mở đầu và những nhóm ví dụ làm rõ bài đó; viết lại giải thích cho dễ hiểu và dịch Việt. Không thay cả bài bằng vài câu mới cùng topic. Nếu chỉ khai thác một phần, phải gọi rõ là trích phần và có lý do phù hợp, không nhận là đã đưa toàn bài vào. Nội dung ứng dụng topic do AI viết là phần bổ sung sau chất liệu nguồn.

Node đánh dấu `source_family: speak_japanese`, có `video: {status: planned, asset_ref: null}` và `practice_node_id`. Chưa tạo video, không đặt URL giả. **Node kế tiếp trong thứ tự học là shadowing** liên kết ngược bằng `knowledge_ids`; danh sách từ/ngữ pháp nếu cần đặt trước cặp hoặc dùng danh sách chung, không chen vào giữa video và luyện.

Bài shadowing sau video luyện **các hội thoại/ví dụ nguồn đã đưa vào bài**, rồi mới có thể thêm ví dụ topic viết mới. Không chỉ luyện vài câu AI thay thế. Dùng chung utterance ID để không có hai bản phải sửa đồng thời. Mỗi câu ghi `source_quote`, `source_adaptation` hoặc `original_extension` và nguồn tương ứng. Các ví dụ nguồn vượt phần ngữ pháp chủ động hiện tại phải được nhận diện rõ là tham khảo, có tên ngữ pháp hỗ trợ khi cần; không coi một đoạn khó là Sơ chỉ vì ngắn hoặc xuất phát từ sách cơ bản.

Không gom 88/125 mẫu vào vài node khổng lồ chỉ vì khung hiện có ít token pool; cũng không có chỉ tiêu phải dùng hết chúng. Phân bổ các bài/mục được chọn đến topic/cấp độ phù hợp, giữ quan hệ nền tảng và rải ôn sau đó. Khi gán một bài nguồn, ghi bài đó đã đi vào node kiến thức và shadowing nào; nếu tách một bài nguồn cho hai topic, ghi rõ phần nào được dùng ở đâu, tránh đếm trùng thành hai bài nguồn đã khai thác độc lập. Chọn lọc nguồn không làm giảm yêu cầu giải thích rõ và luyện đúng những điểm đã chọn để dạy.

## Các nguồn xuất hiện thành bài shadowing

- **B25–B27 Nama Chuukei:** chuyển cảnh nghe/cách phản hồi thành hội thoại/câu thực hành; giữ bối cảnh và ý định. Không biến thành bài thi nghe.
- **B09 なめらか:** các ví dụ, đối đáp và cách nói tự nhiên thành câu/hội thoại luyện; thêm giải thích ngắn khi cần hiểu rút gọn hoặc sắc thái.
- **B13–B14 Shadowing:** dùng các đoạn/cụm phù hợp trong topic và level; không bỏ nhịp đáp, mức thân mật hoặc cách chuyển lượt quan trọng.
- **B01 5500:** gom câu thành các nhóm giao tiếp có mục đích trong topic, ví dụ gọi món, hỏi thành phần, nhận xét món; không dồn hàng trăm câu không liên hệ vào một node.
- **B08 どんどん話せる！日本語会話フレーズ大特訓 必須700:** nhóm theo topic/chức năng thành shadowing. Đây là ngoại lệ với cách đóng gói video của Speak Japanese; không bắt mọi nhóm 必須700 có bài video riêng.
- **B11/B12:** bài luyện ví dụ là shadowing, đặt ngay sau kiến thức/video tương ứng như trên.

Một bài shadowing có thể gồm câu đơn, hội thoại ngắn hoặc tham chiếu tình huống hoàn chỉnh. Các câu cùng nhóm cần quan hệ rõ về hành động giao tiếp/chủ đề; đừng ráp những câu không có quan hệ thành hội thoại giả. Chọn và nhóm theo chất liệu nguồn, không gọi việc ghi tên sách trong `banks` là đã đưa sách vào bài luyện.

## Từ vựng theo miền chủ đề và ôn tích lũy

Soạn và rà hội thoại/câu luyện trước, rồi **trích ngược từ nội dung thực sự xuất hiện** để lập danh sách. Chọn từ/cụm hữu ích cho việc hiểu và nói, không thêm một ngân hàng từ độc lập để làm list dài. Có thể chia theo cụm tình huống hoặc bài nguồn. Tên riêng không nhất thiết phải biến thành thẻ từ.

Động từ ở thể từ điển, tính từ ở dạng cơ bản: 行きます → 行く, 降りて → 降りる, 多かった → 多い; danh từ/cụm cố định dùng dạng mục từ phù hợp. Không sửa câu hội thoại thành thể từ điển theo list. Ghi một vài ví dụ xuất hiện và quyết định chuẩn hóa trong sổ biên tập, không cần mapping từng lần xuất hiện. `exposure` là tùy chọn; không buộc link từng từ ôn. Engine app tự lo bài tập/lịch ôn, người học được mở danh sách tự do.

## Chạy dài, phối hợp và nâng cấp

Mạch gối đầu là cân nhắc biên soạn. Worker có thể tìm nguồn/làm nháp song song; nếu ghi đã tham khảo một bài trước thì phải đọc phần liên quan thực có, không trỏ draft của worker khác như một bản đã chốt. Không bắt tạo `lookback/reuse` để chốt bài. Với liên kết khác chặng được chọn ghi, pin UUID, revision và các file đã tham khảo. Khi pause/resume, giữ sổ này trong checkpoint.

Khi nâng cấp một bài cũ, không đổi ID. Tìm các `lookback/reuse` dùng UID/bài đó trong những chặng sau, so revision và đọc lại phần thực sự ảnh hưởng. Bản đã chốt vẫn giữ snapshot; cập nhật bài sau theo phạm vi ảnh hưởng thay vì tự sinh lại cả lộ trình. Helper phát hiện con trỏ revision cũ khi kiểm draft để tác giả xem lại; không tự sửa nội dung hoặc khóa bài người học.
