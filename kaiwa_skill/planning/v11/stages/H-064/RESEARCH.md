# H-064 — nhật ký biên soạn

Đã đọc brief V10 đủ 36 cảnh, chín sự kiện và sáu chặng liên quan về tìm khách, đàm phán, đổi yêu cầu, demo, bàn giao và nhìn lại. Đã tra cả catalog27 theo 見積・納期・交渉・報告・引き継ぎ và đọc B15 14課 dòng 55–78, 7課 dòng 16–41, 8課 dòng 24–65 cùng B03 Unit 18 dòng 23–67. Đã đọc bài và 15 đoạn luyện cùng topic ở sj-thuong-18, dùng cách kết luận, nêu thêm mục bổ sung hoặc khép báo cáo khi thực sự có bước tương ứng. Ngày 2026-11-18 đã đọc phần tổng quan IPA, https://www.ipa.go.jp/digital/model/model20201222.html, về làm rõ đặc tả, trách nhiệm quản lý và cách nghiệm thu trong thuê phát triển. Trong cảnh, mức dự toán, phạm vi, ngày, quyền duyệt và lịch hỗ trợ do hai công ty giả định đặt ra.

Mori thực thi và điều phối phía cung cấp. Okabe quyết việc nội bộ bên cung cấp. Kanda gom yêu cầu và liên hệ phía khách, trưởng bộ phận Fujita quyết đặt hàng và nghiệm thu phía khách. Imai trực tiếp vận hành. Nishida phụ trách phần kỹ thuật. Mốc dùng thử hai chi nhánh là ngày 24 tháng 6. Mốc xử lý phần tiếp nhận trong phương án hẹp là ngày 20. Các cảnh rẽ chỉ nhận dữ kiện đã có ở điểm rẽ. Trước khi giao việc, hai bên đã duyệt phương án hẹp ngoài cảnh. Đợt mở rộng vẫn để bàn sau.

## E01 — Khách nêu cơ hội

- S001 · `f9a3ace1-aa2e-53c5-b662-8fdeb9686c75`. Mori u02/u04 hỏi điểm nghẽn và ngày cần dùng; Kanda phân biệt hai chi nhánh với ngày mở toàn bộ.
- S002 · `adb9c84e-f37e-5940-9fcf-f3f3d032b3e5`. Mori u02 hỏi điều kiện khiến thử nghiệm phải dừng; khách giữ luồng nhận đơn và cho phép bảng theo chi nhánh làm sau.
- S003 · `16a02eff-00f5-5b46-9f6a-24985bc49865`. Mori u01/u03 tách người dùng, đại diện vận hành, người chốt tiền và phạm vi; Kanda xác định mình chỉ tập hợp yêu cầu.
- S004 · `7164c535-ea1a-5013-8f0e-e2980571905e`. Kanda chưa thể quyết; Mori u04-u06 chốt hai khung giờ để Kanda kiểm và giờ gọi lại, không giữ lịch như đã hẹn.

Điểm nối đã đọc theo từng nhánh.

- S001 → S002. 24/6 hai chi nhánh phải nhận đơn được; lời nhắc bảng tổng hợp là yêu cầu mới được phân loại ở cảnh sau.
- S003 → S004. Kanda biết Fujita mới có quyền duyệt, chưa có lịch của Fujita; cuộc hẹn giữ ngày gửi lựa chọn và giờ liên hệ.

## E02 — Đề xuất và thương lượng

- S005 · `de567d20-da51-520a-8742-a9c999e16356`. Mori u01/u03 phân biệt 80/120 man và 20/28 tháng 6; Kanda u04 dùng thông tin để đưa hai lựa chọn đi bàn.
- S006 · `9517ec28-b3f0-59cd-81f4-04305a82435c`. Mori u02/u04 gọi tên việc kiểm số bị mất nếu ép mốc và đưa cách giao tách; Kanda xác định ngày 20 cần phần nhận đơn.
- S007 · `a2b33a79-8fa9-516e-ac1e-32153faa6a22`. Mori u02 hỏi chi tiết có thể lùi thay vì tự giảm đồng loạt; Kanda giữ phần nhận và danh sách.
- S008 · `94bf4373-dd3e-527f-940b-4af4ab198417`. Mori u02 kết luận bước trình duyệt từ hai thời điểm; Kanda chốt lịch người duyệt và trạng thái chưa đặt.

