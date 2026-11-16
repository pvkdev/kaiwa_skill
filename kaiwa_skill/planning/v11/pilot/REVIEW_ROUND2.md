# V11 · Pilot vòng hai

Đã nghiệm thu lại 71 hội thoại, 406 lượt Nhật–Việt bằng skill V11 đã sửa. Mỗi cấp có một worker sol/high rà đủ tình huống. Điều phối viên đọc lại bản Nhật–Việt theo từng mục tiêu V10 và kiểm bản xuất. Chủ dự án có thể mở ba liên kết dưới đây để review.

## Mở nội dung để review

- [S-021 · Nhận chỉ thị & hỏi lại](ROADMAP.html#stage=af5b5945-8ab2-5cab-9544-56127ff8e8fd) có 15 cảnh, 67 lượt. Cùng chuỗi chuẩn bị tài liệu, người học hỏi hạn, nghe lại số lượng, xác nhận phần được dùng từ mẫu cũ, tìm người quyết định, xin dùng giấy thay thế và sửa bộ thiếu trang. [Hồ sơ Sơ](S-021/RESEARCH.md)
- [T-027 · Nhờ tư vấn & từ chối khéo tại cửa hàng](ROADMAP.html#stage=a458f686-f123-5cdd-a5c8-73cfe6855a32) có 36 cảnh, 212 lượt. Bao gồm nêu ngân sách, so máy, hiểu khác nhau giữa độ bền và bảo hành, từ chối mua thêm, xin giữ hàng, hỏi nhân viên phụ trách và chọn vật liệu đan cho người mới. [Hồ sơ Trung](T-027/RESEARCH.md)
- [H-020 · Họp, đề xuất & phản biện](ROADMAP.html#stage=cba953ce-d3d0-5e71-acb8-419cd0e708a1) có 20 cảnh, 127 lượt. Luyện hỏi phạm vi quyết định, phân biệt số đã kiểm và số ước tính, phản biện mà giữ quan hệ, giảm phạm vi đề xuất, xin bàn lại và báo tác động mới. [Hồ sơ Thượng](H-020/RESEARCH.md)

Các liên kết pilot cũng nằm ở đầu HTML. Toàn bộ preview hiện có 126 hội thoại, 720 lượt nói sau khi ghép hai vòng.

## Các cảnh nên mở trước trong bản sửa

- **S-021, cảnh 05 và 11.** Khi nhân viên hỏi nghĩa của 差し替える, bản Việt giữ chính từ đang hỏi. Đồng nghiệp giải thích ở lượt sau. Khi bị từ chối dùng giấy thay thế, nhân viên tự hỏi mình có thể làm gì trong lúc chờ.
- **T-027, cảnh 10, 29 và 34.** Hai mẫu máy đều có giá *không quá* 25.000 yên. Khi khách hoãn mua, nhân viên nhận hỏi lại thông tin phụ kiện và hẹn trả lời khi khách quay lại. Cảnh này còn bốn lượt. Ở tiệm đan, khách chủ động hỏi nên mua gì trước với chiếc kim đang có và ngân sách 3.000 yên.
- **H-020, cảnh 07–08 và 17–18.** Cảnh 07 xác lập rằng chưa ai hỏi những người sẽ trực tiếp làm. Ở cảnh 08, Sato đề nghị chờ hỏi Tổng vụ rồi mới quyết và nhận phần liên hệ. Ở cảnh 18, người học nghe rõ việc chạy thử vẫn chờ quyết định.
- Khi rà các cảnh liên quan, nhóm cũng làm rõ mục đích đan khăn ở T-027 cảnh 36. Ở H-020 cảnh 11, loại câu hỏi về cấp đồ dùng mới là một phương án đang cân nhắc. Sang cảnh 12, chính Sato mới thu hẹp phạm vi đề xuất.

Biên tập viên mở riêng từng cảnh để tìm lượt nói thực hiện mục tiêu, nghe lời đáp từ vị trí người đối diện và so lại từ ngữ có thể đổi quyết định. Hồ sơ từng chặng lưu nhận xét theo UID cùng dấu vân tay của bản cuối. [S-021](S-021/status.json) · [T-027](T-027/status.json) · [H-020](H-020/status.json)

## Lần nghiệm thu trước tại `944e8f3a`

- Sơ có cảnh nghe nhầm số nhưng ban đầu mô tả đọc ghi chú mờ. Đã sửa bối cảnh thành nghe không rõ rồi hỏi hai con số cụ thể. Câu in thử một bộ được diễn đạt rõ trong cả Nhật và Việt.
- Trung có ba cảnh bị đảo speaker_id của khách và nhân viên. Đã sửa, đọc lại vai của từng lượt trong cả 36 cảnh, và thêm vào skill hướng dẫn gán vai theo người nói khi đóng gói bằng script. Hai lượt liên tiếp cùng người vẫn có thể mang cùng speaker_id. Đã sửa cách xưng hô theo đúng hai nhân vật, bỏ mã cảnh khỏi bối cảnh hiển thị, trả lời cụ thể cho câu hỏi so độ ồn và kiểm độ tương thích của sợi với kim. Nhân viên giữ thông tin đã biết về kim ở cảnh tiếp nối.
- Thượng có hai cảnh hiểu nhầm trái với điều nhân vật vừa xác nhận. Đã thêm nguồn thông tin mới gây hiểu lệch và để người học trực tiếp hỏi chủ trì. Cảnh xin họp lại có lời đề nghị thật và câu trả lời có điều kiện. Các cảnh báo ảnh hưởng nêu rõ hai bộ phận hướng dẫn dùng hai kênh nộp khác nhau.

Ở lần nghiệm thu này, ba chặng có 408 lượt. RESEARCH.md của từng chặng lưu phần nghiên cứu và nhật ký biên tập.

## Nguồn và các dữ kiện minh họa

Nguồn hội thoại được tra từ chỉ mục 27 sách rồi đọc những đoạn phù hợp. Hồ sơ quản trị ghi mã, tên sách, vị trí và điều đã vận dụng; lời viết mới có nhãn original_extension. Cách xác nhận nhiệm vụ lấy chất liệu từ sách giao tiếp công sở, cách tư vấn và từ chối từ sách tiếp khách cùng cụm từ hội thoại, còn mạch đề xuất và phản biện tham khảo role-play business và Nama Chūkei. Các chặng cũng tham khảo chuyên đề gần trước khi phù hợp.

Thông số máy, giá, bảo hành, giờ giữ hàng và chỉ dẫn của cửa hàng là dữ kiện minh họa cho cửa hàng hư cấu. Đối với cảnh đan, nguyên lý thử đan và đo số mũi được đối chiếu hướng dẫn chính hãng. Cỡ kim và nhãn sợi cụ thể trong cảnh vẫn là giả định. [Hướng dẫn Clover về thử đan và đo gauge](https://clover.co.jp/seihin/amimonoyouhin.html)

## Kiểm dữ liệu và preview

Cả sáu chặng đã qua validator. Đã kiểm 126 tình huống đúng UID và thứ tự, 720 ID lượt duy nhất, hai trường Nhật–Việt và giới tính của từng vai. Đối chiếu từng hội thoại với learner.json và JSON nhúng trong HTML. Kiểm bản xuất xác nhận ba pilot vòng trước và các dữ liệu V10 ngoài hội thoại mới còn khớp mốc đối chiếu.

Chrome headless đã mở đủ sáu liên kết pilot ở 1280 × 800 và 390 × 844, mở các nhóm thực hành rồi so từng bối cảnh, câu Nhật, bản Việt và nhãn vai/giọng trong DOM với JSON. Hai file ROADMAP.html và docs/index.html có cùng nội dung.

Lượt này kết thúc ở ba pilot mới. Các checkpoint ghi awaiting_user_review và bulk_run_authorized=false.
