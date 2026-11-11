# Tiếp quản điều phối clean và PDF → knowledge

Repo D:/CODE/git/kaiwa_skill; cwd môi trường D:/AI_SKILL. Luôn đặt workdir. Đọc AGENTS.md và hai skill kaiwa-fork-knowledge/kaiwa-pdf-knowledge trước khi tiếp.

## Mục tiêu và quy tắc

Hoàn tất30 PDF/4597 trang. User yêu cầu giữ lượt điều phối hoạt động, giao sách kế ngay sau bàn giao; không final ở launch/checkpoint. Chỉ kết thúc khi hết phạm vi, user dừng hoặc giới hạn thực sự. Không tạo chat/goal/automation. Checkpoint giúp nối sau gián đoạn, không hứa chạy khi đóng app.

Raw đủ→fork; mới/raw dở→PDF-direct, raw cũ chỉ đọc. Không sửa nguồn/corpus/claim/snapshot. Thư mục theo tên thật; giữ mạch riêng, mọi câu Nhật+Việt, ví dụ, giải thích/ngoại lệ, bài tập/ô trống/lựa chọn, rolecard/dữ kiện hình, chú từ, đáp án/phụ lục. Không tóm tắt, tự giải, dựng Nhật từ bản dịch, gán topic/level. Không đẩy giải thích/khung vốn sau model lên trước. Process notes về scan/lọc dịch/hình trang trí để_meta.

Tận dụng bản Việt in sẵn nhưng so từng lượt với Nhật ngay trong lượt biên tập, không thêm vòng dịch toàn sách. Giữ chiều so sánh/phủ định/nhân quả, nghĩa mảnh câu và hạnまでに. Không thêm ngữ cảnh chưa xác nhận. Số đối thoại đếm mục thật, không section×10 hay tên5500. Audio.json/audio.md ghi title/ISBN/edition/CD/track/script/URL có trang/block; không suy số đĩa/track chưa thấy. Files not_checked khi chưa kiểm, không tìm/tải lúc này.

## Phân công hiện hành

User mới nhất đã đổi lại Sol/high. Ba medium_* đều interrupted, KHÔNG resume. Ba worker high cũ đã tiếp quản checkpoint mới nhất và đang viết; không init/reset. 5500 đã được nghiệm thu phạm vi PDF và worker chuyển sang Shadowing trung–cao. Bối cảnh chuyển model được giữ trong COORDINATOR.worker_switch_history; dùng trạng thái hiện tại bên dưới, không dùng snapshot lúc đổi model.

Tất cả sub gpt-6-sol/high. Runtime4 active tính root nên tối đa3 sub active; /root/knowledge_coordinator idle, ba worker viết. Không tạo sub thứ năm. Root giữ Git/QA; mỗi sách một writer, root chỉ đọc/gửi sửa khi đang viết, sửa/chốt sau handoff.

- /root/clean_keigo: **日本人がよく使う 日本語会話お決まり表現180**, full 209 trang. Snapshot ledger gần nhất: 137 author_checked + PDF53 needs_review, 71 pending; tiếp Section T trở đi. Root đã mở 13 trang: 1–3/10–12/20–21/53/103/129/208–209. PDF53 thật có vai A/A so với Anh A/B; giữ vấn đề. PDF103 chỉ sai bản Anh, đã dịch theo Nhật rõ và chuyển author_checked. Mini-column129 chỉ in số3, không suy29. Báo cáo `reviews/okimari180-root-sampled.md`. Sau handoff giao PDF200 quick phrases 225 trang, ID và identity trong `reviews/next-sources-root-preflight.md`.
- /root/clean_namachuukei_sho: **にほんごで働く！ビジネス日本語30時間**, full 181 trang/15 chapter. Ledger gần nhất 148 author_checked; 8 bài chính và bảng công ty/kính ngữ đã xong, đang script/đáp án143–153, sau đó index154–159, identity160/ad161 và biệt sách162–181. Root đã mở34 trang; chi tiết `reviews/business30-root-sampled.md`. Đã sửa dịch thoại tóm tắt, trọng âm/kana, giữ hai tầng ví dụ thường→kính ngữ và sửa quan hệ hình taxi/thang máy62. So nội bộ chữ kana của bảng từ/bảng dấu cả8 bài chỉ phát hiện thêm 外出先96, đã sửa và root đọc lại. PDF143 mới mở để chuẩn bị; chưa so output đáp án. Một CD xác nhận4/6, inventory đếnCD57, file chưa kiểm. Sau handoff giao Roleplay初中227 trang; chú ý hai trang cuối vẫn học liệu, xem preflight.
- /root/clean_namachuukei_chu: **シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版**, full168 trang. Front và Unit1–3 qua PDF80 đã viết; tiếp Unit4 81–94. Unit1 có38 hội thoại/11 giải thích, Unit2 có39/12, Unit3 có39/8 theo writer. Root đã mở31 trang; báo cáo `reviews/shadow-chujo-root-sampled.md` ghi chính xác phạm vi, hai đợt sửa hướng dẫn và sửa nhỏ Unit1/2 đã đọc lại. Vừa mở70/71, xác nhận thoại S2 số6 thực in A/B/A/A trong Nhật lẫn dịch; đã yêu cầu writer issue đúng70/unit, needs_review page/unit/chapter03 và cảnh báo ngắn, chưa tự sửa vai. Hai CD DISK1U1–4/DISK2U5–8; files chưa kiểm. Sau handoff dự kiến giao 接客700225 trang, preflight đã có tên/ISBN/ấn bản/2CD.


Đây là snapshot; dùng resume/hash thật. Còn8 PDF chưa giao. Khi bàn giao, tiếp phân công ngay, không hỏi lại quyền.

