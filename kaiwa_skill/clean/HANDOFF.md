# Tiếp quản điều phối clean + PDF → knowledge

Repo D:/CODE/git/kaiwa_skill; cwd môi trường D:/AI_SKILL. Luôn đặt workdir đúng repo.

## Mục tiêu và quyền đã giao

User yêu cầu hoàn tất30PDF/4597trang, không kết thúc lượt chỉ để báo khởi chạy hoặc checkpoint giữa chừng. Giữ root điều phối, giao sách kế sau bàn giao. Không tạo goal/automation/chat mới; chỉ final khi hết phạm vi, user dừng hoặc giới hạn thực sự. Đóng app dừng tính toán, checkpoint trên đĩa cho phép nối lại.

Raw đầy đủ→fork clean; raw chưa có/còn dở→PDF-direct, dùng raw cũ chỉ đọc phụ trợ. Không phải hoàn tất raw rồi mới clean. Không sửa PDF/corpus/claim/snapshot cũ. Bản knowledge đi theo tên sách thật, giữ mạch riêng, mọi ví dụJP+VI, giải thích, bài tập/ô trống/lựa chọn/rolecard/đáp án/phụ lục. Chú từ cuối trang/dạng từ điển là kiến thức, không phải rác footer. Giữ dữ kiện hình đủ để tự làm bài, vai manga theo từng bóng thoại. Không tự giải/đoánJP từ bản dịch/hiện đại hóa nội dung/gán topic hoặc level.

Mỗi sách cần audio.json/audio.md: identity/ấn bản/ISBN/nhãn CD/tape/track/script/URL và dẫn trang/block khi thấy. Actual files not_checked nếu chưa kiểm. Không suy sốđĩa từ mã CD hoặc tự tải. Một số inventory bảy sách cũ chỉ rà giới hạn/unknown, không gọi là full audio audit.

## Runtime và bốn vai sub

Tất cả sub gpt-6-sol/high. Runtime4active tính cả root nên tối đa3sub active, luân phiên một vai điều phối và ba vai worker. Không tạo sub thứ năm/chat riêng để lách. Root giữ Git và QA. Một writer cho một sách.

- /root/knowledge_coordinator: idle sau bàn giao parser/rebase tools; code hiện0.4.7 đã root chốt. Chỉ kích hoạt khi có slot/task kỹ thuật cụ thể.
- /root/clean_keigo: active full96trang `knowledge/わかる！話せる！日本語会話 基本文型88`,16chapter. Đã hết phần đầu/PART1/Warm-up và các nhóm tớiPDF68; đang nhóm cuối câu từ69đến76, sau đó77–96. Chỉ sourceissuesPDF9 (công thức mâu thuẫn) và28 (scan cắt mép/đáy, câu8 mất cuốiA/B). Đã giữ phầnEnglish còn đọc được thànhVI, không dựngJP. Warm-up giữ48câu, đã sửa ôVI: bỏ12ô dư ở seedDrillB, thêm1ô mất ở第3回4, không điền ngữ pháp. Root đã QA front mới/ảnh2–6 và đọcunit14/crop28; pilot7–12 có full QA lịch sử. Chưa root QA toàn Warm-up ảnh18–22 hoặc phần sau. Bảnbook.md vẫn là buildpilot cũ khi full chưa đủ. Worker từng bàn giao tới31 giữa chừng, đã followup tiếp32–96, không coi là hoàn thành.
- /root/clean_namachuukei_sho: active full136trang/25chapter `knowledge/しごとの日本語 ビジネスマナー編`. Đã quaUnit18/PDF119; tiếp120–125 rồi tới136. Sourceissues đã biết: phụđề mờ23/69, mảnh lời dẫn28 kết thúcはずで, thiếu trang in104–105 giữaPDF105/106 thuộcUnit16. Root xác minh23/28–29/105–106, không tự nối chữ. Root QA trọnUnit1/ảnh12–17 và bảng kính ngữ44–45; sửa vai ô5 ở23 thành上司, ô6ちょっとね; đoạn28 so sánhtext tự đủ, excerptJP hỏng ởmeta. Divider73 đã cóunit/anchor sau QA. Các dạngMDT/NTD/MTD và七田/イチダ/市田/シチダ trongUnit15 được giữ đúng từng nơi, không normalize. Unit16: chú thíchEnglish/Chinese106 trùngJP107 đã đốichiếu, không bỏ kiến thức riêng. Cần QA cuối các sơ đồ ghếUnit14 và100đáp án○× ở136 nếu có thể. Audio hiệnunknown theo phạm vi đã đọc.
- /root/clean_namachuukei_chu: active full152trang/26chapter `knowledge/聞いて覚える話し方 日本語生中継 初中級編２`, SHA b5b793947c13… (full trongCOORDINATOR). Front1–6,guide7–11 vàBài1/2 PDF12–27 đãchecked; tiếpBài3 từ28. Bản chính10課PDF12–91,あとがき/tácgiả/xuấtbản92–94,別冊95–96,10scriptchapters97–135,単語表136–141,解答142–151,cover152excluded. Phải giữ cả別冊, không lấy script/đápán điền vào đề. Cover ghi2CD; tracks đã ghi1-2…1-17 theo nguồn, actualfilesnot_checked. Nétbútchì người học ở21/23–27 được loại riêng. Root còn cần QA sớm guide/Bài1; nguồn bằngảnh, textlayer rỗng.

