# Clean hàng loạt — đang điều phối

Đã chốt **25/30 bản đọc**, bao phủ **3.512/4.597 trang PDF đầu vào**. Bảy bản đầu được rà độc lập toàn phạm vi; mười tám bản sau writer rà toàn nguồn và root QA mẫu. [Bản đọc và hồ sơ](../knowledge/README.md).

Bản vừa chốt **どんどん話せる！日本語会話フレーズ大特訓 必須700**, commit836c853:208 trang/8 chương/110 unit;91 bài,727 ý luyện và727 hàng mẫu tương ứng,70 câu tra cứu. Root26 trang, toàn bốn cột khẩu ngữ và bảng70. Sau handoff root sửa hai ví dụ English thành hai cách diễn đạt thay thế thay vì tự gán cuộc hỏi đáp, recheckpoint/build/validate0lỗi/4cảnh báo. Hai vấn đề nguồn2/207 giữ: trang in2 vắng, niên hiệu/năm in mâu thuẫn. HaiCD/91mã bài học,guide12 lặpCD1/6 ghi riêng; filesnot_checked. Hash và giới hạn QA trong_meta/coordinator-review.

Hai bản trước là Roleplay sơ–trung227 trang (09c08fc,strict0/0,root33trang) và接客700225 trang (ae73d29,0/4cảnh báo iconvai178–179,root18trang). Mọi phần đáp án/script/bảng tra theo sách được giữ. 5500câu còn66 vấn đề nguồn tại60trang; không gọi mọi nội dung Nhật là đã sạch hoàn hảo.

Ba worker **gpt-6-sol/high** đang tiếp:

- **超ミニフレーズ200**:225 trang/13 chương; đã tới mục170/PDF187. Root22ảnh toàn trang (bao gồm preflight216/217),so nhiều mục và toànessay146. Root còn đối chiếu200crop góc audio:198mã mainthực in,hai mục100/200 khônglabel,hai guide12/13lặpCD1/16 khácmain22. Không suytrack100. Index218–223 và hậu sách phải đủ trước nghiệmthu.
- **Roleplay thương mại cao cấp**:198 trang/17 chương; đã qua10bài chính/PDF130. Root30ảnh,toàn bài1/6 vàfrontmẫu; các sửa logic/sơđồ/はず/JP修復/ngoặc đãđọc lại,writer rà các case. Cuối vẫn phải đủ biệt sách189–198 và hai trang đápán7–8 được tái lập đúng thứtự in.
- **気持ちが伝わる 日本語会話 基本表現180**:209 trang/24 chương,đãinit. Front1–12/Introduction13–18/19sectionsA–S19–199/Englishindex200–204/Japaneseindex205–207/colophon208–209. Có90Unit/180mẫu theo preflight,2mẫu/Unit vớiListen&Speak/Words và50cột văn hóa. Root mới3ảnh1/208/209. CoverCD付,chưa xác nhận sốđĩa.

Còn **2 PDF chưa giao**:210phát triển233 trang vàonomatopoeia180220 trang. Dự kiến worker200→210,Roleplay上級→onomatopoeia để tận dụng ngữcảnh; không giao trùng sách. Runtime4active tính root nên không tạo subđiều phối riêng khi3workerđangviết.

Công cụ0.4.10:80test fork+17directPASS. Regression18bản trước0lỗi/33cảnh báo; bảy bản mới được rootvalidate riêng. Chỉ sửa hướng dẫn skill về cue romaji và mã CD (eec34de/dda893e), không đổi code hoặc chạy lại test không cần thiết. Validator không chứng minh đúng nghĩa hoặc đủ học liệu.

[CD,băng và nguồn nghe](../knowledge/AUDIO_INDEX.md) tách thông tin in khỏi file thực tế; chưa tìm/tải audio. [COORDINATOR](COORDINATOR.json) giữ hàngđợi; [HANDOFF](HANDOFF.md) để tiếp quản. Checkpoint giúp nối sau gián đoạn; không có daemon khi đóng ứng dụng. Lượt điều phối tiếp tục tới đủ30PDF.
