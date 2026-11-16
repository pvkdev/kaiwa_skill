# S-012 — nghiên cứu và tự rà

Ngày đọc: 2026-11-16. Đã chạy dialogue.py và theo đủ 25 UID/tình huống V10 theo thứ tự. Tất cả lời thoại là sáng tác mới (`original_extension`); nguồn sách ở cấp cảnh chỉ là căn cứ ngữ dụng. Đã tra BOOK_GUIDE, manifest và source_index trong phạm vi B01–B27 theo chức năng nói, quan hệ và các cụm Nhật; đọc sâu đúng các dải dưới đây. Không tuyên bố đã đọc toàn văn 27 sách.

## Mạch, chuyên đề và giới hạn dữ kiện

Đã đọc trọn `sj-so-03/lesson.md`, đối chiếu practice về hỏi hướng và mốc. Catalog 27 tra theo 定期券, PASMO, 改札, 乗り換え, 残額, 駅員; B08 và B27 được đọc ở dải ghi dưới. Tokyo Metro/PASMO được kiểm trực tiếp ngày 2026-11-16: [vé tháng Tokyo Metro](https://www.tokyometro.jp/lang_en/ticket/types/pass/commuter/index.html) ghi tuyến/phạm vi và đi quá phạm vi trả phần thêm, thay tuyến do quầy xử lý theo loại vé/hạn; [PASMO Tokyo Metro](https://www.tokyometro.jp/en/ticket/pasmo/index.html) phân biệt thẻ có tên/vô danh khi mất; [quy tắc PASMO](https://www.pasmo.co.jp/en/condition/) đòi giấy tờ chứng minh chủ thẻ; [lịch sử PASMO](https://www.pasmo.co.jp/ic-card/use/history/) cho xem/in ngày/chặng/số dư. E01 và E04 dùng Asakusa–Ginza–Shibuya trên tuyến Ginza; công việc và ngày bắt đầu giả định. E02 S009→S010 dùng khoản 190 yên **hiển thị trong lượt minh họa**, không khẳng định đây là giá thật của chặng Asakusa–Shibuya hay hiện hành. E03 tách quên vé, mất thẻ có tên, mất thẻ vô danh; không gộp quyền cấp lại. E05 S021–S025 giữ hai lượt thứ Ba/thứ Năm; nguyên nhân trừ tiền vẫn đang kiểm, không gán lỗi cho người đi hoặc nhà vận hành. Mọi trường hợp quầy báo thời hạn là thỏa thuận trong cảnh, không phải SLA công bố.

## Đoạn sách đã đọc

- train: どんどん話せる！日本語会話フレーズ大特訓 必須700, `kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md` dòng 8–35. Hỏi tàu, ga, hướng và đường ray trong lời nói ngắn.
- station: 聞いて覚える話し方 日本語生中継 初中級編２, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/09-bai-08-eki-de.md` dòng 19–85. Khách, nhân viên ga và kết quả sự cố vé; viết mới đối đáp Sơ.

## Tự rà từng cảnh

- S001 `3ffecf69-43db-54d6-88fb-0d632a46e7f9` (routine): Nêu chặng đi làm, nhân viên xác nhận ga đầu/cuối trước chọn vé.
- S002 `cdc2018d-d9e2-5f73-bbcf-cd60eb4ee8f1` (routine): Nêu ngày bắt đầu và phạm vi Asakusa–Ginza, nhân viên kiểm.
- S003 `1e2167b7-37e6-593b-a529-1d4eda6086db` (conditional): Nơi làm đổi Shibuya trước khi mua, người học hỏi tuyến mới.
- S004 `ca78b147-b4b7-5d6b-aa71-38d8d80bba20` (pending): Chưa biết ngày, người học hỏi mua sau và được chốt việc cần mang thông tin.
- S005 `c5e410e1-b68c-5a9d-bff8-7dc67fc98226` (resolved, nối S003): Tiếp S003, nhắc Asakusa–Shibuya và thứ Hai trước khi trả.
- S006 `ec177d85-3820-5f52-aeb9-9dbf6a3f2aaf` (routine): Cổng vào không mở, đưa thẻ cho nhân viên kiểm, không tự chẩn đoán.
- S007 `d593c2c2-2eed-5fcb-9526-971326c66011` (routine): Cổng ra không mở, nêu ga lên và ga muốn xuống để kiểm.
- S008 `becde68f-4a8c-5991-9c5c-f178d2bb262e` (misunderstanding): Nhân viên đoán thiếu tiền, người học báo vừa nạp và xin kiểm lịch sử.
- S009 `5ebc159b-d5aa-56d6-9764-a23375b77165` (alternative): Ngoài phạm vi Asakusa–Ginza, hỏi khoản thêm và nhận số trên màn hình minh họa.
- S010 `787b0554-3eab-5945-b258-3fb32d88288c` (resolved, nối S009): Sau S009 cổng đã xử lý, người học hỏi cách xem phạm vi cũ.
- S011 `39e61011-56c3-56b6-a91c-55217d1dd4c0` (routine): Quên vé tháng không được tự đi miễn phí; chọn mua vé cho hôm nay.
- S012 `545cf95b-894d-5ea0-a7f2-9c3c1608e36e` (routine): Mất PASMO, chưa biết loại, hỏi cách kiểm tại quầy.
- S013 `ce504d6d-3af3-566d-9110-abc7b7174f5c` (conditional): Thẻ có tên, hỏi giấy tờ chứng minh người dùng để làm thủ tục.
- S014 `a38cdd5f-2feb-577e-a2b9-e10ee1852fbf` (declined): Thẻ vô danh không cấp lại, người học chọn vé lẻ hôm nay.
- S015 `dedda12e-effb-5512-b3de-0ffb5330b5ea` (follow_up): Quay lại có giấy tờ, sau xác minh nhận số dư giả định 1.000 yên và xin cấp lại.
- S016 `2ab3414e-d810-50e9-880b-03b46f7ab800` (routine): Đổi nơi làm tới Shibuya, báo vé cũ chỉ tới Ginza.
- S017 `6ab0c4cc-03a3-55a5-8fd5-193eee8881a7` (conditional): Hỏi phần còn hạn, nhân viên sẽ tính sau khi xem loại/hạn.
- S018 `69470875-f284-5d0c-8158-de335b9e89b5` (alternative): Hỏi lộ trình gợi ý có qua Ginza, được nhân viên xác nhận trên màn hình.
- S019 `4158cbde-75fb-54ab-9d3c-21e3708ee583` (pending): Chưa biết ngày, không chốt sớm; hẹn kiểm khi có lịch.
- S020 `543fde9d-027e-5aee-be68-84b3e34b2f3b` (follow_up): Có lịch thứ Hai, quay lại chốt ga đầu/cuối và ngày.
- S021 `57478d80-f4a7-5b8e-989e-8648affc0b1f` (problem): Hai lượt bị trừ khác, nêu nghi vấn, chưa tự kết luận sai.
- S022 `9e5ca611-e80e-5614-a8fd-87a371fc8b8c` (routine): Cung cấp thứ Ba/thứ Năm và chặng Asakusa–Shibuya.
- S023 `84606ab6-2abd-5b13-a499-bac4e6350b39` (misunderstanding): Sửa thứ Tư nghe nhầm thành hai ngày đang hỏi.
- S024 `b59dd4fb-b406-5a8e-9ae6-8f76ba84b3d2` (pending): Quầy cần kiểm thêm, người học chốt người và nơi hỏi lại.
- S025 `a5378705-87b3-5e81-aea2-7456c72bddaa` (follow_up): Quay lại đúng hai lượt; số khác được xác nhận nhưng nguyên nhân còn chờ.
