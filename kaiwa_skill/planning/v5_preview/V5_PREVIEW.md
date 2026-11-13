# Kết quả rà soát và bản xem trước V5

> Chưa áp dụng vào 194 chặng. Đọc bản này để duyệt hướng; xem TOPIC_CARDS.md để đọc mọi tình huống.

## Kết quả định lượng

- **120/120** đề xuất gốc đã có quyết định: **47 bổ sung**, **44 tách sâu**, **14 mở rộng tại chỗ**, **9 gộp**, **4 làm rõ chặng cũ**, **2 để lựa chọn sau**.
- Có thêm **13** phương án sau đối chiếu: 5 bổ sung và 8 tách sâu.
- Kho đề xuất gồm **104 phương án bổ sung/tách**: **52 topic mới về phạm vi** và **52 phần đã có cần tách sâu**. Không gọi toàn bộ là 104 chủ đề chưa từng có.
- Trong 104 phương án: **41 P1**, **44 P2**, **19 P3**; P3 chủ yếu theo hoàn cảnh riêng.
- **110 thẻ** có tổng **660 seed tình huống**; gồm 104 phương án trên, 4 làm rõ chặng cũ và 2 để sau. 14 mở rộng có thêm 42 seed riêng; 16 địa danh/mô-đun được để ngoài phép đếm chặng.
- **16 thẻ** có đoạn đã đọc hỗ trợ ít nhất một phần topic/sự kiện; **94 thẻ** còn cần nguồn trực tiếp, dù có thể có nền chức năng nói. Đây không phải tỷ lệ dùng sách và không là tỷ lệ được xác nhận của các seed.
- **Chưa chốt tổng chặng V5**: 194 + 104 = 298 chỉ là kịch bản giữ nguyên mọi chặng mẹ; chưa khử các ô cần gộp/đổi thành bài tổng hợp. Không đề nghị chốt 298.

## Mở tài liệu

- [Danh sách đầy đủ và tình huống từng thẻ](TOPIC_CARDS.md)
- [Đối chiếu đủ 120 đề xuất gốc](REVIEW_AI120.md)
- [16 lớp bối cảnh du lịch](TRAVEL.md)
- [Sổ nguồn và vai trò 27 sách](SOURCE_AUDIT.md)
- [Bản tra cứu có bộ lọc](PREVIEW.html)
- Dữ liệu: `candidates.jsonl`, `review_ai120.jsonl`, `own_additions.jsonl`, `travel_modules.json`, `sources.json`, `book_audit.json`, `snapshot.json`, `stats.json`.


Ngày rà soát: **13/11/2026**. Trạng thái: **đề xuất để duyệt**, chưa áp dụng V5.

## Kết luận biên tập

Lộ trình cần dày hơn bằng **các việc người học thật sự phải giải quyết**, không chỉ thêm tên địa điểm. Một chặng đáng đứng riêng khi có một mục tiêu giao tiếp rõ, một chuỗi tương tác đủ rộng, và ranh giới khác với chặng đang có. Địa điểm, vai trò, quan hệ và kết quả khác nhau là cách mở rộng tình huống; chúng không luôn là chặng mới.

120 đề xuất có nhiều ý dùng được. Tuy nhiên, không thể cộng thẳng 120 vào 194. Một số đã xuất hiện rõ trong khung; nhiều ý khác là phần cần tách sâu khỏi các ô quá rộng như T-03, H-09, H-41 hoặc H-54. Phép tách chỉ hợp lý nếu đồng thời thu hẹp chặng mẹ.

**Tôi đề xuất một kho lựa chọn lớn, rồi chọn tuyến chính và các nhánh theo nhu cầu.** Chặng P3 về ô tô, gia đình, làm đẹp hay vị trí quản lý không phải kiến thức kém quan trọng; nó có đối tượng riêng. Người học được mở thẳng thứ cần dùng, không phải học tuần tự toàn bộ kho mới có ích.

## Cơ sở và giới hạn của lượt rà soát

