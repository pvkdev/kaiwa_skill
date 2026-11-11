# Tiếp quản điều phối clean + PDF → knowledge

Repo: D:/CODE/git/kaiwa_skill. Không ghi nhầm vào cwd D:/AI_SKILL. Người dùng giao hoàn thành tất cả30PDF, giữ lượt điều phối sống; không final chỉ để thông báo khởi chạy. Không tạo automation/goal. Đóng app dừng tính toán; nội dung/checkpoint/history trên đĩa cho phép nối lại.

## Yêu cầu hiện hành

- Raw hoàn chỉnh → fork clean. Raw chưa có hoặc còn dở → PDF-direct, tận dụng trang raw đã có như tài liệu phụ chỉ đọc; không phải hoàn tất lượt raw trước. Giữ corpus/claim/snapshot cũ.
- Viết lại sách dễ đọc, đầy đủ kiến thức, mọi ví dụ Nhật+Việt, bài tập/dữ kiện/ô trống/lựa chọn/đáp án, phần riêng và mạch riêng. Không tóm tắt, không ép template/topic/level, không tự giải hoặc điền phần bị blank vào bản Việt. Bỏ helper furigana/romaji và bản dịch ngoại ngữ trùng; giữ cách đọc khi chính nó là dữ liệu học.
- Mỗi sách cần audio.json + audio.md trong _meta, có thông tin CD/tape/track/script/URL/identity nhìn thấy và dẫn trang. File thực tế chưa kiểm thì not_checked, không suy có audio từ nhãn CD.
- User yêu cầu1sub điều phối+3worker gpt-6-sol/high. Runtime chỉ4active tính cả root, nên luân phiên4vai sub; tối đa3sub active. Không mở chat mới để lách.

## Công cụ/skill hiện tại

Version0.4.5. Đọc AGENTS.md, DIRECT_PLAN.md, COORDINATOR.json rồi skill phù hợp.

- `.agents/skills/kaiwa-fork-knowledge/SKILL.md`: raw-fork, scripts clean_progress.py/build_fork.py/validate_fork.py.
- `.agents/skills/kaiwa-pdf-knowledge/SKILL.md`: direct; đọc references/direct-contract.md và CLI help. direct_progress.py: init/checkpoint/resume/build/validate/extend-scope.
- Full direct còn dở: checkpoint/resume từng trang/chapter và QA chapter trực tiếp. Build cần evidence toàn scope; không tạo trang giả/đổi scope để làm xanh.
- needs_review riêng cho nguồn bị che/mất: issue phải trỏ đúng page/block và unit. Strict validate từ chối; --allow-source-issues chỉ cho cấu trúc đủ kèm warning, vẫn từ chối pending/draft/stale/missing. Builder chèn notice và source-issues.md.
- extend-scope giữ chapter cũ và history, trang mới pending. Sau thay nội dung phải kiểm lại, không dùng review pilot cũ để xác nhận full.
- Raw compiled chỉ thêm anchor/dòng trống, mọi raw page byte-identical/PDF không đổi: coordinator dùng rebase-identical-pages --note. Lệnh lưu history/snapshot mới, không sửa nguồn cũ và không thêm xác nhận nội dung.
- Test gần nhất:35fork +17direct PASS; quick_validate hai skill PASS. Không chạy lại vô cớ. Dùng py -B và PYTHONUTF8=1; Python có pymupdf và yaml, pdfinfo/Poppler trên PATH.

## Bốn vai sub

1. `/root/knowledge_coordinator`: Sol/high, hiện idle sau bàn giao công cụ rebase. Không ghi nội dung sách. Có thể kích hoạt khi worker bàn giao để phân tích/hỗ trợ kỹ thuật; không chạy thêm khi đã3worker active.
2. `/root/clean_keigo`: solewriter direct `knowledge/なめらか日本語会話`,163trang,27chapter. Đã hết23bài và index tớiPDF153; đang phần đáp án154–162. PDF32/chapter05 needs_review vì vùng câu hỏi VII.2/VII.4 bị ghi tay che, các dòng đáp còn rõ được giữ; root mở full và crop, PDF chỉ1image/khôngannotation/textlayer. Không nhập ghi tay làm đáp án. Source SHA7a1ef4391141caedb682df607d058a97be189823fb5e5521d39614fa34d53c28. Front đã sửa đủ câu Nhật kính áp tròng, ý luyện JLPT, điều kiện phương ngữ theo QA root.
3. `/root/clean_namachuukei_sho`: solewriter direct mở rộng `knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）`,152trang,21chapter. Đã hết45Scene tớiPDF129; đang phụ lục130–148, rồi bổ sung đáp án150–151. Chapter đáp án cũ hạ draft chờ150–151, bảo toàn lịch sử pilot. PDF9 từng chỉ là chứng cứ CD đã được viết đầy đủ toàn trang. Scope-history0d41f3f5a6db420eb04b02c26e0c4720.
4. `/root/clean_namachuukei_chu`: solewriter direct `knowledge/日本語でビジネス会話 中級編 練習冊`,148trang,21chapter. Đã tới Bài13/PDF97; đang Bài14 từ98. Raw23trang chỉ tham khảo, không sửa corpus/claim. Root đọc chat ingest và hai child, đều idle/interrupted lúc04:35UTC nên đã phân direct tường minh. Bài15 nguồn vào thẳng談話練習, không thêm pattern. Source SHA3e66906b7e052b1394bb246542ce5087b15570da4dcf2425d037e4d198a2440b.

