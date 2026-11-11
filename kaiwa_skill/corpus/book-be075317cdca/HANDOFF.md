# Bàn giao sách シャドウイング 日本語を話そう 初・中級編

- Nguồn: `kaiwa_skill/book/Shadowing/シャドウイング 日本語を話そう初_中級.pdf`
- SHA-256 nguồn: `be075317cdcab1bad0245126bf7c4fe9bb066fcb714bc19aa841f5373b612869`
- Book ID: `book-be075317cdca`; 145 trang vật lý.
- Worker lượt này: `production_book_13_root_cont3`; claim `production_book_13_root_cont3_20261111` đã release sau checkpoint.
- Checkpoint sau p0145: **66 verified, 79 needs_review, 0 pending, 0 rendered, 0 draft, 0 invalid**. p0117–p0145 đều đã mở ảnh trang gốc, chép nội dung và checkpoint. Các trang Nhật p0117, p0119, p0121, p0123, p0125, p0127, p0129, p0131, p0133 và trang trắng p0140 verified; các trang dịch, giải thích đa ngữ, colophon và quảng cáo cuối sách giữ needs_review theo issue.
- `reconcile` và `build` thành công sau p0145. `book.md`, `search.jsonl`, `build.json` phản ánh **66 trang verified**; `book_sha256: 6b98ebf459e49c959199d9b4005304695cc9b3b98af8ac5fd72e217c6687f79f`, `search_sha256: 14e38763156a2ff2b161765c539b895573d666226900293d942e984e4d7fc20c`. `transcription_complete: false`, `acceptance: coordinator_review_required`.

## Cách làm và trạng thái review

Mỗi trang p0001–p0116 đã mở ảnh trang gốc riêng; crop khi cần để đối chiếu ảnh→Markdown và Markdown→ảnh, gồm văn bản, ruby, nhấn mạnh, bảng, nhãn vai, track, khoảng trống và ngắt trang. Bản nháp/evidence và ảnh render nằm trong `.cache/renders/book-be075317cdca/`; corpus chỉ chứa văn bản, không nhúng ảnh. Worker verified chỉ là checkpoint sản xuất; coordinator nghiệm thu độc lập.

Các trang `needs_review`: p0008, p0012, p0015–p0018, p0020, p0024 và các trang chẵn kế tiếp trong bài học, cùng p0045–p0046, p0065–p0066, p0083–p0086. Xem issue chính xác theo từng trang trong `manifest.json`; không nâng trạng thái chỉ vì đã có bản nháp.

- **Mẫu in cực nhỏ:** p0008, p0012, p0016, p0020 chứa cùng dạng trang mẫu thu nhỏ. Hội thoại và ba cột dịch không đủ rõ để chứng thực từng ký tự, kể cả sau render/crop lớn; phần văn bản, callout và bảng đọc được đã giữ trong draft. Đây là giới hạn kích thước của mẫu in nguồn, tách biệt với vấn đề tiếng Thái.
- **Tiếng Thái:** nhiều trang bản dịch/giới thiệu in rõ, có draft phần đọc được, nhưng worker không thể chứng thực toàn bộ ký tự, nguyên âm và dấu thanh. Cần người đọc tiếng Thái rà chính xác theo ảnh nguồn, đặc biệt p0015–p0018 và các trang bài học. Tesseract cài sẵn với model `tha`: chế độ `psm 6` toàn trang làm rơi nhiều dấu; `psm 7` trên crop từng dòng cho draft tốt hơn nhưng vẫn sai. Không gọi các trang này là PDF hỏng/mờ; không sửa theo suy đoán từ bản Nhật/Anh.
- **p0085:** ruby tiếng Nhật đã rà lại từng lần xuất hiện theo crop nguồn scale 6, loại ruby thừa; root đối chiếu xác nhận 32 mục đúng nguồn. Trang vẫn `needs_review` riêng tiếng Thái; không nâng trạng thái vì review ruby.
- **Source quirks:** p0065 lời giải tiếng Indonesia mục 6 và 7 trùng nhau ngay trong bản in; giữ nguyên. p0064 dòng cuối tiếng Việt in nhãn `B`; giữ nguyên. p0074 dòng Thai row 2 B đã crop xác nhận không có `นี่`. Một số từ Latin bị ngắt dòng với gạch nối trong nguồn; xem note tại trang trước khi chuẩn hóa.
- **Lượt p0088–p0116:** các trang tiếng Nhật p0089, p0091, p0093, p0095, p0097, p0099, p0101, p0107, p0109, p0111, p0113, p0115 đã `verified`. p0103–p0104 là trang giải thích đa ngữ, p0105 là Column 2, p0106 là đầu Unit 5; tất cả đã có draft text đầy đủ và `needs_review` chỉ ở chữ Thái nhỏ. Các trang bản dịch chẵn p0088–p0102 và p0108–p0116 cũng có draft đầy đủ, `needs_review` có issue cụ thể trong `manifest.json`. p0104 có banner nhà phân phối được chép. p0110 mục 10 và p0116 mục 7: cột Việt thiếu nhãn vai ở câu cuối ngay trong bản in, nên để câu không nhãn và ghi chú biên tập. p0108 mục 5: Indonesia “mengopy-” bị ngắt dòng trước “nya”, đã nối thành “mengopynya”, issue yêu cầu QA xét gạch nối. Không diễn giải khác bản Nhật hay tự giải bài.

## Tiếp tục

Các trang vật lý đều đã có bản chép. Tiếp theo xử lý `needs_review` theo issue cụ thể, nhất là người đọc tiếng Thái đối chiếu ký tự và second-pass quảng cáo chữ nhỏ; rồi coordinator QA/acceptance. Không sửa `ROOT_AUDIT.json`, nguồn PDF, tools hoặc Git trong vai worker. Root giữ QA/Git và có thể tạo worker mới sau khi claim hiện tại release.

## Lượt p0117–p0145

- Trang Nhật p0117–p0133 số lẻ được mở toàn ảnh và crop độ phân giải cao, đối chiếu ruby đúng **lần xuất hiện/đoạn chữ**. Trang dịch số chẵn p0118–p0134 đã chép đủ các cột Indonesia/Thai/Việt đọc được từ ảnh; chưa chứng thực exact Thai, nên vẫn `needs_review`.
- p0135–p0137 là giải thích đa ngữ 1–16; chép theo từng ô và giữ `needs_review` vì Thai. p0138 là Column 3 phỏng vấn người học, bốn khối ngôn ngữ với Q, bốn bong bóng và kết luận; đoạn tiếng Việt cuối **lặp nguyên câu thứ nhất trong nguồn**, đã giữ. p0139 là tác giả/ấn bản, tên người dịch bằng Thai cần người đọc bản ngữ; p0140 là trang trắng đã verified.
- p0141–p0145 là quảng cáo sách của nhà xuất bản, bản chép gồm tiêu đề, tên tác giả, giá, ISBN, mô tả, các ô/nhãn và thông tin hình bìa đọc được. Chữ trên bìa và chi tiết in cực nhỏ cần second-pass; `needs_review` là để chỉ rõ phần chưa chứng thực. p0143 có dãy ISBN ở mục 「ストーリーで覚える漢字 II 301-500」 nhìn lặp với mục 「漢字300」 trong nguồn; không tự sửa theo sách khác. p0144 topic list có glyph nhỏ 機会/機械 cần xem lại crop.
- Không lấy OCR làm chứng cứ; `manifest.json` giữ issue cụ thể từng trang. Không có pending/draft/invalid, nhưng chưa đạt acceptance vì 79 trang needs_review.
