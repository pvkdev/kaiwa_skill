# T-134 — nhật ký biên soạn

Đọc toàn brief 30 cảnh, từ thông báo, đổi tuyến, xử lý vé đến cuộc gọi người chờ và chỗ đặt. Tra BOOK_GUIDE, manifest đủ 27 sách và source_index bằng 駅・遅延・終電・振替・乗り換え. Đọc B27-C22 về hỏi nhân viên và xác nhận thông tin. Đọc chuyên đề Đổi kế hoạch nhóm khi có phát sinh và dò practice theo UID, không có ví dụ gắn trực tiếp. Ngày 2026-11-18 đọc Tokyo Metro về kênh vận hành, các tuyến và điều kiện đi đường vòng theo vé. Mọi gián đoạn, hẹn, thời điểm và thỏa thuận riêng trong thoại là giả định. Tuyến, ga có thật được đối chiếu sơ đồ tuyến khi nêu.

## E01 — Nhận thông tin gián đoạn

- S001 · `334fa5b5-aeb9-59e3-a433-1d5b1e6a0e23`. Khách u01/u03 xác định tuyến và hướng rồi tách tình trạng tuyến Hanzōmon; ga chỉ cách đi khi được hỏi.
- S002 · `24b8a0be-ef71-521d-906c-90b3f1c7c399`. Khách u01 nêu đích; u03 dùng ga cuối tạm để tính đi bộ; nhân viên phân biệt đi được một phần và chạy lại toàn đoạn.
- S003 · `42ff42ef-6afe-5471-a569-453d73440df5`. Khách u01 biến mốc ước tính thành giờ lên tàu; u03 điều chỉnh lời sẽ nhắn sau khi ga tách hai mốc.
- S004 · `fb3415a8-2927-597b-acbb-27fc5dd48a0a`. Khách u01/u03 chốt nơi chờ và kênh tự tra, ga vẫn để giờ mở và nhắc kiểm tàu cụ thể.
- S005 · `d5c97cb9-9377-53e9-82b5-6afb7ad7433c`. Khách u03 nhắc lại đúng chuyến bỏ và chuyến lên; người ga duy trì điều kiện xem bảng.

Điểm nối đã đọc theo từng nhánh.

- S004 → S005. Chờ gần cổng theo gợi ý vì chưa có dự báo. Thông báo sau đó mới đổi trạng thái; chỉ nay biết tàu nào đi hết đoạn cần.

## E02 — Tìm đường thay thế

- S006 · `5fff7d1f-7a9d-5be8-a894-f5cd84039aba`. Khách u01/u03 hỏi điểm chuyển và dùng chỉ dẫn để kiểm chiều tàu; ga tách hai ga và đoạn đi bộ.
- S007 · `1b240bb6-b5ed-5048-9cfb-ab9a205cb7c3`. Khách u03 chọn xem hàng taxi vì giờ quầy sắp đóng; ga chỉ lối Nam, bên phải dưới mái che, vị trí thuộc ga giả định.
- S008 · `486b8eb0-ca02-5288-9d62-9bce679de8eb`. Khách u01 ghép hạn chế đổi tàu với chấp nhận đi bộ; u03 kiểm thang máy, chưa quyết vé hoặc lên tàu.
- S009 · `33207d15-ea83-530e-8c4f-1462a504d10e`. Khách u01 từ chối đi vòng và u03 tự đặt mốc xem lại; ga không biến mười phút thành dự báo.
- S010 · `e37e37e2-25d8-5da5-86f9-27b042c2996a`. Khách u01 nhắc ga xuống, u03 nêu chưa vào và chưa mua nên chọn vé thường; không ngầm miễn phí.

Điểm nối đã đọc theo từng nhánh.

- S008 → S010. Giữ phương án không đổi tàu và đi bộ sau Suitengūmae. Chỉ đến cảnh này mới biết chưa vào cổng, chưa mua vé và chọn cách trả.

## E03 — Vé/chặng đang đi

