# Bằng chứng khảo sát nguồn bài 39

Khảo sát ngày 2026-11-25, phiên đọc công khai không đăng nhập. Đây là metadata kỹ thuật và nhận xét cấu trúc, không phải bản sao nội dung giáo trình. URL nguồn:

- [Trang bài](https://www.vnjpclub.com/minna-no-nihongo/bai-39.html)
- [Ngữ pháp/B](https://www.vnjpclub.com/minna-no-nihongo/bai-39-ngu-phap.html)
- [Văn mẫu/A](https://www.vnjpclub.com/minna-no-nihongo/bai-39-luyen-doc.html)
- [C/Kaiwa](https://www.vnjpclub.com/minna-no-nihongo/bai-39-hoi-thoai.html)
- [Nghe](https://www.vnjpclub.com/minna-no-nihongo/bai-39-luyen-nghe.html)
- [Đọc ngắn trong bài tập](https://www.vnjpclub.com/minna-no-nihongo/bai-39-bai-tap.html)
- [Đọc dài](https://www.vnjpclub.com/minna-no-nihongo/bai-39-25-bai-doc-hieu.html)
- [Kiểm tra](https://www.vnjpclub.com/minna-no-nihongo/bai-39-kiem-tra.html)

## Kết luận về cách tải

Web text extractor có lúc chỉ trả menu/header; `Invoke-WebRequest` trả 200 và khoảng 716 nghìn ký tự cho ngữ pháp nhưng không có nội dung lesson trực tiếp. DOM trình duyệt sau render hiển thị nội dung đầy đủ. Trang có wrapper `.ykhp-protected-content` với thuộc tính `data-ykhp`; phương án crawler là đọc DOM được website render bình thường, không tự giải mã/lách cơ chế bảo vệ.

Python urllib mặc định nhận 403 trong một lần thử. Trang bài tập gặp bước xác minh một lần nhưng lần mở bình thường sau đó hiển thị được. Không kết luận nguồn bị chặn vĩnh viễn hoặc cần đăng nhập dựa trên một lần truy cập.

Ngữ pháp có link công khai sang `bai-39-ngu-phap-ban-cu.html`. Chưa khảo sát nội dung bản cũ; không dùng nó làm fallback âm thầm. Ghi edition/page variant để tránh trộn số câu và mapping giữa các bản.

## 1. Ngữ pháp và B đã kiểm chứng trên bài 39

Root `.vnjp-mg#vnjp-mg`, `data-mg-lesson="39"`, `data-mg-drills="32"`.

- `#mg-panel-grammar .mg-point`: 6 điểm.
- Ngữ pháp có `.mg-line`, `.mg-ja`, `.mg-vi`, ruby/rt; 13 nút `.mg-say` cho ví dụ.
- `.mg-q`: 6 câu kiểm tra nhanh; `.mg-explain` ban đầu rỗng.
- `#mg-panel-practice .mg-part`: 8 nhóm `mg-b1` đến `mg-b8`.
- `.mg-drill`: 32 item, 4 item/nhóm, định danh `data-mg-drill`, ví dụ `b1-1`.
- Prompt: `.mg-drill-prompt`; pool thẻ `.mg-pool .mg-chip[data-p]`; bản trả lời `.mg-ans .mg-ans-body`.
- B4 có 5 ảnh trong nhóm (gồm phần minh họa); các nhóm B còn lại không có `img` trong DOM quan sát. Không suy ra toàn bộ các bài khác đều giống.
- Thẻ trong pool có cả phương án nhiễu. Thứ tự DOM/pool không phải đáp án.

Mapping sư phạm đề xuất, chưa được biên tập viên duyệt:

- B1 → Vて chỉ nguyên nhân/cảm xúc.
- B2 → Vなくて chỉ nguyên nhân.
- B3 → Aくて/Aで.
- B4 → Nで; cần chuyển thể tranh hoặc giữ chưa bật.
- B5/B6/B7 → ので, tách dạng động từ, tính từ/danh từ, và xin phép.
- B8 → Nで + ので. Cả bốn đáp án B8-1…B8-4 đều nêu sự kiện/nguyên nhân bằng danh từ + で, rồi nối mệnh đề bằng ので. Đặt B8 sau khi dạy đủ Nで và ので.
- 途中で là điểm thứ sáu; chưa thấy nhóm B chuyên biệt. Không tạo quan hệ giả để “đủ sáu mẫu”.

## 2. Audio ngữ pháp: có clip ghi âm, TTS cache và fallback

Root có `data-mg-tracks` là JSON map track key → URL. Nút ghi âm có `data-track` và `data-t` theo giây. Ví dụ quan sát track `rbk`, khoảng `5.51,8.03`; đó là clip trong file chung, không phải file riêng của câu.

Các track quan sát gồm B1–B8 trong `/wp-content/vnjp-minna-grammar/audio/bai-39/`, cùng track A3 và bunkei/reibun. Chỉ coi đây là URL đã thấy trong DOM, chưa xác minh tải/phát từng file.

Nút khác có `data-tts-key`, `data-tts-ready`. Root công khai `data-mg-tts-base` và `data-mg-tts`. JS nguồn cho thấy ưu tiên file cache khi ready, sau đó endpoint TTS, cuối cùng speech synthesis của trình duyệt. Không gắn một URL tưởng tượng cho fallback speech synthesis.

Đã tải thử track B1 của bài 39 và kiểm bằng FFmpeg. File MP3 dài 63,399184 giây, 44,1 kHz, 761.461 byte. Đoạn 24,71–27,25 giây của B1-1 giải mã thành công. File tạm đã dọn sau khi ghi hash và kết quả. Track Văn mẫu `rbk` trả HTTP 206, `audio/mpeg` và chữ ký ID3 khi yêu cầu 64 byte đầu. Các track khác mới xác minh ở mức tham chiếu. [Biên bản audio B1](../reports/audio-39-b1.json).

## 3. Đáp án và lời giải tải sau thao tác

Đã đọc hai script do chính HTML khai báo tại thời điểm khảo sát:

- `vnjp-minna-grammar-js`: `https://www.vnjpclub.com/wp-content/litespeed/js/fa24ddd8b8dfa17da8bda0a710482fa6.js?ver=e3238`
- `vnjp-answer-check-js`: `https://www.vnjpclub.com/wp-content/litespeed/js/eecb598d66e01fb47c4da987c7afae1a.js?ver=b6168`

URL hash có thể đổi; crawler phải discovery lại qua script ID, không hard-code hash.

Cơ chế quan sát trong mã client: form POST tới URL AJAX cấu hình, `action=vnjp_answer_check`; các trường `op`, `source`, `lesson`, `items`, locale. API client có `check`, `reveal`, `restore`; ngữ pháp dùng source `minna-grammar-quiz` và `minna-grammar-drill`. Renderer đọc các trường như `reveal_html` và `explanation_html`.

**Kết quả chạy thực tế.** Ở giao diện, vùng đáp án B1-1 từng còn rỗng sau khi nhấn. Dùng cấu hình client của trang hiện tại và thao tác đọc `reveal`, máy chủ trả JSON cho cả 8 nhóm, mỗi nhóm 4 item. Tra theo `items[source_item_id]`. Cả 32 item có `answer`, bản dịch trong `.mg-vi` và clip kèm track + thời điểm đầu/cuối. Cả 32 có `explanation_html` rỗng. Ngược lại, mẫu kiểm tra nhanh `vte-nguyen-nhan-1` trả đáp án và 203 ký tự HTML giải thích. Khi parse đáp án quiz, tách ruby/rt để giữ chữ cơ sở. [Biên bản theo từng ID và mẫu Nhật–Việt](../reports/lesson-39-renshuu-b.json).

Chạy lại bằng `pwsh -File scripts/audit_b39.ps1`. Script chỉ yêu cầu các ID trong inventory bài 39, dùng cấu hình phiên trong bộ nhớ và ghi biên bản sau khi nhận đủ các nhóm. Khi thứ tự thẻ bị trộn, đối chiếu câu đáp án với thẻ trong pool. Nếu nhiều cách ghép cho cùng văn bản, giữ các phương án hoặc đưa vào danh sách biên tập.

## 4. Shadowing: selector phải hẹp

- `#mr-bunkei`: 3 câu Văn mẫu, lấy.
- `#mr-reibun`: 15 câu Ví dụ, **bỏ theo phạm vi hiện tại** dù nằm cùng tab “Văn mẫu · Ví dụ 18 câu”.
- `#mr-a1`, `#mr-a2`, `#mr-a3`: 6, 2, 7 câu; tổng 15 câu A, lấy.
- Tab Kiểm tra: 10 câu, bỏ.
- Có `<audio class="mr-track">`, cả file bunkei/reibun và A1–A3; có media fragment `#t=start,end` ở audio của phần kiểm tra.

Kết quả mong đợi cho scope shadowing bài 39: 18 câu, không phải 33 câu. Cần giữ cấu trúc nhóm A, thứ tự và ánh xạ câu–dịch–audio; chưa xác minh toàn bộ timestamp của A.

## 5. Hội thoại

- `#mk-kaiwa`: 12 câu có nút nghe, nằm trong các lượt nói; đặt cuối phần hội thoại.
- `#mk-c1`, `#mk-c2`, `#mk-c3`: 12 câu/nhóm, 36 câu C tổng cộng. Phải tách mẫu/biến thể khi parse, chưa chốt số biến thể bằng phép chia số câu.
- `.mk-line-tools .mk-play` là điều khiển câu; không lấy text nút làm transcript.
- Kaiwa dùng URL `/Audio/minnahonsatsu2/40.mp3` tại bài 39. Đây là bằng chứng **không suy filename từ số bài**.
- C có các URL trong `/Audio/minnarenshuc/`; một số `<audio>` là clip của tab quiz, cần tìm association đúng thay vì lấy tất cả audio theo thứ tự.
- Tab Kiểm tra 10 câu thuộc trang hội thoại nằm ngoài scope.

## 6. Nghe

Root family `ml-*`. `#ml-panel-practice` có bốn section `#ml-c1`…`#ml-c4`; 11 mục bài làm với phân bố 3/2/3/3. Mỗi section còn có ví dụ (`.ml-item--ex`), không tính ví dụ như câu cần chấm. Mục `#ml-c1-1` có `data-ml-item="c1-1"`, track `t1` và khoảng 49,21–91,21 giây. Đây là clip cho cả mục. Chỉ ghi clip cho từng lượt trong transcript nếu nguồn trả thêm mốc tương ứng.

Quan sát bốn audio tại `/Audio/minnaln/minna2/b/18B-18.mp3` đến `21B-21.mp3`. DOM có `<details class="ml-script">`, nhãn Script & dịch nhưng `.ml-script-body` ban đầu rỗng; nút `[data-ml-reveal]` ban đầu ẩn. Transcript/dịch/đáp án vẫn cần xác minh tải sau tương tác; không coi summary của details là transcript. Tab kiểm tra bổ sung 10 câu của trang này không tự đưa vào scope nghe.

## 7. Đọc ngắn và đọc dài

Trang bài tập: chọn `#mx-p7.mx-sec--read`, bài đọc về trang phục, 3 đoạn có nút nghe và 4 câu hỏi gắn bài đọc. Các section `mx-p1`–`p6`, `p8` không lấy. Hai file audio `/Audio/minnahonsatsu2/41.mp3`, `42.mp3` nhìn thấy trên toàn trang thuộc phần nghe; **chưa chứng minh đó là audio của bài đọc**. Không gán chúng cho `mx-p7`.

Trang 25 bài đọc hiểu: root `#vnjp-mtp`, `#mtp-panel-read` có 11 đoạn (`mtp-b-p1`…`p11`), tab câu hỏi 9 câu. Tab 46 từ vựng và tab mở rộng 5 câu nằm ngoài scope. Không thấy thẻ audio tại lần đọc DOM; nút phát có `data-a`, `data-ready`, vì vậy URL/provider cần xác minh riêng. Không kết luận “không có audio” chỉ vì không có thẻ `<audio>`.

## 8. Kiểm tra: ranh giới theo Mondai

Root `#vnjp-mt`. Trong `.mt-sec[data-section]`:

- Mondai 1: `goi-1`.
- Mondai 2: `goi-2`.
- Mondai 3: `kanji-1`.
- Mondai 4: `kanji-2`.
- Mondai 5: `bunpo-1`.
- Mondai 6: `bunpo-2`.

Trang còn Mondai 7–12, gồm sắp xếp, giao tiếp, nghe và đọc: bỏ toàn bộ. Sáu heading kỹ năng lớn không đồng nghĩa với Mondai 1–6. Giữ câu hỏi vocab/kanji thuộc sáu Mondai này dù không crawl **danh sách** từ vựng.

Đã đếm `.mt-item[data-item]` trong từng nhóm. Mondai 1–6 có lần lượt **5, 5, 5, 5, 5, 4 câu**, tổng **29 câu** trong 50 câu toàn trang. Pilot cần kiểm tiếp đáp án và lời giải theo từng ID Mondai.
