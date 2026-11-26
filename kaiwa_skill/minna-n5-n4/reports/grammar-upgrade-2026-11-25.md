# Nâng cấp bài giảng Harumii N5–N4 · 2026-11-25

## Phạm vi và đầu ra

- Đã đọc hợp đồng `materials/grammar/HUONG-DAN-AI.md`, skill biên tập và đối chiếu bài 39 tại `authored/lesson-39/review.md`, `references/SOURCE_AUDIT_39.md` và `catalog/grammar-points.json`.
- Đã rà **cấu trúc bằng script trên toàn bộ 180 bản gốc**: 90 N5 và 90 N4. Inventory từng file nằm ở `grammar-upgrade-2026-11-25-audit.json`. Đây là rà máy về front matter, số ví dụ, heading và ảnh; **174 file chưa được duyệt sâu về ngữ nghĩa**.
- Đã biên tập và đóng gói **6 bài cùng UUID cũ**, gồm **4 bài liên quan bài 39** và 2 bài có lỗi chắc chắn khác. Không thêm bài mới, không đổi cấp hay tên file.
- Gói upload: `exports/grammar-upload/2026-11-25.zip`; nguồn biên tập: `authored/grammar-upload/2026-11-25/`. Chạy `py -X utf8 scripts/grammar_upload.py authored/grammar-upload/2026-11-25 exports/grammar-upload/2026-11-25.zip` thành công: `6 existing, 0 new`.

## Quyết định biên tập

- `61594c26` · **Cách sử dụng て／で** (N4): phân rõ trình tự, nguyên nhân và liệt kê; giữ cả cách dùng Vなくて và Nで trong phần giải thích. Giữ 18 ví dụ. Sửa câu thiếu は ở 木村さんは会社員で; chuyển lời dẫn “gặp lại sau mười năm” ra khỏi dòng Nhật H5, đồng bộ câu/dịch. Sửa bản dịch tự thêm “ăn trưa” cho ご飯 và chính tả Shinkansen.
- `447866c5` · **Trợ từ で** (N5): giữ đủ 30 ví dụ và tách địa điểm, phương tiện, nhóm người, biến cố, giá/thời gian, phạm vi; giải thích riêng きれいで／ベトナム人で và でも／では để tránh coi tất cả là cùng một trợ từ đơn. Sửa câu tai nạn và bản dịch “hôm nay” không có trong Nhật.
- `d740c696` · **～ので～** (N4): giữ 9 ví dụ, sửa mẫu chia **Aな・N＋なので** và **ますので**, sửa câu hỏng `時ご会社へ 行 きます` thành `２時ごろ会社へ行きます` theo bản dịch gốc “khoảng 2 giờ”. Câu về bài thi được chỉnh để “tối nay” và “ngày mai” nhất quán.
- `3fd64d53` · **～途中で** (N4): giữ 13 ví dụ và đủ ba dạng Vる, Vている, Nの. Sửa năm câu Nhật có vị trí/động từ hoặc quan hệ chủ ngữ không tự nhiên (quên vở ở nhà, đang suy nghĩ, để quên đồ ở lớp, điện thoại của giám đốc, người quen đến nhà), kèm bản dịch tương ứng.
- `02683e06` · **ようと思います／つもりです／予定です** (N4): giữ 4 ví dụ và sắc thái ý định/kế hoạch. Bỏ kết luận sai rằng `早く寝るつもりです` luôn sai; giải thích hoàn cảnh dùng từng mẫu. Các câu Nhật đúng được giữ nguyên.
- `345b2e7c` · **đi/đến để làm gì** (N5): giữ 6 ví dụ, sửa tên và cấu trúc sai `[Địa điểm] を V にいきます` thành địa điểm **へ／に**, mục đích **Vます bỏ ます＋に** hoặc **N chỉ hoạt động＋に**. Làm rõ を chỉ gắn với tân ngữ như 昼ごはんを.

