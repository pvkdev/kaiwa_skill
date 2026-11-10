# Rule 06 – Nhân vật: mỗi video một bộ mặt mới

Mỗi video có nhân vật riêng, **không có nhân vật chính cố định**. Người xem gặp người mới ở mỗi bài, cảnh đời thường đa dạng
(văn phòng, ga tàu, tiệm ramen, phòng gym, bệnh viện…), không phải lúc nào cũng "du học sinh Việt ở Nhật".

## Cách chọn nhân vật (bắt buộc, không tốn token)

1. `python tools/nguon.py bat-dau …` (Bước 1 của `WORKFLOW.md`) in sẵn gợi ý; muốn xem lại thì chạy `python tools/pick_cast.py <ID>`.
   Công cụ chọn từ kho `core/cast.json` bộ gồm: nhân vật chính (tên, giới, nghề, nét tính cách, ngoại hình), một nhân vật phụ và bối cảnh;
   nó tự tránh những tên đã dùng ở mục 1 của các bài trước.
2. Dùng tên nhân vật chính cho **mục 1 (mở màn) và câu Kết**. Các gợi ý khác là lựa chọn tham khảo, không phải danh sách phải đưa vào lời kể.
   Không dùng lại tên ở mục "đã dùng" mà công cụ in ra.
3. Đổi hoặc bỏ gợi ý về nghề, người phụ, bối cảnh khi nó **không phục vụ logic và ý muốn nói** của bài (vd không đưa bà chủ nhà vào cuộc phỏng vấn chỉ vì được gợi ý).
   Nếu cần đổi cả tên nhân vật chính, chọn tên khác trong `core/cast.json` hoặc tự đặt tên **chưa từng dùng**; ghi lý do vào Ghi chú biên tập.
4. Không có Python → tự chọn một tên trong `core/cast.json` chưa xuất hiện ở mục 1 của bất kỳ bài nào trong `work/`.

Tên trong ví dụ chuẩn (`core/examples/…`) chỉ là minh họa định dạng – **không chép lại** tên, nghề hay bối cảnh của nó.

## Quy tắc viết

- Tình huống mở màn và câu Kết dùng cùng một nhân vật chính.
- Cách đưa nhân vật vào lời kể theo `02_giong-van.md`, mục "Mở bài và kết bài". Không bắt buộc giới thiệu nghề, ngoại hình hoặc nhân vật phụ.
  Nếu cần giữ gợi ý ngoại hình cho biên tập, ghi trong Ghi chú; NotebookLM tự dựng hình từ hành động và hoàn cảnh có trong Kịch bản.
- Tên người Việt chỉ dùng tên gọi ngắn (vd "Yến", không "Trần Hải Yến"), nhất quán trong cả bài; không viết họ tên đầy đủ để giới thiệu nhân vật.
- Các Tình huống của từng ví dụ có thể đổi người, đổi nơi; tên mới tự đặt, tránh trùng với nhân vật chính của chính bài đó.
- Không ép tình huống cho vừa nhân vật; nét tính cách phải phục vụ ngữ pháp của bài.
- Không gán tính cách tiêu cực nặng nề (gian dối, bạo lực) cho nhân vật.
- Câu tiếng Nhật trong bài gốc có tên riêng (vd 山田さん) → giữ nguyên tên trong câu Nhật.
- Tên chỉ viết chữ Latin trong phần tiếng Việt (được phép theo `04_tieng-nhat.md`); trong câu Nhật theo bài gốc.