Các mốc là snapshot. Chạy resume/hash thật trước nối việc. Khi tác giả đang ghi, root QA chỉ đọc và gửi sửa; không cùng sửa chapter.

## Đã release phạm vi PDF cung cấp

12sách/1242trang, xem knowledge/README.md vàCOORDINATOR.released_supplied_pdf_scope. Bảy sách đầu501trang đã full independent review; năm bản mới chỉ tác giả full/root mẫu. Full ở đây là PDF được cung cấp; vùng nguồn thiếu/che được ghi riêng, không dựng.

Năm bản mới: roleplay140 commit689603f (root16trang mẫu);本文冊138 commit42b8667 (root10mẫu); Nameraka163 c92c81e (root15mẫu, chỉsource32bịche, allow-source-issues0error/2warn); Wakaru152 0a884d7 (root16mẫu qua pilot+extension, strict0/0);練習冊148 a90b875 (root5mẫu86/89/90/91/92, auditgloss toàn8–147 do tác giả, strict0/0). Không gọi các bản này là full independent semantic review.

本文冊 rebase provenance có audit: mọi138rawpage bytes/PDF không đổi, compiled chỉ thêm4anchor/dòngtrống. Snapshot mới b3ee70a10d8ae410/224b77fb-rebase-756b3046; history _meta/rebase-history/756b3046d61f4fd6a3ec63688854bd1c. Snapshot cũ9a2c9088f812080b/224b77fb giữ nguyên.

Book88 đã migrationraw→direct commit1c2d7c0, history647ff62ba2fa4c548d7c92d5fb545857 bảo toàn4chapter/9unit/ledger/review cũ. Sau đó đãextendfull1–96; không init/reset. clean-state cũ inactive, source.mode=pdf_direct và direct-state là luồng hiện hành.

Ngoài3sách active còn15PDF chờ (12chưa khởi tạo+3rawpartial), tra source_queue. Dự kiến sauManners làDenwa cùngseries, sau88 là125patterns; có thể chọn hợp lý trong hàng đợi theo readiness thật. Không giao trùng/đợi user xác nhận lại.

## Công cụ/QA hiện hành

Version0.4.7, commite974bbf.62test fork+17direct PASS;12book regressionexit0, chỉ2warn nguồn Nameraka32. Kết quả cache `.cache/validator-regression/v047-results.json`; helperread-only `.cache/validator-regression/run.py` chọn các bản đãrelease, không phải phụ thuộc sản phẩm.

Skillraw `.agents/skills/kaiwa-fork-knowledge/SKILL.md`; direct `.agents/skills/kaiwa-pdf-knowledge/SKILL.md`, đọc cảcontract. Direct CLI: init/checkpoint/resume/build/validate/extend-scope. build không có cờ--allow-source-issues; validate có. Full còn dở dùngcheckpoint/resume, không fakeevidence/thu scope đểbuildxanh. needs_review chỉ lỗi nguồn đãmởảnh, issue đúngpage/block/unit; pending/nội dung còn thiếu dùngdraft. Parser hỗ trợ nhiều dòng/inline, nhưng không chứng minh đúng nghĩa/đủ mọi dạng dịch. Đừng sửa sách về template chỉ để vượt parser.

Raw-fork scan nhận pin snapshot qua nguồn gốc ledger và bỏ ledgerinactive củaPDF-direct. rebase-identical-pages chỉ dùng khiPDF/rawpage byte-identical vàcompiled chỉ thêmanchor/dòngtrống, lưuhistory/snapshot mới, không giả review.

## Git và môi trường

Git chung với chat ingest khác; chỉ exact-path stage/diff vàcommit --only. Không git add .,reset,push,stage bunpou/PDF/corpus/production hoặc thay đổi khác ngoài phạm vi. Commit code và từng output nghiệm thu riêng. knowledge/source_snapshots giữ nguyênbytes theo.gitattributes; CRLF và2space hardbreak có chủ đích. Check whitespace bằng `git -c core.whitespace=-blank-at-eol,-blank-at-eof,cr-at-eol diff --cached --check -- <paths>`.

`py -B` +PYTHONUTF8=1; Python cópymupdf/yaml, dùngimportpymupdfasfitz; pdfinfo/Poppler trênPATH. Output chỉmd/json/jsonl; ảnh/crop/helperPython tạm ởignored .cache, khôngcommit. Nếuexec_command trảsession_id phảipoll write_stdin, không làm mấtID bằng chỉin.output. Khôngsleeplonger60s khi đang điều phối.

Khi tiếp quản xemgitstatuscó lọc, tránh in hàng trăm đường dẫn và không stage thay đổi ngoài phạm vi. Không kết thúc turn ở trạng thái này; tiếp QA và điều phối hàng đợi.