## Kiểm không mất nội dung

- Script `scripts/grammar_upgrade_20261125.py` giữ ánh xạ từng ví dụ gốc theo chỉ số, ghi rõ chỉ số có chỉnh trong JSON audit, và so lại toàn bộ cặp Nhật–Việt đã sinh với bản gốc cộng các sửa đổi khai báo. Tổng cộng **80/80 cặp ví dụ** của 6 bài còn hiện diện; không bài nào trong batch có ảnh. Các mục lớn đúng của bài gốc được giữ ở cấu trúc bài mới, dù một số mục được đổi tên hoặc tách để phân biệt cách dùng.
- Validator upload đã kiểm front matter, UUID/cấp/tên file, H1/nghĩa/cấu trúc, cặp H5/H6 và ZIP. ZIP chỉ chứa sáu file đã chọn. Admin vẫn cần xem bản New và diff trước khi áp dụng trong Harumii.

## Coverage và phần còn khó

- Trên 180 bản gốc có **3 file thiếu H1**, **1 file có H4**, **39 file không có blockquote nghĩa ở phần đầu**, **35 file có số dòng H5 và H6 không bằng nhau**, **9 file có tổng cộng 23 ảnh**. Đây là cờ rà máy, chưa phải kết luận 35 file mất bản dịch: một số H5 có thể là bảng chia hoặc hội thoại cũ. Danh sách từng file ở JSON audit để ưu tiên duyệt tiếp.
- Các 174 bài còn lại giữ nguyên baseline trong lượt này. Riêng các bài có ảnh hoặc bảng chia cần đối chiếu từng hình/bảng trước khi chuẩn hóa để tránh làm rơi nghĩa; không chuyển hàng loạt bằng regex.
- Mục `で` vốn gộp dạng nối tính từ/danh từ, trợ từ đơn và tổ hợp `でも／では`; batch vẫn giữ các ví dụ này với nhãn phân biệt. Mục `て／で` bao trùm nhiều cách dùng ngoài bài 39, nên không rút còn riêng nguyên nhân.
- Mapping bốn UUID bài 39 dựa trên hồ sơ biên tập lesson 39 và trang nguồn VNJPClub đã khảo sát. Chưa có phê duyệt sư phạm cho toàn bộ lộ trình 50 bài; ZIP là đề xuất để admin so sánh, không phải bản đã import.

## Batch 2: chuẩn hóa hợp đồng cho phần còn lại

- Đã chạy `scripts/grammar_upgrade_structure.py` trên **174 bài còn lại**, ghi từng UUID và trạng thái vào `reports/grammar-upgrade-2026-11-25-structure-audit.json`.
- **62 bài** có prelude, cấu trúc và cặp ví dụ đủ rõ được chuyển đổi vào `authored/grammar-upload/2026-11-25-structure/`, đóng gói thành `exports/grammar-upload/2026-11-25-structure.zip`. Validator trả `62 existing, 0 new`; ZIP có đúng 62 member, không trùng 6 UUID batch đầu, tất cả khớp byte với authored.
- Chuyển đổi chỉ sửa layout: H1 trùng `name`, blockquote nghĩa, nhóm cấu trúc có `<br>`, đánh số H5/H6 liên tục và đặt H6 ngay sau H5. Các dòng ở phần giải thích còn lại được giữ theo thứ tự. Một bài có `description` trống được điền bằng chính câu nghĩa có sẵn ở đầu bài. Script so sánh chính xác **879 cặp câu Nhật–dịch Việt** sau khi bỏ số thứ tự và khoảng trắng rìa; không có ảnh trong 62 bài. Đây là kiểm **bảo toàn**, không chứng minh 879 câu đều đúng về ngữ nghĩa.
- **112 bài** vào hàng chờ có ID và lý do trong audit: 48 thiếu hoặc dùng kiểu heading cấu trúc khác; 36 H5 không phải câu được đánh số chuẩn (gồm hội thoại hoặc bảng chia); 8 phần mở đầu nhiều nội dung; 7 H1 khác tên; 7 H6 không liền cặp; 3 cấu trúc phức tạp; 2 H6 lẻ; 1 nghĩa đầu bài khác front matter. Nhiều bài có hơn một vướng mắc; audit ghi lý do đầu tiên khiến phép chuyển đổi dừng. Cần biên tập thủ công trước khi upload, đặc biệt 9 file có ảnh trong tập 174.

