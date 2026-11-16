# H-041 — Nguồn và tự rà biên tập

Tình huống là gói Sora Travel, tàu ST101, tuyến Nishimachi và khách sạn Mizu hoàn toàn giả định. Giá, thời gian, mã, chính sách giữ chỗ và khoản giảm chỉ là điều kiện của hồ sơ này. Không áp dụng quy tắc hoàn tiền của một hãng thật cho hồ sơ giả định. Kiểm nguồn chính thức ngày 2026-11-16: JNTO Safe Travel Information https://www.japan.travel/en/japan-safe-travel-information/ khuyên xem cập nhật giao thông; JR Central https://global.jr-central.co.jp/en/tickets/accident/ mô tả xử lý riêng cho vé của họ khi gián đoạn, nên cảnh luyện yêu cầu tra đúng đơn vị vận hành và không tự suy quyền hoàn. Các cảnh hỏi xác nhận theo từng bên, không viện điều khoản cụ thể.

## Nguồn đã đọc

- **B05-C07, dòng 153–180**: đã đọc phần yêu cầu tại lễ tân, đặc biệt báo đến muộn và hỏi giờ; áp dụng vào xác minh khách sạn Mizu, không chép mẫu nguyên văn.
- **B08-C05, dòng 95–122**: đã đọc phần khách sạn, đặt phòng và hành lý; áp dụng vào hội thoại đặt dịch vụ và điểm cần hỏi.
- **JNTO Safe Travel Information**, https://www.japan.travel/en/japan-safe-travel-information/ (truy cập 2026-11-16): tham khảo cập nhật vận hành; không là nguồn quy tắc hoàn của Sora Travel.
- **JR Central, In case of Accident**, https://global.jr-central.co.jp/en/tickets/accident/ (truy cập 2026-11-16): chỉ cho thấy xử lý gián đoạn là theo điều kiện hãng/vé; không gán quyền hoặc khoản tiền cho tuyến hư cấu.

## Chuyên đề trước

Đã đọc lesson.md và practice.json của sj-thuong-11. Dùng 急な話で恐縮ですが trong yêu cầu khẩn với mốc rõ, 急に言われても困る trong nhóm khi cần bàn trước, và いえ、結構です để từ chối hai ghế rồi xác nhận hành động. Chỉ gắn ID ở cảnh thực sự dùng; ドタキャン không cần đưa vào vì thông báo hủy được nói chính xác hơn.

## Tự rà từng cảnh

### E01 — Xác định sự cố và ưu tiên

- **S001 1b613599-347f-5c05-b8c6-27d79c2fba87** (routine; sau mở riêng): Tách đúng chặng tàu bị hủy khỏi hai dịch vụ chưa kiểm; phân công đối chiếu. 損失 chưa được suy. Nguồn: travel.
- **S002 d7e0afce-73a3-515e-9b90-3da3bfff8ee4** (routine; sau mở riêng): Ràng buộc về đúng giờ và hành lý được hỏi, không giả định Yui đã đồng ý. Nguồn: travel.
- **S003 63d6295e-2304-5f67-aac4-8c1adcee282b** (misunderstanding; sau mở riêng): Sửa hiểu nhầm toàn bộ hủy; trạng thái hiển thị không được coi là bảo đảm. Nguồn: travel.
- **S004 f4693387-68f0-5630-9d6f-2dc0655f68bb** (conditional; sau mở riêng): Ưu tiên ba người cùng đi và giờ về; tách nhóm cần hỏi Yui. Nguồn: travel.
- **S005 6f560539-5066-5e6c-a99e-e091330ed006** (resolved; sau S004): Sau khi hỏi Yui mới chốt điều kiện, phân công quầy và liên lạc. Nguồn: travel.

### E02 — Liên hệ quầy dịch vụ

- **S006 7c8d2c05-2d85-5292-b127-0fd9c7bb836a** (routine; sau mở riêng): Mã đặt và lời xác nhận rõ; không gán trạng thái các dịch vụ chưa kiểm. Nguồn: travel.
- **S007 1db43241-73cd-58ea-86e7-3d64db619814** (routine; sau mở riêng): Chuỗi hẹn–thông báo–ảnh hưởng, không nói hãng đã từ chối bồi hoàn. Nguồn: travel.
- **S008 176777c2-39df-5f81-accf-1dcab4d36e38** (pending; sau mở riêng): Pending hai đầu mối và thời hạn riêng, chưa tạo cam kết đổi. Nguồn: travel.
- **S009 f63d9bd3-5afd-5352-9eec-262b2aab9c82** (conditional; sau mở riêng): Hai ghế chỉ tạm giữ; bảo toàn lựa chọn cho ba người. Nguồn: travel.
- **S010 06b49e36-ab7c-52d3-b47a-a9127d038709** (declined; sau S009): Từ chối đúng hai ghế, giữ trạng thái đơn; chưa hứa phương án khác. Nguồn: travel.

### E03 — So phương án tại chỗ

