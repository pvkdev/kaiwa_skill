# KAIWA — Thiết kế skill dựng chặng (V2, gộp review độc lập)

Ngày: 2026-11-12 · Thay `KAIWA_SKILL_DESIGN_V1.md`. Đi kèm `KAIWA_CHANG_V4_1.md/.jsonl` (194 chặng) và `REVIEW_CODEX_V4.md`. Các mục B01–B11 trong ngoặc là mã phát hiện của báo cáo review.

Đây là bản **đề xuất để chốt**, chưa xây skill. Nguyên tắc chung: **pilot 3 chặng bằng quy trình thủ công trước, chốt schema v1 sau khi pilot qua**, rồi mới chạy hàng loạt.

## 0. Phạm vi

- Đây là lộ trình **luyện nói và nghe hiểu để nói**. Không có bài viết (email, văn bản). Chữ Nhật, furigana, bản dịch Việt chỉ là chất liệu hỗ trợ nghe và nói.
- Mỗi chặng là một topic rộng, không phải một loại biểu đạt. Các sách mẫu câu và biểu đạt (B06, B07, B09, B11, B12, B18, B19, B20, B24) là ngân hàng cách nói gắn vào chặng theo chức năng.
- Nguồn truy ngược được về 27 sách và memo web, nhưng nội dung trong app phải qua bước quyền sử dụng (mục 9).

## 1. Người học thấy gì

**Chặng:** mục tiêu can-do (3–5 câu), bản đồ tình huống đánh dấu Lõi và Mở rộng, cuối chặng có Live Kaiwa AI mở rộng, can-do check và ôn cách quãng.

**Bài = một tình huống**, chia thành hai phiên có thể làm riêng (B01):

| Phiên | Bước | Chấm phát âm | AI |
|---|---|---|---|
| Chuẩn bị (khoảng 6–8 phút) | 1. Nghe đoán ý, 2. Hiểu (thẻ kiến thức), 3. Từ và mẫu | bước 3 có | không |
| Luyện nói (khoảng 8–12 phút) | 4. Shadowing, 5. Đóng vai, 6. Tự nói, 7. Live mini | có | bước 7 (từ Trung) |

Thời lượng trên là **mục tiêu của pilot**, không phải tiêu chí kiểm tra nội dung. Pilot đo phút nghe và nói thật, số lần thử, tỷ lệ bỏ bài, độ trễ.

**Shadowing không khóa cứng.** Mỗi câu có tối đa 3 lần thử; hết lượt thì cho đi tiếp và đưa câu đó vào hàng ôn. Chỉ các "câu thiết yếu" (đã hiệu chuẩn, ví dụ xin lỗi, hỏi lại, báo khẩn cấp) mới là cổng cứng. Có nút nghe chậm, nghe từng cụm.

**Ba chỗ của Live Kaiwa AI:** mini cuối mỗi tình huống; mở rộng cuối chặng (khóa đến khi xong Lõi); kiểm tra cuối cụm. Ở Sơ, AI nói chậm, có gợi ý. Từ Trung có biến cố; Thượng có áp lực và ngầm ý.

## 2. Ba loại điểm, tách riêng (B02)

| Điểm | Đo gì | Không đo gì |
|---|---|---|
| Phát âm | âm, nhịp, độ rõ của từng câu so với câu chuẩn | có đúng ý hay không |
| Trôi chảy | tốc độ, ngắt nghỉ, ngập ngừng | đúng hay sai nội dung |
| Nhiệm vụ | đã đạt mục tiêu giao tiếp chưa (đủ thông tin, đúng điều kiện, đúng mức lịch sự) | phát âm |

Quy tắc: điểm phát âm **không** được dùng làm bằng chứng đạt can-do. Lỗi nhận dạng giọng nói (không có tiếng, độ tin cậy thấp) cho thử lại, không tính là lỗi người học. Lưu độ tin cậy của từng lần chấm. Cao độ (pitch accent) để giai đoạn sau, nhưng dữ liệu cao độ của câu chuẩn chuẩn bị sẵn.

