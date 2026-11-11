# Tiếp quản điều phối clean và PDF → knowledge

Repo D:/CODE/git/kaiwa_skill; cwd môi trường D:/AI_SKILL. Luôn đặt workdir đúng repo. Đọc AGENTS.md và hai skill hiện hành trước khi nối việc.

## Mục tiêu và quyền đã giao

Hoàn tất30 PDF/4597 trang. User yêu cầu giữ lượt điều phối hoạt động, giao sách kế sau bàn giao, không final tại launch hoặc checkpoint giữa chừng. Không tạo chat, goal hay automation mới. Chỉ kết thúc khi hết phạm vi, user dừng hoặc giới hạn thực sự. Checkpoint trên đĩa giúp tiếp sau gián đoạn; không hứa tiếp tính toán khi ứng dụng đóng.

Raw đầy đủ dùng kaiwa-fork-knowledge; PDF chưa chạy/raw còn dở dùng kaiwa-pdf-knowledge, chỉ tham khảo raw cũ dưới dạng nguồn phụ chỉ đọc. Không sửa PDF/corpus/claim/snapshot. Bản knowledge đặt theo tên sách thật, giữ mạch riêng, mọi ví dụ Nhật kèm Việt, giải thích, bài tập, lựa chọn, ô trống, rolecard, đáp án in sẵn và phụ lục. Chú từ chân trang/dạng từ điển vẫn là kiến thức. Giữ dữ kiện hình đủ để làm bài và vai manga theo từng bóng thoại. Không tự giải, đoán tiếng Nhật từ bản dịch, hiện đại hóa nguồn hoặc gán topic/level.

Mỗi sách cần audio.json/audio.md: tên/ấn bản/ISBN, CD/tape/track/script/URL và bằng chứng trang/block khi thấy. File thực tế chưa kiểm thì not_checked. Không suy số đĩa từ nhãn CD hoặc tự tìm/tải. Một số inventory cũ có phạm vi giới hạn, không gọi là full audio audit.

## Runtime và phân công

Tất cả sub gpt-6-sol/high. Runtime4 active tính root nên tối đa3 sub active, luân phiên một vai điều phối và ba worker. Không tạo sub thứ năm. Root giữ Git và QA; một writer cho mỗi sách. Khi đang viết, root chỉ đọc và gửi sửa; khi bàn giao root mới sở hữu sửa/chốt.

- /root/knowledge_coordinator: idle sau bàn giao công cụ0.4.7; chỉ kích hoạt khi có slot và việc kỹ thuật cụ thể.
- /root/clean_keigo: **わかる！話せる！日本語会話 発展文型125**, full225 trang, 30 chương, book_id125-extended-patterns-for-japanese-conversation-4863922-95f1ac587f24. Front1–12 đã checked, tiếp序章13–16 rồi PART1 từ17. Map: PART1 17–52; PART2/A53–107, B108–155, C156–176; PART3 177–219; 文型リスト220–223; colophon/back224–225. ISBN9784863922440, in lần2 năm2016; CD付, actual files not_checked. Root còn cần QA sớm front/chương đầu. Sách88 đã bàn giao và chốt, không tiếp sửa88.
- /root/clean_namachuukei_sho: **しごとの日本語 電話応対 基礎編**, full162 trang, 38 chương, SHA dfdb0e2b61e0… đầy đủ trongCOORDINATOR. Front1–11, intro12–19, Unit1–3 PDF20–31 đã checked; tiếpUnit4 từ32.35 unit mỗi unit4 trang tới159; colophon/back160–162. Check lựa chọn cùng chữ nhưng khác giọng, tên/số điện thoại/tin nhắn, đáp án/script in riêng; không chuẩn hóa theo suy đoán. CDつき và mã1/2 củaUnit1, actual files not_checked. Root chưa QA, ưu tiên sớm front/intro/Unit1. Manners đã chốt, không tiếp ghi.
- /root/clean_namachuukei_chu: **聞いて覚える話し方 日本語生中継 初中級編２**, full152 trang/26 chương, SHA b5b793947c13… . Main10 bài PDF12–91 đã viết,167 units; tiếpあとがき/colophon92–94,別冊95–96,10 script chapters97–135,単語表136–141,解答142–151,back152. Phải giữ cả別冊, không điền script/đáp án vào đề. PDF83 needs_review hẹp: chỉ dẫn a〜e nhưng khung chỉ a–d. Cover ghi2CD; tracks tới2-43 đã thấy, không suy2-1. Root mở1/7/13/15/16/19/97, so vocab23mục và đềdictation/roleplay mẫu; đã yêu cầu sửa hai VI nhầm ngữ nghĩa ởbài1, worker báo sửa/refreshed. Cần lưu báo cáo QA mẫu, đọc hash mới và tiếp QA script/từ/đáp án khi viết xong. Badge bìa ghi JLPT旧3級, không tự đổi sangN3.

