# Tiếp quản điều phối clean và PDF → knowledge

Repo D:/CODE/git/kaiwa_skill; cwd môi trường D:/AI_SKILL. Luôn đặt workdir. Đọc AGENTS.md và hai skill kaiwa-fork-knowledge/kaiwa-pdf-knowledge trước khi tiếp.

## Mục tiêu và quy tắc

Hoàn tất30 PDF/4597 trang. User yêu cầu giữ lượt điều phối hoạt động, giao sách kế ngay sau bàn giao; không final ở launch/checkpoint. Chỉ kết thúc khi hết phạm vi, user dừng hoặc giới hạn thực sự. Không tạo chat/goal/automation. Checkpoint giúp nối sau gián đoạn, không hứa chạy khi đóng app.

Raw đủ→fork; mới/raw dở→PDF-direct, raw cũ chỉ đọc. Không sửa nguồn/corpus/claim/snapshot. Thư mục theo tên thật; giữ mạch riêng, mọi câu Nhật+Việt, ví dụ, giải thích/ngoại lệ, bài tập/ô trống/lựa chọn, rolecard/dữ kiện hình, chú từ, đáp án/phụ lục. Không tóm tắt, tự giải, dựng Nhật từ bản dịch, gán topic/level. Không đẩy giải thích/khung vốn sau model lên trước. Process notes về scan/lọc dịch/hình trang trí để_meta.

Tận dụng bản Việt in sẵn nhưng so từng lượt với Nhật ngay trong lượt biên tập, không thêm vòng dịch toàn sách. Giữ chiều so sánh/phủ định/nhân quả, nghĩa mảnh câu và hạnまでに. Không thêm ngữ cảnh chưa xác nhận. Số đối thoại đếm mục thật, không section×10 hay tên5500. Audio.json/audio.md ghi title/ISBN/edition/CD/track/script/URL có trang/block; không suy số đĩa/track chưa thấy. Files not_checked khi chưa kiểm, không tìm/tải lúc này.

## Phân công hiện hành

User mới nhất đã đổi lại Sol/high. Ba medium_* đều interrupted, KHÔNG resume. Ba worker high cũ đã tiếp quản checkpoint mới nhất và đang viết; không init/reset. 5500 đã được nghiệm thu phạm vi PDF và worker chuyển sang Shadowing trung–cao. Bối cảnh chuyển model được giữ trong COORDINATOR.worker_switch_history; dùng trạng thái hiện tại bên dưới, không dùng snapshot lúc đổi model.

Tất cả sub gpt-6-sol/high. Runtime4 active tính root nên tối đa3 sub active; /root/knowledge_coordinator idle, ba worker viết. Không tạo sub thứ năm. Root giữ Git/QA; mỗi sách một writer, root chỉ đọc/gửi sửa khi đang viết, sửa/chốt sau handoff.

- /root/clean_keigo: **日本人がよく使う 日本語会話お決まり表現180**,full209 trang. Ledger gần nhất171author_checked+53/168needs_review,next174/chapterY. Root đã mở13 trang:1–3/10–12/20–21/53/103/129/208–209; chưa mở168. PDF53 A/A vsAnhA/B đãrootxácnhận;168/mục149 writerbáo tươngtự,cầnrootmở.103 lỗiAnh đãsửa theoNhật rõ,khôngneedsreview. Mini129 chỉsố3,mini161trùngsố36 writercropgiữnguồn,khôngtựsửa thứtự. Sauhandoff giaoPDF200 quickphrases225trang; preflightđãcó tên/2CD/ISBN.
- /root/clean_namachuukei_sho: **初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―**,full227 trang,idremake-5779739d0a4b. Đã xác minh SHA/227 trang và init full, COORD full_pdf_direct_active. Cấu trúc25 chương theo sách: front/công ty1–29;14課30–181 xen総合タスク70–73/104–106/139–141/182–185 vàCan-do107–111/186–191;敬語192;index/奥付193–205;解答206–215;script216–227. Worker đang front và課1, sẽ gửi phần checked cho root QA. Root đã mở1/226/227,ghi preflight tám sách ởreviews/next-sources-root-preflight.md. Hai trang cuối vẫn nghe bài12–14,giữ đoạn đọc và câu hỏi/lựa chọn; bỏfooterJLPTMOGI. Bìa nói audio trênweb; ghi URL/mã/track theo nguồn,không tìm/tải. Business30h đã chốt, không writer ghi lại.
- /root/clean_namachuukei_chu: **すぐに使える 接客日本語会話大特訓［英語版］決まり文句700**,full225 trang,idconversational-customer-service-japanese-intensive-trai-2ec8b7129cb8. Init full12 chương: front1–9;序章10–14;8chương ngành15–218;丁寧表現早見表219–223;colophon224–225.92Unit theo guide. Cột English prompt là bài luyện, phải chuyển Việt và giữ trước phần Nhật/tips/gloss; không xóa vì tưởng dịch lặp, không đổi phương phápCD English→pause→JP thành tiếngViệt. Đã yêu cầu gửi Unit đầu16–17 checked trang cho root QA rồi tự tiếp. Root đã mở1/224/225 trước đó (3trang). ISBN9784863923126,Jリサーチ,2016-10-10first/2019-04-10second;2CD+download ghi bìa,URL chưa thấy,actualfilesnot_checked. Shadowing168 đã chốt, không writer ghi lại.


