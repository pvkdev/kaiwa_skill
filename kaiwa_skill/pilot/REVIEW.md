# Nghiệm thu pilot — PASS

- Ngày: 2026-11-10 (Asia/Tokyo).
- Skill: 0.1.2, commit `037615b` (gồm công cụ từ `4668d40`).
- Xây dựng và rà soát: Astra/high. Chuyển đổi: hai worker Sol/high tuần tự, `pilot_sol_a` và `pilot_sol_b`.
- Sách: `book/BJT/Shigoto_no_nihongo_Denwa_Outai_Kisohen.pdf`, đường dẫn tương đối từ kaiwa_skill.
- Book ID: `shigoto-no-nihongo-denwa-outai-kisohen-dfdb0e2b61e0`.
- SHA-256 PDF: `dfdb0e2b61e0322252532c2a83a7c4c5d62269b45edb40ae61eb5e3c32b74711`.
- Phạm vi: trang PDF 20–23, tương ứng trang in 18–21; sách có 162 trang. Không nghiệm thu toàn sách.

## Đối chiếu nội dung

Astra mở ảnh gốc cả bốn trang và đối chiếu toàn bộ Markdown: câu mẫu, lựa chọn, đáp án và giải thích, script, CD 1/2, hướng dẫn monologue/roleplay, gạch chân, tham chiếu ghi chú ①–⑤ và bảng từ vựng 8 hàng × 4 ngôn ngữ.

Không phát hiện lỗi chép chữ hoặc thiếu nội dung trong phạm vi đã kiểm tra. Ba lựa chọn giống nhau ở bài nghe p21 đúng theo bản in. Ô tiếng Trung của 統轄 trên p23 in `总括，全全负责的・・・`; giữ nguyên hai chữ 全, không sửa theo suy đoán. Không tạo thêm nội dung audio.

Rà soát đầu phát hiện bốn nhãn do AI thêm chưa phân biệt rõ với nguyên văn. Astra sửa quy tắc trong skill 0.1.2; Sol sửa nhãn trên p20/p21/p23, ghi nhận và xác nhận lại. Astra đọc bản cuối và kết luận PASS. Nội dung nguồn không thay đổi trong lần chỉnh nhãn này.

## Khả năng tiếp tục

Worker A hoàn thành p20–p21, lưu checkpoint và release claim. Worker B có ngữ cảnh mới đọc HANDOFF, xác nhận các hash hiện hữu, claim và tiếp tục p22–p23. Hai Markdown và hai ảnh đã hoàn tất trước bàn giao giữ nguyên hash trong phép thử. Chi tiết tại `RESUME.md`.

Đây là bàn giao sạch, không phải thử kill process thực. Các lỗi ghi dở, state lệch file, lock bị hỏng và nội dung bị sửa được mô phỏng riêng bằng kiểm thử tự động trên dữ liệu tạm. Các hash bàn giao cũ trong RESUME là bằng chứng tại thời điểm phép thử; lần chỉnh nhãn sau đó được ghi rõ riêng.

## Kiểm tra công cụ và dữ liệu

- 21 unittest đạt trên bộ công cụ hiện tại, bao gồm atomic write, checkpoint lệch sau lỗi, dữ liệu hỏng, PDF thay đổi, quyền sở hữu, lock ghi dở, build lỗi thời, issues và asset bị sửa.
- Hai skill vượt kiểm tra frontmatter và cấu trúc bằng quick_validate.
- Status cuối: 4 verified, 158 pending, không issue, không claim còn giữ, `build_current: true`.
- `book.md` mang nhãn INCOMPLETE; `search.jsonl` có 15 khối với mã khối, ngữ cảnh, nguồn và nội dung.
- Toàn kho: 30 PDF, 4.597 trang; mới 4 trang verified, 4.593 trang pending.

## Hash Markdown được nghiệm thu

- p0020: `01b92c723296d439beee964bc4e2e30041b4b5fbc5e9c893b02680abdee6b0ea`
- p0021: `ae20fdde838ed0f164eba2141ba0fcbfcd5c7c30b1324a50eae4b37943b3269c`
- p0022: `6f5fb4bbe051a3b1dd028baca742bc7be2e4c00b5615da034a3ac46b46bee486`
- p0023: `95bd3f6b27ee710ab3bda92b3e24336548f29a5e7fe8a397dfe8cd158a7c7924`

Ảnh và bằng chứng theo trang nằm trong thư mục corpus của sách. Thay đổi các nội dung này phải kiểm tra lại; báo cáo PASS này không tự mở rộng cho phiên bản khác.

## Điều phối sản xuất

Pilot đủ điều kiện để dùng hệ thống điều phối đã cấu hình: hai worker Sol/high song song, một PDF cho mỗi worker, checkpoint theo trang; Astra/high xử lý thay đổi skill và nghiệm thu. Chưa chạy toàn bộ kho trong phiên pilot này. Khi chạy production, mỗi sách vẫn phải đối chiếu đầy đủ và nghiệm thu riêng, commit output riêng.

Giới hạn: bốn trang thuộc một sách scan không bao phủ mọi kiểu bố cục trong 30 PDF; review bằng AI vẫn có thể bỏ sót lỗi. Script xác minh cấu trúc/hash và hồ sơ tự khai đã đọc ảnh, không tự chứng minh độ đúng ngữ nghĩa. Không có điểm tin cậy phần trăm được suy diễn từ OCR.
