# Biên tập S-011 — nâng cấp r0003

Phần này thay các nhận định về nội dung hiện hành ở ghi chép r0002 bên dưới. r0002 được giữ làm lịch sử, không mô tả payload r0003.

## Quyết định tuyển pack

Đã quét chỉ mục/profile của đủ 27 sách, tìm theo 電車, バス, 駅, 乗り換え, sân ga, hỏi lại và lối hỗ trợ. Đọc trọn B08 Part 4 Unit 01/02 và trọn B01 chương phương tiện vận chuyển, bao gồm các câu đáp và lưu ý. Đối chiếu B11 bài ね, B11 bài 16, bài 88 và B14 các Section có vài câu nhà ga: nội dung toàn pack là ăn uống, thời tiết, việc khác hoặc lẫn toán/ý kiến, không phù hợp toàn chặng Sơ. Không tuyển B11/B14/B27 làm shadowing theo mảnh.

Chọn duy nhất pack B08 Part 4 Unit 01 電車に乗る, CD-2/4, tám câu Nhật. Inventory độc lập `kaiwa_skill/planning/catalog27/audio_packs/B08/u-part4-unit01.json` chốt ranh giới ở anchor của Unit, SHA-256 script và đúng thứ tự 8 câu. Câu số 5 đã có ID `k01-ex02` trong kiến thức, được chuyển vào vị trí 5 thay vì lặp; các ID còn lại giữ nơi tương ứng. Câu số 7–8 giữ nguyên dấu ／ và ngoặc của sách; giải thích trong k01 rằng đây là biến thể chữ in, khi nói chọn một cách. Chưa nghe file CD, nên không xác nhận cách thu, số lần lặp slow/natural hoặc rằng file audio có sẵn. CD/track chỉ là nhãn in và metadata sách.

Không chọn pack B08 Unit 02 CD-2/5 vì ba trong tám câu là taxi. S-011 tập trung tàu/buýt; taxi có chặng riêng S-014, không tạo cảnh taxi chỉ để hợp pack. Bỏ các câu B08 buýt từng lấy rời trong pilot cũ; giữ các câu buýt B01 được chọn theo chủ đề và hội thoại tự biên soạn, gắn `source_quote`/`source_adaptation`/`original_extension` đúng từng câu. B01 không thuộc danh mục pack buộc tra CD của SOURCE_SEQUENCE; không nhận đã đối chiếu file audio cho B01.

## Giữ lịch sử và mạch học

Giữ UID S-011, 15 ID tình huống, 3 ID challenge, một free talk cuối chặng và 104 lượt hội thoại tình huống. Retire `vSJ/k02/sh02` cùng câu nguồn B11, ba trích đoạn B14 và skit chuyển soạn B27 khỏi payload hiện hành; ghi retired cho node/câu, không tái sử dụng ID cho nội dung khác. `gSJ` vẫn là node tra cứu N4 cho cấu trúc điều kiện/từ chỉ lúc trong các câu nguồn B08, đã bỏ các tên mẫu không còn hiện diện. `sh03` giữ chức năng hỏi lại khi đứng sai chiều và thay phần trích đoạn bằng cuộc nói mới 6 lượt; ghi từng lời là viết mới.

Lõi học vẫn đi từ hỏi tuyến/ga đổi/sân ga sang phát hiện sai chiều, đi xe buýt, rồi nhờ lối phù hợp. Nhánh thật gồm đi thẳng/đổi tàu, sửa chiều đi, xe không đến thẳng, lỡ bến và báo người đợi, cần phối hợp hỗ trợ rồi chốt điểm gặp, vé không qua cổng. Mạng ga Aoba/Sakura/Midori, tuyến, sân ga, bến, giá và thời gian trong tình huống là giả định. Không dùng tên ga từ câu sách làm chỉ dẫn hành trình thật.

## Rà tiếng Nhật, từ, ngữ pháp và Live

Đã đọc lại từng lượt Nhật–Việt của 15 tình huống và shadowing sau thay đổi; kiểm người hỏi/đáp và thông tin chuyển qua các cảnh. Phần sáng tạo giữ câu Sơ ngắn, có hỏi lại/nhắc lại thực, không dùng mẫu điều kiện N4 như yêu cầu sản xuất bắt buộc. Cấu trúc điều kiện trong câu sách được ghi `source_reference` và tên N4 trong gSJ; とき N4 được hỗ trợ ở cụm buýt. Minna là nguồn tên mẫu, level là phân loại biên tập để admin tra cứu, không là danh sách chính thức JLPT.

