# Chuẩn nội dung khả đọc và truy xuất

Markdown UTF-8. Nguồn chuẩn là từng trang. Mã `book_id:pNNNN` và anchor khối `pNNNN-bNNN` ổn định khi chỉnh chính tả; không đánh số lại khối cũ chỉ để làm đẹp.

## Khung trang

```markdown
# [book_id] — PDF p0007

- Trang in: 5 (hoặc không có/không đọc được)
- Đường dẫn nội dung: Chương / Unit / tiêu đề (chỉ ghi phần xác nhận được)

<a id="p0007-b001"></a>
## Tiêu đề đúng theo sách

Nội dung nguyên văn...
```

Không dùng placeholder trong output thật. Metadata điều phối, trạng thái và review nằm ngoài nguyên văn. Nội dung nguồn phải được phân biệt với nhãn cấu trúc do người chuyển đổi thêm.

Nhãn mô tả không in trên sách phải ghi rõ `(biên tập)`, kể cả nhãn bằng tiếng Nhật. Ví dụ: `Chữ trong hình (biên tập): 営業部`, `Tiêu đề lề (biên tập): 電話を受ける／第一声`. Nếu trang sau không lặp lại tiêu đề ノート, có thể đặt `## Ghi chú tiếp từ trang trước (biên tập)`; không trình bày tiêu đề tự thêm như nguyên văn nguồn. Các trường metadata quy định sẵn ở đầu trang đã là metadata, không cần lặp nhãn.

## Tiếng Nhật và hội thoại

- Câu Nhật giữ nguyên chuỗi từ, dấu câu và ngôn ngữ của sách, không chèn cách đọc vào giữa từ. Furigana ghi ở dòng riêng `Furigana (nguồn): 漢字＝かんじ` theo thứ tự và khối tương ứng; chỉ ghi cách đọc sách thật sự in.
- Tách mỗi lượt thoại thành một đoạn `**A:** ...`; dùng đúng vai nguồn, không đặt tên mới. Nếu không có nhãn, ghi rõ nhãn do biên tập thêm trong ghi chú riêng.
- Giữ câu chưa kết thúc ở cuối trang; dùng ghi chú nối trang riêng, không tự hoàn thành câu.
- Giữ romaji, dịch Việt/Anh hoặc ngôn ngữ khác nếu có trong sách; không thêm bản dịch.
- Giữ số bài, mã track, mũi tên mang ý nghĩa, ô trống và lựa chọn. Không giải bài thay người học.

## Bảng và hình

- Bảng dùng Markdown nếu bảo toàn được các ô. Bảng phức tạp có thể dùng HTML tối thiểu hoặc danh sách ghi rõ nhãn cột; không làm mất quan hệ hàng/cột.
- Hình có chữ phải phiên âm chữ đọc được; hình mang nghĩa lưu crop trong assets và liên kết tương đối. Mô tả AI có nhãn `Mô tả hình (biên tập)` và không thay thế ảnh.
- Nội dung không đọc được: đánh dấu `[không đọc được: vị trí]`, ghi issue, không cho verified.
- Giữ header/footer hữu ích (tên unit, trang, tham chiếu). Các yếu tố trang trí có thể mô tả trong review, không giả làm nội dung văn bản.

## Tìm kiếm

`book.md` có ranh giới trang và liên kết nguồn. Chỉ mục JSONL lưu book_id/page/block hoặc đoạn, đường dẫn nguồn và nội dung đầy đủ của đoạn. Không chỉ lưu tóm tắt; không thay nguyên văn bằng từ khóa AI. Không tách giữa hai vai trong cùng đoạn hội thoại nếu có thể tránh. Bản gốc không bị normalize NFKC; normalization nếu dùng chỉ thuộc chỉ mục phụ và phải ghi rõ.
