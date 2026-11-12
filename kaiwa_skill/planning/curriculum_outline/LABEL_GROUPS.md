# Gom 539 nhãn thành các họ ngữ nghĩa để thiết kế topic

Đây là lớp tổ chức chỉ mục, không phải danh sách bài học. **539/539 nhãn được giữ, mỗi nhãn có đúng một họ chính**; một họ có thể liên kết thêm nhiều topic. Tập hợp theo ngữ nghĩa, chức năng hoặc cùng quy trình, không khẳng định các từ trong một họ là đồng nghĩa và thay thế được cho nhau.

Kết quả: **158 họ nhãn**, gồm **107 họ neo vào topic** và **51 họ kỹ năng/phương pháp xuyên topic**. Có 25 topic đề xuất, trong đó M25 mở rộng từ memo nên chưa có họ nhãn trực tiếp từ danh sách này. [Xem khung](ROADMAP_OUTLINE.md).

Ví dụ: “tự giới thiệu”, “tự giới thiệu nội bộ”, “tự giới thiệu đối ngoại” ở chung một họ nhưng vẫn giữ khác biệt vai/quan hệ. “Xin phép” thuộc X05, được triển khai ở nhà, trường, nơi làm việc… “Biến âm” thuộc X01, không phải một chặng sinh hoạt độc lập. “Kính ngữ” thuộc X04; vẫn phải chọn khác nhau theo tình huống.

Mã L001–L539 theo thứ tự nhãn của snapshot hiện tại; dùng cùng fingerprint trong outline_data.json. Mã chương Bxx-Cyy giải ra vị trí sách tại manifest và có liên kết ngay bên dưới. Level gốc được giữ trong label_assignments.jsonl để tra cứu; level nhiệm vụ đề xuất nằm ở ROADMAP_OUTLINE, chưa phải nhãn cuối cùng từng câu.

## M01 — Giới thiệu bản thân và gặp gỡ lần đầu

<a id="g001"></a>
### G001 — Tự giới thiệu

**Nhãn gốc:** L121 giới thiệu công việc; L445 tự giới thiệu; L446 tự giới thiệu nội bộ; L447 tự giới thiệu đối ngoại; L448 tự xưng tên.

**Chương nguồn:** [B02-C04](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/02-Scene-1-はじめまして.md>), [B04-C18](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/17-Unit16-自分の名前を名乗る.md>), [B10-C02](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/01-紹介する.md>), [B15-C02](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/01-bai-01.md>), [B15-C03](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/02-bai-02.md>), [B17-C02](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/01-新任のあいさつ.md>), [B21-C02](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/01-jiko-shoukai.md>), [B22-C02](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/01-jiko-shoukai.md>), [B23-C02](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/01-bai-1-tu-gioi-thieu.md>).

