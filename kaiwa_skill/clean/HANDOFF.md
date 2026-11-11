# Tiếp quản điều phối clean và PDF → knowledge

Repo D:/CODE/git/kaiwa_skill; cwd môi trường D:/AI_SKILL. Luôn đặt workdir. Đọc AGENTS.md và hai skill kaiwa-fork-knowledge/kaiwa-pdf-knowledge trước khi tiếp.

## Mục tiêu và quy tắc

Hoàn tất30 PDF/4597 trang. User yêu cầu giữ lượt điều phối hoạt động, giao sách kế ngay sau bàn giao; không final ở launch/checkpoint. Chỉ kết thúc khi hết phạm vi, user dừng hoặc giới hạn thực sự. Không tạo chat/goal/automation. Checkpoint giúp nối sau gián đoạn, không hứa chạy khi đóng app.

Raw đủ→fork; mới/raw dở→PDF-direct, raw cũ chỉ đọc. Không sửa nguồn/corpus/claim/snapshot. Thư mục theo tên thật; giữ mạch riêng, mọi câu Nhật+Việt, ví dụ, giải thích/ngoại lệ, bài tập/ô trống/lựa chọn, rolecard/dữ kiện hình, chú từ, đáp án/phụ lục. Không tóm tắt, tự giải, dựng Nhật từ bản dịch, gán topic/level. Không đẩy giải thích/khung vốn sau model lên trước. Process notes về scan/lọc dịch/hình trang trí để_meta.

Tận dụng bản Việt in sẵn nhưng so từng lượt với Nhật ngay trong lượt biên tập, không thêm vòng dịch toàn sách. Giữ chiều so sánh/phủ định/nhân quả, nghĩa mảnh câu và hạnまでに. Không thêm ngữ cảnh chưa xác nhận. Số đối thoại đếm mục thật, không section×10 hay tên5500. Audio.json/audio.md ghi title/ISBN/edition/CD/track/script/URL có trang/block; không suy số đĩa/track chưa thấy. Files not_checked khi chưa kiểm, không tìm/tải lúc này.

## Phân công hiện hành

Tất cả sub gpt-6-sol/high. Runtime4 active tính root nên tối đa3 sub active; /root/knowledge_coordinator idle, ba worker viết. Không tạo sub thứ năm. Root giữ Git/QA; mỗi sách một writer, root chỉ đọc/gửi sửa khi đang viết, sửa/chốt sau handoff.

- /root/clean_keigo: 発展文型125 full225 trang/30 chương. Đã viết tới125 và index125 dòng220–223. Đang evidence/backmatter224–225 và self-audit. Root mở29 trang1/2/8/10–16/18–23/35/51/52/120/208/210/211/218/220–224, đã so toàn index. Source120/unit67 thiếu lượt A Nhật/romaji nhưng còn cột Anh–Trung, giữ Việt riêng/needs_review. Đã sửa guide1–2 thoại,ただ16,hạn35,dẫn具合51,彼女52. Root yêu cầu trả mạch model→giải thích→khung→luyện và ba nhánh công thức119; worker đang sửa trước build. Index123 không tự thêm “chỉ”,115 “người”,114 “đi” nếu chưa có căn cứ. Sau handoff đã cho phép tiếp full209 trang180-common-native-japanese-figures-of-speech-in-regular-conversation-9784863923256-4863923256_compress.pdf; id/SHA trong source_queue. Đổi assignment khi bắt đầu, xác minh title thật.
- /root/clean_namachuukei_sho: 電話応対 基礎編 full162/38chapter, đã tới147, tiếp148 Unit33–35 và hậu sách160–162, rồi audit/build. Root mở23 trang1/5/11–18/20–23/45/49/51/83–87/160; so trọn Unit1/17 và intro mẫu. Source83 Note⑧ cắt tạiため、,84 làUnit17, không bù. Giữ các khác biệt in山本/山川45,30/60phone,小森/子森117/119. Đã sửa notes thiếu ví dụ, giọng thấp/nhanh, monologue bắt đầu trong1phút/kết thúc khoảng2phút; bỏ boilerplate. Sau handoff đã cho phép full181 trang book/BJT/にほんごで働く!ビジネス日本語30時間.pdf, id30-f497459c2a83/SHA trongqueue. Root QA/Git Denwa song song.
- /root/clean_namachuukei_chu: **5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày**, full136 trang spread/9chapter. Init xong/front1–6 checked;p6 đã có đầu chapter01 nhưng chapter01 chưa checked. Title thật dùng **hằng**; phụ đề生活のために日本語会話文句5500, Tri Thức Việt/Sato ToyodaCD/Hồng Đức,tái bản1,ISBN9786048657574,quý3/2015. Ranh giới38/66/99/112/122/127/136 chứa hai phần trên cùngPDF, map block riêng. TOC12p190/13p184/14p187 bất nhất, giữ dữ liệu và chapter theo trang thật. Raw100verified/36needs_review chỉ đọc, không init raw. Root cần QA chương đầu sớm. SHA/id/path trong COORDINATOR.

