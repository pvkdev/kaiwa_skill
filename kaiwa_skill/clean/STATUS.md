# Clean hàng loạt — đang điều phối

Kế hoạch hiện hành: [DIRECT_PLAN.md](DIRECT_PLAN.md). Raw đầy đủ tiếp tục clean; chưa có raw đầy đủ thì PDF-direct theo phân công, giữ raw dở làm tài liệu phụ chỉ đọc. Đã có9bản đọc đủ779trang PDF đầu vào; catalog30PDF vẫn đang xử lý. Các mốc bên dưới là snapshot, dùng resume/state thật khi tiếp quản.

Người dùng yêu cầu một sub điều phối và ba worker, tất cả `gpt-6-sol/high`; runtime chỉ cho ba sub active cùng root nên luân phiên vai. Root giữ lượt điều phối, QA và Git; chưa hoàn thành catalog30 PDF.

## Đã có bản đọc và rà độc lập

Bảy nguồn đầu có501 trang PDF, đã build/validate và rà ảnh/raw/clean toàn phạm vi bởi tác nhân khác tác giả hoặc kết hợp reviewer/root. Mỗi sách có hồ sơ chỉ rõ những phần được rà và sửa sau review; không đồng nghĩa mọi nhận xét trong bản in đã được xác minh ngoài sách.

- 日本語生中継 初中級編1:91 trang,13 chương,253 unit; bản Việt đã làm rõ vai và giữ nhánh lựa chọn.
- 日本語生中継 中～上級編:89 trang,11 chương,122 unit; Bài8 kết thúc PDF87.
- Bảng880 từ N3:47 trang; đủ880 dòng. Bốn gloss English được dịch Việt có log; năm cụm nghĩa nguồn còn cần xác minh ở360/543/632/636/682.
- MINATO checklist1160 từ:8 trang; thiếu STT460/có1161 đúng nguồn, không tự thêm cách đọc/nghĩa.
- Kính ngữ 基本表現85:93 trang,9 chương,116 unit;164 đáp án Nhật có Việt đã được root QA. PDF thiếu trang in106–107/bài14;15 unit còn vấn đề nguồn.
- Bảng1170 từ N1:70 trang; STT1132 khôi phụcきっちり（と） theo ảnh, khác raw có log. Hai nghĩa nguồn1159/1165 còn needs_review.
- 日本語でビジネス会話 中級編〈英訳・語い冊〉:103 trang,21 phần,145 unit; thoại English-only dịch Việt, không dựng Japanese. Các chênh lệch nguồn được giữ riêng.

Pilot 基本文型88 chỉ PDF7–12:4 chapter,9 unit; đã khôi phục CD01–03/trang mở PART1/mạch hội thoại trước giải thích/MEMO. Root mở lại đủ6 ảnh và rà bản sửa; vẫn pilot_partial, không gọi full sách.

## Hai bản full mới: tác giả đối chiếu toàn sách, root QA mẫu

- Roleplay trung cấp140trang:10chương/109unit, commit689603f. Root QA16trang mẫu, inventory1CD/15mã track. Chưa full independent semantic review.
- 本文冊138trang:22chương/128unit, commit42b8667. Root QA10trang mẫu. Rebase provenance chỉ4anchor/dòng trống trong raw tổng hợp; toàn138rawpages và nội dung chapter không đổi, snapshot/history cũ được giữ. Build/validate0/0. Chưa full independent semantic review.

## Đang chạy

- `/root/knowledge_coordinator`: đã bàn giao direct/needs_review/rebase;17test direct +35test fork PASS. Đang idle để ba worker chạy.
- `/root/clean_keigo`: full direct なめらか日本語会話163trang, đã hết23bài và index tớiPDF153, đang đáp án154–162. PDF32/chapter05 needs_review vùng chữ in bị che; không dùng ghi tay làm đáp án, các phần khác vẫn tiếp tục.
- `/root/clean_namachuukei_sho`: full direct わかるビジネス日本語152trang từ pilot PASS; cùng thư mục/history,21chapter. Đã hết45Scene tớiPDF129, đang phụ lục130–148; chapter đáp án draft chờ150–151, không giả complete.
- `/root/clean_namachuukei_chu`: full direct 練習冊148trang, tận dụng23trang raw cũ; đã qua Bài13/PDF97, đang Bài14. Không sửa corpus/claim cũ.

Mọi nghiệm thu dựa hash hiện tại và phạm vi review được ghi rõ. Book88 đã chuyển PDF-direct có history (commit1c2d7c0); giữ byte4chapter/9unit và scope7–12. Công thức nguồnPDF9 vẫn needs_review; chưa mở full96trang. Worker kế dùng extend-scope, không init/reset.

Pilot trực tiếp đã giữ45key lựa chọn,21câu Drill và65mảnh đáp án ôn có Việt; đã sửa bản Việt từng lượt bài tập và hai nghĩa/cách viết. Báo cáo `_meta/pilot-independent-review.json` trong thư mục Wakaru. Các bản toàn sách vẫn cần checkpoint/QA riêng; không suy full acceptance từ PASS pilot.

Bản đọc: [knowledge/README.md](../knowledge/README.md). Ownership và hàng đợi: [COORDINATOR.json](COORDINATOR.json). Tiếp quản: [HANDOFF.md](HANDOFF.md). Phiên bị đóng sẽ dừng tính toán; checkpoint/snapshot hỗ trợ mở lại từ chỗ đã lưu, không có daemon nền.
