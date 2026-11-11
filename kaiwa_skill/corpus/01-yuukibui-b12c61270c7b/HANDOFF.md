# Bàn giao mới nhất book11 — 138/138 trang verified, build complete

- Cập nhật: 2026-11-11 13:09 JST; worker `production_book_11_root_cont7`, `gpt-6-sol/high`, điều phối `/root`; token `book11-cont7-20261111-b7e2` sẽ release sạch sau handoff.
- Book `01-yuukibui-b12c61270c7b`, PDF `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf` từ `kaiwa_skill/`, 138 trang vật lý; SHA-256 nguồn `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt này chuyển **p114–138 (25 trang)**, mỗi trang mở full render và direct4 trên/dưới; p127 thêm direct8 để xác nhận ruby tên `丸越＝まるこし`. Mỗi trang chép văn bản thuần, so hai chiều ảnh→Markdown→ảnh, record/evidence/verify riêng. Giữ p1–113 đã verified trước nguyên trạng.
- Sau `reconcile`/`build`: **138/138 verified, 0 pending/rendered/draft/needs_review/invalid; 0 issue**, `complete=true`, `transcription_complete=true`, `build.complete=true`, `verified_pages=138`. SHA-256 `build.json`: `748db061c84498d597a284e0c87dc03d2c3078d31437a6c4a9887d021ff061cf`. Trạng thái acceptance vẫn `coordinator_review_required` để root QA.

## Nội dung lượt cuối và điểm nguồn

- p114–119 kết 第十七課 `敬語`; p120–125 第十八課 `アポイントメント`; p126–129 第十九課 `注意を受ける`; p130–135 第二十課 `面接試験`. Giữ đầy đủ mẫu, ô trống, mục tiêu bold, vai/lượt thoại, ví dụ, số lề, ruby từng lần, trang in và watermark. p127 hội thoại `習慣の違い` có `丸越` ruby nguồn `まるこし`; p131–133 phỏng vấn `コピーライターに応募する` với lương/giờ làm lịch sử như in.
- p136 trang trắng chỉ có watermark, không có số in; p137 `あとがき` trang in124 giữ nguyên năm `1987年 8月`, thông tin trợ cấp/nhà xuất bản và bốn tên `鈴木禮子`, `郷司幸子`, `野村伸一`, `大橋伸六`; p138 trang cuối trắng chỉ watermark, không có số in.
- Không sửa tools/skill/Git/sách khác. Ảnh/crops/scratch chỉ trong `.cache/renders/<book_id>/`, không thuộc output. `book.md` và `search.jsonl` đã build đủ 138 trang.

## Tiếp theo

- Root làm QA/acceptance/Git theo quyền điều phối. Worker không tự xác nhận acceptance. Nếu root phát hiện sai lệch cục bộ, dùng nguồn/crop đã lưu để sửa và verify lại trang tương ứng rồi reconcile/build.

---

# Bàn giao trước book11 — WIP p1–113; p114 đã render

- Cập nhật: 2026-11-11 12:29 JST; worker `production_book_11_root_cont6`, `gpt-6-sol/high`, điều phối `/root`; token `book11-root107-20261111-7d3c` sẽ release sạch ngay sau handoff này.
- Book `01-yuukibui-b12c61270c7b`, 138 trang vật lý; PDF tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`; SHA-256 nguồn kiểm lại `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt này chuyển mới **p107–113 (7 trang)**. Mỗi trang mở full scale2 và direct4 trên/dưới; p107–112 thêm direct8 theo dải ruby/bold, p113 direct8 nửa đầu và direct4 nửa dưới xác nhận thật sự trống. So hai chiều ảnh→Markdown→ảnh và checkpoint từng trang. p114 render scale2 và mở full để kiểm nối, **chưa chép/verify**.
- Sau reconcile/build: **113/138 verified (p1–113), 1 rendered (p114), 24 pending (p115–138), 0 draft/needs_review/invalid, 0 issue/error**; `build_current=true`, bản ghép partial chỉ gồm p1–113. SHA-256 `build.json`: `b24e11405bc69f9ccc9a3d4a99f304b0d1322e40a5303019f97b0993bad541f0`.

## Nội dung lượt này và điểm nguồn

- p107–109 hoàn tất 第十六課 本文会話 `課長の家で`: nhân vật 課長／課長夫人／サイモン（部下）, cuộc thăm nhà, ăn uống rồi ra về. p107 kết ở chỉ dẫn サイモンさんは正座する, p108 tiếp lời 課長夫人; p108 cuối サイモン cảm ơn, p109 nối bằng 課長 rồi kết hội thoại. Giữ từng vai/lượt, chỉ dẫn hành động, ruby theo lần xuất hiện, số lề và punctuation. p109 tiếp `《類話》` mục1 料理をほめる, hai ví dụ A/B.
- p110 `類話` mục2 `酒を断る`: giữ tên `ブアリ君`, tám lượt, sự kiện 歓迎会の二次会 và 課長命令 như in; sau đó `語句の使い方` mục1–2. p111 mục3–9, p112 mục10–16, p113 mục17–18. Giữ ô trống và bold đúng phần mẫu theo occurrence, các ví dụ/ruby/ref p.94–97. p113 chỉ có hai mục ở đầu, nửa dưới trống ngoài số in100.
- p114 mở **第十七課 `敬語`**, hai hộp 談話型 (`近況を聞く`, `招待者が中座する`) có nhiều ô trống; không có câu nối từ p113. p1–106 verified cũ giữ nguyên. Không sửa tools/skill/Git/sách khác. Cache ảnh và scratch chỉ ở `.cache/renders/<book_id>/`, không thuộc output.

## Tiếp tục ngay

- **Physical p114 (trang in101)** là trang đầu chưa chép: đã render `p0114.png` và mở full. Cần direct4/crop hai hộp để đếm và giữ từng ô trống, vai A/B, chữ ruby và câu mục tiêu; tiếp p115–138.
- Worker mới kiểm source/status/claim thật rồi claim token mới sau release. Bảo toàn p1–113, mỗi trang full/crop và đối chiếu hai chiều, exact ruby/bold/roles/blanks/header/footer; chỗ không chắc thật ghi needs_review cụ thể và đi tiếp. Root giữ QA/Git/acceptance.

---

# Bàn giao mới nhất book11 — WIP p1–106; p107 đã render

- Cập nhật: 2026-11-11 12:11 JST; worker `production_book_11_root_cont5`, `gpt-6-sol/high`, điều phối `/root`; token `book11-root101-20261111-e61a` sẽ release sạch sau ghi handoff.
- Book `01-yuukibui-b12c61270c7b`, 138 trang vật lý; nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`; SHA-256 nguồn kiểm lại `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt này chuyển mới **p101–106 (6 trang)**, mở full source từng trang, direct4 trên/dưới; p101 direct8 theo các dải trái/giữa/phải, p102–105 thêm direct8 vùng ruby nhỏ. So hai chiều ảnh→Markdown→ảnh rồi checkpoint `record`/`verify` từng trang. p107 đã render scale2 và mở full chỉ để kiểm nối, **chưa chép/verify**.
- Sau reconcile/build: **106/138 verified (p1–106), 1 rendered (p107), 31 pending (p108–138), 0 draft/needs_review/invalid, 0 issue/error**; `build_current=true`, bản ghép partial chỉ gồm p1–106. SHA-256 `build.json`: `5a8a86e5613a63b374c48c613da516b9b8316a26e2191f81b350fcddf02546bf`.

## Nội dung lượt này và điểm nguồn

- p101 trang in88 `内閣の組織図`: chuyển tất cả ô/nhánh/chữ/ruby thành danh sách phân cấp có nhãn biên tập. Nhánh trái từ 内閣 có 安全保障会議, 内閣官房, 内閣法制局, 人事院; trục phải có 総理府 và các 省 cùng cấp, các 庁/委員会 con đặt đúng bên dưới. **会計検査院 là ô đứng riêng không có đường nối**, không gán nhánh. Giữ cơ cấu lịch sử như in (大蔵省, 郵政省, 労働省 v.v.). Root đã đọc chéo full/direct4 và draft p101, báo không thấy lệch nhãn/quan hệ.
- p102 mở 第十五課 `問い合わせ`, mục tiêu và hai hộp 談話型 về 催し物/施設, một ô trống trong mẫu điện thoại, đủ sáu loại gợi ý ở hộp đầu và hai hàng hộp sau. p103–104 `図書館の利用について聞く`: giữ hai đoạn gọi điện, các vai 交換手／チャン／図書, số 104 và 353-4231, `『アジア経済研究所』`, `『経済日報』`, giờ thư viện, 十何紙/二十紙 và câu hỏi cuối p103 nối đúng lời đáp đầu p104. p104 bắt đầu `語句の使い方` mục1–2, p105 kết bài15 mục3–5; bold từng occurrence nguồn.
- p106 mở 第十六課 `訪問`, mục tiêu và hai hộp 談話型: đi thăm/ra về, ba ô trống nguyên nguồn, từng lượt A/B, ruby. p107 mở `《本文会話》 課長の家で` với nhân vật 課長／課長夫人／サイモン; không có câu cắt từ p106.
- p1–100 verified cũ giữ nguyên; không sửa tools/skill/Git/sách khác. Ảnh/crops/scratch chỉ trong `.cache/renders/<book_id>/`, không thuộc output.

## Tiếp tục ngay

- **Physical p107 (trang in94)** là trang mới cần chép: đã render và mở full. `課長の家で`, サイモン đến nhà 課長; đầu hội thoại từ `—玄関でのあいさつ—`, lề 1/5/10/15/20/25; cần direct4/crop từng nửa để đọc đầy đủ lời/ruby, phân biệt 課長夫人／課長, rồi tiếp p108–138.
- Worker mới kiểm claim/status/hash thật, claim token mới sau release. Bảo toàn p1–106, mỗi trang tiếp tục full/crop và đối chiếu hai chiều. Chỗ không chắc thật ghi needs_review cụ thể và đi tiếp, không đoán. Root giữ QA/Git/acceptance.

---

# Bàn giao trước — WIP p1–100; p101 đã render

- Cập nhật: 2026-11-11 JST; worker `production_book_11_root_cont4`, `gpt-6-sol/high`, điều phối `/root`; token `book11-root95-20261111-f4c8` sẽ release sạch sau ghi handoff.
- Book `01-yuukibui-b12c61270c7b`, 138 trang vật lý; nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`; SHA-256 nguồn đã kiểm `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt này chuyển mới **p95–100 (6 trang)**, full render và direct4 trên/dưới mỗi trang, so hai chiều rồi verify từng trang. p101 đã render scale2, mở full để xác định bố cục và tạo direct4 hai nửa, **chưa chép/verify**.
- Sau reconcile/build: **100/138 verified (p1–100), 1 rendered (p101), 37 pending (p102–138), 0 draft/needs_review/invalid, 0 issue/error**; build partial, chưa completed/accepted. `book.md`/`search.jsonl` hiện chứa đúng p1–100. SHA-256 `build.json`: `87bedd8f96565c082cb4697c86afc19211f0b0cf361573d271120328481bb97a`.

## Nội dung lượt này và điểm nguồn

- p95 trang in82 là `《本文会話》 社長に紹介される`, 14 lượt của 課長／社長／ジョーンズ, phần giới thiệu 研修生 rồi nói về thị trường, ロックハート, 中東担当部長. p96 đầu tiếp lượt 社長 về 中東, tiếp hai lượt, rồi `《類話》` 1–2. Sơ đồ p96 chuyển đủ: ベルナール và A cùng khung 同じ会社; 伝言 từ ベルナール tới A, 伝える từ A tới B ngoài khung.
- p97 `類話` mục3 và sơ đồ: シャンベ trong アロー社, 伝言 tới A rồi 伝える tới B; phần `語句の使い方` mục1–3. p98 mục4–9(1), p99 nối9(2) rồi10–15. Giữ ô trống, ref p/l, bold theo từng lần nguồn, ruby từng occurrence. p100 chỉ có `〔類話〕` mục16 với hai ví dụ ở đầu trang; nửa dưới thực sự trống ngoài số in87.
- p1–94 verified cũ giữ nguyên. Không sửa tools/skills/Git/sách khác. Ảnh/crops/scratch chỉ trong cache sách, không thuộc output.

## Tiếp tục ngay

- **Physical p101 (trang in88)** là `内閣の組織図`, sơ đồ nhiều nhánh và chữ/ruby rất nhỏ. `p0101.png` đã mở full; `p0101-top4-cont4.png`/`p0101-bot4-cont4.png` đã tạo nhưng chưa mở. Cần crop direct8/16 từng cột và chuyển đủ nhánh/ô/mũi nối thành text có nhãn biên tập. Các nút nhìn toàn trang gồm 内閣, 安全保障会議, 内閣官房, 内閣法制局, 人事院, 会計検査院, hàng loạt 省・庁; không suy thêm quan hệ từ kiến thức ngoài PDF. p102–138 pending.
- Worker mới kiểm claim/status/hash thật rồi claim token mới. Bảo toàn p1–100, đọc p101 chậm chắc từng cột và source→MD→source, sau đó đi từng trang. Với chỗ scan không rõ, ghi needs_review cụ thể thay vì đoán. Root giữ QA/Git/acceptance.

---

# Bàn giao trước — WIP p1–94; p95 đã render

- Cập nhật: 2026-11-11 JST; worker `production_book_11_root_cont3`, `gpt-6-sol/high`, điều phối trực tiếp `/root`.
- Book `01-yuukibui-b12c61270c7b`, 138 physical pages; nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`; SHA-256 nguồn `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt này chuyển mới **p87–94 (8 trang)**; mở full render mỗi trang, direct4/crops trên dưới; p87 direct8 từng cột bảng/map/legend + direct16 hàng 兵庫/神戸, p93 xoay landscape direct4 và mở hai crop. So hai chiều với MD rồi verify từng trang. p95 đã render/mở full preview nhưng chưa draft.
- Sau reconcile/build: **94/138 verified (p1–94), 1 rendered (p95), 43 pending (p96–138), 0 draft/needs_review/invalid, 0 issue/error**, `build_current=true`; partial, chưa complete/accepted. `book.md`/`search.jsonl` chỉ gồm p1–94. SHA-256 `build.json`: `6879b11287fb121f309e7f2c0021df58e9dadd24df171e1a40ba1c0417da39d5`.
- Token lượt này `book11-root87-20261111-d719`; sẽ release sạch sau handoff. Không Git, không sửa ngoài corpus/cache sách được giao.

## Nội dung mới và điểm nguồn

- p87 trang in74 là bảng `都道府県名（ⓐ）と県庁所在地名（ⓑ）`, **47 hàng** trong ba cụm cột nguồn, số 1–47 duy nhất; bản đồ đã chuyển đủ quan hệ A–H, số tỉnh, chấm 県庁所在地 và bốn biển sang text có nhãn biên tập, không hình. Giữ dữ kiện thời sách `13 埼玉／浦和`, không đổi thành Saitama; crop direct16 cho thấy ruby của 兵庫 là `庫＝こ` như in. Bản đồ số47沖縄 tách rời; p88 sang bài mới.
- p88–92 第十三課 `表現、やり方を聞く`: p88 談話型 4 lượt/6 blanks; p89 本文会話 hai đoạn, đoạn2 tiếp qua p90 ba lượt. p90 類話 `お返し` và bắt đầu 語句 1–2; p91 語句3–8; p92 語句9–13, rồi kết bài. Giữ `山本課長` khác `山崎`, notes 目上, ellipsis, dấu `/` lựa chọn và emphasis ngữ pháp theo từng lần nguồn.
- p93 trang in80 là `会社組織図（一例）` nằm ngang trên PDF, xoay crop để đọc; chuyển mọi ô và quan hệ nhánh của `本社`/`役職名`, 10 bộ phận, vai trò đại diện/phó, khung 管理職 thành text có nhãn biên tập. p94 mở 第十四課 `初対面の人と` với hai mẫu 談話型, 7+4 blanks, các slash lựa chọn và ruby. Không issue nguồn trong p87–94.
- p1–86 verified cũ giữ nguyên, gồm root QA sửa p75 ruby `決＝けっ`; không sửa lịch sử.

## Tiếp tục ngay

- **Physical p95 (trang in82)** là trang đầu chưa chép: đã ledger render scale2 và mở full preview. `《本文会話》` / `社長に紹介される`, nhân vật 課長・社長・ジョーンズ (研修生イギリスから), hội thoại dài mở đầu `社長、ご紹介させていただきます。...`. Phải mở direct4 trên/dưới để chép chính xác 14+ lượt/ruby/marginal 1,5,10,15,20,25. p96–138 pending.
- Worker tiếp theo kiểm source/status/release/claim thật rồi claim token mới; bảo toàn p1–94, tiếp tục từng trang full/crop hai chiều, exact occurrence/span ruby/bold, `b001` và checkpoint. Với vùng không rõ thật dùng `needs_review` cụ thể và đi trang khác. Root giữ QA/Git/acceptance.

---

# Bàn giao trước — WIP p1–86; p87 đã render

- Cập nhật: 2026-11-11 JST; worker `production_book_11_root_cont2`, `gpt-6-sol/high`, điều phối trực tiếp `/root`.
- Book `01-yuukibui-b12c61270c7b`, 138 physical pages; nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`; SHA-256 nguồn `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt này chuyển mới **p65–86 (22 trang)**, mỗi trang đã mở full scale2 và direct4 trên/dưới, so hai chiều với Markdown, verify từng trang. p75, p79, p80, p86 thêm direct8 để phân biệt kana hoặc bold. Đã reconcile/build.
- Trạng thái sau build: **86/138 verified (p1–86), 1 rendered (p87), 51 pending (p88–138), 0 draft/needs_review/invalid, 0 issue/error**, `build_current=true`; sách còn partial, chưa complete/accepted. `book.md`/`search.jsonl` chỉ gồm p1–86. SHA-256 `build.json`: `868824b19115f698a34c2db71e3d81feb8d35a78e90c7badec38b38db3a6d7b2`.
- p1–64 đã verified trước, không thay nội dung. Sửa riêng p75 theo QA root: ruby `決＝けっ` trong `決算月`, crop trực tiếp scale8 thấy っ nhỏ; ghi/verify lại. Token lượt này `book11-root65-20261111-a91e`, sẽ release sạch sau handoff. Không Git, không sửa tools/config/sách khác. Ảnh/scratch ở cache riêng.

## Nội dung và điểm nguồn cần giữ ở p65–86

- p65–67 kết 第九課: `レストランの予約` 14 lượt; `六日` đọc nguồn `六＝むい；日＝か`; số khách 10, 5000円, 座敷, đồ uống tính riêng. Sau đó 語句 1–7, bold đúng từng occurrence.
- p68–75 第十課 `お土産`: p69 bản thoại 12 lượt giữ `五日間＝いつかかん`; p70 類話 1–2 có ký hiệu dòng lề phải `1…` bị cắt scan, chỉ ghi phần nhìn thấy; p71 類話3 rồi 語句. p72 mẫu8 bold chỉ `(さ)` và `よ` ở cuối theo crop. p75 là bảng `年中行事` đủ 12 tháng, ô trống, các ngày lễ lịch sử y nguồn. Tháng 7 có **ba dòng riêng** `7日 七夕`, `中元`, `お盆`, không thêm `お` vào 中元. Tháng 3 `決＝けっ` đã sửa bằng direct8; giữ `23日ごろ`.
- p76–81 第十一課 `連絡`: p76 khung 談話型 và ô trống; p77 本文 `出先から会社に連絡する` 10 lượt; p78 hai 類話 (trễ hẹn và 欠勤); p79–81 語句 1–12, mục9 nối p80→81. p80 ruby in dưới `今週中` là `こんしゅうちゅう` (khác đọc thông dụng), đã xác nhận direct8; đừng sửa thành じゅう.
- p82–86 mở 第十二課 `おわび`: p82 khung 談話型; p83 `日にちをまちがえる` 11 lượt với `四日＝よっか`/`八日＝ようか`; p84 類話1 và đầu 類話2 (`借りた物をなくした時`), p85 kết hai lượt rồi 語句 1–4, p86 語句 5–9. p86 crop direct8 xác nhận `二日酔＝ふつかよい` và bold ví dụ `飲ま**なければよかった**`.
- Đã giữ mọi số lề/trang in, watermark, furigana nguồn, vai, ví dụ, dấu câu, blanks và bold nguồn trong p65–86. Mỗi trang có anchor `b001` trước đơn vị nội dung đầu. Không có vùng scan cần `needs_review` trong p65–86.

## Tiếp tục ngay

- **Physical p87 (trang in74) là trang đầu tiên chưa chép**: ledger đã render scale2; file cache `p0087.png` đã mở preview. Đây là bản đồ Nhật và bảng đủ 47 `都道府県名 (a) と県庁所在地名 (b)`, vùng A–H, số trên bản đồ và các nhãn biển; cần direct4/crops và chuyển hết quan hệ bảng/bản đồ thành text/table, không nhúng ảnh. p87 hiện **rendered**, chưa draft/verify; p88–138 pending. Đừng bỏ bảng/bản đồ chỉ vì khó.
- Worker tiếp theo đọc rules/core/HANDOFF, kiểm source hash/status/claim thật, claim token mới sau release. Giữ verified p1–86. Tiếp tục từng trang full/crop thực, đối chiếu hai chiều, exact ruby/emphasis, b001 và checkpoint riêng. Trường hợp bất định thật thì `needs_review` cụ thể rồi đi trang khác.
- Root giữ QA/Git/commit/acceptance. Handoff này chỉ là checkpoint worker, không có quyền xác nhận hoàn tất sách.

---

# Lịch sử checkpoint p1–64

# Bàn giao mới nhất book11 — WIP p1–64

- Cập nhật: 2026-11-11T01:37:58.120054+00:00; worker `production_book_11_sol_cont_root45`, `gpt-6-sol/high`, điều phối trực tiếp `/root`.
- Book `01-yuukibui-b12c61270c7b`, 138 physical pages; nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`.
- SHA-256 nguồn giữ nguyên: `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt này chuyển mới **p45–64 (20 trang)**. Mỗi trang đã mở full render scale2, direct4 trên/dưới, mở lại sau draft để đối chiếu nguồn→Markdown và Markdown→nguồn; verify riêng từng trang bằng CLI. p49 thêm direct8 chữ `斎` để phân biệt biến thể trong `斎藤`.
- Sau reconcile/build: **64/138 verified (p1–64), 74 pending (p65–138), 0 rendered/draft/needs_review/invalid, 0 issue/error**, `build_current=true`. Sách partial, chưa completed/accepted. `book.md` và `search.jsonl` chỉ gồm p1–64.
- SHA-256 `build.json`: `4335cf66a65f9d8913023e5e528916f3f262cf9fd438938636ddc97a2546e698`.
- p1–44 giữ nguyên; p45–64 đều có `b001` duy nhất trước first substantive unit; typography ngữ pháp theo từng occurrence, không bold mù mọi chuỗi trùng. Kiểm cấu trúc anchors/text-only cục bộ đã qua; đây không thay QA ngữ nghĩa độc lập của root.
- Token dùng lượt này: `book11-root45-20261111-c542`; release sạch bằng CLI sau khi ghi handoff. Không Git, không sửa tools/config/roster/main HANDOFF hoặc sách khác. Ảnh/scratch chỉ cache riêng.

## Nội dung và điểm nguồn cần giữ

- p45–48 kết 第六課: các hội thoại転勤/五年ぶり/近所/引っ越し/おくやみ rồi語句; giữ giới thiệu chuyển nhà lặp qua p45→46, `405号室`, `八十一＝はちじゅういち` và typography từng mẫu.
- p49 `日本人に多いみょう字`: 57 họ trong ba dải20/20/17 dòng, giữ7 ô cách đọc trống (安部/荒井/伊東/大田/菊池/酒井/武内). Chữ nguồn là `斎藤`, không đổi `齋藤`; các dòng `なかじま＝中島`, `やまざき＝山崎`, `わたなべ＝渡辺` giữ nguồn.
- p50–55 第七課 `社外からかかって来た電話`: header第七課 ruby `だいななか`. p50 khung có14 ô trống; note review đã sửa lỗi đếm13 thành14, không đổi text nguồn. Nhãn vai `大`/`林`, `交`/`換` được ruby riêng theo cách in; số `391の5231`/`内線321` giữ hai lần p52. p53 `後ほど` có `後＝のち`; p54 tên `おおきた（大来）` khác nghe nhầm `おきた`, giữ rõ. `私＝わたくし` trong hội thoại p52 nhưng `私＝わたし` trong ví dụ p54.
- p56–61 第八課 `社員旅行`: 第八課 ruby `だいはっか`, p56 10lượt/10ô trống. p57 giữ `土＝ど`/`日＝にち`, `一曲＝いっきょく`, `参加するでしょ`, `歌わされたり`/`やらされたり`. p58 form `保養所利用申込書` chuyển đủ text (昭和/ngày/nơi/課/tên/số người/bữa ăn/phí); `利用月日＝りようがっぴ`, `小人＝こども`, `有/無＝う/む` ở nhãn nhưng `あり/なし` ở lựa chọn, phí `2000円`/`1000円`. p61 `今日中＝きょうじゅう` khác `今週中＝こんしゅうちゅう` như ruby in; không đồng nhất hóa.
- p62–64 mở 第九課 `予約`: ruby `だいきゅうか`. p63 hội thoại9lượt `旅行社で`, số `7月28日` giữ ASCII, ruby chỉ `月＝がつ`/`日＝にち`, `午前九時＝ごぜん/くじ`; kết ở `自由席で並ぶしかないですね。`, p64 chuyển類話, không nối giả. p64 `早目＝はやめ`, S席/A席, ngày15/16/9月27/27/29, lời cuối B và chú thích nhận tên/điện thoại đủ.
- Không phát hiện vùng scan thực sự không đọc được trong p45–64; không tạo issue suy đoán. Trang form/bảng đã chuyển đầy đủ text, không phụ thuộc ảnh.

## Tiếp tục ngay

- **Trang mới tiếp theo: physical p65–138**. p65 đã mở preview nguồn trong cache `preview0065-root45.png` chỉ để kiểm nối: mở `《応用会話》` / `レストランの予約`, nhân vật中村 vàレストラン. **p65 vẫn pending, chưa ledger render/record/verify**.
- Đọc current rules và own HANDOFF, kiểm status/claim thật rồi claim token mới. Giữ verified1–64. Root có thể followup worker ngay, không cần chờ user. Mỗi trang mới vẫn full/crop thật, đối chiếu hai chiều và checkpoint riêng, typography đúng occurrence và b001 đầu khối.
- Root giữ Git/QA. Mẫu QA hữu ích trong batch: p49 bảng họ, p50 ô trống, p53 ruby後, p58 form, p60 grammar/emphasis, p61 ruby中, p64 dates/roles.

---

## Lịch sử checkpoint p1–44

# Bàn giao mới nhất book11 — WIP p1–44, QA anchors/emphasis đã sửa

- Cập nhật: 2026-11-11T00:31:16.656522+00:00; worker `production_book_11_sol_cont_root`, `gpt-6-sol/high`, điều phối trực tiếp `/root` theo thay đổi của user.
- Book `01-yuukibui-b12c61270c7b`, 138 physical pages; nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`.
- SHA-256 nguồn giữ nguyên: `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt này chuyển đổi mới **p36–44 (9 trang)**, mở toàn trang và direct4 mỗi trang, đối chiếu hai chiều/ruby/source typography rồi verified từng trang. p37 thêm direct8 để phân biệt `阿佐ヶ谷` và `七分＝ななふん`.
- Sau reconcile/build: **44/138 verified (p1–44), 94 pending (p45–138), 0 rendered/draft/needs_review/invalid, 0 issue/error**, `build_current=true`. Sách partial, chưa completed/accepted. `book.md`/`search.jsonl` chỉ gồm p1–44.
- SHA-256 `build.json`: `6602a768ccedec27cf4833e6ba6b8e3ea2ec0dffe1f4895771bac5ca67b7800c`.

## QA root đã xử lý trong lượt này

- Root mở p16/p25/p35, thấy nguyên văn/ruby phù hợp trong mẫu nhưng thiếu emphasis ngữ pháp và anchor đầu. Worker đã báo phạm vi trước khi sửa.
- Kiểm file thật xác nhận thiếu `b001` đúng toàn **p16–36**. Đã thêm anchor trước nội dung nguồn đầu cho cả 21 trang, giữ nguyên mọi anchor `b002+`, mở lại ảnh từng trang và fresh verify. **p16–44 đều có b001 duy nhất**. p37–38 vốn có b001 do CLI chèn; p39+ đặt rõ ngay từ draft.
- Đã rà và khôi phục emphasis theo vị trí nguồn ở **p16–17, p22–23, p27–29, p33–35**; thêm emphasis tên sách in đậm p26/p27/p29. Không áp dụng tất cả từ trùng: đã kiểm riêng các câu nhắc lại không đậm ở p17 mục8, p27 mục1/4, p28 mục8, p34 mục10, p35 mục15A. P39–41 được giữ emphasis ngữ pháp ngay trong lượt chuyển đổi mới.
- Script so sánh từng trang p16–36 xác nhận bỏ duy nhất Markdown `**` thì nội dung khớp bản sửa anchor-only; không đổi một chữ/ruby/dấu nguồn nào trong đợt QA này. Fresh evidence giữ review nguồn trước và ghi rõ việc sửa anchors/emphasis.
- Các trang p18–21/p24–25/p30–32/p36 chỉ thêm anchor; p26 thêm cả emphasis hai tên sách. P1–15 không sửa.
- Không còn audit emphasis/anchor p16–36 đang treo trong phạm vi đã giao; root vẫn cần QA độc lập và acceptance toàn sách sau đủ nguồn. Các ghi chú audit pending trong lịch sử, nếu có, đã được mục mới nhất này thay thế.

## Phạm vi mới và điểm cần giữ

- p36 mở 第五課 道を聞く / 談話型; p37 本文会話 hỏi đường tới nhà課長; p38 類話 待ち合わせ; p39–41 語句; p42 mở 第六課 あいさつ; p43–44 本文会話 朝/夕方 và đầu 類話1/2.
- p37 đọc `歩いて七分ぐらいかな` và ruby `七分＝ななふん`, không phải 十分. `家` có ruby `いえ`/`うち` khác nhau từng lần; `二階建＝にかいだ` chỉ span chữ Hán.
- p38 giữ `12番線` số ASCII và ruby chỉ `番線＝ばんせん`, `十二時＝じゅうにじ`, `総武線`, `黄色`; không cập nhật dữ kiện đường sắt lịch sử theo hiện tại.
- p39→40 nối mẫu6(1)→6(2); p40→41 nối11b(1)→11b(2), rồi11c. Các mục `は/でしたね`, `というのは/ですね`, `というと/ですね` tách đúng theo nguồn.
- p42 第六課 in ruby `だいろっか`; giữ `あまりお役に立てませんで…` trong khung. P43 朝9 lượt/夕方5 lượt, giữ đoạn tiếp trong cùng vai 松下, không chèn nhãn mới.
- p43→44 nối đoạn hai người rời cơ quan, sau đó caption `駅へ行くとちゅうで`. P44 phần 国へ帰る có `君＝きみ`, khác `君＝くん` ở lời gọi ラーマン君; giữ `あまりお役に立てなかったろう`.
- p44 cuối bắt đầu 類話2 転勤 với một lượt A chúcご栄転/メキシコ. Đã mở preview p45 để kiểm nối: p45 đầu B `うん、二年ばかり行ってくることになってね。...` tiếp chính hội thoại này. **p45 chưa record/render ledger/verify**.

## Tiếp tục

- **Trang mới tiếp theo: physical p45–138**. Đọc rules/core/HANDOFF, kiểm status/claim thật, claim token mới sau release sạch. Giữ typography có ý nghĩa và b001 trước first substantive unit ngay từ draft; chỉ bold nơi nguồn thực sự in, không replace mọi occurrence cùng chuỗi.
- Worker không dùng Git, không sửa tools/config/roster/main production HANDOFF/sách khác. Root sở hữu Git/QA. Render/crop/scratch chỉ trong cache riêng, không thuộc output text.

---

## Lịch sử checkpoint p1–35

# Bàn giao mới nhất book11 — WIP p1–35

- Cập nhật: 2026-11-11T00:12:20.526936+00:00 (2026-11-11 JST).
- Worker tiếp: `production_book_11_sol_cont`, `gpt-6-sol/high`, skill 0.2.4; token đã dùng `book11-cont-20261111-d73b`.
- Book ID: `01-yuukibui-b12c61270c7b`. Nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`.
- SHA-256 nguồn: `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- Lượt tiếp này mở ảnh thật toàn trang và crop direct4 từng physical **p16–35**, chép và đối chiếu hai chiều rồi verify từng trang: **20 trang mới verified**. p1–15 giữ nguyên.
- Trạng thái thật sau reconcile/build: **35/138 verified (p1–35), 103 pending (p36–138), 0 rendered, 0 draft, 0 needs_review, 0 invalid, 0 issue**; mọi page errors đều rỗng. `build_current=true`; partial, chưa completed/accepted.
- Build SHA-256 `build.json`: `be2fefab113daf9fa731d3ad0a7efda2e08a0811233a2602f9d7785c33045b0b`. `book.md`/`search.jsonl` hiện chứa đúng các trang verified p1–35.

## Phạm vi và điểm nguồn cần giữ

- p16–17 kết bài1 語句の使い方; p18–23 bài2 わからない日本語を聞く; p24–29 bài3 依頼; p30–35 bài4 断り. Đọc trực tiếp ảnh, không dùng OCR/text layer để chép.
- Mỗi page checkpoint có source/render/Markdown hashes và review cụ thể; render ledger scale2, crop direct4 trên/dưới mỗi trang, p29 thêm direct8 để phân biệt ruby nhỏ. Cache/scratch chỉ trong `kaiwa_skill/.cache/renders/01-yuukibui-b12c61270c7b/`, không thuộc output.
- p17 8(1) in `交通の便利なのに`, giữ nguyên; p20 in `同音異義語`, khác `同音意義語` ở mục lục p12, không đồng nhất hóa.
- p21 in `漢字の言葉は、ふつう訓読みと訓読み、音読みと音読みです。` và `メジョウ`/`メウエ`, giữ nguyên sau crop. Hai khung chữ là `目上`/`渡部`, đã chuyển text đúng vị trí.
- p25 và p28 `花びん` có ruby nguồn `花＝か`, giữ theo chữ in; p29 direct8 xác nhận `二十分＝にじっぷん`, các lần xuất hiện p31/p34 cũng giữ ruby in này.
- p26/p27/p29 giữ tên `中根千枝` và tên sách `『タテ社会の人間関係』`/`『適応の条件』`, giọng nam/nữ/teinei khác nhau, không tự sửa thống nhất.
- p27 in `買物`; p31/p34 in `手が放せない` (放), không thay bằng 離. p33 5(1) là `お引き受けするんですが`, khác `お引き受けするのですが` trong bài thoại p31.
- p34 mẫu8 là `（時間）する`, không sửa mẫu thành したら dù ví dụ dùng したら. p35 `横文字`, `野田産業`, câu cuối phần15(2) có dấu lửng; giữ nguyên.
- Các số lề, tên bài ở đầu trang, chân trang in3–22, watermark `JLPT Mogi / Yuuki Bùi`, ô trống và ref p/l được đối chiếu từng trang. Không hình mang nghĩa mới ngoài các khung chữ; không nhúng ảnh.

## Ranh trang và tiếp tục

- p15→16: lời tự giới thiệu kết trọn, chuyển 語句. p16→17 tiếp mục7. p18→19 chuyển khung sang bài thoại. p19→20→21 tiếp 類話1→2–5→6–8; p22→23 tiếp 語句5→6–8.
- p25→26: hội thoại2 電話をかけてもらう tiếp bằng ボナン `そうですか。お手数ですが…`, sau hai lượt mới sang 類話; không tạo lời kết p25.
- p26→27: 類話3 tiếp bản 女性と女性; sau bốn lượt chuyển 語句. p27→28: mẫu5 chỉ ví dụ(1) ở p27, ví dụ(2) đứng đầu p28; p28→29 tiếp mẫu11–13.
- p31→32 tiếp 類話1→2–4. p33→34→35 tiếp 語句1–5→6–10→11–15. Lượt B dài trong p32 mục4 giữ hai đoạn cùng một người nói.
- Đã mở preview trực tiếp p36 để kiểm ranh cuối: p36 bắt đầu `第五課 道を聞く` (trang in23), không câu bị cắt cần nối từ p35. Preview p36 **chưa record/render ledger/verify**.
- **Tiếp từ physical p36–138** sau kiểm claim/status thật và claim token mới. Không sửa p1–35 verified nếu không có finding cụ thể. Chưa có source blocker trong p1–35.
- Coordinator giữ quyền QA mẫu/serial Git; worker này không dùng Git, không sửa tools/config/roster/main production HANDOFF hoặc sách khác.

---

## Lịch sử bàn giao trước lượt tiếp

# Bàn giao book11 — WIP

- Cập nhật: 2026-11-10T23:52Z (2026-11-11 JST).
- Worker: `production_book_11_sol`, model `gpt-6-sol/high`, skill 0.2.4.
- Book ID mặc định: `01-yuukibui-b12c61270c7b`.
- Nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`.
- SHA-256 nguồn: `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- 138 trang vật lý. Đã mở ảnh thật toàn trang và crop, chép/đối chiếu/verify **p1–15**. **15 verified, 123 pending (p16–138), 0 draft, 0 rendered, 0 needs_review, 0 invalid** tại checkpoint này. Không có source blocker đã biết trong phạm vi đã chuyển đổi.
- Đã reconcile và build partial; không phải completed/accepted. `book.md` và `search.jsonl` chỉ chứa p1–15. Sau release, CLI xác nhận `claim=null`, `build_current=true`, `issue_count=0`; build.json SHA-256 `059e1926a514632b8bbaa2b96995b6efbd907fdcaabd4b0259cc47a1828dc514`.

## Phạm vi và bằng chứng

- p1 bìa; p2 trang tên sách và dấu thư viện Trung `江苏工业学院图书馆 / 藏书章`; p3 xuất bản; p4 lời tựa Nhật; p5–6 đặc điểm/nội dung Nhật; p7 lời tựa Anh; p8–9 đặc điểm/nội dung Anh; p10–11 hướng dẫn; p12–13 mục lục; p14–15 bài1 tự giới thiệu.
- Mỗi page checkpoint có source/render/Markdown hashes và evidence cụ thể. Render chuẩn CLI scale2; đã mở crop phóng to hoặc direct PDF scale4/8 để kiểm chữ nhỏ. Cache và scratch trong `kaiwa_skill/.cache/renders/01-yuukibui-b12c61270c7b/` chỉ phục vụ đọc ảnh, không thuộc output và không commit.
- Không dùng OCR/text layer làm chứng cứ hoặc để tạo bản chép. Chữ Nhật/Anh/Trung và watermark `JLPT Mogi / Yuuki Bùi` đọc từ ảnh. Mọi hình có nghĩa trong phạm vi đã mô tả text; không nhúng ảnh.
- QA coordinator phát hiện kiểu chữ ngày ở p4: đã sửa `1987年５月` thành `1987年 5 月`, re-record và fresh verify. Cũng sửa chữ số mảnh ở p3 sang ASCII trong ngày/địa chỉ rồi fresh verify. Báo cáo QA coordinator nằm riêng, không ghi nhận là nghiệm thu toàn sách.

## Điểm cần giữ đúng theo nguồn

- p4 in `適確`, không đổi sang 適切; p6 in `話しの`, không sửa thành 話の.
- p6 chỉ lần `類話` đầu trong đoạn 一つの課 có furigana `るいわ`; không tự thêm ở lần lặp.
- p7 giữ ngắt từ `associat-` / `ing`; p8 `congratula-` / `tions`, `appro-` / `priate`, `drink-` / `ing`; p9 `Dis-` / `course`.
- p12 in `同音意義語`, không sửa thành 同音異義語; `5.6.漢字の発音` giữ số như in. Crop focused8 xác nhận `本人不在` có `ほんにん` / `ふざい`.
- p13 crop focused8 xác nhận 第十課 đọc `だいじっか`, 第二十課 đọc `だいにじっか`; không thay bằng dạng từ điển khác.
- p14 khung có ba chỗ trống, không điền. p15 tên in `ウイチャイ・プラモー`; tên vai trong Markdown được chú thích là nhãn biên tập từ dòng giới thiệu, nguồn không gắn nhãn vai cho đoạn phát biểu. Dòng `タイ人研修生` có ruby riêng `人＝じん` cùng `研修生＝けんしゅうせい`.
- Số trang in chuyển v (p6) sang vii (p7) đúng chuỗi PDF; không tạo trang vi.

## Nối trang và trang kế tiếp

- p5→6 nối bảng từ 第十五課 sang 第十六課; phần hướng dẫn sau bảng kết trọn câu tại p6.
- p8→9 nối bảng từ Lesson17 sang Lesson18; không câu bị cắt ở các hàng.
- p10→11 tiếp nội dung hướng dẫn: p11 bắt đầu `語句の使い方`, không lặp tiêu đề 本書の使い方 như nguồn.
- p12→13 nối mục lục từ 第八課 sang 第九課; p14 mở 第一課 bài tự giới thiệu.
- p14 là khung 談話型, p15 là 本文会話; không câu nối cần tự hoàn thành.
- p15 kết thúc `どうぞ、よろしくお願いいたします。`. Đã mở preview trực tiếp p16 để kiểm nối: p16 là `《語句の使い方》` và tham chiếu lại câu p2. Preview này chưa được record/render vào ledger; **trang cần chuyển đổi tiếp theo là physical PDF p16 (trang in3)**.

## Tiếp tục

Đọc AGENTS/core/skill/USAGE và handoff này, kiểm claim/status thật, claim bằng token mới. Tiếp tục p16–138, giữ nguyên các trang verified còn hợp lệ. Không sửa PDF nguồn, tools/config/roster hoặc Git index. Coordinator kiểm mẫu và commit tuần tự.


Xác nhận release lượt tiếp 2026-11-11T00:12:20.526936+00:00: CLI `claim=null`, `build_current=true`, 35 verified / 103 pending / 0 issue.


Release xác nhận 2026-11-11T00:31:16.656522+00:00: `claim=null`, `build_current=true`, 44 verified / 94 pending / 0 issue.

## QA cuối p11–14: bổ sung anchor đầu khối (2026-11-11)

- Worker `production_book_11_anchor_repair`, claim token `production_book_11_anchor_repair_20261111_01`; chỉ sửa bốn trang này. PDF nguồn `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`, SHA-256 `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`, không đổi. Không sửa ROOT_AUDIT hay trang khác.
- Đã mở ảnh gốc toàn trang p11, p12, p13, p14 và xác nhận vị trí khối đầu. Chỉ thêm `<a id="pNNNN-b001"></a>` cùng dòng trống ngay sau metadata, lần lượt trước `## 語句の使い方`, `## 目 次`, `第九課 予約 … 49`, `Chữ đầu trang (biên tập): 第一課`. Giữ nguyên mọi anchor `b002+`; không đổi chữ Nhật/ruby/spacing/emphasis hoặc nội dung khác.
- Bản Markdown trước sửa lưu trong `.cache/renders/01-yuukibui-b12c61270c7b/anchor-repair-original-p0011.md` đến `p0014.md`. Kiểm byte: xóa đúng anchor mới và hai LF trong từng trang sau sửa khôi phục nguyên byte trước sửa; SHA-256 cũ → mới:
  - p11 `104841eaf459dfc83c60f1769780a7ce72575ecd801bcd8503a83f2877d42408` → `8a35c9d59e8c227d11db4098c004c784289ffc3736aea0003cf717cbba08a902`.
  - p12 `073e77f73b4bf351d9a99413111b8d07720777c8b794ef3317fa19ed2c99caf0` → `36a3244059e1b42dc5513aff7642f660c80a6cae6c6acd2142e4ad4f74491b1c`.
  - p13 `b96b841f03801cb29671c572782f8f6682c069380585e44897b2bca7b434126d` → `74f46f1d31fc5282d03a8f5e04a1ffbac6469085c157b9ad2f4e8d5d5c5fb23b`.
  - p14 `24c9b505a18fe143da4bd1e701e305fb90b299c498f9c6f13238a1afcae2d721` → `8f3ee0350f022b6358246eef60c73fec970baf1b8a451b814f2cdb2422e13c4f`.
- Hash ảnh render p11–14 không đổi, lần lượt `e13a8a04bebac25eedf94cb6717d4f1b0d3859c6addd26c5a601ca4e24b9eaa8`, `f48ccff20747747a754d8fac74eb8c1c6789ba3f0be78ede58003369a2386bd5`, `ad359ffca47b81d4c23b9e256ea7acb42fd3e3ee3ce934e90d5dab80a5489ee5`, `612a0ef8a0d88cd881d2ea61253aed73dff9fcee794f27837864bd0cb1542b80`. Không render lại.
- CLI đã record và reverify từng trang với evidence riêng, sau đó reconcile/build: 138/138 verified, 0 issue, build complete. Review lượt này chỉ kiểm vị trí anchor, delta byte và hash nguồn/render. Evidence của worker trước ghi đã đối chiếu toàn trang; lượt này không đọc lại từng kana. Root cần readback và quyết định acceptance/commit.
