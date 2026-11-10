# Production — tiếp tục toàn bộ hàng đợi

Người dùng đã yêu cầu chuyển đổi tất cả PDF. Gate pilot PASS nằm tại `kaiwa_skill/pilot/REVIEW.md`; skill hiện tại 0.2.4 (điều phối và mọi tác nhân sản xuất dùng Sol/high; quy tắc nội dung 0.2.3 giữ nguyên), output chỉ text. Danh sách nguồn và phân công chuẩn: `roster.json`; bản dễ đọc: `ROSTER.txt`. Đường dẫn nguồn trong roster tương đối từ `kaiwa_skill/`; đường dẫn corpus tương đối từ repo.

Điều phối `gpt-6-sol/high`; chỉ hai worker `gpt-6-sol/high` cùng lúc, mỗi worker đúng một PDF. Chạy các lệnh từ gốc repo hiện tại. Root chat không dùng Git; coordinator chịu trách nhiệm commit tuần tự theo sách. Không sửa `bunpou_skill/` hoặc PDF nguồn.

## Tiếp tục

1. Kiểm tra tác nhân đang sống trước khi giao lại sách. Một claim không tự hết hạn. Không thu hồi khi worker cũ vẫn đang ghi.
2. Đọc `AGENTS.md`, hai skill ingest/worker, core docs, `tools/USAGE.md`, rồi chạy `status-all`. Roster là snapshot; cần refresh số đếm/hash từ file thật.
3. Dùng `python kaiwa_skill/production/refresh_roster.py` để cập nhật roster. Script chỉ đọc trạng thái corpus và ghi snapshot; không chạy worker, không xác nhận nội dung.
4. Tiếp tục sách có `worker_state: running` sau khi xác nhận worker còn sống, hoặc xử lý claim cũ/reconcile đúng CLI khi đã dừng. Đọc `corpus/BOOK_ID/HANDOFF.md` nếu có.
5. Lấy sách queued nhỏ nhất theo `queue_order` khi có slot trống. Spawn `gpt-6-sol`, `reasoning_effort=high`, `fork_turns=none`; prompt yêu cầu mở ảnh thật từng trang, mọi ngôn ngữ/bảng/ghi chú/bìa/trắng, checkpoint từng trang, text only. Ghi agent ID thực bằng `refresh_roster.py --assign BOOK_ID AGENT_ID`.
6. Worker chỉ gọi trang verified sau xem ảnh và đối chiếu. Không dùng OCR/text layer làm chứng cứ đã xem ảnh. Những chỗ không đọc được phải `needs_review`, không đoán. Tiếp tục sách độc lập khi một sách cần xử lý lỗi.
7. Khi worker hoàn thành và release: chạy build/status, kiểm tất cả trang lỗi và chọn mẫu theo bố cục/đầu-cuối unit. Ghi báo cáo nghiệm thu với hash, phạm vi mẫu và giới hạn. Chỉ nhận sách khi verified bằng toàn bộ trang, không lỗi, build hiện tại và kiểm mẫu đạt. Coverage máy không phải nghiệm thu.
8. Commit cụ thể từng output đã nghiệm thu; không stage ảnh cache/lock/scratch. Handoff dài hạn chỉ commit `WIP`, ghi rõ số trang thực và phần chưa hoàn tất. Không push.

Python cần có `pypdfium2`, `Pillow` và `pypdf`. Xác định runtime Python của môi trường hiện tại; có thể dùng runtime bundled của Codex. Không giả định đường dẫn cài đặt giữa các máy hoặc các phiên bản.

## Trạng thái đầu đợt

Inventory/status đọc lại ngày 2026-11-10: 30 PDF, 4597 trang vật lý; 4 verified ở pilot điện thoại, 4593 chưa verified. Không suy ra tiến độ hiện tại từ các số đầu đợt này; đọc roster mới hoặc CLI.

- Roster commit: `390dc38`.
- Snapshot assignments + công cụ refresh: `d34ee95`.
- Slot 1 bắt đầu `1160-t-v-ng-mimikara-n2-6d226fd8769f` (8 trang).
- Slot 2 bắt đầu `880-t-v-ng-mimikara-n3-minato-b3140fae78af` (47 trang).

Không có daemon hoặc tiến trình nền được bảo đảm tiếp tục sau khi toàn bộ tác nhân dừng. Tệp này bảo toàn quyền tiếp tục và hàng đợi, không chứng minh công việc đang chạy.

## Sách đã nghiệm thu

- `1160-t-v-ng-mimikara-n2-6d226fd8769f`: 8/8 trang, coordinator kiểm cả tám, ACCEPTED; commit output `5379b10`. Báo cáo riêng và hash-bound acceptance nằm trong corpus sách. Audit phân biệt lỗi ranh giới bảng đã sửa với nhận định thiếu header đã rút sau crop đối chứng.
- Slot được cấp tiếp cho `1170-t-v-ng-mimikara-n1-e1d2f2dffd69` (70 trang), agent `production_book_03`. Sách N3 tiếp tục ở `production_book_02`. Trạng thái số trang mới nhất lấy từ roster/CLI.

