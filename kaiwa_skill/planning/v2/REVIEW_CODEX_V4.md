# Review độc lập V4 và thiết kế skill dựng chặng

Ngày review: 2026-11-12. Phạm vi: KAIWA_CHANG_V4.md/.jsonl, KAIWA_SKILL_DESIGN_V1.md, hai plan V2/V2.1, chỉ mục và nội dung clean có chọn lọc. Bỏ qua nội dung V3 theo yêu cầu. Chỉ tạo file báo cáo này; không sửa nguồn, kế hoạch hoặc skill, không commit/push.

## 1. Kết luận

- **Có thể dùng V4 làm danh sách ứng viên để chỉnh sửa; chưa nên dùng làm đặc tả chạy sản xuất 200 thư mục chặng.**
- Vấn đề nghiêm trọng thứ nhất: nhãn nguồn và báo cáo phủ đang gây hiểu nhầm; có con trỏ sai nghĩa, năm cờ AI sai, hai báo cáo phủ 20/20 sai.
- Vấn đề nghiêm trọng thứ hai: chưa có hợp đồng đánh giá khả thi cho R2/R3/Live; điểm phát âm, đúng ý và đạt mục tiêu đang bị trộn.
- Vấn đề nghiêm trọng thứ ba: chưa chốt schema/ID/phụ thuộc/trạng thái dùng chung để rerun an toàn; nhân rộng sớm sẽ làm lỗi lan sang từ vựng, audio và tiến độ.
- Kiểm tra máy xác nhận 200 ID duy nhất, Sơ59/Trung79/Thượng62; 37 cụm và bảng số chặng theo 27 sách khớp. Kết quả này không chứng minh độ phủ ngữ nghĩa hay hiệu quả học.
- Đã mở nguồn clean cho **49 chặng**, 50 dòng đối chiếu: Sơ16/Trung17/Thượng16, Đời sống25/Công việc24; 21 chặng chỉ có tối đa hai con trỏ cả sources và banks.
- Chỉ nên làm pilot end-to-end nhỏ sau khi sửa chứng cứ nguồn và quy tắc đánh giá; xác minh quyền sử dụng text/audio trước phát hành app.

### Phương pháp và cách hiểu mức độ

“Nghiêm trọng” là vấn đề có thể làm sai học liệu/đánh giá hoặc gây mất tính toàn vẹn/quyền phát hành khi nhân rộng; không có nghĩa phần mềm đã chạy và phát sinh sự cố. “Quan trọng” là điểm cần sửa/chốt trước pilot hoặc mở rộng. Đây là review bản thiết kế, chưa phải kiểm thử runtime.

Nguồn đã mở là file chapters của các bản knowledge thật, không chỉ TOC/HEADINGS. Một con trỏ được ghi “đúng” chỉ nghĩa vị trí/chủ đề được đối chiếu có hỗ trợ phần được ghi; không xác nhận toàn chặng đã đủ nội dung, audio có sẵn hoặc mọi câu phù hợp level. Các bank rộng và tình huống AI được phân biệt với nguồn lõi; không gán lỗi con trỏ chỉ vì bank không bao trọn chặng.

## 2. Các phát hiện có bằng chứng

### A01 — 354 “tình huống có nguồn sách” và hai dòng phủ 20/20 không đúng dữ liệu

**Mức độ:** Nghiêm trọng. **Vị trí:** V4 §1, §5–6; JSONL toàn bộ.

**Bằng chứng:** [v4:25](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:25>) ghi 354 tình huống có nguồn sách. Phân loại từ sources thực tế: 213 có token Bxx, 136 chỉ có memo/NHK, 5 có literal AI nhưng ai=false; 320 còn lại ai=true. Như vậy 354 là số ai=false, không phải số tình huống có nguồn sách. [v4:684](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:684>) và [v4:685](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:685>) ghi B22/B23 20/20, nhưng mỗi tập chỉ có 19 token L, thiếu L17. Cả hai bài 17 tồn tại thật: [B22:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本語でビジネス会話 中級編 練習冊/chapters/17-keigo.md:1>), [B23:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/17-bai-17-kinh-ngu.md:1>). Các số chặng theo sách ở §6 lại khớp máy; lỗi nằm ở ý nghĩa/đơn vị của “phủ” và hai kết quả 20/20.

**Đề xuất:** Đếm riêng book-linked, memo-linked, AI-proposed và verified-used; tách nguồn lõi với bank. Tạo tập mẫu số có ID cụ thể, phép hiệu expected−linked và lý do skipped/reference. Ghi B22/B23 L17 là chưa gắn, hoặc bổ sung vị trí dùng thật. Không gọi token hiện diện là đã khai thác hay đã đọc sâu.

### A02 — Có con trỏ tồn tại nhưng bị gán sai tình huống

**Mức độ:** Nghiêm trọng. **Vị trí:** S-24, T-35, T-55, T-65, H-29, H-59.

**Bằng chứng:** [json:24](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:24>) gán B26:9 cho “nhường chỗ”; [B26:6](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/09-bai-9.md:6>) và dòng13–15 nói tặng/nhượng đồ không còn dùng. [json:94](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:94>) gán B21:L14 (+ B22/B23 L14) cho “Xin phép, xin nghỉ”; [B21:47](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本語でビジネス会話 中級編 本文冊/chapters/14-shotaimen.md:47>) là gặp tổng giám đốc lần đầu. [json:167](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:167>) gán B02:S44/S45 cho phát biểu tiệc cưới; [B02:137](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/15-挨拶する.md:137>) và dòng222 là phát biểu chia tay công sở. [json:197](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:197>) và [json:114](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:114>) dùng B18:P2-2 cho học thuật/giáo viên; [B18:58](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md:58>) là thư viện, còn trao đổi luận văn ở [B18:47](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md:47>) thuộc cảnh1. T-65 gán U4a cho xin thuốc, trong khi cảnh tương ứng đã mở ở [B13:316](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md:316>) thuộc U4b và là xin thuốc sau sáu tháng, không phải cấp thuốc dài hạn.

**Đề xuất:** Đổi/tách đúng từng con trỏ ở cấp tình huống; B26:9 chuyển sang nhận/nhượng đồ, giữ nhường ghế là nguồn khác hoặc AI; L14 chuyển sang làm quen/giới thiệu; S44/S45 chuyển sang chia tay/chuyển công tác; học thuật dùng P2-1/scene4. Với T-65 dùng đúng U4b/scene12 và sửa tên nhu cầu. Cho worker ghi source_span + câu tóm tắt bằng chứng để QA ngữ nghĩa, không chỉ validate token có tồn tại.

### A03 — Chưa có hợp đồng giải token thống nhất và nguồn quá thô

**Mức độ:** Quan trọng. **Vị trí:** T-34, T-59, T-60, H-17, H-20, H-31, H-46, H-49.

**Bằng chứng:** [json:93](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:93>) đồng thời có B12:A6 và B12:P2-A6. Sách thật có PART2 A⑥ ở [B12:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/わかる！話せる！日本語会話 発展文型125/chapters/13-part2-a-hitei.md:1>), nhưng không có registry giải hai alias. S16:STAGE1/2/3 lặp trong nhiều chương ở memo; S11:談話 lặp trong chín chương; bare S09 ở [json:184](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:184>) chỉ xác định được cả nguồn. HEADINGS_27 có file/dòng thật, nhưng không tự định nghĩa phép ánh xạ những alias này.

**Đề xuất:** Tạo registry token→book_id/chapter_path/anchor/source_hash/loại nguồn, chuẩn hóa alias có lịch sử. Với S16 phải có chương + STAGE + mục; S11 phải có chương + số談話; S09 ít nhất có số課. Đánh dấu unresolved/coarse thay vì validator coi đã hợp lệ. Không kết luận mọi alias là sai: nhiều alias nhận ra được theo mục lục nhưng chưa có hợp đồng máy đọc.

### A04 — Các chặng theo loại biểu đạt vẫn còn, trái tiêu chí ngân hàng cách nói

**Mức độ:** Quan trọng. **Vị trí:** T-44, H-40–H-42; V4 §0.

**Bằng chứng:** [v4:7](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:7>) tuyên bố các sách biểu đạt không thành chặng riêng nhưng tự cho ngoại lệ “Thành ngữ: người & thái độ”. [v4:401](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:401>) chia tình huống T-44 theo bốn PART ngôn ngữ học của B19; [v4:584](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:584>)–586 chia H-40–42 theo nhóm nghĩa trong B20. “Dùng với động từ”, “Chênh lệch”, “Điều kiện & diễn biến” là loại chất liệu, chưa phải tình huống có vai/mục tiêu.

**Đề xuất:** Rải B19 vào sức khỏe/thời tiết/miêu tả trải nghiệm và B20 vào kể chuyện/công việc/xung đột. Nếu giữ một chặng về kể hay nhận xét, đặt can-do thực và các bối cảnh độc lập; không giữ ba chặng chỉ để phủ A–Z. Không cần bù lại cho tròn 200.

### A05 — Bộ lọc kiến thức hữu ích cho nói chưa được thực thi nhất quán

**Mức độ:** Quan trọng. **Vị trí:** T-09, T-22, T-47; V4 §0, §5.

**Bằng chứng:** [v4:12](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:12>) nêu loại trang phục/tư thế và B03 U7/U9/U14. Dữ liệu [json:68](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:68>) vẫn trích U7/U9; [json:81](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:81>) còn tình huống “Tiếp đãi, ăn với khách & thứ tự chỗ ngồi” với U14. [v4:411](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:411>) tạo chặng Email/fax/văn bản; [B03:25](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/18-Unit16-ビジネスEメール.md:25>) chủ yếu là mẫu email, CC/BCC/giao diện, lại có cờ thiếu trang104–105 ở dòng5. [v4:687](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:687>) chỉ giải thích bỏ U2–4, khác danh sách bỏ trong §0.

**Đề xuất:** U14/phi ngôn ngữ chỉ làm ghi chú ngữ cảnh nếu cần, không tạo nhiệm vụ học nói. T-47 đổi mục tiêu sang gọi xác nhận đã gửi mail/nhờ sửa hoặc giải thích nội dung, dùng mẫu email làm đạo cụ; hoặc chuyển sang tham khảo. U7/U9 chỉ giữ đoạn nói có can-do cụ thể và ghi mục nào bị loại; bảo toàn cờ nguồn thiếu.