Điểm nối đã đọc theo từng nhánh.

- S005 → S006. Hai gói và ngày đã được nêu, chưa chọn; nhanh hơn chỉ giữ phần phục vụ ngày thử, phần xuất dữ liệu còn mở.
- S005 → S007. Bị bác mức 120 man; không nói khách đã chọn phương án của nhánh muốn nhanh.
- S007 → S008. Giữ nhận đơn và danh sách chưa xử lý, chờ người duyệt; xuất CSV chưa định phạm vi hoặc giá.

## E03 — Phân việc nội bộ

- S009 · `a9f621df-21cf-5a4e-8d56-4736cbd4d4a1`. Mori u01/u03 và Nishida u02/u04 đặt tên đầu ra, đầu vào và mốc chuyển; để hở bước kiểm mẫu nội bộ cho cảnh nối.
- S010 · `d1610cce-d8c1-5351-8e8b-11eb57eb827b`. Mori u03 xác định ai kiểm và ai nhận yêu cầu, u05 nhắc chính mình chỉ gửi sau khi Nishida báo kết quả.
- S011 · `c965c717-e024-59c1-8883-8238c4a7dbab`. Mori u01/u03 xin điều kiện và khung giờ thật, chưa báo mốc chắc; Nishida xác định cần người ngoài phần làm màn hình.
- S012 · `0703d9b4-1651-53b3-8aa1-912e5b77bc8b`. Mori u01/u03 xác nhận Tanabe nhận lịch và đặt giờ giao; Nishida nhắc lại phần kiểm, Mori nắm điều kiện báo ngày 20.

Điểm nối đã đọc theo từng nhánh.

- S009 → S010. Nishida làm mẫu và Mori đưa Imai xem, chưa ai rõ chủ kiểm dữ liệu nội bộ. Nhân vật tự nhận phần còn thiếu trước khi gửi.
- S011 → S012. Kỹ sư QA chỉ được nhờ mở lịch ở gốc. Mori xác nhận Tanabe nhận lịch rồi mới chốt mốc với Nishida.

## E04 — Thực hiện và báo tiến độ

- S013 · `d3860e51-95ad-5ce4-8240-328a21162629`. Mori u01/u03 tách việc gửi đơn đã chạy với quyền còn kiểm và khép báo cáo; Kanda u04 giữ phần hướng dẫn về quyền ở trạng thái chờ.
- S014 · `f06627f8-908c-5aa6-9c08-d35d53c5256c`. Mori u02/u04 tách mốc có kết quả chưa biết và giờ gọi chắc; Kanda giữ phần chưa kiểm khỏi bản hướng dẫn chiều.
- S015 · `397fa6b4-8c5a-519d-921e-d9f091b9e915`. Mori u02/u04 nêu đầu vào cần, phần không đổi và mục phải dời; Kanda xác nhận có thể bàn lịch riêng cho tài khoản.
- S016 · `39c6a4f3-88b8-57ff-89cb-c8b4a0399409`. Kanda u01 đưa mốc có lý do; Mori u02/u04 dùng danh sách sáng 19 làm điều kiện để giữ 21 trưa và nhắc riêng ngày 20.

Điểm nối đã đọc theo từng nhánh.

- S013 → S014. Gửi đơn và xem danh sách đã kiểm, quyền theo chi nhánh còn thử; Kanda vẫn chưa thể chốt hướng dẫn, nhận giờ cập nhật 16:00.
- S015 → S016. Hai bên đã thống nhất giao màn hình ngày 20 và cần dời tài khoản tên thật; khách mới đề nghị ngày 21 giờ trưa ở nhánh này.