## Cập nhật sau nghiệm thu N3

- `880-t-v-ng-mimikara-n3-minato-b3140fae78af`: ACCEPTED 47/47 trang, đủ 880 mục; commit output `ea221b1`. Coordinator đã rà độc lập cả hai cột tiếng Việt toàn bộ 47 trang sau lỗi dấu lặp lại; tiếng Nhật/bố cục lấy mẫu 10 trang. Báo cáo và sổ QA trong corpus ghi rõ lỗi đã sửa, các nhận định sai đã rút và giới hạn.
- Slot này chuyển sang `namachuukei-chuujoukyuu-f08dd9302ee6`, nguồn `book/Shadowing/Namachuukei Chuujoukyuu.pdf` (từ `kaiwa_skill/`), 89 trang; agent `production_book_04`, gpt-6-sol/high.
- N1 vẫn ở `production_book_03`, chưa nghiệm thu. Tiếp tục toàn bộ hàng đợi; không suy ra tác nhân còn chạy chỉ từ file này, kiểm live agents và status thật khi resume.

## Cập nhật sau nghiệm thu N1

- `1170-t-v-ng-mimikara-n1-e1d2f2dffd69`: ACCEPTED 70/70 trang, đủ 1170 mục; commit output `992a210`. Coordinator kiểm toàn bảng 14 trang và các hàng gắn cờ; worker rà rộng các trang liên quan sau bốn lỗi ký tự/dấu. Báo cáo phân biệt lỗi chuyển đổi với những cách in khác thường thật sự của nguồn. Claim đã release.
- Slot chuyển sang `namachuukei-shochuukyuu-1-53b5b51998a3`, nguồn `book/Shadowing/Namachuukei Shochuukyuu 1.pdf` (từ `kaiwa_skill/`), 91 trang; agent `production_book_05`, gpt-6-sol/high.
- `production_book_04` tiếp tục sách 89 trang. Sách kế tiếp chưa giao: `85-21a2cb6f3fef`, 93 trang. Tiếp tục theo queue_order trong roster.

## Khởi động lại sau gián đoạn — 2026-11-10

- Coordinator mới: `/root/production_resume` (gpt-6-astra/high). Live inventory trước spawn chỉ có root và coordinator mới; tất cả tác nhân phiên cũ đã dừng. Hai claim cũ được thu hồi bằng CLI `recover --kind claim --expected-token … --confirm-writer-stopped`, lưu audit nguyên trạng. Không có write lock tồn tại.
- Snapshot hash thực trước resume: 30 PDF / 4597 trang; 211 verified, 3 rendered, 4383 pending, 0 issues. Ba Mimikara accepted và build hiện tại nguyên vẹn.
- `namachuukei-chuujoukyuu-f08dd9302ee6`: giữ p0001–p0042 verified; resume p0043–p0089. Worker mới `/root/production_resume/production_book_04_resume` (gpt-6-sol/high).
- `namachuukei-shochuukyuu-1-53b5b51998a3`: giữ p0001–p0040 verified; resume p0041–p0091. Worker mới `/root/production_resume/production_book_05_resume` (gpt-6-sol/high).
- Scratch/bản nháp cũ giữ để phục hồi nhưng không được coi là verified. Hai worker đọc lại status, nhận claim mới, reconcile, mở ảnh từng trang và checkpoint từng trang. Chưa nghiệm thu hai sách này.
- Tiếp tục toàn bộ hàng đợi sau hai sách đang dở; sách tiếp theo `85-21a2cb6f3fef`. Root không thao tác Git; coordinator commit tuần tự từng sách sau QA.

## Bổ sung quy trình sau QA resume — skill 0.2.3

- Commit skill `0b4b6ad`: cụ thể hóa hai lượt ảnh → Markdown và Markdown → ảnh trước verify, crop để kiểm từng kana nhỏ/cuối chuỗi và occurrence/span. Chỉ sửa hướng dẫn; không đổi CLI/schema hay quy tắc bảo toàn nguyên văn, không sửa nội dung pilot hoặc ba sách accepted. `git diff --check` đạt.
- Đã gửi quy trình mới cho cả hai worker resume; tiếp tục toàn queue. Book05 đã rà mở rộng ruby p24–40 và41–55, sửa/reverify trang có sai khác; coordinator readback các sửa đổi và lưu hash trong COORDINATOR_AUDIT.json. Không suy diễn lượt rà của worker thành kiểm độc lập100% của coordinator.
- Mốc worker gần nhất: book04 p65/89; book05 p56/91 và đang p57. Đây là snapshot, dùng CLI/status để lấy tiến độ hiện tại.

