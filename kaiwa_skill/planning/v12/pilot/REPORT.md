# Sáu pilot từ vựng theo chủ đề · V12.0

Đã soạn mới 534 mục trong 25 nhóm. S-011, T-044 và H-004 được chạy lại từ đầu. S-024, T-008 và H-020 là ba chủ đề bổ sung. Quy tắc chọn từ theo chủ đề lấy từ bản V12.0 ở `e3fdfb39`. [Mở sáu pilot](ROADMAP.html).

| Chặng | Chủ đề | Nhóm | Mục | Từ hội thoại hoặc shadowing | Mở rộng theo chủ đề | Thời gian worker ghi nhận |
|---|---|---:|---:|---:|---:|---|
| S-011 | Tàu điện & xe buýt | 3 | 68 | 38 | 30 | 4 phút 37 giây |
| S-024 | Đi siêu thị và lo bữa ăn hằng ngày | 4 | 96 | 59 | 37 | 5 phút 53 giây |
| T-044 | Gửi bưu kiện cá nhân và hỏi hàng quốc tế | 5 | 100 | 48 | 52 | 5 phút 12 giây |
| T-008 | An ủi, đồng cảm & chia buồn | 5 | 84 | 25 | 59 | 4 phút 35 giây |
| H-004 | Kính ngữ đối ngoại & chuyển lời xã giao | 4 | 91 | 37 | 54 | 4 phút 50 giây |
| H-020 | Họp: tham gia, đề xuất & phản biện | 4 | 95 | 46 | 49 | 3 phút 03 giây |
| **Tổng** | | **25** | **534** | **253** | **281** | |

Thời gian là thời gian thực từng worker ghi nhận cho biên soạn và rà, các worker chạy song song. Mỗi chặng hiển thị một bài với bảng riêng cho từng nhóm. Bốn cột học viên gồm tiếng Nhật, cách đọc, Hán Việt và nghĩa Việt. Metadata và nguồn nằm ở bản biên tập.

## Nhận xét sau khi đọc sáu bài

- **Sơ.** Chặng siêu thị có thể dùng để tự lên thực đơn và hỏi mua lượng vừa đủ. Những mục như 豆腐, 豚肉, りんご và 炒める cho phép thay nguyên liệu và cách nấu. Chặng đi lại tập trung hơn, với các cặp như 前払い／後払い và 乗る／降りる.
- **Trung.** Hai bài có nhu cầu giao tiếp khác nhau. Gửi bưu kiện cần nhận ra tên dịch vụ và trạng thái vận chuyển. Chia buồn cần biết chọn cách nói theo quan hệ, biết khi nào nên lắng nghe hoặc đề nghị giúp.
- **Thượng.** 了承／承認／合意 giúp phân biệt mức cam kết khi chuyển lời đối tác. Trong họp, 根拠／仮説 và 暫定値／確定値 giúp người học chất vấn độ chắc chắn của một đề xuất.

**Điểm cần lưu ý nếu mở rộng.** Validator V12.0 nhận nhầm động từ nguyên dạng 励ます vì phần cuối trùng chuỗi ます. T-008 dùng danh từ 励まし (lời động viên). Đây là giới hạn của validator gốc.

## Nghiệm thu

Sáu checkpoint đã khớp hash skill, nguồn V11, bản thảo và nhóm đã duyệt. Toàn bộ 25 node xuất qua schema Exchange. Đã mở lần lượt sáu bài trong Chrome ở chiều rộng 360 và 1.280 px và so khớp đủ 534 dòng, bốn cột với JSON biên tập. Dữ liệu lộ trình ngoài phần pilot khớp V11.

## Chi tiết theo chặng

### S-011 · Tàu điện & xe buýt

Tuyến tàu, hướng và ga đổi (22); Bến xe buýt, bến xuống và cách trả tiền (21); Sân ga, lối hỗ trợ và hỏi lại nhân viên (25).

Mức biên tập ước lượng: N5 (19), N4 (17), N3 (16), N2 (3), none (13).

Mục vượt dải cấp: 方面, 終点, 時刻表, 間違える, 戻る, 運賃, 現金, 両替する, 過ぎる, 通る, 乗り越す, 改札, 窓口, 通路, 突き当たり, 車いす, 段差, つらい, 確認する. Lý do tiếp nhận nằm trong từng mục.

