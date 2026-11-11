# Tiếp quản điều phối clean và PDF → knowledge

Repo D:/CODE/git/kaiwa_skill; cwd môi trường D:/AI_SKILL. Luôn đặt workdir đúng repo. Đọc AGENTS.md và hai skill hiện hành trước khi nối việc.

## Mục tiêu và quyền đã giao

Hoàn tất30 PDF/4597 trang. User yêu cầu giữ lượt điều phối hoạt động, giao sách kế ngay sau bàn giao; không final tại launch hoặc checkpoint giữa chừng. Không tạo chat, goal hay automation mới. Chỉ kết thúc khi hết phạm vi, user dừng hoặc giới hạn thực sự. Checkpoint trên đĩa giúp tiếp sau gián đoạn; không hứa tiếp tính toán khi ứng dụng đóng.

Raw đầy đủ dùng kaiwa-fork-knowledge; PDF chưa chạy hoặc raw còn dở dùng kaiwa-pdf-knowledge, chỉ tham khảo raw cũ dưới dạng nguồn phụ chỉ đọc. Không sửa PDF/corpus/claim/snapshot. Bản knowledge đặt theo tên sách thật, giữ mạch riêng, mọi ví dụ Nhật kèm Việt, giải thích, bài tập, lựa chọn, ô trống, rolecard, đáp án in sẵn và phụ lục. Chú từ chân trang/dạng từ điển vẫn là kiến thức. Giữ dữ kiện hình đủ để làm bài và vai manga theo từng bóng thoại. Không tự giải, đoán tiếng Nhật từ bản dịch, hiện đại hóa nguồn hoặc gán topic/level.

Chỉ bản dịch ngoại ngữ trùng nghĩa mới được bỏ; phần riêng phải giữ bằng Việt. Mọi lượt trong bản Việt phải đủ, không tóm hội thoại hoặc tự chọn phương án đúng. Dịch các mảnh đáp án theo ngữ cảnh đề, không lấy nghĩa từ điển bất kể ngữ cảnh. Đối chiếu chiều so sánh, phủ định, nhân quả và hạnまでに; không đẩy hạn chậm nhất ngày mai thành hôm nay. Các lời nhắc về xử lý scan/chữ viết tay/ảnh chỉ trang trí/lọc lớp dịch để ở_meta, không lặp trong bài học. Những chú ý lặp nguyên văn trong cùng sách nên dùng bản Việt đã so thống nhất tại từng đề, không tự biến thành yêu cầu mới.

Mỗi sách cần audio.json/audio.md: tên/ấn bản/ISBN, CD/tape/track/script/URL và bằng chứng trang/block khi thấy. Tệp thực tế chưa kiểm thì not_checked. Không suy số đĩa từ nhãn CD, hoặc tự tìm/tải. Một số inventory cũ có phạm vi giới hạn, không gọi là full audio audit.

## Runtime và phân công

Tất cả sub gpt-6-sol/high. Runtime4 active tính root nên tối đa3 sub active, luân phiên một vai điều phối và ba worker. Không tạo sub thứ năm. Root giữ Git và QA; một writer cho mỗi sách. Khi đang viết, root chỉ đọc và gửi sửa; khi bàn giao root mới sở hữu sửa/chốt.