**Hiệu chuẩn:** ngưỡng đạt do pilot và người Nhật có chuyên môn xác định, không đặt cảm tính. Pilot phải thử: câu khác mẫu nhưng đúng, câu phát âm tốt nhưng sai ý, câu bị nhận dạng nhầm.

## 3. Đóng vai và Live AI vận hành thế nào (B02)

| Mức | Cách chạy | Chấm |
|---|---|---|
| R1 có kịch bản | Audio vai A cố định; người học đọc đúng lời vai B | phát âm, trôi chảy |
| R2 có gợi ý | Gợi ý bằng tiếng Việt cho từng lượt; người học tự nói; mỗi lượt có **khoảng đáp án chấp nhận** (slot, ý định, các biến thể đúng). Cây nhánh tối đa 3 nhánh mỗi lượt, audio vai A có sẵn cho từng nhánh | cả ba điểm |
| R3 tự do và Live | Không có lời thoại cố định. AI vai A chạy theo **trạng thái nhiệm vụ**: mục tiêu của người học, biến cố ngầm, ràng buộc, điều kiện kết thúc | nhiệm vụ là chính; phát âm và trôi chảy theo từng lượt |

Nếu người học nói ngoài cây nhánh ở R2, hệ thống xác nhận lại hoặc chuyển sang Live, không phạt. Thẻ vai và persona AI là dữ liệu (mục 7), không phải văn bản.

## 4. Tình huống và độ phủ (B03)

**Định nghĩa tình huống:** vai nói với vai + đích đạt được + dữ kiện hoặc điều kiện + kết thúc quan sát được. Các lượt như "mở lời", "xác nhận", "kết thúc" là `dialogue_moves` bên trong một tình huống, không đếm là tình huống.

**Ma trận phủ mỗi chặng:** quan hệ × mục đích × biến cố × địa điểm hoặc kênh × độ tự chủ. Mỗi trục có danh mục giá trị; ô không áp dụng ghi N/A kèm lý do. Số tình huống là **mục tiêu mềm**: tối thiểu 6 độc lập, Lõi 4, tối đa theo nội dung; không ép 8–12.

Kiểm tự động: có đủ ô bắt buộc, không trùng cặp (vai, đích, biến cố), mỗi tình huống có điều kiện kết thúc. Người review quyết đúng, tự nhiên, nghĩa. Điểm phủ tự động không phải bằng chứng sư phạm.

## 5. Kiến thức và dữ kiện (B11)

Thẻ kiến thức viết theo **vai, mục đích, điều kiện**: "trong bối cảnh này, người nghe thường...", kèm cách nói thay thế và giới hạn. Không gán tâm lý chung cho cả một dân tộc. Với chặng có `fact_check` (y tế, thuế, bảo hiểm, cư trú, thủ tục): chỉ dạy **giao tiếp**; dữ kiện thủ tục tách thành mục "cần kiểm tra thông tin hiện hành" có ngày review. QA ngữ dụng gồm cách từ chối an toàn, xin xác nhận, không hứa quá thẩm quyền.

## 6. Từ vựng và ngữ pháp (B04, B05)

**Từ vựng**
- Khóa là `lexeme_id` + `sense_id` + cách đọc + loại từ + mức lịch sự, không phải mặt chữ. Dạy theo nghĩa và cách dùng.
- Xuất hiện (occurrence) ghi theo câu và đoạn. Có `assumed_known` và `recognition_only`.
- Mỗi từ có một chặng gốc. Nếu người học tới chặng khác mà chặng gốc chưa học, cho học tại chỗ.
- Vòng lặp: viết hội thoại → trích từ → sửa → kiểm tra đến khi ổn định. Không ép 80–150 từ chỉ cho đủ số.
- File từ vựng chung do **một bên ghi** (single-writer) hoặc hợp nhất có khóa, không để các worker tự chọn chặng gốc mâu thuẫn.
- Nguồn: hội thoại của chặng → 5500, Nama Chūkei, Roleplay → MINATO/MIMIKARA cùng chủ đề → AI bổ sung.

