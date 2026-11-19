---
name: kaiwa-topic-vocabulary
description: Biên soạn, sửa và nghiệm thu danh sách từ vựng V12.1 theo chủ đề cho chặng topic, phạm vi rộng để người học tự nói về hoàn cảnh của mình, có cách đọc, Hán Việt và nghĩa Việt ở tầng biên tập, gói app chỉ nhận terms_ja.
---

# Từ vựng theo chủ đề cho chặng topic · V12.1

Danh sách từ của một chặng là vốn từ để người học **tự ghép câu nói của chính mình** trong chủ đề đó: kể hoàn cảnh, trả lời câu hỏi của Live AI, nói chuyện tự do, làm lại tình huống với chi tiết khác. Nó không phải bảng từ trích từ hội thoại mẫu. Hội thoại V11 là một nguồn để rà xem còn thiếu gì, không phải giới hạn của danh sách.

Quyết định của chủ dự án ngày 18 tháng 11 năm 2026, theo yêu cầu V6 (`kaiwa_skill/planning/v6/CHECKPOINT_YEU_CAU.md`, mục 1). Quy tắc cũ “chỉ trích ngược từ hội thoại/câu luyện, không thêm từ chỉ vì cùng topic” đã bỏ; `kaiwa_skill/contracts/harumii-kaiwa/v1/CONTRACT.md` mục 3, `AGENTS.md` và các reference của `kaiwa-stage-content` đã được cập nhật theo quyết định này. Định dạng app giữ nguyên: gói xuất chỉ có `terms_ja`.

V12.1, cập nhật ngày 19 tháng 11 năm 2026. Mỗi mục có bốn trường nội dung theo thứ tự `ja`, `reading`, `han_viet`, `vi`. Khi hiển thị, mỗi chặng có một bài từ vựng với các nhóm và bảng riêng bên trong.

## Phạm vi

- Chỉ chặng `stage_kind: topic`. Chặng chuyên đề Speak Japanese không có node từ vựng.
- Đầu vào chỉ đọc: chặng trong `kaiwa_skill/planning/v11/learner.json` (mục tiêu, nhóm từ V10, sự kiện, vai, tình huống, hội thoại V11, shadowing). Không sửa hội thoại, shadowing, V10/V11, sách nguồn hay `bunpou_skill`.
- Sản phẩm: `vocabulary.json` và `status.json` của từng chặng theo [hợp đồng bản thảo](references/draft.md). Không tạo bài tập, bài kiểm tra, ngưỡng đạt hay lịch ôn; engine Harumii lo phần đó.
- Pilot trước: một chặng mỗi cấp, dựng preview, báo cáo và chờ chủ dự án duyệt. Không tự chạy hàng loạt khi chỉ được giao pilot hoặc một chặng.

## Chuẩn bị cho từng chặng

1. Từ gốc repo chạy `py -X utf8 .agents/skills/kaiwa-topic-vocabulary/scripts/vocab.py T-044`, thay mã theo phân công. Lệnh in mục tiêu, cấp và dải độ khó, nhóm từ V10, sự kiện kèm vai, tiêu đề và nhánh từng tình huống, toàn bộ lượt hội thoại và câu shadowing kèm ID.
2. Đọc hết hội thoại và shadowing của chặng. Ghi nháp những gì người học phải **gọi tên** (người, nơi, đồ vật, giấy tờ, dịch vụ, bộ phận), **làm** (hành động mình làm, nhờ, được yêu cầu, bị ảnh hưởng), **mô tả** (trạng thái, sự cố, cảm giác, mức độ, đánh giá) và **định lượng** (số đếm, thời gian, tần suất, giá, kích cỡ).
3. Mở rộng ra ngoài hội thoại. Với mỗi nhóm, hỏi: nếu người học kể chuyện của chính mình trong chủ đề này, được hỏi “bạn thì sao?”, hoặc gặp lại tình huống nhưng với món, ngày, sự cố, yêu cầu khác, họ còn cần gọi tên hay diễn tả điều gì? Ví dụ chủ đề ăn uống cần món, đồ uống, rau, củ, trái cây, vị, cách chế biến, dị ứng và khẩu phần. Chủ đề gửi bưu kiện cần loại hàng, cách đóng gói, kích thước, cân nặng, phương thức gửi, giấy tờ đi kèm và các trạng thái khi theo dõi.
4. Tra nguồn để chọn từ người ở Nhật thực sự dùng, không chỉ từ sách vở:
   - Bảng từ đã clean trong `kaiwa_skill/knowledge`: Mimikara N3 (880 từ), Minato N2 (1160 từ), Mimikara N1 (1170 từ). Script dùng ba bảng này để gợi ý cấp; vẫn đọc bảng khi cần nghĩa hay cặp từ liên quan.
   - Sách hội thoại trong catalog 27 sách (`kaiwa_skill/planning/catalog27/BOOK_GUIDE.md`), nhất là B01 theo chương chủ đề và B23 語い冊 cho từ công việc.
   - Trang chính thức của dịch vụ, cơ quan hay nhà vận hành cho thuật ngữ thủ tục, y tế, pháp lý, giao thông (ví dụ tên giấy tờ, tên dịch vụ, chữ trên biển và phiếu).
   - Từ điển khi chưa chắc chữ viết, cách đọc hay nghĩa.

   Ghi nguồn vào `admin_sources` khi một mục từ hoặc nghĩa dựa vào nguồn cụ thể, bắt buộc với thuật ngữ thủ tục, y tế, pháp lý. Gắn source_refs vào từng mục này và ghi source_domain là procedural, medical hoặc legal. Từ đời thường không cần dẫn nguồn từng từ.

