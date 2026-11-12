# Hợp đồng metadata ngắn

Mỗi packet chỉ rõ `book_id`, đường dẫn nguồn, hash và danh sách chapter_id. Annotation JSON UTF-8:

```json
{
  "book_id": "B01",
  "source_sha256": "hash từ packet",
  "purpose": "Sách giúp người học làm gì; tối đa khoảng 50 từ.",
  "strengths": ["thế mạnh có căn cứ"],
  "methods": ["cách học/học liệu thật sự có"],
  "knowledge": ["cụm từ", "sắc thái"],
  "level_source": "nhãn sách ghi, hoặc chưa thấy trong packet",
  "levels": ["sơ", "trung"],
  "level_note": "Ước lượng sơ bộ, có thể trộn mức độ.",
  "chapters": [
    {
      "chapter_id": "B01-C01",
      "kind": "lesson",
      "summary": "Khoảng 8–18 từ, mô tả nội dung thực sự thấy.",
      "topics": ["topic/ngữ dụng có mặt"],
      "levels": ["sơ", "trung"]
    }
  ]
}
```

- `kind`: `lesson`, `front`, `reference`, `answers`, `publication`. Bao phủ tất cả chapter_id, kể cả chương phụ, để mục lục đủ.
- `levels`: tập con của `sơ`, `trung`, `thượng`; được để rỗng nếu không đủ căn cứ hoặc phần không mang level. Mục tiêu là tra cứu, không cần rubric/điểm hoặc giải thích từng ví dụ.
- Topic chương: thường 1–5 cụm ngắn nếu có nội dung học; chương dày có thể nhiều hơn để không mất miền lớn. Tên mục/chương và các leaf label chi tiết đã có trong source_index, không sao chép hàng trăm nhãn vào annotation.
- Tách topic/chức năng khỏi loại học liệu. “Shadowing” thuộc methods; những việc đối thoại nói tới nằm ở topics. “Roleplay” không tự chứng minh mọi phần đều business; xem mục cụ thể.
- Không gộp các companion thành một sách; ghi công dụng riêng của 本文冊/練習冊/英訳・語い冊. Giữ nguồn thiếu/mờ ở manifest, không tự loại sách khỏi 27.
- Chương mục lục/chỉ mục/phương pháp học không được gán tất cả topic trong đó như nội dung bài học mới; dùng kind tương ứng. Nội dung bài học mới được tổng hợp trong TOPICS_ALL.
- Có thể dịch/khái quát nhãn sang Việt để tìm kiếm, nhưng không viết tình huống hoặc kiến thức chưa có bằng chứng. Mức không rõ ghi rõ trong level_note hoặc summary.
- Không tạo ví dụ, câu Nhật mới, bài giảng, thiết kế curriculum, log đọc từng dòng hoặc phân tích level từng câu ở bước này.