## E05 — Khách đổi yêu cầu

- S017 · `96908188-f2b4-5869-abc0-e2c88803cb7c`. Mori u02/u04 hỏi người trực và thời điểm cần biết; Kanda làm rõ email đến hộp chung khi có đơn mới.
- S018 · `2f38bd86-925c-5c71-9653-f2544fe7fb76`. Mori u02/u04 giải thích phải thêm kiểm gửi và kiểm thất bại; khách hiểu giá chưa biết và yêu cầu bước thông báo nếu trễ.
- S019 · `ac0132a4-64a3-5c35-85e0-954165ec97d7`. Mori u02/u04 đề xuất bỏ tổng số chung ở đợt đầu và làm rõ không hứa khi chưa duyệt; Kanda đồng ý mang đi hỏi.
- S020 · `33c1af0d-4c0e-5e67-aeab-b3fa02448d70`. Mori u01/u03/u05 xác nhận duyệt nội bộ và từng đầu ra; Kanda u04 dẫn lại căn cứ quyền quyết của Fujita rồi xác nhận phía mình.

Điểm nối đã đọc theo từng nhánh.

- S017 → S018. Kanda xác nhận cần email khi có đơn mới dù không mở danh sách. Nhánh hỏi giá giữ bảng tổng hợp trong phạm vi đang duyệt và chưa chấp thuận thêm.
- S017 → S019. Dùng đúng cùng vấn đề của gốc, chưa có tranh luận về giá hoặc cam kết gửi báo giá của nhánh kia. Mori đề xuất đổi bảng tổng hợp lấy email.
- S019 → S020. Phương án hoán đổi còn chờ Okabe và Fujita. Khách đã đưa cho Fujita xem, Fujita chỉ xác nhận sau khi nghe giá và mốc do Mori báo ở cảnh sau.

## E06 — Sự cố phát sinh

- S021 · `7db9a37e-bf84-5996-b79f-1b3c05101f5e`. Mori u01/u03 tách lỗi đã thấy và phạm vi đã xác nhận; Okabe xin xác minh thêm và không lẫn môi trường dùng thật.
- S022 · `51fcc120-6895-5571-a75e-6de2d53df669`. Mori u01/u03 đưa hai việc và đề xuất kiểm lại luồng tiếp nhận, Okabe quyết ưu tiên và nói dấu hiệu cần thấy.
- S023 · `04539a7c-1a36-5d48-b7da-d5b937f3b1aa`. Mori u01/u03 nêu điều còn mù và nhận việc gọi khách; Okabe chốt Nishida, mốc nội bộ 15:30 và cuộc gọi 16:00.
- S024 · `0d777f88-e675-5edd-81d7-3e7aa2970f4b`. Mori u01/u03 giới hạn nguyên nhân và kết quả ở bản thử; Kanda dùng hướng dẫn để thử lại, chưa suy ra đã triển khai thật.

Điểm nối đã đọc theo từng nhánh.

- S022 → S023. Okabe ưu tiên nhận đơn cho hai tài khoản chạy thử trước thống kê; Nishida chưa được chính thức giao điều tra tại điểm rẽ.
- S023 → S024. Mori đã nhận việc gọi khách lúc 16:00 với điều biết. Bản thử xác minh lại sau sửa, chưa đủ để khẳng định môi trường dùng thật.

## E07 — Demo và chốt nghiệm thu

- S025 · `3288f1b3-800b-5069-a42b-4cd237767227`. Mori u01/u03 mời khách thực hiện từ đầu; Kanda thực sự gửi và đo thời gian email, chưa nói cả hệ thống đạt.
- S026 · `13d4b74f-31bf-52d1-962c-06cb58e089aa`. Kanda u01 nêu điểm chưa đạt dù luồng nhanh; Mori u02/u04 hỏi cần thấy ở đâu và cả hai đồng ý hai chi nhánh thử lại.
- S027 · `0a644b17-2cce-5adf-b496-7046fe6b57b2`. Kanda u01/u03 trao đổi điều kiện với Mori chứ chưa thay Fujita duyệt; Mori u02/u04 chốt bản sửa chậm nhất ngày 22 và cùng kiểm.
- S028 · `361bc758-82a2-59b5-8094-fb237362db7a`. Mori u01 hỏi chính trạng thái nghiệm thu tách với đã gửi. Kanda u02 dẫn phản hồi Fujita, u04 phân biệt đợt thử với triển khai rộng.