**Ngữ pháp**
- Mỗi tham chiếu gồm `pattern_id`, nghĩa và cách dùng, dạng chuẩn và dạng nói, productive hoặc receptive, điều kiện tiên quyết, nguồn, phiên bản. Bài Minna chỉ là con trỏ phụ.
- N3–N1 trỏ `bunpou_skill` (chỉ đọc). N5/N4 chờ danh sách Minna của người dùng; trong lúc chờ, chặng ở trạng thái `blocked: pending_grammar` và **không** được đánh dấu ready.
- Trần ngữ pháp ở Sơ: dựa trên danh sách mẫu đã khai báo và văn bản hội thoại thực, có danh sách cụm cố định (fixed chunks) được duyệt riêng.

## 7. Cấu trúc dữ liệu (B06, B07)

**ID.** Mỗi chặng, tình huống, câu, từ, mẫu có `uid` bất biến. Mã hiển thị (S-01), slug và thứ tự là thuộc tính tách rời; chèn hay đổi thứ tự chỉ đổi thứ tự. Khi tách hoặc gộp chặng: ghi alias và tombstone, cập nhật khóa ngoại, xử lý thẻ ôn và tiến độ theo phiên bản. V4.1 đã có `uid` và `chang_registry.json`.

**Thư mục** theo `uid` để không vỡ khi đánh số lại:

```
kaiwa_content/
  _meta/  schema/, registry.json, vocab_master.jsonl, grammar_inventory.json, source_registry.json, run_state.json
  chang/<uid8>-<slug>/
    chang.json        manifest, can-do, tình huống, phiên bản nội dung
    status.json       trạng thái từng bước (mục 8)
    sources.json      token → chương, neo, đoạn trích làm bằng chứng
    coverage.json     ma trận phủ
    vocab.jsonl, grammar_refs.json, banks.json, review_cards.json
    situations/<sid>/ situation.json, knowledge.json, dialogue.json, roleplay.json, live_ai.json
  index/README.md     bảng thứ tự học, sinh từ registry
```

**Quy tắc bản gốc:** JSON là bản gốc. Markdown (thẻ kiến thức, README) là bản sinh ra có hash, hoặc khai báo rõ "Markdown là trường soạn thảo, biên dịch vào JSON". Không để hai bản gốc.

**Trường bắt buộc tối thiểu trước pilot:** JSON Schema thực với required, enum, khóa ngoại; văn bản `ja`/`vi` với cách đọc và biến thể; vai nói và vai người học; mục tiêu, slot, ràng buộc, rubric của nhiệm vụ; audio (tài nguyên, phiên bản, trạng thái, quyền, mốc thời gian theo câu); `vocab_occurrence`, `grammar_occurrence`; thẻ ôn trỏ tới câu và phiên bản; `content_schema_version`, `content_revision`. Tiến độ người học, lịch SRS và bản ghi giọng nói nằm ở **kho riêng**, không lẫn vào nội dung.

**Nguồn:** `source_registry.json` ánh xạ token → sách, chương, neo, loại nguồn. Alias được định nghĩa, nguồn quá thô ghi `coarse`. Mỗi tình huống có `source_span` và một câu bằng chứng, để QA kiểm ý nghĩa chứ không chỉ kiểm token tồn tại.

**Level nguồn và level đích:** mỗi tình huống có `source_level`, `target_level`, `adaptation_required` và giới hạn về câu, từ, mẫu, độ ngầm. (B13 mục ① ≈ N2 theo lời sách, nên Trung phải chọn đoạn hoặc chuyển thể.)

## 8. Status và chạy lại (B08)