Đây là snapshot; dùng resume/hash thật. Còn11 PDF chưa giao. Khi bàn giao, tiếp phân công ngay, không hỏi lại quyền.

## Đã chốt

16 sách/1771 trang; danh sách/commit trong COORDINATOR.released_supplied_pdf_scope và knowledge/README. Bảy bản đầu501 trang full independent review; chín bản sau author full/root sampled. Full là PDF được cung cấp, không dựng trang thiếu.

Shadowing **初～中級編** bản Indonesia–Thai–Việt145 trang, dca0eff: root34 trang1–4/8–9/20–21/23/25–26/37–38/43–45/63–64/81–82/107–114/131–134/138–139. So trọn Unit1sections1/7/10, Unit2/3section cuối, Unit5sections1/2/7,cột③; front/guide đọc toàn, nguồn QA mẫu.42section/411hội thoại/950JP+950VI.420 từ bàn giao đã đính chính vì section cuốiUnit2 chỉ5/Unit3 chỉ6; không thiếu9thoại. Root crop2/139 xác nhận **初～中級編**, lần đầu ảnh nhỏ đọc nhầm・; đã sửa folder/front/title/audio, lưu lịch sử. Colophon〜 là đúng. Validate0/0;42labels02–43, số đĩa chưa xác nhận, filesnot_checked. BookSHA a7434c89ff818087a03a1941d0191a0ed77b73452f6fad63cd711f46d5d1dc37. Root sở hữu, worker đã sách kế.

Nama2 1e29c64 full152/26ch/227unit,root27 trang; nguồn83/119 và9placeholderwarnings đã so nguồn,0/13allow;2CD/82labels. Manners136 nguồn23/28/69/105/106, thiếu trang in104–105;88patterns96 nguồn9/28;Nameraka163 nguồn32 bị che. Giữ source-warning trong bản đọc, không đoán. BJT本文冊 có rebase byte-identical;88 có migration/history1c2d7c0, không reset/init hoặc sửa pin né stale. Chi tiết từng_meta/coordinator-review và clean/reviews.

## Công cụ và môi trường

0.4.10,80 test fork+17 direct PASS. Regression15 bản trước0/29; Shadowing mới validate riêng0/0. Không lặp rộng khi không đổi công cụ/quan ngại. Skill mới thêm so Việt in sẵn, không có code đổi.

CLI direct init/checkpoint/resume/build/validate/extend-scope; build không cóallow-source-issues, validate có. Scopefull dở dùng checkpoint/resume, không fake evidence/thu scope. needs_review chỉ lỗi nguồn thực đúngpage/block/unit. Parser không chứng minh nghĩa/đủ học liệu; không ép layout đểqua. Builder tạo book/search, không sửa book.md tay.

Git dùng chung ingest: exactpaths, commit --only; không add.,reset,push hoặc stage PDF/corpus/bunpou/production. Chỉroot Git. GiữCRLF/hardbreakspaces khi chỉnh nhỏ; check core.whitespace=-blank-at-eol,-blank-at-eof,cr-at-eol. Output chỉmd/json/jsonl; renders/helpers ở ignored.cache. Dùng py -B/PYTHONUTF8=1/pymupdf as fitz. exec_command cósession_id thì poll write_stdin; functions.wait chỉ khi functions.exec báo runningcell. Không wait/sleep chặn quá60giây. Trao đổi tiếng Việt có khoảng trắng rõ.

Không final trạng thái này; tiếp QA và điều phối tới hết phạm vi.