Mốc trên là snapshot, chạy resume/hash thật trước tiếp quản. Còn13 PDF chưa được giao, tra source_queue; tiếp giao hợp lý sau bàn giao, không hỏi lại quyền.

## Đã chốt phạm vi PDF cung cấp

14 sách/1474 trang. Danh sách/commit ở COORDINATOR.released_supplied_pdf_scope và knowledge/README.md. Bảy bản đầu501 trang full independent review; bảy bản mới author full/root sampled: roleplay140 (689603f, root16trang);本文冊138 (42b8667, root10); Nameraka163 (c92c81e, root15, nguồn32 bị che); Wakaru152 (0a884d7, root16);練習冊148 (a90b875, root5, author audit toàn chú từ); Manners136 (8a162ca, root17,100/100 đáp án ký hiệu);88patterns96 (c0c4dc1, root21 qua pilot/migration/mở rộng).

Manners nguồn23/69 phụ đề mờ,28 mảnh câu,105/106 thiếu trang in104–105. allow-source-issues0error/10warn. Sách88 nguồn9 công thức mâu thuẫn và28 cắt đáy câu8A/B; allow-source-issues0error/4warn. Giữ thông báo ngay trong bản đọc. Root đã so48 câu ôn/đáp án và mục tra cứu95–96; sửa hàng17 降りそう thành có vẻ sắp mưa dựa trên ngữ cảnh31. CD1–88 là nhãn đoạn, không phải88 đĩa. Các bản này không phải full independent semantic review.

本文冊 rebase có audit: toàn138 raw page bytes/PDF không đổi, compiled chỉ thêm4anchor/dòng trống. Snapshot mới b3ee70a10d8ae410/224b77fb-rebase-756b3046; history _meta/rebase-history/756b3046d61f4fd6a3ec63688854bd1c; giữ snapshot cũ9a2c9088f812080b/224b77fb.

Sách88 migration raw→direct1c2d7c0; history647ff62ba2fa4c548d7c92d5fb545857 bảo toàn4chapter/9unit/ledger/review cũ; extend full1–96 có scope-history, không init/reset. clean-state cũ inactive, direct-state hiện hành.

## Công cụ và kiểm tra

Version0.4.7, commite974bbf;62 test fork+17 direct PASS. Regression13 bản trước88:0errors/12warn nguồnNameraka+Manners;88 kiểm riêng0/4. Cache .cache/validator-regression/v047-results.json; helper run.py chỉ hỗ trợ root, không phải phụ thuộc sản phẩm.

Skill .agents/skills/kaiwa-fork-knowledge/SKILL.md và .agents/skills/kaiwa-pdf-knowledge/SKILL.md cùng direct-contract. CLI init/checkpoint/resume/build/validate/extend-scope. build không có --allow-source-issues; validate có. Full đang dở chỉ checkpoint/resume, không fake evidence/thu scope để xanh. needs_review chỉ lỗi nguồn đã mở ảnh, issue đúng page/block/unit; chưa viết dùng draft. Parser không chứng minh đúng nghĩa/đủ nội dung, không ép sách vào template để vượt parser.

Raw-fork scan nhận pin snapshot theo ledger gốc, bỏ ledger inactive của direct. rebase-identical-pages chỉ dùng khi PDF/rawpage byte-identical và compiled chỉ thêm anchor/dòng trống, luôn giữ history/snapshot.

## Git và môi trường

Git dùng chung chat ingest khác; stage exact paths và commit --only. Không add., reset, push, stage bunpou/PDF/corpus hoặc thay đổi ngoài phạm vi. Commit công cụ và từng sách nghiệm thu riêng. knowledge/source_snapshots giữ bytes theo.gitattributes, CRLF và2space hardbreak có chủ đích. Whitespace check với core.whitespace=-blank-at-eol,-blank-at-eof,cr-at-eol.

Dùng py -B, PYTHONUTF8=1, import pymupdf as fitz; pdfinfo/Poppler có PATH. Output chỉmd/json/jsonl; ảnh/crop/helperPython ở ignored.cache. exec_command trảsession_id thì poll write_stdin; functions.wait chỉ dùng nếu functions.exec báo running cell. Không sleep/wait chặn quá60giây; gửi commentary tiếng Việt ngắn khi có thay đổi có ý nghĩa, khoảng60giây trong lúc làm.

Không final ở trạng thái này; tiếp QA và điều phối hàng đợi tới hết phạm vi.