## Nghiệm thu sách 04 và chuyển slot — 2026-11-10

- `namachuukei-chuujoukyuu-f08dd9302ee6`: ACCEPTED 89/89, 0 issue, build hiện tại, claim đã release. Commit output `d8087de`. Coordinator kiểm nguồn/Markdown 58 trang, mọi đầu/cuối unit và các nhóm mở rộng; báo cáo, sổ QA và acceptance hash-bound trong corpus ghi rõ giới hạn. Không còn lỗi đã biết trong phạm vi kiểm.
- Staged 187 file text đúng byte trên đĩa; không có image/cache/claim/lock/scratch/source. Kiểm whitespace với CR-at-EOL và bỏ cảnh báo blank-at-EOF của book.md sinh tự động; không normalize nội dung verified để tránh đổi hash. Validator/hash/build đều đạt.
- Slot mới: `/root/production_resume/production_book_06`, gpt-6-sol/high, `85-21a2cb6f3fef`, nguồn `book/Kaiwa/外国人のための日本語敬語の使い方-基本表現85.pdf`, 93 trang. Worker đọc trạng thái thật rồi init/claim; coordinator tiếp tục QA và commit tuần tự.
- Sách05 vẫn chạy ở `/root/production_resume/production_book_05_resume`, mốc80/91 verified; coordinator đã so nguồn toàn p1–77, tiếp tục mở rộng đến hết sách sau lỗi furigana occurrence lặp. Chưa nghiệm thu05. Dùng CLI/roster mới lấy số hiện tại.

## Nghiệm thu sách 05 và chuyển slot — 2026-11-10

- `namachuukei-shochuukyuu-1-53b5b51998a3`: ACCEPTED 91/91, 0 issue, build hiện tại và claim đã release. Commit output `13fd252`. Coordinator đã mở ảnh nguồn và đối chiếu toàn bộ 91 trang sau lỗi occurrence ruby tái diễn; mọi sai khác đã biết đã sửa/reverify/readback, hash ledger khớp toàn sách. Báo cáo/acceptance hash-bound trong corpus.
- 192 file text staged đúng byte, không ảnh/cache/claim/lock/scratch. Whitespace còn lại là CRLF bảo toàn byte, blank cuối book sinh tự động và hai space Markdown hard-break ở colophon p91/bản ghép; giữ nguyên bằng chứng đã verified. Scratch cũ của05 vẫn tồn tại ngoài commit.
- Slot mới `/root/production_resume/production_book_07`, gpt-6-sol/high, `669041168-4f47df1cc97a`, nguồn `book/Kaiwa/669041168-日本語会話-基本文型８８.pdf`, 96 trang. Worker đọc status rồi init/claim. Tiếp tục toàn queue.
- Book06 đang chạy ở `/root/production_resume/production_book_06`; mốc9/93 verified. Coordinator đã QA toàn p1–6, sửa/readback ruby/nhãn/romanization; giữ ruby dị thường特定＝ことば ởTOC và ghi rõ nhận định受＝う bị rút sau tightcrop đối chứng. Chưa nghiệm thu06; tiếp tục QA phần mở đầu và cặp mẫu bài chínhp10.

## Tiến độ hai sách 06/07 — snapshot 2026-11-10

- Refresh CLI: 343/4597 verified, 8 rendered, 4246 pending, 0 machine issues. Năm sách accepted (305 trang) giữ nguyên; pilot điện thoại 4 trang giữ nguyên.
- Worker06 `/root/production_resume/production_book_06`: 25/93 verified. Coordinator đã đối chiếu nguồn toàn p1–20 và đang mở rộng mẫu phần chính; sửa/readback case romaji và map ruby theo occurrence/span thật. P24 còn chờ sửa hai span ruby xuống dòng.
- Worker07 `/root/production_resume/production_book_07`: 9/96 verified. Coordinator đã đối chiếu nguồn toàn p1–9, gồm mẫu bài thu nhỏ và đủ Nhật/Anh/Trung; lỗi đã sửa/readback, nhận định sai về ruby 天気 được rút sau crop đối chứng.
- Hai sách chưa nghiệm thu; ledger trong corpus ghi hash/phạm vi/trạng thái từng mẫu. Tiếp tục toàn queue, không blocker. Snapshot không chứng minh worker còn sống khi resume; đọc live agents và CLI thực.

## Snapshot tiếp tục 06/07 — 2026-11-10T14:55Z