- S011 · `257584b6-8f70-5343-81ff-4a08f92894f6`. Khách u01/u03 nêu thẻ, cổng, loại số dư và chưa lên tàu; nhân viên mới nhận kiểm, chưa chốt phí.
- S012 · `1985a9d9-9795-57f4-acfd-bd872c999786`. Khách u03 hỏi phạm vi đúng đường sau khi nêu vé; ga xác nhận điều kiện vé, vẫn để tuyến mở.
- S013 · `bc8e79a2-ed17-56e3-bd02-74a4e653419e`. Khách u02 sửa nơi vào và đoạn đã đi; u04 nêu tiếp tục để ga xét đúng tình huống, không tự kết luận hoàn tiền.
- S014 · `89ff2bf4-f9a5-5117-8d22-8531896f4440`. Khách u01 nêu điều chưa chắc, u03 chốt chỗ đợi. Quầy chưa xác nhận quyền đi thay thế và nhắc khoan quẹt.
- S015 · `7ce864fa-9753-55d0-8f46-4af4f7317865`. Khách u02/u04 đọc lại đúng vì vào ngoài chặng, quầy kiểm lượt ra trước và vé đường mới trả riêng; không suy ra mức tiền lượt cũ.

Điểm nối đã đọc theo từng nhánh.

- S014 → S015. Giữ PASMO có vé tháng, ga vào còn chờ kiểm và chưa quẹt ra. Quầy mới xác nhận dùng tiền nạp do ngoài chặng; khách nhận bước ra ga và đi lại.

## E04 — Báo người đang chờ

- S016 · `e089c065-db89-5323-93ef-51428aef6c5b`. Khách u01 giải thích với て lược phần kết quả, nói vị trí ngay; u03 chốt người chờ vào quán và cập nhật khi có đường.
- S017 · `2eae394e-978b-5d66-8fc2-3e60e46238ac`. Khách u01 đưa hai phương án theo cùng tuyến đang chạy, u03 chọn đổi ga gặp sau khi bạn đề nghị; tên cổng còn chờ.
- S018 · `a479b4b2-4512-584c-a908-e14747f8c1d7`. Khách u02 tính cả đi bộ rồi chủ động bỏ đón, u04 giữ cập nhật; bạn được rời ngay.
- S019 · `ac4299da-4741-545b-8ca2-24b87a19c1e5`. Khách u02/u04 sửa cửa ra với cổng soát vé, người đón chốt quầy; thời gian chưa hứa.
- S020 · `8a481be8-17c6-5149-ae2c-8440ed648f75`. Khách u01 cập nhật cùng địa điểm; u03 hủy phần đón vì không biết giờ, bạn nói rõ đã đổi hành động chờ.

Điểm nối đã đọc theo từng nhánh.

- S019 → S020. Đã chốt quầy bên ngoài cổng soát vé Đông, chưa có giờ. Tuyến vòng mới dừng thêm; khách bỏ hẹn đón thay vì để bạn tiếp tục chờ.

## E05 — Lỡ chuyến cuối

- S021 · `481716e3-67a3-529d-9f21-758cdcd45c4a`. Khách u01/u03 hỏi hết tuyến và loại phương tiện vì không có đón giữa chặng; kết quả đêm tập là hết tàu và buýt.
- S022 · `bd2b9753-151c-5a38-84bb-b526a0175c07`. Khách u01/u03 hỏi theo mưa và ga sắp đóng; ga tách chỗ chờ và chỗ xe có thể dừng.
- S023 · `ff65db2f-f99c-5671-ab7e-099c06fd7711`. Khách u03 đổi từ buýt sang hỏi nơi chờ đến sáng vì tiền; ga đưa hướng rồi trả quyết định phòng/giá về đúng nơi.
- S024 · `07149ad6-96e9-58ec-ab75-d22ef41adc68`. Khách u01 đưa trần và giờ nhận, u03/u05 chọn phòng và nêu tên; chỉ u06 xác nhận đặt xong.
- S025 · `df393625-00d3-55d1-a133-3a64acb7403a`. Khách u01/u03 truyền đạt giá/giờ đã chốt và mốc báo; người nhà hiểu không cần đón.

Điểm nối đã đọc theo từng nhánh.

- S024 → S025. Lễ tân đã giữ phòng đơn 8.800 yên gồm thuế, tới muộn nhất 1 giờ, ước đi bộ 15 phút. Đổi vai bên kia sang người nhà chưa biết phòng; Mori kể lại và bỏ đón.

## E06 — Sau khi tới hoặc đổi ngày

