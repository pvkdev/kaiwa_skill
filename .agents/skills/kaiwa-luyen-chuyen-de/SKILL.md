---
name: kaiwa-luyen-chuyen-de
description: Soạn và kiểm tra ví dụ luyện nói V10 cho từng bài trong 72 chặng chuyên đề Speak Japanese, dựa vào các tình huống của chặng topic phía sau trên lộ trình V9.2.
---

# Soạn ví dụ luyện thêm trong chặng chuyên đề

Mỗi ví dụ thuộc về một bài cụ thể trong chuyên đề. Người học vừa hiểu cách nói sẽ có ngay lời để luyện và gặp lại cách nói ấy trong một tình huống sắp học.

## Đọc đầu vào

1. Từ gốc repo, chạy `py -X utf8 .agents/skills/kaiwa-luyen-chuyen-de/scripts/practice.py sj-so-01` với mã chặng được giao. Công cụ đọc thứ tự thật trong `planning/v9_2/learner.json` dưới `kaiwa_skill`, lấy các topic tiếp theo đến chuyên đề kế hoặc hết level. Kết quả có sự kiện, vai, nhánh và UID của từng tình huống. Các liên kết `prior_applications` là gợi ý từ lần tuyển bài.
2. Mở `lesson.md`, `source_raw.md`, `manifest.json` trong thư mục `bundle` được trả về. Đọc từng bài và đoạn nguồn của nó, xác định người nào nói với ai, mục đích, sắc thái, biến thể và ví dụ đã có. Một cặp trao đáp là một ví dụ. Gộp các dòng cùng một cảnh khi kiểm kê.
3. Đọc danh sách tình huống phía sau. Với từng bài, chọn cảnh trong đó người nói **có lý do tự nhiên để dùng** cách nói này. Ưu tiên cụm liền sau. Nếu cụm gần thiếu cảnh phù hợp, xem topic gần kế tiếp cùng cấp, thêm `--extra-topic T-xxx` để đọc và ghi một câu lý do ở `extra_topic_reasons`. Chọn tình huống theo UID, vì mã cục bộ như S002 lặp ở nhiều topic.

## Chọn lượng và viết

- **Mặc định bổ sung 3 ví dụ/bài**. Điểm bắt đầu cho một mẫu linh hoạt là một câu dùng ngay, một đoạn ngắn có lời đáp, một biến thể đổi quan hệ hoặc kết quả. Với cụm đáp, quán ngữ hoặc cảm xúc mà tách khỏi lời dẫn sẽ mơ hồ, có thể dùng cả ba đoạn đối thoại. Hội thoại thường 2–4 lượt, câu đơn phải nói được độc lập trong bối cảnh đã nêu.
- Điều chỉnh xuống 2 khi các ví dụ nguồn đã phủ tốt hoặc chức năng rất hẹp. Lên 4 khi có điểm đáng luyện riêng như đổi người được tôn kính, hiểu nhầm rồi sửa, hoặc hai cách đáp khác hẳn. Đây là khoảng định hướng. Chỉ thêm khi người học có thêm một quyết định giao tiếp để luyện. Nhắm mỗi bài có khoảng 4–6 ví dụ dùng được tính cả phần hiện hữu khi phù hợp. Phần bổ sung đặt liền sau bài gốc và có thể luyện từng ví dụ riêng.
- Viết lời thoại mới từ nhiệm vụ thực tế. Ví dụ ở `sj-so-01`, mục B07-146 dạy xin nhắc lại. Trong S-003/S002, lời vừa nghe là tên món. Câu đáp của nhân viên cần nhắc lại **tên món**, để người học có cơ hội nghe đúng thông tin vừa hỏi. Chuyển sang cảnh nhắc số tiền thì phải thay cả thông tin nghe thiếu và lời xác nhận.
- Sơ ưu tiên mỗi lượt có một ý, câu đáp ngắn, dễ bắt chước. Trung luyện nêu hoàn cảnh, hỏi lại chi tiết và xử lý điều kiện. Thượng luyện hàm ý, lập trường và thay đổi sắc thái qua lời đáp. Chọn độ khó theo người học và tình huống. Với kính ngữ, kiểm riêng người thực hiện hành động và người được kính trọng. Với câu dễ gay gắt, phân đúng vai để người học cũng luyện cách **đáp lại** câu đã nghe.
- Mỗi câu Nhật có bản Việt tự nhiên, đúng quan hệ, thái độ và ý định. Viết tiếng Nhật dùng được cho TTS, không thêm furigana. Tên level, mã sách và mã tình huống chỉ ở metadata. Phân biệt lời của hai vai, chỉ định giới tính giọng đọc. Các ví dụ mới mang tác giả `ai_authored`; giữ bản nguồn, bản biên tập và hash V9.2 làm căn cứ.

