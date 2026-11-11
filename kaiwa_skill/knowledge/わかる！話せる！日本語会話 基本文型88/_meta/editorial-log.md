# Nhật ký biên tập pilot

## Phạm vi nguồn đã đối chiếu

- Bìa PDF trang vật lý 1 xác nhận tên sách: `わかる！話せる！日本語会話 基本文型88`.
- PDF trang vật lý 7: mục mở đầu 1–2, trang in 12–13.
- PDF trang vật lý 8: mục mở đầu 3–4, trang in 14–15.
- PDF trang vật lý 9: mục mở đầu 5 ở panel trái, trang in 16. Panel phải là trang mở PART1 không in số; không đưa vào chương mở đầu.
- PDF trang vật lý 10: PART1 bài 1 `～ね`, trang in 18–19.
- PDF trang vật lý 11: PART1 bài 2 `～よ`, trang in 20–21.
- PDF trang vật lý 12: PART1 bài 3 `～よね`, trang in 22–23. PDF 13 bắt đầu bài 4, ngoài phạm vi pilot.

## Quyết định chuyển đổi

- Giữ nguyên câu Nhật trong hội thoại, ví dụ, các mẫu và cặp biến âm; bỏ furigana, phiên âm Latin, CD, tiếng Anh/Trung lặp nghĩa, số trang trong thân bài, ô điều hướng và dấu trang trí. Đoạn giải thích được viết lại bằng tiếng Việt dựa chủ yếu trên phần Nhật, đối chiếu phần Anh và ảnh PDF khi cần.
- Dịch từng ví dụ hoặc lượt nói sang tiếng Việt ngay dưới câu Nhật. Nhóm A/B/C của mỗi bài được giữ đúng nguồn. Phần hình có ý nghĩa ở PDF 7 (trình tự mở lời, khoảng cách) và PDF 10 (hai người ăn donut) được chuyển thành mô tả tình huống tự nhiên; không giữ chỉ dẫn xem ảnh.
- Mục mở đầu 3, ba văn phong: theo đoạn Nhật và Anh, ① là cách lịch sự, ② là thân mật, ③ là cách rất trang trọng, chủ yếu dùng trong câu cố định hoặc phục vụ khách hàng. Phần Trung trong raw đảo số ① và ② ở một câu; fork không dùng câu đảo này.
- PDF 11, ghi chú N/NA bỏ `だ` trước `よ` được giữ với quy thuộc “sách ghi”, vì đây là nhận xét về sắc thái nữ tính trong nguồn; không mở rộng thành quy tắc xã hội chung.
- Dấu `＊` trước `帰ろう` và `いやになる` là dấu nối tới MEMO, không phải chữ trong lời thoại. Nội dung hai MEMO được giữ bằng tiếng Việt.
- Phần đầu bài 2 lặp nguyên câu tiêu đề `もう帰ったよ` trong ngoặc, nên không tạo một ví dụ mới hay một phép biến đổi giả.

## Vấn đề nguồn cần lưu ý

- **PDF 9 / trang in 16 / `p0009-b005`:** ảnh crop cho thấy sách in `～では→～ちゃ`, nhưng ví dụ cùng dòng lại là `来てはだめ→来ちゃだめ`. Raw chép đúng cả hai. Fork giữ ví dụ Nhật và bản dịch, không khẳng định công thức mâu thuẫn. Cần đối chiếu biên tập nguồn nếu sau này muốn đưa công thức vào bản học.

## Giới hạn trạng thái

Đây là đối chiếu của tác giả pilot cho PDF 7–12, chưa phải rà soát độc lập. Các trang khác của sách nằm ngoài phạm vi này.

## Rà bảo toàn mạch sách — 2026-11-11

- Đã mở lại bìa và từng ảnh PDF7–12, đối chiếu với raw trong snapshot đã ghim `kaiwa_skill/source_snapshots/669041168-4f47df1cc97a/deca656ca2cb8343/135937d1`; không reset ledger hoặc đổi `source_markdown`/`source_pdf`.
- Quyết định cũ “bỏ CD” trong mục chuyển đổi ở trên **hết hiệu lực**: PDF10–12 đặt **CD 01**, **CD 02**, **CD 03** ngay đầu ba bài. Đây là mã track phục vụ luyện nghe, đã khôi phục trong từng chapter; không suy ra transcript âm thanh ngoài lời thoại in sẵn.
- PDF9 panel phải là trang mở **PART1 日本語会話の最重要文型８**, có chức năng chia phần trước Bài 1. Quyết định cũ loại `p0009-b007` **hết hiệu lực**; đã đưa tên phần vào đầu chapter Bài 1 và thêm unit `u-part1-opening` trỏ đúng anchor ấy. Không coi trang mở là Bài 1.
- PDF10–12 đều đặt hội thoại ví dụ trước phần `意味・使う場面`, `基本パターン`, `ポイント`, rồi mới đến `会話練習`. Các chapter Bài 1–3 trước đây đưa giải thích lên trước hội thoại; đã chuyển hội thoại về đầu, giữ toàn bộ A/B/C, tám mục luyện mỗi bài và MEMO ở cuối nơi có nguồn.
- PDF7 phần mở lời nêu cả khả năng người nghe tự nhủ “người nước ngoài nên đành vậy”. Đã khôi phục sắc thái này trong bản Việt. Các hình khoảng cách/cúi chào ở PDF7 và hai người ăn donut PDF10 đã có mô tả bằng text đúng chức năng; không cần output hình.
- Lệch công thức PDF9 `～では→～ちゃ` so với ví dụ `来てはだめ→来ちゃだめ` vẫn là issue nguồn. Giữ ví dụ, không nâng công thức thành quy tắc chắc chắn.
- Các review `pilot-review.json`, `independent-review.md`, `coordinator-review.json` và `resume-review.json` vẫn là hồ sơ lịch sử. Hash chapter/unit và kết luận độc lập cũ không còn xác nhận phiên bản đã sửa. Hồ sơ đối chiếu mới nằm ở `_meta/preservation-recheck.md`; cần root build/validate và review độc lập lại.

## Root independent preservation review — 2026-11-11

Root mở đủ PDF7–12, so chapter với ảnh. Khôi phục ý giải thích chiều cao/vóc dáng-vs-khoảng cách ở7 và lời dẫn nhiều văn phong ở8; đưa MEMO帰ろう của11 về sau tám lượt luyện đúng cuối trang. Các câu Nhật và mọi ví dụ giữ nguyên. Ghi preservation-independent-review.md; checkpoint intro và bài2 đã refresh. Review cũ chỉ là lịch sử, không nâng phạm vi pilot thành full.
