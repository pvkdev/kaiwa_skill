# V11 · Ba pilot hội thoại

Trạng thái bàn giao là chờ chủ dự án duyệt. Phạm vi gồm S-011, T-044, H-004 với 55 hội thoại Nhật–Việt. Mỗi chặng có dialogues.json, status.json và RESEARCH.md. BUILD.json ghi số lượng và hash của bản đã ghép vào preview.

## Nội dung đã đọc và sửa

Root đã đọc đủ 15 hội thoại S-011, 25 hội thoại T-044 và 15 hội thoại H-004 bằng cả hai ngôn ngữ. Các worker tự đọc lại chặng của mình; sau đó có lượt đọc chéo Sơ → Thượng và Trung, Thượng → Sơ. Root quyết định sửa và đọc lại các lượt liên quan sau góp ý.

- S-011 có 77 lượt nói. Các cảnh phân biệt hỏi tàu, đổi tuyến, đứng sai phía, đi quá bến, báo muộn cho bạn và nhờ hỗ trợ đi cùng mẹ. Đã sửa cách gọi người đi cùng, trình tự hỏi quầy kiểm vé và dịch 番線 thành sân ga để người học hiểu đúng nơi lên tàu. Đã đọc lại các cảnh tiếp nối cùng hành trình. Các ga và chỉ dẫn cụ thể là giả định cho bài luyện; riêng cảnh lên/trả tiền xe buýt nêu rõ phạm vi Toei Bus trong 23 quận Tokyo.
- T-044 có 151 lượt nói. Đã sửa bốn cảnh nhân viên mở lời bị đảo ID vai; thêm câu trả lời về phí và thời gian để khách chọn được cách gửi; phân biệt bưu kiện từ Nhật đi Canada với kiện hỏng từ Canada đến Nhật. Đã sửa cách giữ bao bì và hẹn kiểm tra tại nơi nhận, mức chắc chắn về việc bắt đầu điều tra và cách dịch trạng thái theo dõi. Thời gian tới Toronto là ước lượng trong tình huống. Bảng giá được ghim theo tài liệu Japan Post đã tra, có nguồn và ngày đọc ở hồ sơ nội bộ.
- H-004 có 92 lượt nói. Đã sửa chỗ nhân vật phía đối tác dùng kính ngữ cho cấp trên của chính mình, sự khác nhau giữa đã nhận tài liệu/đã đọc/đã có ý kiến/đã phê duyệt, và lời dịch có thể khiến người học hiểu việc phê duyệt chắc chắn sẽ tới. Cảnh chuyển lời về nội bộ giữ cách gọi phù hợp quan hệ mới. Đã bổ sung mốc tháng vào lời mong muốn để tình huống hiểu nhầm tiếp theo có căn cứ.

Các mã cảnh nội bộ trong bối cảnh hiển thị được đổi thành tên tình huống. JA và VI nằm ở hai trường riêng, speaker_id nối tới vai có gender male/female. Nguồn sách được ghi cả mã, tên, đường dẫn và dải dòng. Các hội thoại mới có ghi nhận viết mới ở từng lượt, cùng căn cứ tham khảo cấp cảnh.

## Nguồn được đối chiếu

Worker tra chỉ mục trên phạm vi 27 sách rồi mở các đoạn phù hợp và bài chuyên đề gần trước để đọc. RESEARCH.md của từng chặng ghi phạm vi đọc thật, những đoạn không dùng và lý do. Root đối chiếu các đoạn nguồn chính và mở lại hướng dẫn của Cơ quan Văn hóa về quan hệ trong–ngoài, Toei Bus về cách lên/trả tiền và Japan Post về thay đổi địa chỉ, hàng cấm, kiện hỏng. Lượt đọc chéo còn kiểm bảng cước Zone 3 của Japan Post.

- [Cơ quan Văn hóa · ウチとソト](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter7/detail.html)
- [Toei Bus · cách sử dụng](https://www.kotsu.metro.tokyo.jp/bus/kanren/riyo.html)
- [Japan Post · bưu kiện bị hỏng](https://www.post.japanpost.jp/question/oversea/16_en.html)
- [Japan Post · giới hạn sửa địa chỉ EMS](https://www.post.japanpost.jp/question/oversea/135_en.html)
- [Japan Post · cước bưu kiện Zone 3](https://www.post.japanpost.jp/send/oversea/charge/list-parcel/zone3_en.html)

## Preview và kiểm kỹ thuật

ROADMAP.html nhúng đúng nội dung pilot/learner.json. docs/index.html dùng cùng bản dựng. Ba liên kết Pilot ở đầu nội dung mở đúng chặng; các tab Sơ/Trung/Thượng vẫn duyệt được toàn bộ nền V10 để xem chuyên đề và vị trí học. Hội thoại nằm trong mục Thực hành tình huống, phân nhóm theo sự kiện.

Đã kiểm đủ UID/thứ tự của 55 cảnh, 320 ID lượt duy nhất, JA–VI, hai vai, gender, con trỏ sách và liên kết chuyên đề. Đã kiểm trùng nguyên kịch bản giữa ba pilot. Kiểm hàm render bằng DOM giả lập xác nhận các bối cảnh, 320 lời Nhật và 320 bản dịch được tạo vào phần tình huống; kiểm cú pháp JavaScript đạt. Kiểm lại dữ liệu xuất sau sửa và dựng lại để xác nhận ID giữ nguyên.

**Giới hạn nghiệm thu giao diện.** Công cụ browser chặn URL file cục bộ khi mở ROADMAP.html. Lượt này đã kiểm dữ liệu nhúng và đường render bằng mã, chưa quan sát giao diện thật trên PC/mobile. Có thể mở trực tiếp file preview hoặc dùng docs/index.html khi đưa lên GitHub Pages để duyệt.

Skill được bổ sung hướng dẫn kiểm thông tin từng vai thực sự biết, rà kính ngữ của cả hai phía và cho cảnh hỏi giá/điều kiện có câu trả lời đủ để luyện bước tiếp. Token thực không được runtime cung cấp nên báo cáo này không quy đổi thành quota hay dự báo chính xác chi phí hàng loạt.