## Giao dữ liệu

Mỗi worker ghi `kaiwa_skill/planning/v10/stages/<stage_code>/practice.json`. Dùng UTF-8 và cấu trúc sau. Ví dụ minh họa cấu trúc bên dưới dùng ký hiệu thay cho UID thật.

~~~json
{
  "stage_uid": "<uid chuyên đề>",
  "items": [{
    "item_id": "sj-so-01-b07-146",
    "practice": [{
      "id": "sj-so-01-b07-146-ex01",
      "authorship": "ai_authored",
      "type": "dialogue",
      "topic_uid": "<uid topic liền sau>",
      "situation_uid": "<uid tình huống thật>",
      "context_vi": "Ở quầy ăn, khách nghe chưa rõ tên món.",
      "speakers": [
        {"id": "A", "role_vi": "Khách", "gender": "female"},
        {"id": "B", "role_vi": "Nhân viên", "gender": "male"}
      ],
      "turns": [
        {"speaker_id": "A", "ja": "すみません、料理の名前、もう一度いいですか。", "vi": "Xin lỗi, anh nhắc lại tên món giúp tôi được không ạ?"},
        {"speaker_id": "B", "ja": "親子丼です。", "vi": "Dạ, món cơm gà trứng ạ."}
      ]
    }]
  }]
}
~~~

`single_sentence` dùng một vai và một lượt. `dialogue` dùng hai vai và các lượt theo thứ tự nói. `items` bám đúng ID và thứ tự selections. Giữ ID ví dụ qua các lần sửa. Nếu cần mở rộng phạm vi topic, thêm object cấp gốc `extra_topic_reasons`, với key là mã topic và value là lý do.

## Rà soát và bàn giao

Worker đọc thành tiếng hoặc đọc nối các lượt, đối chiếu ngược từng ví dụ với **cả** cách dùng của bài và tình huống đã chọn. Xem câu đáp có xử lý đúng điều vừa nói, hai vai có nhất quán, bản Việt có nói được ngoài đời và các ví dụ có lặp nhau khi chỉ thay tên hoặc danh từ. Khi mẫu dành để nghe hiểu, kiểm tra lời đáp của người học có phù hợp.

Chạy `practice.py <stage_code> --check <practice.json>` sau từng chặng. Lệnh kiểm ID, thứ tự, liên kết, vai, bản dịch có mặt và kịch bản trùng nguyên chuỗi trong chặng. Người biên tập chịu trách nhiệm về độ tự nhiên và sát nghĩa. Hoàn tất từng file rồi mới chuyển sang chặng kế. Khi resume, kiểm file đã có và rà trạng thái bàn giao trước khi viết tiếp.

Khi người dùng giao chạy hàng loạt, ba worker chia theo level và theo thứ tự chặng. Điều phối ghép phần luyện vào từng selection của **bản xuất V10** theo `item_id`, cho HTML đọc chính JSON xuất. Hiển thị bối cảnh, câu Nhật–Việt và vai ngay dưới bài tương ứng. Metadata nguồn và liên kết QA ở phần nội bộ. Kiểm đủ 18/36/18 chuyên đề và 81/156/85 bài, kiểm cả 365 chặng và thứ tự cũ, kiểm trùng giữa các bài gần nhau, mở thử bài có câu đơn và bài có đối thoại ở mỗi cấp. Báo số bài, ví dụ, lượt nói, tình huống đích và trường hợp cần rà. Phát hành V10 sau lượt nghiệm thu này.