Đây là snapshot; dùng resume/hash thật. Còn6 PDF chưa giao. Khi bàn giao, tiếp phân công ngay, không hỏi lại quyền.

## Đã chốt

Mới nhất **Shadowing中～上級編** bảnIndonesia–Thai–Việt168 trang/10 chương/93unit,commit0feafae,BookSHAcaddf9c8beada3cb90b0935557653f4bc95d7995078046326e5eb13bdd53c6e7. Root36 trang mẫu;232 thoại ngắn(38/39/39/23/42/30/21)+8section dài.167pages/9chapters/92units checked+1needs_review doA/B/A/A70;khôngpending/draft/stale. Rootvalidateallow0/2 chỉ cùngsourceissue70; giữ cảnh báo trong bản đọc.2CD/DISK1labels02–33,DISK2labels02–31,62cặp đĩa-track,file not_checked. Root đã sửa3時に ở150khôngchoJPkhớpVI;front/hướngdẫn vàcácmẫutheobáocáo đãđọclại. Root sở hữu,writer sang接客700225 trang.

Mới nhất **にほんごで働く！ビジネス日本語30時間**,181 trang/15 chương/171 unit,commit62fd98b,BookSHA82bc042a6dfeb1fbadb47d132bdfbcfec9934c76ea908a293f08355b1a4770ce. Root40 trang mẫu; strictvalidate0/0;181pages/15chapters/171units author_checked,khôngpending/draft/stale/needs_review. Giữ đáp án/script/index và biệt冊162–181; writer audit395 hàng index,root chỉ mẫu.1CD/57labels01–57,script15→145/28→147/37→149/44→151,file not_checked. Root sở hữu, writer đã giao Roleplay sơ–trung227. Chi tiết trong_meta/coordinator-review vàclean/reviews/business30-root-sampled.md.

Mới nhất **5500 câu...hằng ngày**,136 trang/9ch/141unit,commit6f689ed. Root17pages1–8/10/16/38/66/99/128/132/135/136; đọc toànfront vàVậnchuyển nhưngnguồn chỉQAmẫu.76checked/60needs_review,66sourceissues/25pagescắtche;rootvalidateallow0/132. Khôngfullindependentsemanticreview, khôngcoinguồnNhậtchuẩntoànbộ. Đã sửaViệt sai/headingvậnchuyểnII-IV/lặp貸切131, đủ33glossrowscuối. Authorđếm1188câumẫuđánh số,1697JP/VIlabel+2inline, khôngsuy5500từtitle. CDMP3 source1/2/5,khôngtrack/sốdisc/filethật. BookSHA9a9b6267c45252b07bc179efef6c7458cbdc1bb473fe7df04e3b93be66af2152. RootgiữQA/Git, writerđãShadowing168. Cataloghelperignored .cache/root-live-qa/sync_catalog.py --release BOOKDIR COMMIT --assign WORKER BOOKID sauquyếtđịnhQAexplicit,khôngtựnghiệmthu. Scriptverifyreviewhash/errors,refreshaudio/README/COORD;STATUS/HANDOFF cậpnhậttay.

