# Tiếp quản điều phối clean và PDF → knowledge

Repo D:/CODE/git/kaiwa_skill; cwd môi trường D:/AI_SKILL. Luôn đặt workdir. Đọc AGENTS.md và hai skill kaiwa-fork-knowledge/kaiwa-pdf-knowledge trước khi tiếp.

## Mục tiêu và quy tắc

Hoàn tất30 PDF/4597 trang. User yêu cầu giữ lượt điều phối hoạt động, giao sách kế ngay sau bàn giao; không final ở launch/checkpoint. Chỉ kết thúc khi hết phạm vi, user dừng hoặc giới hạn thực sự. Không tạo chat/goal/automation. Checkpoint giúp nối sau gián đoạn, không hứa chạy khi đóng app.

Raw đủ→fork; mới/raw dở→PDF-direct, raw cũ chỉ đọc. Không sửa nguồn/corpus/claim/snapshot. Thư mục theo tên thật; giữ mạch riêng, mọi câu Nhật+Việt, ví dụ, giải thích/ngoại lệ, bài tập/ô trống/lựa chọn, rolecard/dữ kiện hình, chú từ, đáp án/phụ lục. Không tóm tắt, tự giải, dựng Nhật từ bản dịch, gán topic/level. Không đẩy giải thích/khung vốn sau model lên trước. Process notes về scan/lọc dịch/hình trang trí để_meta.

Tận dụng bản Việt in sẵn nhưng so từng lượt với Nhật ngay trong lượt biên tập, không thêm vòng dịch toàn sách. Giữ chiều so sánh/phủ định/nhân quả, nghĩa mảnh câu và hạnまでに. Không thêm ngữ cảnh chưa xác nhận. Số đối thoại đếm mục thật, không section×10 hay tên5500. Audio.json/audio.md ghi title/ISBN/edition/CD/track/script/URL có trang/block; không suy số đĩa/track chưa thấy. Files not_checked khi chưa kiểm, không tìm/tải lúc này.

## Phân công hiện hành

User mới nhất đã đổi lại Sol/high. Ba medium_* đều interrupted, KHÔNG resume; ba high cũ clean_keigo/clean_namachuukei_sho/clean_namachuukei_chu đang tiếp file mới nhất. Snapshot lúc đổi lại:180 tới62 (61checked+53issue), Business30h63checked/64–65draft/66+pending;5500 có nội dung/evidence128–135 chưacheckpoint,136chưa xong. Phải chạy resume và đọc draft trước nối, không init/reset/ghi đè phần medium đã làm. Sách kế của clean_namachuukei_chu sau handoff vẫn Shadowing中上168, idbook-f4bcdf991dba. Source18053 A/A vsEnglishA/B đãroot xácnhận. Root mới mở5500 thêm128/132/135,tổng17pages, đã gửi các sửa nghĩa cho writer.

Tất cả sub gpt-6-sol/high. Runtime4 active tính root nên tối đa3 sub active; /root/knowledge_coordinator idle, ba worker viết. Không tạo sub thứ năm. Root giữ Git/QA; mỗi sách một writer, root chỉ đọc/gửi sửa khi đang viết, sửa/chốt sau handoff.

- /root/clean_keigo: **日本人がよく使う 日本語会話お決まり表現180**, full209 trang. Đã init, đang front1–12 rồi序章13–18,26 sectionA–Z20–199, Englishindex200–204, Japaneseindex205–207,colophon/back208–209. Nguồn có mạch title+explanation→Listen & Speak→mini-column, giữ mạch này, KHÔNG áp thứ tự125. Tác giả清ルミ, Jリサーチ,ISBN9784863923256,2017-01-10 lần1/2018-04-10 lần2 theo1/208. CD付+音声ダウンロード付,12 nói thu title vàListen&Speak Nhật; ghi URL/mã in nếu có, không tìm/tải. Root chưa QA sách này; ưu tiên front và kiểu bài/mini-column.
- /root/clean_namachuukei_sho: **にほんごで働く！ビジネス日本語30時間**, full181 trang/15chapter. Front1–10 checked, tiếp Bài1 11–28. Main8課11–139;会社ことば140;敬語表141–142;解答script143–153;索引154–159;colophon160/ad161;別冊162–181. Root mở10 trang1/3–10/160, so trọn lời đầu/hai guides/TOC. Đã yêu cầu nghĩaViệt TOC và chuyển©/addressEnglishra_meta; chưa đọc lại sửa. Source4/6 xácnhận1CD; ISBN9784883194902,宮崎道子・郷司幸子,3A,2009-03-10 lần1/2017-05-26 lần10. Cần QA sớm bài chính, dữ kiện hình/bài luyện/chú từ và đápán sau.
- /root/clean_namachuukei_chu: **シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版**, full168 trang, đã init. PDFbook/Shadowing/シャドウイング 日本語を話そう中_上級.pdf, idbook-f4bcdf991dba, SHA trongqueue. Front1–18,p2trắng;Unit1 19–38,U2 39–60,U3 61–80,U4 81–94,U5 95–118,U6 119–134,U7 135–148,U8 149–167,colophon168. U1–7 cóintro/bảngbiểuđạt,section1trung/section2cao,解説;U8 tám bài thoại dài/speech150–164,giảithích166–167. CóViệtinsẵn,soJP từnglượt, khôngtóm lời dài. くろしお,2014-06-18 lần1,ISBN9784874246252 theo168.2CD:DISK1Unit1–4,DISK2Unit5–8;ghi từngnhãn/pagemapping,khôngđoántrack1,filesnotchecked. Root chưaQA sách này, ưu tiênfront/chươngđầu khiwriterbáo. 5500đãhandoffroot, khôngwriterquaylạighi.


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
