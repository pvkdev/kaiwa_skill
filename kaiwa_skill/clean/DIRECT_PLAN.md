# Chuyển sang xử lý một lượt PDF → knowledge

Yêu cầu mới ngày 2026-11-11 thay kế hoạch chạy hai lượt cho toàn bộ kho. Đích vẫn là bản sách Nhật–Việt đầy đủ, giữ mạch riêng, ví dụ, bài tập, đáp án và đặc trưng của mỗi sách.

1. Raw đã đầy đủ: dùng fork-knowledge, tiếp tục checkpoint hiện có; không bỏ công việc đã làm.
2. Raw đang làm: giữ nguồn/checkpoint, không chạy trùng. Coordinator kiểm manifest/claim thật để tiếp tục hoặc xử lý vấn đề; không tự coi raw partial là đủ.
3. PDF chưa bắt đầu: dành cho kaiwa-pdf-knowledge; không khởi tạo raw mới. Snapshot kiểm kê ban đầu: 30 sách, 4597 trang, 16 đã khởi tạo raw, 14 chưa khởi tạo. Kiểm lại khi nhận sách vì số liệu có thể thay đổi.
4. Viết contract và công cụ PDF-native: PDF hash, page/block evidence, coverage, units/search, checkpoint dependency, resume và audio inventory; không giả tạo raw provenance.
5. Pilot một worker trên một phần sách Wakaru_Bijinesu_Nihongo.pdf (152 trang); chốt phạm vi sau khi xem ảnh. Root kiểm độc lập toàn bộ phạm vi theo cùng chuẩn clean. Lỗi pilot phải sửa output và skill trước khi PASS.
6. Sau PASS, mở full direct cho sách chưa chạy; worker khác tiếp tục clean nguồn hoàn chỉnh. Root nghiệm thu, commit từng output và giao tiếp sách kế tiếp cho tới hết phần xử lý được; sách thiếu/mờ nguồn được ghi rõ, không bù nội dung.
7. Bổ sung danh mục CD/audio cho cả bản clean cũ và mới, kèm bằng chứng trang và trạng thái file thực tế. Không coi thông tin CD là đã có audio.

## Vai trò và giới hạn thực tế

Người dùng yêu cầu 1 sub điều phối + 3 sub worker, tất cả gpt-6-sol/high. Runtime chỉ cho 4 tác nhân active tính cả root: giữ bốn vai sub nhưng luân phiên, tối đa ba sub active cùng lúc. Sub điều phối phụ trách công cụ/hàng đợi/handoff khi active; khi ba worker cùng chạy thì root nhận điều phối. Không mở chat mới hoặc giả định đã có bốn sub active. Writer một sách duy nhất; reviewer chỉ đọc và gửi lỗi cho writer sửa.

Các author trước khi đổi luồng đang dừng ở checkpoint: roleplay trung cấp, BJT本文冊. Reviewer roleplay đã kiểm một phần, cần kiểm hash trước khi tiếp tục. Không bỏ hoặc ghi đè công việc này.

## Nghiệm thu

PASS pilot phải có đối chiếu ảnh thật và output, giữ toàn bộ phạm vi và audio evidence; script pass chỉ kiểm cấu trúc/hash. Full chỉ hoàn thành sau khi đủ coverage, xử lý mọi omission, review có giới hạn rõ và ghi các thiếu sót nguồn. Báo cáo dừng/resume lưu xuống đĩa; không gửi final chỉ để thông báo đã khởi chạy.