Các mốc trên là snapshot; khi tiếp quản dùng state thật/resume. Không giao hai writer một sách. Root QA chỉ đọc khi writer active, gửi tác giả sửa. Root giữ Git.

## Đã có bản đọc đủ PDF đầu vào

9sách/779trang:7sách trước501trang đã full independent QA (xem knowledge/README.md và từng _meta); thêm roleplay140 và本文冊138 được tác giả đối chiếu toàn sách, root QA mẫu16/10trang. Không gọi hai bản mới là full independent semantic review.

- Roleplay140: commit689603f;10chapter/109unit, coverage124author_checked+16excluded. Root sửa deadlinePDF35, bài tập không lộ blank và nghĩa 行っております ở quiz97. Root crop140 xác nhậnヨツビシ khác raw OCR, lỗi chép đã giải quyết. Nhãn case2ởPDF56 vs case3trongTOC/PDF69 là vấn đề nguồn có log. Audio1CD/ISBN9784883197705/15mã01–15/URL3A4018, actualfiles not_checked.
- 本文冊138: commit42b8667;22chapter/128unit,135content+3excluded. Root QA10trang, sửa khung3ô/điều kiện cóai thíchbơi/lời rủ kết thúc ngày làm việc/helperfuri bảng họ. Rebase tường minh sau compiled raw thêm4anchor trang11–14; tất cả138rawpage bytes và nội dung22chapter không đổi. Snapshot mới b3ee70a10d8ae410/224b77fb-rebase-756b3046; history _meta/rebase-history/756b3046d61f4fd6a3ec63688854bd1c. Old snapshot9a2c9088f812080b/224b77fb giữ nguyên. Build/validate0/0; resume22current, không drift/pending/stale. Coverage/audio giữ một số refs snapshot cũ như bằng chứng lúc tác giả đọc; unitrefs hiện tại dùng bản mới byte-identical.

## Pilot và việc còn lại

- Pilot direct Wakaru đã root xem toàn6trang1/17/18/23/149/152 và9CD, sửa rồi PASS; commit9e2f7d5. Report `_meta/pilot-independent-review.json` lưu hash lịch sử. Sau đó đã giao full và extend cùngfolder; không init/reset.
- Pilot88 đã migration PDF-direct commit1c2d7c0; vẫn scope7–12,4chapter/9unit. History647ff62ba2fa4c548d7c92d5fb545857 bảo toàn toàn bộ metadata/ledger/review cũ; chapter bytes không đổi. Công thức nguồn PDF9 mâu thuẫn vẫn needs_review, validate --allow-source-issues0error/2warning. Full96trang/PDF28crop chưa làm; worker kế dùng extend-scope, không init/reset.
- Routing toàn30PDF ở COORDINATOR.json. Ngoài3sách active, còn12PDF chưa khởi tạo,5rawpartial chuyển direct và88 chờ extend-scope sau migration. Chọn sách kế khi một worker bàn giao, tiếp tới hết phạm vi được giao. Nguồn hỏng giữ needs_review và cảnh báo, không suy chữ/audio.
- Root đã tạo inventory cho7bản full cũ và pilot88; nhiều hồ sơ chỉ một phần/unknown, không giả full audio audit. knowledge/AUDIO_INDEX.md có dẫn hồ sơ; cần cập nhật snapshot sau milestone.

## Git và QA

Git chung checkout/index với chat ingest khác. Không git add ., không reset/push. Chỉ exact-path stage/diff rồi commit --only. Code, output từng sách và control tách commit. Đầu ra chỉmd/json/jsonl; ảnh/crop cache không commit, bunpou và PDF chỉ đọc. .gitattributes giữ bytes knowledge/source_snapshots; CRLF và2space Markdown hardbreak là chủ ý, không normalize snapshot hoặc nội dung đã chốt chỉ để hết diff whitespace.

Recent code:09add94 directskill;5a36306 pilotfix;1f573f3 extend-scope;27f72c5 needs_review+legacycompat;62033eb auditedrebase+partialrawroute. Control/audio snapshot trước c8a3c4e; control hiện có thay đổi chưa commit sau hai book completion.

Root sampled QA bổ sung ngoài livebook trong clean/reviews. Validator/hash không chứng minh đúng nghĩa hoặc đọc ảnh; không nâng review ngoài phạm vi đã xem.