### A06 — Ranh giới chặng chưa đủ rõ để tránh dạy lặp và ghép nguồn cho đủ số

**Mức độ:** Quan trọng. **Vị trí:** T-19/T-23/T-24, T-25/T-27/T-28, T-65/T-66; H-03/H-19, H-58.

**Bằng chứng:** T-19 và T-24 cùng dùng B21:L8 du lịch công ty; T-19 và T-23 cùng phần tiệc của B13:U5a; T-65/T-66 cùng U4a y tế. Chưa có can-do phân biệt hay điều kiện đạt riêng trong JSON. H-03 có tình huống telesales trỏ đúng [B13:225](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/08-unit-8-hoi-thoai-dai.md:225>) nhưng xa trọng tâm hẹn khách của tên chặng; đây là lỗi đóng gói, không phải token sai. [v4:623](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:623>) ghép thuế/bảo hiểm/PTA với cửa hàng tiện lợi/máy bán hàng tự động từ S22:10.

**Đề xuất:** Đặt 3–5 can-do, phạm vi không gồm gì và khóa phân biệt mỗi chặng; một hội thoại có một nơi dạy chính, nơi khác ghi ôn/chuyển bối cảnh. Xem gộp nhóm T-19/23/24 hoặc tách rõ quà tặng–tổ chức tiệc–chuyến đi. Tách H-58 thành việc hành chính/tài chính và tham gia cộng đồng; chuyển tiện ích/vending sang mua sắm/đời sống, telesales sang chào bán. Chưa đủ bằng chứng nói các cặp trên trùng hoàn toàn.

### A07 — Có mạch liên hệ tốt nhưng chưa kiểm được phụ thuộc; một số cụm xen kẽ còn rời rạc

**Mức độ:** Quan trọng. **Vị trí:** V4 §2, 37 cụm; schema JSONL.

**Bằng chứng:** [v4:56](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:56>) xen T-01 nhà ở → T-02 chọn ngành → T-03 sharehouse → T-04 gặp tiền bối → T-05 thủ tục → T-06 hồ sơ: hai mạch song song nhưng chưa thấy nhiệm vụ nối. S-29 đã yêu cầu nghe điện thoại trong [json:29](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.jsonl:29>), trước S-36/38 dạy điện thoại công sở; S-40 ôn đi uống trong khi chặng công ty/sở thích còn ở S-46. JSON chỉ có chín trường, không có prerequisite, grammar/skill introduced/reused hoặc core/optional. Do đó chưa thể xác nhận trần ngữ pháp hay “mỗi cụm từ dễ đến khó”.

**Đề xuất:** Giữ liên hệ nhà hàng→ăn cùng đồng nghiệp, khám bệnh→báo ốm, khách→nhân viên. Với cụm hai mạch, nhóm thành tiểu mạch có điểm nối hoặc đặt một can-do chung có tình huống chuyển tiếp. Khai báo prerequisite tối thiểu theo kỹ năng/mẫu, không chỉ số thứ tự; chuyển tổng hợp sau những kỹ năng nó kiểm hoặc hạ yêu cầu/có hỗ trợ. Bảng rà 37 cụm ở §2.1 phân biệt đánh giá chủ đề với phụ thuộc chưa xác minh.

### A08 — Level của nguồn và level đích đang bị đánh đồng

**Mức độ:** Quan trọng. **Vị trí:** S-03; T-23/26/27/28/63/66; H-04; các chặng chỉ có tên 'nâng cao'.

**Bằng chứng:** [B13:56](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/00-bia-muc-luc-huong-dan.md:56>) nói section① khoảng N2, section② khoảng N1 theo lời sách. V4 dùng section① ở 25 chặng Trung, trong khi tiêu chí review đặt Trung≈N4–N3; section② ở Thượng N3–N2+ cũng cần điều chỉnh. [B21:33](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本語でビジネス会話 中級編 本文冊/chapters/01-jiko-shoukai.md:33>)–41 là bài giới thiệu dài với 申します, まいりました, として知られています, ことになりました, nhưng được trỏ ở S-03, ngay đầu hành trình zero. Không có hội thoại đích/mapping ngữ pháp để chứng minh đã đơn giản hóa.