- Các bước có **phụ thuộc thật** (DAG): đọc nguồn → tình huống và ma trận phủ → hội thoại → từ vựng → ngữ pháp → thẻ kiến thức → đóng vai và persona → kiểm tra → review → xuất bản. Sửa hội thoại làm từ vựng và thẻ ôn thành `stale`.
- Trạng thái: pending, blocked, running, done, stale, needs_review, reviewed, published, failed.
- Mỗi bước ghim hash của spec, nguồn, schema, prompt, model, công cụ và hash của đầu ra. Resume đối chiếu file và hash, không tin riêng trạng thái.
- Worker nhận việc bằng claim có chủ, thời hạn (lease) và heartbeat; worker hết lease không được ghi.
- Mỗi lần chạy ghi vào thư mục run riêng, kiểm cả bộ rồi cam kết một lần bằng manifest. File dùng chung (từ vựng, nguồn) chỉ một bên ghi, hoặc hợp nhất có khóa.
- Bản người sửa tay được bảo vệ bằng revision và phát hiện xung đột, không bị máy ghi đè.
- Thử bắt buộc: ngắt sau khi ghi hội thoại nhưng trước khi ghi trạng thái; đổi spec giữa chừng; hai worker nhận cùng một bước; tranh chấp file chung.

## 9. Quyền sử dụng (B10)

Mỗi văn bản và audio có nhãn: `licensed`, `original`, hoặc `needs_rights_review`. Giữ provenance nội bộ. "Viết lại theo cấu trúc sách" và "ghi nguồn" **không** tự bảo đảm quyền; đổi vài từ hoặc dùng giọng TTS cũng không xóa vấn đề với văn bản. Hội thoại `original` phải viết độc lập từ can-do và bối cảnh phổ quát. Hội thoại hoặc audio thương mại dùng nguyên hay gần nguyên cần xin phép. Trước khi phát hành app cần đánh giá pháp lý theo nội dung, hợp đồng và thị trường; tài liệu này không kết luận về từng tác phẩm.

## 10. Pilot và điều kiện mở rộng (B09)

Thứ tự pilot, mỗi bước kiểm một rủi ro:

1. **Sơ "Nhà hàng & quán ăn":** đủ vòng từ nghe, câu mẫu, audio từng vai, chấm âm, R1 và dữ kiện thật. Chọn nguồn có quyền rõ.
2. **Trung "Chuyển máy, gọi nhầm & để khách chờ":** R2 với người cần gặp vắng, nghe không rõ, số và tên; nhiều đáp án đúng khác mẫu; một nhánh ngoài dự kiến.
3. **Thượng "Nhận khiếu nại & xin lỗi chính thức":** R3 và Live với giới hạn thẩm quyền, khách không đồng ý; phải đạt mục tiêu chứ không trả lời giống bản mẫu.
4. **Một chặng liên quan nhỏ:** thử tái dùng từ vựng, đổi thứ tự cụm, sửa một câu sau QA, ngắt giữa bước, tranh chấp claim.

Ghi token, giờ, chi phí theo từng bước; tỷ lệ phải sửa; lỗi ngữ dụng. Đặt ngân sách dừng và điều kiện qua pilot. QA gồm: máy kiểm schema và nguồn; **người Nhật có chuyên môn** duyệt hội thoại và độ tự nhiên; người học thật kiểm tra chuyển giao. AI tự chấm chính nó không phải bằng chứng duy nhất.

Chỉ sau pilot mới ước lượng chi phí chung và chạy theo từng cụm (Lõi trước, Mở rộng sau), không chạy Lõi của cả 194 chặng một lần.

## 11. Quyết định cần chốt (mặc định đề xuất)

1. Bài = một tình huống, hai phiên, shadowing có giới hạn lần thử (như mục 1)?
2. Ba loại điểm tách riêng, R1/R2/R3 như mục 2–3?
3. Dạng hội thoại trong app: `original` viết độc lập, hay có xin phép dùng nội dung sách? (ảnh hưởng quy trình viết và rủi ro pháp lý)
4. Nơi chạy: máy bạn bằng agent CLI, đọc sách tại chỗ, thư mục trong repo git, status lưu bền (đề xuất).
5. Pilot đúng thứ tự mục 10 trước khi chốt schema v1?
6. Bạn cấp danh sách 50 bài Minna (N5/N4), và cách hiển thị furigana, romaji, bản dịch Việt.
7. Model cho worker: dựng nội dung dùng model mạnh nhất; kiểm tra tự động dùng script.
