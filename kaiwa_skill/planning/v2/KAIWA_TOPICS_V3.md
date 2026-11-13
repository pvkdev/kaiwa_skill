# KAIWA V3 — Lộ trình 400 chặng, đời sống và công việc đan xen, từ zero đến hero ở Nhật

Ngày: 2026-11-12 · Thay thế `TOPIC_CANDIDATES_V2.md` (196 chặng). Dựng lại từ 27 sách + memo web S01–S22 bằng script, kèm kiểm tra phủ nguồn.
Đi kèm: `KAIWA_TOPICS_V3.jsonl` (mỗi dòng 1 chặng: id, level, arc, track, title, sources).

## 0. Trả lời nhanh

**Tsunagaru (S01) và NHK:** ở bản V2 mình mới dùng NHK 48 đầy đủ; Tsunagaru chỉ trích theo dải, còn NHK-công sở chỉ nêu rõ 10/43 bài. Bản V3 này đã đối chiếu từng mục: **S01 60/60, NHK 48/48, NHK-công sở 43/43** đều gắn vào ít nhất một chặng (bài #31, #32, #34 của NHK-công sở không tồn tại trong nguồn nên không tính).

**Số lượng:** 400 chặng — Sơ 155 · Trung 134 · Thượng 111. Trong đó **355 chặng bối cảnh** (đời sống/công việc) và **45 chặng mini** (phản xạ & mẫu câu, 1 buổi ngắn). Vượt mức 250–300 bạn đặt ra; nếu muốn gọn, bỏ 45 chặng mini là còn 355.

**Xen kẽ:** trong mỗi level, danh sách đi theo nhịp đời sống ↔ công việc ↔ chặng mini; không còn khối thuần một loại (tối đa 2 chặng cùng loại liên tiếp).

## 1. Hành trình

Nhân vật: người học sang Nhật, vừa sống vừa làm.

- **Sơ — Năm 1 (12 tháng):** sinh tồn & công ty ở mức baito/thực tập. Bám NHK 48 làm xương sống, Tsunagaru S01 làm bối cảnh, B08/B01/B07 làm ngân hàng câu, B17 làm Roleplay đầu.
- **Trung — Năm 2–3 (24 tháng):** chuyển thành nhân viên chính thức, điện thoại, tiếp khách, nuôi con, trường học, kính ngữ. B21–23, B02, B04, B05, B16, B26/27.
- **Thượng — Năm 4–6 (36 tháng):** khiếu nại, đàm phán, lãnh đạo họp, quan hệ tinh tế, văn hóa Nhật, nói như người bản địa. B15, B13 phần cao cấp, B24, B20, B25.

Mỗi level gồm 12 giai đoạn ('arc'), tên giai đoạn nêu cả đời sống và công việc.

## 2. Số liệu

| Level | Đời sống | Công việc | Mini | Tổng |
|---|---|---|---|---|
| Sơ | 96 | 49 | 10 | 155 |
| Trung | 51 | 60 | 23 | 134 |
| Thượng | 51 | 48 | 12 | 111 |
| **Tổng** | 198 | 157 | 45 | **400** |

## 3. Danh sách chặng

Cột 'Loại': ĐS = đời sống, CV = công việc, PX = chặng mini phản xạ/mẫu. Nguồn viết tắt: `N` NHK 48, `W` NHK-công sở, `S01` Tsunagaru, `Sxx` memo web khác, `Bxx` sách. **[AI]** = không có nguồn sách, cần AI bổ sung tình huống.

### Level Sơ


#### Tháng 1 — Chạm đất, mở miệng lần đầu: chào, tự giới thiệu, ngày đầu ở công ty

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-001 | ĐS | Chào hỏi theo thời điểm & hoàn cảnh | S01 T1,A1-1,A2-1 · B08 P1-01,P2-01 · B14 U1 |
| S-002 | CV | Nhớ tên đồng nghiệp & hỏi cách đọc tên | W 11 · B04 U30 |
| S-003 | ĐS | Tự giới thiệu: tên, nghề, nơi xuất thân | N 2,3 · B08 P2-02 · S08 1 · B21 L1 · B22 L1 · B23 L1 |
| S-004 | CV | Cảm ơn & nhận lời cảm ơn ở công ty | W 1 · S07 4 |
| S-005 | ĐS | Gia đình & giới thiệu người khác | N 8 · B08 P5-03 · S05 T1 |
| S-006 | ĐS | Nghe không rõ: hỏi lại, nhờ nói chậm | N 7 · S08 2 · B21 L2 · B22 L2 · B23 L2 |
| S-007 | CV | Ngày đầu đến công ty: chào hỏi & tự giới thiệu | S01 B1-1 · S17 1,5 · B17 L1 · B10 1 · B02 S3 · S07 5,6 |
| S-008 | PX | Câu ngắn phản xạ (1): cảm nhận & cảm xúc | B07 P1-2 |
| S-009 | ĐS | Hỏi tên đồ vật: "cái này là gì?" | N 9 |
| S-010 | ĐS | Số, giờ, ngày tháng, tiền [AI] | N 36 |
| S-011 | CV | Chào hỏi hằng ngày ở công sở: đến làm, ra về, gặp khách | S17 2 · B10 2 |
| S-012 | ĐS | Cảm ơn, xin lỗi & đáp lại | B01 C2 · B08 P2-03 |

#### Tháng 2 — Nhà ở & khu phố: tìm nhà, hàng xóm, nơi để đồ

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-013 | ĐS | Nói thứ mình thích và không thích | N 23 · S04 T6 |
| S-014 | CV | Hỏi nơi để đồ, phòng họp, chỗ trong công ty | B08 P4-17,P4-18 · S01 T6 |
| S-015 | ĐS | Hỏi địa điểm: "ở đâu?" | N 1 · S08 3 |
| S-016 | ĐS | Nói mình đang ở chỗ nào | N 21 |
| S-017 | CV | Lịch làm việc: chia sẻ & xác nhận giờ giấc | S14 6,7 |
| S-018 | ĐS | Nhà ở: số phòng, nhận xét căn phòng | S04 T4 |
| S-019 | ĐS | Nhà môi giới & thuê nhà cơ bản | B08 P4-21 |
| S-020 | CV | Hỏi đồng nghiệp: văn phòng phẩm ở đâu, máy dùng thế nào | B02 S13,S14,S15 |
| S-021 | ĐS | Hàng xóm: chào hỏi & nói chuyện | S01 T4 · B08 P4-22,P4-20 · B26 10 |
| S-022 | ĐS | Phép tắc cư dân: rác, tiếng ồn, quy tắc khu phố | S01 A1-11 |
| S-023 | CV | Đi công tác ngắn: tàu, taxi & báo lịch | S05 T7 |
| S-024 | PX | Mẫu hội thoại cơ bản: ね・よ・よね・か | B11 P1 |
| S-025 | ĐS | Sinh hoạt hằng ngày trong nhà | B01 C4 · S04 T5 · B08 P1-02 |

#### Tháng 3 — Di chuyển trong thành phố & công ty: hỏi đường, tàu, taxi, công tác ngắn

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-026 | ĐS | Đến nhà bạn / thầy cô | S01 T5 · B08 P4-19 |
| S-027 | CV | Báo đến muộn & trục trặc đi làm | S14 10 |
| S-028 | ĐS | Hỏi đường & chỉ đường | S01 A1-9 · B08 P4-03 · N 32 · B18 P2-11 |
| S-029 | ĐS | Mất bao lâu, đi bằng gì | N 33 · S04 T7 |
| S-030 | CV | Hỏi ý nghĩa biển báo, ký hiệu nơi làm việc | S14 1 |
| S-031 | ĐS | Xác nhận tàu/xe đúng đích đến | N 6 · S01 A1-8 |
| S-032 | ĐS | Đi tàu điện: mua vé, nhờ giúp, xuống ga | B08 P4-01 · B01 C7 · B27 8 · S19 U1-1 · B26 8 |
| S-033 | CV | Ăn trưa & gọi món cùng đồng nghiệp | S10 5 |
| S-034 | ĐS | Xe buýt & taxi | N 15 · B08 P4-02 |
| S-035 | ĐS | Shinkansen, quầy thông tin du lịch, đường dài | S19 U1-2,U1-3 |
| S-036 | CV | Mua văn phòng phẩm & việc vặt cho công ty [AI] | AI |
| S-037 | ĐS | Lái xe & bãi đỗ xe | B01 C7 |
| S-038 | ĐS | Khám phá khu phố: đền chùa, địa danh | S05 T3 · S20 1 |

#### Tháng 4 — Ăn uống, mua sắm & việc baito đầu tiên

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-039 | PX | Câu ngắn phản xạ (2): hỏi & xác nhận | B07 P1-1 |
| S-040 | CV | Tìm việc làm thêm & phỏng vấn baito | B26 6 · B08 P4-33 · S01 A2-16,A2-17 |
| S-041 | ĐS | Siêu thị & konbini | S01 A1-2 · B08 P4-09 · B05 ch4 · S04 T8 · B26 5 |
| S-042 | ĐS | Hỏi giá & hỏi khu bán hàng | N 10 · S01 A1-3 |
| S-043 | CV | Điện thoại công sở: nghe & chuyển máy cơ bản | B17 L2 · B04 U1,U2,U3 · B10 3 · B08 P4-24,P4-25 |
| S-044 | ĐS | Có món mình muốn không? Chọn món | N 11,19 · S01 A1-4 |
| S-045 | ĐS | Chọn cái nào? So sánh hai thứ | N 27,38 |
| S-046 | CV | Nhờ vả & xin phép việc nhỏ | B10 5,6 · S17 3,4 · B02 S18,S19,S20 · B08 P2-04 |
| S-047 | ĐS | Nói mong muốn với nhân viên cửa hàng | S01 A1-5,T2 |
| S-048 | ĐS | Quần áo: thử, cỡ, màu | B08 P4-07,P4-08 · S19 U2-1 |
| S-049 | CV | Xin lỗi khi mắc lỗi | B17 L3 · B27 5 · W 7 · S08 12 |
| S-050 | ĐS | Điện máy & đồ gia dụng | B08 P4-10 · S19 U2-2 |
| S-051 | ĐS | Gọi món & đặt chỗ ở nhà hàng | S01 A1-6,T3 · B01 C5 · B08 P4-05 · B26 3 · S08 4 · S19 U3-1,U3-2,U3-4 |

#### Tháng 5 — Đứng được trong công ty: nhận việc, nội quy, máy móc, an toàn

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-052 | CV | Nhận chỉ thị, nhận việc | S14 5 · B02 S21,S22,S23 |
| S-053 | ĐS | Ăn uống: không ăn được gì, nhờ bỏ gì | N 20,24 |
| S-054 | ĐS | Quán cà phê, fast-food & thanh toán | B08 P4-06 · S19 U3-3 |
| S-055 | PX | Câu ngắn phản xạ (3): giải thích & đánh giá | B07 P1-3,P1-4 |
| S-056 | CV | Nội quy & phép tắc nơi làm việc | S14 2 · B03 U1 |
| S-057 | ĐS | Mua đồ ăn & mua quà | S19 U2-3,U2-4 |
| S-058 | ĐS | Chuyển phát nhanh & gửi hàng | S01 A1-7 |
| S-059 | CV | Dùng máy móc, hỏi cách sử dụng | S14 8 · S01 A1-12 |
| S-060 | ĐS | Mượn đồ, đổi lịch, nhường chỗ | B26 1,2,9 |
| S-061 | ĐS | Mắc lỗi trong đời sống & xin lỗi | B27 5 · N 39 |
| S-062 | CV | An toàn lao động & tai nạn nhỏ | S01 A2-14,A2-15 |
| S-063 | ĐS | Duy trì hội thoại & aizuchi cơ bản | S08 8,14 |
| S-064 | ĐS | Nói chuyện với bạn thân | S08 15 · B14 U1 |

#### Tháng 6 — Bạn bè & cuối tuần: rủ rê, xin phép, kể chuyện đã làm

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-065 | CV | Báo không khỏe & xin nghỉ | S14 9 · S01 A2-19 |
| S-066 | ĐS | Phàn nàn đơn giản | S08 13 |
| S-067 | ĐS | Rủ đi chơi, nhận lời, từ chối | N 22,31 · B08 P2-05,P2-06 · S08 6 |
| S-068 | CV | Đề xuất ý kiến ngắn & xin phép ở công ty | W 8,6 |
| S-069 | ĐS | Xin phép làm gì | N 28 · S08 16 · B08 P2-07 |
| S-070 | ĐS | Làm được không? Hỏi khả năng | N 41 |
| S-071 | PX | Mẫu đi với danh từ & tính từ | B11 P2-NA |
| S-072 | CV | Rủ đồng nghiệp ăn trưa | S10 5 · S07 7 |
| S-073 | ĐS | Sở thích, thể thao, phim, sách | B08 P5-01,P5-02,P5-05,P5-09 · S04 T6 · B27 9 |
| S-074 | ĐS | Cuối tuần & ngày nghỉ | B08 P5-06 · S04 T9 · S05 T4 |
| S-075 | CV | Báo vấn đề phát sinh & xin ý kiến | S14 11,12 |
| S-076 | ĐS | Kể điều đã làm, đã từng | N 29,34 |
| S-077 | ĐS | Liệt kê hành động & kể lần lượt | N 30,35 |

#### Tháng 7 — Sức khỏe & kết bạn mới: bệnh viện, hiệu thuốc, tham quan, nghe hướng dẫn

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-078 | CV | Nghe thông báo & hướng dẫn sơ tán nơi làm việc | S14 3 |
| S-079 | ĐS | Kể cảm tưởng về điều đã trải qua | N 18,12,16 |
| S-080 | CV | Hỏi đồng nghiệp & trao đổi giấy tờ | S01 A2-18 |
| S-081 | ĐS | Diễn tả nhiều ấn tượng cùng lúc | N 26,46,43 |
| S-082 | ĐS | Gặp gỡ, kết bạn mới | B27 1 · S08 7 · B08 P2-01 |
| S-083 | CV | Nhận chỉ dẫn, nghe giải thích khi tham quan nhà máy | S14 4 |
| S-084 | ĐS | Nói mình không khỏe | N 25 · B08 P1-03 |
| S-085 | ĐS | Bệnh viện: khám & mô tả triệu chứng | B08 P4-12 · S19 U5-1 · S01 A2-8 · B27 7 |
| S-086 | PX | Mẫu đầu câu & cuối câu | B11 P2-HT |
| S-087 | CV | Nhận hướng dẫn và lời khuyên | S14 14 |
| S-088 | ĐS | Hiệu thuốc | B08 P4-11 · S19 U5-2 |
| S-089 | ĐS | Giữ gìn sức khỏe | S05 T8 · B08 P5-04 |
| S-090 | CV | Trả lời điện thoại thay đồng nghiệp | W 13 |

#### Tháng 8 — Khẩn cấp, thủ tục & điện thoại công sở: cấp cứu, thiên tai, ngân hàng, nhắn lời

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-091 | ĐS | Gọi cấp cứu, nhờ giúp khi khẩn cấp | S01 A2-9 |
| S-092 | ĐS | Mất đồ & đồn cảnh sát | B08 P4-29 · S08 9 |
| S-093 | CV | Nhờ chuyển máy & nhờ gọi lại | B02 S16,S17,S11 |
| S-094 | ĐS | Động đất, hỏa hoạn, thông báo thiên tai | S14 3 · B05 ch8 |
| S-095 | ĐS | Đồ vật trục trặc | N 37 · B27 4 |
| S-096 | CV | Điện thoại công sở: gọi đi & để lại lời nhắn | B04 U21,U24,U28 · S17 6 |
| S-097 | ĐS | Giải thích lý do | N 40 |
| S-098 | ĐS | Ngân hàng | S01 A1-10 · B08 P4-13 |
| S-099 | CV | Chuyển lời nhắn | W 5 · S14 13 · B04 U13,U14 · B02 S42 |
| S-100 | ĐS | Bưu điện & gửi bưu thiếp | S01 A2-12 · B08 P4-14 |
| S-101 | ĐS | Cơ quan hành chính: thủ tục | S01 A2-10 · S19 U4-1 |
| S-102 | PX | Câu ngắn phản xạ (4): nhờ, ý chí, lời khuyên | B07 P1-5,P1-6,P1-7 |
| S-103 | CV | Hẹn gặp & đổi lịch | B10 7 · S17 7 · B04 U22 · B02 S10 |

#### Tháng 9 — Dịch vụ, khách & hẹn gặp: thư viện, tiệm tóc, danh thiếp, điện thoại

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-104 | ĐS | Thư viện | S01 A2-11 · S19 U4-2 |
| S-105 | ĐS | Trung tâm cộng đồng & thể thao | S19 U4-3,U4-4 |
| S-106 | CV | Đến thăm công ty khác | B10 8 · B02 S12,S43 |
| S-107 | ĐS | Internet & điện thoại: hợp đồng, nạp tiền | S01 A2-13 · B01 C6 |
| S-108 | ĐS | Tiệm tóc | B08 P4-32 · S19 U5-3 |
| S-109 | CV | Danh thiếp & chào hỏi khách | B03 U11 · B02 S1,S2 |
| S-110 | ĐS | Hội cư dân & sự kiện địa phương | S01 A2-6,A2-7 · S19 U6-1 |
| S-111 | ĐS | Đặt chỗ & hẹn lịch | B08 P2-14 · S08 18 |
| S-112 | CV | Hỏi thông tin & xác nhận | B02 S9,S35,S36,S37 |
| S-113 | ĐS | Gọi điện cho bạn / thầy | B08 P4-23 · B01 C6 · B27 6 |
| S-114 | ĐS | Đặt hàng & hỏi thông tin qua điện thoại | B08 P4-26,P4-27 |
| S-115 | CV | Đặt câu hỏi bằng kính ngữ cơ bản | W 9 |
| S-116 | ĐS | Cảm xúc cơ bản | B01 C1 |

#### Tháng 10 — Cảm xúc, mong muốn & kế hoạch: nói ý kiến, hỏi ý cấp trên, họp báo cáo

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-117 | PX | Mẫu nối hội thoại & こそあど | B11 P2-CK |
| S-118 | ĐS | Mong muốn & nguyện vọng | N 13,14 · B08 P2-15 |
| S-119 | CV | Hỏi ý kiến cấp trên | B02 S31 |
| S-120 | ĐS | Dự định, kế hoạch, tương lai | N 4,42,48 · B27 10 |
| S-121 | ĐS | Đang làm gì, vừa làm gì | N 17 |
| S-122 | CV | Chào & giới thiệu với đối tác (mức cơ bản) | S07 6 · S17 5 |
| S-123 | ĐS | Lời khuyên & ý kiến | B01 C3 · S08 20 · S12 6 |
| S-124 | ĐS | Khen & khiêm tốn | B26 7 · S08 11 · S12 8 · B08 P2-12 |
| S-125 | CV | Nói ý kiến, tán thành & phản đối đơn giản ở công ty | B02 S4,S5,S6 |
| S-126 | ĐS | Động viên & hỏi thăm | B08 P2-10,P2-11,P2-13 |
| S-127 | ĐS | Đề nghị giúp đỡ | B08 P2-09 · S12 5 · W 10 |
| S-128 | CV | Họp báo cáo kinh doanh: nghe & ghi chú | S10 4 |
| S-129 | ĐS | Tin đồn & chuyện nghe được | N 44 · B27 3 |

#### Tháng 11 — Học hành, du lịch & báo–liên–tương: kể cách học, khách sạn, đón người thân

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-130 | ĐS | Đề nghị một cách lịch sự | N 45 · B08 P2-08 |
| S-131 | CV | Tiệc cuối năm & năm mới ở công ty | B17 L10,L11 |
| S-132 | ĐS | Hỏi cách làm | N 47 |
| S-133 | PX | Câu ngắn phản xạ (5): câu hằng ngày | B07 P2 |
| S-134 | ĐS | Kể cách mình học tiếng Nhật | N 5 · S01 B1-23 |
| S-135 | CV | Báo – liên – tương cơ bản | B03 U18 · B17 L4 · S17 8 |
| S-136 | ĐS | Ăn ngoài trời & picnic | S05 T6 |
| S-137 | ĐS | Đón người thân ở sân bay | B17 L7 |
| S-138 | CV | Nhận chỉ thị & hỏi lại | B03 U17 · W 2,12 |
| S-139 | ĐS | Đại học: thầy cô, thủ tục | B08 P4-15,P4-16 · S08 19 · B18 P2-1 |
| S-140 | ĐS | Mua vé & đăng ký | S08 5 |
| S-141 | CV | Báo cáo kết quả ngắn | S14 15 · W 29 · S07 9 |
| S-142 | ĐS | Du lịch: lập kế hoạch, công ty du lịch | B08 P4-30,P4-31,P5-10 · B26 4 |

#### Tháng 12 — Tổng kết năm đầu: họp đầu tiên, hẹn hò, phục vụ khách, một ngày ở Nhật

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| S-143 | ĐS | Khách sạn | B08 P4-04 · B27 2 |
| S-144 | CV | Họp đầu tiên: nghe & nói một câu | W 3 · B02 S33,S5 |
| S-145 | ĐS | Thời tiết & bốn mùa | B08 P5-07 · S05 T2 |
| S-146 | ĐS | Lễ hội & sự kiện theo mùa | S05 T9 · B17 L8 |
| S-147 | CV | Phục vụ khách cơ bản | B05 ch1,ch2,ch3 |
| S-148 | ĐS | Nhật Bản & đất nước mình | B08 P5-08 · S05 T5 |
| S-149 | PX | Mẫu nhiều dạng: biến hình trong hội thoại | B11 P2-FM |
| S-150 | ĐS | Đi thăm người ốm | S08 17 |
| S-151 | CV | Giao tiếp nội bộ & trò chuyện đồng nghiệp | B03 U19 · B02 S8,S7 |
| S-152 | ĐS | Hẹn hò đầu tiên | B08 P4-28 |
| S-153 | ĐS | Ôn tổng hợp: một ngày ở Nhật | B08 P1-02 · N 36 |
| S-154 | CV | Xin phép & xin nghỉ phép | B17 L6 · S07 11 · B02 S32 |
| S-155 | ĐS | Công việc & sở thích cân bằng | B17 L13 · S04 T9 |

### Level Trung


#### Tháng 13–14 — Từ baito thành nhân viên chính thức: tìm nhà, chọn nghề, hồ sơ, phỏng vấn

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-001 | ĐS | Tìm nhà & thuê nhà nâng cao | S01 B1-8 · B13 U4a |
| T-002 | CV | Tự phân tích bản thân & chọn ngành nghề | S13 1,2 |
| T-003 | PX | Vui, xúc động, ngạc nhiên | B24 A,B |
| T-004 | CV | Gặp tiền bối, tham dự buổi giới thiệu công ty | S13 3,7 |
| T-005 | ĐS | Chuyển nhà: chuẩn bị & thủ tục | S01 B1-9 · S11 5 |
| T-006 | CV | Lý do ứng tuyển, hồ sơ & lý lịch | S13 4,5 · B16 U1 |
| T-007 | ĐS | Quản lý việc nhà & đồ đạc | B13 U1a |
| T-008 | CV | Thực tập | B16 U2 · S13 6 |
| T-009 | PX | Biết ơn, hy vọng, mong đợi | B24 C,D |
| T-010 | ĐS | Điện thoại đặt chỗ & hỏi thông tin đời sống | B05 ch7 · B21 L9,L15 · B22 L9,L15 · B23 L9,L15 |
| T-011 | CV | Phỏng vấn tuyển dụng | B16 U3 · S13 8 · B21 L20 · S10 9 · B13 U7a · B22 L20 · B23 L20 |

#### Tháng 15–16 — Nhận việc & những cuộc gọi khó đầu tiên

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-012 | ĐS | Nhận bưu phẩm, hàng, ký nhận | B13 U4a |
| T-013 | CV | Làm việc với công ty giới thiệu nhân sự | S10 7,8 |
| T-014 | ĐS | Báo vắng, nhắn tin nội dung qua điện thoại bạn bè | B25 1 |
| T-015 | PX | Mong ước, hứng thú, ý chí mạnh | B24 E,F,G |
| T-016 | CV | Nhận việc: những ngày đầu | B16 U4 · S10 1 |
| T-017 | CV | Gọi điện đàm phán xử lý vấn đề khó | W 16 |
| T-018 | ĐS | Phàn nàn từ hàng xóm & cách giải quyết | W 33 · B13 U3a |
| T-019 | CV | Gọi điện thực hiện yêu cầu khẩn cấp | W 42 |
| T-020 | ĐS | Quà tặng & lễ nghi tặng quà | B21 L10 · B13 U1a,U3a · S19 U2-4 · B22 L10 · B23 L10 |
| T-021 | PX | An tâm, thoải mái, nhẹ nhõm | B24 H |
| T-022 | CV | Điện thoại: câu đầu & xác nhận nội dung | B04 U1,U2,U3 · B16 U5 · B03 U15 |

#### Tháng 17–18 — Nomikai, quà tặng & điện thoại công sở: chuyển máy, gọi nhầm, lời nhắn

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-023 | ĐS | Tiệc, nomikai, karaoke | B17 L5 · B13 U5a · B21 L8 · S11 3 · B22 L8 · B23 L8 |
| T-024 | CV | Chuyển máy: người bận, rời chỗ, vắng mặt | B04 U4,U5,U6,U7 · B02 S16 |
| T-025 | ĐS | Đến thăm nhà người khác nâng cao | B21 L16 · B13 U3a · B22 L16 · B23 L16 |
| T-026 | CV | Gọi nhầm, không có người tên đó, chuyển số khác | B04 U8,U9,U10,U29 |
| T-027 | PX | Bất an, lo lắng, thế khó | B24 I,J |
| T-028 | ĐS | Quan niệm làm việc & văn hóa công ty Nhật | B03 U20 · S20 6 |
| T-029 | CV | Nhận & chuyển lời nhắn | B04 U13,U14,U24 · B21 L7,L11 · B02 S42 · B22 L7,L11 · B23 L7,L11 |
| T-030 | ĐS | Nhờ vả, nhận lời & từ chối khéo | B21 L3,L4 · B25 5 · B12 A6 · B22 L3,L4 · B23 L3,L4 |
| T-031 | CV | Gọi lại & nhờ gọi lại | B04 U11,U12,U25,U26 · B02 S17 |
| T-032 | CV | Nhắc lại số, chữ, hỏi cách viết tên | B04 U15,U16,U30,U31 |
| T-033 | PX | Khó chịu, giận dữ | B24 K,L |

#### Tháng 19–20 — Điện thoại khách hàng & xã giao: fax, email, khách giận, hộp thư thoại

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-034 | ĐS | Xin ý kiến, xin lời khuyên đời thường | B02 S29,S30,S31 · S12 1,6 |
| T-035 | CV | Fax, email & để khách chờ | B04 U17,U18,U23 · B02 S11 |
| T-036 | ĐS | Cảm ơn nâng cao & lời cảm tạ | S07 4 · B05 ch1 |
| T-037 | CV | Khách giận, xin lỗi qua điện thoại | B04 U19 · W 19 |
| T-038 | ĐS | Lên kế hoạch nghỉ cùng gia đình | S10 6 |
| T-039 | PX | Thất vọng, hối tiếc, tự nhìn lại | B24 M,N |
| T-040 | CV | Nghe không rõ, kết thúc cuộc gọi, hộp thư thoại | B04 U27,U28,U32,U33,U34,U35,U20,U21 |
| T-041 | ĐS | Bình luận phim, sách, tin tức với bạn | S06 C9 · B13 U2a |
| T-042 | CV | Trò chuyện xã giao với khách hàng | W 25 |
| T-043 | ĐS | Nêu ý kiến & bất đồng nhẹ nhàng | B01 C3 · B25 6 · S12 7 · B24 O |
| T-044 | CV | Phép tắc ngoại hình, vào/rời phòng, cách nói | B03 U2,U3,U4,U5,U6 |

#### Tháng 21–22 — Tiếp khách, tiệc rượu & chuyện đời: danh thiếp, chỗ ngồi, tin đồn, mang thai

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-045 | PX | Bất mãn, phản đối, đành chịu | B24 O,P |
| T-046 | ĐS | Rủ rê, đề xuất & thuyết phục nhẹ | B25 2,7 · S07 7 · S12 4 |
| T-047 | CV | Danh thiếp, tiếp khách, đi thăm đối tác | B03 U11,U12 · B21 L16 · B02 S12 · S10 3 · B22 L16 · B23 L16 |
| T-048 | CV | Tiếp đãi, ăn với khách & thứ tự chỗ ngồi | B03 U13,U14 · B13 U7a |
| T-049 | ĐS | Tin đồn, thông tin chắc & không chắc | B25 4 · B27 3 |
| T-050 | PX | Cho là chắc, sơ ý, hoài nghi, coi nhẹ | B24 Q,R,S |
| T-051 | CV | Từ chối ly rượu & lời mời xã giao | B02 S26,S27,S28 · B13 U7a |
| T-052 | ĐS | Mang thai & chuẩn bị sinh | S01 B1-10 |
| T-053 | CV | Nhận lời nhắc & góp ý từ tiền bối | B10 4 · B21 L19 · B02 S38,S39,S40,S41 · W 40 · B22 L19 · B23 L19 |
| T-054 | ĐS | Trao đổi tư vấn về sinh con | S01 B1-11 |
| T-055 | CV | Điện thoại di động & sắp xếp bàn làm việc | B03 U7,U8,U9,U10 |

#### Tháng 23–24 — Văn bản, báo–liên–tương & nuôi con: email, chuyển công tác, nhà trẻ

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-056 | PX | Phản ứng nhanh sắc thái (1): あ・か | B06 1 |
| T-057 | ĐS | Dịch vụ hỗ trợ nuôi con | S01 B1-12 |
| T-058 | CV | Đề nghị cấp trên một cách lịch sự | W 44 |
| T-059 | ĐS | Đưa con đi bệnh viện | S01 B1-13 |
| T-060 | CV | Email & văn bản công việc | B03 U16 |
| T-061 | CV | Chuyển công tác & lời chia tay | B17 L14 · B02 S44,S45 |
| T-062 | PX | Phản ứng nhanh sắc thái (2): さ・た | B06 2 |
| T-063 | ĐS | Nhà trẻ & cơ sở chăm sóc trẻ | S01 B1-14 |
| T-064 | CV | Báo – liên – tương nâng cao | B03 U18 · B13 U6a · B02 S6 |
| T-065 | ĐS | Tư vấn nuôi dạy con | S01 B1-15 |
| T-066 | CV | Nhận chỉ thị & làm rõ | B21 L2 · W 28,35,45 · S07 8 · B22 L2 · B23 L2 |
| T-067 | ĐS | Chuẩn bị nhập học | S01 B1-16 |

#### Tháng 25–26 — Trường học của con, lỗi & nhờ giúp: xin lỗi, xử lý sai sót, quá tải

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-068 | PX | Phản ứng nhanh sắc thái (3): N・H | B06 3 |
| T-069 | CV | Xin phép, xin nghỉ | B02 S34 · B21 L14 · B22 L14 · B23 L14 |
| T-070 | ĐS | Đời sống học đường | S01 B1-17 |
| T-071 | CV | Đổi lịch hẹn với đối tác | B21 L18 · S07 2 · W 24 · B22 L18 · B23 L18 |
| T-072 | ĐS | Rắc rối ở trường | S01 B1-18 |
| T-073 | CV | Xin lỗi & xử lý sai sót | B21 L12 · W 7 · S07 3 · S12 3 · B02 S30 · B22 L12 · B23 L12 |
| T-074 | PX | Phản ứng nhanh sắc thái (4): M・Y・W | B06 4 |
| T-075 | ĐS | Tư vấn hướng học tập & nghề nghiệp | S01 B1-19 |
| T-076 | CV | Quá tải: nhờ giúp, chia việc, từ chối hỗ trợ | W 14,27,30,38 · S07 1 · S12 2 · B02 S24,S25 |
| T-077 | CV | Chủ động giúp đồng nghiệp | W 17 · S07 10 · S17 8 |
| T-078 | ĐS | Hiệu thuốc nâng cao & mua thuốc | S01 B1-4 · B13 U4a |

#### Tháng 27–28 — Kính ngữ vào guồng & họp: thuyết trình ngắn, y tế, thiên tai

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-079 | CV | Báo khách đang vội có thể bị chậm | W 20 |
| T-080 | PX | Kính ngữ cơ bản: lịch sự, tôn kính, khiêm nhường | B18 P1-1,P1-2,P1-3 · S19 U1-1 |
| T-081 | ĐS | Phòng bệnh & khám sức khỏe | S01 B1-6 · B13 U5a |
| T-082 | CV | Tìm điều khách lo lắng & đề xuất sửa chữa thêm | W 43,46 |
| T-083 | ĐS | Nghĩ về phòng chống thiên tai | S01 B1-5 · B17 L12 |
| T-084 | CV | Họp: nghe, hỏi, phát biểu ngắn | W 3,22 · S07 12 · B13 U5a |
| T-085 | ĐS | Tự đi đến nơi mình muốn & di chuyển an toàn | S01 B1-2,B1-3 · B21 L5 · B22 L5 · B23 L5 |
| T-086 | PX | Kính ngữ theo chức năng: nhờ, xin phép, từ chối, xin lỗi | B18 P2-F · B21 L17 · B22 L17 · B23 L17 |
| T-087 | CV | Thuyết trình ngắn có tài liệu | W 4 · S11 2 |
| T-088 | ĐS | Y tế nâng cao: khám đau đầu, xin thuốc dài hạn | B13 U4a · S06 C7 |
| T-089 | CV | Giải thích logic & gỡ hiểu lầm | W 15,23 |

#### Tháng 29–30 — Thương lượng mức vừa & cân bằng việc–đời: đồng cảm, xin nghỉ chăm con

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-090 | ĐS | Thể thao, gym & giải tỏa căng thẳng | S06 C5 · B17 L13 |
| T-091 | PX | Kính ngữ ở trường, thư viện, baito | B18 P2-1,P2-2,P2-3 |
| T-092 | CV | Nói "chưa quyết được ngay" & hỏi kỹ thông tin | W 37,36 |
| T-093 | CV | Giải thích quy định & định hướng công ty | W 18,21 |
| T-094 | ĐS | An ủi, đồng cảm, chia buồn | B13 U3a · B01 C3 |
| T-095 | CV | Thương lượng mức vừa | B16 U6,U7 |
| T-096 | ĐS | Tạo cớ thân thiết: điểm giống & khác | S21 1 |
| T-097 | PX | Kính ngữ ở văn phòng & với khách | B18 P2-4,P2-5,P2-6,P2-7 |
| T-098 | CV | Xin nghỉ chăm con & giờ làm linh hoạt [AI] | S06 C6 |
| T-099 | ĐS | Chia sẻ điều chưa vừa ý & lo lắng nhỏ | S21 2 |
| T-100 | CV | Cân bằng công việc & cuộc sống | S06 C6,C5 |

#### Tháng 31–32 — Kết thân & hiện trường: động viên, khen, hẹn hò sau thời gian dài, share house

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-101 | ĐS | Tìm chủ đề ngay tại chỗ | S21 3 |
| T-102 | CV | Báo cáo ốm & vắng mặt của đồng nghiệp | W 29 · B25 1 |
| T-103 | PX | Khẩu ngữ: biến âm てる・ちゃ・ん | B09 P1 · B08 P1-NAT |
| T-104 | ĐS | Hỏi tiếp chuyện lần trước | S21 4 |
| T-105 | CV | Hiện trường: an toàn, xác nhận việc, sự cố | S14 11,12 · B18 P2-9 |
| T-106 | CV | Động viên đàn em & đồng nghiệp | W 26,41 |
| T-107 | ĐS | Tiệc sushi & tìm hiểu người mới | S06 C2 |
| T-108 | CV | Khen, đánh giá, nhận xét | S12 8 · B25 8 |
| T-109 | PX | Aizuchi & dẫn dắt hội thoại | B09 P3 |
| T-110 | ĐS | Đổi không khí ngày nghỉ: tiệm quen & dạo phố | S06 C3 |
| T-111 | CV | Share house & quy tắc sống chung | S06 C1 |

#### Tháng 33–34 — Nghề phục vụ & dịch vụ: nhà hàng, cửa hàng, konbini, mua sắm nâng cao

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-112 | ĐS | Gặp bạn mới & đi phượt | S06 C8 |
| T-113 | CV | Đi thăm khách cùng đồng nghiệp & chuyện đồn | S06 C4 |
| T-114 | ĐS | Hẹn hò sau thời gian dài | S06 C9 |
| T-115 | PX | Nói mơ hồ, rút gọn, lặp & đảo trật tự | B09 P2 |
| T-116 | CV | Kính ngữ khi phục vụ khách | B05 ch1 · B18 P2-6 |
| T-117 | ĐS | Nơi ở mới & hướng đi mới | S06 C10 |
| T-118 | CV | Nhà hàng: phục vụ từ phía nhân viên | B05 ch2 |
| T-119 | ĐS | Nhà hàng nâng cao: kiêng ăn, món sai, phàn nàn | B25 6 · B01 C5 · B13 U4a |
| T-120 | CV | Cửa hàng bán lẻ & quần áo: góc nhân viên | B05 ch3 |
| T-121 | PX | Mẫu hội thoại ね・よ・よね & nối câu | B11 · B12 P1 |
| T-122 | CV | Konbini & quầy thu ngân | B05 ch4 |

#### Tháng 35–36 — Khách sạn, du lịch & tổng kết Trung: điện thoại tiếp khách, chào hỏi nâng cao

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| T-123 | ĐS | Mua sắm nâng cao: so sánh, đổi trả, đặt hàng | B13 U4a · S01 A2-2,A2-3,A2-4,A2-5 |
| T-124 | CV | Khách sạn: đặt phòng, nhận phòng, yêu cầu | B05 ch5 |
| T-125 | ĐS | Du lịch, onsen & sự cố chuyến đi | B17 L9 · B13 U3a |
| T-126 | CV | Karaoke, thuê video, lớp học & dịch vụ khác | B05 ch6 |
| T-127 | PX | Từ tượng thanh – tượng hình (1): động tác & biến đổi | B19 P1,P2 |
| T-128 | ĐS | Chào hỏi theo hoàn cảnh nâng cao | B21 L6 · S07 6 · S17 2 · B22 L6 · B23 L6 |
| T-129 | CV | Điện thoại tiếp khách | B05 ch7 |
| T-130 | ĐS | Phát biểu tại lễ nhập học & sự kiện | S19 U6-2,U6-1 |
| T-131 | CV | Cấp cứu, sự cố & đồ bỏ quên (góc nhân viên) | B05 ch8 |
| T-132 | ĐS | Nói chuyện với giáo viên & du học | S08 5,10 · B18 P2-2 |
| T-133 | PX | Từ tượng thanh – tượng hình (2): trạng thái & tâm lý | B19 P3,P4 |
| T-134 | CV | Hỏi thông tin, hỏi cách làm | B21 L13,L15 · B22 L13,L15 · B23 L13,L15 |

### Level Thượng


#### Tháng 37–39 — Bước vào sân chơi chuyên nghiệp: ẩn ý, hẹn, họp & phản biện

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-001 | ĐS | Tình cảm tan vỡ: giận, chia tay, người cũ | B13 U2b |
| H-002 | CV | Tự giới thiệu nội bộ & với bên ngoài | B15 L1,L2 · S16 1 |
| H-003 | ĐS | Tâm sự về sức khỏe, giấc ngủ & thiếu quyết đoán | B13 U2b |
| H-004 | CV | Điện thoại đối ngoại cấp cao | B15 L3 · B13 U7b |
| H-005 | PX | Nói ẩn ý, bóng gió, đọc không khí | B12 P2-A · B20 Z · B09 P2 |
| H-006 | ĐS | Khác biệt quan điểm & giữ quan hệ | B13 U3b |
| H-007 | CV | Hẹn, đổi lịch & hẹn khách mới | B15 L4,L11 · S09 1 |
| H-008 | ĐS | Từ chối lời mời mua hàng & hủy lời nhờ | B13 U3b |
| H-009 | CV | Họp: tham gia & phản biện | B15 L5 · S09 10 |

#### Tháng 40–42 — Đời sống chín chắn & hàng giao trễ: gia đình, bạn thân, giảm giá, ký duyệt

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-010 | ĐS | Gia đình: vợ chồng, cha mẹ, con cái | B13 U1b |
| H-011 | CV | Phỏng vấn & thu thập thông tin | S09 9 |
| H-012 | ĐS | Bạn thân: tâm sự, giận hờn, hàn gắn | B13 U2b |
| H-013 | CV | Giao hàng trễ, hàng lỗi & yêu cầu giảm giá | B13 U7b |
| H-014 | PX | Biểu đạt nghĩa vụ, đánh giá thấp, dè dặt | B12 P2-B |
| H-015 | ĐS | Người quen & hàng xóm: chuyện đời, xã hội | B13 U3b |
| H-016 | CV | Xin phép cấp trên trước khi ký & báo giá không hạ | B13 U7b |
| H-017 | ĐS | Dịch vụ & mua sắm cao cấp: so sánh, đóng tài khoản, đổi lịch | B13 U4b |
| H-018 | CV | Nhận khiếu nại | B15 L6 · S09 4 |

#### Tháng 43–45 — Khiếu nại: nhận, báo cáo, xử lý & xin lỗi chính thức

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-019 | ĐS | Phàn nàn dịch vụ & lấy lại quyền lợi | S16 7 · B25 6 |
| H-020 | CV | Báo cáo khiếu nại lên cấp trên | B15 L7 · S09 5 |
| H-021 | ĐS | Món ăn đến chậm & trục trặc đời sống | B13 U4b |
| H-022 | CV | Xử lý khiếu nại & xin lỗi chính thức | B15 L8 · B13 U8-1 |
| H-023 | ĐS | Quan hệ nhạy cảm nơi làm: sếp, đám cưới, đồng nghiệp cũ | B13 U5b |
| H-024 | PX | Từ chối gián tiếp & phủ định nhẹ | B12 P2-A6 |
| H-025 | CV | Khiếu nại bằng lời: nói mạnh & nói nhẹ | S16 7 |
| H-026 | ĐS | Quan hệ nơi làm: đồng nghiệp, tiền lương, sa thải, hiểu lầm | B13 U5b |
| H-027 | CV | Xử lý sự cố & báo cáo | S09 6,7 · S11 4 |

#### Tháng 46–48 — Quan hệ nhạy cảm, tình cảm & chào bán: nơi làm, cưới hỏi, thuyết phục

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-028 | ĐS | Chuyện tình cảm & hẹn hò chín chắn | B13 U8-2 |
| H-029 | CV | Trưởng nhóm mới, tranh cãi nhân sự & bị sa thải | B13 U5b |
| H-030 | ĐS | Thể thao, bóng chày & giải trí | B13 U8-3 · S22 4 |
| H-031 | CV | Đề xuất trong họp | B15 L9 · S16 2 |
| H-032 | ĐS | Phát biểu tiệc cưới & lễ nghi | B13 U8-7 · B02 S44,S45 |
| H-033 | PX | Giải thích bằng từ ngữ đúng sắc thái | B12 P3 |
| H-034 | CV | Khai thác khách hàng mới | B15 L10 |
| H-035 | ĐS | Cưới hỏi, tang lễ & chia buồn | B13 U8-7,U3b |
| H-036 | CV | Chào bán & thuyết phục | B15 L12 · B13 U8-6 · S16 6 |
| H-037 | ĐS | Bàn chuyện chuyển nhà & chọn nơi ở | S11 5 · B13 U1b |

#### Tháng 49–51 — Kể chuyện & đàm phán: hồi ức, chốt đơn, hợp đồng, giá cả

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-038 | ĐS | Bàn việc với vợ/chồng | S11 8 |
| H-039 | CV | Gọi nhắc phản hồi | B15 L13 |
| H-040 | ĐS | Chuyện kể dài & hồi ức | S21 5 |
| H-041 | CV | Đàm phán | B15 L14 · S16 5 · B13 U7b |
| H-042 | PX | Cảm xúc tinh tế: thất vọng, hối hận, coi thường | B24 M,N,S |
| H-043 | ĐS | Kể chuyện có điểm chốt | S21 5 |
| H-044 | CV | Chốt đơn & giữ quan hệ | B15 L15 |
| H-045 | ĐS | Trích lời người khác & kể sinh động | S21 7 |
| H-046 | CV | Hợp đồng, giá cả, điều kiện | B13 U7b · S16 3 |

#### Tháng 52–54 — Bàn giao & đàm phán trực tiếp: hải quan, cấp trên–cấp dưới, học thuật

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-047 | ĐS | Nhớ lại chuyện chung | S21 6 |
| H-048 | CV | Hải quan, công tác gấp & chuyển chi nhánh | B13 U6b |
| H-049 | ĐS | Học thuật & nghiên cứu | B18 P2-2 · S08 19 |
| H-050 | CV | Bàn giao công việc | S09 2 · S10 2 |
| H-051 | ĐS | Địa lý & danh thắng Nhật | S22 1 · S20 1 |
| H-052 | PX | Thuận lợi, hiệu quả, quan tâm mạnh | B20 A,B,C |
| H-053 | CV | Gặp mặt trực tiếp để đàm phán | S09 3 |
| H-054 | ĐS | Phong cách nói: mức lịch sự, lời nói nam–nữ | S22 2 · S20 2 |
| H-055 | CV | Cấp trên & cấp dưới: quản lý, ngân sách, dự án | B13 U6b,U8-4 |

#### Tháng 55–57 — Từ chối khéo & dẫn dắt họp: nhân sự, kết luận; Nhật Bản qua công nghệ, võ đạo, tôn giáo

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-056 | ĐS | Công nghệ & robot | S22 3 · S20 3 |
| H-057 | CV | Từ chối khéo & bác bỏ lịch sự | S09 8 · B25 5 |
| H-058 | ĐS | Võ đạo, thể thao & tinh thần | S22 4 · S20 4 |
| H-059 | CV | Điều chỉnh nhân sự & nhắc nhở cấp dưới | W 39,17,21 |
| H-060 | ĐS | Ẩm thực Nhật & vòng ra thế giới | S22 5 · S20 5 |
| H-061 | PX | Hiểu ra, an tâm, chu đáo, khao khát | B20 D,E,F,G |
| H-062 | CV | Giải thích, ý kiến, tán thành, phản đối trong họp cao cấp | S16 1,2,3,4 |
| H-063 | ĐS | Tôn giáo & tập quán | S22 6 · S20 6 |
| H-064 | CV | Kết luận & dẫn dắt cuộc họp tới quyết định | S16 5 |

#### Tháng 58–60 — Thuyết phục bằng chiến lược & văn hóa đại chúng: manga, giáo dục, lịch sử

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-065 | ĐS | Văn hóa đại chúng: manga, anime | S22 7 · S20 7 |
| H-066 | CV | Thuyết phục bằng chiến lược | S16 6 |
| H-067 | ĐS | Nghệ thuật biểu diễn truyền thống | S22 8 · S20 8 |
| H-068 | CV | Đề xuất với khách hàng | S11 2 |
| H-069 | ĐS | Giáo dục Nhật | S22 9 |
| H-070 | PX | Lách, tác động, đánh giá người | B20 H,I,J |
| H-071 | CV | Chào cảm ơn người đã giúp đỡ | S11 1 |
| H-072 | ĐS | Cửa hàng tiện dụng & máy bán hàng tự động | S22 10 |
| H-073 | CV | Tiệc mừng kết thúc dự án | S11 3 |
| H-074 | ĐS | Lịch sử Nhật | S22 11 |

#### Tháng 61–63 — Họp bữa trưa, đối tác chiến lược & xã hội Nhật: thủ công, haiku, chính trị

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-075 | ĐS | Thủ công truyền thống | S22 12 |
| H-076 | CV | Họp trong bữa trưa | S11 6 |
| H-077 | ĐS | Thiên nhiên & haiku | S22 13 |
| H-078 | CV | Được ngỏ lời bàn chuyện kinh doanh | S11 7 |
| H-079 | ĐS | Chính trị Nhật & bầu cử | S22 14 · B13 U1b |
| H-080 | PX | Bận rộn, căng thẳng, chênh lệch, động viên | B20 K,L,M,N |
| H-081 | CV | Thảo luận với đối tác chiến lược | S11 9 |
| H-082 | ĐS | Xã hội: bắt nạt, tội phạm, tình nguyện | B13 U3b |
| H-083 | CV | Thuyết trình: mở đầu, nội dung, kết | S16 8 · S09 11 · B13 U8-8 |

#### Tháng 64–66 — Pháp lý, định cư & sự nghiệp: bảo hiểm, thuế, phản biện giữ thể diện

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-084 | ĐS | Vấn đề xã hội toàn cầu & tương lai | S22 15 |
| H-085 | CV | Sự nghiệp: động cơ, phát triển, đổi việc, phỏng vấn cấp cao | B13 U7b,U8-5 · S13 4 |
| H-086 | ĐS | Pháp lý – tài chính – bảo hiểm – thuế [AI] | AI |
| H-087 | CV | Phản biện, tranh luận & giữ thể diện | S09 10 · B13 U3b |
| H-088 | ĐS | Định cư lâu dài: tự trị hội, PTA, hợp đồng nhà [AI] | S01 B1-7 · AI |
| H-089 | PX | Thái độ cứng–mềm, bị chỉ trích, kiêu căng | B20 O,P,Q |
| H-090 | CV | Chuyển lời xã giao, thăm hỏi & lời chúc đối tác | B13 U7b |
| H-091 | ĐS | Xin phép tinh tế (使わせてもらってもいいかなって) | B25 3 |
| H-092 | CV | Kính ngữ đối ngoại thượng cấp | B18 P1-1,P2-4 · S19 U1-3 |

#### Tháng 67–69 — Như người bản địa: nghe ngầm ý, nhờ cho bằng được, thương mại quốc tế

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-093 | ĐS | Thông tin chắc & không chắc ở mức cao | B25 4 |
| H-094 | CV | Văn hóa kinh doanh Nhật & ngầm ý | B03 U20 · S07 12 |
| H-095 | ĐS | Nhờ cho bằng được (そこをなんとか) | B25 5 |
| H-096 | CV | Điện thoại thương mại: mua sắm qua điện thoại | B13 U8-6 |
| H-097 | ĐS | Đề xuất & nêu cảm tưởng tự nhiên | B25 7,8 |
| H-098 | PX | Chán, xao nhãng, gặp khó, xấu hổ | B20 R,S,T,U |
| H-099 | CV | Kinh tế, công nghệ, môi trường & doanh nghiệp | B13 U3b,U4b |
| H-100 | ĐS | Nghe, nhắn, rủ, xin phép ở mức tự nhiên | B25 1,2,3 |
| H-101 | CV | Thương mại quốc tế & hải quan | B13 U6b |

#### Tháng 70–72 — Tổng kết: omotenashi, lãnh đạo họp lớn, một dự án từ đầu đến cuối

| ID | Loại | Chặng | Nguồn |
|---|---|---|---|
| H-102 | ĐS | Thông tin chắc & không chắc, nhờ vả, phàn nàn, đề xuất, cảm tưởng | B25 4,5,6,7,8 |
| H-103 | CV | Nghề dịch vụ cao cấp & omotenashi | B05 ch1,ch8 |
| H-104 | ĐS | Sự kiện, lễ hội & tổ chức sự kiện | S01 B1-21,B1-22 |
| H-105 | CV | Lãnh đạo cuộc họp nhiều người | B25 8 · B13 U6b |
| H-106 | ĐS | Sống cùng thú cưng & thời gian riêng | S01 B1-20 |
| H-107 | CV | Phàn nàn đúng đòn (予約したはずなんですけど) | B25 6 |
| H-108 | PX | Chịu đựng, kinh ngạc, tai họa | B20 V,W,X,Y |
| H-109 | ĐS | Tình huống tổng hợp A: một ngày ở Nhật không cần kịch bản [AI] | AI |
| H-110 | CV | Tình huống tổng hợp B: một dự án từ đầu đến cuối [AI] | AI |
| H-111 | ĐS | Học tiếng Nhật bằng nhiều cách & tự học lâu dài | S01 B1-23 |

## 4. Báo cáo phủ nguồn

| Nguồn | Mục cần phủ | Đã phủ | Thiếu |
|---|---|---|---|
| S01 | 60 | 60 | — |
| N | 48 | 48 | — |
| W | 43 | 43 | — |
| S04 | 6 | 6 | — |
| S05 | 9 | 9 | — |
| S06 | 10 | 10 | — |
| S07 | 12 | 12 | — |
| S08 | 20 | 20 | — |
| S09 | 11 | 11 | — |
| S10 | 9 | 9 | — |
| S11 | 9 | 9 | — |
| S12 | 8 | 8 | — |
| S13 | 8 | 8 | — |
| S14 | 15 | 15 | — |
| S16 | 8 | 8 | — |
| S17 | 8 | 8 | — |
| S19 | 20 | 20 | — |
| S20 | 8 | 8 | — |
| S21 | 7 | 7 | — |
| S22 | 15 | 15 | — |
| B02 | 45 | 45 | — |
| B15 | 15 | 15 | — |
| B16 | 7 | 7 | — |
| B17 | 14 | 14 | — |
| B21 | 20 | 20 | — |
| B22 | 20 | 20 | — |
| B23 | 20 | 20 | — |
| B06 | 4 | 4 | — |
| B07 | 8 | 8 | — |
| B10 | 8 | 8 | — |
| B03 | 20 | 20 | — |
| B04 | 35 | 35 | — |
| B25 | 8 | 8 | — |
| B26 | 10 | 10 | — |
| B27 | 10 | 10 | — |
| B13 | 22 | 22 | — |
| B08 | 58 | 58 | — |
| B24 | 19 | 19 | — |
| B20 | 26 | 26 | — |
| B05 | 8 | 8 | — |
| B01 | 7 | 7 | — |

Ghi chú: danh sách 'mục cần phủ' lấy từ mục lục/đầu mục nên là đơn vị bài/tình huống, không phải câu thoại. Phủ nghĩa là đã gắn mục vào một chặng, chưa có nghĩa đã đọc sâu nội dung.

## 5. 27 sách dùng ở đâu

| Sách | Số chặng trích | Sơ | Trung | Thượng |
|---|---|---|---|---|
| B01 | 12 | 9 | 3 | 0 |
| B02 | 29 | 15 | 13 | 1 |
| B03 | 14 | 5 | 8 | 1 |
| B04 | 14 | 5 | 9 | 0 |
| B05 | 14 | 3 | 10 | 1 |
| B06 | 4 | 0 | 4 | 0 |
| B07 | 5 | 5 | 0 | 0 |
| B08 | 49 | 48 | 1 | 0 |
| B09 | 4 | 0 | 3 | 1 |
| B10 | 7 | 6 | 1 | 0 |
| B11 | 6 | 5 | 1 | 0 |
| B12 | 6 | 0 | 2 | 4 |
| B13 | 56 | 0 | 20 | 36 |
| B14 | 2 | 2 | 0 | 0 |
| B15 | 13 | 0 | 0 | 13 |
| B16 | 6 | 0 | 6 | 0 |
| B17 | 14 | 9 | 5 | 0 |
| B18 | 11 | 2 | 7 | 2 |
| B19 | 2 | 0 | 2 | 0 |
| B20 | 8 | 0 | 0 | 8 |
| B21 | 19 | 2 | 17 | 0 |
| B22 | 19 | 2 | 17 | 0 |
| B23 | 19 | 2 | 17 | 0 |
| B24 | 11 | 0 | 10 | 1 |
| B25 | 18 | 0 | 8 | 10 |
| B26 | 8 | 8 | 0 | 0 |
| B27 | 12 | 11 | 1 | 0 |

Sách chưa được trích trong chặng nào: không có.

## 6. Speak Japanese (B11/B12): mẫu theo chức năng

B11 (88 mẫu) và B12 (125 mẫu) không làm chặng riêng; chúng là 'mẫu của chặng' (bài loại 3), gán theo chức năng giao tiếp. Bảng dưới là gán sơ bộ theo từ khóa tên chặng, sẽ tinh chỉnh khi dựng từng chặng.

| Sách | Nhóm mẫu | Chức năng | Vùng | Chặng gợi ý |
|---|---|---|---|---|
| B11 | P1 Mẫu 1–8: ね・よ・よね・か・の・んだ・って | Hội thoại cơ bản | Sơ tháng 1–4 | S-001, S-003, S-007, S-009, S-024 |
| B11 | P2 Mẫu 9–24: gắn động từ | Nhờ, xin phép, rủ, dự định, khả năng | Sơ tháng 5–10 | S-046, S-067, S-069, S-070, S-087, S-102, S-120, S-123 |
| B11 | P2 Mẫu 25–40: gắn danh từ & tính từ | Chủ đề, so sánh, ưa thích | Sơ tháng 4–6 | S-013, S-045, S-071, S-073, S-155 |
| B11 | P2 Mẫu 41–47: đầu câu (あのう・ねえ・ほら・まあ…) | Mở lời, gây chú ý | Sơ tháng 1–7 | S-006, S-015, S-086 |
| B11 | P2 Mẫu 48–67: cuối câu (かな・かも・でしょ・し・のに…) | Suy đoán, giải thích, lý do | Sơ tháng 6–10 | S-047, S-079, S-097, S-118, S-129, S-149 |
| B11 | P2 Mẫu 68–74: nối hội thoại (うん・へー・なるほど…) | Aizuchi & duy trì hội thoại | Sơ tháng 6, 10 | S-063, S-064, S-117 |
| B11 | P2 Mẫu 75–82: こそあど | Chỉ vật, chỉ nơi, hỏi đường | Sơ tháng 2–3 | S-009, S-015, S-028, S-117 |
| B11 | P2 Mẫu 83–88: nhiều dạng (なんか・ほう・やっぱり) | Nói tự nhiên, chọn lựa | Sơ tháng 11–12 | S-045, S-149, S-153 |
| B12 | P1 Mẫu 1–23: nối câu, て形, rút gọn, biến âm, こそあど nâng cao | Khẩu ngữ tự nhiên | Trung giai đoạn 11 (PX) | T-103, T-109, T-115, T-121 |
| B12 | P2-A 24–29: đồng tình, tiếp nhận | Tán thành, nghe hiểu | Trung/Thượng | S-125, T-043, T-084, H-009, H-062, H-087 |
| B12 | P2-A 30–42: bắt đầu, nối, bổ sung chuyện | Dẫn chuyện, thêm ý | Trung/Thượng | T-042, T-089, H-040, H-043 |
| B12 | P2-A 43–58: nhận lời, ngập ngừng, phủ định nhẹ, kết chuyện | Từ chối khéo, giữ nhịp, kết thúc | Trung/Thượng | S-067, T-030, T-051, T-076, T-086, T-092, H-008, H-024 |
| B12 | P2-B 59–76: an tâm, khó xử, nhấn mạnh, bỏ cuộc, dè dặt | Cảm xúc nâng cao | Trung giai đoạn 3–6 · Thượng (PX) | T-021, T-027, T-033, T-039, T-045, H-005, H-042, H-052 |
| B12 | P2-B 77–82: bất mãn, yêu cầu, lý do | Phàn nàn đúng đòn | Thượng | S-066, T-018, T-119, H-018, H-019, H-025, H-102, H-107 |
| B12 | P2-B 83–85, P2-C 86–99: ngạc nhiên, khen, thúc giục, hỏi tiếp | Khen, động viên, hỏi sâu | Trung/Thượng | S-126, T-041, T-104, T-106, T-108, H-080 |
| B12 | P3 100–125: từ giải thích, 何…, cách nói gợi | Mô tả, giải thích, xin lỗi | Thượng | H-033, H-059, H-062, H-071 |

## 7. Mạch công việc (business)

- **Sơ:** B17 (Roleplay đầu), B10, B02 phần ngày đầu, S17, S07.
- **Trung:** B16, B21 (+B22 luyện, B23 từ), B02, B03, B04, B05, S09–S16 phần cơ bản, NHK-công sở.
- **Thượng:** B15 (đỉnh Roleplay), B13 phần cao cấp, S09/S16 phần chiến lược, B25 (cầu).

## 8. Việc còn lại / cần bạn quyết

1. Duyệt số lượng: giữ 400 hay gọn về 355 (bỏ 45 chặng mini hoặc gộp bớt chặng nhỏ).
2. Duyệt tên và thứ tự 36 giai đoạn.
3. Pilot 3 chặng (đề xuất: Sơ 'Gọi món & đặt chỗ ở nhà hàng', Trung 'Điện thoại công sở: chuyển máy', Thượng 'Xử lý khiếu nại & xin lỗi chính thức'). 
4. Model cho sub-agent dựng chặng.
5. Core + Mở rộng cho mỗi chặng.
6. Danh sách ngữ pháp Minna no Nihongo N5/N4 (bạn bảo sẽ cung cấp).
