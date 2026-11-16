---
name: kaiwa-speak-japanese-roadmap
description: Phân bổ trọn pack của tám sách Speak Japanese vào các chặng chuyên đề V7 có tên, cấp độ, thứ tự pack và vị trí trong lộ trình Kaiwa. Dùng khi lập kế hoạch, pilot, phân bổ hoặc chỉnh một chuyên đề.
---

# Xếp pack Speak Japanese vào lộ trình

Đọc [kế hoạch V7](../../../kaiwa_skill/planning/v7/PLAN.md) và [hợp đồng phân bổ](references/allocation.md). Sản phẩm của pha này là từng chặng chuyên đề có tên và danh sách pack theo thứ tự. Việc phối hợp nội dung, dựng flow giảng, viết hội thoại và sản xuất video thuộc pha biên soạn sau.

## Đọc và phân cấp từng pack

1. Kiểm kê từ tám catalog V6.3 của B06, B07, B11, B12, B18, B19, B20, B24. Một khóa gồm book_id và pack_id. Ghim nguồn, dải dòng, extra_parts và hash. V6.4 cung cấp lịch sử gán. V6.5 cung cấp thứ tự topic hiện hành. B05 dành cho kiến thức tình huống dịch vụ, B08 thuộc nguồn shadowing topic.
2. Mở toàn bộ pack, kể cả tài liệu bổ trợ, ghi chú, cặp cách nói và ví dụ ở bối cảnh khác. Giữ nguyên đơn vị, lời Nhật và thứ tự nội dung trong từng phần. Ghi một nhận xét ngắn về kiến thức chính, sắc thái, người nói/người nghe và độ khó thực tế. Một pack có nhiều nghĩa vẫn đi nguyên vẹn tới nơi học.
3. Đề xuất level phù hợp với lần học đầu. Xét độ khó của cả pack, độ tinh tế khi nghe và quan hệ giữa người nói. Nhãn sơ–trung của B07/B11, trung–thượng của B06/B12 là gợi ý tìm vùng đặt. Có thể đưa cùng pack nguyên vẹn vào nhiều level khi lần học sau giúp ôn đúng lúc hoặc nhận ra sắc thái mới. Mỗi lượt đặt có lý do, dùng chung khóa nguồn.

## Nhóm, đặt tên và chọn vị trí

- Nhóm các pack có điểm chung có thể gọi tên được, chẳng hạn cùng cách mở lời, cùng quan hệ giao tiếp, hoặc hai cách biểu đạt đáng đặt cạnh nhau. Có thể dùng một hay nhiều sách, hoặc để một pack thành chuyên đề riêng. Đánh giá độ phù hợp của toàn pack. Chấp nhận những ví dụ phụ thuộc các topic khác.
- Xếp thứ tự giữa các pack theo lý do người học hiểu được, như cách dùng quen thuộc trước rồi tới biến thể tinh tế, hoặc trường hợp cơ bản trước rồi mới đối chiếu cách dùng. Giữ mỗi pack thành một mục riêng trong danh sách. Chỉ cần ghi lý do sắp xếp ở cấp nhóm.
- Đặt tên tiếng Việt cụ thể, tự nhiên, bao được điểm chung của các pack. Đọc tên rồi kiểm từng pack có thực sự thuộc tên đó. Nếu tên chỉ đúng với ví dụ mở đầu hoặc quá rộng như “Các cách nói hay”, thử tên khác hoặc đổi nhóm. Giữ mã, tên sách và số mục trong admin.
- Chọn cấp và vị trí cụ thể trong thứ tự 289 topic. Xem cả hàng xóm trước và sau. Ưu tiên đặt trước topic sẽ dùng được khi vừa tầm. Ghi liên kết tới tình huống cụ thể nếu có căn cứ. Chuyên đề độc lập có thể đặt theo vốn kiến thức đã có, độ khó, nhu cầu ôn hoặc nhịp học của cụm. Một vị trí hợp lý với danh sách ứng dụng rỗng là hợp lệ.
- Khi review, đọc liên tiếp các tiêu đề topic và chuyên đề rồi mở danh sách pack của từng chuyên đề. Chỉnh vị trí có thể chỉ cần đổi điểm chèn. Tên, UID và nguồn có thể quản lý độc lập với thứ tự hiển thị.

## Bao phủ, phân công và phục hồi

Mục tiêu là đặt toàn bộ tài nguyên hiện có của tám sách. Pack bổ trợ cần có nơi dùng cụ thể. Nếu cách nhóm ban đầu không hợp, thử đổi nhóm, đổi level hoặc để chuyên đề độc lập. Ngoại lệ chỉ dùng khi đưa vào thực sự bất hợp lý; ghi khóa, lý do và phương án đã cân nhắc. Phân biệt ngoại lệ với trang nguồn thiếu và với quyết định còn dở. Một pack có thể xuất hiện nhiều lần nhưng chỉ tính một lần khi báo độ phủ.

Khi được giao chạy nhiều worker, chia lượt đọc theo sách, lưu từng phiếu theo khóa nguồn. Root đối chiếu các ứng viên toàn kho rồi điều phối lượt đặt theo cấp, tránh hai worker ghi chung registry hoặc thứ tự. Lưu checkpoint nguyên tử, kèm hash đầu vào và danh sách cần duyệt. Sau gián đoạn, đọc tiếp phiếu dở hoặc nguồn đã đổi. Root kiểm toàn vẹn nguồn, UID, thứ tự, tên chuyên đề và ngoại lệ rồi build, kiểm preview và commit release. Lệnh thiết kế hoặc pilot chỉ triển khai đến phạm vi được giao.
