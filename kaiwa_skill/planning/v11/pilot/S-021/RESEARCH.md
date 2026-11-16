# S-021 — Nhận chỉ thị & hỏi lại

## Quy ước và căn cứ

- Ngày đọc: 2026-11-16. Đường dẫn nguồn trong `dialogues.json` tính từ gốc repo. Mọi hội thoại là biên soạn mới (`original_extension`); sách cung cấp chức năng giao tiếp và nhịp hỏi đáp, không cung cấp cuộc thoại pilot hay audio cho cuộc thoại này.
- Tra `planning/catalog27/BOOK_GUIDE.md`, `source_index.jsonl`, `manifest.json` theo `指示`, `確認`, `聞き返す`, `報告`, `依頼されたこと`, việc in/sắp tài liệu và các lời đáp công sở. Kho 27 sách được tra ở cấp chỉ mục; đọc sâu ba sách khớp chức năng và cấp. B01 đời sống và B15–B17 role-play có các tình huống liên quan nhưng đoạn khớp mục tiêu nhận chỉ thị ngắn ở mức Sơ của B03/B10/B02 trực tiếp hơn; không gán nguồn không dùng.
- B03 `しごとの日本語 ビジネスマナー編`, `chapters/19-Unit17-指示を受ける.md` dòng 37–47: hỏi sau khi nghe hết, xác nhận hạn cụ thể, số, tên riêng, nhắc lại; dòng 50–72: chuyện in tài liệu sai do tự đoán và yêu cầu kiểm mặt/trang/chất lượng. Đã đọc lời dẫn và kết quả ngay trước/sau các đoạn. Cảnh pilot thay bằng tài liệu đào tạo và giấy, không lấy nguyên cuộc thoại hoặc lời Nhật của sách.
- B10 `にほんごで働く！ビジネス日本語30時間`, `book.md` dòng 1528–1543: người nhận việc nhắc lại đối tượng được giao sau lời nhờ. Đã đọc phần dẫn và biến thể bên cạnh; nhiệm vụ, số và hạn trong pilot là ví dụ biên tập.
- B02 `「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語`, `chapters/13-確認する.md` dòng 148–202: người nhận việc hỏi rõ ý, diễn đạt lại cách làm, cấp trên xác nhận. Đã đọc trọn Scene 37, lời đáp và giải thích; từ vựng và kính ngữ của pilot được hạ xuống Sơ.
- Chuyên đề ngay trước `sj-so-05`, `lesson.md` và `practice.json`: vận dụng `わかりました` trong lời nhận chỉ thị và kiểm lại, tránh `了解` với trưởng nhóm. `specialty_item_ids` chỉ gắn ở những cảnh dùng rõ. Không dùng `よね` để ép xác nhận khi người nghe chưa hề biết thông tin.
- Đây là văn phòng giả định: buổi đào tạo, 12 bộ trước 15:00, mẫu cũ chỉ lấy bố cục bìa, trang 3 cần thay, giấy trắng là yêu cầu nội bộ của trưởng nhóm. Không có nhận định về chính sách lao động, an toàn máy in hoặc quyền lợi. Vì không có dữ kiện bên ngoài làm căn cứ, không cần gắn nguồn web; khi triển khai ở đơn vị thật phải hỏi người giao việc như các lượt trong thoại.

## Mạch sự kiện

- E01: Nhân viên nữ nhận việc tài liệu đào tạo, hỏi hạn; phát hiện ghi chú 12/20 mờ và xác nhận là 12; hỏi dùng mẫu cũ, biết chỉ được dùng bố cục bìa. Trưởng nhóm nam đưa điều kiện và xác nhận.
- E02: Nhân viên hỏi đồng nghiệp nam nghĩa `差し替える`; đồng nghiệp chưa rõ phạm vi nên trực tiếp hỏi trưởng nhóm ngoài khung thoại, trở lại với câu trả lời chỉ trang 3. Một cảnh độc lập tập tìm đúng người duyệt khi chỉ dẫn kẹp/ghim xung đột. Không tạo người nói thứ ba trong cùng cảnh.
- E03: Nhân viên báo giấy trắng hết trước khi in, xin phép dùng giấy kem; trưởng nhóm chưa duyệt rồi từ chối, giao việc kiểm thứ tự trang trong lúc đợi; giấy trắng đến mới tiếp tục và in thử một bộ.
- E04: Nhân viên báo đã xếp 12 bộ và chỉ nơi đặt; tự rà thêm thấy một bộ thiếu trang 3 trước khi trưởng nhóm xem; sửa và nhờ kiểm bộ vừa sửa rồi mới bàn giao.