- CLI refresh: 359/4597 verified, 5 rendered, 4233 pending, 0 machine issues; 5 sách accepted/305 trang nguyên vẹn, pilot điện thoại 4 trang nguyên vẹn. Hai worker hiện tại vẫn là production_book_06 và production_book_07 dưới /root/production_resume.
- Coordinator đã mở/so toàn p1–36 sách06, p1–14 sách07. P36 chờ bảo toàn gạch bỏ ます trong khung/ví dụ; p14 chờ giữ đúng lỗi thiếu んです ở đoạn Anh của nguồn. P33 macron kīte và p13 ruby xuống dòng đã sửa/reverify/readback. Ledger hash-bound ghi chi tiết, chưa nghiệm thu06/07.
- Tiếp tục toàn hàng đợi; snapshot không chứng minh tiến độ hiện tại hoặc tác nhân còn sống khi resume. Đọc CLI/status và live agents.

## Checkpoint tiếp tục 2026-11-10T15:22Z

Snapshot CLI/hash thực: 378/4597 verified, 3 rendered, 4216 pending, 0 machine issues. Năm sách đã nghiệm thu (305 trang) giữ nguyên. Hai worker Sol/high vẫn chạy: `/root/production_resume/production_book_06` 48/93 và `/root/production_resume/production_book_07` 21/96; không đổi claim. Astra/high đã mở ảnh/Markdown và crop kiểm tra chéo mọi trang 1–48 của book06, 1–21 của book07. Các ruby tự thêm p44–45 và dấu dakuten p18 đã sửa, reverify, đọc lại; audit ledger hiện không có finding chưa giải quyết. Đây là checkpoint giữa chừng, chưa nghiệm thu hai sách đang chạy; tiếp tục toàn bộ hàng đợi, không phải yêu cầu dừng.

Giới hạn nguồn book06 đã kiểm tra độc lập: PDF p54 in104–105/mục13/audio58, p55 in108–109/mục15/audio60; khoảng106–107/mục14 không có ở đoạn liên tiếp này. Ghi trong REVIEW nghiệm thu, không tái tạo nội dung thiếu. Bằng chứng hash ảnh trong COORDINATOR_AUDIT.json.


Snapshot 2026-11-10T15:40:07.475813+00:00: status_all 394 verified / 4597, 2 rendered, 4201 pending, 0 machine issues. Hai worker06/07 vẫn running; QA độc lập06 p1–57 và07 p1–25,07p26 đang sửa ruby/diagram theo crop. 5 sách accepted/305 trang giữ nguyên; source gap06 đã ghi ở trên. Tiếp tục toàn queue, chưa phải handoff dừng.


Source issue07 p28 (printed54–55): ảnh gốc PDF bị cụt lề trái/đáy, mất một phần hội thoại8 và dịch. Coordinator đã mở full và kiểm MediaBox/CropBox/XObject: p28 728.4×516, image3035×2150; p27/p29 841.68×595.2,image3507×2480. Worker lưu phần đọc được, đặt needs_review, tiếp tục p29+. Không tự thay nguồn hay suy đoán chữ; sách07 chưa thể nghiệm thu đầy đủ nếu thiếu nguồn trang này.


Snapshot 2026-11-10T15:58:22.759572+00:00: CLI thực 406 verified /4597, 2 rendered, 1 needs_review (book07 p28 nguồn cụt ảnh), 4188 pending. Worker06 báo 68/93; worker07 29 verified qua p30, tiếp p31+. Coordinator đã QA hash-bound06 p1–65,07 p1–27+29; p30 chờ bỏ một ruby 方 không in. Hai build partial đã chạy tại06 p65 và07 p30; chưa nghiệm thu. Tiếp tục toàn queue; source issue07 không chặn các trang/sách độc lập còn lại.

## Checkpoint 2026-11-10T16:19:09.813337+00:00

- status_all thực tế: 420 verified / 4597; 4172 pending, 4 rendered, 1 needs_review, 1 issue (book07 p28 nguồn bị cắt).
- Book06 đã build checkpoint75/93 partial; coordinator QA toàn trang1–75 currenthash clear. Book07 coordinator QA1–27+29–34 currenthash clear; tiếp tục các trang còn lại, p28 không được verify/accepted thiếu nguồn.
- Hai worker Sol/high production_book_06 và production_book_07 vẫn chạy; không có yêu cầu pause. Sau hoàn tất/QA từng sách tiếp tục queue08/09 theo AUDIT_NOTES.

Snapshot 2026-11-10T16:32:56.677575+00:00: CLI420→428/4597 verified,4161pending,7rendered,1needs_review (07p28 sourcecrop). Worker06 verified84/93, independent QA1–84 hashbound clear. Worker07 verified35 physical pages (1–27,29–36), auditing English line-end hyphens across1–27 after systemic corrections29/31/32/33/35/36; p37 rendered. Corrected pages29–36 independently read back, current hashes refreshed. Two workers running; next queue08 after06 accepted.


Snapshot 2026-11-10T16:49:09.327930+00:00: CLI438/4597verified,4154pending,3rendered,1draft,1needs_review(07p28sourcecrop). Haiworker06/07 running;06qua91/93,coordinatorQA1–90currentclear,p91chờ6hyphensEnglishheader.07qua40(39verified),partialbuild40;QA1–27+29–39currentclear sau16trangEnglishhyphenaudit1–27 đã mởsource/readback. Tiếpaccept06/dispatch08 khi QA/build đủ; chưa nghiệmthu06/07.

