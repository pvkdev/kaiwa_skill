# Kaiwa V5 — lộ trình nghe và nói

> **“Bạn chỉ giỏi kaiwa khi bạn nói đủ nhiều.”**

**289 chặng · 33 cụm · 1304 họ sự kiện · 5914 tình huống nói.**

Đây là khung lộ trình và bản thiết kế tình huống chi tiết. Chưa phải toàn bộ bài học, danh sách từ/ngữ pháp hay hội thoại Nhật–Việt đã được biên soạn.

27 sách là nền tài nguyên; nghiên cứu ngoài và AI viết mới có vai trò thiết yếu. Mọi tình huống mới ở bản này đều ghi AI biên soạn. Token sách kế thừa và đầu mối tra tiếp không được coi là nguồn xác nhận cho mọi tình huống mới.

Thứ tự là gợi ý từ dễ đến khó; người học mở tự do theo nhu cầu. Sơ luyện thông tin cụ thể và nhận hỗ trợ; Trung giải thích, điều chỉnh và xử lý nhánh; Thượng thương lượng, điều phối và quan hệ phức tạp. Không bài viết/email/điền form, không kiểm tra, điểm hay cổng mở bài.

Giữ UID của **185** chặng cũ, phân lại nội dung **9** chặng quá rộng/tổng hợp, thêm **104** chặng. Mã hiển thị được đánh lại; dùng UID hoặc stage key khi chỉnh sửa.

- [Đọc đầy đủ Sơ cấp](SO_CAP.md)
- [Đọc đầy đủ Trung cấp](TRUNG_CAP.md)
- [Đọc đầy đủ Thượng cấp](THUONG_CAP.md)
- [Tra cứu và lọc tương tác](ROADMAP.html)
- [Phạm vi, nguồn, kế thừa và kế hoạch biên soạn](DESIGN_AND_MIGRATION.md)
- [16 bối cảnh du lịch để lồng ghép](TRAVEL_CONTEXTS.md)
- [Kiểm tra biên tập và giới hạn](EDITORIAL_REVIEW.md)

## Sơ — 80 chặng

### S01 — Mở miệng, làm quen và hỏi cho rõ

- **S-001 — Chào hỏi theo thời điểm & hoàn cảnh** · Đời sống · 3 sự kiện / 15 tình huống · key `S-01`
- **S-002 — Tự giới thiệu & hỏi về người khác** · Đời sống · 3 sự kiện / 15 tình huống · key `S-03`
- **S-003 — Nghe không rõ, hỏi lại & giữ nhịp hội thoại** · Đời sống · 3 sự kiện / 15 tình huống · key `S-05`
- **S-004 — Đồ vật, số, giờ, ngày tháng & tiền** · Đời sống · 3 sự kiện / 15 tình huống · key `S-06`

### S02 — Có chỗ ở và biết khu phố

- **S-005 — Tìm & thuê nhà** · Đời sống · 3 sự kiện / 15 tình huống · key `S-07`
- **S-006 — Gia đình & sống cùng gia đình chủ nhà** · Đời sống · 4 sự kiện / 16 tình huống · key `S-11`
- **S-007 — Sinh hoạt trong nhà & với hàng xóm** · Đời sống · 3 sự kiện / 15 tình huống · key `S-09`
- **S-008 — Vào và sống trong ký túc xá, nhà công ty** · Đời sống · 3 sự kiện / 15 tình huống · key `V5P-024`
- **S-009 — Khu phố, thư viện và cơ sở cộng đồng** · Đời sống · 4 sự kiện / 21 tình huống · key `S-12`

### S03 — Tự đi lại trong thành phố

- **S-010 — Hỏi đường & chỉ đường** · Đời sống · 3 sự kiện / 15 tình huống · key `S-13`
- **S-011 — Tàu điện & xe buýt** · Đời sống · 3 sự kiện / 15 tình huống · key `S-14`
- **S-012 — Đi tàu hằng ngày: IC, vé tháng và quầy hỗ trợ** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-041`
- **S-013 — Mua, gửi và xử lý sự cố xe đạp** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-045`
- **S-014 — Đi xa: shinkansen, taxi và quầy hướng dẫn** · Đời sống · 4 sự kiện / 21 tình huống · key `S-17`

### S04 — Bắt đầu một ngày làm việc

- **S-015 — Chào hỏi & trò chuyện hằng ngày ở công sở** · Công việc · 3 sự kiện / 14 tình huống · key `S-02`
- **S-016 — Ngày đầu ở công ty** · Công việc · 3 sự kiện / 13 tình huống · key `S-04`
- **S-017 — Tìm chỗ & dùng đồ trong văn phòng** · Công việc · 3 sự kiện / 13 tình huống · key `S-08`
- **S-018 — Nội quy & phép tắc nơi làm việc** · Công việc · 3 sự kiện / 13 tình huống · key `S-10`
- **S-019 — Đi làm đúng giờ & công tác ngắn** · Công việc · 3 sự kiện / 13 tình huống · key `S-15`
- **S-020 — Lịch trình & chỉ thị trong ngày** · Công việc · 3 sự kiện / 12 tình huống · key `S-16`
- **S-021 — Nhận chỉ thị & hỏi lại** · Công việc · 4 sự kiện / 15 tình huống · key `S-43`
- **S-022 — Nhận việc tại xưởng và xác nhận trước khi làm** · Công việc · 4 sự kiện / 16 tình huống · key `V5P-122`

### S05 — Mua đồ, ăn uống và dịch vụ gần nhà