Điểm nối đã đọc theo từng nhánh.

- S025 → S026. Luồng gửi từ Đông đã qua và email tới trong năm phút. Kanda mới cho biết email thiếu tên chi nhánh, không biến bài demo thành chấp nhận hoàn tất.
- S026 → S027. Kanda đã chốt tên chi nhánh cần nằm ở tiêu đề. Sửa và ngày kiểm lại được đưa ra ở cảnh nối, ngày 24 giữ có điều kiện.
- S027 → S028. Chậm nhất 22 giao bản sửa để Kanda xem cùng Fujita; kết quả nghiệm thu tới sau khi cả hai chi nhánh đã thử lại và Fujita phản hồi.

## E08 — Bàn giao và hỗ trợ

- S029 · `2f6843a9-babd-5b86-964b-7bca9fe9c090`. Mori u01/u03 nói phần xong, quan sát tuần đầu, đầu mối và dữ kiện cần báo; Imai nhắc lại phạm vi vận hành.
- S030 · `e14dc8f6-44a5-505e-82b6-b496e42581af`. Mori u02/u04 sửa hiểu lầm bằng hai đường liên hệ, Imai nhắc lại đúng ngày chuyển và người chuyển.
- S031 · `60a0167b-fe69-5e69-81ca-0f7cb8d0f779`. Mori u01/u03 cho người vận hành thao tác và phân loại lỗi; Imai tự đánh dấu đơn, nói tình huống cần báo và hẹn sau ba ngày.
- S032 · `51710a41-f4a8-533c-afba-38c3c9f4ca3c`. Mori u01/u03 hỏi thao tác vướng và nêu cách xử lý cho cả nhóm; Imai thử ngay và chọn test thật ngày mai.

Điểm nối đã đọc theo từng nhánh.

- S029 → S030. Đầu mối vẫn mở trực tiếp tới hết 30/6, qua Kanda từ 1/7; chỉ đổi luồng sau tuần theo dõi.
- S031 → S032. Imai dùng quyền đã xác định để thử lọc và cập nhật trạng thái; vẫn giữ báo lỗi kỹ thuật cho hỗ trợ; mốc gọi sau ba ngày khép trong tuần đầu.

## E09 — Nhìn lại và quan hệ tiếp

- S033 · `2b881f13-9a97-5237-99f7-fad8c6865c6e`. Okabe u01/u03 gợi điều cụ thể và kiểm quan hệ nhân quả; Mori u02/u04 nêu chuyện Imai thử sớm và quyết giữ cơ hội xem mẫu.
- S034 · `40e1d3aa-8d39-5f35-af09-a7d1859df689`. Okabe u01 mở dữ kiện lúc mất thời gian, Mori u02/u04 đề xuất ngưỡng báo và bước đo; hai người giao đúng đầu mối.
- S035 · `5bb4b45c-aaf0-5904-a47e-92f655657ab0`. Mori u02/u04 nêu thay đổi sẽ làm thật, tiếp nhận yêu cầu có giờ hẹn; Kanda có căn cứ báo chi nhánh trong khi chờ.
- S036 · `5a6b67a3-3bb6-5e93-8770-fc90e0f609ff`. Kanda u01 đề nghị áp dụng thỏa thuận trước, Mori u02 đưa ngay một báo cáo có phần đã biết và giờ 14:00; khách điều chỉnh kế hoạch thật.

Điểm nối đã đọc theo từng nhánh.

