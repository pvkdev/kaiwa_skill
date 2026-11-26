# Renshuu B: biến thể trực tiếp từ drill nguồn, 50 bài

## Phạm vi

- Drill nguồn: **1471** trên 50 bài.
- Đã có trong bộ B chính: **100** biến thể trực tiếp (2/bài).
- Vòng bổ sung này: **959** biến thể ở **50** bài; gồm 949 chọn một, 6 điền chỗ trống, 4 chọn nhiều.
- Trong đó có **17** bài AI viết lại từ cue nguồn mơ hồ; mỗi bài có ngữ cảnh chữ, ba nhiễu và giải thích riêng. Đáp án của bài viết lại không phải khóa nguồn.
- **1059** drill đã có biến thể với đáp án AI biên tập xác định. Đây là số *eligible ở mức bản nháp AI*, không tính ví dụ nhận diện trong bộ B chính.
- **1041** drill không mang ảnh trong markup hoặc thuộc nhóm có dữ kiện chữ đã kiểm. Đây là bộ lọc ứng viên theo markup, không phải tập bao trùm các câu đã biên tập: một số câu nguồn có ảnh đã được viết lại thành ngữ cảnh chữ.

## Còn chờ theo lý do

- **412** drill có ảnh/ngữ cảnh bên ngoài cue chưa được biên tập chắc.
- **0** drill chữ chưa được giải và kiểm riêng.
- **0** cue mơ hồ còn thiếu biến thể. Danh sách gốc 17 cue đã viết lại nằm ở mục dưới và trường `original_ambiguous_source_cues` trong JSON bài.

Tổng pending: **412**. Tất cả **1471** đáp án nguồn vẫn chưa được site trả trong snapshot. Trường `correct` của biến thể là đáp án suy luận/biên tập AI, `human_review` vẫn là `pending`; không gắn nhãn đáp án chính thức. Không dùng vị trí chip hoặc `data-p` làm đáp án.

## Cue nguồn mơ hồ đã viết lại

- Bài 08, b5-1: そして và が đều tạo được câu; mức tương phản là lựa chọn biên tập.
- Bài 08, b5-2: そして và が đều tạo được câu; mức tương phản là lựa chọn biên tập.
- Bài 08, b5-3: そして và が đều tạo được câu; mức tương phản là lựa chọn biên tập.
- Bài 08, b5-4: そして và が đều tạo được câu; mức tương phản là lựa chọn biên tập.
- Bài 13, b8-3: ごろ và ぐらいに đều diễn đạt giờ gần đúng.
- Bài 15, b4-4: 知りません và 知っていません đều có thể diễn đạt không biết.
- Bài 20, b7-1: 何時？ và 何時だ？ đều là lối hỏi thân mật.
- Bài 20, b7-2: 休み？ và 休みだ？ đều là lối hỏi thân mật.
- Bài 20, b8-1: phương án còn lại là mảnh câu đáp cùng nguồn.
- Bài 20, b8-6: phương án còn lại là mảnh câu đáp cùng nguồn.
- Bài 20, b8-8: phương án còn lại là mảnh câu đáp cùng nguồn.
- Bài 40, b6-1: phương án còn lại là thành phần khác của cùng một đáp án.
- Bài 40, b6-2: phương án còn lại là thành phần khác của cùng một đáp án.
- Bài 40, b6-3: phương án còn lại là thành phần khác của cùng một đáp án.
- Bài 49, b5-6: お見になる và ご覧になる đều là kính ngữ đúng.
- Bài 49, b6-5: お見になる và ご覧になる đều là kính ngữ đúng.
- Bài 50, b2-2: お用意します và ご用意します đều được dùng.


## Tái tạo

Chạy `py -X utf8 scripts/renshuu_drill_round2.py` từ thư mục `minna-n5-n4`. Script tạo đủ 50 file `authored/renshuu-drills/lesson-NN.json` và báo cáo `reports/renshuu-drill-round2.json`. Bộ B chính `authored/renshuu/lesson-NN.json` được đọc để tránh trùng `source_id`; script này không sửa bộ chính.

## Giới hạn QA

Cặp đáp án được so với prompt, chỉ dẫn nhóm và bank lựa chọn đã lưu; mục mơ hồ bị giữ pending. Bản này là nháp biên tập AI cho root kiểm độc lập trước xuất native. `eligible_markup_text_review_candidates` không phải số câu có khóa chắc.