- **S-023 — Konbini và dịch vụ nhanh hằng ngày** · Đời sống · 4 sự kiện / 20 tình huống · key `S-21`
- **S-024 — Đi siêu thị và lo bữa ăn hằng ngày** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-001`
- **S-025 — Quần áo: chọn, thử và so sánh** · Đời sống · 4 sự kiện / 20 tình huống · key `S-22`
- **S-026 — Đi trung tâm thương mại và quầy thông tin** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-002`
- **S-027 — Đi home center và mua đồ cho căn nhà** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-003`
- **S-028 — Mua và bán tại recycle shop** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-004`
- **S-029 — Đi cửa hàng kính và chọn kính phù hợp** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-006`
- **S-030 — Giặt khô, sửa quần áo và sửa giày** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-013`
- **S-031 — Nhà hàng & quán ăn** · Đời sống · 4 sự kiện / 20 tình huống · key `S-18`
- **S-032 — Quán cà phê, fast-food & thanh toán** · Đời sống · 4 sự kiện / 20 tình huống · key `S-20`
- **S-033 — Ăn trưa cùng đồng nghiệp** · Công việc · 3 sự kiện / 13 tình huống · key `S-19`
- **S-034 — Đi cắt tóc và trao đổi kiểu tóc** · Đời sống · 5 sự kiện / 24 tình huống · key `V5P-009`

### S06 — Nhờ, xin phép, xin lỗi và báo lại

- **S-035 — Nhờ vả & đề nghị lịch sự** · Đời sống · 4 sự kiện / 20 tình huống · key `S-25`
- **S-036 — Xin phép, hỏi khả năng & ngỏ ý giúp** · Đời sống · 4 sự kiện / 20 tình huống · key `S-27`
- **S-037 — Nhờ hỗ trợ và xin phép ở công ty** · Công việc · 3 sự kiện / 13 tình huống · key `S-26`
- **S-038 — Xin lỗi & phàn nàn** · Đời sống · 4 sự kiện / 20 tình huống · key `S-28`
- **S-039 — Xin lỗi & báo vấn đề ở công ty** · Công việc · 3 sự kiện / 12 tình huống · key `S-29`
- **S-040 — Báo ốm & xin nghỉ** · Công việc · 3 sự kiện / 12 tình huống · key `S-32`
- **S-041 — Báo – liên – tương & báo cáo ngắn** · Công việc · 3 sự kiện / 12 tình huống · key `S-45`

### S07 — Gọi điện, đến quầy và tìm hỗ trợ

- **S-042 — Gọi điện cho bạn, thầy cô & đặt chỗ** · Đời sống · 4 sự kiện / 20 tình huống · key `S-36`
- **S-043 — Điện thoại công sở: nghe & chuyển máy** · Công việc · 3 sự kiện / 12 tình huống · key `S-37`
- **S-044 — Điện thoại công sở: gọi đi & lời nhắn** · Công việc · 3 sự kiện / 12 tình huống · key `S-39`
- **S-045 — Gọi đặt dịch vụ và xác nhận yêu cầu cơ bản** · Đời sống · 5 sự kiện / 25 tình huống · key `S-38`
- **S-046 — Ngân hàng và bưu điện: giao dịch cơ bản tại quầy** · Đời sống · 4 sự kiện / 20 tình huống · key `S-42`
- **S-047 — Đến quầy hành chính và xin giải thích dễ hiểu** · Đời sống · 4 sự kiện / 16 tình huống · key `S-44`
- **S-048 — Đến trung tâm hỗ trợ người nước ngoài** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-073`

### S08 — Sức khỏe và lời nhờ giúp thiết yếu

- **S-049 — Nói về sức khỏe & đi bệnh viện** · Đời sống · 4 sự kiện / 16 tình huống · key `S-31`
- **S-050 — Hiệu thuốc & giữ gìn sức khỏe** · Đời sống · 4 sự kiện / 16 tình huống · key `S-33`
- **S-051 — Đi nha sĩ từ đặt lịch đến tái khám** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-049`
- **S-052 — Nhờ giúp khi khẩn cấp và tìm đúng đầu mối** · Đời sống · 5 sự kiện / 20 tình huống · key `S-34`
- **S-053 — Báo sự việc khẩn cấp với cảnh sát** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-057`
- **S-054 — Gọi hỗ trợ y tế khẩn cấp** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-058`
- **S-055 — Báo cháy và phối hợp khi được hướng dẫn** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-059`
- **S-056 — Đến koban báo mất, nhận và trả đồ thất lạc** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-060`
- **S-057 — Đến nơi sơ tán và sống tạm trong cộng đồng** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-062`
- **S-058 — An toàn & sơ tán nơi làm việc** · Công việc · 4 sự kiện / 17 tình huống · key `S-35`

### S09 — Tìm việc làm thêm và làm cùng người khác

- **S-059 — Việc làm thêm: tìm việc & phỏng vấn baito** · Công việc · 4 sự kiện / 16 tình huống · key `S-23`
- **S-060 — Làm theo ca: xếp ca, đổi ca và hỗ trợ người vắng** · Công việc · 4 sự kiện / 17 tình huống · key `V5P-121`
- **S-061 — Làm thêm ở quầy: phục vụ khách cơ bản** · Công việc · 3 sự kiện / 12 tình huống · key `S-24`
- **S-062 — Hẹn gặp, thăm công ty khác & danh thiếp** · Công việc · 3 sự kiện / 12 tình huống · key `S-40`
- **S-063 — Họp & nêu ý kiến** · Công việc · 3 sự kiện / 12 tình huống · key `S-54`

### S10 — Kết bạn và có đời sống riêng

- **S-064 — Rủ rê, hẹn & cuối tuần** · Đời sống · 4 sự kiện / 20 tình huống · key `S-46`
- **S-065 — Sự kiện công ty & trò chuyện nội bộ** · Công việc · 4 sự kiện / 16 tình huống · key `S-47`
- **S-066 — Sở thích: thể thao, phim ảnh & sách** · Đời sống · 4 sự kiện / 20 tình huống · key `S-48`
- **S-067 — Gia nhập và sinh hoạt cùng circle, câu lạc bộ** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-077`
- **S-068 — Tham gia tình nguyện với vai thành viên** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-076`
- **S-069 — Hẹn hò đầu tiên** · Đời sống · 4 sự kiện / 20 tình huống · key `S-49`
- **S-070 — Quan tâm & động viên bạn bè** · Đời sống · 4 sự kiện / 16 tình huống · key `S-50`
- **S-071 — Kể chuyện đã làm & trải nghiệm** · Đời sống · 4 sự kiện / 20 tình huống · key `S-51`
- **S-072 — Cảm xúc, mong muốn & dự định** · Đời sống · 4 sự kiện / 20 tình huống · key `S-52`
- **S-073 — Ý kiến, lời khuyên & tin đồn** · Đời sống · 4 sự kiện / 20 tình huống · key `S-53`
- **S-074 — Thời tiết, mùa & lễ hội** · Đời sống · 4 sự kiện / 20 tình huống · key `S-55`

### S11 — Đi chơi, đón người thân và học mỗi ngày 

- **S-075 — Du lịch & khách sạn** · Đời sống · 5 sự kiện / 25 tình huống · key `S-56`
- **S-076 — Đi máy bay nội địa và xử lý hành trình tại sân bay** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-127`
- **S-077 — Đón và hỗ trợ người thân đến chơi ở Nhật** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-128`
- **S-078 — Đi sento, sauna và cơ sở tắm công cộng** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-016`
- **S-079 — Trường học & học tiếng Nhật** · Đời sống · 4 sự kiện / 16 tình huống · key `S-57`
- **S-080 — Tổng hợp: một ngày ở Nhật** · Đời sống · 4 sự kiện / 20 tình huống · key `S-60`

