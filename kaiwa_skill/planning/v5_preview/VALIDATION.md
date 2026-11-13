# Kiểm tra bản preview — 13/11/2026

- 120/120 đề xuất gốc có đúng một bản đánh giá; 13 phương án riêng; 16 mô-đun du lịch.
- 110 ID thẻ duy nhất, 110 tên duy nhất; mỗi thẻ có 6 seed tình huống. Kiểm tên chỉ phát hiện trùng chữ; ranh giới gần nghĩa được đánh giá biên tập trong từng thẻ và kế hoạch thu hẹp chặng mẹ.
- 104 phương án bổ sung/tách = 52 bổ sung + 52 tách; 4 làm rõ chặng cũ và 2 để sau không cộng vào 104.
- Các ID chặng cũ, đích gộp, mã sách và mã bằng chứng đều phân giải được.
- 28 cửa sổ nguồn có đường dẫn, số dòng và hash đoạn khớp file clean hiện có; điều này kiểm con trỏ, không chứng minh tính đúng ngữ nghĩa hay ảnh PDF.
- Khung gốc vẫn 194 UID duy nhất, 645 seed; hash JSONL và registry khớp snapshot. Không ghi lại lộ trình V4.1.
- HTML chạy thử bằng Node với DOM tối thiểu: render 110 thẻ, tìm tiếng Việt không dấu, lọc P1/quyết định, chuyển 120 đánh giá và 16 bối cảnh đều đạt. Chưa kiểm hiển thị thực trong trình duyệt.
- Mọi thẻ vẫn `authoring_ready=false`; tình huống là `editorial_proposal_not_book_transcription`.

## Tái kiểm và cập nhật

Chạy từ gốc repo:

```powershell
py -B -X utf8 kaiwa_skill/planning/v5_preview/render_preview.py
```

Mặc định chỉ kiểm, không ghi. Sau khi sửa dữ liệu/EDITORIAL.md có chủ đích, thêm `--write` để dựng lại các Markdown dẫn xuất, stats.json và PREVIEW.html. Không sửa bảng thống kê hoặc HTML riêng vì sẽ lệch dữ liệu.

Nguồn chỉnh thẻ là `candidates.jsonl`; quyết định đủ 120 ý ở `review_ai120.jsonl`; ý riêng ở `own_additions.jsonl`; địa danh ở `travel_modules.json`. Nếu đổi đích gộp/tách cần sửa các file tương ứng cùng nhau. Không đổi snapshot để bỏ qua thay đổi khung gốc: phải đối chiếu lại trước.

Chưa tạo UID V5, chưa thay skill nội dung, chưa chạy pilot hoặc sinh bài. Lượt tiếp theo cần phản hồi chọn/loại/gộp các ID V5P, rồi mới quyết định khung V5.
