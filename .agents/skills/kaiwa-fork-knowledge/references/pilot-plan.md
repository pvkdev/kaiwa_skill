# Pilot fork — sách 基本文型88

Đọc [hợp đồng đầu ra](output-contract.md) trước khi thực hiện. Tài liệu này chỉ chốt phạm vi và bố cục riêng cho pilot.

## Phạm vi và điểm dừng

Nguồn thô hiện tại: `kaiwa_skill/corpus/669041168-4f47df1cc97a/`; PDF hiện tại: `kaiwa_skill/book/Kaiwa/669041168-日本語会話-基本文型８８.pdf`. Tên sách trên bìa PDF p0001 đã được author pilot xác nhận là `わかる！話せる！日本語会話 基本文型88`; nếu tái dùng pilot, kiểm lại bằng ảnh bìa. Chỉ làm PDF p0007–p0012: phần mở đầu p0007–p0009 và PART1 bài 1–3 ở p0010–p0012. PDF p0009 có trang mở PART1 ở panel phải; không tự gọi đó là bài 1. Xác nhận trang in từ ảnh; raw ghi p0007=12–13, p0008=14–15, p0009=16 + trang mở PART1 không số, p0010=18–19, p0011=20–21, p0012=22–23, nhưng đây chỉ là chỉ dẫn tìm trang trước khi xem ảnh.

Pilot đạt khi bốn đơn vị được đối chiếu hai chiều (PDF → chapter để tìm sót; chapter → PDF để tìm thêm/sai), lời Nhật và bản dịch Việt đúng nghĩa/sắc thái, nguồn truy ngược được đến raw anchors, mọi điều chưa chắc được nêu trong `_meta`, và reviewer độc lập đã kiểm lại. Không gọi toàn sách đã clean hoặc tự mở rộng full: các trang khác nằm ngoài phạm vi pilot.

## File pilot

```text
kaiwa_skill/knowledge/<tên sách xác nhận trên bìa>/
  chapters/
    00-mo-dau.md
    01-ne.md
    02-yo.md
    03-yone.md
  book.md                         # root build nối bốn chapter theo thứ tự
  _meta/
    book.json                      # root viết
    units.jsonl                    # author viết, một dòng JSON mỗi unit
    search.jsonl                   # builder tạo từ unit
    editorial-log.md              # author: quyết định lọc/dịch và điểm chưa chắc
    pilot-review.json              # author: đối chiếu trang/khối đã thực hiện
    independent-review.md          # reviewer độc lập
```

Pilot sau rà bảo toàn có chín unit: `u-intro-01`–`u-intro-05`, `u-part1-opening`, `u-part1-01`, `u-part1-02`, `u-part1-03`; khớp `unit_id` trong `_meta/units.jsonl`. `_meta/book.json` có `scope.pdf_pages: [7,8,9,10,11,12]`, `scope.chapters` theo thứ tự bốn file trên, `status: "pilot_partial"`. Trang in/panel có thể thêm vào metadata sau khi đối chiếu ảnh; nếu khác raw, ghi nguyên nhân. Các unit chỉ dùng tra cứu, không cho phép đổi thứ tự dạy của sách. `u-part1-opening` giữ trang mở PART1 ở panel phải PDF9 trước Bài1; không bỏ như trang trí. Mã CD01/02/03 của Bài1–3 được giữ. MEMO của Bài2 nằm sau tám lượt luyện như nguồn.

## Rà soát theo nội dung

- Mở đầu: giữ các cách mở lời, khoảng cách, kiểu câu nói chưa trọn, phong cách và biến đổi phát âm đúng nguồn. Không biến nhận xét của sách thành quy tắc phổ quát mới.
- Bài 1–3: giữ hội thoại Nhật, ví dụ Nhật, mẫu, A/B/C, phần thực hành, MEMO và phân biệt sắc thái `ね`, `よ`, `よね`. Giữ mạch nguồn: hội thoại mở đầu, phần ý nghĩa/cách dùng, mẫu, điểm lưu ý rồi bài thực hành; không chuyển giải thích lên trước hội thoại vì template. Dịch từng lời thoại/ví dụ sang Việt; nếu bản dịch Anh/Trung trong sách mâu thuẫn câu Nhật, ưu tiên câu Nhật/PDF và ghi quyết định vào log. Mã track có chức năng luyện nghe được giữ hoặc dẫn rõ, không bỏ như dấu trang trí.
- Hình có ý nghĩa: diễn đạt bối cảnh hoặc quan hệ mà hình bổ sung cho câu/mẫu. Không chép mô tả hình thô kiểu vị trí trái/phải, màu sắc, hoặc lệnh nhìn hình khi chi tiết ấy không giúp hiểu kaiwa.
- PDF p0009 in công thức `～では→～ちゃ` nhưng ví dụ `来てはだめ→来ちゃだめ`. Đây là mâu thuẫn trong nguồn, không phải lỗi OCR nếu ảnh xác nhận như vậy; giữ ví dụ và ghi issue, không lặp công thức đáng nghi như quy tắc chắc chắn.
- Kết thúc pilot: root chạy builder rồi validator theo [hợp đồng đầu ra](output-contract.md), đọc cảnh báo và kiểm lại bằng mắt. Validator không thay thế đối chiếu ngữ nghĩa.

## Rà bảo toàn sau pilot ban đầu

Bản rà lại được ghi ở `_meta/preservation-recheck.md` và `_meta/preservation-independent-review.md`. Review cũ được giữ như lịch sử, không xác nhận các chapter đã đổi. `book.json.completion.independent_preservation_review` ghi hash và phạm vi sáu trang được rà lại; trạng thái vẫn `pilot_partial`, không mở rộng thành toàn sách.
