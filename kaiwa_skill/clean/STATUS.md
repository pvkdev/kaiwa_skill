# Clean hàng loạt — đang điều phối

Đã có12bản đọc đủ phạm vi1242trang PDF đầu vào trên catalog30PDF/4597trang. Các vùng nguồn thiếu/che vẫn được đánh dấu; không phục dựng bằng suy đoán. Bản đọc và giới hạn QA: [knowledge/README.md](../knowledge/README.md).

Bảy bản đầu501trang đã rà độc lập toàn phạm vi. Năm bản mới do tác giả đốichiếu toàn sách và root QA mẫu: roleplay140,本文冊138,Nameraka163,Wakaru152,練習冊148. Hồ sơ từng sách ghi rõ phạm vi, không gọi tất cả là full independent semantic review.

練習冊 đã khôi phục/audit toàn chú từ chân trang, releasea90b875. Công cụ0.4.7 có62test fork+17direct PASS, regression12bản0lỗi; chỉ2cảnh báo nguồn Nameraka32 đã biết. Kiểm cấu trúc không thay kiểm nghĩa.

## Ba writer hiện tại

- clean_keigo: full96trang 基本文型88, đã tớiPDF68, đang69–76; giữ sourceissues9/28. Front/PART1/Warm-up/chươngđộngtừ/danhtừ/tínhtừ/đầucâu đãcheckpoint. Bảnbook.md cònbuildpilot cũ khi fullchưađủ.
- clean_namachuukei_sho: full136trang しごとの日本語 ビジネスマナー編, đã tới119, đangUnit19từ120. Nguồn cóphụđề mờ23/69, mảnhcâu28 và thiếu trang in104–105 giữaPDF105/106. Giữ dữliệu còn đọc được và bối cảnh ấn bản2015.
- clean_namachuukei_chu: full152trang 日本語生中継 初中級編２, gồm本冊+別冊 scripts/từvựng/đápán; đã tới27, đangBài3từ28. Cover ghi2CD, đã ghi tracks1-2…1-17; file nghe chưa kiểm.

Subcoordinator knowledge_coordinator idle sau xử lý công cụ. Runtime cho4active tínhroot nên luân phiên bốn vai sub, tất cảSol/high. Ngoài ba sách active còn15PDF chờ; root tiếp giao việc sau bàn giao, chưa hoàn tất toànkho.

[CD/băng/nguồn nghe](../knowledge/AUDIO_INDEX.md) có inventory và trạng thái file riêng. Một số hồ sơ cũ rà giới hạn; unknown không nghĩa không cóaudio. Chưa tìm/tải tệp nghe.

Mốc trên làsnapshot; [COORDINATOR.json](COORDINATOR.json) là hàng đợi/phân công, [HANDOFF.md](HANDOFF.md) là hướng dẫn tiếp quản. Đóngapp dừngtính toán, checkpoint/hash/history giúp nối lại từ phần còncurrent. Không tạo daemon/automation.