**Có thể dùng thêm tại:** [M15 — Tìm việc và phát triển nghề nghiệp](ROADMAP_OUTLINE.md#m15), [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16).

<a id="g002"></a>
### G002 — Giới thiệu người khác

**Nhãn gốc:** L122 giới thiệu người khác.

**Chương nguồn:** [B02-C05](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/02b-紹介する-Scene2-3.md>).

**Có thể dùng thêm tại:** [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16), [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g003"></a>
### G003 — Làm quen và gặp lần đầu

**Nhãn gốc:** L051 chào làm quen; L126 gặp gỡ; L127 gặp gỡ công việc; L128 gặp lần đầu; L129 gặp mặt ban đầu; L130 gặp người mới; L220 làm quen.

**Chương nguồn:** [B02-C04](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/02-Scene-1-はじめまして.md>), [B02-C05](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/02b-紹介する-Scene2-3.md>), [B10-C02](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/01-紹介する.md>), [B21-C15](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/14-shotaimen.md>), [B22-C15](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/14-shotaimen.md>), [B23-C15](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/14-bai-14-gap-lan-dau.md>), [B27-C03](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/02-bai-01-deai.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16).

## M02 — Trò chuyện và xây dựng quan hệ

<a id="g004"></a>
### G004 — Chào hỏi theo hoàn cảnh

**Nhãn gốc:** L048 chào hỏi; L049 chào hỏi công sở; L050 chào hỏi công việc; L052 chào theo mùa; L231 lời chào.

**Chương nguồn:** [B02-C17](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/15-挨拶する.md>), [B03-C03](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/02-Unit01-あいさつの基本.md>), [B08-C02](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/01-part1-shoho.md>), [B10-C03](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/02-あいさつをする.md>), [B14-C03](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/02-unit-1.md>), [B14-C04](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/03-unit-2.md>), [B17-C02](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/01-新任のあいさつ.md>), [B17-C16](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/15-新年のあいさつ.md>), [B21-C07](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/06-aisatsu.md>), [B22-C07](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/06-aisatsu.md>), [B23-C07](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/06-bai-6-chao-hoi.md>).

**Có thể dùng thêm tại:** [M13 — Sở thích, giải trí, ngày nghỉ và sự kiện](ROADMAP_OUTLINE.md#m13), [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16), [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g005"></a>
### G005 — Bắt chuyện và mở quan hệ

**Nhãn gốc:** L028 bắt chuyện; L154 hỏi chuyện; L263 mở lời; L264 mở quan hệ.

**Chương nguồn:** [B02-C09](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/07-話しかける.md>), [B09-C15](<../../knowledge/なめらか日本語会話/chapters/15-14-話を切り出す.md>), [B11-C02](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/00-mo-dau.md>), [B11-C11](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/09-part2-dau-cau.md>), [B12-C10](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/09-part2-a-hajimeru.md>), [B15-C11](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/10-bai-10.md>).

**Có thể dùng thêm tại:** [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16), [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g006"></a>
### G006 — Bạn bè, người quen và sự thân thiết

**Nhãn gốc:** L022 bạn bè; L112 giao tiếp xã hội; L278 người quen; L338 quan hệ thân mật.

**Chương nguồn:** [B13-C02](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/01-unit-1-gia-dinh-vo-chong-nguoi-yeu.md>), [B13-C03](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/02-unit-2-ban-than.md>), [B13-C04](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/03-unit-3-nguoi-quen-hang-xom.md>), [B24-C02](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/01-introduction.md>).

**Có thể dùng thêm tại:** [M03 — Gia đình và người thân](ROADMAP_OUTLINE.md#m03).

<a id="g007"></a>
### G007 — Khen và đáp lời khen

**Nhãn gốc:** L177 khen ngợi; L508 đáp lời khen.

**Chương nguồn:** [B06-C07](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/06-s-82-98.md>), [B12-C24](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/23-part2-c-homeru.md>), [B26-C09](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/07-bai-7.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17), [M23 — Kể trải nghiệm, chia sẻ cảm xúc và nhận xét](ROADMAP_OUTLINE.md#m23).

<a id="g008"></a>
### G008 — Cảm ơn và biết ơn

**Nhãn gốc:** L085 cảm ơn; L224 lòng biết ơn.

**Chương nguồn:** [B02-C17](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/15-挨拶する.md>), [B08-C03](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/02-part2-kinou.md>), [B09-C21](<../../knowledge/なめらか日本語会話/chapters/21-20-お礼を言う・あやまる.md>), [B24-C05](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/04-section-c.md>).

**Có thể dùng thêm tại:** [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16), [M23 — Kể trải nghiệm, chia sẻ cảm xúc và nhận xét](ROADMAP_OUTLINE.md#m23).

<a id="g009"></a>
### G009 — Chia buồn

**Nhãn gốc:** L034 chia buồn.

**Chương nguồn:** [B23-C07](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/06-bai-6-chao-hoi.md>).

**Có thể dùng thêm tại:** [M03 — Gia đình và người thân](ROADMAP_OUTLINE.md#m03).

<a id="g010"></a>
### G010 — Khích lệ và hỗ trợ tinh thần

**Nhãn gốc:** L020 bênh vực; L197 khích lệ; L416 trấn an; L536 động viên.

**Chương nguồn:** [B06-C09](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/08-t-116-137.md>), [B12-C24](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/23-part2-c-homeru.md>), [B20-C16](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/15-section-n.md>).

**Có thể dùng thêm tại:** [M03 — Gia đình và người thân](ROADMAP_OUTLINE.md#m03), [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17), [M23 — Kể trải nghiệm, chia sẻ cảm xúc và nhận xét](ROADMAP_OUTLINE.md#m23).

## M03 — Gia đình và người thân

<a id="g011"></a>
### G011 — Gia đình và người thân

**Nhãn gốc:** L105 gia đình; L513 đón người thân.

**Chương nguồn:** [B13-C02](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/01-unit-1-gia-dinh-vo-chong-nguoi-yeu.md>), [B17-C09](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/08-いとこを空港まで迎えに.md>).

## M04 — Sinh hoạt, thời gian và kế hoạch

<a id="g012"></a>
### G012 — Dự định và quyết tâm

**Nhãn gốc:** L012 bày tỏ ý định; L102 dự định; L342 quyết tâm; L482 ý định.

**Chương nguồn:** [B02-C07](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/05-意思を表明する.md>), [B07-C08](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/07-part1-will.md>), [B27-C12](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/11-bai-10-houfu.md>).

**Có thể dùng thêm tại:** [M15 — Tìm việc và phát triển nghề nghiệp](ROADMAP_OUTLINE.md#m15), [M23 — Kể trải nghiệm, chia sẻ cảm xúc và nhận xét](ROADMAP_OUTLINE.md#m23).

<a id="g013"></a>
### G013 — Lịch trình và thay đổi kế hoạch

**Nhãn gốc:** L357 sắp xếp lịch; L371 thay đổi kế hoạch; L487 điều chỉnh lịch; L532 đổi lịch; L533 đổi lịch hẹn.

**Chương nguồn:** [B06-C05](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/04-k-40-60.md>), [B10-C08](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/07-アポイントをとる.md>), [B15-C05](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/04-bai-04.md>), [B17-C08](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/07-夏休みはいつ取る.md>), [B22-C19](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/18-apointmento.md>), [B26-C04](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/02-bai-2.md>).

**Có thể dùng thêm tại:** [M10 — Du lịch, công tác và lưu trú](ROADMAP_OUTLINE.md#m10), [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g014"></a>
### G014 — Sinh hoạt và thói quen

**Nhãn gốc:** L351 sinh hoạt; L352 sinh hoạt hàng ngày; L353 sinh hoạt thường ngày; L377 thói quen sinh hoạt; L450 việc cá nhân; L537 đời sống.

**Chương nguồn:** [B01-C05](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/04-van-dong.md>), [B02-C14](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/12-許可を求める.md>), [B07-C11](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/10-part2-routines.md>), [B08-C02](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/01-part1-shoho.md>), [B14-C07](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/06-unit-5.md>), [B27-C09](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/08-bai-07-kenkou-no-tame-ni.md>).

**Có thể dùng thêm tại:** [M11 — Sức khỏe và chăm sóc bản thân](ROADMAP_OUTLINE.md#m11).

## M05 — Nhà ở, sống chung và chuyển nhà

<a id="g015"></a>
### G015 — Nhà ở và căn hộ

**Nhãn gốc:** L079 căn hộ.

**Chương nguồn:** [B26-C12](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/10-bai-10.md>).

<a id="g016"></a>
### G016 — Cho, nhận và nhượng lại đồ

**Nhãn gốc:** L282 nhượng đồ; L296 nhận đồ.

**Chương nguồn:** [B26-C11](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/09-bai-9.md>).

**Có thể dùng thêm tại:** [M08 — Mua sắm, thanh toán và dịch vụ đời sống](ROADMAP_OUTLINE.md#m08).

<a id="g158"></a>
### G158 — Mượn và cho mượn đồ

**Nhãn gốc:** L252 mượn đồ.

**Chương nguồn:** [B26-C03](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/01-bai-1.md>).

**Có thể dùng thêm tại:** [M14 — Học tập và trường học](ROADMAP_OUTLINE.md#m14), [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

## M06 — Khu phố, cộng đồng và dịch vụ công

<a id="g018"></a>
### G018 — Hàng xóm và quan hệ địa phương

**Nhãn gốc:** L145 hàng xóm.

**Chương nguồn:** [B13-C04](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/03-unit-3-nguoi-quen-hang-xom.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02).

<a id="g019"></a>
### G019 — Thông tin về cơ sở vật chất

**Nhãn gốc:** L080 cơ sở vật chất.

**Chương nguồn:** [B22-C16](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/15-toiawase.md>).

**Có thể dùng thêm tại:** [M10 — Du lịch, công tác và lưu trú](ROADMAP_OUTLINE.md#m10).

## M07 — Đi ăn, nhà hàng và những bữa gặp gỡ

<a id="g020"></a>
### G020 — Ăn uống và dùng bữa

**Nhãn gốc:** L098 dùng bữa; L483 ăn uống; L538 ẩm thực.

**Chương nguồn:** [B01-C06](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/05-am-thuc.md>), [B03-C16](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/15-Unit13-接待・会食.md>), [B17-C12](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/11-食欲の秋.md>).

<a id="g021"></a>
### G021 — Gọi món, nhà hàng và đặt bàn

**Nhãn gốc:** L132 gọi món; L281 nhà hàng; L519 đặt bàn.

**Chương nguồn:** [B05-C04](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/03-ch2-inshokuten.md>), [B26-C05](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/03-bai-3.md>).

**Có thể dùng thêm tại:** [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g022"></a>
### G022 — Đi uống và giao lưu

**Nhãn gốc:** L345 quán rượu; L486 đi uống.

**Chương nguồn:** [B17-C07](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/06-飲みニケーション.md>), [B17-C10](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/09-総合タスク2.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16).

## M08 — Mua sắm, thanh toán và dịch vụ đời sống

<a id="g024"></a>
### G024 — Mua sắm và bán lẻ

**Nhãn gốc:** L014 bán lẻ; L089 cửa hàng tiện lợi; L249 mua sắm.

**Chương nguồn:** [B05-C05](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/04-ch3-hanbaiten.md>), [B05-C06](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/05-ch4-konbini.md>), [B13-C05](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md>), [B26-C07](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/05-bai-5.md>).

**Có thể dùng thêm tại:** [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

<a id="g025"></a>
### G025 — Quà tặng và quà lưu niệm

**Nhãn gốc:** L343 quà lưu niệm; L344 quà tặng.

**Chương nguồn:** [B21-C11](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/10-omiyage.md>), [B22-C11](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/10-omiyage.md>), [B23-C11](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/10-bai-10-qua-tang.md>).

**Có thể dùng thêm tại:** [M03 — Gia đình và người thân](ROADMAP_OUTLINE.md#m03), [M13 — Sở thích, giải trí, ngày nghỉ và sự kiện](ROADMAP_OUTLINE.md#m13), [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g026"></a>
### G026 — Thanh toán và giao dịch

**Nhãn gốc:** L106 giao dịch; L369 thanh toán.

**Chương nguồn:** [B05-C03](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/02-ch1-keigo.md>), [B05-C06](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/05-ch4-konbini.md>).

**Có thể dùng thêm tại:** [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

<a id="g027"></a>
### G027 — Các dịch vụ đời sống

**Nhãn gốc:** L100 dịch vụ; L101 dịch vụ khác.

**Chương nguồn:** [B05-C08](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/07-ch6-sonota.md>), [B13-C05](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md>).

**Có thể dùng thêm tại:** [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

## M09 — Đi lại, phương tiện và nhà ga

<a id="g028"></a>
### G028 — Đi lại, phương tiện và nhà ga

**Nhãn gốc:** L104 ga tàu; L107 giao thông; L321 phương tiện vận chuyển; L322 phương tiện đi lại; L484 đi lại.

**Chương nguồn:** [B01-C08](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/07-phuong-tien-van-chuyen.md>), [B17-C17](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/16-雪による交通マヒ.md>), [B26-C10](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/08-bai-8.md>), [B27-C10](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/09-bai-08-eki-de.md>).

<a id="g029"></a>
### G029 — Hỏi và chỉ đường

**Nhãn gốc:** L057 chỉ đường; L169 hỏi đường.

**Chương nguồn:** [B21-C06](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/05-michi-o-kiku.md>), [B22-C06](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/05-michi-o-kiku.md>), [B23-C06](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/05-bai-5-hoi-duong.md>).

**Có thể dùng thêm tại:** [M10 — Du lịch, công tác và lưu trú](ROADMAP_OUTLINE.md#m10).

<a id="g030"></a>
### G030 — Thời tiết gây trở ngại đi lại

**Nhãn gốc:** L388 thời tiết xấu.

**Chương nguồn:** [B17-C17](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/16-雪による交通マヒ.md>).

**Có thể dùng thêm tại:** [M12 — An toàn, sự cố và trợ giúp khẩn cấp](ROADMAP_OUTLINE.md#m12), [M13 — Sở thích, giải trí, ngày nghỉ và sự kiện](ROADMAP_OUTLINE.md#m13).

<a id="g031"></a>
### G031 — Sân bay

**Nhãn gốc:** L355 sân bay.

**Chương nguồn:** [B17-C09](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/08-いとこを空港まで迎えに.md>).

**Có thể dùng thêm tại:** [M10 — Du lịch, công tác và lưu trú](ROADMAP_OUTLINE.md#m10).

## M10 — Du lịch, công tác và lưu trú

<a id="g032"></a>
### G032 — Du lịch, chuyến đi công ty và công tác

**Nhãn gốc:** L039 chuyến đi công ty; L076 công tác; L094 du lịch; L095 du lịch công ty; L212 kế hoạch đi lại.

**Chương nguồn:** [B06-C09](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/08-t-116-137.md>), [B17-C13](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/12-旅行に行くなら.md>), [B21-C09](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/08-shain-ryokou.md>), [B22-C09](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/08-shain-ryokou.md>), [B23-C09](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/08-bai-8-chuyen-di-cong-ty.md>), [B26-C06](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/04-bai-4.md>).

**Có thể dùng thêm tại:** [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16).

<a id="g033"></a>
### G033 — Khách sạn và lưu trú

**Nhãn gốc:** L195 khách sạn; L226 lưu trú.

**Chương nguồn:** [B05-C07](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/06-ch5-shukuhaku.md>), [B17-C20](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/19-総合タスク4.md>), [B27-C04](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/03-bai-02-hoteru-de.md>).

**Có thể dùng thêm tại:** [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

## M11 — Sức khỏe và chăm sóc bản thân

<a id="g035"></a>
### G035 — Sức khỏe và khám bệnh

**Nhãn gốc:** L196 khám bệnh; L360 sức khỏe.

**Chương nguồn:** [B06-C06](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/05-k-61-81.md>), [B13-C05](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md>), [B27-C09](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/08-bai-07-kenkou-no-tame-ni.md>).

## M12 — An toàn, sự cố và trợ giúp khẩn cấp

<a id="g036"></a>
### G036 — An toàn và tình huống khẩn cấp

**Nhãn gốc:** L002 an toàn; L204 khẩn cấp.

**Chương nguồn:** [B05-C10](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/09-ch8-kinkyu.md>), [B08-C02](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/01-part1-shoho.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17), [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

## M13 — Sở thích, giải trí, ngày nghỉ và sự kiện

<a id="g034"></a>
### G034 — Ngày nghỉ và kỳ nghỉ

**Nhãn gốc:** L065 cuối tuần; L273 nghỉ hè.

**Chương nguồn:** [B08-C06](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/05-part5-topic.md>), [B17-C08](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/07-夏休みはいつ取る.md>).

**Có thể dùng thêm tại:** [M04 — Sinh hoạt, thời gian và kế hoạch](ROADMAP_OUTLINE.md#m04), [M10 — Du lịch, công tác và lưu trú](ROADMAP_OUTLINE.md#m10).

<a id="g037"></a>
### G037 — Sở thích, thể thao và vận động

**Nhãn gốc:** L358 sở thích; L387 thể thao; L453 vận động.

**Chương nguồn:** [B01-C03](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/02-nguyen-vong.md>), [B01-C05](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/04-van-dong.md>), [B08-C06](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/05-part5-topic.md>), [B17-C18](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/17-趣味も大切.md>), [B27-C11](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/10-bai-09-shumi.md>).

**Có thể dùng thêm tại:** [M11 — Sức khỏe và chăm sóc bản thân](ROADMAP_OUTLINE.md#m11).

<a id="g038"></a>
### G038 — Mùa, lễ tết và tổ chức sự kiện

**Nhãn gốc:** L251 mùa thu; L313 năm mới; L364 sự kiện; L399 tiệc tất niên; L432 tổ chức sự kiện.

**Chương nguồn:** [B17-C12](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/11-食欲の秋.md>), [B17-C14](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/13-忘年会の幹事.md>), [B17-C16](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/15-新年のあいさつ.md>), [B22-C16](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/15-toiawase.md>).

**Có thể dùng thêm tại:** [M06 — Khu phố, cộng đồng và dịch vụ công](ROADMAP_OUTLINE.md#m06), [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16).

## M14 — Học tập và trường học

<a id="g039"></a>
### G039 — Giao tiếp ở trường

**Nhãn gốc:** L115 giao tiếp ở trường.

**Chương nguồn:** [B18-C07](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md>).

## M15 — Tìm việc và phát triển nghề nghiệp

<a id="g040"></a>
### G040 — Tìm việc và việc làm thêm

**Nhãn gốc:** L046 chuẩn bị tìm việc; L424 tìm việc làm thêm.

**Chương nguồn:** [B16-C02](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/02-Unit1-就活の準備.md>), [B26-C08](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/06-bai-6.md>).

<a id="g041"></a>
### G041 — Thực tập

**Nhãn gốc:** L223 làm việc thực tập; L368 tham gia thực tập; L391 thực tập.

**Chương nguồn:** [B16-C02](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/02-Unit1-就活の準備.md>), [B16-C03](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/03-Unit2-インターンシップ.md>).

**Có thể dùng thêm tại:** [M16 — Bắt đầu và hội nhập công sở](ROADMAP_OUTLINE.md#m16).

<a id="g042"></a>
### G042 — Phỏng vấn và trả lời câu hỏi

**Nhãn gốc:** L331 phỏng vấn; L332 phỏng vấn tuyển dụng; L333 phỏng vấn xin việc; L506 đáp câu hỏi.

**Chương nguồn:** [B13-C08](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/07-unit-7-nguoi-ngoai-cong-ty.md>), [B16-C04](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/04-Unit3-就職の面接.md>), [B21-C21](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/20-mensetsu-shiken.md>), [B22-C21](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/20-mensetsu-shiken.md>), [B23-C21](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/20-bai-20-phong-van.md>).

**Có thể dùng thêm tại:** [M21 — Họp, báo cáo và trình bày ý tưởng](ROADMAP_OUTLINE.md#m21).

## M16 — Bắt đầu và hội nhập công sở

<a id="g043"></a>
### G043 — Bắt đầu làm việc và môi trường công ty

**Nhãn gốc:** L074 công sở; L075 công ty; L078 công việc đầu tiên; L314 nơi làm việc.

**Chương nguồn:** [B03-C03](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/02-Unit01-あいさつの基本.md>), [B03-C09](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/08-Unit07-整理整頓.md>), [B16-C05](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/05-Unit4-初めての仕事.md>), [B23-C08](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/07-bai-7-nhan-dien-thoai-ngoai.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

<a id="g044"></a>
### G044 — Trang phục, diện mạo và tác phong

**Nhãn gốc:** L058 chỉn chu; L093 diện mạo; L400 trang phục; L421 tác phong công sở; L429 tư thế; L454 vẻ ngoài.

**Chương nguồn:** [B03-C04](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/03-Unit02-身だしなみ１.md>), [B03-C05](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/04-Unit03-身だしなみ２.md>), [B03-C06](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/05-Unit04-入室・退室.md>), [B03-C12](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/11-Unit10-社会人らしい行動と言葉遣い.md>).

**Có thể dùng thêm tại:** [M15 — Tìm việc và phát triển nghề nghiệp](ROADMAP_OUTLINE.md#m15), [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g045"></a>
### G045 — Ứng xử, ngăn nắp và quan niệm công việc

**Nhãn gốc:** L125 gắn bó công ty; L146 hành vi cần tránh; L276 ngăn nắp; L340 quan niệm công việc.

**Chương nguồn:** [B03-C09](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/08-Unit07-整理整頓.md>), [B03-C11](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/10-Unit09-社会人として、してはいけないこと.md>), [B03-C23](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/22-Unit20-日本人の仕事観.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

<a id="g046"></a>
### G046 — Quan hệ đồng nghiệp, cấp bậc và trong–ngoài

**Nhãn gốc:** L086 cấp trên cấp dưới; L111 giao tiếp nội bộ; L113 giao tiếp đối ngoại; L114 giao tiếp đồng nghiệp; L336 quan hệ cấp trên; L339 quan hệ trong ngoài; L406 trong ngoài công ty; L529 đồng nghiệp.

**Chương nguồn:** [B02-C10](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/08-依頼する.md>), [B03-C22](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/21-Unit19-社内でのコミュニケーション.md>), [B13-C06](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/05-unit-5-dong-nghiep.md>), [B13-C07](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/06-unit-6-cap-tren-cap-duoi.md>), [B13-C08](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/07-unit-7-nguoi-ngoai-cong-ty.md>), [B15-C03](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/02-bai-02.md>), [B17-C07](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/06-飲みニケーション.md>), [B17-C19](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/18-上司の転勤.md>), [B18-C02](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/02-序章-敬語の世界.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17), [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g047"></a>
### G047 — Chia tay đồng nghiệp và chuyển công tác

**Nhãn gốc:** L035 chia tay đồng nghiệp; L042 chuyển công tác.

**Chương nguồn:** [B10-C03](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/02-あいさつをする.md>), [B17-C19](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/18-上司の転勤.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02).

<a id="g048"></a>
### G048 — Danh thiếp

**Nhãn gốc:** L090 danh thiếp; L403 trao đổi danh thiếp.

**Chương nguồn:** [B02-C16](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/14-助言する.md>), [B03-C14](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/13-Unit11-名刺.md>).

**Có thể dùng thêm tại:** [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19).

<a id="g049"></a>
### G049 — Vào ra phòng và vị trí chỗ ngồi

**Nhãn gốc:** L347 rời phòng; L389 thứ tự chỗ ngồi; L452 vào phòng; L456 vị trí đứng.

**Chương nguồn:** [B03-C06](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/05-Unit04-入室・退室.md>), [B03-C17](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/16-Unit14-席次.md>).

**Có thể dùng thêm tại:** [M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón](ROADMAP_OUTLINE.md#m19), [M21 — Họp, báo cáo và trình bày ý tưởng](ROADMAP_OUTLINE.md#m21).

## M17 — Phối hợp, bàn giao và xử lý công việc

<a id="g050"></a>
### G050 — Công việc, nhận việc và phối hợp

**Nhãn gốc:** L077 công việc; L108 giao tiếp công việc; L291 nhận việc; L402 trao đổi công việc.

**Chương nguồn:** [B02-C13](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/11-相談する.md>), [B06-C08](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/07-s-99-115.md>), [B13-C06](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/05-unit-5-dong-nghiep.md>), [B17-C02](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/01-新任のあいさつ.md>), [B17-C05](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/04-仕事が山積み.md>), [B18-C07](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md>), [B22-C02](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/01-jiko-shoukai.md>), [B22-C15](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/14-shotaimen.md>), [B22-C18](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/17-keigo.md>).

<a id="g051"></a>
### G051 — Giao việc, chỉ dẫn và nhận chỉ thị

**Nhãn gốc:** L054 chỉ dẫn; L116 giao việc; L136 hiểu chỉ thị; L285 nhận chỉ thị.

**Chương nguồn:** [B03-C20](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/19-Unit17-指示を受ける.md>), [B06-C12](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/11-m-172-194.md>), [B17-C15](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/14-総合タスク3.md>), [B25-C07](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/06-bai-5-irai-shiji.md>).

<a id="g052"></a>
### G052 — Khối lượng việc, tiến độ và sự chủ động

**Nhãn gốc:** L026 bận rộn; L062 chủ động; L140 hiệu quả; L207 khối lượng công việc; L393 tiến độ.

**Chương nguồn:** [B17-C05](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/04-仕事が山積み.md>), [B20-C04](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/03-section-b.md>), [B20-C13](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/12-section-k.md>), [B22-C12](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/11-renraku.md>).

**Có thể dùng thêm tại:** [M23 — Kể trải nghiệm, chia sẻ cảm xúc và nhận xét](ROADMAP_OUTLINE.md#m23).

<a id="g053"></a>
### G053 — Báo cáo, liên lạc và xin ý kiến trong công việc

**Nhãn gốc:** L015 báo cáo; L217 liên lạc; L218 liên lạc công việc; L378 thông tin 5W3H; L449 viết báo cáo; L462 xin ý kiến.

**Chương nguồn:** [B03-C19](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/18-Unit16-ビジネスEメール.md>), [B03-C21](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/20-Unit18-報告・連絡・相談.md>), [B16-C05](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/05-Unit4-初めての仕事.md>), [B21-C12](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/11-renraku.md>), [B22-C12](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/11-renraku.md>).

**Có thể dùng thêm tại:** [M21 — Họp, báo cáo và trình bày ý tưởng](ROADMAP_OUTLINE.md#m21).

<a id="g054"></a>
### G054 — Sai sót và sự cố công việc, thiết bị

**Nhãn gốc:** L120 giải thích sự cố; L349 sai sót; L363 sự cố; L383 thất bại; L419 trục trặc máy móc.

**Chương nguồn:** [B03-C11](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/10-Unit09-社会人として、してはいけないこと.md>), [B05-C07](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/06-ch5-shukuhaku.md>), [B05-C10](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/09-ch8-kinkyu.md>), [B17-C04](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/03-ミスをして謝る.md>), [B22-C13](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/12-owabi.md>), [B27-C06](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/05-bai-04-kikai-no-toraburu.md>), [B27-C07](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/06-bai-05-shippai.md>).

**Có thể dùng thêm tại:** [M12 — An toàn, sự cố và trợ giúp khẩn cấp](ROADMAP_OUTLINE.md#m12), [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

<a id="g055"></a>
### G055 — Nhận và đưa lời nhắc nhở công việc

**Nhãn gốc:** L287 nhận lời nhắc; L300 nhắc nhở công việc; L395 tiếp nhận góp ý; L397 tiếp nhận nhắc nhở; L517 được nhắc nhở.

**Chương nguồn:** [B10-C05](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/04-注意をする・注意を受ける.md>), [B21-C20](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/19-chuui-o-ukeru.md>), [B22-C20](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/19-chuui-o-ukeru.md>), [B23-C20](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/19-bai-19-tiep-nhan-phe-binh.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02).

<a id="g056"></a>
### G056 — Cân bằng công việc và cuộc sống

**Nhãn gốc:** L070 cân bằng công việc.

**Chương nguồn:** [B17-C18](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/17-趣味も大切.md>).

**Có thể dùng thêm tại:** [M03 — Gia đình và người thân](ROADMAP_OUTLINE.md#m03).

## M18 — Điện thoại, lời nhắn và liên lạc

<a id="g057"></a>
### G057 — Gọi, nhận và ứng xử điện thoại

**Nhãn gốc:** L131 gọi hỏi thông tin; L134 gọi điện thoại; L244 lời đầu tiên khi nhận điện thoại; L271 nghe điện thoại; L277 người gọi ngoài; L294 nhận điện thoại; L404 trao đổi qua điện thoại; L489 điện thoại; L490 điện thoại công sở; L491 điện thoại công ty; L492 điện thoại công việc; L493 điện thoại di động; L494 điện thoại dịch vụ; L495 điện thoại đời sống; L505 đáp cuộc gọi; L511 đáp điện thoại; L539 ứng xử điện thoại công việc.

**Chương nguồn:** [B01-C07](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/06-dien-thoai.md>), [B03-C10](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/09-Unit08-携帯電話のマナー.md>), [B03-C18](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/17-Unit15-電話応対.md>), [B04-C02](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/01-ビジネス電話応対の基本.md>), [B04-C03](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/02-Unit01-第一声.md>), [B04-C25](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/24-Unit23-問い合わせをする.md>), [B05-C09](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/08-ch7-denwa.md>), [B10-C04](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/03-電話をかける・受ける.md>), [B15-C04](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/03-bai-03.md>), [B17-C03](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/02-電話がこわい.md>), [B21-C08](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/07-shagai-denwa.md>), [B22-C08](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/07-shagai-denwa.md>), [B23-C08](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/07-bai-7-nhan-dien-thoai-ngoai.md>), [B23-C16](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/15-bai-15-hoi-thong-tin.md>), [B27-C08](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/07-bai-06-denwa-o-kakeru.md>).

<a id="g058"></a>
### G058 — Chuẩn bị và kết thúc cuộc gọi

**Nhãn gốc:** L045 chuẩn bị cuộc gọi; L213 kết thúc cuộc gọi.

**Chương nguồn:** [B04-C02](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/01-ビジネス電話応対の基本.md>), [B04-C37](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/36-Unit35-電話を切る.md>).

<a id="g059"></a>
### G059 — Chuyển cuộc gọi

**Nhãn gốc:** L041 chuyển cuộc gọi; L044 chuyển máy cho người phụ trách; L301 nhờ chuyển cuộc gọi.

**Chương nguồn:** [B04-C06](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/05-Unit04-担当者へ取り次ぐ.md>), [B04-C23](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/22-Unit21-取り次ぎを頼む.md>), [B15-C04](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/03-bai-03.md>), [B16-C06](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/06-Unit5-電話対応.md>).

<a id="g060"></a>
### G060 — Nhận và chuyển lời nhắn

**Nhãn gốc:** L043 chuyển lời nhắn; L235 lời nhắn; L288 nhận lời nhắn; L302 nhờ chuyển lời; L525 để lại lời nhắn trong hộp thư thoại.

**Chương nguồn:** [B04-C15](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/14-Unit13-伝言を受ける.md>), [B04-C16](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/15-Unit14-伝言を伝える.md>), [B04-C26](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/25-Unit24-伝言を頼む.md>), [B04-C30](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/29-Unit28-留守番電話に伝言を残す.md>), [B10-C04](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/03-電話をかける・受ける.md>), [B16-C06](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/06-Unit5-電話対応.md>), [B23-C12](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/11-bai-11-de-lai-loi-nhan.md>), [B25-C03](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/02-bai-1-dengon.md>).

<a id="g061"></a>
### G061 — Gọi lại và gọi nhắc

**Nhãn gốc:** L017 báo sẽ gọi lại; L133 gọi điện nhắc; L303 nhờ gọi lại; L304 nhờ gọi lại số khác; L305 nhờ người gọi gọi lại.

**Chương nguồn:** [B04-C10](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/09-Unit08-ほかの番号へかけ直してもらう.md>), [B04-C13](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/12-Unit11-コールバックすることを伝える.md>), [B04-C14](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/13-Unit12-コールバックしてもらう.md>), [B04-C27](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/26-Unit25-コールバックすることを伝える.md>), [B04-C28](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/27-Unit26-コールバックしてもらう.md>), [B15-C14](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/13-bai-13.md>).

<a id="g062"></a>
### G062 — Người cần gặp không sẵn có

**Nhãn gốc:** L019 báo vắng mặt; L182 khi không có người đúng như tên được hỏi; L184 khi người cần gặp đang có cuộc gọi khác; L187 khi người phụ trách rời chỗ; L188 khi người phụ trách vắng mặt.

**Chương nguồn:** [B04-C07](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/06-Unit05-担当者が電話中のときの対応.md>), [B04-C08](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/07-Unit06-担当者が離席中のときの対応.md>), [B04-C09](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/08-Unit07-担当者が不在のときの対応.md>), [B04-C11](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/10-Unit09-該当者がいないときの対応.md>), [B25-C03](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/02-bai-1-dengon.md>).

<a id="g063"></a>
### G063 — Xác nhận tên, số và thông tin liên lạc

**Nhãn gốc:** L018 báo số fax và địa chỉ email; L155 hỏi chữ Hán viết tên; L298 nhắc lại để xác nhận số và chữ; L465 xác nhận nội dung cuộc gọi; L466 xác nhận tên và thông tin khi đã nghe rõ.

**Chương nguồn:** [B04-C04](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/03-Unit02-用件確認.md>), [B04-C17](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/16-Unit15-復唱する（数字など）.md>), [B04-C19](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/18-Unit17-Fax番号・メールアドレスを伝える.md>), [B04-C32](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/31-Unit30-名前の漢字を尋ねる.md>), [B04-C33](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/32-Unit31-名前などを確認する（聞き取れているとき）.md>).

<a id="g064"></a>
### G064 — Nghe chưa rõ do bản thân hoặc đường truyền

**Nhãn gốc:** L178 khi bản thân nghe hiểu chưa đủ; L181 khi khó nghe vì sóng điện thoại hoặc tiếng ồn.

**Chương nguồn:** [B04-C34](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/33-Unit32-よく聞き取れないとき（電波障害など）.md>), [B04-C35](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/34-Unit33-よく聞き取れないとき（リスニング力不足）.md>).

<a id="g065"></a>
### G065 — Gọi nhầm và nhận cuộc gọi nhầm

**Nhãn gốc:** L180 khi gọi nhầm số; L189 khi nhận cuộc gọi nhầm.

**Chương nguồn:** [B04-C12](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/11-Unit10-間違い電話を受けたとき.md>), [B04-C31](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/30-Unit29-間違い電話をしたとき.md>).

<a id="g066"></a>
### G066 — Người gọi không xưng tên hoặc muốn gặp mình

**Nhãn gốc:** L185 khi người gọi không xưng tên; L186 khi người gọi muốn gặp chính mình.

**Chương nguồn:** [B04-C05](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/04-Unit03-自分への用事のとき.md>), [B04-C36](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/35-Unit34-相手が名乗らないとき.md>).

<a id="g067"></a>
### G067 — Liên lạc gấp

**Nhãn gốc:** L179 khi cần liên lạc gấp.

**Chương nguồn:** [B04-C29](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/28-Unit27-至急のとき.md>).

<a id="g068"></a>
### G068 — Không thể tự xử lý cuộc gọi

**Nhãn gốc:** L183 khi không thể tự xử lý.

**Chương nguồn:** [B04-C22](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/21-Unit20-自分で対応できないとき.md>).

**Có thể dùng thêm tại:** [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

<a id="g069"></a>
### G069 — Để người gọi chờ

**Nhãn gốc:** L190 khi để người gọi đợi.

**Chương nguồn:** [B04-C20](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/19-Unit18-相手を待たせているとき.md>).

<a id="g070"></a>
### G070 — Email và thông tin công việc dạng viết

**Nhãn gốc:** L103 email công việc.

**Chương nguồn:** [B03-C19](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/18-Unit16-ビジネスEメール.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

## M19 — Thu xếp cuộc hẹn, đến thăm và tiếp đón

<a id="g017"></a>
### G017 — Thăm nhà người khác

**Nhãn gốc:** L381 thăm nhà.

**Chương nguồn:** [B23-C17](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/16-bai-16-tham-nha.md>).

**Có thể dùng thêm tại:** [M05 — Nhà ở, sống chung và chuyển nhà](ROADMAP_OUTLINE.md#m05).

<a id="g023"></a>
### G023 — Đặt chỗ và đặt dịch vụ

**Nhãn gốc:** L520 đặt chỗ.

**Chương nguồn:** [B21-C10](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/09-yoyaku.md>), [B22-C10](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/09-yoyaku.md>), [B23-C10](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/09-bai-9-dat-cho.md>).

**Có thể dùng thêm tại:** [M07 — Đi ăn, nhà hàng và những bữa gặp gỡ](ROADMAP_OUTLINE.md#m07), [M10 — Du lịch, công tác và lưu trú](ROADMAP_OUTLINE.md#m10).

<a id="g071"></a>
### G071 — Hẹn gặp

**Nhãn gốc:** L149 hẹn gặp; L150 hẹn gặp công việc; L151 hẹn khách hàng; L152 hẹn đối tác; L522 đặt lịch hẹn.

**Chương nguồn:** [B04-C24](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/23-Unit22-アポイントをとる.md>), [B10-C08](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/07-アポイントをとる.md>), [B15-C05](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/04-bai-04.md>), [B15-C12](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/11-bai-11.md>), [B16-C07](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/07-Unit6-社外の交渉.md>), [B21-C19](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/18-apointmento.md>), [B22-C19](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/18-apointmento.md>), [B23-C19](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/18-bai-18-hen-gap.md>).

**Có thể dùng thêm tại:** [M04 — Sinh hoạt, thời gian và kế hoạch](ROADMAP_OUTLINE.md#m04).

<a id="g072"></a>
### G072 — Đến thăm, ra về và đón tiếp

**Nhãn gốc:** L109 giao tiếp khi ra về; L110 giao tiếp khi đến nơi; L380 thăm công ty; L382 thăm đối tác; L485 đi thăm; L512 đón khách; L514 đón tiếp khách.

**Chương nguồn:** [B03-C15](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/14-Unit12-接客・訪問.md>), [B05-C03](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/02-ch1-keigo.md>), [B10-C09](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/08-訪問する.md>), [B21-C17](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/16-houmon.md>), [B22-C17](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/16-houmon.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

## M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng

<a id="g073"></a>
### G073 — Phục vụ, tiếp đãi và tư vấn khách

**Nhãn gốc:** L172 hỗ trợ khách hàng; L243 lời với khách; L317 omotenashi; L325 phản hồi khách hàng; L334 phục vụ khách; L376 thái độ phục vụ; L398 tiếp đãi; L430 tư vấn khách.

**Chương nguồn:** [B03-C16](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/15-Unit13-接待・会食.md>), [B05-C02](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/01-jo.md>), [B05-C05](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/04-ch3-hanbaiten.md>), [B05-C08](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/07-ch6-sonota.md>), [B15-C14](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/13-bai-13.md>), [B15-C16](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/15-bai-15.md>), [B18-C07](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md>).

**Có thể dùng thêm tại:** [M07 — Đi ăn, nhà hàng và những bữa gặp gỡ](ROADMAP_OUTLINE.md#m07), [M08 — Mua sắm, thanh toán và dịch vụ đời sống](ROADMAP_OUTLINE.md#m08), [M10 — Du lịch, công tác và lưu trú](ROADMAP_OUTLINE.md#m10).

<a id="g074"></a>
### G074 — Phàn nàn, khiếu nại và xử lý

**Nhãn gốc:** L016 báo cáo khiếu nại; L318 phàn nàn; L396 tiếp nhận khiếu nại; L469 xử lý khiếu nại; L470 xử lý vấn đề.

**Chương nguồn:** [B05-C04](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/03-ch2-inshokuten.md>), [B08-C03](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/02-part2-kinou.md>), [B09-C22](<../../knowledge/なめらか日本語会話/chapters/22-21-文句を言う・断る.md>), [B15-C07](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/06-bai-06.md>), [B15-C08](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/07-bai-07.md>), [B15-C09](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/08-bai-08.md>), [B25-C08](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/07-bai-6-monku.md>), [B26-C12](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/10-bai-10.md>).

**Có thể dùng thêm tại:** [M05 — Nhà ở, sống chung và chuyển nhà](ROADMAP_OUTLINE.md#m05), [M07 — Đi ăn, nhà hàng và những bữa gặp gỡ](ROADMAP_OUTLINE.md#m07), [M08 — Mua sắm, thanh toán và dịch vụ đời sống](ROADMAP_OUTLINE.md#m08), [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

<a id="g075"></a>
### G075 — Khách hàng mới và phát triển quan hệ

**Nhãn gốc:** L194 khách hàng mới.

**Chương nguồn:** [B15-C11](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/10-bai-10.md>).

**Có thể dùng thêm tại:** [M22 — Chào bán, thương lượng và hợp tác kinh doanh](ROADMAP_OUTLINE.md#m22).

## M21 — Họp, báo cáo và trình bày ý tưởng

<a id="g076"></a>
### G076 — Họp và phát biểu

**Nhãn gốc:** L319 phát biểu; L367 tham gia cuộc họp.

**Chương nguồn:** [B02-C17](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/15-挨拶する.md>), [B13-C09](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/08-unit-8-hoi-thoai-dai.md>), [B15-C06](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/05-bai-05.md>).

**Có thể dùng thêm tại:** [M13 — Sở thích, giải trí, ngày nghỉ và sự kiện](ROADMAP_OUTLINE.md#m13).

## M22 — Chào bán, thương lượng và hợp tác kinh doanh

<a id="g077"></a>
### G077 — Bán hàng, chào bán và chốt đơn

**Nhãn gốc:** L013 bán hàng; L047 chào bán sản phẩm; L061 chốt đơn hàng.

**Chương nguồn:** [B15-C10](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/09-bai-09.md>), [B15-C13](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/12-bai-12.md>), [B15-C16](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/15-bai-15.md>).

**Có thể dùng thêm tại:** [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

<a id="g078"></a>
### G078 — Thương lượng và chi phí

**Nhãn gốc:** L033 chi phí; L496 đàm phán.

**Chương nguồn:** [B15-C15](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/14-bai-14.md>).

**Có thể dùng thêm tại:** [M08 — Mua sắm, thanh toán và dịch vụ đời sống](ROADMAP_OUTLINE.md#m08).

## M23 — Kể trải nghiệm, chia sẻ cảm xúc và nhận xét

<a id="g079"></a>
### G079 — An tâm, dễ chịu và bớt lo

**Nhãn gốc:** L003 an tâm; L004 an tâm và dễ chịu; L201 không bận tâm.

**Chương nguồn:** [B12-C16](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/15-part2-b-anshin.md>), [B20-C07](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/06-section-e.md>), [B24-C10](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/09-section-h.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02).

<a id="g080"></a>
### G080 — Lo lắng, bận tâm và hồi hộp

**Nhãn gốc:** L023 bất an và lo lắng; L027 bận tâm; L171 hồi hộp; L219 lo lắng.

**Chương nguồn:** [B06-C06](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/05-k-61-81.md>), [B07-C09](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/08-part1-advice.md>), [B20-C14](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/13-section-l.md>), [B24-C11](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/10-section-i.md>).

**Có thể dùng thêm tại:** [M11 — Sức khỏe và chăm sóc bản thân](ROADMAP_OUTLINE.md#m11).

<a id="g081"></a>
### G081 — Khó chịu, bất mãn và không hài lòng

**Nhãn gốc:** L024 bất mãn; L025 bất mãn và phản đối; L032 bực bội; L198 khó chịu; L199 khó chịu và bất bình.

**Chương nguồn:** [B06-C04](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/03-a-25-39.md>), [B06-C11](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/10-h-155-171.md>), [B12-C22](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/21-part2-b-fuman.md>), [B24-C13](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/12-section-k.md>), [B24-C17](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/16-section-o.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

<a id="g082"></a>
### G082 — Tức giận

**Nhãn gốc:** L434 tức giận.

**Chương nguồn:** [B24-C14](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/13-section-l.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02).

<a id="g083"></a>
### G083 — Chán ngán, thất vọng và giảm hứng thú

**Nhãn gốc:** L053 chán ngán; L372 thiếu hứng thú; L384 thất vọng và chán nản.

**Chương nguồn:** [B20-C20](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/19-section-r.md>), [B20-C21](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/20-section-s.md>), [B24-C15](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/14-section-m.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02).

<a id="g084"></a>
### G084 — Không hợp

**Nhãn gốc:** L202 không hợp.

**Chương nguồn:** [B20-C20](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/19-section-r.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M08 — Mua sắm, thanh toán và dịch vụ đời sống](ROADMAP_OUTLINE.md#m08).

<a id="g085"></a>
### G085 — Hy vọng, nguyện vọng và mong chờ

**Nhãn gốc:** L143 hy vọng; L144 hy vọng và mong chờ; L176 khao khát; L248 mong ước và nguyện vọng; L274 nguyện vọng; L412 trông đợi.

**Chương nguồn:** [B01-C03](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/02-nguyen-vong.md>), [B20-C09](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/08-section-g.md>), [B24-C06](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/05-section-d.md>), [B24-C07](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/06-section-e.md>).

**Có thể dùng thêm tại:** [M04 — Sinh hoạt, thời gian và kế hoạch](ROADMAP_OUTLINE.md#m04).

<a id="g086"></a>
### G086 — Ý chí mạnh

**Nhãn gốc:** L479 ý chí mạnh.

**Chương nguồn:** [B24-C09](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/08-section-g.md>).

**Có thể dùng thêm tại:** [M04 — Sinh hoạt, thời gian và kế hoạch](ROADMAP_OUTLINE.md#m04).

<a id="g087"></a>
### G087 — Vui mừng và xúc động

**Nhãn gốc:** L308 niềm vui và xúc động; L451 vui mừng.

**Chương nguồn:** [B06-C13](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/12-y-195-206.md>), [B12-C16](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/15-part2-b-anshin.md>), [B24-C03](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/02-section-a.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M13 — Sở thích, giải trí, ngày nghỉ và sự kiện](ROADMAP_OUTLINE.md#m13).

<a id="g088"></a>
### G088 — Ngạc nhiên, kinh ngạc và cảm thán

**Nhãn gốc:** L082 cảm thán; L208 kinh ngạc; L279 ngạc nhiên; L361 sự bất ngờ.

**Chương nguồn:** [B06-C14](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/13-w-207-210.md>), [B07-C02](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/01-part1-surprise.md>), [B12-C23](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/22-part2-b-odoroki.md>), [B20-C25](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/24-section-w.md>), [B24-C04](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/03-section-b.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02).

<a id="g089"></a>
### G089 — Hoảng hốt và sợ hãi

**Nhãn gốc:** L142 hoảng hốt; L359 sợ hãi.

**Chương nguồn:** [B20-C13](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/12-section-k.md>), [B20-C25](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/24-section-w.md>).

**Có thể dùng thêm tại:** [M12 — An toàn, sự cố và trợ giúp khẩn cấp](ROADMAP_OUTLINE.md#m12).

<a id="g090"></a>
### G090 — Hối tiếc, phản tỉnh và xấu hổ

**Nhãn gốc:** L170 hối tiếc và tự nhìn lại; L327 phản tỉnh; L468 xấu hổ.

**Chương nguồn:** [B20-C23](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/22-section-u.md>), [B24-C16](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/15-section-n.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

<a id="g091"></a>
### G091 — Sơ ý và mất tập trung

**Nhãn gốc:** L036 cho là chắc và sơ ý; L254 mất tập trung.

**Chương nguồn:** [B20-C21](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/20-section-s.md>), [B24-C19](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/18-section-q.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

<a id="g092"></a>
### G092 — Hứng thú, quan tâm và say mê

**Nhãn gốc:** L175 hứng thú và quan tâm; L341 quan tâm; L350 say mê.

**Chương nguồn:** [B20-C05](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/04-section-c.md>), [B24-C08](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/07-section-f.md>).

**Có thể dùng thêm tại:** [M13 — Sở thích, giải trí, ngày nghỉ và sự kiện](ROADMAP_OUTLINE.md#m13).

<a id="g093"></a>
### G093 — Chu đáo và tận tình

**Nhãn gốc:** L038 chu đáo; L431 tận tình.

**Chương nguồn:** [B20-C08](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/07-section-f.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M20 — Phục vụ, hỗ trợ và xử lý phàn nàn khách hàng](ROADMAP_OUTLINE.md#m20).

<a id="g094"></a>
### G094 — Tính cách, kiêu ngạo, bướng bỉnh và nịnh nọt

**Nhãn gốc:** L021 bướng bỉnh; L209 kiêu ngạo; L315 nịnh nọt; L427 tính cách; L500 đánh giá con người.

**Chương nguồn:** [B20-C10](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/09-section-h.md>), [B20-C12](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/11-section-j.md>), [B20-C19](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/18-section-q.md>).

**Có thể dùng thêm tại:** [M03 — Gia đình và người thân](ROADMAP_OUTLINE.md#m03).

<a id="g095"></a>
### G095 — Chỉ trích, bị công kích và bị xem nhẹ

**Nhãn gốc:** L029 bị công kích; L055 chỉ trích; L501 đánh giá hành vi; L502 đánh giá thấp; L503 đánh giá thấp và xem nhẹ.

**Chương nguồn:** [B06-C13](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/12-y-195-206.md>), [B12-C20](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/19-part2-b-hyouka.md>), [B20-C18](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/17-section-p.md>), [B24-C21](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/20-section-s.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

<a id="g096"></a>
### G096 — Kiên nhẫn, khoan dung và nghiêm khắc

**Nhãn gốc:** L059 chịu đựng; L192 khoan dung; L272 nghiêm khắc.

**Chương nguồn:** [B20-C17](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/16-section-o.md>), [B20-C24](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/23-section-v.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

<a id="g097"></a>
### G097 — Đành chịu và từ bỏ

**Nhãn gốc:** L030 bỏ cuộc; L497 đành chịu; L498 đành chịu, từ bỏ.

**Chương nguồn:** [B12-C19](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/18-part2-b-akirame.md>), [B24-C18](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/17-section-p.md>).

**Có thể dùng thêm tại:** [M04 — Sinh hoạt, thời gian và kế hoạch](ROADMAP_OUTLINE.md#m04).

<a id="g098"></a>
### G098 — Diễn biến, xu hướng và điều kiện thuận lợi

**Nhãn gốc:** L091 diễn biến; L374 thuận lợi; L463 xu hướng.

**Chương nguồn:** [B20-C03](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/02-section-a.md>), [B20-C27](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/26-section-y.md>), [B20-C28](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/27-section-z.md>).

**Có thể dùng thêm tại:** [M04 — Sinh hoạt, thời gian và kế hoạch](ROADMAP_OUTLINE.md#m04).

<a id="g099"></a>
### G099 — May mắn

**Nhãn gốc:** L247 may mắn.

**Chương nguồn:** [B20-C03](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/02-section-a.md>).

<a id="g100"></a>
### G100 — Khó khăn, trở ngại và kết quả bất lợi

**Nhãn gốc:** L200 khó khăn; L326 phản tác dụng; L417 trở ngại; L426 tình thế khó và thiếu dư dả.

**Chương nguồn:** [B12-C17](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/16-part2-b-warui.md>), [B20-C22](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/21-section-t.md>), [B24-C12](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/11-section-j.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

<a id="g101"></a>
### G101 — Rủi ro và đánh liều

**Nhãn gốc:** L348 rủi ro; L504 đánh liều.

**Chương nguồn:** [B20-C11](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/10-section-i.md>), [B20-C24](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/23-section-v.md>).

**Có thể dùng thêm tại:** [M22 — Chào bán, thương lượng và hợp tác kinh doanh](ROADMAP_OUTLINE.md#m22).

<a id="g102"></a>
### G102 — Phản bội

**Nhãn gốc:** L323 phản bội.

**Chương nguồn:** [B20-C26](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/25-section-x.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M03 — Gia đình và người thân](ROADMAP_OUTLINE.md#m03).

<a id="g103"></a>
### G103 — Tai họa theo cách nói tu từ

**Nhãn gốc:** L365 tai họa.

**Chương nguồn:** [B20-C26](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/25-section-x.md>).

<a id="g104"></a>
### G104 — Cảm xúc, cảm nhận và đánh giá

**Nhãn gốc:** L009 biểu đạt cảm xúc; L081 cảm nhận; L083 cảm tưởng; L084 cảm xúc; L216 kể cảm nhận; L292 nhận xét; L293 nhận xét thường ngày; L295 nhận định; L375 thái độ; L422 tâm lý; L423 tâm trạng; L499 đánh giá.

**Chương nguồn:** [B01-C02](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/01-cam-xuc.md>), [B06-C02](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/01-a-01-10.md>), [B06-C03](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/02-a-11-24.md>), [B06-C05](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/04-k-40-60.md>), [B06-C07](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/06-s-82-98.md>), [B06-C10](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/09-n-138-154.md>), [B06-C12](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/11-m-172-194.md>), [B07-C04](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/03-part1-feelings.md>), [B07-C06](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/05-part1-evaluation.md>), [B07-C08](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/07-part1-will.md>), [B11-C10](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/08-part2-tinh-tu.md>), [B11-C12](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/10-part2-cuoi-cau.md>), [B12-C17](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/16-part2-b-warui.md>), [B12-C24](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/23-part2-c-homeru.md>), [B14-C06](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/05-unit-4.md>), [B19-C06](<../../knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/05-part4.md>), [B20-C28](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/27-section-z.md>), [B24-C02](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/01-introduction.md>), [B25-C10](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/09-bai-8-kansou.md>), [B26-C06](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/04-bai-4.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M13 — Sở thích, giải trí, ngày nghỉ và sự kiện](ROADMAP_OUTLINE.md#m13).

<a id="g105"></a>
### G105 — Nhận ra và hiểu tình thế

**Nhãn gốc:** L137 hiểu lời; L138 hiểu rõ; L139 hiểu ý; L289 nhận ra; L526 đọc tình huống.

**Chương nguồn:** [B02-C11](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/09-了解する.md>), [B06-C14](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/13-w-207-210.md>), [B20-C06](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/05-section-d.md>), [B23-C03](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/02-bai-2-hoi-lai-cho-ro.md>).

**Có thể dùng thêm tại:** [M17 — Phối hợp, bàn giao và xử lý công việc](ROADMAP_OUTLINE.md#m17).

## M24 — Văn hóa, đất nước và cách sống

<a id="g106"></a>
### G106 — Phong tục và cách nói của người Nhật

**Nhãn gốc:** L067 cách nói Nhật; L164 hỏi phong tục.

**Chương nguồn:** [B23-C14](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/13-bai-13-phong-tuc-cach-noi.md>).

## X01 — Nghe, phát âm, nhịp điệu và âm nói

<a id="g107"></a>
### G107 — Biến âm, âm nói và rút gọn âm

**Nhãn gốc:** L005 biến âm; L006 biến đổi âm; L346 rút gọn âm; L475 âm nói.

**Chương nguồn:** [B09-C02](<../../knowledge/なめらか日本語会話/chapters/02-01-てる・てく・とく.md>), [B09-C03](<../../knowledge/なめらか日本語会話/chapters/03-02-ちゃ・じゃ・きゃ.md>), [B09-C04](<../../knowledge/なめらか日本語会話/chapters/04-03-たって・だって.md>), [B09-C06](<../../knowledge/なめらか日本語会話/chapters/06-05-ん.md>), [B09-C07](<../../knowledge/なめらか日本語会話/chapters/07-06-変化した言葉.md>), [B12-C07](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/06-part1-henkei.md>), [B14-C03](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/02-unit-1.md>).

<a id="g108"></a>
### G108 — Khẩu ngữ, lược lời và dạng nói thân mật

**Nhãn gốc:** L088 cụm rút ngắn; L099 dạng nói thân mật; L205 khẩu ngữ; L227 lược lời; L228 lược trợ từ; L275 ngôn ngữ nói.

**Chương nguồn:** [B09-C02](<../../knowledge/なめらか日本語会話/chapters/02-01-てる・てく・とく.md>), [B09-C03](<../../knowledge/なめらか日本語会話/chapters/03-02-ちゃ・じゃ・きゃ.md>), [B09-C04](<../../knowledge/なめらか日本語会話/chapters/04-03-たって・だって.md>), [B09-C05](<../../knowledge/なめらか日本語会話/chapters/05-04-って・て.md>), [B09-C08](<../../knowledge/なめらか日本語会話/chapters/08-07-助詞の省略.md>), [B09-C09](<../../knowledge/なめらか日本語会話/chapters/09-08-短縮句.md>), [B09-C10](<../../knowledge/なめらか日本語会話/chapters/10-09-決まり文句.md>), [B12-C06](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/05-part1-shouryaku.md>), [B12-C07](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/06-part1-henkei.md>), [B12-C28](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/27-part3-nani.md>).

## X02 — Mẫu câu, ngữ pháp và vốn biểu đạt

<a id="g109"></a>
### G109 — Mẫu câu và ngữ pháp

**Nhãn gốc:** L071 câu cơ bản; L255 mẫu câu; L256 mẫu câu cốt lõi; L257 mẫu danh từ; L258 mẫu ngữ pháp; L259 mẫu tính từ; L260 mẫu đa dạng; L261 mẫu động từ; L386 thể te.

**Chương nguồn:** [B08-C04](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/03-part3-bunpou.md>), [B08-C07](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/06-basic70.md>), [B11-C06](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/04-part1-mau-04-08.md>), [B11-C08](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/06-part2-dong-tu.md>), [B11-C09](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/07-part2-danh-tu.md>), [B11-C10](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/08-part2-tinh-tu.md>), [B11-C15](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/13-part2-nhieu-dang.md>), [B12-C03](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/02-part1-bun-setsuzoku.md>), [B12-C04](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/03-part1-doushi-setsuzoku.md>), [B12-C05](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/04-part1-tekei.md>).

<a id="g110"></a>
### G110 — Trợ từ cuối câu ne, yo, yone

**Nhãn gốc:** L064 cuối câu; L269 ne; L418 trợ từ cuối câu; L471 yo; L472 yone.

**Chương nguồn:** [B09-C20](<../../knowledge/なめらか日本語会話/chapters/20-19-主張を伝える.md>), [B11-C03](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/01-ne.md>), [B11-C04](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/02-yo.md>), [B11-C05](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/03-yone.md>), [B11-C12](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/10-part2-cuoi-cau.md>).

<a id="g111"></a>
### G111 — Dạng って

**Nhãn gốc:** L420 tte.

**Chương nguồn:** [B09-C05](<../../knowledge/なめらか日本語会話/chapters/05-04-って・て.md>).

<a id="g112"></a>
### G112 — Chỉ xuất, tham chiếu và cách nói về vị trí

**Nhãn gốc:** L056 chỉ xuất; L366 tham chiếu; L455 vị trí.

**Chương nguồn:** [B11-C14](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/12-part2-kosoado.md>), [B12-C08](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/07-part1-kosoado.md>).

<a id="g113"></a>
### G113 — Từ hỏi

**Nhãn gốc:** L441 từ hỏi.

**Chương nguồn:** [B12-C28](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/27-part3-nani.md>).

<a id="g114"></a>
### G114 — Từ tượng thanh, tượng hình

**Nhãn gốc:** L442 từ tượng thanh; L443 từ tượng thanh tượng hình.

**Chương nguồn:** [B14-C06](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/05-unit-4.md>), [B19-C02](<../../knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/01-jo-sho.md>).

<a id="g115"></a>
### G115 — Cách nói, biểu thức và diễn đạt tự nhiên

**Nhãn gốc:** L007 biểu thức thông dụng; L008 biểu đạt chức năng; L011 biểu đạt tự nhiên; L066 cách nói; L068 cách nói thiết thực; L072 câu giao tiếp; L073 câu nói cố định; L092 diễn đạt chính xác; L174 hội thoại tự nhiên; L237 lời nói quen dùng; L240 lời thoại thực tế; L241 lời thường ngày; L356 sắc thái lời nói; L440 từ diễn đạt.

**Chương nguồn:** [B02-C18](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/16-便利な表現.md>), [B03-C07](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/06-Unit05-話し方.md>), [B06-C04](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/03-a-25-39.md>), [B07-C11](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/10-part2-routines.md>), [B08-C04](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/03-part3-bunpou.md>), [B08-C05](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md>), [B09-C10](<../../knowledge/なめらか日本語会話/chapters/10-09-決まり文句.md>), [B11-C15](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/13-part2-nhieu-dang.md>), [B12-C03](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/02-part1-bun-setsuzoku.md>), [B12-C09](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/08-part2-a-hanou.md>), [B12-C18](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/17-part2-b-kyouchou.md>), [B12-C27](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/26-part3-kaiwa-kotoba.md>), [B14-C07](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/06-unit-5.md>), [B19-C02](<../../knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/01-jo-sho.md>), [B19-C03](<../../knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/02-part1.md>).

<a id="g116"></a>
### G116 — Hành động, cách thực hiện và sự thay đổi

**Nhãn gốc:** L069 cách thực hiện; L147 hành động; L370 thay đổi.

**Chương nguồn:** [B19-C03](<../../knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/02-part1.md>), [B19-C04](<../../knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/03-part2.md>).

<a id="g117"></a>
### G117 — Mô tả trạng thái và mức độ

**Nhãn gốc:** L250 mô tả; L267 mức độ; L413 trạng thái; L414 trạng thái sự vật.

**Chương nguồn:** [B11-C10](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/08-part2-tinh-tu.md>), [B12-C20](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/19-part2-b-hyouka.md>), [B14-C06](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/05-unit-4.md>), [B19-C05](<../../knowledge/日本人がよく使う 日本語会話 オノマトペ基本表現180/chapters/04-part3.md>).

## X03 — Mạch hội thoại, lượt lời và phản hồi người nghe

<a id="g118"></a>
### G118 — Cấu trúc, duy trì và lặp lại trong hội thoại

**Nhãn gốc:** L087 cấu trúc hội thoại; L096 duy trì hội thoại; L229 lặp từ; L253 mạch hội thoại.

**Chương nguồn:** [B07-C10](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/09-part2-response.md>), [B09-C08](<../../knowledge/なめらか日本語会話/chapters/08-07-助詞の省略.md>), [B09-C11](<../../knowledge/なめらか日本語会話/chapters/11-10-くり返し.md>), [B09-C14](<../../knowledge/なめらか日本語会話/chapters/14-13-会話を進める.md>), [B11-C02](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/00-mo-dau.md>), [B11-C08](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/06-part2-dong-tu.md>), [B12-C02](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/01-josho.md>), [B12-C10](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/09-part2-a-hajimeru.md>).

<a id="g119"></a>
### G119 — Phản hồi người nghe, aizuchi và tiếp lời

**Nhãn gốc:** L001 aizuchi; L148 hưởng ứng; L297 nhắc lại; L324 phản hồi; L328 phản ứng; L329 phản ứng hội thoại; L330 phản ứng người nghe; L394 tiếp lời; L507 đáp lời; L510 đáp lời tự nhiên; L528 đối đáp ngắn.

**Chương nguồn:** [B01-C02](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/01-cam-xuc.md>), [B02-C09](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/07-話しかける.md>), [B03-C07](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/06-Unit05-話し方.md>), [B06-C02](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/01-a-01-10.md>), [B06-C03](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/02-a-11-24.md>), [B06-C11](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/10-h-155-171.md>), [B07-C10](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/09-part2-response.md>), [B09-C11](<../../knowledge/なめらか日本語会話/chapters/11-10-くり返し.md>), [B09-C14](<../../knowledge/なめらか日本語会話/chapters/14-13-会話を進める.md>), [B09-C17](<../../knowledge/なめらか日本語会話/chapters/17-16-反応を見ながら話す.md>), [B09-C18](<../../knowledge/なめらか日本語会話/chapters/18-17-あいづち.md>), [B09-C19](<../../knowledge/なめらか日本語会話/chapters/19-18-確かめる.md>), [B11-C11](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/09-part2-dau-cau.md>), [B11-C13](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/11-part2-noi-thoai.md>), [B12-C12](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/11-part2-a-uketsugu.md>), [B12-C14](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/13-part2-a-hitei.md>), [B14-C03](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/02-unit-1.md>), [B14-C05](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/04-unit-3.md>), [B15-C12](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/11-bai-11.md>), [B22-C05](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/04-kotowari.md>), [B27-C07](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/06-bai-05-shippai.md>), [B27-C11](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/10-bai-09-shumi.md>).

<a id="g120"></a>
### G120 — Nối ý, bổ sung thông tin và chuyển chủ đề

**Nhãn gốc:** L031 bổ sung thông tin; L040 chuyển chủ đề; L238 lời nối hội thoại; L316 nối ý.

**Chương nguồn:** [B06-C08](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/07-s-99-115.md>), [B12-C11](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/10-part2-a-tsuketasu.md>), [B12-C12](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/11-part2-a-uketsugu.md>).

<a id="g121"></a>
### G121 — Chốt ý và kết thúc hội thoại

**Nhãn gốc:** L060 chốt ý; L214 kết thúc hội thoại.

**Chương nguồn:** [B12-C15](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/14-part2-a-oeru.md>).

<a id="g122"></a>
### G122 — Ngập ngừng và từ đệm

**Nhãn gốc:** L280 ngập ngừng; L444 từ đệm.

**Chương nguồn:** [B12-C13](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/12-part2-a-ma.md>).

<a id="g123"></a>
### G123 — Nói để ngỏ, nói lảng, mơ hồ và phủ định nhẹ

**Nhãn gốc:** L010 biểu đạt mơ hồ; L311 nói lảng; L312 nói để ngỏ; L335 phủ định nhẹ; L415 trả lời tế nhị.

**Chương nguồn:** [B09-C12](<../../knowledge/なめらか日本語会話/chapters/12-11-あいまい表現.md>), [B09-C15](<../../knowledge/なめらか日本語会話/chapters/15-14-話を切り出す.md>), [B09-C16](<../../knowledge/なめらか日本語会話/chapters/16-15-答える.md>), [B09-C21](<../../knowledge/なめらか日本語会話/chapters/21-20-お礼を言う・あやまる.md>), [B12-C14](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/13-part2-a-hitei.md>), [B20-C10](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/09-section-h.md>).

<a id="g124"></a>
### G124 — Nhấn mạnh, nhấn thông tin và đảo trật tự

**Nhãn gốc:** L283 nhấn mạnh; L284 nhấn thông tin; L518 đảo trật tự.

**Chương nguồn:** [B09-C13](<../../knowledge/なめらか日本語会話/chapters/13-12-語順の変化.md>), [B12-C18](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/17-part2-b-kyouchou.md>).

<a id="g125"></a>
### G125 — Nêu chủ đề và mở đầu câu

**Nhãn gốc:** L265 mở đầu câu; L309 nêu chủ đề.

**Chương nguồn:** [B11-C09](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/07-part2-danh-tu.md>), [B11-C11](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/09-part2-dau-cau.md>).

<a id="g126"></a>
### G126 — Kể chuyện, trò chuyện chủ đề và đoạn dài

**Nhãn gốc:** L173 hội thoại dài; L215 kể chuyện; L411 trò chuyện chủ đề.

**Chương nguồn:** [B08-C06](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/05-part5-topic.md>), [B12-C02](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/01-josho.md>), [B13-C09](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/08-unit-8-hoi-thoai-dai.md>), [B14-C07](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/06-unit-5.md>).

**Có thể dùng thêm tại:** [M23 — Kể trải nghiệm, chia sẻ cảm xúc và nhận xét](ROADMAP_OUTLINE.md#m23).

## X04 — Lịch sự, kính ngữ và quan hệ người nói

<a id="g127"></a>
### G127 — Lịch sự, dè dặt và điều chỉnh lời nói

**Nhãn gốc:** L097 dè dặt; L123 giữ lịch sự; L230 lịch sự; L232 lời lịch sự; L236 lời nói; L242 lời trang trọng; L246 lựa chọn kính ngữ; L320 phép lịch sự; L401 trang trọng; L488 điều chỉnh lời.

**Chương nguồn:** [B02-C07](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/05-意思を表明する.md>), [B02-C12](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/10-断る.md>), [B03-C10](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/09-Unit08-携帯電話のマナー.md>), [B03-C12](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/11-Unit10-社会人らしい行動と言葉遣い.md>), [B09-C17](<../../knowledge/なめらか日本語会話/chapters/17-16-反応を見ながら話す.md>), [B12-C21](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/20-part2-b-teinei.md>), [B18-C02](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/02-序章-敬語の世界.md>), [B18-C03](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/03-PART1-丁寧語・美化語.md>), [B18-C05](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/05-PART1-謙譲語・丁重語.md>), [B23-C18](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/17-bai-17-kinh-ngu.md>).

<a id="g128"></a>
### G128 — Kính ngữ: tôn kính, khiêm nhường và mỹ hóa

**Nhãn gốc:** L191 khiêm nhường ngữ; L211 kính ngữ; L268 mỹ hóa ngữ; L428 tôn kính ngữ; L535 động từ kính ngữ.

**Chương nguồn:** [B03-C08](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/07-Unit06-敬語の使い方.md>), [B03-C18](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/17-Unit15-電話応対.md>), [B05-C03](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/02-ch1-keigo.md>), [B18-C03](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/03-PART1-丁寧語・美化語.md>), [B18-C04](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/04-PART1-尊敬語.md>), [B18-C05](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/05-PART1-謙譲語・丁重語.md>), [B21-C18](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/17-keigo.md>), [B22-C18](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/17-keigo.md>), [B23-C18](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/17-bai-17-kinh-ngu.md>).

<a id="g129"></a>
### G129 — Lời nói theo quan hệ người nói

**Nhãn gốc:** L337 quan hệ người nói.

**Chương nguồn:** [B22-C07](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/06-aisatsu.md>), [B27-C03](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/02-bai-01-deai.md>).

## X05 — Chức năng giao tiếp xuyên bối cảnh

<a id="g130"></a>
### G130 — Hỏi, tìm và trao đổi thông tin

**Nhãn gốc:** L153 hỏi; L165 hỏi thông tin; L168 hỏi đáp; L290 nhận thông tin; L405 trao đổi thông tin; L521 đặt câu hỏi.

**Chương nguồn:** [B02-C08](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/06-質問する.md>), [B07-C03](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/02-part1-questions.md>), [B11-C06](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/04-part1-mau-04-08.md>), [B12-C06](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/05-part1-shouryaku.md>), [B14-C04](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/03-unit-2.md>), [B21-C16](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/15-toiawase.md>), [B22-C09](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/08-shain-ryokou.md>), [B22-C16](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/15-toiawase.md>), [B23-C16](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/15-bai-15-hoi-thong-tin.md>), [B27-C10](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/09-bai-08-eki-de.md>).

<a id="g131"></a>
### G131 — Hỏi lại, làm rõ và hỏi nghĩa

**Nhãn gốc:** L161 hỏi lại; L162 hỏi nghĩa; L163 hỏi nghĩa tiếng Nhật; L166 hỏi tiếp; L221 làm rõ; L222 làm rõ tiếng Nhật.

**Chương nguồn:** [B02-C15](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/13-確認する.md>), [B12-C26](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/25-part2-c-shitsumon.md>), [B21-C03](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/02-wakaranai-nihongo.md>), [B22-C03](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/02-wakaranai-nihongo.md>), [B23-C03](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/02-bai-2-hoi-lai-cho-ro.md>).

<a id="g132"></a>
### G132 — Hỏi cách làm và cách diễn đạt

**Nhãn gốc:** L156 hỏi cách diễn đạt; L157 hỏi cách làm; L158 hỏi cách nói.

**Chương nguồn:** [B21-C14](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/13-hyougen-yarikata.md>), [B22-C14](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/13-hyougen-yarikata.md>).

<a id="g133"></a>
### G133 — Hỏi ý kiến và cảm nhận

**Nhãn gốc:** L159 hỏi cảm nhận; L167 hỏi ý kiến.

**Chương nguồn:** [B02-C08](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/06-質問する.md>), [B02-C13](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/11-相談する.md>).

<a id="g134"></a>
### G134 — Hỏi gián tiếp và nêu ý kiến nhẹ

**Nhãn gốc:** L160 hỏi gián tiếp; L481 ý kiến nhẹ.

**Chương nguồn:** [B09-C24](<../../knowledge/なめらか日本語会話/chapters/24-23-問いかける.md>).

<a id="g135"></a>
### G135 — Nhờ vả và yêu cầu

**Nhãn gốc:** L306 nhờ vả; L307 nhờ vả công việc; L473 yêu cầu; L474 yêu cầu lịch sự.

**Chương nguồn:** [B02-C10](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/08-依頼する.md>), [B02-C18](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/16-便利な表現.md>), [B07-C07](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/06-part1-requests.md>), [B08-C03](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/02-part2-kinou.md>), [B09-C09](<../../knowledge/なめらか日本語会話/chapters/09-08-短縮句.md>), [B10-C06](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/05-頼む・断る.md>), [B12-C22](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/21-part2-b-fuman.md>), [B18-C06](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/06-PART2-機能別.md>), [B21-C04](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/03-irai.md>), [B22-C04](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/03-irai.md>), [B23-C04](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/03-bai-3-nho-va.md>), [B25-C07](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/06-bai-5-irai-shiji.md>), [B26-C03](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/01-bai-1.md>).

<a id="g136"></a>
### G136 — Giúp đỡ

**Nhãn gốc:** L117 giúp đỡ.

**Chương nguồn:** [B12-C05](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/04-part1-tekei.md>).

<a id="g137"></a>
### G137 — Xin phép và cho phép

**Nhãn gốc:** L037 cho phép; L460 xin phép; L461 xin phép công việc.

**Chương nguồn:** [B02-C14](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/12-許可を求める.md>), [B10-C07](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/06-許可をもらう.md>), [B16-C08](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/08-Unit7-社内の交渉.md>), [B25-C05](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/04-bai-3-kyoka.md>).

<a id="g138"></a>
### G138 — Đề nghị

**Nhãn gốc:** L523 đề nghị.

**Chương nguồn:** [B11-C06](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/04-part1-mau-04-08.md>), [B12-C06](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/05-part1-shouryaku.md>), [B12-C21](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/20-part2-b-teinei.md>).

<a id="g139"></a>
### G139 — Từ chối theo đối tượng và tình huống

**Nhãn gốc:** L435 từ chối; L436 từ chối lời mời; L437 từ chối lời nhờ; L438 từ chối tế nhị; L439 từ chối yêu cầu.

**Chương nguồn:** [B02-C12](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/10-断る.md>), [B08-C03](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/02-part2-kinou.md>), [B09-C22](<../../knowledge/なめらか日本語会話/chapters/22-21-文句を言う・断る.md>), [B09-C23](<../../knowledge/なめらか日本語会話/chapters/23-22-申し出を断る.md>), [B10-C06](<../../knowledge/にほんごで働く！ビジネス日本語30時間/chapters/05-頼む・断る.md>), [B16-C08](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/08-Unit7-社内の交渉.md>), [B21-C05](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/04-kotowari.md>), [B22-C05](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/04-kotowari.md>), [B23-C05](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/04-bai-4-tu-choi-loi-nho.md>).

<a id="g140"></a>
### G140 — Mời, rủ và đáp lời mời

**Nhãn gốc:** L233 lời mời; L234 lời mời lịch sự; L239 lời rủ; L262 mời rủ; L509 đáp lời mời.

**Chương nguồn:** [B08-C03](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/02-part2-kinou.md>), [B18-C06](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/06-PART2-機能別.md>), [B25-C04](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/03-bai-2-kanyuu.md>), [B27-C11](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/10-bai-09-shumi.md>).

<a id="g141"></a>
### G141 — Nhận lời

**Nhãn gốc:** L286 nhận lời.

**Chương nguồn:** [B02-C11](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/09-了解する.md>).

<a id="g142"></a>
### G142 — Xin lỗi trong quan hệ đời sống và công việc

**Nhãn gốc:** L457 xin lỗi; L458 xin lỗi người gọi đang giận; L459 xin lỗi đối tác.

**Chương nguồn:** [B04-C21](<../../knowledge/しごとの日本語 電話応対 基礎編/chapters/20-Unit19-怒っている相手に謝る.md>), [B05-C03](<../../knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/02-ch1-keigo.md>), [B09-C21](<../../knowledge/なめらか日本語会話/chapters/21-20-お礼を言う・あやまる.md>), [B16-C07](<../../knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/07-Unit6-社外の交渉.md>), [B17-C04](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/03-ミスをして謝る.md>), [B21-C13](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/12-owabi.md>), [B22-C13](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/12-owabi.md>), [B23-C13](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/12-bai-12-xin-loi.md>).

<a id="g143"></a>
### G143 — Khuyên nhủ, góp ý và nhắc nhở

**Nhãn gốc:** L124 góp ý; L193 khuyên nhủ; L299 nhắc nhở; L516 đưa lời khuyên.

**Chương nguồn:** [B02-C16](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/14-助言する.md>), [B07-C09](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/08-part1-advice.md>), [B26-C07](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/05-bai-5.md>), [B26-C10](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/08-bai-8.md>).

<a id="g144"></a>
### G144 — Xác nhận và xác nhận điều kiện

**Nhãn gốc:** L464 xác nhận; L467 xác nhận điều kiện.

**Chương nguồn:** [B02-C15](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/13-確認する.md>), [B03-C20](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/19-Unit17-指示を受ける.md>), [B07-C03](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/02-part1-questions.md>), [B09-C19](<../../knowledge/なめらか日本語会話/chapters/19-18-確かめる.md>), [B11-C05](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/03-yone.md>), [B12-C25](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/24-part2-c-kakunin.md>), [B22-C10](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/09-yoyaku.md>).

<a id="g145"></a>
### G145 — Giải thích, nêu lý do và truyền đạt

**Nhãn gốc:** L118 giải thích; L225 lý do; L310 nêu lý do; L408 truyền đạt.

**Chương nguồn:** [B07-C05](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/04-part1-explanation.md>), [B09-C23](<../../knowledge/なめらか日本語会話/chapters/23-22-申し出を断る.md>), [B11-C04](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/02-yo.md>), [B12-C22](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/21-part2-b-fuman.md>), [B12-C27](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/26-part3-kaiwa-kotoba.md>), [B22-C11](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/10-omiyage.md>).

<a id="g146"></a>
### G146 — Khả năng và giải thích khả năng

**Nhãn gốc:** L119 giải thích khả năng; L203 khả năng.

**Chương nguồn:** [B12-C04](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/03-part1-doushi-setsuzoku.md>), [B22-C20](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/19-chuui-o-ukeru.md>).

<a id="g147"></a>
### G147 — Thử làm

**Nhãn gốc:** L390 thử làm.

**Chương nguồn:** [B12-C05](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/04-part1-tekei.md>).

<a id="g148"></a>
### G148 — Chắc chắn, hoài nghi và thông tin chưa rõ

**Nhãn gốc:** L141 hoài nghi và chưa rõ; L362 sự chắc chắn; L385 thắc mắc; L534 độ chắc chắn thông tin.

**Chương nguồn:** [B01-C04](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/03-y-kien-quan-diem.md>), [B07-C02](<../../knowledge/すぐに使える 日本語会話 超ミニフレーズ200/chapters/01-part1-surprise.md>), [B24-C20](<../../knowledge/気持ちが伝わる 日本語会話 基本表現180/chapters/19-section-r.md>), [B25-C06](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/05-bai-4-jouhou.md>).

<a id="g149"></a>
### G149 — Thúc giục

**Nhãn gốc:** L379 thúc giục.

**Chương nguồn:** [B12-C25](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/24-part2-c-kakunin.md>).

<a id="g150"></a>
### G150 — Thuật lại thông tin và tin đồn

**Nhãn gốc:** L392 tin đồn; L407 truyền thông tin; L409 truyền đạt thông tin; L410 truyền đạt tin.

**Chương nguồn:** [B14-C04](<../../knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/03-unit-2.md>), [B25-C06](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/05-bai-4-jouhou.md>), [B27-C05](<../../knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/04-bai-03-uwasa.md>).

**Có thể dùng thêm tại:** [M02 — Trò chuyện và xây dựng quan hệ](ROADMAP_OUTLINE.md#m02), [M18 — Điện thoại, lời nhắn và liên lạc](ROADMAP_OUTLINE.md#m18).

<a id="g151"></a>
### G151 — So sánh và chênh lệch

**Nhãn gốc:** L354 so sánh chênh lệch.

**Chương nguồn:** [B20-C15](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/14-section-m.md>).

<a id="g152"></a>
### G152 — Ý kiến, tán thành và phản đối

**Nhãn gốc:** L206 khẳng định ý kiến; L480 ý kiến; L530 đồng tình; L531 đồng tình phản đối.

**Chương nguồn:** [B01-C04](<../../knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/03-y-kien-quan-diem.md>), [B09-C20](<../../knowledge/なめらか日本語会話/chapters/20-19-主張を伝える.md>), [B11-C03](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/01-ne.md>).

**Có thể dùng thêm tại:** [M21 — Họp, báo cáo và trình bày ý tưởng](ROADMAP_OUTLINE.md#m21), [M25 — Xã hội, công nghệ và tương lai](ROADMAP_OUTLINE.md#m25).

<a id="g153"></a>
### G153 — Gợi ý, đề xuất và lựa chọn

**Nhãn gốc:** L135 gợi ý; L245 lựa chọn; L524 đề xuất.

**Chương nguồn:** [B09-C09](<../../knowledge/なめらか日本語会話/chapters/09-08-短縮句.md>), [B11-C09](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/07-part2-danh-tu.md>), [B15-C10](<../../knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/09-bai-09.md>), [B25-C09](<../../knowledge/聞いて覚える話し方 日本語生中継 中～上級編/chapters/08-bai-7-teian.md>).

**Có thể dùng thêm tại:** [M04 — Sinh hoạt, thời gian và kế hoạch](ROADMAP_OUTLINE.md#m04), [M21 — Họp, báo cáo và trình bày ý tưởng](ROADMAP_OUTLINE.md#m21).

<a id="g154"></a>
### G154 — Thuyết phục

**Nhãn gốc:** L373 thuyết phục.

**Chương nguồn:** [B20-C11](<../../knowledge/日本人がよく使う 日本語会話お決まり表現180/chapters/10-section-i.md>).

**Có thể dùng thêm tại:** [M21 — Họp, báo cáo và trình bày ý tưởng](ROADMAP_OUTLINE.md#m21), [M22 — Chào bán, thương lượng và hợp tác kinh doanh](ROADMAP_OUTLINE.md#m22).

## X06 — Cách luyện và cấu trúc học liệu

<a id="g155"></a>
### G155 — Mục đích, chức năng và tổng hợp tình huống

**Nhãn gốc:** L063 chức năng hội thoại; L210 kiểm tra phép ứng xử; L266 mục đích giao tiếp; L425 tình huống giao tiếp; L433 tổng hợp tình huống; L515 đóng vai công ty.

**Chương nguồn:** [B03-C24](<../../knowledge/しごとの日本語 ビジネスマナー編/chapters/23-ビジネスマナー○×確認問題100.md>), [B08-C05](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md>), [B11-C07](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/05-warming-up-va-doumo.md>), [B12-C09](<../../knowledge/わかる！話せる！日本語会話 発展文型125/chapters/08-part2-a-hanou.md>), [B17-C06](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/05-総合タスク1.md>), [B17-C10](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/09-総合タスク2.md>), [B17-C15](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/14-総合タスク3.md>), [B17-C20](<../../knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/19-総合タスク4.md>).

<a id="g156"></a>
### G156 — Ôn mẫu câu và ôn biểu đạt

**Nhãn gốc:** L476 ôn biểu đạt; L477 ôn mẫu câu; L478 ôn tập giới thiệu.

**Chương nguồn:** [B02-C06](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/03-紹介する-復習.md>), [B08-C07](<../../knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/06-basic70.md>), [B11-C07](<../../knowledge/わかる！話せる！日本語会話 基本文型88/chapters/05-warming-up-va-doumo.md>).

<a id="g157"></a>
### G157 — Nghe hiểu và đối chiếu cách nói

**Nhãn gốc:** L270 nghe hiểu; L527 đối chiếu cách nói.

**Chương nguồn:** [B09-C06](<../../knowledge/なめらか日本語会話/chapters/06-05-ん.md>), [B09-C07](<../../knowledge/なめらか日本語会話/chapters/07-06-変化した言葉.md>).