## 2026-11-10T17:02Z — book06 accepted, book08 dispatched

- Book06 `85-21a2cb6f3fef`: accepted all 93 physical pages after independent full-page QA; 0 issues, current build, claim released. Output commit `af0374b`; build SHA `13fb6c0136543cfb83bb91a92a0baf95c2399bf34ff93ccb95ee039402f3de05`. Supplied PDF itself skips printed106–107/item14 between physical54–55; limitation retained in acceptance. Accepted queue now6books/398pages.
- Running Sol/high agents: `/root/production_resume/production_book_07` continues book07 (p28 source crop blocker retained; other pages continue), and `/root/production_resume/production_book_08` owns `03-yuukibui-dd762e3fd201`103pages. New08 token `production_book_08_1794330003838_204673952`; fresh source hash matched and initialized103pending before work.
- Coordinator remains active through entire queue; next free slot gets queue09. No push. No source/bunpou/image output changes.


Snapshot 2026-11-10T17:19:51.873748+00:00: CLI486/4597verified,4109pending,1rendered,1needs_review(07p28sourcecrop). Accepted6books/398pages unchanged. Worker07 through50(49verified), correctingQA48–50 and expanding circled例1–50; worker08 through35/103. CoordinatorQA07 through50 pending3findings,08 all1–15 plus16/20/21/24/25/28–30 clear;35 bracketstyle correctionpending. TwoSol/highworkerscontinue;nextqueue09,notpaused.

QA follow-up:07 findings48–50 resolved/reverified/readback; expanded circled例 review31/48/50currenthashes clear.08 bracket35resolved/readback; independentQA36–37clear,40 pendingprintedunderline span. Worker08through40,07continues51+.

## Resume checkpoint 2026-11-10 17:39 UTC

Actual CLI snapshot: 519/4597 verified, 4076 pending, 1 rendered, 1 needs_review. Six accepted books (398 pages) remain intact. Active book07 has 57 verified through physical58, source-cropped28 remains needs_review; book08 has60/103 verified. Same two live Sol/high workers continue. Coordinator independently compared07 through57 and08 sampled lesson/vocabulary boundaries through57. Narrow italic span51 and punctuation53 corrected/reverified/readback. Queue continues09 then10 as slots free; no pause.


## Checkpoint 2026-11-10 17:58 UTC

Actual CLI snapshot at17:58:16Z:545/4597 verified,4049pending,1draft,1rendered,1needs_review (07p28 sourcecrop),1issue. Six accepted books/398pages intact. Book07 65verified through66 except28; book08 snapshot78verified, subsequently worker reported80. Same two Sol/high agents continue. Independent coordinator QA07 through65 except28;08 selected earlier pages and all64-78 plus80,79 bracket correction pending. Expanded08 Vocabulary/WordUsage emphasis audit1-65 done; changed18/19/33 independently source/crop/readback cleared. Expanded07 English romanized-form italics1-64 requested after64 omission, in progress. Continue entire queue09/10 as slots free; no pause and no complete acceptance for07 with cropped28.


## Checkpoint 2026-11-10 18:17 UTC

CLI thực: 571/4597 verified, 4022 pending, 3 rendered, 1 needs_review (book07 p28 nguồn bị cắt). Sáu sách đã nghiệm thu/398 trang giữ nguyên. Hai worker tiếp tục. Sau snapshot, book08 đến100/103 và book07 đến72. Coordinator đã kiểm độc lập các trang chọn trước đó và toàn64–100 của08; toàn1–27,29–72 của07. Rà mở rộng nhấn mạnh meaning/Point của07 còn chờ hoàn tất. Tiếp tục toàn hàng đợi, không tạm dừng.

## Nghiệm thu book08, cấp queue09 — 2026-11-10 18:26 UTC

- `03-yuukibui-dd762e3fd201`: ACCEPTED 103/103 trang vật lý, 0 issue, build hiện tại, claim đã release. Commit output `6f45fdc`; build SHA `d5ce526d1167c5ca7b82f644bbc200940ca6aea7889c8c7df81b5d98803a599f`. Coordinator kiểm độc lập92/103 trang và xử lý toàn bộ finding; báo cáo/acceptance ràng buộc hash trong corpus.215 file text staged đúng byte; kiểm whitespace đạt, bảo toàn hard-break/CRLF nguồn. Tổng đã nghiệm thu:7 sách/501 trang.
- Worker Sol/high mới `/root/production_resume/production_book_09` nhận136 trang của “5500 câu giao tiếp tiếng Nhật trong sinh hoạt hàng ngày”, book ID `5500-c-u-giao-ti-p-ti-ng-nh-t-trong-sinh-ho-t-h-ng-ng-y-c8933782539c`. Đã hash lại nguồn trước dispatch; worker init và claim owner `production_book_09`, token `production_book_09_20261111_0327`.
- Snapshot refresh18:26:53Z:579/4597 verified,4016 pending,1 rendered,1 needs_review. Snapshot chạy trước claim09 nên claim_owner còn null; token mới ở trên. Book07 qua75, tiếp76; trang28 thiếu nguồn vẫn needs_review, rà mở rộng nhấn mạnh còn chờ. Queue10 nhận slot kế sau bàn giao partial07. Tiếp tục toàn hàng đợi; không push.