Ba danh sách từ đã rút lại từ câu còn được nói, thay bằng chứng trích từ khi bỏ câu B11/B14/B27/B08 Unit 02. Động từ như 乗る, 降りる, 聞く, 待つ ở dạng từ điển; không giữ 快速, 終電, 朝, 明日, 整理券 khi không còn trong lời luyện. `validate` kiểm dấu vết chữ, còn tính đúng hình thái là phần rà của tác giả.

Ba challenge còn brief người học, context vai AI, nhánh variant và gợi ý; free talk cuối chặng có mở chuyện tự do và material context. Đã sửa lời dẫn k04/free talk để không nói bài ね còn được dạy. Không kiểm Live AI thực chạy, TTS hay import app; compiler chỉ kiểm cấu trúc. Nguồn web JR East/Kyoto trong pilot trước được giữ cho nhận định về khả năng phải chờ và sự khác nhau giữa các tuyến; không kiểm lịch, giá hoặc quy định hiện hành cho ga/xe giả định.

## Trước khi chốt

Đã đối chiếu toàn pack B08 với script/manifest nguyên văn và thứ tự; kiểm 8 câu Nhật và nghĩa Việt. Đã đọc lại B01 các câu buýt được giữ, sự khác nhau giữa quote và adaptation, 15 hội thoại, ba challenge và free talk. Không có người bản ngữ hoặc learner thử nghiệm. Phần còn nên được root nghiệm thu riêng là độ tự nhiên từng câu Nhật, bản dịch của biến thể sách có dấu ／, và quyết định xuất một pack tàu duy nhất khi buýt không có pack trọn cùng chủ đề. Chỉ finalize sau validate và đọc lại preview sinh ra.

---

# Nghiệm thu biên tập S-011 — r0002

## Phạm vi

Nâng cấp pilot theo review Claude và feedback chủ dự án; giữ UID chặng và đủ 15/15 tình huống V5. Không đổi V5, không chạy hàng loạt, không sửa repo Harumi. r0001 giữ nguyên để đối chiếu.

## Speak Japanese và shadowing

Đã đọc lại trọn B11 bài 1 (ね), đối chiếu hội thoại donut, dạng lịch sự và tám cặp ví dụ thuộc ba chức năng. k02 giữ những chất liệu này, viết lại giải thích Việt và thêm ba câu vận dụng tàu điện ở phần riêng. Không còn gọi ba câu mới là toàn bộ bài nguồn. sh02 đứng ngay sau k02, dùng chung utterance ID cho toàn bộ ví dụ; video vẫn planned.

Năm nhóm shadowing chứa 42 câu độc lập và 13 hội thoại mini với 36 lượt: chín đoạn B11 (mở đầu + tám ví dụ), ba đoạn B14 và một đoạn B27 chuyển soạn. Chúng nằm bên trong shadowing, không phình thành 13 chặng/bài tình huống độc lập. B08 có tám mẫu tàu điện được chọn (một câu đổi tàu đã ở nhóm lõi nên không lặp lại lần hai) và bốn mẫu buýt; B01 góp mười câu buýt giữ nguyên hoặc chuyển soạn. Đây là chất liệu luyện thực, không chỉ tên nguồn. sh05 vẫn là phần ứng dụng viết mới, không nhận là nguyên văn sách.

Nguồn B27 dùng cả bài diễn đạt và skit② của bài 8: giữ việc hỏi tàu có dừng, không hiểu thuật ngữ, hỏi lại và chuyển sang nhân viên khi người trả lời không chắc. Không nâng suy đoán sân ga trong sách thành dữ kiện chắc chắn. Các tên ga thật trong đoạn nguồn là bối cảnh luyện, không lời chỉ đường hiện hành.

## Từ vựng và gối đầu

Bốn danh sách gồm 90 mục, 82 từ khác nhau, trích ngược từ câu thực sự được nói trong tình huống hoặc shadowing. Mỗi mục có dấu vết câu/surface ở source-map.vocabulary_evidence. Động từ dùng dạng từ điển (行く, 降りる, 乗り換える…); tính từ dùng dạng cơ bản (おいしい, 暑い). Đã bỏ 使う và 着く khi hội thoại giản hóa không còn dùng, không thêm ngược câu chỉ để giữ từ. Chuẩn hóa hình thái đã được rà biên tập; bộ kiểm chỉ kiểm dấu vết và vài lỗi hình thức, không thay từ điển hình thái/người đọc.

Gối đầu là cân nhắc tự nhiên: các đoạn sau vận dụng hỏi vị trí, nêu điểm đến, nhắc lại bằng ね và hỏi lại khi chưa hiểu. review_links để rỗng; không link từng từ, không bắt đọc/tái dùng đủ hai bài gần nhất, không tạo nợ do chặng trước chưa soạn. Danh sách lặp giữa các cụm được giữ khi có ích cho ngữ cảnh, không gọi đó là trùng lỗi.