- **S011 e583828f-9acc-5f0e-8017-e6908b277565** (routine; sau mở riêng): So thời gian, điểm đến, hành lý, tiền; ba ghế tàu/chi phí chưa xác nhận. Nguồn: travel.
- **S012 b8ad5ab2-87b1-5c05-9083-f17291d96e7f** (routine; sau mở riêng): Giải thích chờ quá lâu không đạt mục đích và đặt mốc, không biến nhu cầu thành quyền. Nguồn: travel.
- **S013 fb79a981-5818-5a08-acaa-0a817fdf4b90** (alternative; sau mở riêng): Chấp nhận có điều kiện chứ chưa chốt; ghế, kết nối, hành lý được tách. Nguồn: travel.
- **S014 7a947bef-471b-53b6-8726-1fd3ab9a75a8** (conditional; sau mở riêng): Phòng thay khác diện tích; chênh giá và nhóm đồng ý còn mở. Nguồn: hotel, travel.
- **S015 e4ec456f-5c20-545c-be7b-e6a9278ffb9b** (resolved; sau S014): Sau S014, nhóm đồng ý điều kiện phòng nhưng vẫn giữ tạm phụ thuộc tuyến; 6k là điều kiện giả định. Nguồn: travel.

### E04 — Phối hợp hai đầu mối

- **S016 0d87e079-1e17-5ca0-9049-9c31196e6edc** (routine; sau mở riêng): Tách phòng xác nhận khỏi giờ đến/giảm giá còn cần đối chiếu hai bên. Nguồn: hotel, travel.
- **S017 2dbd1e81-e631-511e-93e8-a85ddbb7eeaf** (problem; sau mở riêng): Không để lời khách thay xác nhận nhà cung cấp; giấy C-27 cần đối chiếu. Nguồn: hotel, travel.
- **S018 a42d2cd6-9f62-5540-bab8-aecd52c826da** (misunderstanding; sau mở riêng): Sửa nhầm arrival/departure trước khi tạo đặt phòng sai. Nguồn: hotel, travel.
- **S019 cd1cde02-083d-5c7a-b55e-38e8e3cf009b** (pending; sau mở riêng): Pending thực sự, người gọi và mốc 11:30 rõ; giờ tàu bên Travel xử lý. Nguồn: hotel.
- **S020 c50876a6-6b7e-59c8-8b7e-121cbf657704** (follow_up; sau S019): Sau S019: phòng đã chốt, tàu chưa; nhóm nghe kết quả, không nói toàn hành trình an toàn. Nguồn: hotel.

### E05 — Sự cố lặp trong hành trình

- **S021 cab0c62d-db08-51ef-b1ab-a218ee05e788** (routine; sau mở riêng): Sự cố lặp là chặng nối của phương án đã chọn, nhóm còn ở Tokyo; phòng đã chốt. Nguồn: travel.
- **S022 5f139d2e-f531-5d10-96bd-22cdacc719d0** (routine; sau mở riêng): Các option có trạng thái thời điểm hiện tại; không đưa hai ghế như lời giải. Nguồn: travel.
- **S023 0e6888cb-3bc2-5dba-86ec-84a37ebdfebd** (conditional; sau mở riêng): Người thứ ba chưa đồng ý; giữ lựa chọn và hỏi hệ quả tách. Nguồn: travel.
- **S024 ade27648-4a59-59c4-aadc-ffa94e57fea7** (declined; sau mở riêng): Từ chối hai ghế rõ, chuyển cấp; không coi lời đề nghị chỗ ở là xác nhận. Nguồn: travel.
- **S025 9e5ebf9c-f71a-533a-9d75-3f4a6b6976a8** (resolved; sau S024): Sau S024 chốt phương án tối nay đủ ba ghế, phòng có xác nhận; tiền vẫn pending. Nguồn: hotel, travel.

### E06 — Sau chuyến

- **S026 267ef1aa-619a-5d46-97a4-268b468622a0** (routine; sau mở riêng): Nhấn thanh toán thực 60k+9k; 6k là khoản hứa giảm chưa nhận, không cộng trừ nhầm. Nguồn: travel.
- **S027 da821e6e-1e7d-5c94-bd1b-8a6085fba5c4** (routine; sau mở riêng): Hai khoản pending tách, không hứa quyền hay số tiền tàu. Nguồn: travel.
- **S028 c4a0d31c-68d2-5984-9345-471b9dae270e** (pending; sau mở riêng): Chứng từ có mục đích, mốc nhận và mốc kết luận tách; chưa ra quyết định. Nguồn: travel.
- **S029 2455e479-4918-5dbe-9249-8b5e37ae591e** (follow_up; sau mở riêng): Follow-up sau mốc thật, tách processing vs tiền vào, tiền tàu vẫn chưa rõ. Nguồn: travel.
- **S030 f47020d3-234c-54a9-98b5-689867d6f09d** (resolved; sau S029): Sau S029 nhóm được cập nhật đúng pending vs paid; Nam nhận việc theo dõi, không khép hoàn tiền. Nguồn: travel.