## Ba bước QA theo tình huống

Mỗi dòng ghi (1) lượt người học thực hiện việc đích và lời chốt, (2) kết quả đọc Nhật liền / Việt độc lập và cảnh kề, (3) thử cả hai vai và nét khác nhánh. UID lượt lấy hậu tố `uNN` của `situation_uid` trong JSON. Trạng thái `reviewed` gắn với hash cảnh trong `status.json`.

- **S001 `b58df347-1426-52c3-9a69-0a0b55b64d27`:** u02 hỏi hạn, u04 tự nhắc tên việc và 15:00, u05 trưởng nhóm xác nhận. Nhật–Việt cùng hạn, không lẫn ngày mai; S002 mới kiểm số. Hai vai nói gọn, nhánh mở việc.
- **S002 `1c6e544c-37e7-5d86-8375-49dcd177a197`:** u01 chủ động nêu hai con số nghe/ghi dễ nhầm; u02 chốt 12, u03 sửa ghi chú. Việt giữ đúng 12/20; mạch tiếp S001 vì số chưa từng xác nhận ở S001. Vai trưởng nhóm chỉ đáp một con số, khác mục tiêu hỏi hạn.
- **S003 `55762402-82b6-5b2e-bce0-4057fa70ce99`:** u01 hỏi dùng mẫu cũ; u02–u04 trả lời được dùng có điều kiện: bố cục bìa, nội dung mới; u05 nhắc lại. Nhật `表紙の形` là bố cục bìa, không phải tái dùng nội dung; nối S004. Cả hai vai có lời tự nhiên, không biến đồng ý thành toàn phần.
- **S004 `c9b62a8f-9cd7-501b-8680-d8479ce246fd`:** u01 nhân viên tự xác nhận giới hạn; u02 trưởng nhóm nói rõ thân bài mới, u03 chốt sẽ làm mới. Đọc Việt độc lập cho đúng giới hạn; nhánh conditional có việc cụ thể khác S003.
- **S005 `25fa54cd-46a6-5b61-b7a1-be6c9f31a30b`:** u01 hỏi nghĩa từ chưa hiểu, u02 giải thích bằng động tác, u03 hỏi trang nào, u04 nói chưa chắc và sẽ kiểm. Việt giữ độ bất định `だと思います`; S006 tiếp chờ. Hai vai nói được, không giả rằng đồng nghiệp đã biết kết quả.
- **S006 `f15ff307-cf0d-59e8-a052-b0dc8172f52d`:** u02 hỏi đúng đầu mối, u03 đồng nghiệp nhận hỏi trưởng nhóm, u04 nhân viên chờ rồi mới sửa. Nhật–Việt cùng trạng thái pending; S007 chỉ mở sau khi đồng nghiệp đã hỏi. Vai đồng nghiệp không tự quyết phạm vi.
- **S007 `9308b68b-93de-5888-b638-2e1adfcaa860`:** u01 đồng nghiệp báo đã hỏi trưởng nhóm, u02 và u04 nhân viên nói lại thao tác (lấy trang 3 cũ, giữ các trang khác), u03/u05 xác nhận. Nhật–Việt giữ rõ trang 3 mới thay vào; kết thúc nhánh chờ bằng câu trả lời thật. Hai vai ngắn và có bước mới.
- **S008 `c54ebfbd-fbc8-5d34-a894-3a98f4a5155f`:** u01 và u03 nhân viên nêu lần lượt hai chỉ dẫn trái nhau rồi hỏi người duyệt, u04 nêu trưởng nhóm, u05 nói sẽ để nguyên và đi hỏi. Việt không ngụ ý đã có quyết định kẹp hay ghim. Cảnh độc lập có mục tiêu tìm người quyết định, khác S006 hỏi nghĩa/phạm vi; u02/u06 là phản ứng ngắn của đồng nghiệp.
- **S009 `62c336f1-3825-548b-a6b3-e76301e3c60c`:** u01 nhân viên báo giấy thực tế khác chỉ thị, u02/u03 xác nhận chưa in, u04 trưởng nhóm sẽ kiểm. Nhật–Việt cùng trạng thái chưa làm; S010 mới đề nghị phương án. Hai vai phản ứng được, không tự dùng giấy xanh.
- **S010 `50c84cf1-41f1-58a6-9da7-8a8cab88321d`:** u01 nhân viên xin phép dùng giấy kem; u02 chưa duyệt, u03 chấp nhận chờ, u04 hứa trả lời. Việt giữ đúng chưa có phép; S011 từ chối không mâu thuẫn. Khác S009 vì chủ động đề xuất phương án.
- **S011 `123542f0-6256-5cc3-8b46-c32c117ab32e`:** u01 từ chối giấy kem; u02 nhân viên hỏi việc làm trong lúc chờ; u03 giao kiểm thứ tự trang, u04 nhắc sẽ chờ in. Nhật–Việt rõ việc được làm và việc chưa được làm; S012 sau khi giấy trắng đến. Vai nhân viên có phản ứng hữu ích trước từ chối.
- **S012 `7d01ae36-779a-58c2-ba0a-ee3cee160048`:** u01 báo giấy trắng đã đến và xin tiếp tục; u02 chốt 12 bộ; u03 nhân viên chủ động in thử một bộ; u04 trưởng nhóm xác nhận điều kiện in phần còn lại. Việt không coi đây là quy tắc máy in chung. Hai vai ngắn, nhánh tái khởi động khác chờ.
- **S013 `b0f1ca82-9d45-574d-82f4-4b2214609224`:** u01 nhân viên báo xong 12 bộ, u02 hỏi vị trí, u03 nêu bàn, u04 nói sẽ xem sau. Nhật–Việt đều không nói trưởng nhóm đã xem. S014 có thể xảy ra vì nhân viên kiểm thêm trước lúc trưởng nhóm xem; hai vai có hành động nhận và chỉ vị trí.
- **S014 `8b6b9c26-9552-5d9a-a82b-95e66095afd6`:** u01 nhân viên phát hiện một bộ thiếu trang 3 và báo ngay, u02 giữ bộ ấy lại, u03 hẹn sửa rồi báo. Việt giữ `一部だけ` là một bộ trong 12, không phải toàn bộ tài liệu; nối S015. Nhánh lỗi có hành động khác báo xong.
- **S015 `725e1d3b-371c-5c87-8d9b-46a33f8ffed3`:** u01 báo bổ sung trang 3, u02 hỏi đủ 12 bộ, u03 nhân viên xác nhận và xin xem lại đúng bộ vừa sửa, u04 kiểm rồi đồng ý, u05 mới bàn giao. Nhật–Việt nhất quán số và thời điểm; cả hai vai nói được, không suy từ việc sửa sang đã được duyệt trước u04.

## Vấn đề mở

Không còn lỗi đã biết ở bản tác giả. Chờ root rà độc lập toàn bộ Nhật–Việt và HTML hai vai; `root_review` giữ `pending`.

Điều phối viên đã hoàn tất lượt đọc độc lập, đối chiếu bản Nhật–Việt và nhãn vai của tất cả các cảnh. Ghi nhận bàn giao tác giả ở trên được giữ để đối chiếu. Trạng thái và hash nghiệm thu mới nhất nằm trong root_review của status.json.