## Độ khó và ngữ pháp

Phần lõi 15 tình huống đã giản hóa các thể khả năng, điều kiện ば, 〜たかったんですが và cách hỏi 行かれますか bị review chỉ ra. Cụm trả tiền dùng とき (N4) có hỗ trợ rõ và tên mẫu riêng; không tuyên bố mọi câu ở chặng 11 đều chỉ dùng Minna 1–25.

Bảy mục ngữ pháp lõi và tám mục tham khảo nguồn có level + tên Minna; とき xuất hiện ở hai ngữ cảnh nên có 14 tên khác nhau. Ví dụ nguồn khó hơn có learning_scope: source_reference, danh sách ngữ pháp hỗ trợ gSJ và ghi chú trong kiến thức/preview. Chúng là phần làm quen tùy chọn, không yêu cầu Sơ phải tự sản xuất toàn bộ cấu trúc. Không dùng nhãn tham khảo để che câu lõi quá khó. Level N5/N4 là phân loại biên tập để admin tìm, không phải danh mục chính thức JLPT. ね và sắc thái/rút gọn được giải thích ở bài kiến thức; danh sách Minna không thay bài đó.

## Những sửa lời thoại

Đã đọc lại Nhật–Việt của 15 tình huống sau giản hóa và toàn bộ nhóm shadowing. S004 hỏi sân ga khi thông tin đó chưa được cung cấp, không ép hỏi lại hai lựa chọn sau câu trả lời rõ. S010 dịch cùng mức lịch sự với Nhật. Lược tám lượt kết công thức đã thừa; giữ ID các lượt còn lại, ghi retired cho lượt bỏ. Rà tiếp S009/S011 để lời đáp khớp câu hỏi mở đã đổi. Hội thoại lõi còn 104 lượt, không kéo dài để tăng số lượng.

## Nguồn và dữ kiện

Quét chỉ mục 27 sách là phần của r0001; lượt này đọc lại phần được chọn B01/B08/B11/B14/B27 và tên mẫu Minna, không nhận đã đọc hết 27 sách hoặc kiểm ảnh PDF. Giữ source hash/locator, thêm skit B27 thực dùng. Mỗi utterance có source_quote/source_adaptation/original_extension và source_refs; quote giữ chữ Nhật đã đối chiếu, dịch Việt được biên tập. Câu generic viết mới không tự biến thành quote chỉ vì giống sách. Nhãn cấp node không thay nhãn từng câu.

Nguồn web JR East/Kyoto kế thừa lần đọc ở r0001, không có nghiên cứu web mới trong lượt này. Mạng tuyến, giá, thời gian và điểm gặp trong 15 tình huống/challenge vẫn là giả định; không hứa thủ tục/dịch vụ/giá thật. Nguồn ngoài chỉ hỗ trợ nhận định quy tắc có thể khác nhau và việc hỗ trợ có thể cần chờ.

## Challenge, free talk và phục hồi

Giữ ba challenge/sáu biến thể và một free talk cuối chặng. Context challenge được chọn lại để không trộn toàn bộ đoạn nguồn có tên ga thật vào mạng giả định. Free talk giữ đủ material nodes, tách câu nguồn tham khảo khỏi phần luyện chủ động; không ghép lệnh kín của challenge.

Lượt nâng cấp đã pause/recover thật khi thay helper/schema: giữ draft cũ, nhận run/draft mới, kiểm lại thay đổi spec và tiếp nội dung đã ghi. Không sửa hash để che drift. Canonical là bản nội dung gốc; workspace/context và artifact được sinh. Chưa chạy Live AI, TTS, import DB hoặc pilot Trung/Thượng. Chưa có người bản ngữ hoặc thử nghiệm với learner; kiểm cấu trúc không chứng minh hiệu quả sư phạm hay tiếng Nhật hoàn hảo.

## Sau pilot

Bản này để chủ dự án đọc và đánh giá độ sâu/độ vừa sức. Không tự chạy hàng loạt. Nếu cần sửa tiếp, begin --from-current tạo revision mới; giữ ID đối tượng còn cùng nghĩa, cập nhật lời thoại/từ/ngữ pháp/nguồn/context liên quan. Chất lượng giao tiếp quyết định việc tuyển chọn, không đặt KPI dùng hết tài nguyên.


Đã chỉnh lời bài về cách đi xe buýt và chỉ dẫn Live để đứng độc lập với tên cấp.