## Trung — 145 chặng

### T01 — Kết nối sâu hơn với người xung quanh

- **T-001 — Làm quen & trò chuyện với người mới** · Đời sống · 5 sự kiện / 25 tình huống · key `T-08`
- **T-002 — Thăm nhà & chào hỏi theo hoàn cảnh** · Đời sống · 5 sự kiện / 25 tình huống · key `T-20`
- **T-003 — Kết thân & trò chuyện** · Đời sống · 5 sự kiện / 25 tình huống · key `T-24`
- **T-004 — Bạn thân: chuyện đời & tâm sự** · Đời sống · 5 sự kiện / 25 tình huống · key `T-26`
- **T-005 — Người quen & hàng xóm: mời, nhờ & xã giao** · Đời sống · 5 sự kiện / 25 tình huống · key `T-27`
- **T-006 — Kể chuyện đời & trải nghiệm** · Đời sống · 5 sự kiện / 25 tình huống · key `T-29`
- **T-007 — Chia sẻ cảm xúc với bạn bè & đồng nghiệp** · Đời sống · 3 sự kiện / 15 tình huống · key `T-40`
- **T-008 — An ủi, đồng cảm & chia buồn** · Đời sống · 3 sự kiện / 15 tình huống · key `T-42`
- **T-009 — Gia đình, vợ chồng & người yêu: chuyện hằng ngày** · Đời sống · 4 sự kiện / 19 tình huống · key `T-47`
- **T-010 — Hẹn hò & tình cảm** · Đời sống · 5 sự kiện / 25 tình huống · key `T-32`
- **T-011 — Quà tặng & lễ nghi tặng quà** · Đời sống · 5 sự kiện / 25 tình huống · key `T-18`
- **T-012 — Nhờ vả, nhận lời & từ chối khéo** · Đời sống · 5 sự kiện / 25 tình huống · key `T-33`
- **T-013 — Ý kiến, lời khuyên & thuyết phục nhẹ** · Đời sống · 5 sự kiện / 25 tình huống · key `T-38`

### T02 — Tự quản cuộc sống và căn nhà

- **T-014 — Tìm, xem và thuê nhà phù hợp** · Đời sống · 6 sự kiện / 30 tình huống · key `T-01`
- **T-015 — Share house & sống chung** · Đời sống · 5 sự kiện / 25 tình huống · key `T-02`
- **T-016 — Mở, chuyển và ngừng điện, nước, gas** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-017`
- **T-017 — Báo hỏng trong nhà và hẹn người sửa** · Đời sống · 6 sự kiện / 30 tình huống · key `V5P-018`
- **T-018 — Phân loại, đăng ký và giao rác cồng kềnh** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-019`
- **T-019 — Làm việc với công ty chuyển nhà** · Đời sống · 6 sự kiện / 30 tình huống · key `V5P-020`
- **T-020 — Làm việc với ban quản lý tòa nhà** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-022`
- **T-021 — Nhận hàng tại nhà và xử lý giao nhầm** · Đời sống · 5 sự kiện / 25 tình huống · key `T-28`
- **T-022 — Đăng ký, chuyển mạng và sửa dịch vụ điện thoại, internet** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-036`
- **T-023 — Gặp để mua bán và trao lại đồ cá nhân** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-038`

### T03 — Dịch vụ cá nhân và nhu cầu mua sắm riêng

- **T-024 — Điện thoại đời sống: đặt chỗ, hỏi thông tin, báo vắng** · Đời sống · 5 sự kiện / 25 tình huống · key `T-11`
- **T-025 — Điện thoại: đặt hàng, nhờ giao hàng & hỏi thông tin** · Đời sống · 5 sự kiện / 25 tình huống · key `T-13`
- **T-026 — Mua sắm nâng cao: so sánh, đổi trả, đặt hàng** · Đời sống · 6 sự kiện / 30 tình huống · key `T-58`
- **T-027 — Nói rõ ý mình với nhân viên cửa hàng: nhờ tư vấn & từ chối khéo** · Đời sống · 7 sự kiện / 36 tình huống · key `T-59`
- **T-028 — Mua điện máy, giao hàng và lắp đặt** · Đời sống · 6 sự kiện / 31 tình huống · key `V5P-005`
- **T-029 — Dùng dịch vụ giao thực phẩm định kỳ** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-007`
- **T-030 — Đi làm nail và dịch vụ chân mày, mi** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-010`
- **T-031 — Đăng ký phòng gym và tập cùng huấn luyện viên** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-015`
- **T-032 — Sống cùng thú cưng: bác sĩ thú y, dịch vụ và khu phố** · Đời sống · 6 sự kiện / 30 tình huống · key `H-12`