- S026 · `52f1ad89-bbd9-5125-99e2-b2c1cbd8c0d7`. Khách u02/u04 kể theo thứ tự, kết luận というわけで trả lời lời hỏi Hibiya; bạn biết chỉ một chặng tàu.
- S027 · `7cbcf39e-4ac8-53b6-ad0d-325788f0f4e2`. Khách u01 nói giờ đến và xin lỗi vì ảnh hưởng; u03 kiểm còn làm việc đã hẹn sau khi bạn giải thích đã vào.
- S028 · `cae8f9bb-b09f-57c3-bc34-21951eeea412`. Khách u01 báo đã quá giờ đặt, số người và lý do; u03 chốt gọi lại cùng số. Tối nay hủy, chưa có chỗ mới.
- S029 · `1603642f-199a-58d4-9e98-5e35f64a7d12`. Khách u01/u03 hỏi khoản theo chặng và cung cấp đường đã đi, quầy nhận kiểm trước khi nói tiền; kết mở là thuộc tính khoản trừ.
- S030 · `f98a9700-7452-5674-8468-887833530de6`. Khách u03 dùng hạn người đi cùng để chọn giờ; nhà hàng u04 xác nhận đặt mới cụ thể, không tự chuyển bàn cũ.

Điểm nối đã đọc theo từng nhánh.

- S028 → S030. Tối cũ đã hủy, chưa hẹn lần mới và được gọi lại cùng số. Chỉ ở cảnh sau mới có thứ Bảy; nhân viên đưa chỗ trống, khách chọn 20 giờ.

Đã đọc Nhật và Việt riêng, đối chiếu hai bản theo vai, đổi vai và kiểm các nhánh đã ghi.

Rà độc lập toàn bộ chặng.

FAQ xác nhận số dư IC được đọc ở bản hiển thị kết quả tìm kiếm chính thức; lần mở trực tiếp trả 502. Dữ kiện cùng phạm vi đối chiếu với trang hướng dẫn và PDF chính thức về vận chuyển thay thế của Tokyo Metro. Đọc lại S028 → S030 sau khi chỉnh lời xin lỗi vì đã quá giờ đặt.

Đã đọc lại bản Việt ở 21 cảnh có người phục vụ nói trực tiếp với khách nữ để dùng “chị” hoặc lược chủ ngữ theo câu. Đọc lại S004 → S005, S008 → S010, S014 → S015, S024 → S025 và S028 → S030. Giữ giờ, giá, điều kiện vé và tình trạng chờ như bản Nhật.

## Rà độc lập Batch05 · E01

Ngày 2026-11-18 đối chiếu thứ tự Ōtemachi → Nihombashi → Kayabachō → Nishi-Funabashi trong [sơ đồ Tozai](https://www.tokyometro.jp/station/line_tozai/index.html). [Trang vận hành Tozai](https://www.tokyometro.jp/unkou/history/touzai.html) có chức năng cập nhật và thông tin theo đoạn; giờ và chuyến trong bài là giả định. Đọc B27 bài 8 dòng 26–38 về hỏi điểm tàu dừng và đường chuyển theo đích.

## Rà độc lập Batch05 · E02

Ngày 2026-11-18 kiểm [sơ đồ Hibiya](https://www.tokyometro.jp/station/line_hibiya/index.html) xác nhận điểm nối Ningyōchō–Suitengūmae và một ga theo hướng Naka-Meguro tới Kayabachō. [Sơ đồ Tozai](https://www.tokyometro.jp/station/line_tozai/index.html) cho thấy kết nối Hanzōmon ở Ōtemachi và Hibiya tại Kayabachō. Đường đi bộ được dùng như lựa chọn trong cảnh, không ghi thời lượng cố định. Lối Nam và mái che ở S007 thuộc ga giả định.

## Rà độc lập Batch05 · E03

Ngày 2026-11-18 đọc [hướng dẫn Tokyo Metro](https://www.tokyometro.jp/ticket/guide/substitute/index.html) và mục 29 của [PDF 営業のご案内, bản 14/03/2026](https://www.tokyometro.jp/support/guide/operation/pdf/information_20260314.pdf) về vé có sẵn đúng chặng, vé tháng trong chặng, loại trừ số dư nạp ngoài chặng và trả vé riêng trên đường đi vòng không thuộc diện. FAQ OpenFAQ-000377 đọc mục trả lời hiển thị trong kết quả tìm kiếm chính thức, lần mở trực tiếp không thành công. Chỉ xác nhận phạm vi Tokyo Metro. S012 hỏi tuyến thực hiện của ngày tập; S015 chuyển cách xử lý lượt vào/ra cho nhân viên ga. Đọc B27 bài 8 dòng 49–63 về hỏi và nhắc lại thuộc tính vé.

## Rà độc lập Batch05 · E04

Đọc B27 bài 8 dòng 105–115 về kiểm giờ và cửa ga khi hẹn. S019/S020 dùng ga giả định, cảnh nối dùng đúng điểm đã đính chính.
