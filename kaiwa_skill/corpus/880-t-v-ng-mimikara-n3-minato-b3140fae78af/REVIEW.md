# Nghiệm thu — Mimikara N3 Minato

Quyết định: ACCEPTED cho PDF `vocab/880 TỪ VỰNG MIMIKARA N3 MINATO.pdf` (đường dẫn từ `kaiwa_skill/`), 47 trang vật lý. Nguồn SHA-256 `b3140fae78afe369b2909847034d1b2b870e6114ee3c786588c5e3508f890ea0`. Worker `production_book_02`, gpt-6-sol/high; coordinator gpt-6-astra/high; skill 0.2.1.

## Phạm vi kiểm tra

Worker đã mở ảnh và đối chiếu từng trang 1–47, gồm các bảng, ô trống, quote, dải thương hiệu và Fanpage. Mỗi trang có evidence gắn hash; các sửa sau QA đã record/reverify. Sau release, trạng thái thực là 47/47 verified, không issue, không claim, build_current=true.

Coordinator đọc mẫu toàn bảng Nhật/Việt và bố cục ở trang 1, 4, 9, 19, 24, 29, 34, 40, 42, 47: bảng mở đầu có tiêu đề, bảng tiếp nối, chữ Hán/kana, Katakana với ô trống, từ ghép nhiều dòng và trang cuối. Vì lỗi dấu tiếng Việt lặp lại, phạm vi đã mở rộng: đọc trực tiếp cả hai cột tiếng Việt của tất cả 47 trang bằng crop phóng to, so từng hàng với Markdown. Những dấu nghi ngờ được crop sát riêng. Sổ `COORDINATOR_VIET_AUDIT.json` lưu hash từng trang, phát hiện, nội dung trước/sau và kết quả kiểm lại.

## Phát hiện và sửa

Lần xác nhận ban đầu của worker đã bỏ sót nhiều dấu nhỏ; không xem các evidence ban đầu là chứng minh bản chép đầu đúng hoàn toàn. Các lỗi gồm TIỀN/TIẾN, HỒN/HỖN, THỤC/THỰC, chữ thiếu dấu mũ hoặc hỏi/ngã, viết hoa sai, một dấu chấm thừa và chữ Giơ bị chép Gio. Trang 15 mục 273 từng thiếu cụm `thẳng thắn,`; đã khôi phục. Mẫu Nhật cuối phát hiện trang 47 mục 877 chép `まだ` thay cho nguồn `また`; đã sửa sau crop độc lập. Danh sách chi tiết đầy đủ nằm trong sổ QA; mọi phát hiện đã được kiểm lại trong Markdown cuối.

Header/footer cần đọc riêng: nhận định đầu về quote/Fanpage không có trên một số ảnh toàn trang đã bị rút sau crop nguyên vùng và đối chứng pixel nguồn. Không xác định được nguyên nhân khác biệt quan sát toàn trang/crop; không kết luận lỗi công cụ. Chữ `DOORIMU` nhìn thấy trên ảnh ghép cột là một nhận định sai khác: đường nối hai vùng x không kề nhau lặp hình chữ O. Crop nguyên dải trang 12 đọc rõ `MINATO DORIMU` bốn lần. Không áp dụng sửa sai này vào corpus. Các ghi nhận đã rút được tách khỏi lỗi nội dung thật.

Các cách ghi bất thường của nguồn được giữ, ví dụ `VU`, `TAO`, `HẾ KỈ`, `VÂN THUẬT`, `DƯ TƯỞNG`; không chuẩn hóa theo từ điển. Nhãn cột trên trang tiếp nối và nhãn mô tả dải thương hiệu là biên tập, đã đánh dấu rõ.

## Sản phẩm và giới hạn

Kiểm máy xác nhận số mục liên tiếp 1–880, không thiếu/trùng; chỉ mục có 47 block trang đầy đủ, chứa bảng và ngữ cảnh nguồn; book.md/search.jsonl được build từ bản hiện tại. Output chỉ text, không nhúng ảnh. `acceptance.json` gắn quyết định này với hash nguồn, từng Markdown, build và sản phẩm ghép.

Coordinator kiểm toàn bộ tiếng Việt nhưng chỉ lấy mẫu tiếng Nhật/bố cục như nêu trên; không tuyên bố đã kiểm độc lập toàn bộ tiếng Nhật. Worker chịu trách nhiệm đối chiếu 100% trang. Không còn khác biệt đã biết trong phạm vi đã kiểm; nghiệm thu này không phải bảo đảm tuyệt đối không còn lỗi chưa phát hiện.