### T04 — Làm việc với cơ quan và dịch vụ tài chính

- **T-033 — Đến shiyakusho khi chuyển đến hoặc đổi thông tin** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-025`
- **T-034 — Trao đổi tại Nyukan về tình trạng cư trú** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-027`
- **T-035 — Hỏi thủ tục cư trú cho vợ chồng và con** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-028`
- **T-036 — Trao đổi về thuế tại quầy tư vấn** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-030`
- **T-037 — Làm việc với quầy nenkin** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-031`
- **T-038 — Chuyển đổi và hỏi về bảo hiểm y tế** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-032`
- **T-039 — Xử lý vấn đề tài khoản tại ngân hàng** · Đời sống · 5 sự kiện / 20 tình huống · key `V5P-033`
- **T-040 — Gửi tiền quốc tế và hỏi giao dịch bị vướng** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-034`
- **T-041 — Liên hệ về thanh toán thẻ và giao dịch lạ** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-035`
- **T-042 — Hủy dịch vụ định kỳ và nhờ tư vấn tiêu dùng** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-039`
- **T-043 — Mất thẻ cư trú hoặc hộ chiếu khi đang sống ở Nhật** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-125`
- **T-044 — Gửi bưu kiện cá nhân và hỏi hàng quốc tế** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-123`
- **T-045 — Về Việt Nam tạm thời rồi quay lại sinh hoạt ở Nhật** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-124`
- **T-046 — Rời Nhật dài hạn và bàn giao các việc còn lại** · Đời sống · 4 sự kiện / 16 tình huống · key `V5P-080`

### T05 — Chăm sóc sức khỏe và gia đình

