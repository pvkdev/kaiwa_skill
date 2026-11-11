# Rà bảo toàn pilot 基本文型88 — 2026-11-11

## Phạm vi và bằng chứng

Phạm vi không đổi: PDF vật lý **7–12**, bốn chapter `00-mo-dau.md`, `01-ne.md`, `02-yo.md`, `03-yone.md`. Đã mở lại ảnh bìa PDF1 để xác nhận nhan đề, rồi mở ảnh gốc từng trang PDF7–12 tại `kaiwa_skill/.cache/fork-pilot/page-NN.png`. So với PDF, raw snapshot ghim `kaiwa_skill/source_snapshots/669041168-4f47df1cc97a/deca656ca2cb8343/135937d1` và chapter theo cả hai chiều. Snapshot/PDF và scope cũ không thay đổi.

**SHA-256 ảnh đã mở:** bìa PDF1 `28d18c8de8809a76659fe242c33f019e0a42126bbd5940e864b5616f46f182c7`; PDF7 `e4c4acfca691a64f3ac725c5a1d25571ac086f7fae2cca504c604cd28e72444c`; PDF8 `3b9f9325b8b87668f56144873d595f9358889bac9c6472586499637fd5fecaac`; PDF9 `f547639c52cca5d469943cc7b309c0b2bc4f5fe2fbe43faf8506b6517ffc71ab`; PDF10 `99cdced4f6e493ff415ca0b999e97cf094c6d2661ca4d0343bcb25412056bb3c`; PDF11 `a845592fed2b51475e87825dade51f1166c5e55005013c677b5e17aecbf0f0c4`; PDF12 `636432e95ee45166769179fbe1de3f92f3382057a198005663df635b05be053a`.

**SHA-256 raw snapshot:** PDF7 `e8535712b1e2a0327c6c0f8cf1700d4b020bfba79b3c31cd284d45b10d965d33`; PDF8 `46d358d3fd9c2ef4ef03b8cab09148ac07a43ee185a03bf1ae89a720b886fef5`; PDF9 `5a828c66eb5b091267e3dc02d0ce89b821a351145973e613dedc7f0a80f4f922`; PDF10 `6c360a3976aff32a73cece7812b951e8a762827e90f33615fb214dda92ee2b29`; PDF11 `f60cb821171158015c1020b56df0fd37e3f6ac798f51c8b63419c7a93ee3f2a7`; PDF12 `ab795fd019fa93cdde375ba7e5caee38a55c683686b66b90ca4ae8ea22abdd06`.

| PDF | Trang in/panel | Nội dung và quyết định sau rà |
|---|---|---|
| 7 | 12–13 | Mở lời `あのう` → người kia đáp → mới hỏi; giọng dè dặt; khoảng cách cúi chào so với bắt tay; hình quan hệ được giữ bằng text. Khôi phục phản ứng được nguồn nêu “người nước ngoài nên đành vậy”. |
| 8 | 14–15 | Câu để mở ở `が`/`けど`, ba văn phong, bốn kiểu rút gọn và mọi ví dụ giữ đúng thứ tự. Không thấy mã CD hoặc bài tập bị thiếu. |
| 9 | 16 + trang mở PART1 không số | Giữ các cặp biến âm và ví dụ. Công thức `～では→～ちゃ` vẫn mâu thuẫn với ví dụ cùng dòng, giữ issue. Khôi phục trang mở **PART1 日本語会話の最重要文型８** qua unit `u-part1-opening`, trước Bài 1. |
| 10 | 18–19 | Bài 1: khôi phục **CD 01**; hội thoại donut A/B đứng trước giải thích; giữ mẫu, điểm lưu ý, ba nhánh A/B/C và đủ tám lượt luyện. Hình donut chỉ thêm tình huống hai người cùng ăn, không thêm lời. |
| 11 | 20–21 | Bài 2: khôi phục **CD 02**; hội thoại về trưởng bộ phận đã về đứng trước giải thích; giữ mẫu, ghi chú sắc thái N/NA bỏ `だ`, hai nhánh A/B, tám lượt luyện và MEMO số 4 về ngữ điệu `帰ろう↗`. |
| 12 | 22–23 | Bài 3: khôi phục **CD 03**; hội thoại lễ hội đứng trước giải thích; giữ mẫu, ba nhánh A/B/C, tám lượt luyện và MEMO số 8 về `いやんなる`. |

## Hiệu lực review

`pilot-review.json`, `independent-review.md`, `coordinator-review.json` và `resume-review.json` phản ánh bản trước lần sửa này. Các hash và kết luận ở đó **không còn xác nhận** chapter `00-mo-dau.md`, `01-ne.md`, `02-yo.md`, `03-yone.md` hiện tại, cũng như unit mới và `units.jsonl`. Hồ sơ lịch sử được giữ nguyên để truy vết. Sau checkpoint mới, trạng thái `author_checked` chỉ có nghĩa tác giả đã đối chiếu lại PDF7–12; cần reviewer độc lập kiểm lại phần sửa và root build/validate. Không mở rộng ngoài pilot.