- Đối chiếu cấu trúc 194 chặng, 645 seed tình huống và phạm vi các chặng dễ trùng.
- Tra hồ sơ, mục lục/chỉ mục của **cả 27 sách clean**, rồi đọc chọn các đoạn có ý nghĩa quyết định. Có sổ `book_audit.json` cho từng cuốn và con trỏ đoạn đọc trong `sources.json`.
- Đọc toàn bộ 120 ứng viên trong bản đính kèm, cùng 16 mô-đun du lịch; dùng memo web để đối chiếu phần đã biết.
- Tìm thêm nguồn công khai của cơ quan Nhật, bài viết tiếng Việt về đời sống và một lời kể trên diễn đàn. Đây là cách phát hiện loại vấn đề; không phải nghiên cứu thống kê để xếp hạng mức phổ biến.

**Không đọc lại toàn văn 27 PDF và không kiểm lại ảnh từng trang trong lượt này.** Bản clean và chỉ mục sẵn có là nền để đánh giá topic. Nơi chưa có đoạn nguồn trực tiếp được đánh dấu cần đọc/bổ sung; không gọi nội dung AI tự đề xuất là nội dung đã có trong sách. Các tình huống ở preview là phác thảo biên tập, chưa phải hội thoại được nguồn xác nhận.

`lookup_books` nghĩa là nơi nên tra tiếp. `book_evidence` ghi đoạn đã đọc và quan hệ của nó: đúng topic, một phần sự kiện, chỉ cùng chức năng, khác vai, chỉ bối cảnh, hoặc ví dụ không nên coi là mẫu. Hai loại này không được tính chung thành độ phủ sách.

## Những phát hiện làm thay đổi cách chọn chặng

**Xin nghỉ việc khác phát biểu chia tay.** H-30 đang có lời chào và cảm ơn đồng nghiệp/đối tác. B09 có đoạn nhân viên xin nghỉ và bị sếp giữ lại: đủ cơ sở mở V5P-086, trong khi H-30 vẫn giữ chức năng lời chào. E02 là đoạn tham chiếu; nó không phải quy trình pháp lý nghỉ việc.

**Vai 幹事 đáng có chặng riêng.** B17 có bài 忘年会の幹事 với việc hỏi gợi ý quán và món, cân nhắc người uống/không uống. V5P-118 tách vai tổ chức khỏi T-22 đi dự tiệc. MC làm rõ H-46; tổ chức chuyến công ty làm rõ T-23. Không cộng ba chặng mới cho ba cách viết lại cùng khung tổ chức.