## Quickcheck bài 18–34

- Đã đọc từng prompt/choice trong `normalized/lesson-18` đến `lesson-34` và ghi `authored/quick-checks/keys-18-34.json`: **137 record**, gồm **136 đáp án với giải thích tiếng Việt riêng** và **1 issue**. Script `scripts/grammar_upgrade_quickchecks.py` kiểm đủ mọi `source_id` và ID phương án tồn tại trong câu tương ứng.
- Issue ở bài 34 `toori-ni-2`: `見たとおりに` là dạng giáo trình mong đợi, nhưng `見ましたとおりに` có thể dùng trong ngữ cảnh trang trọng; prompt chưa giới hạn văn phong. Cần sửa câu hỏi hoặc chấp nhận hai dạng trước khi chốt đáp án.
- Mức rà ngữ nghĩa trong lượt này: 6 bài giảng batch đầu và 137 quickcheck. Batch 2 chỉ được duyệt cấu trúc và bảo toàn văn bản; 112 bài còn lại mới có audit máy và danh sách chờ.

## Xác minh tái lập và rà chéo quickcheck

- Tái sinh batch 2 từ thư mục xác minh sạch, chạy lại validator và đối chiếu: **62/62 file authored, 62/62 member ZIP, toàn bộ audit JSON giống bản bàn giao theo nội dung**. Đã dọn bản xác minh tạm. SHA-256 của ZIP bàn giao: `68d88aba76f74140ed4a8e0120e7dd01f651190061df58c1db1b0566f6391248`.
- Rà chéo `authored/quick-checks/keys-35-50.json` với từng prompt và phương án trong `normalized/lesson-35` đến `lesson-50`: đủ **105/105 câu**, ID không trùng, mọi đáp án trỏ đúng choice và có giải thích Việt. Các ca dễ đa nghĩa tại bài 35 `wa-arimasenka-1`, bài 39 `node-1` và bài 41 `te-kudasaimasenka-1` đã có `prompt_override` trong khóa của root để giới hạn cách hiểu. Chưa thấy thêm đáp án sai rõ ràng trong lượt rà chéo này.

## Batch N4 biên tập từ hàng chờ