Mới thêm **Denwa** full162/38ch/259unit commit49b0926,root27 trang gồm trọnUnit1/17/35; source83 Note⑧ dở,0/2allow;70CDlabels,file not_checked. Root đã sửa hạn ngàymai, trả mô tả tôngABC xuống script/đápán thay lộởđề Unit1/35; tácgiảràUnit3. **発展文型125** full225/30ch/143unit commit89f4c0f,root29 trang+toànindex125dòng;125model cóluyện,mạchđãtrảvềnguồn,119ba nhánh khung giữrõ. Source120 thiếuA NhậtgiữViệtriêng,0/2allow;99CDlabels,file not_checked. BookSHA71e9ba82546f8db41e3be73583da56dd057cccf7b785bf1ca014cf694fa9c5f1. Báocáo trong_meta/coordinator-review, root sởhữu, workersđãsáchkế.

21 sách/2643 trang; danh sách/commit trong COORDINATOR.released_supplied_pdf_scope và knowledge/README. Bảy bản đầu501 trang full independent review; mười bốn bản sau author full/root sampled. Full là PDF được cung cấp, không dựng trang thiếu.

Shadowing **初～中級編** bản Indonesia–Thai–Việt145 trang, dca0eff: root34 trang1–4/8–9/20–21/23/25–26/37–38/43–45/63–64/81–82/107–114/131–134/138–139. So trọn Unit1sections1/7/10, Unit2/3section cuối, Unit5sections1/2/7,cột③; front/guide đọc toàn, nguồn QA mẫu.42section/411hội thoại/950JP+950VI.420 từ bàn giao đã đính chính vì section cuốiUnit2 chỉ5/Unit3 chỉ6; không thiếu9thoại. Root crop2/139 xác nhận **初～中級編**, lần đầu ảnh nhỏ đọc nhầm・; đã sửa folder/front/title/audio, lưu lịch sử. Colophon〜 là đúng. Validate0/0;42labels02–43, số đĩa chưa xác nhận, filesnot_checked. BookSHA a7434c89ff818087a03a1941d0191a0ed77b73452f6fad63cd711f46d5d1dc37. Root sở hữu, worker đã sách kế.

Nama2 1e29c64 full152/26ch/227unit,root27 trang; nguồn83/119 và9placeholderwarnings đã so nguồn,0/13allow;2CD/82labels. Manners136 nguồn23/28/69/105/106, thiếu trang in104–105;88patterns96 nguồn9/28;Nameraka163 nguồn32 bị che. Giữ source-warning trong bản đọc, không đoán. BJT本文冊 có rebase byte-identical;88 có migration/history1c2d7c0, không reset/init hoặc sửa pin né stale. Chi tiết từng_meta/coordinator-review và clean/reviews.

## Công cụ và môi trường

0.4.10,80 test fork+17 direct PASS. Regression18 bản đã chốt0/33, cache .cache/validator-regression/v0410-18-results.json; cảnhbáonguồn+9placeholderNama2 đãkiểm. Không lặp rộng khi không đổi công cụ/quan ngại. Skill mới thêm so Việt in sẵn và giữ miêu tả ngữ điệu sau đề nghe, không có code đổi.

CLI direct init/checkpoint/resume/build/validate/extend-scope; build không cóallow-source-issues, validate có. Scopefull dở dùng checkpoint/resume, không fake evidence/thu scope. needs_review chỉ lỗi nguồn thực đúngpage/block/unit. Parser không chứng minh nghĩa/đủ học liệu; không ép layout đểqua. Builder tạo book/search, không sửa book.md tay.

Git dùng chung ingest: exactpaths, commit --only; không add.,reset,push hoặc stage PDF/corpus/bunpou/production. Chỉroot Git. GiữCRLF/hardbreakspaces khi chỉnh nhỏ; check core.whitespace=-blank-at-eol,-blank-at-eof,cr-at-eol. Output chỉmd/json/jsonl; renders/helpers ở ignored.cache. Dùng py -B/PYTHONUTF8=1/pymupdf as fitz. exec_command cósession_id thì poll write_stdin; functions.wait chỉ khi functions.exec báo runningcell. Không wait/sleep chặn quá60giây. Trao đổi tiếng Việt có khoảng trắng rõ.

Không final trạng thái này; tiếp QA và điều phối tới hết phạm vi.