- **T-047 — Khám và tái khám: giải thích triệu chứng, hỏi điều trị** · Đời sống · 4 sự kiện / 20 tình huống · key `T-63`
- **T-048 — Khám sức khỏe định kỳ và trao đổi kết quả** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-051`
- **T-049 — Nhận thuốc theo đơn và dùng thuốc lâu dài** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-056`
- **T-050 — Nhập viện, nằm viện và ra viện** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-052`
- **T-051 — Xin tư vấn khi căng thẳng và sức khỏe tinh thần bị ảnh hưởng** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-054`
- **T-052 — Mang thai & sinh con** · Đời sống · 5 sự kiện / 25 tình huống · key `T-48`
- **T-053 — Nuôi con: chăm sóc hằng ngày và tìm hỗ trợ** · Đời sống · 4 sự kiện / 19 tình huống · key `T-50`
- **T-054 — Gửi con ở nhà trẻ và trao đổi hằng ngày** · Đời sống · 7 sự kiện / 33 tình huống · key `V5P-065`
- **T-055 — Trường học của con** · Đời sống · 6 sự kiện / 30 tình huống · key `T-51`
- **T-056 — Đăng ký juku và lớp ngoại khóa cho con** · Đời sống · 3 sự kiện / 15 tình huống · key `V5P-067`
- **T-057 — Xin tư vấn hỗ trợ phát triển và học tập cho con** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-068`
- **T-058 — Trao đổi khi kết hôn và xây dựng gia đình quốc tế** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-069`
- **T-059 — Đứng ra lo việc tang và liên hệ các bên** · Đời sống · 4 sự kiện / 20 tình huống · key `V5P-071`
- **T-060 — Trao đổi dịch vụ chăm sóc người cao tuổi** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-072`

### T06 — Chọn nghề, ứng tuyển và quyết định nhận việc

- **T-061 — Chọn ngành, thực tập & tự phân tích bản thân** · Công việc · 4 sự kiện / 19 tình huống · key `T-04`
- **T-062 — Gặp tiền bối & dự buổi giới thiệu công ty** · Công việc · 3 sự kiện / 15 tình huống · key `T-05`
- **T-063 — Đến Hello Work để tìm việc phù hợp** · Công việc · 4 sự kiện / 20 tình huống · key `V5P-081`
- **T-064 — Trao đổi với recruiter và nói lý do ứng tuyển** · Công việc · 4 sự kiện / 20 tình huống · key `T-06`
- **T-065 — Phỏng vấn tuyển dụng** · Công việc · 3 sự kiện / 15 tình huống · key `T-07`
- **T-066 — Phỏng vấn chuyển ngành và giải thích chặng nghỉ nghề** · Công việc · 4 sự kiện / 19 tình huống · key `V5P-083`
- **T-067 — Trao đổi offer và quyết định nhận việc** · Công việc · 4 sự kiện / 20 tình huống · key `V5P-084`

### T07 — Nhận việc, phối hợp và giữ nhịp công sở

- **T-068 — Những ngày đầu nhận việc** · Công việc · 3 sự kiện / 12 tình huống · key `T-09`
- **T-069 — Văn phòng: thiết bị, họp trực tuyến & nhờ hỗ trợ** · Công việc · 4 sự kiện / 17 tình huống · key `T-10`
- **T-070 — Đồng nghiệp: chuyện công ty & nhờ giúp** · Công việc · 3 sự kiện / 13 tình huống · key `T-25`
- **T-071 — Động viên, khen & nhận góp ý** · Công việc · 3 sự kiện / 12 tình huống · key `T-31`
- **T-072 — Nhờ vả, đề nghị cấp trên & nhận chỉ thị** · Công việc · 3 sự kiện / 12 tình huống · key `T-34`
- **T-073 — Xin phép & xác nhận lại** · Công việc · 7 sự kiện / 38 tình huống · key `T-35`
- **T-074 — Xin lỗi, xử lý sai sót & đổi lịch hẹn** · Công việc · 3 sự kiện / 12 tình huống · key `T-36`
- **T-075 — Quá tải: nhờ giúp & chủ động giúp đồng nghiệp** · Công việc · 4 sự kiện / 15 tình huống · key `T-37`
- **T-076 — Hỏi ý kiến & xin lời khuyên của cấp trên** · Công việc · 3 sự kiện / 12 tình huống · key `T-39`
- **T-077 — Bày tỏ ý định & bắt chuyện, hỏi đáp** · Công việc · 3 sự kiện / 12 tình huống · key `T-41`
- **T-078 — Văn hóa & quy định công ty Nhật** · Công việc · 3 sự kiện / 12 tình huống · key `T-44`
- **T-079 — Báo – liên – tương nâng cao & hiện trường** · Công việc · 4 sự kiện / 15 tình huống · key `T-45`
- **T-080 — Làm rõ brief và tiêu chí trước khi nhận việc** · Công việc · 4 sự kiện / 16 tình huống · key `V5P-098`
- **T-081 — Phối hợp công việc giữa các bộ phận** · Công việc · 4 sự kiện / 15 tình huống · key `V5P-097`
- **T-082 — Phối hợp tiến độ và việc phụ thuộc lẫn nhau** · Công việc · 4 sự kiện / 15 tình huống · key `V5P-099`
- **T-083 — Hướng dẫn người mới và theo dõi OJT** · Công việc · 4 sự kiện / 16 tình huống · key `V5P-104`
- **T-084 — Review sản phẩm và phản hồi để sửa** · Công việc · 4 sự kiện / 15 tình huống · key `V5P-101`

### T08 — Điện thoại và gặp gỡ trong công việc

- **T-085 — Điện thoại công sở: câu đầu, xác nhận & nghe không rõ** · Công việc · 3 sự kiện / 12 tình huống · key `T-12`
- **T-086 — Chuyển máy, gọi nhầm & để khách chờ** · Công việc · 3 sự kiện / 12 tình huống · key `T-14`
- **T-087 — Nhận & chuyển lời nhắn, gọi lại** · Công việc · 3 sự kiện / 12 tình huống · key `T-15`
- **T-088 — Điện thoại khách hàng: khách giận, khẩn cấp & đàm phán** · Công việc · 4 sự kiện / 15 tình huống · key `T-16`
- **T-089 — Điện thoại tiếp khách dịch vụ** · Công việc · 4 sự kiện / 15 tình huống · key `T-17`
- **T-090 — Tiếp khách, danh thiếp & thăm đối tác** · Công việc · 4 sự kiện / 15 tình huống · key `T-21`
- **T-091 — Gặp đối tác & khách hàng: mở đầu, hỏi lại, hẹn & kết thúc** · Công việc · 4 sự kiện / 15 tình huống · key `T-61`
- **T-092 — Hỏi thông tin & hỏi cách làm với khách** · Công việc · 3 sự kiện / 12 tình huống · key `T-75`
- **T-093 — Xã giao với khách hàng & từ chối lời mời** · Công việc · 4 sự kiện / 15 tình huống · key `T-19`

### T09 — Họp, giải thích và làm việc với khách

- **T-094 — Họp: nghe, hỏi & phát biểu** · Công việc · 4 sự kiện / 15 tình huống · key `T-53`
- **T-095 — Thuyết trình ngắn & giải thích logic** · Công việc · 4 sự kiện / 15 tình huống · key `T-55`
- **T-096 — Giải thích, so sánh & báo cáo kết quả khảo sát** · Công việc · 4 sự kiện / 15 tình huống · key `T-56`
- **T-097 — Động não ý tưởng & nêu cảm nhận về sản phẩm** · Công việc · 4 sự kiện / 15 tình huống · key `T-57`
- **T-098 — Bán hàng cơ bản: giới thiệu sản phẩm & báo giá** · Công việc · 4 sự kiện / 16 tình huống · key `T-60`
- **T-099 — Thương lượng mức vừa & điều khách lo lắng** · Công việc · 4 sự kiện / 16 tình huống · key `T-62`
- **T-100 — Làm việc nhiều ngày tại công ty khách hàng** · Công việc · 5 sự kiện / 20 tình huống · key `V5P-113`
- **T-101 — Đến nhà máy hoặc nhà cung cấp để trao đổi công việc** · Công việc · 4 sự kiện / 15 tình huống · key `V5P-116`
- **T-102 — Demo, nghiệm thu và hướng dẫn khách sử dụng** · Công việc · 5 sự kiện / 19 tình huống · key `V5P-115`
- **T-103 — Đại diện công ty tại triển lãm và hội thảo** · Công việc · 5 sự kiện / 21 tình huống · key `V5P-117`

### T10 — Điều kiện làm việc và chuyển tiếp nghề nghiệp

- **T-104 — Cân bằng công việc & cuộc sống** · Công việc · 3 sự kiện / 15 tình huống · key `T-49`
- **T-105 — Làm việc qua haken và phối hợp hai đầu mối** · Công việc · 4 sự kiện / 19 tình huống · key `V5P-089`
- **T-106 — Trao đổi gia hạn hợp đồng và thay đổi điều kiện làm việc** · Công việc · 4 sự kiện / 20 tình huống · key `V5P-090`
- **T-107 — Hỏi bảng lương, chấm công và khoản làm thêm** · Công việc · 4 sự kiện / 19 tình huống · key `V5P-091`
- **T-108 — Trao đổi đánh giá và phát triển nghề với quản lý** · Công việc · 3 sự kiện / 15 tình huống · key `V5P-092`
- **T-109 — Trình bày vấn đề với quầy tư vấn lao động** · Công việc · 5 sự kiện / 23 tình huống · key `V5P-093`
- **T-110 — Phản ánh hành vi gây tổn hại và xin hỗ trợ ở nơi làm** · Công việc · 4 sự kiện / 19 tình huống · key `V5P-094`
- **T-111 — Báo và phối hợp sau tai nạn tại nơi làm việc** · Công việc · 4 sự kiện / 19 tình huống · key `V5P-095`
- **T-112 — Xin nghỉ dài ngày và trở lại công việc** · Công việc · 4 sự kiện / 19 tình huống · key `V5P-096`
- **T-113 — Xin nghỉ việc và xử lý cuộc trao đổi với sếp** · Công việc · 6 sự kiện / 28 tình huống · key `V5P-086`
- **T-114 — Tìm hỗ trợ và quay lại việc làm sau khi mất việc** · Công việc · 3 sự kiện / 15 tình huống · key `V5P-088`
- **T-115 — Chuyển công tác & lời chia tay** · Công việc · 3 sự kiện / 15 tình huống · key `T-46`

### T11 — Từ người dự tiệc đến người đứng ra tổ chức

- **T-116 — Đi dự nomikai, tiệc công ty và giao lưu** · Công việc · 7 sự kiện / 35 tình huống · key `T-22`
- **T-117 — Làm 幹事 cho nomikai và tiệc đón tiễn** · Công việc · 8 sự kiện / 40 tình huống · key `V5P-118`
- **T-118 — Làm người phụ trách chuyến du lịch công ty** · Công việc · 7 sự kiện / 31 tình huống · key `T-23`

### T12 — Làm dịch vụ: hiểu khách và phối hợp đồng nghiệp

- **T-119 — Nhà hàng: phục vụ từ phía nhân viên** · Công việc · 6 sự kiện / 25 tình huống · key `T-69`
- **T-120 — Cửa hàng bán lẻ & quần áo** · Công việc · 5 sự kiện / 19 tình huống · key `T-71`
- **T-121 — Konbini & quầy thu ngân** · Công việc · 5 sự kiện / 20 tình huống · key `T-72`
- **T-122 — Dịch vụ khác phía nhân viên: karaoke, thuê đồ, lớp học** · Công việc · 5 sự kiện / 20 tình huống · key `T-73`
- **T-123 — Khách sạn: đón khách và xử lý yêu cầu lưu trú** · Công việc · 6 sự kiện / 25 tình huống · key `T-74`
- **T-124 — Cấp cứu, sự cố & đồ bỏ quên (góc nhân viên)** · Công việc · 4 sự kiện / 16 tình huống · key `T-64`

### T13 — Đi xa, trải nghiệm và điều chỉnh kế hoạch

- **T-125 — Nhà hàng nâng cao: kiêng ăn, món sai, phàn nàn** · Đời sống · 6 sự kiện / 30 tình huống · key `T-70`
- **T-126 — Cuối tuần: thể thao, phượt & tiệc** · Đời sống · 6 sự kiện / 30 tình huống · key `T-30`
- **T-127 — Du lịch cùng người thân: bàn kế hoạch và điều chỉnh** · Đời sống · 6 sự kiện / 30 tình huống · key `T-67`
- **T-128 — Ở ryokan và trải nghiệm lưu trú kiểu Nhật** · Đời sống · 3 sự kiện / 15 tình huống · key `V5P-131`
- **T-129 — Thuê xe du lịch từ nhận đến trả** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-126`
- **T-130 — Học lái và làm việc tại trung tâm bằng lái** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-046`
- **T-131 — Sử dụng ô tô: bãi đỗ, gara và bảo dưỡng** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-047`
- **T-132 — Cắm trại hoặc BBQ theo nhóm** · Đời sống · 3 sự kiện / 15 tình huống · key `V5P-132`
- **T-133 — Công tác xa: phối hợp lịch đi, lưu trú và báo lại** · Công việc · 5 sự kiện / 20 tình huống · key `T-66`
- **T-134 — Tàu ngừng chạy, lỡ chuyến cuối và đổi đường** · Đời sống · 6 sự kiện / 30 tình huống · key `V5P-042`
- **T-135 — Trao đổi sau va chạm và khi xe gặp sự cố** · Đời sống · 6 sự kiện / 30 tình huống · key `V5P-048`
- **T-136 — Tham gia workshop văn hóa và làm đồ thủ công** · Đời sống · 5 sự kiện / 25 tình huống · key `V5P-129`
- **T-137 — Đi xem concert, sân vận động và biểu diễn trực tiếp** · Đời sống · 3 sự kiện / 15 tình huống · key `V5P-130`
- **T-138 — Bình luận phim, sách & tin tức** · Đời sống · 5 sự kiện / 25 tình huống · key `T-43`
- **T-139 — Phong tục & sự kiện theo mùa** · Đời sống · 6 sự kiện / 31 tình huống · key `T-68`