## Cấu trúc danh sách

- **Nhóm.** Dùng các nhóm `vocabulary_topics` của V10 làm xương sống, giữ thứ tự. Có thể sửa tên cho rõ, tách nhóm quá rộng, hoặc thêm nhóm khi chủ đề cần, ví dụ “Kể về bản thân: thói quen, sở thích, kinh nghiệm”. Mỗi nhóm V10 phải nằm trong ít nhất một nhóm mới qua trường `v10_topic`; nếu bỏ một nhóm V10 thì ghi lý do trong `dropped_topics`.
- **Quy mô.** Số mục do phạm vi giao tiếp thực tế quyết định. Ưu tiên đủ vốn từ để người học nói về hoàn cảnh của mình và xử lý các biến thể trong chủ đề. Tiếp tục bổ sung những mục có ích dù vượt 100 từ trong chặng hoặc 25 từ trong nhóm. Kết thúc tuyển chọn khi đã rà nhu cầu diễn đạt và các khoảng thiếu, ghi kết quả vào checkpoint. Chia nhóm theo ý nghĩa để người học tìm và học dần.
- **Thứ tự trong nhóm.** Từ cốt lõi, hay dùng đứng trước. Đặt cạnh nhau những cặp người học hay cần dùng cùng: tự động từ/tha động từ (届く/届ける), đối nghĩa (重い/軽い), cùng trường nghĩa.
- **Lặp lại giữa các chặng.** Tự do. Mỗi chặng tự đủ dùng; không cần tra chặng khác để tránh trùng. Trong cùng một chặng không có hai mục trùng nhau (cùng `ja` và `reading`).

## Chọn từ và ghi mục từ