- S033 → S034. Đội đã nhìn ra việc đưa mẫu sớm có ích. Vẫn có thời điểm báo sự cố muộn, được nói riêng ở cảnh sau và không phủ nhận ngày chạy thử đã giữ.
- S035 → S036. Mori đã nói với Kanda về cách báo sớm khi biết ảnh hưởng. Dự án sau đưa cùng quy tắc vào một tình huống thực tế với giờ cập nhật mới.

Đã đọc Nhật và Việt riêng, thử đảo vai và đọc nối mọi cạnh. Chờ rà độc lập.

## Rà độc lập Batch04 · E01

- S002 · `adb9c84e-f37e-5940-9fcf-f3f3d032b3e5-u02`. Lời Nhật vừa hỏi lại điều kiện bằng 確認, lời Việt giữ sức nặng của 困ります ở yêu cầu tổng hợp. Câu hỏi hoãn hay chạy làm lộ điều kiện thật là nhận và thấy đơn chưa xử lý.
- S004 · `7164c535-ea1a-5013-8f0e-e2980571905e-u06`. Giữ hai khung giờ ở trạng thái đề xuất đến cuộc gọi của Kanda. Sửa câu chốt Việt để người học nói được tự nhiên khi cuộc hẹn còn chờ xác nhận.

Điểm nối. S001 kết bằng mục tiêu gửi–nhận đơn ở Đông và Tây ngày 24/6, S002 chỉ thêm yêu cầu về số riêng chi nhánh rồi kiểm liệu thiếu số có phải hoãn. S003 chốt Imai xem thao tác, Fujita quyết việc đặt làm. S004 vẫn chờ Fujita xác nhận lịch thứ Năm và chỉ giữ 10 hoặc 15 giờ làm giờ đề xuất, Kanda gọi lại chiều thứ Tư.