### T14 — Sống chủ động, học tiếp và xử lý biến cố

- **T-140 — Phòng chống thiên tai & di chuyển an toàn** · Đời sống · 3 sự kiện / 15 tình huống · key `T-65`
- **T-141 — Xin hỗ trợ khi bị đe dọa, theo dõi hoặc bạo lực** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-061`
- **T-142 — Trao đổi để ổn định cuộc sống sau thiên tai** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-063`
- **T-143 — Tư vấn học tập & du học** · Đời sống · 3 sự kiện / 15 tình huống · key `T-52`
- **T-144 — Tham gia đào tạo nghề và học lại khi đi làm** · Đời sống · 3 sự kiện / 15 tình huống · key `V5P-075`
- **T-145 — Tổng hợp: một tuần ở công ty & ngoài đời** · Công việc · 4 sự kiện / 16 tình huống · key `T-76`

## Thượng — 64 chặng

### H01 — Hiện diện chuyên nghiệp và giữ quan hệ

- **H-001 — Tự giới thiệu & chào cảm ơn người giúp đỡ** · Công việc · 4 sự kiện / 16 tình huống · key `H-01`
- **H-002 — Nhận vị trí mới & ra mắt đội** · Công việc · 4 sự kiện / 16 tình huống · key `H-02`
- **H-003 — Điện thoại đối ngoại & hẹn gặp khách mới** · Công việc · 4 sự kiện / 16 tình huống · key `H-04`
- **H-004 — Kính ngữ đối ngoại & chuyển lời xã giao** · Công việc · 4 sự kiện / 15 tình huống · key `H-38`
- **H-005 — Đổi cách nói theo quan hệ và hoàn cảnh** · Đời sống · 5 sự kiện / 25 tình huống · key `H-37`
- **H-006 — Ghi nhận công sức, khen & đáp lời khen** · Công việc · 4 sự kiện / 16 tình huống · key `H-27`
- **H-007 — Chào chia tay công ty và giữ quan hệ sau chuyển việc** · Công việc · 3 sự kiện / 15 tình huống · key `H-30`
- **H-008 — Họp bữa trưa & bàn chuyện kinh doanh tự nhiên** · Công việc · 4 sự kiện / 16 tình huống · key `H-47`
- **H-009 — Tiếp đãi & ăn uống với đối tác** · Công việc · 5 sự kiện / 20 tình huống · key `H-23`