## Checkpoint 2026-11-10T18:50:45.904532+00:00

CLI thực: {'pending': 3993, 'verified': 600, 'needs_review': 2, 'rendered': 2}; tổng4597 trang,2issues nguồn. Bảy sách accepted/501 trang nguyên vẹn. Hai Sol/high worker07 và09 vẫn running. Coordinator QA07 qua84 trừ28; rà mở rộng meaning/Point emphasis vẫn chờ worker hoàn tất. QA09 p2–10 hash-bound clear; p1 bìa sau khối liên hệ quá mờ, giữ needs_review và phần đọc được, không suy đoán.07p28 nguồn bị cắt giữ needs_review. Tiếp toàn queue; slot kế nhận10 khi07 bàn giao WIP partial, không gọi07/09 completed khi thiếu nguồn.

## Resume 2026-11-11 — toàn đội Sol/high

- User yêu cầu toàn bộ coordinator, QA, worker và sửa skill dùng `gpt-6-sol/high`, thay thế cấu hình Astra cũ. Skill 0.2.4 chỉ cập nhật phân công model, không đổi bằng chứng hay báo cáo QA lịch sử.
- Các agent 07/09 phiên cũ đã dừng theo live inventory của root. Trước recover, `status-all` kiểm file thật: 607/4597 verified, 3985 pending, 2 rendered, 3 needs_review, 3 issues. Book07 87/96 verified; p28 nguồn bị cắt, p89 rendered, p90–96 pending. Book09 15/136 verified; 2 needs_review, 1 rendered, 118 pending. Không sửa các trang đã verified còn hợp lệ.
- Phục hồi claim bằng CLI audit có token và `--confirm-writer-stopped`; sau đó giao hai sách cho worker Sol/high mới, ghi agent ID thật trong roster. Xem các mục tiếp theo để biết tiến độ sau mốc này.

## Book07 bàn giao WIP; queue10 bắt đầu — 2026-11-11

- Worker Sol/high `/root/production_sol_resume/production_book_07_sol_resume` đã verify p89–96, build partial và release. Book07 `669041168-4f47df1cc97a` hiện 95/96 verified; p28 nguồn PDF bị cụt giữ `needs_review`. `build_current=true`, build SHA-256 `084650d56ea9e4aa9e78e097aa20766d67ca1cc69a71549a7ac89502d6ec2716`; không gọi accepted. `corpus/.../HANDOFF.md`, `REVIEW.md`, `COORDINATOR_SOL_AUDIT.json` ghi chi tiết QA và hai audit mở rộng còn pending. Commit output mang nhãn WIP riêng.
- Slot được giao `/root/production_sol_resume/production_book_10_sol` (gpt-6-sol/high), book `shigoto-no-nihongo-bijinesu-manaa-hen-0e3d5e9467fa`, nguồn `book/BJT/Shigoto_no_nihongo_Bijinesu_Manaa_hen.pdf`, 136 trang. SHA nguồn preflight khớp roster. Bìa p1 có đoạn quảng bá bị cắt lề trái trong PDF; worker kiểm crop và giữ issue nếu thiếu chữ, không tái tạo.
- `/root/production_sol_resume/production_book_09_sol_resume` tiếp tục book09; p1/p16/p22/p24–27 có chữ mờ hoặc bị gáy đen che, lưu `needs_review` và vẫn xử lý p29+. Snapshot roster sau dispatch: 623/4597 verified, 9 needs_review, 1 rendered, 3964 pending. Số tiếp theo phải đọc CLI/file thật, không suy từ mốc này.

## Checkpoint Sol/high — 2026-11-10T21:43Z