- **Dạng mục từ.** Động từ thể từ điển (送る, 届ける, 予約する). Tính từ đuôi い dạng cơ bản (重い). Tính từ đuôi な không kèm な/だ (丁寧). Danh từ ở dạng mục từ. Không ghi cả 予約 lẫn 予約する trong một chặng; chọn dạng người học cần dùng nhiều hơn trong chủ đề.
- **Cụm cố định ngắn** được nhận khi người học cần dùng nguyên khối (お先に失礼します, 着払い, 割れ物注意). Câu hoàn chỉnh dài để cho hội thoại và shadowing, không đưa vào danh sách từ.
- **Chữ viết.** Viết như người Nhật thường viết: kanji khi thường viết kanji, kana khi thường viết kana (たばこ, ください), katakana cho từ ngoại lai. Kiểm okurigana. Giữ chữ Latin khi đó là tên hoặc ký hiệu dùng trong tiếng Nhật như EMS và có nguồn xác nhận cách viết. Ghi cách đọc kana và nghĩa Việt như các từ khác.
- **Cách đọc (`reading`).** Toàn bộ bằng kana: hiragana cho từ Hán và từ thuần Nhật, giữ katakana cho phần ngoại lai.
- **Hán Việt (`han_viet`).** Ghi âm Hán Việt của từng kanji theo đúng thứ tự xuất hiện, viết HOA có dấu, cách nhau một khoảng trắng. Ví dụ `学習 → HỌC TẬP`, `申し込む → THÂN NHẬP`, `お客様 → KHÁCH DẠNG`. Bỏ qua kana, okurigana, chữ Latin và số Ả Rập. Chữ `々` lặp lại âm của kanji ngay trước nó, như `時々 → THỜI THỜI`. Từ toàn kana hoặc Latin có chuỗi rỗng `""`. Dùng mặt chữ Nhật hiện có để tra, kể cả dạng giản thể Nhật tương ứng với chữ truyền thống. Tra bảng âm Hán Việt trong kho hoặc từ điển Hán Việt khi cần xác minh. Với chữ đa âm, chọn âm thích hợp cho nghĩa của chữ trong từ, ghi căn cứ trong `note_vi` và `source_refs` khi có điểm cần giải thích. Nếu đã tra và xác nhận chữ chưa có âm Hán Việt được nguồn công nhận, đặt `—` đúng vị trí chữ đó, kèm `han_viet_note_vi` và nguồn. Nếu còn chưa xác minh, ghi vấn đề vào `open_issues` và tiếp tục rà trước khi duyệt. Chuỗi này chỉ biểu thị âm từng chữ; nghĩa dùng trong tiếng Nhật được viết ở `vi`.
- **Nghĩa (`vi`).** Ngắn, đúng nghĩa dùng trong chủ đề. Từ nhiều nghĩa thì ghi nghĩa hợp chủ đề trước, có thể thêm nghĩa thứ hai sau dấu chấm phẩy. Không viết câu ví dụ.
- **Loại từ (`pos`)** theo [hợp đồng bản thảo](references/draft.md).
- **Tên riêng, số cụ thể, nhãn hiệu** không thành mục từ, trừ tên chung của loại dịch vụ hay giấy tờ người học cần gọi đúng (マイナンバーカード, 在留カード, ゆうパック), có ghi nguồn.

## Độ khó theo cấp

| Cấp chặng | Dải mục tiêu | Trần |
|---|---|---|
| Sơ | N5–N4 | N4 |
| Trung | N3–N2 | N2 |
| Thượng | N2–N1 | N1 |

- `level_hint` là **ước lượng biên tập** (N5, N4, N3, N2, N1, hoặc `none` cho từ đời sống ở Nhật không thuộc phạm vi JLPT), không phải danh mục JLPT chính thức. Khi từ có trong bảng Mimikara N3, Minato N2 hoặc Mimikara N1, dùng bảng đó làm căn cứ; script nhắc khi ước lượng lệch bảng.
- Từ vượt trần được nhận khi thiết yếu cho đời sống hay chủ đề (chữ trên biển, phiếu, giấy tờ, triệu chứng, thủ tục), kèm `level_note_vi` nói vì sao người học ở cấp này cần nó. Mục `none` cũng cần `level_note_vi`.
- Từ dưới dải được dùng khi là nền cốt lõi của chủ đề. Ở Trung và Thượng, phần lớn danh sách nên nằm trong dải hoặc là từ chuyên biệt của chủ đề; không lấp danh sách bằng từ sơ cấp người học chắc chắn đã biết.

## Nguồn gốc từng mục

- `origin: dialogue` khi từ, ở bất kỳ dạng chia nào, xuất hiện trong hội thoại V11 hoặc shadowing của chặng. Ghi 1–2 bằng chứng `{utterance_id, surface}` hoặc `{shadowing_item, surface}`, trong đó `surface` là chuỗi đúng như trong câu (送りたい cho 送る). Không cần ghi mọi lần xuất hiện. Từ hữu ích xuất hiện trong hội thoại nên có trong danh sách, trừ từ quá cơ bản so với cấp.
- `origin: topic_extension` cho từ thêm để phủ chủ đề. Đây là phần chính của danh sách, không phải ngoại lệ.

## Ba lượt rà trước khi duyệt

