# Clean hàng loạt — đang điều phối

Đã chốt **20/30 bản đọc**, bao phủ **2.475/4.597 trang PDF đầu vào**. Bảy bản đầu được rà độc lập toàn phạm vi; mười ba bản sau tác giả đối chiếu toàn nguồn và root QA mẫu. [Bản đọc và hồ sơ](../knowledge/README.md).

Bản vừa chốt: **にほんごで働く！ビジネス日本語30時間**,181 trang/15 chương/171 unit,commit62fd98b. Root QA40 trang mẫu và validate strict0 lỗi/0 cảnh báo. Giữ đủ8 bài chính, đáp án/script, chỉ mục395 hàng theo audit của writer và tập từ riêng20 trang;1CD/57 nhãn01–57,file chưa kiểm.

5500 câu136 trang đã chốt trước đó (6f689ed), còn66 vấn đề nguồn tại60 trang; xem cảnh báo trong bản đọc, không coi toàn bộ là câu Nhật đã xác nhận.

Ba bản trước: Shadowing 初～中級編145 trang (dca0eff,411 hội thoại/950 lượt Nhật–Việt,root34 trang mẫu); 電話応対 基礎編162 trang (49b0926,root27 trang, nguồn83 cắt ghi chú); 発展文型125225 trang (89f4c0f,root29 trang và bảng125 dòng, nguồn120 thiếu một lượt Nhật). Mạch bài, chức năng bài nghe, bản Việt và tham chiếu đã được sửa qua QA; các lỗi nguồn vẫn được cảnh báo.

Ba worker Sol/high tiếp **Roleplay tiếng Nhật thương mại sơ–trung** (227 trang,đang khởi tạo theo sách), **Shadowing trung–cao bản Indonesia–Thai–Việt** (168 trang,đã xong Unit1–5), và **お決まり表現180** (209 trang). Còn7 PDF chưa giao. Runtime4 active tính root nên sub điều phối idle trong lúc ba worker viết.

Root đã mở31 trang mẫu của Shadowing trung–cao và13 của180. Hai sách giữ vấn đề nhãn vai nguồn lần lượt ở70 và53, không tự đổi lời/nhãn. Báo cáo và checkpoint nằm trong clean/reviews và từng_meta. Chưa tính hai sách đang dở là nghiệm thu.

Công cụ0.4.10:80 test fork+17 direct PASS. Regression18 bản trước: **0 lỗi/33 cảnh báo**, gồm vấn đề nguồn và9 cảnh báo bố cục ô trống đã kiểm củaNama2. Skill đã thêm kiểm bản Việt in sẵn và giữ mô tả giọng của script ở sau đề nghe. 5500 mới validate riêng0/132. Validator không chứng minh đúng nghĩa hoặc đủ kiến thức.

[CD, băng và nguồn nghe](../knowledge/AUDIO_INDEX.md) có inventory và tình trạng file tách riêng; chưa tìm/tải audio. [COORDINATOR](COORDINATOR.json) giữ hàng đợi; [HANDOFF](HANDOFF.md) giúp tiếp quản. Checkpoint giúp nối sau gián đoạn; không có daemon khi đóng ứng dụng. Lượt điều phối còn tiếp tục.