- `refresh_roster.py` đọc file thật: 635/4597 verified, 3943 pending, 4 rendered, 1 draft, 14 needs_review (14 issue); bảy sách accepted/501 trang giữ nguyên. Hai worker live: `/root/production_sol_resume/production_book_09_sol_resume` (book09) và `/root/production_sol_resume/production_book_10_sol` (book10). Book07 đã bàn giao WIP 95/96, commit `e536c4e`; p28 còn phụ thuộc nguồn tốt hơn.
- Coordinator Sol/high đã mở ảnh thật và so Markdown book09 p14/15/17/35/38, đều không có sai khác đã biết trong mẫu; đã mở ảnh p22/24/33 kiểm chữ/dấu bị gáy che, giữ needs_review. Book10 đã so p11 divider và p12 quiz, đều không có sai khác đã biết trong mẫu; p1 bìa cụt, p3 publisher mark quá mờ. Hai sổ `COORDINATOR_SOL_AUDIT.json` giữ hash và phạm vi cụ thể. Book10 p5–7 nhiều ngôn ngữ/chữ nhỏ đang deferred rendered và worker cam kết quay lại trước handoff.
- Mốc này không phải nghiệm thu; cả hai worker giữ claim và tiếp tục trang đọc được. Tiếp tục toàn queue, không push.

## Book09 bàn giao WIP — 2026-11-10T21:48Z

- Worker `/root/production_sol_resume/production_book_09_sol_resume` dừng sau p41 và release claim sạch. Book09 có 28/136 verified, 13 needs_review do scan mờ/gáy đen che chữ, 95 pending p42–136; `build_current=true`. Chưa nghiệm thu. HANDOFF riêng và sổ QA coordinator ghi chi tiết; coordinator đã mở ảnh nguồn p31/p33 và xác nhận ví dụ chữ/dấu bị che, so nội dung p14/15/17/35/38 không thấy sai khác trong mẫu.
- Roster CLI ngay sau release: 636/4597 verified, 3942 pending, 2 draft, 1 rendered, 16 needs_review. Book10 worker vẫn chạy. Sẽ giao một worker Sol/high mới tiếp tục chính book09 p42–136; không bỏ qua các trang pending để chuyển queue11.

## Book09 tiếp tục p42+ — 2026-11-10T21:49Z

- Worker mới `/root/production_sol_resume/production_book_09_sol_cont` đã đọc handoff/status, nhận claim riêng `production_book_09_sol_cont_20261111_42b197`, bắt đầu render p42+. Roster đã gán đúng agent ID, `worker_state=running`. Book10 vẫn ở worker Sol/high riêng. Commit WIP book09 trước lượt mới: `50e43fc`; mọi số sau mốc này đọc từ CLI.
- Coordinator phát hiện tên tác giả ở chân preface book10 p5 bị chuyển chữ: nguồn in `釜渕優子`, Markdown trước sửa ghi `金渊优子`. Worker10 đang mở lại crop và sửa/reverify hash-bound; sổ QA ghi finding đang mở. Chưa coi mẫu p5 đạt.

## QA sửa tên tác giả book10 — 2026-11-10T21:51Z

- Worker10 đã tự mở crop PDF 8x p1/p3/p5, xác nhận cả ba in `釜渕優子`; sửa draft p1/p3 và re-record/reverify p5. Coordinator đọc lại ba Markdown, p5 checkpoint/evidence khớp SHA mới `1d13493bc54dcef765f33212895771ec3fdbae3c197f362d661e4fdd5f2638ad`. Finding trước đó đã được ghi resolved trong `COORDINATOR_SOL_AUDIT.json`. P1/p3 vẫn needs_review vì những vùng khác của nguồn bị cắt/mờ, không gọi verified.

## Checkpoint hai worker Sol/high — 2026-11-10T22:01Z

- Roster đọc file thật: 648/4597 verified, 3922 pending, 3 rendered, 2 draft, 22 needs_review. Bảy sách accepted/501 trang giữ nguyên. Book09 worker tiếp tục p42+, đến khoảng p52; p43/44/46 và các trang sát gáy khác có partial draft/issue nguồn, không đoán chữ. Coordinator đã mở/so toàn p42, không thấy sai khác trong mẫu. Book10 đến p19 verified (trừ p1/p3 needs_review và p6/p7 draft chờ so inset), còn đang tiếp p20+.
- QA book10 p16: worker đã sửa ba dấu lửng thành bốn dấu chấm rời `・・・・` theo crop 8x PDF, reverify; coordinator readback SHA mới `a751fe515b216b216e1050af672b85f855843b94f4762598d5ec2a4a593e1a08`. Mẫu p17 (ba ngôn ngữ) và p19 (sơ đồ đánh số hai người) không có sai khác đã biết. Sổ `COORDINATOR_SOL_AUDIT.json` ghi hash/phạm vi thật; đây vẫn là WIP, không nghiệm thu.

## Book09 bàn giao tiếp WIP tại p55 — 2026-11-10T22:04Z

- Worker `/root/production_sol_resume/production_book_09_sol_cont` đã nhả claim sau build/reconcile sạch. Book09 33/136 verified, 22 needs_review do scan che chữ, 81 pending p56–136; `build_current=true`, chưa nghiệm thu. Trong lượt p42–55: p42/45/47/49/50 verified, chín trang còn lại có draft và issue cục bộ. Coordinator đã so toàn p42 và p50 với ảnh, không có sai khác đã biết trong mẫu; sổ QA cập nhật hash.
- Roster ngay sau release: 649/4597 verified, 3920 pending, 2 draft, 1 rendered, 25 needs_review. Book10 worker tiếp tục p20+ và p6–7 còn đợi đối chiếu inset. Giao worker Sol/high mới tiếp book09 p56–136 sau commit WIP; không bỏ phần pending.

