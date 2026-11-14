# Nghiệm thu chuyển PDF sang knowledge

Đã chuyển đủ **156 trang PDF vật lý** thành **20 chương, 219 unit** Nhật–Việt; build `book.md`, chỉ mục `search.jsonl` và nguồn trang/block. Đây là bản chuyển đủ PDF được cung cấp, còn hai vấn đề ngay trong nguồn; không xác nhận toàn bộ nội dung đã sạch hoàn toàn.

- Tên xác nhận từ PDF156: **シャドーイング 日本語を話そう 就職・アルバイト・進学面接編 インドネシア語・タイ語・ベトナム語訳版**. Không lấy nhan đề từ filename. ISBN978-4-87424-719-8; 2016年11月25日 第1刷発行; 株式会社くろしお出版.
- Tác giả được phân công đã mở ảnh từng trang trong phạm vi của mình: A1–50, B51–105, C106–152; root153–156. Chỉ render ảnh hoặc chạy script không được tính là đọc trang.
- Root đối chiếu 52 trang, trong đó 48 trang là mẫu kiểm độc lập phần của worker;4 trang do root biên tập trực tiếp. Ngoài ra kiểm tập trung POINT tại PDF44/60/78/88, không tính thành mẫu rà toàn trang mới. Phạm vi và hash ở `coordinator-review.json`/`root-qa-progress.json`.
- Ba lượt kiểm chéo độc lập bổ sung18 trang: B kiểm A44–49; C kiểm B78–83; A kiểm C126–131. Hợp mẫu kiểm độc lập là **66 trang**, không phải kiểm độc lập toàn156 trang. Findings và followup giữ riêng theo hash và phạm vi thực đọc; các chỉnh sau review được root kiểm lại phần ảnh hưởng.
- Đã sửa các lỗi được phát hiện: nhãn vai ngoại lệ, bỏ sót lời đáp/chuyển máy; từ/giờ bản Việt in sai; kana/kanji hoặc trợ từ bị tự chuẩn hóa; ý hướng dẫn bị rút; điều kiện ở POINT; sắc thái悔しい/くじけずに; placeholder Việt phải giữ chỗ trống tương ứng.
- My Page giữ nguyên ô trả lời chưa điền; ba bảng từ ngữ giữ8/12/11 mục theo Unit và7 thuật ngữ làm thêm củaUnit1. Không tự tạo đáp án, hội thoại hay nội dung cho trang thiếu.
- Audio:2 nhãn DISC,55 mã phân biệt nhìn thấy trong PDF. DISC2/23 bao gồm đuôi simulation1 và simulation2; giữ đúng ranh giới nguồn. Chưa kiểm tệp nghe thực tế.

## Giới hạn nguồn và trạng thái

PDF bắt đầu ở trang in25: không có bìa, mục lục và phần đầu của ấn bản giấy. Không bổ sung từ suy đoán. PDF32 chuyển giữa専門学校/大学; PDF106 có câuIndonesia bị đứt mạch. Hai vùng giữ `needs_review`, có cảnh báo trong bản đọc và [`source-issues.md`](source-issues.md).

Kiểm tra full bằng `direct_progress.py validate ... --allow-source-issues`: **0 lỗi,4 cảnh báo cho2 vấn đề** (mỗi vấn đề được ghi ở page vàunit). Không có trang/chương pending,draft,stale;18 chương author_checked,2 chương needs_review do nguồn. Trạng thái `full` xác nhận phạm vi PDF, không xóa cảnh báo nguồn. Script kiểm cấu trúc/hash, không thay việc đối chiếu nghĩa.

## Khôi phục và hồ sơ

`direct-state.json` chứa checkpoint nguồn/trang/chương; `coordination.json` ghi cách chia việc. `worker-reports/` giữ sổ biên tập, checkpoint gốc và báo cáo kiểm chéo; tênchapter của cache tương ứng trực tiếp với chapter chính. `pilot-review.json` và `pilot-snapshot/` lưu bằng chứng5 trang đã PASS trước khi mở rộng; `scope-history/` giữ lịch sử mở rộng, không init/reset ghi đè. `book.md` chỉ được sinh từ chapters.

## Rà riêng hướng dẫn trước chốt

Ba tác giả rà lại toàn bộ POINT/hướng dẫn của phần mình, tập trung phủ định, điều kiện và mức bắt buộc. Đã sửa trước commit một chỗ đảo nghĩa `答えずに` ở PDF34 cùng các chỗ bị rút ý; root mở nguồn xác nhận các phần thay đổi. Phạm vi ở `focused-guidance-review.json`; đây là lượt tác giả tự rà, không tự nâng thành kiểm độc lập toàn sách.