**Cần mở rộng đời sống ngoài công sở.** Rác, tiếng ồn, sinh hoạt cộng đồng và nhà tắm xuất hiện trong hướng dẫn tiếng Việt về đời sống Nhật; đây là cơ sở tìm thêm chuỗi hỏi, báo và phối hợp thay vì chỉ một bài văn hóa. Không coi cách làm của một địa phương là cả nước. [Kokoro: quy định và tập quán sinh hoạt](https://www.kokoro-vj.org/vi/post_6597).

**Cần người học biết tìm đúng người hỗ trợ.** Nguồn MHLW có đầu mối tư vấn lao động và tài liệu cho người nước ngoài; bài tiếng Việt cũng nêu vấn đề lương, ngày nghỉ và cách tìm hỗ trợ. Vì vậy V5P-073 và V5P-093 có giá trị riêng: kể sự việc, hỏi đúng đầu mối, nhắc lại hướng dẫn. Không biến nội dung học thành tư vấn quyền lợi cá nhân. [MHLW](https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/foreign/index.html), [Kokoro](https://www.kokoro-vj.org/vi/post_2058).

**Không gắn nguồn chỉ vì gặp đúng một từ.** B13 có đổi lịch nha sĩ, không đồng nghĩa phủ điều trị nha khoa. B17 có xin về sớm để đón họ ở sân bay, không đồng nghĩa có đầy đủ hội thoại tại sân bay. B13 có đồng nghiệp than khó dạy người mới, không phải mẫu OJT nên bắt chước. B21/B22/B23 về chuyến công ty thiên vai người hỏi thông tin, không phải ba giáo trình tổ chức chuyến đi.

## Cách đóng gói lộ trình

Giữ ba cấp là độ sâu nói, không biến thành ba nhóm địa điểm tách biệt:

- **Sơ — tự lo được việc trước mắt:** nêu nhu cầu, hỏi lại, nói thông tin cụ thể, nhận hỗ trợ và kết thúc một việc ngắn. Đi siêu thị, shiyakusho, tàu, tiệm tóc và câu nhờ giúp khẩn cấp đều có thể bắt đầu ở đây.
- **Trung — tự xử lý khi việc không diễn ra như dự kiến:** kể bối cảnh, sửa hiểu nhầm, hỏi lựa chọn, ứng phó bị từ chối, đổi hẹn và phối hợp hai đầu mối. Cùng là đi bệnh viện nhưng câu chuyện dài hơn và có thông tin cần kiểm lại.
- **Thượng — chủ động điều phối và xử lý quan hệ phức tạp:** thương lượng ưu tiên, phạm vi, trách nhiệm; điều hành trao đổi nhiều người; nói rõ nhưng giữ quan hệ, nhận ra điều chưa được nói thẳng.

Mức trên mỗi thẻ là **dải dự kiến**, chưa phải kết luận về độ khó của câu chưa viết. Chủ đề pháp lý/y tế không tự động phải ở Thượng: nhu cầu nhờ giúp ngắn phải có từ Sơ. Chuyện riêng tư, tổn hại hoặc sức khỏe không yêu cầu người học tiết lộ trải nghiệm thật để luyện.

Có thể tổ chức thành ba lớp lựa chọn trong mỗi cấp: **đời sống dùng rộng**, **công việc dùng rộng**, và **nhánh theo hoàn cảnh**. Đây là cách hiển thị/lựa chọn, không phải ba khóa cứng bắt buộc. P1/P2/P3 là ưu tiên biên soạn đề xuất, không là cổng học hoặc mức độ nghiêm trọng của vấn đề.

## Các chặng mẹ cần thu hẹp khi tách

- **S-21:** để konbini và dịch vụ nhanh; chuyển chuỗi mua bữa ăn sang V5P-001.
- **S-12:** giữ tìm hiểu khu phố, thư viện/cơ sở cộng đồng; tóc sang V5P-009, gym sang V5P-015. Chỉ tách thêm thư viện khi tài liệu thực tế quá lớn.
- **S-14/S-17:** giữ nền đi tuyến và đi xa; vé tháng/IC, gián đoạn, chuyến bay, xe thuê là các phần có ranh giới. Bối cảnh xe buýt hoặc cần trợ giúp được rải vào, không tự tạo mọi biến thể thành chặng.
- **S-34:** giữ bộ câu sinh tồn và bản đồ tìm trợ giúp. Các chặng cảnh sát, cấp cứu, cháy, koban và sơ tán đi sâu từng cuộc nói. Nhắc lại câu sinh tồn là ôn có chủ đích, không dạy mới lại y hệt.
- **S-38:** giữ nền cuộc gọi đặt dịch vụ; chuyển viễn thông sang V5P-036, tiện ích nhà sang V5P-017. Khôi phục tài khoản chỉ giữ phần nói với hỗ trợ, không bài thao tác app.
- **S-42/T-03/H-54:** đây là cụm có nguy cơ lặp cao nhất. Sau khi chuyển hành chính, ngân hàng, thuế, nenkin, bảo hiểm, tiện ích và bưu kiện, nên **gộp hoặc chuyển T-03/H-54 thành bài tổng hợp liên kết**, thay vì giữ các chặng mẹ rỗng rồi cộng số chặng con.
- **T-01/H-10:** T-01 tập trung tìm và thuê nhà; vận chuyển sang V5P-020, báo sửa đơn giản xuống Trung ở V5P-018. H-10 giữ hợp đồng dài hạn, trách nhiệm và tranh chấp phức tạp. Gia hạn/bảo lãnh là biến thể của quan hệ thuê, không một chặng giấy tờ mới.
- **T-22:** giữ vai đi dự, nâng ly, giao lưu, từ chối đồ uống. V5P-118 nhận việc 幹事; V5P-117 nhận vai đại diện triển lãm/hội thảo.
- **T-23/H-46/H-40/H-12:** bốn đề xuất làm rõ phạm vi giữ UID cũ, không cộng số. Lần lượt là phụ trách du lịch công ty, MC sự kiện, nemawashi, và sống cùng thú cưng.
- **T-50/T-51:** nhà trẻ có thể tách V5P-065; trường học đã có giáo viên nên chỉ mở rộng T-51. T-50 giữ gia đình, nuôi dạy con và tìm hỗ trợ chung.
- **T-63/H-09:** khám sức khỏe, thuốc theo đơn, nhập viện và chăm sóc người cao tuổi là các nhánh có thể tách. Giữ khám thông thường, trao đổi triệu chứng, chuyên khoa và quan hệ gia đình đúng phạm vi; không nhân chặng theo từng bệnh.
- **T-54/H-41/H-44:** T-54 tách vai OJT; H-41 giữ nguồn lực/ngân sách, tách one-on-one. H-44 giữ bàn giao; giao quyền, điều hành sự cố và cải tiến có mục tiêu khác. Nếu T-54 hết nội dung riêng, gộp lại thay vì giữ tên.
- **H-43:** sau khi tách chấm công, nghỉ việc, phản ánh hành vi gây tổn hại và xung đột nhóm, giữ phần quan hệ tế nhị còn thật sự riêng; phần còn lại có thể làm kiến thức xen kẽ, không cố giữ một ô quá trừu tượng.
- **H-55:** đã có jichikai/PTA; thêm tình huống nhận việc, đổi trực, họp và đại diện. V5P-076 mở đường tham gia tình nguyện từ Sơ/Trung, H-55 giữ độ sâu điều phối cộng đồng.
- **S-41:** là bài tổng hợp nhiều việc; khi đã có nhánh đón người thân và nomikai riêng, nên làm bài ôn nối chặng hoặc gộp, không dạy mới các đoạn đó lần nữa.

Vì vậy, chưa thể chốt số chặng V5 bằng phép cộng. Cần duyệt các thẻ và quyết định chặng mẹ nào giữ, gộp hoặc đổi thành node tổng hợp trước. Các UID cũ không bị thay trong preview này.

## Lồng ghép tài nguyên thành một khóa

Đừng đặt người học trước 27 danh sách bài của 27 cuốn. Mỗi chặng lấy **một hoặc một vài nhiệm vụ giao tiếp làm xương sống**, sách cung cấp những lớp bổ sung:

1. Bài kiến thức Markdown từ nguồn phù hợp; B11/B12 Speak Japanese là nguồn quan trọng, có video dự kiến và shadowing ví dụ ngay sau.
2. Danh sách từ vựng phục vụ tình huống sắp tới; tên ngữ pháp cần dùng từ bunpou/Minna, theo khả năng người học. Chưa cần viết bài ngữ pháp mới ở bước preview.
3. Cụm shadowing B01 5500 và B08 700 theo mục đích; ví dụ B09/B13/B14 và Nama B25–B27 khi đúng bối cảnh/quan hệ. Đừng ép bối cảnh mới vào một câu nguồn khác nghĩa.
4. Các tình huống mẫu xen giữa kiến thức, kể cả nhánh được/không được, thiếu thông tin, đổi phương án và liên hệ lại. Không bắt sáu seed của thẻ thành đúng sáu bài.
5. Bài công việc lấy cấu trúc diễn tiến từ B15–B17; B03/B18 cung cấp ứng xử và quan hệ; B04 bổ sung khi có điện thoại. B21/B22/B23 được dùng như bộ chính–bài tập–giải thích, không ba khóa lặp.
6. B06/B07/B19/B20/B24 tăng độ tự nhiên, cảm xúc và sắc thái khi hữu ích. Không buộc phải chèn đủ vào mọi chặng.
7. Một node Live AI nhận bối cảnh và kiến thức của chặng. App lo shadowing toàn đoạn/chia vai, phát âm và hội thoại trực tiếp; nội dung không thêm test, điểm hay khóa mở bài.

Ví dụ **V5P-118 幹事**: lấy nền tổ chức từ B17; tìm bài Speak phù hợp cho hỏi ý kiến/xác nhận; luyện cụm đặt quán trong B01 và vai nhân viên ở B05; dùng Nama về đề xuất/nhờ để luyện khi đổi số người. Đây là hướng tuyển chọn, chưa phải xác nhận đã chọn các unit cuối cùng. Phải đọc và gắn con trỏ trước khi soạn.

**Gối đầu:** bài mới xem hai bài trước và những bài cũ liên quan. Từ hỏi ý kiến đã học ở chọn quán có thể quay lại khi chọn lịch chuyển nhà; mẫu xin giải thích có thể quay lại tại ngân hàng. Dùng lại với mục tiêu nói mới, không sao chép nguyên bài kiến thức rồi gọi là bài mới. Theo dõi nơi dạy lần đầu, nơi ôn và phần mở rộng; nguồn chưa chọn không mặc nhiên là bỏ sót cần bù.

## Cách duyệt và tiến tới V5

Bản preview có ID tạm `V5P-xxx`; số này truy về đề xuất gốc, không phải thứ tự học hay UID chính thức. Các câu tình huống mới vẫn có trạng thái đề xuất biên tập. Chưa có thẻ nào đủ điều kiện tự động sinh bài.

Có thể phản hồi theo dạng: **“V5P-018 giữ; V5P-022 gộp vào 018; V5P-065 để nhánh phụ huynh; V5P-118 cho bắt đầu Trung; DL08 cần thành nhánh ngoài trời.”** Sửa theo ID, không cần viết lại cả lộ trình.

Sau khi duyệt: chốt phạm vi chặng mẹ/con; gắn vị trí dự kiến và UID mới; kiểm trùng mục tiêu dạy mới; đọc sâu nguồn theo từng chặng được chọn; rồi mới pilot bài học. Giữ checkpoint và revision theo skill đang có. Không cần kiểm kê chi tiết mọi trang của mọi sách trước khi pilot, cũng không chạy sinh hàng loạt từ preview này.



## Nhóm P1 nên duyệt trước

P1 là thứ tự ưu tiên đầu tư nội dung; mỗi người chỉ cần chọn nhánh phù hợp. Không phải yêu cầu viết hết nhóm này ngay.

### Đời sống

- **V5P-001 — Đi siêu thị và lo bữa ăn hằng ngày** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-005 — Mua điện máy, giao hàng và lắp đặt** · Trung · Tách từ chặng hiện có
- **V5P-009 — Đi cắt tóc và trao đổi kiểu tóc** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-017 — Mở, chuyển và ngừng điện, nước, gas** · Trung · Tách từ chặng hiện có
- **V5P-018 — Báo hỏng trong nhà và hẹn người sửa** · Trung · Tách từ chặng hiện có
- **V5P-019 — Phân loại, đăng ký và giao rác cồng kềnh** · Sơ → Trung · Bổ sung chặng
- **V5P-020 — Làm việc với công ty chuyển nhà** · Trung · Tách từ chặng hiện có
- **V5P-025 — Đến shiyakusho khi chuyển đến hoặc đổi thông tin** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-027 — Trao đổi tại Nyukan về tình trạng cư trú** · Trung → Thượng · Tách từ chặng hiện có
- **V5P-032 — Chuyển đổi và hỏi về bảo hiểm y tế** · Trung · Tách từ chặng hiện có
- **V5P-033 — Xử lý vấn đề tài khoản tại ngân hàng** · Trung · Tách từ chặng hiện có
- **V5P-035 — Liên hệ về thanh toán thẻ và giao dịch lạ** · Trung · Bổ sung chặng
- **V5P-036 — Đăng ký, chuyển mạng và sửa dịch vụ điện thoại, internet** · Trung · Tách từ chặng hiện có
- **V5P-041 — Đi tàu hằng ngày: IC, vé tháng và quầy hỗ trợ** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-042 — Tàu ngừng chạy, lỡ chuyến cuối và đổi đường** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-045 — Mua, gửi và xử lý sự cố xe đạp** · Sơ → Trung · Bổ sung chặng
- **V5P-049 — Đi nha sĩ từ đặt lịch đến tái khám** · Sơ → Trung · Bổ sung chặng
- **V5P-051 — Khám sức khỏe định kỳ và trao đổi kết quả** · Trung · Tách từ chặng hiện có
- **V5P-056 — Nhận thuốc theo đơn và dùng thuốc lâu dài** · Trung · Tách từ chặng hiện có
- **V5P-057 — Báo sự việc khẩn cấp với cảnh sát** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-058 — Gọi hỗ trợ y tế khẩn cấp** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-059 — Báo cháy và phối hợp khi được hướng dẫn** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-060 — Đến koban báo mất, nhận và trả đồ thất lạc** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-062 — Đến nơi sơ tán và sống tạm trong cộng đồng** · Sơ → Trung · Tách từ chặng hiện có
- **V5P-065 — Gửi con ở nhà trẻ và trao đổi hằng ngày** · Trung · Tách từ chặng hiện có
- **V5P-073 — Đến trung tâm hỗ trợ người nước ngoài** · Sơ → Trung · Bổ sung chặng
- **V5P-125 — Mất thẻ cư trú hoặc hộ chiếu khi đang sống ở Nhật** · Trung · Bổ sung chặng

### Công việc

- **V5P-081 — Đến Hello Work để tìm việc phù hợp** · Sơ → Trung · Bổ sung chặng
- **V5P-083 — Phỏng vấn chuyển ngành và giải thích chặng nghỉ nghề** · Trung → Thượng · Tách từ chặng hiện có
- **V5P-084 — Trao đổi offer và quyết định nhận việc** · Trung → Thượng · Bổ sung chặng
- **V5P-086 — Xin nghỉ việc và xử lý cuộc trao đổi với sếp** · Trung → Thượng · Tách từ chặng hiện có
- **V5P-091 — Hỏi bảng lương, chấm công và khoản làm thêm** · Trung · Tách từ chặng hiện có
- **V5P-093 — Trình bày vấn đề với quầy tư vấn lao động** · Trung → Thượng · Bổ sung chặng
- **V5P-097 — Phối hợp công việc giữa các bộ phận** · Trung → Thượng · Bổ sung chặng
- **V5P-098 — Làm rõ brief và tiêu chí trước khi nhận việc** · Trung · Bổ sung chặng
- **V5P-099 — Phối hợp tiến độ và việc phụ thuộc lẫn nhau** · Trung → Thượng · Bổ sung chặng
- **V5P-104 — Hướng dẫn người mới và theo dõi OJT** · Trung → Thượng · Tách từ chặng hiện có
- **V5P-113 — Làm việc nhiều ngày tại công ty khách hàng** · Trung → Thượng · Tách từ chặng hiện có
- **V5P-118 — Làm 幹事 cho nomikai và tiệc đón tiễn** · Trung → Thượng · Tách từ chặng hiện có
- **V5P-120 — Làm người phụ trách chuyến du lịch công ty** · Trung → Thượng · Làm rõ chặng cũ
- **V5P-121 — Làm theo ca: xếp ca, đổi ca và hỗ trợ người vắng** · Sơ → Trung · Bổ sung chặng
- **V5P-122 — Nhận việc tại xưởng và xác nhận trước khi làm** · Sơ → Trung · Tách từ chặng hiện có
