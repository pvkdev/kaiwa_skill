# Chọn bài theo chặng và tra lại CD

Chọn nguồn bằng tình huống, chức năng giao tiếp và quan hệ giữa hai vai của chặng đang viết. Đọc lời thoại để xét độ khó thực tế. Ví dụ, chặng hỏi đường ở ga có thể chọn ngay skit 「駅で」 trong bài 8 nếu lời thoại vừa sức. Nếu chỉ giống về địa điểm nhưng mục tiêu nói khác, hoặc phải viết lại lời mới vừa sức, chọn pack khác. `SOURCE_SEQUENCE.json` là danh mục tra cứu và gợi ý phân bổ. Worker có thể chọn khi danh sách phân bổ trống, bỏ qua gợi ý hoặc chọn bài ở vị trí bất kỳ.

| Nhóm | Sách | Cấp chặng được dùng | Đơn vị tra trong chỉ mục |
|---|---|---|---|
| Speak Japanese | B11 基本文型88 (cơ bản) | Sơ, Trung | một bài/mẫu, 88 đơn vị |
| Speak Japanese | B12 発展文型125 (phát triển) | Trung, Thượng | một mẫu, 125 đơn vị |
| Shadowing | B14 初～中級 | Sơ, Trung | một Section, 42 đơn vị |
| Shadowing | B13 中～上級 | Trung, Thượng | một trang đoạn luyện của Section |
| Nama Chuukei | B27 初中級2 | Sơ, Trung | một trang script trong phụ lục |
| なめらか | B09 | Trung, Thượng | phần 用例 của một mục |

B25 và B26 (Nama Chuukei) đang ở trạng thái `excluded`: bản knowledge không có script hội thoại. Chủ dự án cho phép bỏ khi không tìm thấy script. Khi có script thì coordinator mở lại trong kế hoạch, không tự dùng trong chặng.

Các sách còn lại **không thuộc kế hoạch** và vẫn chọn theo topic của chặng: B01 5500 (gom theo nhóm mục đích), B08 必須700 (gom theo topic/chức năng), các sách công việc, roleplay, kính ngữ, biểu đạt cảm xúc. Cấp trong bảng lấy từ `catalog27/annotations`; coordinator sửa trong kế hoạch khi chủ dự án quyết khác.

## Giữ pack dùng chung audio

Pack là **toàn bộ phần nghe được sách hoặc CD nhóm thành một đơn vị**. Ranh giới do nguồn xác định. Một pack có thể gồm nhiều hội thoại, nhiều track, nhiều trang hoặc file. Nếu nguồn nhóm cả bộ thành một pack thì giữ nguyên cả bộ. Chỉ coi hai track trên cùng đĩa là hai pack khi có bằng chứng chúng là hai bài nghe độc lập. Chọn theo chủ đề và độ khó của **toàn pack**. Nếu chỉ vài đoạn hợp chặng, tìm pack khác hoặc soạn tình huống mới.

Đặt đủ mọi track và lượt của pack trong **một node shadowing của một chặng**, đúng thứ tự, đủ cả lời đệm, lời đáp và các lần lặp. Có thể chia hiển thị thành nhiều hội thoại bên trong cùng node theo cách sách chia. Không lấy trích đoạn, chia sang hai node/chặng, đảo lượt hoặc chen câu AI giữa cụm. Giải thích/biên dịch bằng tiếng Việt; ví dụ ứng dụng mới đặt sau pack. Bài Speak Japanese phải khai báo đúng book_id và unit của bài, dùng các utterance gốc của pack trong MD theo thứ tự, và ngay sau đó là shadowing dùng lại đúng các ID ấy.

### Lập bảng kê trước khi soạn

Tra đúng ấn bản ở script, PDF và kiểm kê audio của sách. Lưu **một bảng kê dùng chung cho mỗi pack** trong `kaiwa_skill/planning/catalog27/audio_packs/<book_id>/<mã-pack>.json`. Tìm theo sách, bài và nhãn track trước khi lập mới để tránh hai mã cho hai nửa cùng pack. Lập dần theo nhu cầu. Không sinh bảng kê từ những câu đã chọn trong draft. Rà toàn bộ ranh giới mở đầu/kết thúc, từng track và lượt với nguồn trước khi đưa vào danh mục; không sửa bảng kê cho khớp một draft thiếu. Khi ranh giới chưa xác định, để pack đó chờ đối chiếu.

Mẫu thật để tra là `B14/u-sd-u1-s01.json` (Unit 1, Section 1, CD 02, mười đoạn A/B). Bảng kê ghi ấn bản, bằng chứng ranh giới, danh sách track theo thứ tự in, nhãn đĩa/track và locator. Trong mỗi track, `parts` là các phần script vật lý theo thứ tự, chỉ để đối chiếu nếu script trải qua nhiều trang hoặc file. Mỗi phần ghi đường dẫn chương từ gốc repo, SHA-256 của file, anchor unit, và toàn bộ lượt nói. Mỗi lượt là bộ ba [số dòng tính từ 1, vị trí bắt đầu tính từ 0, vị trí kết thúc không bao gồm], tính bằng ký tự Unicode của dòng UTF-8 đã giải mã, bỏ ký tự xuống dòng. Lấy chính xác lời Nhật, loại nhãn vai, dịch Việt và chỉ dẫn sân khấu. Nhiều lượt có thể có cùng lời. Không suy số đĩa từ tên bài; ghi `unknown` cho nhãn chưa biết, kèm nơi tra lại. Số track in trong sách chưa chứng minh có file audio.

### Khai báo và tra lại trong revision

`sequence_units` ghi các unit đã chọn tại node tương ứng; với Speak Japanese khai báo tại node kiến thức. Trong `source-map.json.audio_packs`, mỗi pack có một mục gồm `pack_id`, `manifest_sha256`, `shadowing_node_id`, `utterance_ids` theo đủ thứ tự của mọi track. Không tự khai báo một danh sách rút gọn làm chuẩn. Đăng ký từng file script trong `sources.json` với book_id, path và sha256 thực, mỗi utterance là `source_quote` trỏ đúng script. Dùng ID lặp ở vị trí tương ứng nếu cùng một câu được thu hai lần.

Compiler mở bảng kê độc lập, so số lượng, nguyên văn và thứ tự từng lượt từ các vị trí trong script, rồi kiểm các ID nằm liên tiếp trong một node. Với Speak Japanese, compiler đối chiếu book_id/unit của pack với bài khai báo và thứ tự câu trong MD kiến thức. Bảng tra được sinh thành `audio-index.json` trong revision, gồm node, ID câu, ấn bản, track và vị trí script. Khi sửa hoặc phục hồi, đối chiếu lại nếu hash của script/bảng kê thay đổi. Muốn thay track khi sửa nội dung thì thay cả pack.

## Tra cứu

Từ gốc repo, dùng `source_sequence.py` trong thư mục scripts của skill. `units --book B27` liệt kê anchor, `stage --stage UID` xem gợi ý, `check` rà danh mục và `table --level Trung` xem phân bổ. Thứ tự in trong chỉ mục giúp tìm lại bài trong sách. Chọn thứ tự học theo mục tiêu của chặng.
