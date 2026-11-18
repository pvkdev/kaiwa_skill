# T-124 — nhật ký biên soạn

Tra catalog27 với 急病人・119番・反応・停電・避難・落とし物 và đọc B05 chương xử lý khẩn. Đọc chuyên đề Tiếp nhận sự cố và báo đúng người, đọc các ví dụ practice về nhận tin sự cố, xác nhận yêu cầu và gọi lại; practice không gắn UID của chặng này. Cảnh cấp cứu nói điều tận mắt thấy, báo 119 ngay khi mất đáp ứng hoặc có khó thở rõ, trả lời điều phối, không tập chẩn đoán hay thao tác sơ cứu. Tên vị trí nội bộ, giờ và quy trình phục vụ thuộc cơ sở giả định.

## Nguồn đã đọc

- B05 — すぐに使える 接客日本語会話大特訓［英語版］決まり文句700, `kaiwa_skill/knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/09-ch8-kinkyu.md`, dòng 53–61. Dùng câu ngắn báo điều thấy và chuyển sang gọi cấp cứu. Không dùng lời chỉ dẫn sơ cứu từ sách.
- B05 — すぐに使える 接客日本語会話大特訓［英語版］決まり文句700, `kaiwa_skill/knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/09-ch8-kinkyu.md`, dòng 133–143. Đưa vị trí và hướng di chuyển cụ thể khi báo cho khách.
- B05 — すぐに使える 接客日本語会話大特訓［英語版］決まり文句700, `kaiwa_skill/knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/09-ch8-kinkyu.md`, dòng 161–172. Hỏi đặc điểm và vị trí, tách chưa có đồ giống và đã xác minh đúng món.
- Đọc ngày 2026-11-18. 消防庁 xác nhận 119 dùng khi cần xe cấp cứu hoặc cứu hỏa; nơi đến, tên và liên lạc người gọi là thông tin điều phối hỏi. Khi chưa biết địa chỉ, có thể nêu mốc, nhân viên trả lời câu hỏi điều phối. [総務省消防庁 119番緊急通報](https://www.fdma.go.jp/mission/enrichment/kyukyumusen_kinkyutuhou/119.html)
- Đọc ngày 2026-11-18. Đọc mục 救急車の呼び方, nói cứu cấp, địa chỉ, ai và tình trạng, ý thức/hô hấp trong phần quan sát được, tên và số có thể gọi lại. Dùng tín hiệu quan sát và báo người hỗ trợ, không suy diễn chẩn đoán. [総務省消防庁 救急車利用マニュアル 日本語版](https://www.fdma.go.jp/publication/portal/items/portal002_japanese.pdf)
- Đọc ngày 2026-11-18. Mất điện bên trong một tòa nhà có thể không hiện như mất điện khu vực; có nhiều khả năng từ đường dây đến thiết bị trong tòa nhà. Không suy nguyên nhân từ nơi có đèn tắt. Cơ sở ở Tokyo trong bài tự liên hệ kỹ thuật tòa nhà. [東京電力パワーグリッド 停電復旧情報](https://www.tepco.co.jp/pg/teiden-fukkyu/index-j.html)
- Đọc ngày 2026-11-18. NPA hướng dẫn đưa đồ nhặt trong cơ sở có quản lý cho nhân viên/quản lý cơ sở. Cảnh giả định đồ còn được quản lý tại chỗ, việc đối chiếu khi trả do đầu mối của cơ sở; không đưa thời hạn hoặc quyền pháp lý. [警察庁 施設で落とし物を拾った場合](https://www.npa.go.jp/bureau/soumu/ishitsubutsu/otoshimono/pickedup-institution.html)

## E01 — Khách hoặc đồng nghiệp cần hỗ trợ khẩn

- S001 · `ac4c65be-3f32-5c1a-98d6-1f718e205159`. Nhân viên u01/u03 nói địa điểm, gọi không phản hồi, chưa rõ thở. Trưởng ca u04 nhận gọi 119 ngay.
- S002 · `27fd2b13-7ec9-55f3-a534-1609c14d624b`. Nhân viên u01/u03 nêu thêm người, vị trí riêng và còn trả lời. Trưởng ca chuyển thông tin cho điều phối, không suy hai ca cùng nguyên nhân.
- S003 · `5d3f2d3f-ea4f-59f7-8eb2-b1c3ff5c288d`. Nhân viên u01 nêu tình trạng và hỏi ai gọi; trưởng ca u02 nhận gọi 119 ngay với địa chỉ và vị trí, u04 nhận chuyển tình trạng.
- S004 · `bae6eb1d-3997-517c-8846-5c3195e86b53`. Nhân viên u02/u04 đưa thời điểm khoảng 15:10, lời khách và phản ứng quan sát được; không đoán nguyên nhân hoặc tiền sử.

Điểm nối đã đọc theo từng nhánh.

- S001 → S002. Trưởng ca đã nhận gọi 119 ở quầy dịch vụ phía bắc. Thêm người còn trả lời bên ghế phía nam, báo hai vị trí riêng.
- S003 → S004. Trưởng ca đã gọi 119 cho khách ở quầy tầng hai. Nhân viên trực tiếp quan sát bàn giao cho đội đã tới.

## E02 — Sự cố dịch vụ tại chỗ

- S005 · `9ccde47f-5cde-56a7-bf95-9bf268f452bd`. Nhân viên u01/u03 chỉ hai máy và đèn ở phía đông, phía tây còn hoạt động. Trưởng ca giao nhân viên gọi kỹ thuật.
- S006 · `29e73d0d-0c74-52a1-b064-cf3abfc8f83e`. Nhân viên u02/u04 nhắc phạm vi phía đông, hỏi xử lý hồ sơ dở. Trưởng ca giao chuyển khách mới sang phía tây.
- S007 · `426b9eec-23d6-5e88-a8d4-a3c98d1031a4`. Nhân viên u01/u03 nhận báo nhóm chờ và chuẩn bị mốc cập nhật kỹ thuật, chưa hứa giờ mở quầy.
- S008 · `b7db8fb3-f0d1-5b95-ad49-14ba8f87499b`. Nhân viên u01/u03 phân biệt giờ kỹ thuật tới với giờ mở lại; khách chưa làm thủ tục nên được sang phía tây.

Điểm nối đã đọc theo từng nhánh.

- S005 → S006. Điện tắt ở quầy phía đông, xử lý chờ; chỉ tạm dừng nhận khách mới tại quầy đó, phía tây còn hoạt động.
- S007 → S008. Nhân viên được giao báo nhóm đang đợi phía đông; có mốc 17:30 kỹ thuật tới, vẫn chưa có giờ hoạt động lại.

## E03 — Đồ khách bỏ quên

- S009 · `20757018-d028-57be-a89d-7ccd564e9f40`. Nhân viên u02/u04 lấy bình xanh đậm có chữ M khắc dưới đáy, vị trí ghế bên cửa tây, nhận kiểm.
- S010 · `916d4875-3b54-5ddc-ae01-5f820228af5a`. Nhân viên u01/u03 nói chưa có trong ghi nhận, nhận kiểm ghế và hỏi người phụ trách, gọi sớm nhất có thể và chậm nhất 16 giờ.
- S011 · `33695ace-965a-5a53-a2ef-989e048e9f81`. Nhân viên u01/u03 đối chiếu đáy bình và nắp, giữ bình khác chủ, quay lại kiểm khu ghế.
- S012 · `ed2ef8d1-5ba3-5c55-9afb-8fcb8656dba6`. Nhân viên u01/u03 báo bình trùng dấu hiệu, nhắc nơi gặp và việc vẫn cần đối chiếu trực tiếp trước khi giao.

Điểm nối đã đọc theo từng nhánh.

- S009 → S010. Bình giữ nhiệt xanh đậm có chữ khắc M, thấy lần cuối ghế cạnh cửa tây; chưa có trong sổ, tiếp tục tìm tới 16 giờ.
- S009 → S011. Cùng đồ màu xanh, nhánh riêng tìm thấy một bình giống mà thiếu chữ M, giữ lại và kiểm thêm.
- S010 → S012. Đồ tìm được đúng chữ M và chỗ ghế cửa tây trước 16 giờ. Báo đầu mối và chưa giao vật khi khách chưa tới.

## E04 — Sau sự cố

- S013 · `d411db4d-c4e3-5147-a293-2b1e83701298`. Nhân viên u02/u04 ghi 14:10 hai máy và đèn tắt, báo trưởng ca rồi gọi kỹ thuật 14:12. Ca còn kiểm.
- S014 · `3850bb07-7577-5f82-946b-811d29ba9c74`. Nhân viên u02/u04 phân biệt quan sát với kết luận, kỹ thuật mới tiếp nhận. Trưởng ca giữ ghi chép ở mức đã quan sát.
- S015 · `6dd0190d-3a69-5094-9400-561ba28eba49`. Nhân viên u01/u03 hỏi phạm vi, xác nhận hai nhóm 15:30 và 16:00, nhận báo tình trạng và hỏi mong muốn đổi lịch.
- S016 · `d0a8560c-0372-526b-8fcc-6b68bc665593`. Nhân viên u01/u02 giữ đúng ai đã nhận, ai chưa. U04 nhận kiểm chỗ sáng mai và thử gọi lại chậm nhất 17 giờ.

Điểm nối đã đọc theo từng nhánh.

- S013 → S014. Giữ mốc 14:10/14:12 và hai thiết bị đã thấy tắt; lời kỹ thuật tiếp nhận không phải kết luận nguyên nhân.
- S015 → S016. A nhận gọi hai nhóm đặt lịch, một trả lời muốn dời, một chưa nghe máy. Mốc kiểm chỗ và gọi lại là 17 giờ.

Đã đọc Nhật và Việt riêng, thử đổi vai và đọc nối từng cạnh, trở về điểm rẽ trước khi sang nhánh khác. Chờ rà độc lập.

## Rà độc lập ngày 2026-11-18

Đã đọc ba trích đoạn B05 và đối chiếu bốn nguồn chính thức. FDMA hướng dẫn gọi 119 ngay khi cần cấp cứu, nói địa chỉ, vị trí, số người và điều quan sát được, rồi trả lời và thực hiện theo điều phối. S001 và S003 chuyển tiếp hướng dẫn tới nhân viên ở cạnh khách, không chờ chẩn đoán nội bộ. TEPCO nêu sự cố trong tòa nhà có thể không xuất hiện trên bản đồ mất điện. S013–S014 chỉ ghi đèn và máy tắt, chưa kết luận nguyên nhân. NPA hướng dẫn giao đồ nhặt được cho cơ sở quản lý. Việc gọi lại và trả bình ở quầy thuộc tình huống của cơ sở giả định. [FDMA — 119](https://www.fdma.go.jp/mission/enrichment/kyukyumusen_kinkyutuhou/119.html) · [FDMA — Sổ tay sử dụng xe cấp cứu](https://www.fdma.go.jp/publication/portal/items/portal002_japanese.pdf) · [FDMA — Hướng dẫn từ điều phối](https://www.fdma.go.jp/relocation/kyukyukikaku/oukyu/05kobetsu/01/05_01_12.html) · [TEPCO](https://www.tepco.co.jp/pg/teiden-fukkyu/index-j.html) · [NPA](https://www.npa.go.jp/bureau/soumu/ishitsubutsu/otoshimono/pickedup-institution.html)
