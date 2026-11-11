# Cập nhật gần nhất — pilot trực tiếp đã PASS

- Skill v0.4.1, code mới commit09add94, quy tắc sửa sau QA5a36306, output pilot commit9e2f7d5. Root đã mở ảnh và đọc toàn output pilot, sửa bản dịch bài tập/2nghĩa/nhãn4lượt. Report trong thư mục Wakaru `_meta/pilot-independent-review.json` có hash; chỉ6trang, không full152trang.
- Full direct đã giao `/root/clean_keigo`: `なめらか日本語会話`163trang, PDF `book/Shadowing/なめらか日本語会話 Nameraka Nihongo Kaiwa.pdf`, sourcehash7a1ef4391141caedb682df607d058a97be189823fb5e5521d39614fa34d53c28. Xác nhận title/ALC/富阪容子, lần in6 ngày2002-08-05; tape bán riêng. Map27chapter: front1–9;23§ (PART1p10–43/PART2p44–85/PART3p86–145);index146–153;answers154–162;colophon163. Đang bắt đầu; chưa xác nhận fullbook.
- Roleplay author đã115/140; 本文冊 author41/138. Cả hai đang tiếp, inventory audio thêm theo nguồn. Sub điều phối công cụ idle nhườngslot cho3worker.
- Root thêm CLI `extend-scope` để sau này mở rộng đúng sách pilot sang full mà giữ checkpoint cũ, lưu scope-history và để trang mới pending;10test direct PASS. Chưa chạy extension trên sách thật vì worker đang làm Nameraka. Không init/reset pilot.
- Các ghi chú trước đó dưới đây là checkpoint lịch sử; dùng COORDINATOR.json/manifest/ledger hiện tại để xác nhận tiến độ.

# Tiếp quản luồng clean + PDF trực tiếp (yêu cầu mới 2026-11-11)

Kế hoạch hiện hành: `DIRECT_PLAN.md`; phân công/routing thực tế: `COORDINATOR.json`. Phần dưới mục **Handoff cũ** là lịch sử, không phải lệnh khởi chạy raw cho mọi sách nữa.

- Giữ raw hoàn chỉnh → fork clean; 14 PDF chưa khởi tạo raw được dành cho kaiwa-pdf-knowledge, không ingest raw mới. 7 nguồn raw dở/có vấn đề phải kiểm claim/trạng thái trước phân công; không lấy bản dở giả làm hoàn chỉnh.
- Root đã viết `.agents/skills/kaiwa-pdf-knowledge/SKILL.md`. Sub `/root/knowledge_coordinator` (gpt-6-sol/high) viết scripts/direct_progress.py + references/direct-contract.md + tests, không viết nội dung sách. Đọc CLI/contract thật; PDF-native không có source_markdown hoặc raw snapshot.
- `/root/clean_keigo` (Sol/high) là solewriter pilot Wakaru_Bijinesu_Nihongo.pdf: scope PDF1/17/18/23/149/152, toàn bộ nội dung các trang trong scope; PDF9 supplementaryCD evidence. Đã mở nguồn, đang viết bản sạch; chưa PASS. Root cũng đã mở ảnh1–10,17/18/23/24/149/152; checklist độc lập cache `.cache/direct-pilot/root-source-check.md`. Root phải kiểm output và sửa skill nếu lỗi rồi mới mở full direct.
- `/root/clean_namachuukei_sho` tiếp roleplay140 từ checkpoint85 trang, đang Unit5. `/root/clean_namachuukei_chu` 本文冊138 đã author-check1–29, tạm dừng nhường slot, cần resume khi sub công cụ bàn giao. Không reset hai sách này.
- Người dùng yêu cầu1subđiềuphối+3worker, tất cảSol/high; runtime chỉ4active kểroot, nên luân phiên4vai sub, tối đa3sub active. Root điều phối lúc3worker cùng chạy. Không tạo chat mới để lách giới hạn.
- Mọi sách cần `_meta/audio.json`+audio.md: identity/edition/ISBN/publisher khi thấy, CD/track labels và map bài/hoạtđộng/unit/trang, script/downloadrefs in nguồn, fileactualstatus. Không đoán CD count/trackrange; `not_checked` khi chưa kiểm file. Pilot88 đã được root mở lạiPDF10–12 và ghi inventory3nhãnCD1/2/3, không suy3đĩa; các bảnclean cũ còn lại cần bổ sung.
- 30testsold vàquickvalidate2skills PASS sauentryskillmới; directtestsđang đượcsubviết, chưanghiệmthu. Git chungvớichatingest, chỉexactpaths vàcommit--only.

## Handoff cũ — lưu lịch sử trước đổi luồng

# Tiếp tục điều phối clean từ đây

Repo D:/CODE/git/kaiwa_skill. Người dùng yêu cầu giữ lượt sống, điều phối clean toàn catalog30 PDF và đúng3 worker gpt-6-sol/high. Không final chỉ vì đã khởi chạy/bàn giao một sách; tiếp tục nhận nguồn ready. Không tạo goal hay automation. Đóng app dừng tính toán; checkpoint là để mở lại.

Đọc AGENTS.md, skill `.agents/skills/kaiwa-fork-knowledge/SKILL.md` (v0.3.8), COORDINATOR.json, STATUS.md. Root trực tiếp QA/Git; workers không Git/spawn/sửa corpus/PDF. Source snapshots bất biến nằm ngoài knowledge.

## Ownership hiện tại