1. **Đủ để tự nói.** Với từng nhóm, thử đặt 3–5 câu về hoàn cảnh của chính mình bằng từ trong nhóm cùng vốn từ và ngữ pháp nền của cấp. Nếu thiếu động từ, tính từ hay từ định lượng để nói trọn câu, bổ sung. Đi qua từng tình huống của chặng và thử làm lại việc đó với chi tiết khác (đổi món, đổi ngày, đổi sự cố). Với mỗi tình huống, rà các loại người hoặc đồ vật liên quan, thuộc tính và số lượng, hành động, nhu cầu, lựa chọn, sự cố và kết quả cần diễn đạt. Thử thay chi tiết theo hoàn cảnh của nhiều người học, gồm cả thuận lợi và gặp trục trặc. Bổ sung từ giúp người học nói rõ nhu cầu còn thiếu. Ghi vào note_vi của nhóm những biến thể đã rà và phần đã bổ sung hoặc khoảng thiếu còn mở vào open_issues. Nhu cầu thiết yếu có thể cần từ vượt cấp kèm giải thích theo quy tắc độ khó.
2. **Đúng chữ, đúng đọc, đúng nghĩa.** Đọc từng mục: kanji và okurigana, cách đọc (âm đục, trường âm, âm ngắt), dạng mục từ, âm Hán Việt từng kanji và nghĩa Việt theo chủ đề. Rà riêng từ đồng âm, cặp tự/tha động từ và từ Hán Việt dễ hiểu sai nghĩa (ví dụ 勉強 khi nói giảm giá). Đối chiếu từng surface với dạng từ điển và nghĩa trong cả câu. 送りたい là dạng của 送る trong ngữ cảnh gửi hàng; 贈りたい thuộc 贈る khi tặng quà. Đối chiếu bảng Mimikara/Minato khi có.
3. **Đúng cấp, đúng chủ đề, không thừa.** Bỏ từ sách vở hoặc hiếm khi dùng trong chủ đề, từ trùng ý không có khác biệt dùng, từ chỉ “có liên quan” mà người học khó cần nói. Kiểm từ vượt trần có lý do thật. Cân đối số mục giữa các nhóm.

Sau khi sửa một nhóm, đọc lại cả nhóm và các nhóm có từ liên quan. Ghi kết quả rà theo nhóm trong `status.json`.

## Dữ liệu, checkpoint và nghiệm thu

Đọc [hợp đồng bản thảo](references/draft.md) khi tạo hoặc sửa file. Mỗi chặng có một người sở hữu tại một thời điểm. Lưu bản thảo sau từng nhóm bằng file tạm rồi thay thế nguyên tử, sau đó cập nhật `status.json`. Khi tiếp một chặng dở, kiểm owner và trạng thái, so hash đầu vào, giữ nhóm đã `reviewed` có hash khớp, làm tiếp nhóm còn lại.

Kiểm từ gốc repo bằng `py -X utf8 .agents/skills/kaiwa-topic-vocabulary/scripts/vocab.py <stage_code> --check <vocabulary.json>`. Lệnh kiểm cấu trúc bốn trường, định dạng Hán Việt và số âm tương ứng số kanji, ID, dạng mục từ cơ bản, kana của cách đọc, trùng lặp, phủ nhóm V10, lý do vượt trần, bằng chứng hội thoại có thật và nguồn sách có thật. Các dòng `Note:` là nhắc việc, không chặn. Khi nghiệm thu, chạy `--check-checkpoint <vocabulary.json>` để đối chiếu status.json cùng thư mục. Lệnh `--export <vocabulary.json>` chỉ xuất các node Exchange đã qua cùng kiểm tra này. Mỗi nhóm xuất các chuỗi Nhật duy nhất. Nếu hai mục cùng mặt chữ nhưng khác cách đọc, giữ cả hai ở bản biên tập và chọn rõ mục đại diện trong nhóm theo hợp đồng bản thảo. Script không xác minh từ có tự nhiên, nghĩa có đúng hay danh sách có đủ để nói; ba lượt rà ở trên là phần người biên tập phải làm.

Pilot kết thúc bằng preview cho chủ dự án xem trên PC và mobile, báo cáo ngắn (số mục, tỷ lệ `dialogue`/`topic_extension`, phân bố cấp, các từ vượt trần, điểm còn băn khoăn) và thời gian thực đo cho mỗi chặng.

Khi nâng bản V12 cũ lên V12.1, bổ sung và rà han_viet từng nhóm rồi cập nhật checkpoint bằng hash mới. Các pilot cũ cần bước nâng dữ liệu này trước khi nghiệm thu lại bằng skill hiện hành.