- Từ **59 bài N4** còn hoãn sau batch cấu trúc, đã đọc cấu trúc/mục lớn và xét từng cặp ví dụ. **28 bài** có đủ căn cứ được sửa thành `authored/grammar-upload/2026-11-25-N4-editorial/N4/` và `exports/grammar-upload/2026-11-25-N4-editorial.zip`; validator trả `28 existing, 0 new`. Batch này không trùng 68 UUID của hai ZIP trước.
- Với bài thiếu heading cấu trúc, `scripts/grammar_upgrade_n4_editorial.py` đặt cấu trúc riêng dựa trên cách dùng thực tế của bài, không dùng tên bài làm công thức. Phần giải thích, bảng chữ, ví dụ và chú thích gốc được giữ theo thứ tự. Hội thoại có nhãn A/B hoặc 客/店員 được tách nhãn vai ra dòng ghi chú trước cặp ví dụ. Tổng cộng **397 cặp Nhật–Việt còn hiện diện**, **17 ảnh giữ nguyên URL và vị trí**. Ngoại lệ có chủ đích: một bản dịch được sửa theo câu Nhật.
- Ba lỗi nội dung chắc chắn đã sửa: `来られる → 来られれば` thay cho lỗi gõ `来れれれば` trong bài điều kiện ～ば; `立ち入り禁止` nghĩa là **Cấm vào**, không phải “Không dẫm lên”; bỏ khẳng định ～かもしれません luôn là **50%** chắc chắn. Cách ghi một H5 có chữ in đậm được chuẩn hóa. Những sửa này có ghi trong audit của batch.
- **31 bài N4 còn chờ** nằm ở `reports/grammar-upgrade-2026-11-25-N4-editorial-audit.json` với UUID và lý do riêng từng bài: bảng chia từng được gắn H5, hội thoại có hai H5 rồi mới tới hai H6, dịch lẻ, phản ví dụ đánh dấu sai, hoặc bài tổng hợp nhiều cách dùng và câu Nhật hỏng. Bài `～いい` được giữ trong hàng chờ sau khi phát hiện nhiều câu hỏng và năm nhóm cách dùng khác nhau; không ép thành bài upload chỉ vì đủ số H5/H6.
- Sau ba ZIP đầu, coverage là **96/180 bài**, còn 84 bài chờ (31 N4, 53 N5). Mức rà ngữ nghĩa sâu ở giai đoạn này giới hạn ở batch sáu bài và các sửa cụ thể nêu trên; batch cấu trúc không được gắn nhãn đã duyệt sư phạm.

## Batch N4-final: biên tập hội thoại, bảng chia và phản ví dụ

- Từ 31 bài N4 còn chờ, đã xử lý **30 bài** thành `authored/grammar-upload/2026-11-25-N4-final/N4/` và `exports/grammar-upload/2026-11-25-N4-final.zip`. Validator trả `30 existing, 0 new`; ZIP không trùng 96 UUID ở ba batch trước. Fresh build từ thư mục sạch cho đúng 30 file, các member ZIP và audit JSON giống bản bàn giao theo nội dung. SHA-256 ZIP: `a02bbebd25c366fda88ab85dacf3ac48e5929ecfd9a37ea9cf4ba2c04760a756`.
- Script `scripts/grammar_upgrade_n4_final.py` nhận diện **70 H5 là công thức, mẩu thư hoặc phản ví dụ** và **12 H6 là ghi chú, không phải bản dịch**; các dòng này được giữ làm nội dung thường để không sinh furigana sai. Ví dụ còn lại được ghép theo cụm H5/H6 để xử lý đối thoại hai câu Nhật rồi hai bản dịch. **667 cặp trực tiếp** đã so lại với bản nguồn; tổng **795 cặp** hiện diện trong batch. **6 bản dịch Việt** được viết cho câu Nhật đọc hiểu được nhưng thiếu dịch. Ảnh duy nhất trong batch được giữ nguyên URL/vị trí.
- Ba bài câu hỏi gián tiếp `9959d2a0`, `47669f80` và nghĩa `173cd56e` được tách câu hỏi gốc, lời đáp và câu gián tiếp thành các cặp riêng; giữ cả hai biến thể hỏi nghĩa `何という意味ですか／どういう意味ですか`. Các ví dụ bổ sung đúng trong bài かどうか vẫn được giữ. Các mục rộng như bị động, kính ngữ, nguyên nhân, ところ, はず và んです vẫn giữ nội dung các cách dùng ngoài bài Minna đang luyện.
- Một bài N4 `a1bcb005` (**～いい**) còn chờ do có nhiều câu Nhật hỏng trong năm nhóm cách dùng; root nhận biên tập riêng. Audit `reports/grammar-upgrade-2026-11-25-N4-final-audit.json` ghi 30 file đã chuyển và lý do cụ thể của bài này.
- **Coverage mới nhất của lane này: 126/180 bài** trong bốn ZIP; **54 bài** chưa có bản nâng cấp (1 N4 do root xử lý, 53 N5). Không coi kiểm hợp đồng hoặc kiểm bảo toàn là duyệt sư phạm toàn bộ các câu gốc.