- /root/knowledge_coordinator: idle sau bàn giao công cụ; chỉ kích hoạt khi có slot và việc kỹ thuật cụ thể.
- /root/clean_keigo: **わかる！話せる！日本語会話 発展文型125**, full225 trang/30 chương, book_id125-extended-patterns-for-japanese-conversation-4863922-95f1ac587f24. Đã qua PART1/PART2 và đang PART3 từ177; snapshot gần nhất source185 checked, xem resume thật. Source issue120/unit67: lượt A cuối chỉ có ở cột Anh–Trung, thiếu Nhật/romaji; giữ Việt riêng, không dựng Nhật. Root đã mở21 trang1/2/8/10–16/18–23/35/51/52/120/224, so trọn nhóm01–04 và các mẫu bổ sung. Đã sửa số1–2 hội thoại trong guide11,ただ ở序章16, hạn35, dẫnMEMO具合51 và nghĩa彼女52. Colophon224: ISBN9784863922440, lần1 ngày2015-10-10/lần2 ngày2016-11-10. Báo cáo ngoài sách: clean/reviews/125-root-sampled.md. Worker đang bỏ boilerplate xử lý ảnh/dịch khi rà cuối. Bảng mẫu220–223 và colophon/back224–225 vẫn phải được viết đầy đủ.
- /root/clean_namachuukei_sho: **しごとの日本語 電話応対 基礎編**, full162 trang/38 chương, book_idshigoto-no-nihongo-denwa-outai-kisohen-dfdb0e2b61e0. Đã tới Unit23/PDF111, tiếp112; source issue83/Unit16 Note⑧ dừng ởため、,84 mở Unit17. Root đã mở23 trang:1/5/11–18/20–23/45/49/51/83–87/160. So trọn Unit1/17, intro12–18, rolecard45, ví dụ49/51 và identity160. Đã sửa đảo nghĩa giọng thấp/nhanh, mất lời khuyên, TOC34; khôi phục ví dụ notes và audit Unit1–9; sửa chú ý monologue Unit10–17: bắt đầu nói trong1phút, kết thúc khoảng2phút, không phải2phút tự kiểm. Worker đã bỏ boilerplate hình trang trí/bảng ngoại ngữ lặp tớiUnit22 và refresh checkpoint. Rolecard45 cố ý giữ khác biệt山本商事/山川商事 theo nguồn; số60/30 lạ vẫn giữ bản in, không normalize. ISBN9784757413313, lần1 ngày2007-12-25/lần4 ngày2014-05-26. Xem clean/reviews/denwa-root-sampled.md; cần bổ sung vào báo cáo lần mở83–87 và sửa thời gian sau khi root đọc lại bản mới. Chưa release.
- /root/clean_namachuukei_chu: **シャドーイング 日本語を話そう！ 初・中級編 インドネシア語・タイ語・ベトナム語版**, full145 trang; book_idbook-be075317cdca, SHAbe075317cdcab1bad0245126bf7c4fe9bb066fcb714bc19aa841f5373b612869. Front1–6 và guide7–23 đã checked, tiếp Unit1 PDF24–45. Source có sẵn Việt, tận dụng/đối chiếu với Nhật; Indonesia11–14/Thai15–18 chỉ loại sau so trùng. Preflight title2/colophon139, ISBN9784874246061,2013-12-24 lần1. Cấu trúc:5 Unit24–137, cột cuối138, xuất bản139,140 trắng,141–145 quảng cáo. Phải xác minh F/C/D và số CD qua legend, không coi là3đĩa. Root chưa QA sách này, ưu tiên sớm hai chapter đầu; sau đó tiếp mẫu thoại/đối chiếu Việt. Không init raw, corpus/book-be075317cdca chỉ đọc; fresh scan raw vẫn chờ với66verified/77needs_review/2draft. Không chờ raw hoàn tất.

Mốc trên là snapshot. Chạy resume/hash thật trước nối việc. Còn12 PDF chưa được giao, tra source_queue. Tiếp giao hợp lý sau bàn giao, không hỏi lại quyền. Với raw đang dở, PDF-direct là tuyến đã được user cho phép.

## Đã chốt phạm vi PDF cung cấp

15 sách/1626 trang. Danh sách/commit ở COORDINATOR.released_supplied_pdf_scope và knowledge/README.md. Bảy bản đầu501 trang full independent review; tám bản mới author full/root sampled. Full là PDF được cung cấp; vùng thiếu/che/mâu thuẫn không được dựng lại.