Nguồn đã mở ở lượt rà ngày 2026-11-18. B15 bài 14 dòng 55–78 cho cách hỏi rào cản sau lời từ chối và đưa đề xuất về đúng người quyết. Đã đọc mục 背景・概要 của [IPA, 情報システム・モデル取引・契約書（第二版）](https://www.ipa.go.jp/digital/model/model20201222.html). Trang mô tả vai trò của mẫu hợp đồng trong việc giúp phía khách và bên cung cấp thống nhất đặc tả, cách quản lý dự án và cách nghiệm thu. Rà trong phạm vi trang tổng quan. Các mốc, mức dự toán và người có quyền duyệt trong chặng là dữ kiện của dự án giả định.

## Rà độc lập Batch04 · E02

- S008 · `94bf4373-dd3e-527f-940b-4af4ab198417-u04`. Lời Việt phân biệt phần màn hình dùng được ngay trong đợt một. Kanda chỉ xác nhận Fujita có mặt lúc 10 giờ, việc đặt giai đoạn hai để sau.

Điểm nối. S005 chỉ mang hai báo giá về bàn. Từ đó S006 đánh đổi thời gian kiểm số và còn phải tính lại lịch/giá nếu chia đợt; trở về đúng S005 ở S007, gói 120 man khó duyệt và Kanda giữ biểu mẫu cùng danh sách chưa xử lý. S008 đi từ S007, nhờ Fujita xem giai đoạn đầu lúc 10 giờ thứ Năm, CSV chờ kết quả thử.

## Rà độc lập Batch04 · E03

- S010 · `d1610cce-d8c1-5351-8e8b-11eb57eb827b-u03`. Mori nhận phần phân công chưa rõ và chia lại: Nishida đối chiếu hiển thị, Mori chuẩn bị các mục nhờ Imai xem. Làm rõ cụm sắp lại trong Việt.

Điểm nối. S009 hẹn Nishida giao mẫu sáng 17, Mori nhờ Imai xem hôm sau, chưa giao người đối chiếu nội bộ. S010 đặt Nishida kiểm và trả 11:30 trước khi Mori gửi. S011 chỉ ngỏ lời hỏi Tanabe hai giờ ngày 19; S012 xác nhận Tanabe nhận 13–15 giờ, yêu cầu chuẩn bị trước trưa và để việc báo mốc 20 sau kết quả.

Đã mở B03 Unit 18 dòng 23–67. Các mục 報告・連絡・相談 cung cấp cách báo điểm chính, báo thay đổi và trao đổi việc cần ý kiến. Vai, mẫu dữ liệu và lịch kiểm thử trong các cảnh là tình tiết biên soạn.

## Rà độc lập Batch04 · E04

- S013 · `d3860e51-95ad-5ce4-8240-328a21162629-u03`. Phân biệt luồng gửi đơn và lọc đã kiểm với quyền xem riêng từng chi nhánh vẫn đang kiểm. Đổi cách diễn đạt Việt ở câu chốt của Kanda để chỉ đúng quyền truy cập.
- S014 · `f06627f8-908c-5aa6-9c08-d35d53c5256c-u02`. Mori cam kết giờ báo 16 giờ, chưa hứa giờ kiểm xong. Việt ở lượt quyết định của Kanda nói rõ hoãn hướng dẫn về quyền xem đơn.
- S016 · `39c6a4f3-88b8-57ff-89cb-c8b4a0399409-u02`. Giữ điều kiện nhận danh sách trong sáng 19 và mốc 21 đúng trưa. Việt trước dễ nghe thành hạn trước buổi sáng; lượt chốt nêu điều kiện để không biến thành cam kết vô điều kiện.

Điểm nối. S013 để quyền xem đơn của chính chi nhánh ở trạng thái kiểm. S014 nối đúng điểm chờ đó, hẹn báo 16 giờ và chỉ chuẩn bị sẵn hướng dẫn gửi đơn. S015 giữ màn hình ngày 20 nhưng chưa định ngày giao tài khoản. S016 thêm hạn trưa 21 kèm điều kiện nhận danh sách trong buổi sáng 19, giữ ngày thử 24.

## Rà độc lập Batch04 · E05

- S018 · `2f38bd86-925c-5c71-9653-f2544fe7fb76-u04`. Lượt trước hứa có kết quả về giá và lịch muộn nhất 15 giờ, lượt cuối lại chừa khả năng chưa xong. Sửa lời hẹn thành cập nhật phần đã kiểm lúc 15 giờ dù phép tính còn mở.
- S020 · `33c1af0d-4c0e-5e67-aeab-b3fa02448d70-u04`. Điều kiện Fujita giao là không đổi ngày và chi phí. Mori nay xác nhận cả hai giữ nguyên, nên Kanda có thể xác nhận phạm vi. Việt ở lượt đầu trình bày phương án đã duyệt rõ hơn.

Điểm nối. S017 chốt mục đích gửi thư vào hộp chung lúc có đơn mới. S018 hẹn cập nhật giá và lịch dù kết quả phân tích có thể còn chờ; S019 trở về S017, đề nghị hoán đổi tính năng, chưa có bất kỳ cam kết nào từ S018. S020 cho hay bên Mori đã duyệt, Kanda dùng đúng điều kiện Fujita đã cho là giữ giá/lịch rồi mới xác nhận.

## Rà độc lập Batch04 · E06

- S021 · `7db9a37e-bf84-5996-b79f-1b3c05101f5e-u03`. Mori mới có báo từ hai chi nhánh và đã tái hiện ở môi trường thử. Giữ độ chắc của 少なくとも trong Việt, tránh biến xác nhận phạm vi tối thiểu thành phủ định mọi ảnh hưởng khác.
- S024 · `0d777f88-e675-5edd-81d7-3e7aa2970f4b-u03`. Cuộc gọi phân biệt hai tài khoản thử đã xác minh và môi trường thật còn phải kiểm trước chuyển. Chỉnh lời xin lỗi Nhật để khớp Việt và nêu đúng lỗi cài đặt phía Mori.

Điểm nối. S021 báo sự cố trước ở môi trường thử. S022 đặt chuẩn khôi phục là mỗi chi nhánh gửi một đơn và hiện tại trụ sở. S023 giữ chuẩn đó, giao Nishida kiểm, cập nhật nội bộ 15:30 và Mori gọi khách 16:00. S024 đáp cuộc gọi bằng nguyên nhân đã rõ và kiểm đủ hai đơn, chỉ cho tiếp tục thử.

Đã đọc B15 bài 7 dòng 16–41 và bài 8 dòng 24–65. Đoạn báo cấp trên tách ảnh hưởng, căn cứ và việc cấp trên nhận. Đoạn xử lý khiếu nại chuyển sang báo nguyên nhân sau khi xác minh. Các đoạn được dùng để tham khảo cách trao đổi, câu sửa trong cảnh là lời mới.

## Rà độc lập Batch04 · E07

- S028 · `361bc758-82a2-59b5-8094-fb237362db7a-u02`. Fujita mới có quyền nghiệm thu. Chuyển lời Kanda thành thuật lại xác nhận đã nghiệm thu từ Fujita để lượt sau có căn cứ gọi là hoàn tất; ghi rõ ngày 23 để 明日 thống nhất với ngày 24.

Điểm nối. S025 Kanda gửi từ Đông, thư tới sau hai phút; S026 bổ sung tiêu chí đọc tên chi nhánh ngay ở tiêu đề và cả hai nơi dưới năm phút. S027 chốt bản sửa trưa 22, thử lại 15 giờ và chuyển Fujita nếu đạt. S028 đặt rõ ngày 23, Fujita xác nhận đã nghiệm thu sau kết quả của ngày 22, chỉ chạy thử hai chi nhánh ngày 24.

## Rà độc lập Batch04 · E08

- S030 · `e14dc8f6-44a5-505e-82b6-b496e42581af-u04`. Làm rõ câu hỏi gửi vào đâu từ 1/7 bằng một đầu mối cụ thể. Nói rõ hộp Hỗ trợ chạy thử dùng trong tháng Sáu, tránh để Imai phải đoán thư có tới hoặc hỗ trợ đã dừng.

Điểm nối. S029 hoàn tất bàn giao trước ngày 24 và gửi thẳng hỗ trợ thử đến hết 30/6. S030 chỉ thay đầu mối từ 1/7 khi Imai nghe nhầm là hết hỗ trợ. S031 để Imai tự thao tác và hẹn gọi sau ba ngày. S032 nối đúng cuộc gọi, vẫn dùng quyền Imai đã có để sắp đơn chưa xử lý lúc đổi ca.

## Rà độc lập Batch04 · E09

- S035 · `5bb4b45c-aaf0-5904-a47e-92f655657ab0-u04`. Kanda nói bất tiện khi phải chờ; Mori cam kết cả phạm vi đã biết và giờ cập nhật. Bỏ câu kết kiểu báo cáo khiến lời trò chuyện với khách bị cụt.
- S036 · `5a6b67a3-3bb6-5e93-8770-fc90e0f609ff-u01`. Để chứng minh quy ước được thực hiện, Mori chủ động gọi ngay khi xác nhận vướng, rồi báo phần bị ảnh hưởng, phần vẫn chạy và mốc 14 giờ. Kanda không phải đi hỏi mới được báo.

Điểm nối. S033 nhận ra ích lợi của duyệt mẫu sớm; S034 giữ việc đó và xử lý riêng khoảng chờ báo lỗi ở môi trường thử. S035 đưa quy ước báo phần đã biết lẫn giờ báo tiếp tới Kanda. S036 đặt ngay cuộc gọi từ Mori về thống kê Tây, Kanda dùng dữ kiện để tiếp tục nhận đơn và đợi 14 giờ.

Dấu vân tay nguồn IPA trong hồ sơ rà là SHA-256 của ghi chú `admin_sources.ipa.use_vi` bằng UTF-8, không có xuống dòng cuối. Dấu vân tay nguồn trước lượt rà được giữ trong lịch sử nguồn của tác giả.