### H02 — Đàm phán và phát triển quan hệ kinh doanh

- **H-010 — Khai thác khách mới & chào bán** · Công việc · 5 sự kiện / 20 tình huống · key `H-20`
- **H-011 — Đề nghị hợp tác & thăm dò ý định** · Công việc · 5 sự kiện / 20 tình huống · key `H-21`
- **H-012 — Thuyết phục bằng chiến lược** · Công việc · 5 sự kiện / 20 tình huống · key `H-22`
- **H-013 — Đàm phán, giá cả & hợp đồng** · Công việc · 6 sự kiện / 24 tình huống · key `H-32`
- **H-014 — Thương lượng giá bán buôn & giảm chi phí** · Công việc · 6 sự kiện / 24 tình huống · key `H-33`
- **H-015 — Thống nhất thay đổi yêu cầu với khách hàng** · Công việc · 6 sự kiện / 24 tình huống · key `V5P-114`
- **H-016 — Chốt đơn, thương mại quốc tế & giữ quan hệ** · Công việc · 6 sự kiện / 24 tình huống · key `H-24`
- **H-017 — Bàn công việc phụ và dự án cá nhân có khách hàng** · Công việc · 4 sự kiện / 19 tình huống · key `V5P-133`

### H03 — Lắng nghe sâu, phản biện và dẫn dắt trao đổi

- **H-018 — Phỏng vấn lấy thông tin và khai thác câu chuyện** · Công việc · 5 sự kiện / 19 tình huống · key `H-07`
- **H-019 — Phỏng vấn tuyển người từ vai người tuyển dụng** · Công việc · 6 sự kiện / 24 tình huống · key `V5P-109`
- **H-020 — Họp: tham gia, đề xuất & phản biện** · Công việc · 5 sự kiện / 20 tình huống · key `H-06`
- **H-021 — Phản biện, tranh luận & giữ thể diện** · Công việc · 5 sự kiện / 20 tình huống · key `H-35`
- **H-022 — Lãnh đạo họp, kết luận & dẫn dắt quyết định** · Công việc · 6 sự kiện / 23 tình huống · key `H-45`
- **H-023 — Thuyết trình: mở đầu, nội dung, kết** · Công việc · 6 sự kiện / 24 tình huống · key `H-48`
- **H-024 — Nemawashi: trao đổi trước để tạo đồng thuận** · Công việc · 6 sự kiện / 24 tình huống · key `H-40`

### H04 — Làm leader và phát triển đội ngũ

- **H-025 — Làm leader: trao đổi riêng và hỗ trợ thành viên** · Công việc · 6 sự kiện / 24 tình huống · key `V5P-105`
- **H-026 — Làm leader: ưu tiên, nguồn lực và ngân sách** · Công việc · 6 sự kiện / 24 tình huống · key `H-41`
- **H-027 — Làm leader: giao trách nhiệm và quyền quyết định** · Công việc · 6 sự kiện / 24 tình huống · key `V5P-107`
- **H-028 — Bàn giao công việc và trách nhiệm khi thay người** · Công việc · 6 sự kiện / 24 tình huống · key `H-44`
- **H-029 — Giải quyết bất đồng giữa đồng đội** · Công việc · 6 sự kiện / 24 tình huống · key `V5P-102`
- **H-030 — Với cấp trên: xin chỉ đạo, ký duyệt & nhận phê bình** · Công việc · 5 sự kiện / 20 tình huống · key `H-42`
- **H-031 — Làm leader khi xảy ra sự cố trong nhóm** · Công việc · 6 sự kiện / 24 tình huống · key `V5P-111`
- **H-032 — Họp nhìn lại và đề xuất cải tiến công việc** · Công việc · 6 sự kiện / 24 tình huống · key `V5P-112`
- **H-033 — Báo cáo lên cấp cao & phản hồi dự án** · Công việc · 5 sự kiện / 20 tình huống · key `H-19`