- `/root/clean_namachuukei_sho`: FULL CLEAN mới `remake-ad35b87b708d`, PDF roleplay中級140 trang. Folder `kaiwa_skill/knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―`. Snapshot `kaiwa_skill/source_snapshots/remake-ad35b87b708d/87df499c907819b7/61190cf5`. Plan10 phần: front1–25; Unit1 26–40; Unit2 41–55; Unit3 56–69; Unit4 70–85; Unit5 86–99; Unit6 100–115; Unit7 116–127;敬語/ấn bản128–129;別冊 đáp án130–140. Worker tự tiếp từng chương, dịch cả đáp án Nhật, giữ mọi phần riêng/mạch/role/blank/track. Root không sửa khi worker còn sở hữu.
- `/root/clean_namachuukei_chu`: FULL CLEAN source01-yuukibui-b12c61270c7b,138 trang, đã ready. Folder `knowledge/日本語でビジネス会話 中級編 本文冊`, title thật có本文冊 trênPDF2. Snapshot `source_snapshots/01-yuukibui-b12c61270c7b/9a2c9088f812080b/224b77fb`. Plan22 file: front1–13,20課14–135,hậu từ/trắng136–138. Tự checkpoint và tiếp toàn sách.
- `/root/clean_keigo`: PREFLIGHT ONLY shadowing初中級145 trang, corpusbook-be075317cdca. Preflight full88/5500/businessmanners/telephone đã bàn giao trongclean/preflight; root đã đọc. Không sửa knowledge hoặc nguồn khi chưa ready.

## Đã bàn giao và commit

7 nguồn/501 trang đã clean và independent QA toàn phạm vi: Sho91p latest87139ff; Chu89p6a11343; N3 47p primaryebdd6d6 + root dịch4gloss600a35d; MINATO1160 checklist8p eea30db; Keigo93p3f227ed; N1 70p5d1612f; business英訳・語い冊103p4b99345. Xem metadata completion/review của mỗi sách. Chưa push.

- Keigo: root mởPDF85–87/đọc đủ164 cặp đáp án mới, sửa taxi đến và明日までに chậm nhất ngày mai;164 câu Nhật giữ nguyên. Whole93p primary QA do Sho, phần Việt mới root QA. PDF nguồn thiếu trang in106–107/bài14;15 units needs_review. Không phục dựng bài thiếu.
- N1: raw1132 thiếu（と）. Worker sửa theo ảnh, root mởzoom68-68.png xác nhận, chấp nhận statuspdf_checked_with_raw_correction cho unit68; provenance giữ, không cần nghi vấn chép chữ vĩnh viễn. Chỉ đúng1 ô khác raw; source gloss1159/1165 vẫn needs_review.
- N3:880 hàng/cách đọc/Hán Việt giữ;5 nghĩa đáng ngờ360/543/632/636/682 ở4 units needs_review. Chỉ4 gloss517/520/532/546 được dịch/lọc English có log, không còn khẳng định mọi ô khớp raw tuyệt đối. Review chính và root follow-up hashes được giữ tách.
- Pilot88: PDF7–12,4 chapters/9units, commitab929bd. Root mở đủ6 ảnh, khôi phục thêm giải thích/mạch/MEMO; CD01–03 và trang mở PART1 đã giữ. Scope vẫnpartial; review lịch sử không xác nhận bản mới. Record mới preservation-independent-review.md. Full nguồn cònPDF28 chưaready, không mở rộng hoặc reset ledger.

## Vận hành

Dùng `py -B`, PYTHONUTF8=1; `python` PATH là Store alias. clean_progress.py scan/resume/checkpoint; build_fork.py/validate_fork.py trong scripts skill.30 tests đã pass ởv0.3.8; validator mới chỉ thêm cảnh báo heuristic số ô trống và đã chạy trên7 bản full +pilot đều0 lỗi/cảnh báo; quick_validate skill pass. Không chạy lại toàn bộ tests vô cớ.

Quét nguồn sau bàn giao và định kỳ. Chỉ clean nguồnready; preflight không nghĩađãclean. Giữ đúng1owner/book, không lấy nguồn đang dở để init full. Metadata source/hash và ledger khác phạm vi sẽ báo lỗi; không reset/đổi hash để che. Raw correction theoPDF có chứng cứ được phép, không sửa snapshot.

Git chung checkout/index với ingest ở chat khác. Chỉ exact-path `git commit --only -- <book> <snapshot>`; file mới dùng gitadd-N đúng path. Kiểm shortstat/commit paths, không gitadd., không reset history, không push. Ảnh chỉ ignoredcache, output chỉ.md/.json/.jsonl. Control files/README mới cập nhật hiện trạng rồi commit riêng. Worker tựcheckpoint và báo tiến độ; root không kết thúc khi một worker rảnh, giao nguồn ready hoặc preflight hữu ích tiếp.

## Root sampled QA đang dở

Roleplay: root đã mở ảnh PDF7/19/24/31/35 từ `.cache/renders/remake-ad35b87b708d`. Front table/14 tình huống/cast/chú thích若干名1–5 đúng nguồn; resumeformふりがな là dữ liệu nên giữ. Yêu cầu sửa deadline PDF35 thành chậm nhất sáng ngày kia đã được worker sửa/checkpoint Unit1. Ghi chú tạm ở `.cache/clean/root-roleplay-qa.md` để dùng lúc fullhandoff. Chưa gọi QA toàn25/40/140 trang.
