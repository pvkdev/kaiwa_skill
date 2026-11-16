# S-011 — nghiên cứu và tự rà bản thảo V11

Ngày đọc: 2026-11-16. Phạm vi: đúng 15 tình huống V10 của chặng S-011, ba sự kiện E01–E03. Đây là hội thoại mới do biên tập, không phải lời thoại/audio nguyên bản sách. `origin: ai_authored` trong V10 chỉ nói về khung tình huống.

## Đối chiếu V10 và chuyên đề liền trước

Đã chạy `dialogue.py S-011` và đọc toàn bộ brief: UID, thứ tự, nhánh, `continues_from`, vai và mục tiêu. E01 dùng lộ trình **minh họa** ga Sakura → đổi ở ga Aoba → đường ray 2; S004→S005 là cặp sai chiều rồi kiểm lại. E02: S006/S007/S008 là các cảnh riêng; S009→S010 cùng một lần đi quá bến Thư viện, xuống bến Hội trường Thành phố rồi gọi bạn. E03: S011, S012 và S015 độc lập; S013→S014 chỉ chốt điểm gặp sau khi ga chuyển đã xác nhận. Tên ga, bến, số sân ga, thứ tự bến là dữ kiện hư cấu để tập nói, không là hướng dẫn hành trình thật.

Đã đọc `kaiwa_skill/planning/v10/stages/sj-so-03/lesson.md` trọn bài và `practice.json` các ví dụ gắn UID S003, S004, S011 cùng phần luyện kế cận. Dùng `どちら` khi hỏi hướng, `こちら/あちら` từ điểm nhìn hai vai; chỉ gắn `specialty_item_ids` nơi cách dùng có trong lời nói. Không chép nguyên câu luyện của chuyên đề.

## Tra đủ catalog 27 và đọc Markdown gốc

Đã mở `kaiwa_skill/planning/catalog27/BOOK_GUIDE.md`, `manifest.json` và tìm trong `source_index.jsonl` trên toàn bộ B01–B27 theo chức năng/quan hệ/cụm `乗り換え`, `乗り場`, `ホーム`, `バス停`, `駅員`, `改札`, `エレベーター`, `方向`, `電車`, cùng `道を` và hỏi lại. Chỉ mục theo nhãn cho nhiều kết quả liên quan ở B08, B18, B27; B01 có đoạn đi lại hữu ích dù truy vấn chỉ mục không bộc lộ đủ nội dung trong nhãn. B03/B05 nêu thang máy trong công ty/khách sạn, không dùng để suy đường trong ga. B26 có role-play so tàu nhanh hơn; quá mục tiêu cảnh Sơ. B14 và các sách nghiệp vụ không cho đoạn gần mục tiêu bằng các nguồn đã chọn. Đây là tra toàn kho để chọn, **không phải** đã đọc sâu cả 27 sách.

Các đoạn đã mở và đọc lời trước/sau:

- B01, *5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày*, `kaiwa_skill/knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/07-phuong-tien-van-chuyen.md`, dòng 5–127 (xe buýt, đổi và xuống quá bến), 130–202 (tàu). Sách có ví dụ tàu điện ngầm chạy 24 giờ ở dòng 157–164; **không dùng** khẳng định đó vì không đúng như một quy tắc chung ở Nhật.
- B08, *どんどん話せる！日本語会話フレーズ大特訓 必須700*, `kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md`, dòng 8–35 (hỏi tàu/ga đổi/sân ga), 37–64 (xe buýt, hỏi lúc trả tiền). Lời khuyên trong sách nói có tuyến trả khi lên, có tuyến trả khi xuống; xác minh theo nhà vận hành cho S007.
- B18, *外国人のための日本語敬語の使い方 基本表現85*, `kaiwa_skill/knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md`, dòng 429–461, gồm cảnh hỏi xe buýt và hỏi tàu ngược chiều. Chỉ lấy chức năng và sắc thái hỏi, không lấy dữ kiện tuyến/số từ sách.
- B27, *聞いて覚える話し方 日本語生中継 初中級編２*, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/09-bai-08-eki-de.md`, dòng 1–84 và 105–220, gồm quan hệ hành khách–nhân viên, sân ga, xác nhận và chuyện nhầm vé. Các mẫu nâng hơn được rút về câu Sơ.
- B25, *聞いて覚える話し方 日本語生中継 中～上級編*, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/02-bai-1-dengon.md`, dòng 3–35: lời nhắn thân mật về đến muộn và liên lạc lại. S010 viết thành cuộc gọi mới, không hứa giờ đến chưa biết.
- Có mở B26, *聞いて覚える話し方 日本語生中継 初中級編 1*, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/08-bai-8.md`, dòng 325–348; không gắn nguồn vào cảnh vì nội dung so phương tiện/tốc độ không được dùng.

Các dải và tiêu đề sách đã dùng được ghi ở `dialogues.json.admin_sources`; từng cảnh ghi `source_refs`. Mỗi lượt là `original_extension`. Các cụm rất thường gặp như `すみません` và `ありがとうございます` không được trình bày như trích dẫn sách.

## Kiểm thực tế tại nhà vận hành

- [Tokyo Metro — Before Getting on the Subway](https://www.tokyometro.jp/en/tips/before.html): biển sân ga chỉ tuyến, hướng, số và ga chính. Căn cứ cho việc hỏi lại hướng/sân ga; không chứng minh lộ trình hư cấu Aoba/Sakura.
- [東京都交通局 — バスの利用方法](https://www.kotsu.metro.tokyo.jp/bus/kanren/riyo.html): Toei Bus **trong 23 quận Tokyo** lên cửa trước, trả lúc lên, xuống cửa sau; bấm nút sau thông báo bến. Trang này cũng ghi **Tama lên cửa sau, trả lúc xuống**, nên S007 nêu rõ khu vực. S009 chỉ hỏi bến xuống kế tiếp; không khẳng định có thể xuống giữa bến.
- [JR East — Accessibility](https://www.jreast.co.jp/multi/customer_support/accessibility.html) và [JR East — hỗ trợ đi lại](https://www.jreast.co.jp/en/equipment/equipment_1/wheelchair/): nhân viên có thể hỗ trợ và điều phối với ga; mức hỗ trợ và thời điểm phụ thuộc tình huống. S013 chỉ nói sẽ kiểm rồi chờ, S014 xác nhận một điểm gặp cụ thể **sau khi kiểm trong câu chuyện**. Không suy mọi ga đều có cùng lối hay dịch vụ.
- [Tokyo Metro FAQ — ticket gate mistake](https://ssl.tokyometro.jp/support/faq_answer?faqno=OpenFAQ-001047&lang=en): đưa vé cho nhân viên cổng để họ kiểm và xử lý trường hợp đi nhầm. S015 là lỗi vé không qua máy, nên chỉ dùng nguyên tắc nhờ nhân viên kiểm, không tự nói nguyên nhân hay cách xử lý phí.

Các URL trên đã tra bằng tìm kiếm web ngày 2026-11-16. Chúng chỉ làm căn cứ cho dữ kiện nhà vận hành, còn hội thoại là cảnh giả định. Không dùng phí, giờ xe hoặc quyền lợi trợ giúp cụ thể.

## Mục đích từng cảnh và kết quả

- S001: người học chưa biết tàu có đi thẳng Sakura; nhân viên biết tàu dừng Aoba; chốt phải lên tàu này rồi đổi ở Aoba. Lời đáp nêu rõ tàu này **không** đến Sakura.
- S002: người học chưa nghe rõ ga đổi; nhân viên nhắc Aoba; người học xác nhận tên ga sẽ xuống.
- S003: người học đã ở Aoba nhưng chưa biết đường ray; nhân viên chỉ số 2 và cầu thang; người học sửa lựa chọn cầu thang khi bị chỉ nhầm.
- S004: người học ở sân ga ngược; nhân viên nói sai chiều và chỉ phía đối diện; người học nhắc lại đường ray 2.
- S005: sau S004, người học kiểm lại ga hiện tại và đường ray/hướng; rời sân ga sai.
- S006: trước khi lên buýt, người học hỏi bến Thư viện và số thứ tự; biết đó là bến thứ ba trong cảnh minh họa.
- S007: người học hỏi cửa và lúc trả tiền; lái xe trả lời theo Toei Bus khu vực đã nêu; người học trả khi lên.
- S008: xe không đi thẳng bến Bệnh viện; người học hỏi bến đổi; biết xuống Công viên Trung tâm rồi kiểm chỗ đón xe tiếp.
- S009: đã quá bến Thư viện; người học hỏi bến kế có thể xuống; chọn bấm nút để xuống Hội trường Thành phố.
- S010: bạn đang đợi chưa biết sự cố; người học báo đi quá bến, bến sẽ xuống và sẽ liên lạc lại; bạn tiếp tục chờ ở thư viện.
- S011: người học nhiều hành lý cần thang máy; nhân viên chỉ theo mốc cổng soát vé; người học nhắc lại mốc.
- S012: mẹ khó dùng cầu thang; người học hỏi một lối đang thấy; nhân viên chỉ lối thang máy cụ thể; người học nhắc lại điểm rẽ.
- S013: cần hỗ trợ ở ga chuyển nhưng chưa có xác nhận; nhân viên kiểm với ga Aoba; hai mẹ con chờ bên cổng.
- S014: ga Aoba đã xác nhận trong câu chuyện; người học kiểm lại điểm gặp ở trước thang máy trên sân ga và đi cùng mẹ tới đó.
- S015: vé không qua máy, nguyên nhân chưa rõ; người học hỏi quầy; nhân viên chỉ quầy và xin xem vé; người học đưa vé, chưa tự kết luận vé hỏng.

## Tự rà tác giả

Đã đọc liền 15 cảnh theo thứ tự, đọc riêng toàn bộ JA và VI, kiểm hai vai, hậu quả nhánh, vai người đợi ở S010, nhất quán Aoba/Sakura/đường ray 2, Thư viện/Hội trường Thành phố và mẹ ở S012–S014. Đã sửa sau lần đọc đầu: S001 làm rõ tàu không đến thẳng Sakura nhưng đi Aoba; S012/S013 dùng “mẹ” và câu ngắn tự nhiên; S014 giữ quan hệ đó; S015 hỏi quầy trước khi đưa vé; S009 đặt câu hỏi khi xe tạm dừng; S010 rút lời báo muộn xuống mức Sơ. Lời nhân viên có vài cụm nghe cố định lịch sự (`お待ちください`, `ご案内します`); người học nói ngắn. Không có khẳng định y tế/quyền lợi, giờ hay phí. `dialogue.py --check` chỉ xác nhận cấu trúc, không thay việc root review ngôn ngữ và preview.