### H05 — Giải quyết sự cố và phục vụ trong hoàn cảnh khó

- **H-034 — Nhận khiếu nại & xin lỗi chính thức** · Công việc · 6 sự kiện / 24 tình huống · key `H-14`
- **H-035 — Báo cáo khiếu nại, xử lý sự cố & hàng lỗi** · Công việc · 7 sự kiện / 28 tình huống · key `H-16`
- **H-036 — Báo sự cố cho cấp trên & giải tỏa lo ngại** · Công việc · 5 sự kiện / 20 tình huống · key `H-18`
- **H-037 — Nghề dịch vụ cao cấp & omotenashi** · Công việc · 6 sự kiện / 24 tình huống · key `H-25`
- **H-038 — Công tác gấp & chuyển chi nhánh: sân bay, hải quan, hủy chuyến** · Công việc · 7 sự kiện / 28 tình huống · key `H-03`

### H06 — Thương lượng đời sống và quyết định nhạy cảm

- **H-039 — Phàn nàn dịch vụ & lấy lại quyền lợi** · Đời sống · 6 sự kiện / 30 tình huống · key `H-13`
- **H-040 — Mua sắm & dịch vụ cao cấp: đặt may, hợp đồng, đổi trả khó** · Đời sống · 7 sự kiện / 36 tình huống · key `H-15`
- **H-041 — Du lịch: sự cố & đàm phán dịch vụ** · Đời sống · 6 sự kiện / 30 tình huống · key `H-17`
- **H-042 — Nhà ở lâu dài: thương lượng trách nhiệm và giải quyết bất đồng** · Đời sống · 6 sự kiện / 30 tình huống · key `H-10`
- **H-043 — Khai báo sự việc và hỏi hồ sơ bồi thường bảo hiểm** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-040`
- **H-044 — Khám chuyên khoa và trao đổi quyết định điều trị** · Đời sống · 6 sự kiện / 29 tình huống · key `H-09`
- **H-045 — Tìm hỗ trợ khi ly thân và thay đổi hoàn cảnh gia đình** · Đời sống · 4 sự kiện / 19 tình huống · key `V5P-070`
- **H-046 — Gia đình: vợ chồng, cha mẹ & con cái** · Đời sống · 4 sự kiện / 19 tình huống · key `H-08`
- **H-047 — Tâm sự: tình cảm, sức khỏe & giấc ngủ** · Đời sống · 3 sự kiện / 15 tình huống · key `H-26`
- **H-048 — Khác biệt quan điểm & giữ quan hệ** · Đời sống · 6 sự kiện / 30 tình huống · key `H-28`
- **H-049 — Nhờ việc khó với người thân & nêu điều kiện** · Đời sống · 6 sự kiện / 30 tình huống · key `H-29`
- **H-050 — Nhờ việc khó, từ chối và thương lượng giới hạn** · Đời sống · 6 sự kiện / 30 tình huống · key `H-34`
- **H-051 — Cảm xúc tinh tế: bất mãn, đành chịu, hoài nghi, coi nhẹ** · Đời sống · 4 sự kiện / 19 tình huống · key `H-39`

### H07 — Điều phối sự kiện, gia đình và cộng đồng

- **H-052 — Cưới hỏi, tang lễ & phát biểu nghi thức** · Đời sống · 4 sự kiện / 19 tình huống · key `H-31`
- **H-053 — Dẫn chương trình và điều phối sự kiện công ty** · Công việc · 9 sự kiện / 41 tình huống · key `H-46`
- **H-054 — Hàng xóm, người quen & chuyện xã hội** · Đời sống · 6 sự kiện / 30 tình huống · key `H-11`
- **H-055 — Jichikai, PTA và điều phối việc cộng đồng** · Đời sống · 6 sự kiện / 30 tình huống · key `H-55`
- **H-056 — Kể chuyện có điểm chốt & hồi ức** · Đời sống · 6 sự kiện / 30 tình huống · key `H-36`

### H08 — Mở rộng thế giới mình có thể trò chuyện

- **H-057 — Văn hóa đại chúng & giải trí: manga, anime, thể thao** · Đời sống · 5 sự kiện / 25 tình huống · key `H-49`
- **H-058 — Ẩm thực, thủ công & tập quán** · Đời sống · 6 sự kiện / 30 tình huống · key `H-50`
- **H-059 — Lịch sử, địa lý & thiên nhiên** · Đời sống · 6 sự kiện / 30 tình huống · key `H-51`
- **H-060 — Xã hội, chính trị & giáo dục** · Đời sống · 6 sự kiện / 30 tình huống · key `H-52`
- **H-061 — Kinh tế, công nghệ & vấn đề toàn cầu** · Đời sống · 6 sự kiện / 30 tình huống · key `H-53`
- **H-062 — Trao đổi học thuật và học tập lâu dài** · Đời sống · 4 sự kiện / 19 tình huống · key `H-56`
- **H-063 — Tổng hợp A: một ngày ở Nhật không kịch bản** · Đời sống · 6 sự kiện / 30 tình huống · key `H-57`
- **H-064 — Tổng hợp B: một dự án từ đầu đến cuối** · Công việc · 9 sự kiện / 36 tình huống · key `H-58`