Các nhắc nhở của công cụ đã rà: 乗る: level_hint N5, vocabulary book lists N3 · 降りる: level_hint N5, vocabulary book lists N3.

[Từ vựng](S-011/vocabulary.json) · [Checkpoint](S-011/status.json) · [Gói Exchange](S-011/exchange.json)

### S-024 · Đi siêu thị và lo bữa ăn hằng ngày

Nguyên liệu cho bữa ăn (25); Hỏi lượng, chia phần và chuẩn bị món (21); Hạn dùng, giữ lạnh và lựa chọn thay (25); Giá kệ, hóa đơn và hàng thiếu (25).

Mức biên tập ước lượng: N5 (23), N4 (38), N3 (17), N2 (3), none (15).

Mục vượt dải cấp: 食材, 分ける, 焼く, 煮る, 炒める, 表示, 避ける, 含む, 別, 種類, 新鮮, 傷む, 値札, 割引, レシート, 商品, 足りる, 確認する, 担当者, 交換する. Lý do tiếp nhận nằm trong từng mục.

Các nhắc nhở của công cụ đã rà: パック: level_hint N4, vocabulary book lists N1 · 生: level_hint N4, vocabulary book lists N3 · アレルギー: level_hint N4, vocabulary book lists N1 · レジ: level_hint N4, vocabulary book lists N3.

[Từ vựng](S-024/vocabulary.json) · [Checkpoint](S-024/status.json) · [Gói Exchange](S-024/exchange.json)

### T-044 · Gửi bưu kiện cá nhân và hỏi hàng quốc tế

Nội dung, nơi đến và đóng gói kiện quốc tế (22); Dịch vụ gửi, kích thước, cước và thời gian (21); Tên, địa chỉ và nội dung trên phiếu gửi (18); Theo dõi, phát lại và hoàn trả (20); Hàng thiếu, hư hỏng, chứng cứ và nơi liên hệ (19).

Mức biên tập ước lượng: N3 (25), N2 (57), N1 (4), none (14).

Mục vượt dải cấp: 目安, 追跡, 発送, 補償. Lý do tiếp nhận nằm trong từng mục.

[Từ vựng](T-044/vocabulary.json) · [Checkpoint](T-044/status.json) · [Gói Exchange](T-044/exchange.json)

### T-008 · An ủi, đồng cảm & chia buồn

Hỏi người kia muốn kể hay cần yên tĩnh (16); Phản hồi khi nghe chuyện thất bại hoặc mất mát (20); Chia buồn theo mức độ thân thiết (16); Đề nghị giúp việc cụ thể và tôn trọng lựa chọn (18); Hỏi thăm sau vài ngày và để người kia tự chọn khi trả lời (14).

Mức biên tập ước lượng: N4 (1), N3 (27), N2 (49), N1 (4), none (3).

Mục vượt dải cấp: 打ち明ける, 決めつける, 差し入れ, 優先する. Lý do tiếp nhận nằm trong từng mục.

[Từ vựng](T-008/vocabulary.json) · [Checkpoint](T-008/status.json) · [Gói Exchange](T-008/exchange.json)

### H-004 · Kính ngữ đối ngoại & chuyển lời xã giao

Xưng hô, chức danh và đón khách (23); Nhận lời nhắn, chuyển lời và hẹn phản hồi (24); Mức chắc chắn, xem xét và phê duyệt (22); Đính chính tên, chức danh và đầu mối (22).

Mức biên tập ước lượng: N3 (9), N2 (57), N1 (25).

[Từ vựng](H-004/vocabulary.json) · [Checkpoint](H-004/status.json) · [Gói Exchange](H-004/exchange.json)

### H-020 · Họp: tham gia, đề xuất & phản biện

Mục tiêu họp, phạm vi quyết định và người duyệt (23); Dữ kiện, xuất xứ số liệu, giả định và đề xuất (24); Rủi ro, phạm vi thử và tiêu chí thành công (23); Phản biện, giữ quan hệ và theo dõi sau họp (25).

Mức biên tập ước lượng: N3 (1), N2 (43), N1 (51).

[Từ vựng](H-020/vocabulary.json) · [Checkpoint](H-020/status.json) · [Gói Exchange](H-020/exchange.json)
