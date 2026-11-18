# T-118 — Làm người phụ trách chuyến du lịch công ty

Đã đọc mục tiêu và bảy sự kiện, đối chiếu 31 cảnh cùng từng cạnh từ brief V10. Tra chỉ mục 27 sách theo 社員旅行・旅行・団体・集合・宿泊・バス・幹事・旅程・引率, đọc ba tập bài 8, đối chiếu sách đặt phòng và giờ/điểm tập trung. Bài 8 dạy người hỏi về chuyến và đăng ký; dùng cho chức năng hỏi/đáp và đầu mối, mở rộng bằng lời của người điều phối, không giữ giả định người đi phải hát. Đã đọc mục tiêu T-117 về tổ chức tiệc và H-053 về dẫn chương trình để giữ phạm vi chuyến đi. Đã đọc lesson.md và thực hành sj-trung-29, nối lại chỗ từ chối và hỏi phép tự nhiên. Chi phí, giờ, thẩm quyền, điểm gặp và phương án dự phòng là dữ kiện riêng của tình huống.
Nguồn allergy, đọc 2026-11-18. Đã đọc mục hướng dẫn tại trang 7 về trả lời đúng mức biết, nguy cơ từ dùng chung đồ bếp hoặc dầu và chuyển thông tin cho khách cân nhắc. [外食・中食事業者向け食物アレルギーパンフレット｜消費者庁](https://www.caa.go.jp/policies/policy/food_labeling/food_sanitation/allergy/assets/food_labeling_cms204_230324_03.pdf)
Nguồn emergency, đọc 2026-11-18. Hướng dẫn 119 là đường gọi khẩn và tiếp nhận thông tin cần cho điều xe, không dùng để hỏi thông tin thông thường. [119番緊急通報｜総務省消防庁](https://www.fdma.go.jp/mission/enrichment/kyukyumusen_kinkyutuhou/119.html)

## E01 — Nhận vai phụ trách chuyến

Lấy điều kiện để chuẩn bị thông báo: mục đích giao lưu, tự nguyện, phê duyệt chi, đầu mối lúc có sự cố. S003 chỉ kế thừa cuộc trao đổi về mục đích và người được mời.

- S001 · `ac7a9fed-ca4b-538d-8092-71499258c79c`. An u01/u03 hỏi mục đích và người dự, xác nhận tự nguyện; Kanda giữ vai duyệt nội dung lời mời.
- S002 · `2369cd2c-25b6-58d6-8083-e21bea893fbb`. An hỏi trần và quyền tự quyết, nhắc lại báo giá chưa thành đặt chỗ.
- S003 · `32e5fc8e-f597-5ffc-ab54-a7990e0224f8`. An đề xuất lộ trình có chỗ tách đoàn và quay lại, Kanda chốt nguyên tắc cho riêng chương trình.
- S004 · `de300bc3-9733-55b3-88fd-7f13f5d1b207`. An định đầu mối theo loại việc và có người trực khi mình đi hỗ trợ.

Điểm nối đã đọc theo từng nhánh.

- S001 → S003. S001→S003 giữ mục đích giao lưu và quyền không đi; người đã đi cũng được chọn hoạt động.

## E02 — Hỏi nhu cầu người tham dự

S005 hỏi lịch tạm trước khi đặt. S006 và S007 là hai phản hồi thay thế của Sano. S009 nối riêng S007 khi lịch dừng ga đã xác nhận; S008 là hỏi riêng nhu cầu trước khi chuyển cho nhà hàng.

- S005 · `da57bfb3-4ea6-564a-8433-34d329389a68`. An nói hai mốc và mời nêu phần có thể tham gia. Sano chưa chọn, sẽ xem lịch và trả lời vào hôm sau.
- S006 · `eb9947cb-af63-5906-b252-7258690af2a1`. Sano nói từ chối, An xác nhận cách ghi và không yêu cầu giải thích với đoàn.
- S007 · `0082b628-2aa4-557c-a5d6-1ac37368e487`. Sano dùng xin phép lịch sự, An nêu mốc cần kịp và chỉ điểm dự kiến, chưa bảo đảm xe dừng được.
- S008 · `7500fc48-c830-5e94-acdd-b2707cba91e9`. An xin phép chuyển đúng nội dung cần hỏi; chỉ trả thông tin nhà hàng xác nhận, người dự tự cân nhắc.
- S009 · `67b4dd3d-3581-5169-a483-203f932b41d0`. An cho giờ và điểm xuống, Sano đồng ý, An cập nhật lịch nửa chặng.

Điểm nối đã đọc theo từng nhánh.

- S005 → S006. S005→S006 từ chưa định thành không dự; nhánh này không lấy thông tin về điểm rời đoàn ở S007.
- S005 → S007. S005→S007 chọn đi thứ Bảy sau khi xem lịch, không kế thừa lời từ chối S006.
- S007 → S009. S007→S009 giữ tàu 16 giờ 30 và hạn tới ga 16 giờ 15. Giờ dự kiến 16 giờ có dư thời gian nhưng không biến thành bảo đảm.

## E03 — Làm việc với nhà cung cấp

S010 đối chiếu xe 18 người; S011 và S012 rẽ từ chuyến đang đặt. S011 sửa giờ xuất bến xe với giờ xuất phát chở khách. S012–S014 trao đổi riêng với khách sạn, qua báo giá, xin duyệt và chốt đúng điều kiện.

- S010 · `64138ac9-7e14-5c87-918b-97c153e06e58`. An nói đủ ba dữ kiện, yêu cầu phân biệt giờ xe đến đón và giờ xe lăn bánh.
- S011 · `b123315c-d850-56c7-b078-6dd699544ded`. An chỉ đúng chỗ lệch trên giấy, Noda giải nghĩa rồi sửa nhãn giờ. An giữ giờ công bố đúng.
- S012 · `fb46c767-ae60-592a-8f1a-3bbafb88d7b8`. An hỏi số phòng, sức chứa, giá và điều kiện loại phòng, chưa xác nhận nhận phương án.
- S013 · `8762c434-ae8a-575f-abce-83163f9a6b48`. An tách đã nhận phương án với đồng ý, xin mốc đủ để lấy ý kiến, không để kết thúc thành chốt ngầm.
- S014 · `39cca268-622f-5056-a09b-870f7da13638`. An nói hai điều kiện đã đạt và đọc lại điều khoản. Endo tiếp nhận đặt sửa và hẹn bản xác nhận.

Điểm nối đã đọc theo từng nhánh.

- S010 → S011. S010→S011 vẫn 18 người, cùng điểm ga Chūō, xe vào 8 giờ 30 và chở đoàn đi 8 giờ 40; 8 giờ 20 là giờ xe rời bãi.
- S010 → S012. S010→S012 đoàn vẫn 18 người. Bên lưu trú là Endo; giờ và điểm xe vừa xác nhận chưa thay đổi.
- S012 → S013. S012→S013 cùng phương án 16 đơn và một hai giường, 18 người và tổng giá không đổi, chưa chấp thuận.
- S013 → S014. S013→S014 cùng thời hạn và cùng loại/số phòng, lấy đủ người duyệt và hai khách trước khi đổi.

## E04 — Trước giờ đi

Thời điểm tập trung trước 8 giờ 40, điểm đón ở lối Nam. S015→S018 giải quyết hai cửa gần nhau, còn S016→S017 xử lý chậm giờ ở một cuộc gọi khác.

- S015 · `8dfb2aaf-26f6-59d2-93f6-bb4cf6063af7`. An phân biệt ga, cửa và chỗ đứng, sau đó kiểm tra cách Mori hiểu giờ gặp và giờ xe đi.
- S016 · `260dcfe9-c9aa-5f61-ade7-369e52ca0cc0`. An hỏi vị trí và giờ tới thay vì đoán; Mori ở ga Aoba vì tàu chậm và sẽ cập nhật.
- S017 · `86cf2293-a254-5889-8553-e54b21cdd966`. An nêu giờ không chờ, chỉ chỗ và giờ gặp ở nơi đến, xác nhận mốc liên hệ tiếp theo.
- S018 · `0f671e8f-c8f2-5dd7-9ea6-6da095579569`. An hỏi chữ trên biển, phân biệt cửa phía Đông và lối Nam chính, cho chỉ dẫn từ nơi Mori đang đứng.

Điểm nối đã đọc theo từng nhánh.

- S016 → S017. S016→S017 Mori vẫn tới ga sau giờ xe. An đã kiểm phương án gặp sau và gọi lại như hẹn.
- S015 → S018. S015→S018 giữ giờ 8 giờ 25 và đồng hồ ngoài lối Nam. Đây là nhánh nhầm cửa, Mori không mắc kẹt ở ga Aoba như S016.

## E05 — Trong chuyến có thay đổi

S019 và S020 giữ hai lựa chọn vì mưa, điểm gặp lại trước bữa trưa. S021→S022 chỉ báo giờ xe đến sau khi xác nhận lại lối, tách khỏi nhánh thời tiết. S023 ưu tiên hỏi người cần giúp và nối đầu mối tại chỗ.

- S019 · `8dab039b-84cd-50e1-a1c6-3498936a7a84`. An nói hoạt động hủy, nêu giờ và quyền chọn chỗ nghỉ, không trộn giờ của phương án cũ.
- S020 · `fc1dff01-d2e2-5512-ad73-ddba6431312a`. Mori từ chối lựa chọn và báo số nhóm, An chốt mốc và xử lý nếu ai ra ngoài lâu hơn dự kiến.
- S021 · `0c964527-dec4-532a-9fdd-4682002fcf0c`. An đọc đúng nơi nhóm đứng, yêu cầu xác nhận đổi hướng và giờ trước khi báo đoàn.
- S022 · `37ce0c95-c5cf-59fa-b8c0-b61f34be96bb`. An nói xe đã có mặt và phân biệt giờ dự kiến mới với lịch cũ. Mori hỏi lịch nhận phòng, An giữ chờ khách sạn trả lời.
- S023 · `71d53e5e-dc54-5a58-ba3e-b4ea7e10291a`. An xin gọi quầy và ở lại với Mori theo yêu cầu. Nhắc gọi cấp cứu nếu tình hình khẩn, không tự chẩn đoán hoặc chờ duyệt nội bộ.

Điểm nối đã đọc theo từng nhánh.

- S019 → S020. S019→S020 giữ sảnh khách sạn và giờ ăn 12 giờ. 11 giờ 45 là mốc nhóm tham quan quay về và hai nhóm gặp lại ở sảnh.
- S021 → S022. S021→S022 xác nhận xe tới bãi Tây, đoàn không đi sang bãi Đông. Giờ tới khách sạn mới là dự kiến.

## E06 — Sau chuyến

Phản hồi có ví dụ và việc đổi cho lần sau. S026 nói trực tiếp với lễ tân vì mục tiêu là gọi khách sạn hỏi thủ tục; S027 chuyển sang đúng người quên đồ. Nhân viên khách sạn chỉ giữ vật nghi là của người gọi và tự xác minh.

- S024 · `325dd7d3-8188-5830-a5a1-476eb884e076`. An cảm ơn hành động cụ thể, Mori nêu một việc để phân rõ vai lần sau, An nhận làm.
- S025 · `db10ae9f-b0ca-532a-b0e7-42703d111d92`. An hỏi hai phía, đào sâu đoạn nghỉ ngắn và kiểm lại đề xuất. Mori nói trải nghiệm của mình, không đại diện cả đoàn.
- S026 · `62ad64a0-c1ec-5a8f-a272-8d5d9fb29be2`. An nêu đồ, chỗ, ngày; kiểm thủ tục và tránh coi vật giống là đã tìm đúng của Mori.
- S027 · `ffa44028-8a92-52f3-bf57-81105cae6d08`. An nói mức đã biết, Mori tự mô tả đồ và thỏa thuận cách nhận để giảm chia sẻ thông tin riêng.
- S028 · `9c028cb8-a016-5c7c-9607-175349c985b8`. An đưa quan sát, đề xuất hai chỉnh sửa nhỏ, Kanda giao việc soạn mẫu và kiểm trước ngày gửi.

Điểm nối đã đọc theo từng nhánh.

- S026 → S027. S026→S027 Endo chưa xác nhận người sở hữu, chưa gửi đồ; An chỉ chuyển lời và đầu mối.

## E07 — Ranh giới vai trò

S029 chuyển câu hỏi chấm công về nhân sự và S030 làm rõ phạm vi An có thể xác nhận về lựa chọn hoạt động. S031 phân giờ xe và giờ tiệc theo đúng người điều phối.

- S029 · `a8b61240-0e80-5eb6-900c-5b28efc0a598`. An không đoán cách tính, chuyển hỏi nhân sự và chỉ phần có thể cung cấp để họ xác nhận đúng trường hợp.
- S030 · `990ad285-3b4e-5b98-9209-3833304e1112`. An tách quyền đi chuyến và quyền chọn từng mục, nói cụ thể người bỏ tham quan làm gì và không đánh đồng với chấm công.
- S031 · `21c00da3-bb17-567d-87ef-795fcd197119`. An nhìn ra hai mốc dễ lẫn, chốt nhãn, địa điểm và vai khi giờ xe thay đổi.

Điểm nối đã đọc theo từng nhánh.

- S029 → S030. S029→S030 Mori đã xin và nhận bản hướng dẫn, việc chấm công vẫn do nhân sự. Ở đây An xử lý cách đọc chương trình.

Đã đọc riêng lời Nhật và lời Việt, đối chiếu hai vai rồi đọc nối các cạnh đã ghi.

## Rà độc lập — 2026-11-18

Đã đọc 31 cảnh tiếng Nhật, tiếng Việt và từng cặp lượt. Đã kiểm 14 nhánh qua 7 sự kiện và đối chiếu S018 với S028 khi giữ chữ trên biển. Đã mở B21 bài 8 phần hỏi chuyến đi, B22 bài 8 hai mục hỏi và mốc nhớ chừng, B23 bài 8 biến thể đổi cơ sở, B05 Ch.5 về đặt phòng, B11 mục 9 về điểm tập trung và B12 mục 39 về giờ/địa điểm khi đổi lịch. B21–B23 chỉ hỗ trợ cách hỏi và nhận thông tin, không lấy áp lực tham gia trong ví dụ làm thông lệ.

- Đọc ngày 2026-11-18 [CAA, sổ tay cho cơ sở ăn uống](https://www.caa.go.jp/policies/policy/food_labeling/food_sanitation/allergy/assets/food_labeling_cms204_230324_03.pdf), mục 取組状況（注意点） về thông tin chưa rõ, dùng chung dầu/dụng cụ và quyết định của người có dị ứng. S008 yêu cầu riêng theo đồng ý của Sano và báo phần xác nhận được lẫn phần còn thiếu, không bảo đảm món cụ thể.
- Đọc ngày 2026-11-18 [FDMA về 119](https://www.fdma.go.jp/mission/enrichment/kyukyumusen_kinkyutuhou/119.html), mục 119番緊急通報 và quy trình hỏi thông tin điều phối. S004 và S023 tách đầu mối nội bộ/lễ tân với gọi 119 ngay khi cần xe cấp cứu ở Nhật. Tình huống này không thực hiện cuộc gọi hoặc đưa ra chẩn đoán.
- Mục 3 của hướng dẫn MHLW xác định giờ làm theo hoàn cảnh cụ thể và việc người lao động có đặt dưới sự chỉ đạo của người sử dụng lao động hay không. S029 chỉ hướng tới nhân sự với thông tin chuyến đi. Đã đọc ngày 2026-11-18 [hướng dẫn giờ làm của MHLW](https://www.startup-roudou.mhlw.go.jp/pdf/guidelines.pdf).

Rà các mốc chậm nhất và giờ dự kiến ở E02–E05. Phương án 18 khách lưu trú và ngày đầu không lưu trú thuộc tình huống riêng. Ở E03 chỉ chốt đổi phòng sau phê duyệt và đồng ý của cả hai khách. Ở E06 khách sạn mới tìm thấy túi giống mô tả, Mori tiếp tục xác nhận trực tiếp trước khi chọn cách nhận.
