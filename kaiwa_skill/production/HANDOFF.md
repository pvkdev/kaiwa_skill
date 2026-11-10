# Production — tiếp tục toàn bộ hàng đợi

Người dùng đã yêu cầu chuyển đổi tất cả PDF. Gate pilot PASS nằm tại `kaiwa_skill/pilot/REVIEW.md`; skill hiện tại 0.2.3 (làm rõ đối chiếu header/footer, furigana và dòng nối bảng, không đổi nội dung pilot), output chỉ text. Danh sách nguồn và phân công chuẩn: `roster.json`; bản dễ đọc: `ROSTER.txt`. Đường dẫn nguồn trong roster tương đối từ `kaiwa_skill/`; đường dẫn corpus tương đối từ repo.

Điều phối `gpt-6-astra/high`; chỉ hai worker `gpt-6-sol/high` cùng lúc, mỗi worker đúng một PDF. Chạy các lệnh từ gốc repo hiện tại. Root chat không dùng Git; coordinator chịu trách nhiệm commit tuần tự theo sách. Không sửa `bunpou_skill/` hoặc PDF nguồn.

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
