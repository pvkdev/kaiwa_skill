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
