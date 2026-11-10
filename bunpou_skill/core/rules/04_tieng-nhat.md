# Rule 04 – Quy tắc về câu tiếng Nhật

## Chữ viết

- Dùng chữ Nhật chuẩn: kanji + kana như sách giáo trình. Dấu câu Nhật: `。`, `、`, `？`, `！`, `「」`.
- Cấp N5–N4: hạn chế kanji ngoài danh sách cấp độ; có thể viết kana thay cho kanji khó (vd `ごはん`, `ともだち`).
- Ký hiệu mẫu: dùng `〜` (U+301C) và gạch chéo toàn góc `／` khi liệt kê biến thể: `〜ところに／へ／を／で`.
- Số trong câu: viết như bài gốc (vd `３億円`).

## Không ghi cách đọc – 2 dòng trên màn hình: câu Nhật / câu Việt

- Mọi câu Nhật hiện trên màn hình đi theo đúng 2 dòng: **câu Nhật gốc** ở trên → **câu Việt** ở dưới.
- **Không** dòng cách đọc hiragana, **không** furigana, **không** ghi cách đọc trong ngoặc sau kanji ở bất kỳ đâu.
- Kịch bản **không có ký hiệu ruby 《 》, ｜, 【 】** – NotebookLM chép nguyên ký hiệu lên màn hình (validate.py báo LỖI).
- Câu Nhật dùng kanji/kana như sách giáo trình theo cấp độ (mục "Chữ viết" ở trên); người xem nghe cách đọc qua lời giảng.

## Tô màu mẫu ngữ pháp

- Câu Nhật để sạch; phần cần tô màu ghi ở dòng riêng `**Tô màu:**` (câu mẫu, ví dụ và câu kết), chép **đúng y** đoạn mẫu trong câu Nhật.
- Chỉ ghi **chính mẫu ngữ pháp** (なんて, とは, ところに…), không ghi cả câu. Phần chia/nối phía trước (だ, な, の, đuôi động từ)
  không ghi: câu `静かだなんて` → Tô màu `なんて`.
- Kèm dòng `**Tô màu Việt:**`: cụm nghĩa tương ứng trong câu Việt, chép đúng y (video tô cùng màu). Có ở ví dụ, câu mẫu, câu kết.
- Câu mẫu trong phần Ý nghĩa có dòng Tô màu như ví dụ. Câu "Người Nhật thường nói" không cần Tô màu.
- Câu bẫy (mục 4) không có dòng Tô màu (mẫu của bẫy khác mẫu chính, không tô để khỏi nhầm).

## Tên mẫu khi giảng

- Tên mẫu luôn nói bằng tiếng Nhật, không phiên âm Việt hóa kiểu "tô cô rô ni".
- Dòng `**Mẫu:**` mục 2 ghi tên mẫu đúng như bài gốc (chuẩn hóa ký hiệu 〜 và ／).

## Romaji

- **Không có romaji trong file Kịch bản.** Romaji chỉ dùng cho ID thư mục và slug tên file.
- Được phép viết chữ Latin cho: tên nhân vật (Minh, Yuki, Tanaka…), tên riêng/thương hiệu, từ mượn đã quen trong tiếng Việt (flan, radar, karaoke), và "JLPT".
  Không được phiên âm câu hay từ tiếng Nhật bằng romaji.
- Món ăn, đồ vật Nhật trong phần tiếng Việt: dùng tên tiếng Việt ("tôm chiên") hoặc chữ Nhật (`天ぷら`), không viết romaji.

## Câu tự nhiên

- Chọn thể thường hay thể lịch sự (です・ます) theo quan hệ giữa các nhân vật và hoàn cảnh nói trong tình huống, như người Nhật thật sẽ nói.
- Không pha thể thường và thể lịch sự trong cùng một câu.
- Ví dụ `[MỚI]` phải qua tự kiểm: "Người Nhật bản ngữ có nói đúng câu này trong tình huống này không?" Không chắc → viết câu khác.
