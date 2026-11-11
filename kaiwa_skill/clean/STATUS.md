# Clean hàng loạt — đang điều phối

Đã có **14/30 bản đọc**, bao phủ **1.474/4.597 trang PDF đầu vào**. Bảy bản đầu được rà độc lập toàn phạm vi; bảy bản sau do tác giả đối chiếu toàn nguồn và root QA mẫu. Vùng nguồn thiếu, mờ hoặc mâu thuẫn vẫn được ghi rõ, không đoán phục dựng. Xem [bản đọc và giới hạn QA](../knowledge/README.md).

Hai bản vừa chốt: ビジネスマナー136 trang, commit8a162ca; 基本文型88 đủ96 trang, commitc0c4dc1. Root kiểm100/100 ký hiệu đáp án của Manners và48 câu ôn/đáp án của88. Hồ sơ từng sách phân biệt rõ author review với QA độc lập mẫu.

Ba worker Sol/high đang tiếp: 発展文型125 (225 trang), 電話応対 基礎編 (162 trang), 日本語生中継 初中級編２ (152 trang). Còn13 PDF chưa được giao; root tiếp tục giao khi có bàn giao. Bốn vai sub được luân phiên vì runtime chỉ cho4 active tính cả root; sub điều phối hiện idle, ba worker đang viết.

Công cụ0.4.7 có62 test fork và17 test direct PASS. Regression13 bản trước release88:0 lỗi,12 cảnh báo nguồn đã biết;88 kiểm riêng0 lỗi/4 cảnh báo nguồn. Kiểm cấu trúc không chứng minh đúng nghĩa hoặc đủ kiến thức.

[CD, băng và nguồn nghe](../knowledge/AUDIO_INDEX.md) có inventory và tình trạng file riêng. Một số hồ sơ cũ mới rà giới hạn; unknown không có nghĩa sách không có audio. Chưa tìm hoặc tải file nghe.

[COORDINATOR.json](COORDINATOR.json) ghi snapshot hàng đợi/phân công; [HANDOFF.md](HANDOFF.md) hướng dẫn tiếp quản. Checkpoint/hash/history lưu xuống đĩa để nối lại sau gián đoạn. Đóng ứng dụng dừng tính toán; không có daemon hoặc automation chạy riêng.