## Book09 p56+ và QA book10 p20 — 2026-11-10T22:07Z

- Worker mới `/root/production_sol_resume/production_book_09_sol_cont2` đã nhận claim riêng `production_book_09_sol_cont2_20261111_87ea`, tiếp tục p56+ sau commit WIP `b9f0bd3`. Roster đã gán đúng agent ID; kiểm CLI thấy claim live, không reclaim.
- Book10 p20 có một chữ Hán trong dòng Trung ③ sau `而不是` không phân biệt chắc bằng crop 8x; worker đã reset p20 khỏi verified sang draft và tiếp tục p21. Coordinator cũng mở crop, không xác nhận dự đoán chữ. Cần nguồn/ảnh rõ hoặc giữ needs_review, không suy diễn từ ngữ cảnh.

## Book09 bàn giao WIP tại p70 — 2026-11-10T22:26Z

- Worker `/root/production_sol_resume/production_book_09_sol_cont2` đã xử lý p56–70, build/reconcile sạch và nhả claim; book09 hiện 37/136 verified, 33 needs_review vì gáy đen che ký tự/dấu, 66 pending p71–136, `build_current=true`, chưa nghiệm thu. Mới verified p57/61/66/67; các trang còn lại p56–70 có draft phần đọc được và marker cục bộ. HANDOFF riêng của sách ghi chi tiết từng issue. Coordinator mở nguồn/so Markdown p57/61/66 không thấy sai khác trong mẫu; p58 xác nhận gáy che chữ; sổ QA gắn hash.
- `refresh_roster.py` đọc file thật ngay sau release: 662/4597 verified, 3893 pending, 39 needs_review, 1 draft, 2 rendered; bảy sách accepted/501 trang giữ nguyên. Book10 worker Sol/high vẫn giữ claim và tiếp tục, đã verified p6 sau đối chiếu mini-spread với bản đầy đủ PDF p30–31; p7 còn chờ PDF p34–35. Coordinator so p21/22/24/25/26/28/31, chưa thấy sai khác trong các phạm vi ghi sổ; p23/p27 có chữ nguồn quá mờ nên needs_review. Tiếp tục giao Sol/high book09 từ p71 sau commit WIP, không đoán chữ.

## Book09 tiếp tục p71+ — 2026-11-10T22:29Z

- WIP p56–70 đã commit `6420e9e`. Worker Sol/high mới `/root/production_sol_resume/production_book_09_sol_cont3` đã đọc handoff, claim thành công với token `production_book_09_sol_cont3_20261111_d91f` và bắt đầu physical p71. Roster đã gán agent ID thật, `worker_state=running`. Book10 worker riêng vẫn tiếp tục; status/QA về sau đọc từ file thật, không coi WIP là nghiệm thu.

## Book10 bàn giao WIP tại p41 — 2026-11-10T22:42Z

- Worker `/root/production_sol_resume/production_book_10_sol` đã xử lý qua PDF p41, build/reconcile thành công, nhả claim sạch. Book10 36/136 verified, 5 needs_review (p1 bìa cụt, p3 publisher mark mờ, p20 chữ Trung trước 用, p23 dòng viết tay mờ, p27 chữ Trung trước 鸡窝), 95 pending p42–136; `build_current=true`, chưa nghiệm thu. HANDOFF riêng ghi nguồn SHA/issue/next page. P6/p7 miniature đã đối chiếu đúng bản in cỡ đầy đủ PDF p30–31/p34–35 và verified; p36–41 verified.
- Roster đọc file thật sau release: 683/4597 verified, 3871 pending, 42 needs_review, 1 draft; bảy sách accepted/501 trang giữ nguyên, book09 worker Sol/high cont3 còn giữ claim và đang tiếp khoảng p83. Coordinator QA book10 thêm p21/22/24/25/26/28/31/34/35/36 và guide p6/7, không thấy sai khác trong phạm vi ghi hash; p23/p27 source issue xác nhận bằng ảnh/crop. Tiếp tục giao Sol/high book10 từ p42 sau commit WIP.

## Book10 tiếp tục p42+ — 2026-11-10T22:45Z

- WIP book10 p1–41 đã commit `610a9fd`. Worker Sol/high mới `/root/production_sol_resume/production_book_10_sol_cont` đã claim token `production_book_10_sol_cont_20261111_42f9a1`, bắt đầu PDF p42+. Roster đã gán agent ID thật, `worker_state=running`. Book09 worker Sol/high cont3 tiếp tục song song p85+; mọi count sau mốc này lấy CLI thực tế.