Các bản mới: roleplay140 (689603f, root16 trang);本文冊138 (42b8667, root10); Nameraka163 (c92c81e, root16 sau audio followup8f19042, nguồn32 bị che); Wakaru152 (0a884d7, root16);練習冊148 (a90b875, root5, tác giả audit toàn chú từ); Manners136 (8a162ca, root17 và100/100 ký hiệu đáp án);88patterns96 (c0c4dc1 + deadline followup, root21); Nama2 152 (1e29c64, root27).

Manners nguồn23/69 phụ đề mờ,28 mảnh câu,105/106 thiếu trang in104–105.88patterns nguồn9 công thức mâu thuẫn,28 cắt đáy câu8A/B. Nama2 nguồn83 a〜e nhưng khung chỉa–d;119 hai nhãnB liên tiếp. Những bản này dùng validate --allow-source-issues, giữ cảnh báo ngay đầu bản đọc. Nama2 còn9 cảnh báo bố cục ô trống đã root so nguồn15/23/31/39/47/87, đề/câu/bảng vẫn giữ ô thật;0error/13warning. Root đã đưa các chỉ dẫn xử lý scan/lọc dịch tự thêm ra_meta và build/validate lại trước release. Các phần khác do tác giả đối chiếu toàn sách, không gọi là full independent semantic review.

本文冊 có rebase byte-identical đã audit; giữ cả snapshot/history cũ.88patterns có migration raw→direct1c2d7c0, giữ history647ff62ba2fa4c548d7c92d5fb545857 và scope-history, clean-state cũ inactive. Không init/reset hoặc sửa nguồn để né stale. Những lịch sử này đã commit, không cần làm lại.

## Công cụ và kiểm tra

Version0.4.10;80 test fork+17 direct PASS. Regression15 bản đã chốt:0errors/29warnings; cache .cache/validator-regression/v0410-15-results.json. Cảnh báo gồm vùng nguồn đã biết và9 cảnh báo bố cục của Nama2. Không chạy lặp tests khi không có thay đổi công cụ hoặc quan ngại mới.

Skill .agents/skills/kaiwa-fork-knowledge/SKILL.md và .agents/skills/kaiwa-pdf-knowledge/SKILL.md cùng direct-contract. CLI init/checkpoint/resume/build/validate/extend-scope. build không có --allow-source-issues; validate có. Full đang dở chỉ checkpoint/resume; không fake evidence hoặc thu scope để xanh. needs_review chỉ lỗi nguồn đã mở ảnh, issue đúng page/block/unit; chưa viết dùng draft. Parser hỗ trợ inline/multiline, nhóm dịch đánh số đặt sau đề và nhãn Việt nêu rõ lượt chỉ có trong cột dịch ngoại ngữ. Nó không chứng minh đúng nghĩa/đủ nội dung; không ép sách về template để vượt kiểm tra.

## Git và môi trường

Git dùng chung chat ingest khác; stage exact paths và commit --only. Không add.,reset,push hoặc stage bunpou/PDF/corpus/thay đổi ngoài phạm vi. Commit công cụ và từng sách nghiệm thu riêng. knowledge/source_snapshots giữ bytes theo.gitattributes; giữ CRLF và hardbreak2space khi chỉnh đoạn nhỏ. Whitespace check với core.whitespace=-blank-at-eol,-blank-at-eof,cr-at-eol.

Dùng py -B, PYTHONUTF8=1, import pymupdf as fitz; pdfinfo/Poppler có PATH. Output chỉmd/json/jsonl; ảnh/crop/helperPython ở ignored.cache. exec_command trảsession_id thì poll write_stdin; functions.wait chỉ dùng nếu functions.exec báo running cell. Không chặn wait/sleep quá60giây. Trao đổi tiếng Việt rõ, có khoảng trắng bình thường.

Không final ở trạng thái này; tiếp QA và điều phối tới hết phạm vi được giao.