**Đề xuất:** Không cần đẩy toàn bộ topic bạn bè/nhà hàng lên Thượng. Ghi riêng source_level, target_level, adaptation_required và giới hạn câu/từ/mẫu/độ ngầm; bản Trung chỉ chọn đoạn/mẫu phù hợp hoặc viết bản chuyển thể riêng. S-03 cần lời ngắn độc lập; bản nguồn dài có thể để cấp sau. H-11 thú cưng chỉ có một đầu mục chưa thể hiện nhiệm vụ thượng cấp, nên đưa nhu cầu cơ bản xuống sớm và giữ biến cố phức tạp về sau. JLPT chỉ làm tham khảo ngôn ngữ, không đo trực tiếp năng lực nói ([nguồn JLPT](https://www.jlpt.jp/e/about/points.html)).

### A09 — Đủ 27 tên sách không chứng minh đã tận dụng đủ tài nguyên; một số phần chưa có nơi dùng cụ thể

**Mức độ:** Quan trọng. **Vị trí:** B14, B22/B23; V4 §5–6.

**Bằng chứng:** §6 có đủ B01–B27 và số chặng theo sách khớp. Tuy nhiên B14 chỉ xuất hiện token U1 trong hai chặng; U2–U5 chưa được định vị. [B14:19](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/01-gioi-thieu-huong-dan.md:19>)–29 phân biệt năm Unit và độ khó, không thể suy U1 đại diện mọi đoạn shadowing cho toàn Sơ. B22/B23 L17 thiếu như A01. B06/B07/B09/B11/B12/B18/B19/B20/B24 chủ yếu được gắn theo phần rộng, chưa có bằng chứng từng mẫu độc đáo được dùng.

**Đề xuất:** Giữ bản đồ hai tầng: stage→section hiện tại và resource→planned/used/reference/skipped với lý do, chỉ điền đến mẫu/cảnh khi dựng chặng. Mỗi họ bank cần có kế hoạch chọn theo chức năng, vai và level; không nạp nguyên sách mỗi worker. B14 thêm U2–U5 vào pool có định vị, không bắt tất cả vào Sơ. Không tuyên bố còn thiếu toàn bộ thuê nhà/thiên tai/trường học con: các nhóm đó đã có chặng, chỉ còn vấn đề độ sâu/chứng cứ.

### B01 — Khung 12–15 phút chưa có cơ sở tải học; khóa shadowing tới ngưỡng có thể làm kẹt bài

**Mức độ:** Quan trọng. **Vị trí:** Skill §1, dòng16–34.

**Bằng chứng:** [skill:16](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:16>)–26 gom nghe, thẻ150–250 chữ, 5–8 câu + từ/mẫu, shadowing, hai vai, tự nói và Live2–3 phút vào một bài; [skill:23](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:23>) bắt đạt ngưỡng mới qua nhưng không có retry cap, cấu hình ngưỡng hay đường hỗ trợ. Nếu chỉ riêng ba lượt nói cho 5–8 câu đã có15–24 lượt cần thu và phản hồi, cộng hai vai/Live thì thời lượng phụ thuộc rất lớn vào người học và độ trễ. Sách shadowing còn yêu cầu hiểu nghĩa, chọn đoạn vừa sức, luyện lặp nhiều lượt: [B13:82](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/00-bia-muc-luc-huong-dan.md:82>)–86.

**Đề xuất:** 12–15 phút là mục tiêu pilot, không tiêu chí validate nội dung. Chia phần chuẩn bị và luyện nói thành phiên nối tiếp được; hỗ trợ nghe chậm/nhắc theo đoạn trước shadowing. Cho sửa vài lần rồi lưu mục cần ôn/đi tiếp, chỉ đặt cổng cứng cho năng lực thiết yếu đã hiệu chuẩn. Đo phút nghe/nói thực, số lần thử, bỏ bài và độ trễ trên người học thật; chưa có bằng chứng để kết luận khung chắc chắn bất khả thi.

### B02 — Chưa tách chấm âm với chấm nhiệm vụ; R2/R3 có nguy cơ không vận hành với audio cố định

**Mức độ:** Nghiêm trọng. **Vị trí:** Skill §1, dòng24–34, §6 dòng90.

**Bằng chứng:** [skill:24](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:24>) đánh giá đạt mục tiêu ở Đóng vai nhưng cột AI ghi không; [skill:30](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:30>) lại nói R3 để AI chấm. R2 so với các cách đúng chưa định nghĩa khoảng chấp nhận hay nhánh phản hồi; audio vai A cố định có thể mâu thuẫn với câu trả lời tự do đúng của user. [skill:34](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:34>) gộp 'đủ ý' vào chấm phát âm, Live đánh từng câu nhưng chưa có quy tắc tách lượt/hỗ trợ khi ASR không chắc. Dòng26 nói Live từ Trung, dòng28 lại Sơ tùy chọn — cần một cấu hình rõ.

**Đề xuất:** Tách pronunciation (âm/nhịp/độ rõ), fluency và task/pragmatics bằng rubric riêng. R1 có script/reference audio; R2 dùng slot/intent/acceptable variants và nhánh audio đã định; nếu user ra ngoài nhánh thì xác nhận/chuyển Live. R3/Live dùng policy + trạng thái nhiệm vụ, không ép khớp lời thoại. Lưu confidence, lỗi kỹ thuật/no-speech và human fallback; pilot đánh cả câu khác mẫu nhưng đúng, câu âm tốt nhưng sai ý, câu ASR nhận nhầm. Không lấy điểm phát âm làm bằng chứng đạt can-do.

### B03 — Đủ ô ma trận hoặc 8–12 đầu mục chưa đảm bảo đủ tình huống thực

**Mức độ:** Quan trọng. **Vị trí:** Skill §2; H-46; T-40; V4 §0.

**Bằng chứng:** [skill:38](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:38>)–46 chỉ có bốn trục và vài số tối thiểu, không có danh mục giá trị, ô bắt buộc/không áp dụng, trọng số nhu cầu hay tiêu chí trùng. [v4:597](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:597>) gọi mở lời→giao việc→xác nhận→đầu mối khẩn cấp→kết thúc là năm tình huống: đây có thể chỉ là năm bước của một cuộc bàn giao. T-40 cũng chia một cuộc xin lời khuyên thành các lượt. V4 có674 đầu mục, min1/max9, 27 chặng chỉ1 đầu mục; V4 đã nói sẽ mở rộng sau, nên chưa đủ8–12 không phải lỗi schema của bản khung.

**Đề xuất:** Định nghĩa situation bằng vai + đích đạt được + dữ kiện/điều kiện + kết thúc quan sát được; lượt mở/kết là dialogue_moves. Chọn ô thiết yếu dựa nhu cầu và nguồn, thêm kênh/độ nghe khó/repair/độ tự chủ. Cho N/A với lý do, kiểm các cặp trùng và sự khác biệt của biến thể. Máy kiểm tính hiện diện/count/quan hệ, người review quyết đúng/nghĩa/tính tự nhiên; không gán điểm phủ tự động như chứng minh sư phạm.

### B04 — Quy tắc từ vựng chưa đủ nghĩa/từ loại; 'chặng gốc' có thể làm đứt đường học

**Mức độ:** Quan trọng. **Vị trí:** Skill §3 và thứ tự dựng §7.

**Bằng chứng:** [skill:50](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:50>)–55 đặt20–30 từ Lõi,80–150 Mở rộng/chặng, vòng kín và mỗi từ một chặng gốc, nhưng chưa có word/sense ID, cách tách hình thái hay phân biệt từ mới với từ chức năng đã biết. Cùng chữ có nhiều nghĩa/cách dùng; kiểm bằng substring không đủ. Khi học vào Trung/nhánh tùy chọn hoặc dựng200 Lõi song song, chặng gốc có thể bị bỏ qua/chưa xuất bản. [skill:94](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:94>) lại dựng từ vựng trước hội thoại, nên danh sách có thể stale khi hội thoại được viết lại.

**Đề xuất:** Dùng lexeme_id + sense_id + reading/POS/register, occurrences theo utterance/span; dạy mới theo sense/use, không chỉ mặt chữ. Có assumed_known/recognition-only và cho phép học tại chỗ khi chưa học chặng gốc. Lặp vòng dialogue→extract vocab→revise→validate đến ổn định; không ép80–150 từ chỉ để đủ số. Master dùng single-writer/merge có khóa như B08; không để worker tự chọn các chặng gốc mâu thuẫn.

### B05 — Ngữ pháp pending và trần Minna chưa có dữ liệu để kiểm; trạng thái xong cần chặn thiếu đầu vào

**Mức độ:** Quan trọng. **Vị trí:** Skill §4, §7–8; Plan V2.1 §2.

**Bằng chứng:** [skill:59](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:59>) nói N5/N4 đang chờ danh sách Minna nhưng cho để trống rồi gắn lại; [skill:99](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:99>) lại hứa validator trần ngữ pháp. JSON V4 không có grammar_ref, ceiling hay prerequisite. Con trỏ tới một bài Minna chứa nhiều mục không đủ chỉ ra mẫu/nghĩa; tiếng nói rút gọn, kính ngữ và mẫu trong Speak Japanese còn cần ánh xạ với dạng chuẩn. Chưa có ngữ liệu đích nên không thể kiểm 'chặng dùng cấu trúc chưa dạy' như một phép kiểm đã hoàn tất.

**Đề xuất:** Cho phép blueprint ở blocked/pending_grammar, không publish/mark ready khi ngữ pháp bắt buộc chưa resolve. Mỗi ref gồm pattern_id, sense/use, dạng chuẩn/dạng nói, productive/receptive, prerequisite, nguồn và phiên bản; bài Minna chỉ là locator phụ. Trần dựa inventory đã khai báo và văn bản lời thoại thực, có danh sách fixed chunks ngoại lệ được review. Chỉ tra bunpou read-only khi đến bước dựng; review này chưa xác minh kho đó.

### B06 — Schema mới là danh mục file, chưa đủ hợp đồng để chuyển app/DB

**Mức độ:** Quan trọng. **Vị trí:** Skill §6, dòng74–90.

**Bằng chứng:** [skill:74](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:74>)–90 nêu thư mục và tên bảng, utterance mới có người nói/kana/lịch sự/đáp án/audio ref; chưa thấy JSON Schema thực, required/enum/FK, cấu trúc text tiếng Nhật + nghĩa Việt, audio alignment, goal rubric, review-card version hay content version. Dòng86–87 để knowledge.md là nội dung nguồn bên cạnh tuyên bố JSON là bản gốc, khiến nơi sửa/nơi render chưa nhất quán.

**Đề xuất:** Trước pilot chốt schema tối thiểu, không cần thiết kế toàn sản phẩm: immutable IDs/FK; text locales ja/vi, display/reading và biến thể; speaker/learner-role; task goal/slots/constraints/rubric; audio asset/version/status/rights/timing với utterance alignment; vocab/grammar occurrences; card_id→utterance/version. Tách nội dung học với learner progress/SRS scheduling/recordings; có content_schema_version/content_revision và migration/tombstone. Chọn JSON cho knowledge hoặc tuyên bố Markdown là authoring field rồi biên dịch có hash, tránh hai bản gốc.

### B07 — ID theo vị trí chưa chứng minh ổn định khi đổi thứ tự/chèn chặng

**Mức độ:** Quan trọng. **Vị trí:** Skill §6 dòng74, thư mục ví dụ dòng79; V4 IDs S/T/H.

**Bằng chứng:** [skill:74](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:74>) gọi S-01.03.u05 là ID cố định, nhưng các thành phần giống level/thứ tự/số tình huống; thư mục cũng gắn S-01 và slug. V4 từng thay/đổi số lượng qua phiên bản, mà chưa có registry identity hay bảng alias từ ID hiển thị sang identity. Nếu renumber hoặc đổi level sẽ có nguy cơ mất liên kết card/audio/tiến độ.

**Đề xuất:** Tách immutable stage/situation/utterance UUID hoặc opaque ID khỏi level/order/display_code/slug. Khi chèn chỉ đổi order; khi thay nội dung ghi revision, giữ alias/redirect cho mã cũ. Quy tắc tách/gộp/deprecate phải cập nhật các FK và xử lý review-card/tiến độ theo version. Kiểm reorder pilot: xuất app/DB trước và sau, không tạo ID mới cho cùng đối tượng.

### B08 — Atomic rename từng file không đủ cho rerun nhiều bước và nhiều worker dùng dữ liệu chung

**Mức độ:** Nghiêm trọng. **Vị trí:** Skill §7 dòng94–99; shared vocab_master/run_state.

**Bằng chứng:** [skill:96](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:96>) liệt kê pending/running/done/failed/needs_review nhưng dòng98 dùng stale ngoài enum. 'Hash đầu vào' chưa xác định có source/spec/prompt/dependency/output nào; resume theo bước đầu chưa done không xác minh output còn tồn tại/khớp hash. Đổi spec có thể ảnh hưởng các bước trước lẫn sau (cảnh, level, từ, hội thoại, audio/card); sửa hội thoại có thể làm vocab bước trước stale. Atomic rename chỉ bảo vệ một file, không giao dịch cả bộ chặng và master dùng chung.

**Đề xuất:** Thiết kế DAG phụ thuộc thật + states blocked/stale/reviewed/published; pin spec/source/schema/prompt/model/tool và hash output. Worker claim một stage với owner/lease/heartbeat/run_id; worker cũ hết lease không được publish. Viết vào run riêng, validate bundle rồi commit manifest/revision nguyên tử; master vocabulary/source registry single-writer hoặc merge có CAS/lock. Resume đối chiếu artifact/hashes, không chỉ status. Bảo vệ bản người sửa bằng revision/conflict; thử kill sau ghi dialogue trước status, thay spec, hai worker claim cùng stage và tranh chấp master.

### B09 — Ước lượng token đúng phép nhân nhưng chưa được đo; Lõi cho cả200 trước vẫn là quy mô lớn

**Mức độ:** Quan trọng. **Vị trí:** Skill §7 dòng101, §8 dòng109.

**Bằng chứng:** [skill:101](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:101>):200×40–80k =8–16 triệu token là đúng số học, nhưng chưa có pilot/log input/output/reasoning/cache/rerun/QA để kiểm mức40–80k. Lõi4×200=800 tình huống; theo mục tiêu12–15 phút là160–200 giờ hoạt động dự kiến, chưa tính ôn và không phải nhãn thời gian của lộ trình. Làm800 Lõi trước vẫn khóa một schema chưa thử, không phải một MVP nhỏ. Chưa có cổng người Nhật/người học thực nghiệm trước khi xem output là cuối.

**Đề xuất:** Dựng một chặng S-18 end-to-end với audio thật/được phép dùng trước; tiếp T-15 và H-13 để kiểm R2/R3, kính ngữ và branch; thêm một chặng liên quan nhỏ để thử vocab dùng lại và reorder. Ghi token/giờ/cost theo step, tỷ lệ phải sửa và lỗi ngữ dụng; đặt ngân sách dừng và điều kiện qua pilot trước khi mở rộng một cụm. QA tự động cho schema/provenance, review người có năng lực cho lời thoại/độ tự nhiên, người học thật cho chuyển giao; không dùng việc AI tự chấm chính nó làm chứng cứ duy nhất.

### B10 — 'Viết lại + con trỏ' chưa phải phương án bảo đảm quyền phát hành

**Mức độ:** Nghiêm trọng. **Vị trí:** Skill §8 dòng107; audio/clean sources.

**Bằng chứng:** [skill:107](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:107>) đặt viết lại theo cấu trúc sách và chỉ ghi con trỏ là phương án đề xuất. Cơ quan Văn hóa Nhật phân biệt ý tưởng với biểu đạt sáng tạo, và nêu quyền dịch/chuyển thể, sử dụng tác phẩm phái sinh, sao chép/truyền công cộng ([tổng quan chính thức](https://www.bunka.go.jp/english/policy/copyright/system/)). Hướng dẫn AI của cơ quan này vẫn xét sự tương đồng và phụ thuộc ở giai đoạn sử dụng; không coi AI sinh hay ghi nguồn là tự động hợp pháp ([JCO, trang12–13](https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/workingteam/r06_01/pdf/94080501_11.pdf)). Hồ sơ hiện tại là inventory nguồn nghe, chưa chứng minh quyền phân phối.

**Đề xuất:** Phân loại licensed/original/needs_rights_review ở text và audio; giữ provenance nội bộ, xin quyền khi dùng hội thoại/bài tập/audio thương mại, và viết lời thoại độc lập từ can-do/bối cảnh phổ quát khi làm original. Đổi tên/đổi vài từ hoặc tạo TTS không tự xóa vấn đề quyền với văn bản. Trước phát hành cần đánh giá pháp lý theo nội dung, hợp đồng và thị trường áp dụng; review này không kết luận đoạn nào vi phạm.

### B11 — Thẻ kiến thức có nguy cơ tuyệt đối hóa văn hóa và dùng quy trình cũ như sự thật hiện hành

**Mức độ:** Quan trọng. **Vị trí:** Skill §1 dòng21; nguồn manners và đời sống.

**Bằng chứng:** [skill:21](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_SKILL_DESIGN_V1.md:21>) yêu cầu150–250 chữ về 'người Nhật nghĩ gì', không ghi quan điểm của ai/giới hạn bối cảnh. [B03:8](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/19-Unit17-指示を受ける.md:8>)–17 có các lựa chọn ứng xử trong tình huống nhận việc; không nên biến chúng thành luật 'luôn phải nhận việc/không được từ chối'. Các đoạn đời sống như [B08:347](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md:347>) hỏi mang thẻ bảo hiểm và các quy trình quầy là ngôn ngữ trong nguồn, chưa chứng minh thủ tục hiện hành. V1 chưa có factual/currentness_review hoặc người chịu trách nhiệm kiểm ngữ dụng.

**Đề xuất:** Viết theo vai, mục đích và điều kiện; dùng 'trong bối cảnh này...' cùng cách nói thay thế/đặt giới hạn thay vì gán tâm lý chung cho một dân tộc. Với nội dung y tế, lao động, thuế, cư trú: giới hạn mục tiêu ở giao tiếp, tách dữ kiện quy trình cần kiểm hiện hành và có ngày review. QA ngữ dụng bao gồm từ chối an toàn, xin xác nhận và không hứa quá thẩm quyền.

### 2.1. Rà lần lượt 37 cụm: chủ đề và thứ tự

Đã kiểm mọi cụm trong danh sách thứ tự, không yêu cầu phải xen Đời sống/Công việc từng chặng một. Nhận xét dưới đây ở mức mạch chủ đề/can-do dự kiến. Vì V4 chưa có lời thoại đích, dữ liệu ngữ pháp và prerequisite, **chưa thể kết luận không có nhảy kiến thức** ở bất kỳ cụm nào.

| Cấp / cụm / phạm vi | Nhận xét |
|---|---|
| Sơ — [Mở miệng lần đầu: chào hỏi, giới thiệu, ngày đầu (S-01–S-06)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:40>) | Chào hỏi→ngày đầu có liên hệ; S-03 lấy lời nguồn trung cấp quá sớm nếu không đơn giản hóa. Cần bổ trợ hỏi lại trước khi giao tiếp với công sở. |
| Sơ — [Chỗ ở, khu phố & văn phòng (S-07–S-12)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:41>) | Nhà ở↔văn phòng nối được qua tìm chỗ/dùng đồ; S-10 phải lọc nguồn phi ngôn ngữ, S-11 là nhánh homestay riêng. |
| Sơ — [Đi lại & thời gian (S-13–S-17)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:42>) | Đi lại↔đúng giờ/lịch trình hợp chủ đề; chưa có độ khó/câu đích để phân thứ tự phương tiện xa. |
| Sơ — [Ăn uống & mua sắm (S-18–S-23)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:43>) | Nhà hàng→ăn với đồng nghiệp hợp lý; S-23 phỏng vấn+phục vụ là hai nhiệm vụ, cần làm rõ Lõi. |
| Sơ — [Nhờ vả, xin phép, xin lỗi (S-24–S-29)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:44>) | Nhờ–xin phép–xin lỗi hợp chức năng; S-29 kiểm nghe điện thoại trước cụm điện thoại công sở. |
| Sơ — [Sức khỏe & an toàn cơ bản (S-30–S-34)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:45>) | Sức khỏe→báo ốm→khẩn cấp có liên hệ; không nên khóa lời trợ giúp thiết yếu đến tận cụm6. |
| Sơ — [Điện thoại & hẹn gặp (S-35–S-40)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:46>) | Đời sống→công sở hợp lý; S-40 nomikai/câu chuyện ngoài giờ chưa có phụ thuộc rõ với S-46. |
| Sơ — [Giấy tờ, thủ tục & báo cáo (S-41–S-44)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:47>) | Giấy tờ↔chỉ thị/báo cáo chỉ có liên hệ hình thức; cần can-do nối như nhận yêu cầu→xác nhận→báo hoàn tất. |
| Sơ — [Bạn bè, cuối tuần & trò chuyện (S-45–S-50)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:48>) | Bạn bè→rủ/hẹn→kể trải nghiệm mạch hợp lý; nguồn phép khen/phản hồi cần chọn mức Sơ. |
| Sơ — [Ý kiến, cảm xúc, kế hoạch & du lịch (S-51–S-57)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:49>) | Cảm xúc–kế hoạch–họp–thời tiết–du lịch gom quá nhiều trục; nên tách tiểu mạch, xác định mục tiêu ôn của S-57. |
| Sơ — [Tổng kết Sơ (S-58–S-59)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:50>) | Tổng hợp có vai trò; S-58/59 chưa có rubric/phụ thuộc và tình huống kiểm thật để xác nhận đầu ra Sơ. |
| Trung — [Tự lập: chỗ ở, giấy tờ & hướng nghề (T-01–T-06)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:56>) | Nhà ở→chọn ngành→sharehouse→tiền bối→thủ tục→hồ sơ là xen hai mạch, cần cầu nối thực hoặc nhóm lại. |
| Trung — [Vào nghề: từ phỏng vấn đến những ngày đầu (T-07–T-11)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:57>) | Chuẩn bị nghề→phỏng vấn→nhận việc là hợp; xen T-08 người mới có liên hệ. T-11 phát biểu nâng cao chưa rõ vai trò. |
| Trung — [Điện thoại: đời sống đến công sở (T-12–T-18)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:58>) | Bảy chặng điện thoại cùng một họ, có trình tự; T-12/14/18 cần phân vai/mục tiêu, không chỉ cùng nguồn. |
| Trung — [Xã giao: ngoài công ty ↔ trong công ty (T-19–T-24)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:59>) | Quà→khách→thăm nhà→tiếp khách có liên hệ; T-19/23/24 chồng nguồn sự kiện/du lịch, cần dedup. |
| Trung — [Bạn bè, đồng nghiệp & chuyện trò (T-25–T-33)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:60>) | Quan hệ tăng thân thiết hợp; T-26/27/28 đang theo phân nhóm của B13, cần can-do khác nhau thay vì chép mục lục. |
| Trung — [Nhờ vả, từ chối, xin lỗi (T-34–T-38)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:61>) | Nhờ/từ chối/xin lỗi có liên hệ; nằm sau nhiều điện thoại cần các chức năng này. Có thể ôn nếu khai báo prerequisite. |
| Trung — [Ý kiến, cảm xúc & lời khuyên (T-39–T-45)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:62>) | Đời sống↔cấp trên qua ý kiến/cảm xúc là hợp; T-40 biến lượt nói thành tình huống, T-44 theo loại từ cần tháo. |
| Trung — [Làm việc theo cách Nhật (T-46–T-49)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:63>) | Báo–liên–tương thuộc mạch công việc; email/T-47 lệch trọng tâm nói; cả cụm CV không tự là lỗi xen kẽ. |
| Trung — [Gia đình, con cái & công việc (T-50–T-55)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:64>) | Gia đình→cân bằng công việc→con cái là liên hệ tốt; cần nhánh tùy nhu cầu, không mặc định mọi người có con. |
| Trung — [Họp, thuyết trình & quan hệ nơi làm (T-56–T-60)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:65>) | Họp→trình bày→giải thích→ý tưởng có trình tự chủ đề; T-57 chồng T-48, T-59/60 cần định vị memo cụ thể. |
| Trung — [Mua sắm, bán hàng & thương lượng (T-61–T-64)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:66>) | Mua với tư cách khách→bán→thương lượng có liên hệ; T-63 quá rộng theo quan hệ, chưa rõ khoảng trống riêng. |
| Trung — [Sức khỏe & an toàn (T-65–T-68)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:67>) | Y tế↔sự cố↔an toàn có liên hệ; T-65/66 trùng phạm vi, xin thuốc sai section. |
| Trung — [Đi lại, du lịch & mùa (T-69–T-71)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:68>) | Công tác→nghỉ→mùa có thể nối bằng lập kế hoạch, nhưng T-71 toàn AI và T-69 bank du lịch chưa đủ chi phí công tác. |
| Trung — [Nghề phục vụ ↔ khách (T-72–T-78)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:69>) | Khách↔nhân viên là chuyển vai có chủ đích; không ép mọi người học cả hai vai, tránh dạy kính ngữ thiếu cầu nối. |
| Trung — [Tổng kết Trung (T-79–T-79)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:70>) | Định vị là tổng hợp nhưng sáu tình huống hiện đều nghiêng công sở, chưa thể hiện phần ngoài đời trong tên. |
| Thượng — [Bước vào sân chơi chuyên nghiệp (H-01–H-06)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:76>) | Sáu chặng nghề nghiệp có mạch vai, nhưng H-03 chứa telesales; chưa phải mọi bài đều khó hơn Trung nếu chỉ đổi tên. |
| Thượng — [Gia đình, nhà ở & sức khỏe chín chắn (H-07–H-11)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:77>) | Nhà ở/gia đình/sức khỏe liên hệ đời sống, nhưng AI chiếm nhiều; H-11 thú cưng chưa nêu đặc trưng thượng cấp. |
| Thượng — [Phàn nàn ↔ khiếu nại (H-12–H-18)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:78>) | Khách phàn nàn↔nhân viên xử lý là liên hệ rõ; H-17/18 cần tách khỏi báo cáo ở H-43/44 bằng điều kiện cụ thể. |
| Thượng — [Bán hàng & chào bán (H-19–H-23)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:79>) | Chào bán→thuyết phục→tiếp đãi→chốt có liên hệ; H-20 định vị bank quá thô, H-22 chỉ có manners. |
| Thượng — [Tâm sự, quan điểm & nghi thức (H-24–H-29)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:80>) | Tình cảm→bất đồng→nhờ khó có liên hệ; chia tay việc và nghi thức cưới/tang cần cầu nối/mục tiêu riêng. |
| Thượng — [Đàm phán & từ chối (H-30–H-34)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:81>) | Thương lượng→từ chối→tranh luận có liên hệ; H-34 công tác/chuyển chi nhánh lệch cụm, nên sang di chuyển/nhận vai mới. |
| Thượng — [Kể chuyện & nói như người bản địa (H-35–H-42)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:82>) | Kể chuyện/phong cách/cảm xúc hợp mục tiêu nói; H-40–42 là nhóm thành ngữ, không phải chặng thực tế. |
| Thượng — [Quản lý đội & quan hệ nhạy cảm (H-43–H-47)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:83>) | Quản lý→quan hệ nhạy cảm→bàn giao có liên hệ; H-45 track Đời sống cần giải thích, H-46/47 chồng bàn giao. |
| Thượng — [Họp, thuyết trình & dẫn dắt (H-48–H-52)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:84>) | Họp→thuyết trình có liên hệ; H-49 là các mức đồng ý nên vào ngân hàng, H-50 sự kiện ngoài công ty cần cầu nối. |
| Thượng — [Nói chuyện về Nhật Bản & xã hội (H-53–H-59)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:85>) | Văn hóa/xã hội là miền hợp lý cho Thượng; H-58 trộn việc hành chính với vending, H-59 có con trỏ sai. |
| Thượng — [Tổng kết Thượng (H-60–H-62)](<D:/CODE/git/kaiwa_skill/kaiwa_skill/planning/v2/KAIWA_CHANG_V4.md:86>) | Tổng kết chưa có rubric; H-60 omotenashi là nội dung mới hơn là bài tổng hợp, nên dạy trước khi kiểm. |

Không thấy lịch học bị gắn tháng/tuần vào tên cụm. “Một tuần ở công ty” của T-79 là bối cảnh mô phỏng, không tự chứng minh có lịch ép học một tuần; không coi đó là lỗi nhãn thời gian.

## 3. Bảng con trỏ đã mở và đối chiếu

50 dòng dưới đây thuộc 49 chặng khác nhau; T-35 có hai lượt kiểm. Kết quả “sai” là sai gán nghĩa hoặc sai section, không đồng nghĩa toàn bộ chặng phải bỏ. “Không rõ” là alias chưa định nghĩa/nguồn quá rộng hoặc bank chưa chứng minh đủ mục tiêu. Không suy tỷ lệ lỗi của toàn corpus từ mẫu có chủ ý ưu tiên chỗ yếu này.

| Chặng | Token | Kết quả | File clean và dòng đã mở | Ghi chú |
|---|---|---|---|
| S-03 | B21:L1 | đúng | [B21/01-jiko-shoukai.md:29](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本語でビジネス会話 中級編 本文冊/chapters/01-jiko-shoukai.md:29>) | Tự giới thiệu đúng chủ đề, nhưng lời mẫu và mẫu giải thích vượt mức zero; phải viết bản Sơ riêng. |
| S-04 | B04:U30 | đúng | [B04/31-Unit30-名前の漢字を尋ねる.md:6](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/31-Unit30-名前の漢字を尋ねる.md:6>) | Hỏi chữ Hán của tên; chỉ hỗ trợ tình huống hỏi tên. |
| S-07 | B08:P4-21 | đúng | [B08/04-part4-bamen.md:598](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md:598>) | Môi giới nhà, điều kiện thuê. |
| S-10 | B03:U1 | không rõ | [B03/02-Unit01-あいさつの基本.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/02-Unit01-あいさつの基本.md:1>) | Unit là chào hỏi, chỉ hỗ trợ phép chào; không đủ cho toàn nội quy nơi làm. |
| S-11 | B08:P4-20 | đúng | [B08/04-part4-bamen.md:569](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md:569>) | Homestay và bữa ăn/giao tiếp gia đình chủ nhà. |
| S-14 | B27:8 | đúng | [B27/09-bai-08-eki-de.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/09-bai-08-eki-de.md:1>) | Bài 8 ở ga. |
| S-18 | B26:3 | đúng | [B26/03-bai-3.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/03-bai-3.md:1>) | Bài 3 nhà hàng; cần chọn mức khó cho Sơ. |
| S-21 | B05:ch4 | đúng | [B05/05-ch4-konbini.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/05-ch4-konbini.md:1>) | Konbini, chủ yếu vai nhân viên; chưa chứng minh hợp mọi lời của khách. |
| S-29 | B17:T1 | không rõ | [B17/05-総合タスク1.md:6](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/05-総合タスク1.md:6>) | T1 có thật: gặp khách, xin lỗi gọi nhầm tên và thuật lại với đồng nghiệp; bốn tình huống V4 là AI, không phải bốn thẻ gốc T1. |
| S-32 | B08:P4-11 | đúng | [B08/04-part4-bamen.md:312](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md:312>) | Câu ở hiệu thuốc. |
| S-38 | B04:U28 | đúng | [B04/29-Unit28-留守番電話に伝言を残す.md:6](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/29-Unit28-留守番電話に伝言を残す.md:6>) | Để lời nhắn trong hộp thư thoại. |
| S-42 | B03:U17 | đúng | [B03/19-Unit17-指示を受ける.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/19-Unit17-指示を受ける.md:1>) | Nhận chỉ thị, ghi nhớ và xác nhận. |
| S-44 | B17:L4 | đúng | [B17/04-仕事が山積み.md:19](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/04-仕事が山積み.md:19>) | Quá tải công việc, nhờ giúp/xác nhận hạn; nguồn bổ trợ, không bao trọn báo–liên–tương. |
| S-48 | B08:P4-28 | đúng | [B08/04-part4-bamen.md:795](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md:795>) | Hẹn hò, sở thích và rủ đi xem phim. |
| S-51 | B01:C1 | đúng | [B01/01-cam-xuc.md:4](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/01-cam-xuc.md:4>) | Cảm xúc và phản ứng. |
| T-07 | B16:U3 | đúng | [B16/04-Unit3-就職の面接.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/04-Unit3-就職の面接.md:1>) | Unit3 phỏng vấn tuyển dụng. |
| T-14 | B08:P4-27 | đúng | [B08/04-part4-bamen.md:767](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md:767>) | Đặt chỗ/hỏi thông tin; P4-26 bổ sung giao hàng, không phải cả hai mục đều dạy giao hàng. |
| T-15 | B04:U4 | đúng | [B04/05-Unit04-担当者へ取り次ぐ.md:6](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/05-Unit04-担当者へ取り次ぐ.md:6>) | Chuyển máy cho người phụ trách. |
| T-18 | B05:ch7 | đúng | [B05/08-ch7-denwa.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/08-ch7-denwa.md:1>) | Điện thoại vai nhân viên dịch vụ. |
| T-23 | B13:U5a | đúng | [B13/05-unit-5-dong-nghiep.md:158](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/05-unit-5-dong-nghiep.md:158>) | Chọn ngày tiệc đón tiễn. |
| T-24 | B21:L8 | đúng | [B21/08-shain-ryokou.md:55](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本語でビジネス会話 中級編 本文冊/chapters/08-shain-ryokou.md:55>) | 社員旅行, đúng chủ đề du lịch công ty. |
| T-26 | B13:U5a | đúng | [B13/05-unit-5-dong-nghiep.md:88](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/05-unit-5-dong-nghiep.md:88>) | Section1 có trao đổi đồng nghiệp khi mất dữ liệu; cần chọn đúng anchor, không lấy toàn section làm một tình huống. |
| T-27 | B13:U2a | đúng | [B13/02-unit-2-ban-than.md:17](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/02-unit-2-ban-than.md:17>) | Trò chuyện với bạn thân; tương đương nguồn khoảng N2, cần đơn giản hóa cho Trung N4–N3. |
| T-28 | B13:U3a | đúng | [B13/03-unit-3-nguoi-quen-hang-xom.md:17](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/03-unit-3-nguoi-quen-hang-xom.md:17>) | Người quen và xã giao, tiệc năm mới. |
| T-34 | B12:A6 | không rõ | [B12/13-part2-a-hitei.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/わかる！話せる！日本語会話 発展文型125/chapters/13-part2-a-hitei.md:1>) | Có PART2 A⑥ phủ định nhẹ; A6 là alias không được định nghĩa, khác token P2-A6 cùng hồ sơ. Không phải nguồn riêng về nhận/từ chối lời nhờ. |
| T-35 | B21:L2 | không rõ | [B21/02-wakaranai-nihongo.md:10](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本語でビジネス会話 中級編 本文冊/chapters/02-wakaranai-nihongo.md:10>) | L2 là hỏi cách đọc/nghĩa tiếng Nhật; chỉ hỗ trợ hỏi làm rõ, không đủ chứng minh chỉ thị/đề nghị cấp trên. |
| T-44 | B19:P1 | đúng | [B19/02-part1.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/02-part1.md:1>) | Dùng onomatopoeia cùng động từ; nguồn đúng nhưng chặng lấy loại từ làm chủ đề trái tiêu chí. |
| T-47 | B03:U16 | đúng | [B03/18-Unit16-ビジネスEメール.md:24](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/18-Unit16-ビジネスEメール.md:24>) | Email công việc, đúng nguồn nhưng chủ yếu học viết; nguồn còn thiếu trang in104–105. |
| T-63 | B13:U7a | đúng | [B13/07-unit-7-nguoi-ngoai-cong-ty.md:17](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/07-unit-7-nguoi-ngoai-cong-ty.md:17>) | Quan hệ đối ngoại/phỏng vấn; chặng đang là tập quan hệ hơn là mục tiêu giao tiếp riêng. |
| T-66 | B13:U4a | đúng | [B13/04-unit-4-bac-si-cua-hang.md:32](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md:32>) | Bác sĩ hỏi đau đầu/triệu chứng; cùng section còn có dịch vụ cửa hàng. |
| H-03 | B13:U8-6 | đúng | [B13/08-unit-8-hoi-thoai-dai.md:225](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/08-unit-8-hoi-thoai-dai.md:225>) | Token đúng cảnh mua sắm qua chương trình telesales như tình huống con ghi; lạc khỏi trọng tâm hẹn khách của tên chặng. |
| H-04 | B13:U7b | đúng | [B13/07-unit-7-nguoi-ngoai-cong-ty.md:108](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/07-unit-7-nguoi-ngoai-cong-ty.md:108>) | Section2 quan hệ đối ngoại; nguồn khoảng N1 theo lời sách, cần xử lý cho đích N3–N2+. |
| H-08 | B13:U4b | không rõ | [B13/04-unit-4-bac-si-cua-hang.md:148](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md:148>) | Có đổi lịch nha khoa và xin thuốc; chưa thấy bảo hiểm/chăm sóc người thân hay khám phức tạp trong section. |
| H-09 | B13:U3b | không rõ | [B13/03-unit-3-nguoi-quen-hang-xom.md:186](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/03-unit-3-nguoi-quen-hang-xom.md:186>) | Bank có thật nhưng section nói với người quen, không chứng minh đủ hợp đồng nhà/sửa chữa; sáu cảnh đã gắn AI, không coi là chép sai nguồn. |
| H-13 | B15:L6 | đúng | [B15/06-bai-06.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/06-bai-06.md:1>) | L6 tiếp nhận khiếu nại, đúng chức năng. |
| H-18 | B03:U18 | đúng | [B03/20-Unit18-報告・連絡・相談.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/20-Unit18-報告・連絡・相談.md:1>) | Báo cáo/liên lạc/xin ý kiến chung; chưa đủ bằng chứng đặc thù cấp cao/phản hồi dự án. |
| H-22 | B03:U13 | đúng | [B03/15-Unit13-接待・会食.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/15-Unit13-接待・会食.md:1>) | Tiếp đãi và dùng bữa cùng khách; phải lọc phần trang phục/ngồi và quy tắc phi ngôn ngữ. |
| H-23 | B13:U6b | đúng | [B13/06-unit-6-cap-tren-cap-duoi.md:290](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/06-unit-6-cap-tren-cap-duoi.md:290>) | Có cảnh hải quan thiếu chứng từ; B15:L15 mới là lõi chốt đơn. |
| H-34 | B13:U6b | đúng | [B13/06-unit-6-cap-tren-cap-duoi.md:304](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/06-unit-6-cap-tren-cap-duoi.md:304>) | Công tác gấp, thiếu chứng từ thông quan và chuyển chi nhánh có thật ở các mục11/12/16. |
| H-37 | B18:P1-1 | đúng | [B18/03-PART1-丁寧語・美化語.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/03-PART1-丁寧語・美化語.md:1>) | 丁寧語・美化語 là nền kính ngữ; chỉ một phần của đối ngoại, cần tôn kính/khiêm nhường kèm theo. |
| H-38 | B12:P3 | đúng | [B12/26-part3-kaiwa-kotoba.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/わかる！話せる！日本語会話 発展文型125/chapters/26-part3-kaiwa-kotoba.md:1>) | PART3 là từ giải thích rộng, có いや/だめ và dạng 何 cảm xúc; bank hợp lệ nhưng nên chỉ rõ mẫu, không khẳng định toàn P3 là cảm xúc. |
| H-40 | B20:A | đúng | [B20/02-section-a.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/02-section-a.md:1>) | SectionA: thuận lợi/may mắn; nguồn đúng, cách tạo chặng bằng nhóm thành ngữ trái tiêu chí. |
| H-43 | B13:U8-4 | đúng | [B13/08-unit-8-hoi-thoai-dai.md:145](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/08-unit-8-hoi-thoai-dai.md:145>) | Đoạn sếp mời nhân viên dự bữa tiếp đãi có quan hệ họ hàng, hỗ trợ quan hệ; ngân sách ở U6b, không ở U8-4. |
| H-45 | B13:U5b | đúng | [B13/05-unit-5-dong-nghiep.md:272](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/05-unit-5-dong-nghiep.md:272>) | Đồng nghiệp bàn sa thải; track Đời sống chưa nhất quán với tên quan hệ nơi làm. |
| H-59 | B18:P2-2 | sai | [B18/07-PART2-場面別.md:58](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md:58>) | PART2 cảnh2 là thư viện, không phải học thuật/nghiên cứu; cảnh1 có trao đổi luận văn. |
| S-24 | B26:9 | sai | [B26/09-bai-9.md:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/09-bai-9.md:1>) | ゆずります là nhượng/tặng đồ không dùng nữa, không phải nhường chỗ ngồi như tình huống con gán. |
| T-35 | B21:L14 | sai | [B21/14-shotaimen.md:45](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本語でビジネス会話 中級編 本文冊/chapters/14-shotaimen.md:45>) | 初対面の人と, giới thiệu/nhắn lời; không phải xin phép/xin nghỉ. B22:L14/B23:L14 kế thừa nhầm cùng bài. |
| T-55 | B18:P2-2 | sai | [B18/07-PART2-場面別.md:58](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md:58>) | Cảnh2 là thư viện; trao đổi luận văn/giáo viên nằm cảnh1, mục4. |
| T-65 | B13:U4a → U4b | sai | [B13/04-unit-4-bac-si-cua-hang.md:316](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md:316>) | Cảnh xin thuốc sau sáu tháng ở section2/U4b, không phải section1/U4a; không phải xin thuốc dài hạn. |
| H-29 | B02:S44,S45 | sai | [B02/15-挨拶する.md:137](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/15-挨拶する.md:137>) | Hai scene chào khi quay về chi nhánh/chia tay đồng nghiệp; không phải tiệc cưới như tình huống con ghi. |

Đối chiếu bổ sung các bản companion L14 đã xác nhận B22 là 初対面の人と và B23 là Gặp người lần đầu, cùng lỗi gán xin phép/xin nghỉ ở T-35. Các con trỏ memo được kiểm theo nội dung đã có trong memo, không coi là đã mở toàn văn sách web.

## 4. Kết quả script kiểm tra tính nhất quán

Script được chạy bằng Python trong bộ nhớ, chỉ đọc file; không ghi script/helper vào repo. Một lượt kiểm khung cơ bản và một lượt kiểm sâu hơn về AI/token/index cho kết quả:

| Kiểm tra | Kết quả |
|---|---|
| JSONL parse / trường bắt buộc / kiểu chính / enum / ID | 200 dòng hợp lệ; 200 ID duy nhất, không đứt dãy S01–59/T01–79/H01–62 |
| Level và track | Sơ:36 Đời sống +23 Công việc; Trung:34+45; Thượng:29+33; tổng99+101 |
| Chặng/ID/title/track/nội dung tình huống MD so JSONL | 200 hàng tương ứng; không phát hiện khác biệt ở các trường đã so |
| Bảng thứ tự cụm | 37/37 khớp tên cụm, dải ID, số lượng và chuỗi Đ/C theo đúng thứ tự JSONL |
| sources của chặng bằng hợp sources của các tình huống | 200/200 khớp; không có sources rời không được gắn tình huống |
| Số đầu mục tình huống | 674 =198 Sơ +251 Trung +225 Thượng; min1/max9; 27 chặng hiện có một đầu mục |
| Cờ ai | 320 true /354 false; năm trường hợp false nhưng sources chứa literal AI: S-08 tình huống5; H-58 tình huống1–2; H-61 và H-62 tình huống1 |
| Phân loại thực của354 mục ai=false | 213 có token sách Bxx;136 chỉ có token memo/NHK;5 có AI. Đây là liên kết, chưa phải verified-used |
| Tên sách được gắn | Đủ27/27; mọi số chặng và phân bố cấp của bảng §6 khớp |
| B22/B23 L1–20 | Mỗi tập có19 token, cùng thiếuL17; báo cáo20/20 ở §5 sai |
| B08/B12 đơn vị đếm | B08 có61 token gồm3 P1 +15 P2 +33 P4 +10 P5; bảng58 cần nói rõ có loại P1 hay không. B12 có7 token nhưng A6/P2-A6 có thể là cùng alias |
| S01 / NHK N / NHK W / S19 | 60 /48 /43 /20 token đúng miền số đã có trong memo; không thêm W31/W32/W34 |
| Token nguồn | 772 chuỗi riêng biệt cả sources+banks; không có book_id lạ, không thấy số ngoài miền trong các quy tắc nhận diện |
| Token chưa giải chính thức | 21 alias cần registry, gồm B07/B09/B11 và B12:A6; không kết luận21 token sai. 13 con trỏ ở mức nhóm/toàn nguồn cần cụ thể hóa, gồm S11:談話 và S16:STAGE* |
| HEADINGS_27.jsonl | 7.361 vị trí file/dòng tồn tại và trỏ vào dòng heading thật; không chứng minh nội dung heading hỗ trợ nghĩa gán |
| Chặng trống cả sources+banks | T-05,T-10,T-11,T-62,T-71,T-79,H-02,H-16; tình huống đều đã gắn AI. Không tự là lỗi bản khung, nhưng là việc chưa có nguồn khi dựng |

**Giới hạn của script:** quy tắc miền token được suy từ đầu mục thật và memo, chưa phải registry chính thức được kế hoạch cung cấp. Không thể dùng PASS miền số thay thế xác minh ngữ nghĩa. MD đã so ID/title/track/chuỗi tình huống; không tuyên bố máy đã giải ngữ nghĩa mọi ô nguồn hiển thị gộp trong MD. Những con trỏ sai nghĩa ở A02 do mở nguồn và đọc, không do phép đếm.

### Script kiểm tra đã chạy (read-only)

Chạy từ repo bằng Python, không có thao tác ghi. Kết quả chi tiết hiển thị alias/coarse thay vì giả vờ đã resolve hết:

```python
from pathlib import Path
import json,re,collections,hashlib
ROOT=Path.cwd(); V=ROOT/'kaiwa_skill/planning/v2'
rows=[json.loads(l) for l in (V/'KAIWA_CHANG_V4.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
byid={r['id']:r for r in rows}
manifest=json.loads((ROOT/'kaiwa_skill/planning/catalog27/manifest.json').read_text(encoding='utf-8'))
books={b['book_id']:b for b in manifest['books']}
heads=[json.loads(l) for l in (V/'index/HEADINGS_27.jsonl').read_text(encoding='utf-8').splitlines()]
# Read-only validation; aliases below are provisional contracts inferred from actual headings.
required={'id','level','cum','track','title','master_topic','situations','sources','banks'}
errors=[]; ids=[r.get('id') for r in rows]; seen=set();mdlines=(V/'KAIWA_CHANG_V4.md').read_text(encoding='utf-8').splitlines()
for n,r in enumerate(rows,1):
 if set(r)!=required:errors.append((r.get('id'),'unexpected_or_missing_keys',sorted(set(r)^required)))
 if r.get('id') in seen:errors.append((r.get('id'),'duplicate_id'))
 seen.add(r.get('id'))
 for key in ['id','level','cum','track','title','master_topic']:
  if not isinstance(r.get(key),str) or not r[key].strip():errors.append((r.get('id'),'invalid_string',key))
 if r['level'] not in ['Sơ','Trung','Thượng'] or r['track'] not in ['Đời sống','Công việc']:errors.append((r['id'],'bad_enum'))
 for key in ['situations','sources','banks']:
  if not isinstance(r.get(key),list):errors.append((r['id'],'not_list',key))
 if not r['situations']:errors.append((r['id'],'no_situation'))
 if set(r['sources'])!={t for s in r['situations'] for t in s['sources']}:errors.append((r['id'],'source_union'))
 for j,s in enumerate(r['situations'],1):
  if set(s)!={'title','sources','ai'} or not isinstance(s['ai'],bool) or not isinstance(s['sources'],list) or not isinstance(s['title'],str):errors.append((r['id'],j,'situation_schema'))
  if not s['sources'] and not s['ai']:errors.append((r['id'],j,'no_source_unmarked'))
  if 'AI' in s['sources'] and not s['ai']:errors.append((r['id'],j,'AI_token_but_false'))
tokens={t for r in rows for t in r['sources']+r['banks']}
unknown_ids=sorted(t for t in tokens if re.match(r'^B\d\d:',t) and t.split(':')[0] not in books)
bounds={1:7,2:45,3:20,4:35,5:8,6:4,10:8,15:15,16:7,19:4,21:20,22:20,23:20,25:8,26:10,27:10}
patterns={1:'C',2:'S',3:'U',4:'U',5:'ch',6:'',10:'',15:'L',16:'U',19:'P',21:'L',22:'L',23:'L',25:'',26:'',27:''}
bad=[];coarse=[];opaque=[]
for t in sorted(tokens):
 if ':' not in t:
  if t!='AI':coarse.append(t)
  continue
 b,k=t.split(':',1)
 if b.startswith('B'):
  bnum=int(b[1:])
  if bnum in bounds:
   prefix=patterns[bnum];mo=re.fullmatch(re.escape(prefix)+r'(\d+)',k)
   if mo and not 1<=int(mo[1])<=bounds[bnum]:bad.append(t)
   elif not mo:
    if bnum==2 and k in {'了解する','助言する','意思を表明する','相談する','確認する','許可を求める','話しかける','質問する'}:coarse.append(t)
    else:bad.append(t)
  elif bnum==13:
   if not (re.fullmatch(r'U[1-7][ab]',k) or re.fullmatch(r'U8-[1-8]',k)):bad.append(t)
  elif bnum==14:
   if not re.fullmatch(r'U[1-5]',k):bad.append(t)
  elif bnum==17:
   if not ((re.fullmatch(r'L\d+',k) and 1<=int(k[1:])<=14) or re.fullmatch(r'T[1-4]',k)):bad.append(t)
  elif bnum==18:
   if not (re.fullmatch(r'P1-[1-3]',k) or (re.fullmatch(r'P2-\d+',k) and 1<=int(k[3:])<=11)):bad.append(t)
  elif bnum==20:
   if not re.fullmatch('[A-Z]',k):bad.append(t)
  elif bnum==24:
   if not re.fullmatch('[A-S]',k):bad.append(t)
  elif bnum==8:
   mo=re.fullmatch(r'P([1245])-(\d\d)',k)
   if not mo or not 1<=int(mo[2])<={1:3,2:15,4:33,5:10}[int(mo[1])]:bad.append(t)
  elif bnum==12:
   if k=='A6':opaque.append(t)
   elif k not in {'P1','P2-A','P2-A6','P2-B','P2-C','P3'}:bad.append(t)
  elif bnum in [7,9,11]:opaque.append(t)
 elif b=='N':
  if not k.isdigit() or not 1<=int(k)<=48:bad.append(t)
 elif b=='W':
  if not k.isdigit() or int(k) not in set(range(1,47))-{31,32,34}:bad.append(t)
 elif re.fullmatch(r'S\d\d',b):
  sn=int(b[1:])
  if sn==1:
   if not (re.fullmatch(r'T[1-6]',k) or (re.fullmatch(r'A1-\d+',k) and 1<=int(k[3:])<=12) or (re.fullmatch(r'A2-\d+',k) and 1<=int(k[3:])<=19) or (re.fullmatch(r'B1-\d+',k) and 1<=int(k[3:])<=23)):bad.append(t)
  elif sn==4:
   if not re.fullmatch(r'T[4-9]',k):bad.append(t)
  elif sn==5:
   if not re.fullmatch(r'T[1-9]',k):bad.append(t)
  elif sn==6:
   if not re.fullmatch(r'C(?:[1-9]|10)',k):bad.append(t)
  elif k.startswith('STAGE') or k=='談話':coarse.append(t)
  else:
   hi={7:12,8:20,9:11,10:9,11:9,12:8,13:8,14:15,15:10,16:8,17:8,18:8,20:8,21:7,22:15}.get(sn)
   if sn==19:
    mo=re.fullmatch(r'U([1-6])-([1-4])',k)
    if not mo or not 1<=int(mo[2])<={1:3,2:4,3:4,4:4,5:3,6:2}[int(mo[1])]:bad.append(t)
   elif hi is None or not k.isdigit() or not 1<=int(k)<=hi:bad.append(t)
 else:bad.append(t)
# Index coordinates are checked against the actual clean Markdown.
index_bad=[]
for h in heads:
 p=ROOT/'kaiwa_skill/knowledge'/h['dir']/'chapters'/h['file']
 if not p.is_file():index_bad.append((h['book'],h['file'],'missing'));continue
 ls=p.read_text(encoding='utf-8').splitlines()
 if not 1<=h['line']<=len(ls) or not ls[h['line']-1].lstrip().startswith('#'):index_bad.append((h['book'],h['file'],h['line']))
actual_book_counts={b:sum(any(t.startswith(b+':') for t in r['sources']+r['banks']) for r in rows) for b in books}
coverage_gaps={}
for b in ['B21','B22','B23']:
 have={int(t.split(':L')[1]) for t in tokens if t.startswith(b+':L')}
 coverage_gaps[b]=sorted(set(range(1,21))-have)
print(json.dumps(dict(structural_errors=errors,unique_tokens=len(tokens),unknown_book_ids=unknown_ids,range_errors=bad,
  provisional_or_opaque_aliases=opaque,coarse_refs=coarse,index_rows=len(heads),index_errors=index_bad,
  book_counts=actual_book_counts,companion_lesson_gaps=coverage_gaps,
  book_token_counts={b:len({t for t in tokens if t.startswith(b+':')}) for b in books}),ensure_ascii=False))
```

## 5. Chủ đề/tình huống nên thêm, bỏ, gộp hoặc tách

Đây là đề xuất thay đổi phạm vi để duyệt, không phải một danh sách chặng thay thế đã xây. Không đề nghị thêm mới hàng loạt chỉ để đủ số200 hoặc đủ8–12.

### Bỏ khỏi cấp chặng hoặc chuyển thành chất liệu

- **T-44, H-40–42:** tháo thành ngân hàng B19/B20 dùng trong sức khỏe, kể trải nghiệm, quan hệ, công việc. [B19:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/02-part1.md:1>); [B20:1](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/02-section-a.md:1>). Giữ những đoạn hội thoại thực tế có mục tiêu; không bỏ kiến thức.
- **T-47:** bỏ mục tiêu học viết email như một chặng của khóa nói; hoặc đổi sang gọi xác nhận email/giải thích nội dung bằng lời. Nguồn của nội dung viết là [B03:25](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/18-Unit16-ビジネスEメール.md:25>). (Cách đổi thành nhiệm vụ nói là đề xuất biên tập [AI], cần nguồn lời thoại bổ sung.)
- **T-40/H-46/H-49:** không nhất thiết bỏ topic xin lời khuyên/bàn giao/họp; đưa các bước mở lời, nêu vấn đề, xác nhận, đồng ý… xuống dialogue_moves/banks. Chỉ đếm tình huống khi đổi đích/bối cảnh/điều kiện thực; memo S09/chương2, S16/chương3 hỗ trợ mạch và cách đồng ý.

### Gộp hoặc phân ranh rõ

- **T-19/T-23/T-24:** cân nhắc chặng xã giao và sự kiện nội bộ, hoặc tách rõ quà tặng / tổ chức tiệc / chuyến đi. Nguồn B21:L8,L10; B17:L5; B13:U5a có phần tiệc đã mở. Không dùng lại L8 ở hai chặng như hai nguồn mới.
- **T-65/T-66:** gộp phần khám bệnh; đưa phần nhân viên cửa hàng của U4a về mua sắm/dịch vụ. Chọn đúng U4b/scene12 cho xin thuốc sau sáu tháng, không tự suy thành thuốc dài hạn.
- **T-25/T-27/T-28 và T-48/T-57:** giữ riêng chỉ khi can-do và điều kiện khác nhau. Các nguồn quan hệ B13:U2a/U3a/U6a là pool dùng chung; tên quan hệ không tự tạo ra mục tiêu học khác.

### Tách/chuyển chỗ

- **H-58:** tách việc hỏi thủ tục/tài chính khỏi tham gia cộng đồng; phần máy bán hàng tự động/cửa hàng tiện dụng từ S22/bài10 chuyển về sinh hoạt/mua sắm. Thuế/cư trú/bảo hiểm hiện chủ yếu [AI] và cần nguồn quy trình hiện hành nếu giảng kiến thức, không gán cho sách khi không có.
- **H-03:** chuyển tình huống chương trình telesales sang H-19/chào bán hoặc nhánh thuyết trình sản phẩm. Token B13:U8-6 đúng nội dung telesales.
- **H-34:** cân nhắc đặt cạnh công tác/nhận vị trí mới; tách thiếu giấy tờ thông quan khỏi hủy chuyến/hành lý và nhận đội mới. Phần thông quan có nguồn B13:U6b/scene11; các phần AI vẫn phải ghi AI.
- **H-59/T-55:** đổi nguồn học thuật sang B18:P2-1/scene4 tại [B18:47](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md:47>); B18:P2-2 giữ cho thư viện ở S-12 phù hợp ngữ cảnh, không làm chứng cứ nghiên cứu.

### Làm rõ các tình huống hữu ích đang bị ẩn dưới nhãn rộng

- **Báo dị ứng/kiêng và xác nhận thành phần:** nên có can-do rõ ở S-18/T-73 và nhánh nhân viên T-72. Có nguồn B05:ch2 tại [B05:175](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/03-ch2-inshokuten.md:175>); câu từ vai khách cần chọn/biên tập riêng. Không coi đây là miền hoàn toàn vắng trong V4.
- **Không mang giấy tờ khi đi khám, hỏi cần làm gì:** nên có đầu mục rõ ở S-30/T-65. Có câu nguồn B08:P4-12 tại [B08:347](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md:347>); thông tin giấy tờ hiện hành phải kiểm riêng, không học thuộc một thủ tục cũ như quy định.
- **Báo mất và xin cấp lại thẻ tích điểm:** đưa vào T-61/H-14 bằng nguồn B13:U4b/scene5 tại [B13:205](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md:205>). Mở rộng sang khóa thẻ ngân hàng/điện thoại là [AI] và cần nguồn khác; không coi mọi loại thẻ có cùng quy trình.
- **Từ chối hoặc giới hạn làm thêm giờ khi đã có hẹn:** làm rõ can-do ở T-38/S-25 theo mức khó. Nguồn B02:S25 tại [B02:84](<D:/CODE/git/kaiwa_skill/kaiwa_skill/knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/10-断る.md:84>) đã có trong liên kết T-38, nên đây là làm rõ độ phủ, không thêm chặng để đếm lại.
- **Tìm hỗ trợ khi bị quấy rối, khi điều kiện làm việc không như thỏa thuận; báo nghi bị lừa đảo:** [AI] nếu thêm tình huống thao tác thực tế. Tìm tên/cảnh hiện tại chưa thấy các mục rõ đó; không khẳng định sách hoàn toàn không nhắc vì chưa đọc sâu toàn bộ. Đặt mục tiêu giao tiếp an toàn và đầu mối hỗ trợ, không tự giảng luật hoặc xử lý chuyên môn.

**Không coi là miền đang thiếu hoàn toàn:** thuê nhà đã có S-07/T-01/H-09; bảo hiểm/thuế T-05/H-08/H-58; con cái/trường học T-51–55; thiên tai S-33/34/T-68; hàng xóm S-09/T-28/29/H-10. Vấn đề cần giải là nguồn cụ thể, can-do, mức khó và độ sâu; chưa có bằng chứng để tăng chặng chỉ vì những tên miền này.

### Pilot nên phát hiện rủi ro theo thứ tự nào

1. **S-18 end-to-end:** một tập Lõi nhỏ nhưng có nghe, câu mẫu, audio từng vai, chấm âm, R1 và chuyển dữ kiện; chọn nguồn có quyền sử dụng rõ. Đo thời lượng thực, khả năng hiểu trước shadowing và số lần lặp tới ngưỡng.
2. **T-15:** R2 với người cần gặp vắng/bận, nghe không rõ, số/tên, chuyển máy; thử nhiều đáp án đúng khác mẫu và một nhánh ngoài dự kiến. Kiểm điểm âm tách điểm nhiệm vụ.
3. **H-13:** khiếu nại với giới hạn thẩm quyền, khách không đồng ý, lời xin lỗi phù hợp; R3/Live phải đạt mục tiêu chứ không trả lời giống bản mẫu.
4. **Kiểm vận hành và tái dùng:** thêm một chặng liên quan dùng lại vocab, đổi thứ tự, sửa một câu sau QA; ngắt giữa bước, tranh chấp claim và master. Chỉ mở rộng sau khi dữ liệu/tiến độ không hỏng và reviewer kiểm lời thoại. Không dựng Lõi cả200 trước khi các phép thử này qua.

Rủi ro lớn nhất là tạo ra một kho có vẻ đủ chặng/đủ nguồn nhưng sai ngữ cảnh, quá khó hoặc chấm sai; schema chưa ổn làm chi phí sửa lan sang hàng trăm chặng. Ngân sách pilot cần đo theo output thực và tỷ lệ sửa, không theo số worker hay số chương gắn.

## 6. Những gì chưa kiểm tra được hoặc còn không chắc

- Không đọc sâu từng câu của cả27 sách; không quay lại PDF/ảnh để xác nhận chất lượng ingest. 49 chặng là mẫu có chủ đích, không ngẫu nhiên đại diện để suy tỷ lệ lỗi.
- Không xác nhận đầy đủ8–12 tình huống, mọi từ/mẫu/kiến thức độc đáo hoặc chất lượng lời thoại đích: các artifact đó chưa có trong phạm vi review.
- Không chạy app, nhận diện tiếng nói, chấm âm, audio thực hoặc Live AI; chưa có số đo latency, độ chính xác, completion/retention hay ngân sách40–80k token/chặng. Các nhận định thời lượng/chi phí là đánh giá tính đủ của thiết kế, không phải kết quả thử người học.
- Không xác minh từng mục ngữ pháp trong bunpou/Minna hoặc chứng nhận level bằng JLPT/CEFR. Nguồn JLPT được mở chỉ để xác nhận giới hạn của phép quy chiếu sang năng lực nói.
- Không đọc toàn văn các sách/khóa chỉ có memo; không xác minh quyền text/audio, giấy phép, hợp đồng hoặc pháp luật của tất cả thị trường app. Phần quyền là đánh giá rủi ro có nguồn chính thức, không kết luận pháp lý từng tác phẩm.
- Không kết luận mọi bank rộng là gán sai, mọi chặng giống tên là trùng, hay ba câu trong một phần sách đủ chứng minh toàn chặng; đã tách những kết quả đó ở §3.
- Đã đọc hai plan để hiểu lịch sử; PLAN_V2 tự đánh dấu bị V2.1 thay thế. Không dùng yêu cầu đọc toàn văn4–6M token, 125 worker hoặc các chặng cũ làm tiêu chuẩn vận hành hiện hành. Không dùng/sửa V3.

### Snapshot đầu vào của review

Hash SHA-256 của bảy file đầu vào, ghi để phát hiện đổi phiên bản sau review; các liên kết dòng chỉ có nghĩa với snapshot này:

```json
{
  "KAIWA_CHANG_V4.md": "17fbf8dda5d5b31461f22085f8a75c0ce3ab1208b8a7393300773a92840b895d",
  "KAIWA_CHANG_V4.jsonl": "74925584c87a3cefbf06e1d0ec184b051a016e3f8211a72d799b6ac585b7cf5b",
  "KAIWA_SKILL_DESIGN_V1.md": "a596d5515918fc5745c928fa9e9cb8e35a90c4e1e93ac48df12215ee9f88023e",
  "PLAN_V2_1_LO_TRINH_RE_HON.md": "b423ab2f299d6ea4e7462358e07e4dcec733cd0d6c0b7bd130d6be3a50722fc3",
  "PLAN_V2_KAIWA_LO_TRINH.md": "00768b9889268c787155b2f27ea9935f13f5c69e75c43a5e4822531cfc7f3566",
  "index/TOC_27_BOOKS.md": "16fdc3a622853a3794ea597265b12fb0c5c48fd3d5c7fc94f9a9a762bad581af",
  "index/HEADINGS_27.jsonl": "d7db2728c87baea1e842f94504cd4fc06c552c9a48c489f4c050ea867448794a"
}
```

### Nguồn ngoài repo đã đối chiếu

- [JLPT — Four Key Characteristics](https://www.jlpt.jp/e/about/points.html): JLPT không đo trực tiếp nói/viết; chỉ dùng khi nhận xét level, không coi là chứng minh phương pháp học.
- [Agency for Cultural Affairs — Overview of the Copyright System](https://www.bunka.go.jp/english/policy/copyright/system/): biểu đạt/ý tưởng, quyền dịch/chuyển thể và các quyền khai thác.
- [JCO — General Understanding on AI and Copyright in Japan, Overview, May2024](https://www.bunka.go.jp/seisaku/bunkashingikai/chosakuken/workingteam/r06_01/pdf/94080501_11.pdf), trang12–13: tương đồng/phụ thuộc và phân biệt tạo nội dung với sử dụng. Tài liệu là hướng dẫn giải thích, tự nêu không có tính ràng buộc pháp lý.

Không có thay đổi nào được thực hiện vào V4, thiết kế skill, index, knowledge, corpus, PDF hoặc bunpou trong lượt review này.

