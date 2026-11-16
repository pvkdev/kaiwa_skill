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

## Rà vòng hai từng cảnh — tác giả, 2026-11-16

Quy ước bảng: `u01–u06` là hậu tố turn ID đầy đủ `<situation_uid>-u01` đến `<situation_uid>-u06`. Đã đọc lượt liên tiếp theo JA rồi VI, đọc cả lượt A và B để thử đổi vai; cột cuối ghi quyết định sau ba phép rà: hành vi/kết quả, ngôi-nghĩa/gối đầu, và sức nói–nghe mức Sơ. Đây là tự rà tác giả, không phải root nghiệm thu.

| UID tình huống | Turn ID đã rà | Kết quả và ghi nhận cụ thể |
|---|---|---|
| `519f0e38-bbc1-5164-a0a0-bd370a5e996d` (S001) | u01–u06 | A hỏi tàu đến Sakura, B nói không đến Sakura nhưng đi Aoba; A xác nhận lên tàu hiện tại đến Aoba. Hai vai rõ, VI không biến thành tàu đi thẳng. Giữ. |
| `ae9d1408-aae7-5398-85ba-a2c7f29a45d6` (S002) | u01–u05 | A hỏi ga đổi, B nhắc Aoba và nơi xuống; A nhắc lại. Bối cảnh chỉ cho biết người học nghe nói phải đổi, chưa biết ga nào; không lấy đáp án từ S001. Giữ lời thoại. |
| `c86d5282-a8f9-5db3-9a55-2ded9d0541b0` (S003) | u01–u05 | A hỏi phía tàu tới Sakura, B chỉ số 2; A trỏ nhầm cầu thang, B sửa, A nhận ra. `こちら/あちら` đúng điểm nhìn, VI giữ đúng cầu thang phía trước. Giữ. |
| `2f02b243-cae3-5107-bff3-aa7a1e38f18c` (S004) | u01–u05 | A ở chiều ngược và hỏi lại hướng; B chỉ sân ga 2 đối diện. Sửa u04 thành `あちらのホームへどうぞ` / “Mời chị sang sân ga đó”, rõ nơi đến và lịch sự hơn “Bạn đi phía kia”; A nhắc lại. |
| `68b27ce2-cdc7-550e-a748-0b7dfe400a8c` (S005) | u01–u05 | Tiếp S004: A nay hỏi chính Aoba là ga đổi ở u01 **và** xác nhận sân ga 2 hướng Sakura ở u03; B đáp từng dữ kiện, A đi. Không chỉ hỏi tên ga; không đổi kết quả S004. |
| `25ad555b-8021-5d65-8c3b-e53b723c403a` (S006) | u01–u05 | A hỏi xe có dừng Thư viện, rồi số bến; B nói bến thứ ba, A nhắc lại. Không lẫn “bến thứ ba” với số tuyến. Giữ. |
| `52f40bb7-9557-5778-a222-b3e2006859b0` (S007) | u01–u05 | A hỏi cửa và lúc trả, B đáp cửa trước/trả khi lên; A thực hiện. Chỉ áp dụng Toei Bus trong 23 quận Tokyo như bối cảnh; không phổ quát cho Tama. Giữ. |
| `ea8e465e-3b20-539c-8168-255b71403c65` (S008) | u01–u06 | B từ chối xe đi thẳng Bệnh viện, A hỏi điểm đổi, B chỉ Công viên Trung tâm và yêu cầu kiểm chỗ đón kế tiếp. VI không hứa có sẵn bến/tuyến thật. Giữ. |
| `0c09f777-1f73-55e3-b5a5-c365485eb552` (S009) | u01–u05 | A biết vừa quá bến Thư viện, hỏi bến có thể xuống tiếp; B chỉ Hội trường Thành phố; A bấm nút. Cảnh đặt lúc xe tạm dừng, không xin xuống giữa đường. Giữ. |
| `82d2a9aa-d6d8-54cc-9fbd-dbb23b49a236` (S010) | u01–u05 | Tiếp S009: A gọi bạn nam bằng giọng thân, nêu bến sẽ xuống và chỉ báo “muộn một chút”; B chờ trước thư viện, A hứa gọi lại sau khi xuống. Không tự hứa giờ đến. Giữ. |
| `4e5556ca-92ca-5164-95fa-96f682da6aea` (S011) | u01–u05 | A mang nhiều hành lý hỏi thang máy; B chỉ mốc bên phải cổng, A xác nhận. Mốc là ví dụ ga không định danh, không tuyên bố mọi ga giống nhau. Giữ. |
| `add40c3f-065e-5f08-9731-8961e5ccf623` (S012) | u01–u05 | A nêu mẹ khó đi cầu thang rồi hỏi lối đang chỉ; B chỉ đường qua thang máy; A nhắc điểm rẽ. Hai vai ngắn, `母`/“mẹ” nhất quán với S013–S014. Giữ. |
| `ef5dae70-6a18-50f5-a57c-0fb6506894dc` (S013) | u01–u05 | A nêu đổi ở Aoba và mẹ khó đi cầu thang; B nói cần kiểm hỗ trợ; **A tự hỏi đâu để đợi ở u03**, B mới chỉ cạnh cổng ở u04, A nhắc mốc ở u05. Bối cảnh không cho trước đáp án chờ. |
| `14c7db18-06fa-519f-9b65-1872108db28d` (S014) | u01–u05 | Tiếp S013 sau khi B đã kiểm Aoba: B báo nhân viên đợi trước thang máy sân ga bằng câu ngắn hơn; A nhắc điểm gặp; B chỉ bước sau khi xuống, A nói sẽ đi cùng mẹ. Không hứa hỗ trợ trước lúc xác nhận. |
| `2393a507-1d7c-5210-8725-49c28f0ed7ae` (S015) | u01–u05 | A nói vé không qua cổng rồi hỏi quầy; B chỉ quầy và xin vé; A nhờ kiểm. Rút u02 thành `窓口で確認します` cho nhân viên đang nói tại cổng; không kết luận nguyên nhân vé. |

Rà thêm bối cảnh/ngôi: S004 chỉ cho biết người học **chưa rõ** chiều tàu, S008 chưa nói trước xe có đi thẳng hay bến cần đổi, S013 chưa cho biết câu đáp hoặc chỗ chờ, S014 chỉ cho biết nhân viên vừa quay lại. S005 mở bằng việc đã được báo sai chiều ở S004, không dùng cụm khó hiểu “được chỉ khỏi sân ga”. S003 nêu rõ hỏi lối đến sân ga. Bỏ “trong hành trình minh họa” khỏi bối cảnh học viên ở S001/S003; tuyến và bến giả định vẫn được giải thích ở phần quản trị đầu file này. Khi nhân viên nam nói trực tiếp với người học nữ, VI dùng “chị” nếu cần đại từ; người học cảm ơn “anh” ở S006, cùng giọng với các cảnh ga/buýt khác. Đã đọc lại trọn E01, E02, E03 sau chỉnh, kể cả S004→S005, S009→S010 và S013→S014; lời đáp vẫn tiết lộ thông tin theo đúng lượt.
