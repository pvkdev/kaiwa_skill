# Gối đầu, Speak Japanese và bài shadowing

## “Bài” và trí nhớ của lộ trình

Một chặng có nhiều bài. Một bài là nhóm node có cùng mục đích học, khai báo bằng `lessons[].id` trong `learning-map.json` và tham chiếu qua `lesson_id`; không thêm một loại màn hình bắt buộc cho app. Ví dụ một bài Speak Japanese gồm node kiến thức dành cho video và node shadowing theo ngay sau, có thể được chuẩn bị từ vựng/ngữ pháp trước cặp đó. ID bài/node giữ nguyên khi sửa; không lấy số thứ tự làm danh tính.

Trước bài 3, đọc lại bài 1 và 2 đã biên soạn. Tương tự ở bài sau: hai bài gần nhất là điểm bắt đầu, không phải giới hạn trí nhớ. Tìm thêm nội dung cũ liên quan trong các chặng trước theo thứ tự V4.1. Gối đầu đi xuyên ranh giới chặng và áp dụng cho Speak Japanese, tình huống, câu mẫu lẫn danh sách từ.

Tìm bài trước bằng thứ tự node trong sổ bài hiện tại, rồi lần ngược các chặng trước trong JSONL, mở `current.json` và sổ bài của revision đã chốt. Nếu chặng ngay trước chưa soạn, ghi khoảng trống đó; không âm thầm nhảy qua rồi gọi hai bài tìm thấy là hai bài liền trước. Khi soạn Speak Japanese, tra thêm các bài Speak Japanese đã có liên quan đến mẫu đang dạy, bên cạnh hai bài gần nhất của lộ trình chung.

Đọc sổ bài để chọn nội dung, rồi mở MD/JSON gốc của phần định dùng. Không nạp lại cả lịch sử lộ trình vào mỗi lượt. Ghi ba điều:

- Điều mới của bài, tóm tắt trong `summary`.
- Những bài trước đã tham khảo (`lookback`).
- Nội dung nào được dùng lại, từ bài/node/item nào, xuất hiện ở đâu trong bài mới và để làm gì (`reuse`). Tham khảo một bài không có nghĩa đã dùng lại toàn bộ bài đó.

Ưu tiên kiến thức vừa học và nội dung cũ phù hợp ngữ cảnh: từ về món ăn có thể trở lại trong đặt bàn, hỏi thành phần, đổi món; cách chia sẻ cảm nhận đã học có thể đi vào ví dụ mới về ăn uống. Có thể quay lại xa hơn để ôn, không ép đưa mọi từ/mẫu của hai bài trước vào cuộc thoại mới. Giữ mục tiêu mới rõ ràng và độ khó hợp cấp.

Mặc định có ôn ứng dụng khi đã có chất liệu phù hợp. Chỉ bỏ phần tái sử dụng khi có lý do biên tập cụ thể; không dùng một lý do chung để soạn mọi bài độc lập. `lookback` ghi đã tham khảo, còn `reuse` phải chỉ tới nơi nội dung cũ thật sự xuất hiện trong bài mới.

Chỉ nội dung **đã tồn tại và đã đọc** mới được ghi là ôn lại. Cần dùng mẫu chưa giới thiệu thì bổ sung hỗ trợ/giải thích thích hợp hoặc ghi là chất liệu mới; không giả vờ nó đã học vì có trong sách nguồn. Chọn đoạn sách hợp cấp; không làm sai sắc thái hay xóa mất điểm hay của ví dụ chỉ để ép nó khớp danh sách ngữ pháp.

Nếu chưa có bài trước (ví dụ pilot riêng một chặng), ghi `pending_previous` và lý do; vẫn được làm bản nháp độc lập. Không bịa tham chiếu, không tuyên bố mạch gối đầu đã hoàn chỉnh. Bài đầu tiên của lộ trình ghi rõ chưa có tiền lệ. Đây là trạng thái biên tập, không là cổng học.

## Speak Japanese: kiến thức → shadowing

Hai sách hiện có là B11 **基本文型88** và B12 **発展文型125**. Đọc bài/mục cụ thể, không dùng token pool P1/P2 thay việc đọc. Biên soạn nội dung như một **bài kiến thức Markdown**: nghĩa, chức năng, ngữ cảnh/quan hệ, cách dùng, đối chiếu và lưu ý đặc trưng có trong bài; giữ ví dụ có ích, có nghĩa Việt. Không chỉ lấy tên mẫu làm danh sách ngữ pháp.

Node đánh dấu `source_family: speak_japanese`, có `video: {status: planned, asset_ref: null}` và `practice_node_id`. Chưa tạo video, không đặt URL giả. **Node kế tiếp trong thứ tự học là shadowing** liên kết ngược bằng `knowledge_ids`; danh sách từ/ngữ pháp nếu cần đặt trước cặp hoặc dùng danh sách chung, không chen vào giữa video và luyện.

Bài shadowing bao gồm các ví dụ/hội thoại tương ứng với những điểm thực sự vừa giải thích, không phải một đoạn bất kỳ cùng topic. Dùng `example_id` ổn định để nối ví dụ trong MD với item luyện; có thể đặt anchor trong MD. Phân biệt ví dụ chuyển soạn từ sách với ví dụ viết mới lồng nội dung cũ. Phần viết mới vẫn phải thực hành điểm mới của bài. Nếu thay ví dụ ở một bên, đối chiếu và cập nhật bên còn lại; không gắn audio sách vào câu đã sửa.

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

Danh sách ăn uống nên bao gồm các nhóm cần dùng như món/nguyên liệu, đồ uống, vị/cách nấu, khẩu phần, đồ dùng và thao tác gọi món/thanh toán, tùy phạm vi chặng. Từ phục vụ thực hành trực tiếp là phần đầu; từ giúp mở rộng lựa chọn và diễn đạt thực tế là phần tiếp. Không cần ép mọi chặng vào cùng một bộ tiểu mục hoặc số từ.

Giữ sự chọn lọc theo cấp và nhu cầu, không thêm thuật ngữ xa chủ đề chỉ để có danh sách dài. Có thể chia danh sách theo cụm sự kiện. Mỗi item đánh dấu `exposure: new|review`; từ ôn trỏ về lần học trước bằng `reuse`, xét đúng nghĩa/cách dùng chứ không chỉ trùng chữ Nhật. Người học có thể mở mọi danh sách tự do. Engine app tự lo bài tập và lịch ôn; skill lo lựa chọn từ và sự tái xuất hiện trong câu/hội thoại.

## Chạy dài, phối hợp và nâng cấp

Mạch gối đầu là quan hệ biên soạn. Worker có thể tìm nguồn/làm nháp song song; trước khi chốt phần nối tiếp phải đọc các bài trước thực có, cập nhật `lookback/reuse`, không trỏ draft của worker khác như một bản đã chốt. Với bài khác chặng, pin UUID, revision và các file của bài đã tham khảo. Khi pause/resume, giữ cả sổ này trong checkpoint.

Khi nâng cấp một bài cũ, không đổi ID. Tìm các `lookback/reuse` dùng UID/bài đó trong những chặng sau, so revision và đọc lại phần thực sự ảnh hưởng. Bản đã chốt vẫn giữ snapshot; cập nhật bài sau theo phạm vi ảnh hưởng thay vì tự sinh lại cả lộ trình. Helper phát hiện con trỏ revision cũ khi kiểm draft để tác giả xem lại; không tự sửa nội dung hoặc khóa bài người học.