## Đã chốt

Mới nhất **5500 câu...hằng ngày**,136 trang/9ch/141unit,commit6f689ed. Root17pages1–8/10/16/38/66/99/128/132/135/136; đọc toànfront vàVậnchuyển nhưngnguồn chỉQAmẫu.76checked/60needs_review,66sourceissues/25pagescắtche;rootvalidateallow0/132. Khôngfullindependentsemanticreview, khôngcoinguồnNhậtchuẩntoànbộ. Đã sửaViệt sai/headingvậnchuyểnII-IV/lặp貸切131, đủ33glossrowscuối. Authorđếm1188câumẫuđánh số,1697JP/VIlabel+2inline, khôngsuy5500từtitle. CDMP3 source1/2/5,khôngtrack/sốdisc/filethật. BookSHA9a9b6267c45252b07bc179efef6c7458cbdc1bb473fe7df04e3b93be66af2152. RootgiữQA/Git, writerđãShadowing168. Cataloghelperignored .cache/root-live-qa/sync_catalog.py --release BOOKDIR COMMIT --assign WORKER BOOKID sauquyếtđịnhQAexplicit,khôngtựnghiệmthu. Scriptverifyreviewhash/errors,refreshaudio/README/COORD;STATUS/HANDOFF cậpnhậttay.

Mới thêm **Denwa** full162/38ch/259unit commit49b0926,root27 trang gồm trọnUnit1/17/35; source83 Note⑧ dở,0/2allow;70CDlabels,file not_checked. Root đã sửa hạn ngàymai, trả mô tả tôngABC xuống script/đápán thay lộởđề Unit1/35; tácgiảràUnit3. **発展文型125** full225/30ch/143unit commit89f4c0f,root29 trang+toànindex125dòng;125model cóluyện,mạchđãtrảvềnguồn,119ba nhánh khung giữrõ. Source120 thiếuA NhậtgiữViệtriêng,0/2allow;99CDlabels,file not_checked. BookSHA71e9ba82546f8db41e3be73583da56dd057cccf7b785bf1ca014cf694fa9c5f1. Báocáo trong_meta/coordinator-review, root sởhữu, workersđãsáchkế.

19 sách/2294 trang; danh sách/commit trong COORDINATOR.released_supplied_pdf_scope và knowledge/README. Bảy bản đầu501 trang full independent review; mười hai bản sau author full/root sampled. Full là PDF được cung cấp, không dựng trang thiếu.

Shadowing **初～中級編** bản Indonesia–Thai–Việt145 trang, dca0eff: root34 trang1–4/8–9/20–21/23/25–26/37–38/43–45/63–64/81–82/107–114/131–134/138–139. So trọn Unit1sections1/7/10, Unit2/3section cuối, Unit5sections1/2/7,cột③; front/guide đọc toàn, nguồn QA mẫu.42section/411hội thoại/950JP+950VI.420 từ bàn giao đã đính chính vì section cuốiUnit2 chỉ5/Unit3 chỉ6; không thiếu9thoại. Root crop2/139 xác nhận **初～中級編**, lần đầu ảnh nhỏ đọc nhầm・; đã sửa folder/front/title/audio, lưu lịch sử. Colophon〜 là đúng. Validate0/0;42labels02–43, số đĩa chưa xác nhận, filesnot_checked. BookSHA a7434c89ff818087a03a1941d0191a0ed77b73452f6fad63cd711f46d5d1dc37. Root sở hữu, worker đã sách kế.

Nama2 1e29c64 full152/26ch/227unit,root27 trang; nguồn83/119 và9placeholderwarnings đã so nguồn,0/13allow;2CD/82labels. Manners136 nguồn23/28/69/105/106, thiếu trang in104–105;88patterns96 nguồn9/28;Nameraka163 nguồn32 bị che. Giữ source-warning trong bản đọc, không đoán. BJT本文冊 có rebase byte-identical;88 có migration/history1c2d7c0, không reset/init hoặc sửa pin né stale. Chi tiết từng_meta/coordinator-review và clean/reviews.

## Công cụ và môi trường

0.4.10,80 test fork+17 direct PASS. Regression18 bản đã chốt0/33, cache .cache/validator-regression/v0410-18-results.json; cảnhbáonguồn+9placeholderNama2 đãkiểm. Không lặp rộng khi không đổi công cụ/quan ngại. Skill mới thêm so Việt in sẵn và giữ miêu tả ngữ điệu sau đề nghe, không có code đổi.

CLI direct init/checkpoint/resume/build/validate/extend-scope; build không cóallow-source-issues, validate có. Scopefull dở dùng checkpoint/resume, không fake evidence/thu scope. needs_review chỉ lỗi nguồn thực đúngpage/block/unit. Parser không chứng minh nghĩa/đủ học liệu; không ép layout đểqua. Builder tạo book/search, không sửa book.md tay.

Git dùng chung ingest: exactpaths, commit --only; không add.,reset,push hoặc stage PDF/corpus/bunpou/production. Chỉroot Git. GiữCRLF/hardbreakspaces khi chỉnh nhỏ; check core.whitespace=-blank-at-eol,-blank-at-eof,cr-at-eol. Output chỉmd/json/jsonl; renders/helpers ở ignored.cache. Dùng py -B/PYTHONUTF8=1/pymupdf as fitz. exec_command cósession_id thì poll write_stdin; functions.wait chỉ khi functions.exec báo runningcell. Không wait/sleep chặn quá60giây. Trao đổi tiếng Việt có khoảng trắng rõ.

Không final trạng thái này; tiếp QA và điều phối tới hết phạm vi.
