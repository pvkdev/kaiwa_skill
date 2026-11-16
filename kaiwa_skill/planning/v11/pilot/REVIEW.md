# V11 · Nghiệm thu lại ba chặng pilot

Có 55 hội thoại và 314 lượt nói Nhật–Việt trong [HTML preview](ROADMAP.html). Trạng thái hiện tại là chờ chủ dự án duyệt ba pilot.

## Các cảnh nên mở khi đối chiếu

- **S-011 · Tàu điện và xe buýt** có 15 cảnh, 77 lượt. Ở cảnh 4–5, nhân viên chỉ đúng phía rồi hành khách tự nhắc cả ga đổi tàu lẫn sân ga. Ở cảnh 13–14, hành khách hỏi chờ ở đâu khi đi cùng mẹ. Chỉ khi nhân viên quay lại, họ mới biết nơi nhân viên ga sau sẽ đón. [Ghi nhận từng cảnh Sơ](S-011/RESEARCH.md)
- **T-044 · Gửi bưu kiện cá nhân và hỏi hàng quốc tế** có 25 cảnh, 145 lượt. Cảnh 13 tập hỏi phía nào có thể xử lý sau khi kiện rời Nhật. Cảnh 15 tập nghe cuộc gọi lại, xin người nói nhắc chậm rồi đọc lại cả tên đơn vị và cách dùng mã theo dõi. Cảnh 18–19 có cuộc hẹn hỏi tiến độ sau hai tuần và lượt người gửi thực sự đọc mã khi gọi lại. Mốc đó là thời điểm hai nhân vật thỏa thuận hỏi tiến độ. [Ghi nhận từng cảnh Trung](T-044/RESEARCH.md)
- **H-004 · Kính ngữ đối ngoại và chuyển lời xã giao** có 15 cảnh, 92 lượt. Cảnh 1 để chủ nhà giới thiệu trưởng bộ phận rồi mời khách vào việc. Cảnh 5–6 sửa hiểu lầm giữa lời mong được trao đổi tiếp và sự đồng thuận của hai công ty. Cảnh 7–8 giữ đúng ý khách khi chuyển lời ra ngoài và về nội bộ. Cảnh 11–12 tách việc đã xem tài liệu, đã phản hồi và đã phê duyệt. [Ghi nhận từng cảnh Thượng](H-004/RESEARCH.md)

## Cách rà và kiểm preview

Áp dụng ba lượt rà cho từng cảnh theo [skill V11](../../../../.agents/skills/kaiwa-topic-dialogue/SKILL.md). Đối chiếu lời của từng vai với việc cần làm và kết quả của tình huống. Đọc liền các cặp hỏi–đáp bằng cả hai ngôn ngữ và kiểm lại thông tin truyền sang cảnh sau. Sau đó đọc theo từng vai, kiểm độ khó khi đổi vai và những cuộc trao đổi dễ bị lặp trong cùng sự kiện. Bảng ở từng hồ sơ nghiên cứu ghi UID và lượt đối chiếu. Tệp status.json cạnh bản thảo gắn kết quả rà với dấu vân tay của từng cảnh.

Bộ kiểm cấu trúc đã kiểm 55 UID tình huống theo đúng thứ tự, 314 ID lượt duy nhất, hai trường Nhật–Việt, vai, giới tính và nguồn nội bộ. Đã đối chiếu từng hội thoại trong JSON xuất với bản tác giả, đối chiếu JSON nhúng trong HTML với learner.json, và so phần còn lại của lộ trình với V10.

Đã mở ba liên kết pilot trong Chrome headless ở hai kích thước 1280 × 800 và 390 × 844. Ở mỗi kích thước, mở phần thực hành và các sự kiện, so từng bối cảnh, câu Nhật, bản dịch Việt và nhãn vai/giọng trong DOM với JSON xuất. Hai file HTML preview và docs/index.html trùng nội dung.

## Nguồn đối chiếu

Hồ sơ từng chặng ghi tên sách, vị trí tra cứu và căn cứ cho các dữ kiện thực tế. Tên ga, người và mã bưu kiện phục vụ tình huống luyện. Cảnh xe buýt có phạm vi Toei Bus trong 23 quận Tokyo. Cảnh báo giá cho kiện 1,8 kg từ Tokyo tới Toronto phân biệt cước tại quầy với thời gian đến dự kiến. [Hướng dẫn Toei Bus](https://www.kotsu.metro.tokyo.jp/bus/kanren/riyo.html) · [Cước Japan Post](https://www.post.japanpost.jp/send/oversea/charge/list-parcel/zone3_en.html)

Trong cảnh gọi lại, Canada Post cung cấp nơi tra hành trình bằng mã theo dõi. Việc thay đổi địa chỉ phải hỏi riêng theo kiện và dịch vụ. Cảnh kiện hỏng khi đến Nhật dựa trên hướng dẫn về giữ nguyên bao bì và liên hệ bưu cục phụ trách phát. [Tra kiện trên Canada Post](https://www.canadapost-postescanada.ca/track-reperage/en) · [Japan Post về kiện hỏng](https://www.post.japanpost.jp/question/oversea/16_en.html)

H-004 đối chiếu cách nhắc đến cấp trên của công ty mình khi chuyển lời cho đối tác và cách xưng hô khi quay về nội bộ. [Hướng dẫn ウチとソト của Cơ quan Văn hóa Nhật Bản](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter7/detail.html)
