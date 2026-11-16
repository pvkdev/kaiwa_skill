# S-023 — Konbini và dịch vụ nhanh hằng ngày

## Mục tiêu và nguồn đã đọc

- Đọc toàn bộ brief V10 của S-023: 20 UID, bốn sự kiện E01–E04; các đường S003→S004, S009→S010, S013→S014 và S017→S018→S019. Mục tiêu: tìm và chọn món; trả lời câu hỏi của thu ngân; hỏi dịch vụ; kiểm giao dịch khi trở lại.
- Tra `catalog27/BOOK_GUIDE.md`, `manifest.json` và toàn bộ `source_index.jsonl` cho 27 sách bằng `コンビニ`, `レジ`, `スーパー`, `袋`, `温め`, `荷物`, `値段`, `買い物`, `試着`, `案内` cùng từ khóa chức năng Việt. B05 sát cảnh nhất; B08 có đoạn siêu thị/konbini, B01 có thanh toán, B14 có hội thoại mua hàng. Chọn B05 để đọc sâu; không gán câu AI cho sách.
- Đã đọc B05, *すぐに使える 接客日本語会話大特訓［英語版］決まり文句700*, `kaiwa_skill/knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/04-ch3-hanbaiten.md` dòng 615–642 về vị trí trên kệ, giá và hết hàng; `chapters/05-ch4-konbini.md` dòng 9–35 về túi, tiền thừa, hóa đơn; dòng 93–118 về hâm và đũa; dòng 120–147 về hỏi dịch vụ gửi hàng. Đây là sách dạy lời quầy; người học được biên soạn lời đáp riêng.
- Đã đọc bài chuyên đề ngay trước S-023 `kaiwa_skill/planning/v10/stages/sj-so-06/lesson.md` và tra `practice.json` theo UID. Cách `お願いします` được dùng khi chốt chọn/nhờ nhân viên; chỉ các cảnh có lời đó mới ghi `sj-so-06-b07-85`.
- [FamilyMart 店頭受取サービス](https://www.family.co.jp/services/delivery/shop_receive.html?0=uketori), đọc 2026-11-16: dịch vụ nhận đơn hàng đủ điều kiện tại FamilyMart, không suy ra mọi đơn hoặc mọi konbini nhận được.
- [FamilyMart FAQ: 店頭受取サービスの受取方法](https://www.inq.family.co.jp/familymart/QA_Customer/web/knowledge9174.html), đọc 2026-11-16: phương thức nhận tùy đơn, có mã vạch trên điện thoại hoặc máy đa năng. Cảnh S011–S014 chỉ dùng thông báo với mã vạch; nhân viên vẫn kiểm đơn cụ thể.

## Quyết định biên tập theo sự kiện

- **E01:** Người học hỏi đúng vị trí/giá/vị thay thế, rồi chọn món. S003 để việc kiểm nhãn còn mở; S004 trả lời rõ 300 yên cho *một* bánh bên phải. Giá 300/400 yên là ví dụ của Midori hư cấu.
- **E02:** Thu ngân hỏi hâm, túi, đồ ăn kèm. S009 dừng trước khi hâm nhầm mì lạnh; S010 chỉ hâm cơm hộp. Tiền 1.000, 380 và 620 yên ở S016 là phép tính của giao dịch hư cấu, không phải giá niêm yết thực.
- **E03:** FamilyMart chỉ được dùng ở nhánh nhận đơn đã chọn địa điểm này. S013 chưa có xác nhận trong dữ liệu cửa hàng, không kết luận kiện bị thất lạc; S014 quay lại cùng thông báo, mã vạch và tên Nguyễn An. S015 dùng câu hỏi về dịch vụ, không dạy thao tác máy.
- **E04:** S017 phát hiện món thiếu và đưa hóa đơn; S018 nhân viên mới kiểm túi/quầy; S019 vẫn không tìm ra và chuyển hỏi người phụ trách, không tự hứa bồi hoàn. S020 là tình huống riêng sau khi hai bên đã xác nhận đủ hàng.

## Nhật ký tự rà

Đã đọc JA liền mạch và VI độc lập cho từng cảnh, kiểm người nói theo `speaker_id` và đọc nối các đường `continues_from`. Mỗi cảnh có hai vai và mỗi vai nói thật. Tất cả lượt là `original_extension`; B05 và các trang FamilyMart chỉ làm căn cứ cho ngữ cảnh/cách hỏi. Đầu việc cho root: kiểm biên tập độc lập và preview hai vai, đặc biệt S011–S014 và S017–S019.
