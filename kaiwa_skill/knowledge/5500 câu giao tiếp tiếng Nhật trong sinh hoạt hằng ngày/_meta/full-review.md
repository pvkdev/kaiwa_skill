# Rà soát toàn sách — 2026-11-11

## Phạm vi và phương pháp

- Nguồn chính: PDF 136 trang vật lý, SHA-256 `c8933782539c7bbe8ac755f2278bb7a6d7cf0d9165843c9ef14a198993b1825a`. Corpus đang dở chỉ hỗ trợ tra chữ; provenance của sách là PDF trực tiếp.
- Đã mở và đối chiếu ảnh từng trang PDF1–136, gồm cả hai nửa của mỗi spread. Evidence `_meta/pdf-pages/pNNNN.json` có hash ảnh, block included/excluded, unit và trạng thái. Ranh giới chương trên PDF38/66/99/112/122/127/136 đã được tách theo trang in thật; PDF136 trái là năm mục từ cuối, phải là colophon.
- Đã so thứ tự bảy phần học, các câu mẫu, đối thoại, diễn đạt tương tự/mở rộng, bảng từ và thông tin xuất bản. Những lời Việt in sẵn đảo nghĩa/phủ định, sai chủ thể, sai số hoặc bỏ chiều so sánh đã được sửa theo câu Nhật. Không điền phần Nhật bị scan cắt từ romaji hoặc lời Việt.

## Đếm nội dung thực trong PDF này

- 9 chapter files, 141 units có ID duy nhất, evidence cho 136/136 trang. Có 268 vùng nguồn included và 259 vùng excluded có lý do (romaji/furigana phụ trợ, header/footer lặp và hình trang trí).
- 1.188 câu mẫu đánh số: Cảm xúc 241; Nguyện vọng 285; Ý kiến/quan điểm 295; Vận động 128; Ẩm thực 100; Điện thoại 51; Phương tiện 88. Mỗi dãy số trong tiểu mục liên tục; hai câu đầu của Cảm xúc được trình bày theo bố cục riêng của bản in. Ngoài các câu đánh số còn có đối thoại và cách diễn đạt tương tự/mở rộng, không gộp vào con số trên. Tên sách “5500” không dùng để suy số câu thực trong PDF.
- Có 1.697 cặp dòng `JP`/`VI` gắn nhãn và hai cặp đầu trình bày cùng dòng. Các bảng từ cuối phần được giữ riêng; không lấy lời dịch câu mẫu thay cho headword.

## Nguồn còn cần xem lại

- 76 trang `author_checked`, 60 trang `needs_review`, không còn trang `draft`/`pending`/`stale`. `needs_review` phản ánh 66 vấn đề nguồn ở block cụ thể; 25 trang có chữ Nhật bị vùng gáy che/cắt nên `text_complete=false`. Những bất thường in sẵn và gloss nguồn lệch nghĩa cũng được giữ cùng giải thích hẹp. Xem `_meta/source-issues.md` và evidence từng trang; không xem kết quả cho phép source issues là xác nhận mọi chữ nguồn đã rõ.
- Các trường hợp cuối sách gồm PDF118 thiếu đơn vị sau 一, PDF119 焼きできだ, PDF121/122 gloss từ sai, PDF127 gloss điện thoại lệch ngữ cảnh, PDF130 代用貨幣, PDF131 nhãn diễn đạt tương tự đặt hai câu taxi khác nghĩa cạnh nhau, PDF133 上海オーバー, PDF134 đuôi ありません và PDF135 gloss/mục từ không chắc. Chữ Nhật của nguồn không bị tự sửa.

## Audio và kiểm tra máy

- Bìa PDF1, trang tên PDF2 và lời đầu PDF5 nhắc CD–MP3; không thấy số đĩa, mã track hay mapping câu–track trong PDF. Inventory ở `_meta/audio.json` và `audio.md`; tệp âm thanh thực tế `not_checked`.
- `direct_progress build`: 9 chapters, 141 units, completion `source_issues_unresolved`. `validate --allow-source-issues`: 0 lỗi, 132 cảnh báo (cùng 66 issue được báo theo trang và unit). Không dùng cờ để hạ phạm vi.
