# Tiếp quản điều phối clean và PDF → knowledge

Repo D:/CODE/git/kaiwa_skill; cwd môi trường D:/AI_SKILL. Luôn đặt workdir. Đọc AGENTS.md và hai skill kaiwa-fork-knowledge/kaiwa-pdf-knowledge trước khi tiếp.

## Mục tiêu và quy tắc

Hoàn tất30 PDF/4597 trang. User yêu cầu giữ lượt điều phối hoạt động, giao sách kế ngay sau bàn giao; không final ở launch/checkpoint. Chỉ kết thúc khi hết phạm vi, user dừng hoặc giới hạn thực sự. Không tạo chat/goal/automation. Checkpoint giúp nối sau gián đoạn, không hứa chạy khi đóng app.

Raw đủ→fork; mới/raw dở→PDF-direct, raw cũ chỉ đọc. Không sửa nguồn/corpus/claim/snapshot. Thư mục theo tên thật; giữ mạch riêng, mọi câu Nhật+Việt, ví dụ, giải thích/ngoại lệ, bài tập/ô trống/lựa chọn, rolecard/dữ kiện hình, chú từ, đáp án/phụ lục. Không tóm tắt, tự giải, dựng Nhật từ bản dịch, gán topic/level. Không đẩy giải thích/khung vốn sau model lên trước. Process notes về scan/lọc dịch/hình trang trí để_meta.

Tận dụng bản Việt in sẵn nhưng so từng lượt với Nhật ngay trong lượt biên tập, không thêm vòng dịch toàn sách. Giữ chiều so sánh/phủ định/nhân quả, nghĩa mảnh câu và hạnまでに. Không thêm ngữ cảnh chưa xác nhận. Số đối thoại đếm mục thật, không section×10 hay tên5500. Audio.json/audio.md ghi title/ISBN/edition/CD/track/script/URL có trang/block; không suy số đĩa/track chưa thấy. Files not_checked khi chưa kiểm, không tìm/tải lúc này.

## Phân công hiện hành

User mới nhất đã đổi lại Sol/high. Ba medium_* đều interrupted, KHÔNG resume. Ba worker high cũ đã tiếp quản checkpoint mới nhất và đang viết; không init/reset. 5500 đã được nghiệm thu phạm vi PDF và worker chuyển sang Shadowing trung–cao. Bối cảnh chuyển model được giữ trong COORDINATOR.worker_switch_history; dùng trạng thái hiện tại bên dưới, không dùng snapshot lúc đổi model.

Tất cả sub gpt-6-sol/high. Runtime4 active tính root nên tối đa3 sub active; /root/knowledge_coordinator idle, ba worker viết. Không tạo sub thứ năm. Root giữ Git/QA; mỗi sách một writer, root chỉ đọc/gửi sửa khi đang viết, sửa/chốt sau handoff.

- /root/clean_keigo: **超ミニフレーズ 発展210**,233trang, SHA2fdf1586c2e2673f6b27b93fcf3c04c8584567fdd3c2258bcdd0033743de2b05. Main đến108/PDF123;TOC4–9draft. Root17nguồn:1/12–14/16–25/75/232–233. Full10mục đầu vàmục60 đãso;いや18sửađúng.75nhãnA/A sourceissuehẹp. Audio độc lập đủ210occurrences/198unique, report.cache/root-live-qa/mini210-audio-independent.json(fe3f28b86dc17164136c0dcd1ed2c984bc42ea72552be8a0b8d80933e27ff161),chuQAallcrops. Guide12/13 cóhaioccurrenceslặpmã;khôngsuytừhead. Xemreportthật,khôngdùng câusnapshot này suy thêm.
- /root/clean_namachuukei_sho: **オノマトペ基本表現180**,220trang, SHA458b548674d123f0e35c8df67395c3e569eab80ffa6e9c4a7848a8489547d439. Full8chương;Part1/2checked,Part3draftđến111,tiếp112–163rồiPart4 164–209/index210–216/cuối217–220. Root31nguồn:1–24/38/41/208/209/217/219/220. Fullfront/intro,head1–4/18/21soảnh;fixđãđọclại.217colophon ISBN9784863923874/first2018-05-10;218trắngauthorkiểm,rootchưamở. Media38thậtin1,giữvàlogkhôngsuy8;guide11icon28khớpmain37/PDF83authorđãso,rootchưamở83.
- /root/clean_namachuukei_chu: **QA chỉ đọc index onomatopoeia210–216**,khôngviếtknowledge/Git. Đãhandoffcảmxúc180vàđượcrelease,root sởhữu. SauQA210audio210crop/198mã đãgửireportchokeigo,đangkiểm7indexpageschocuốnonomatođểđếmkeys/duplicate/crop;chỉghi.cache/root-live-qa/onomato-index-independent*. Rootchưađượcreportindexthìkhôngtựcoiđãpass.

**28/30PDF,4144/4597trang đãrelease**. Mới nhấtcảmxúc1807f22d1d/bookSHA8211e098a36f3ee17c876abd9188effa2f73c53a797ba24f70ca8202d0d68641;root43ảnh,và180heads/90Units/360hoạtđộng/50Hintsđếmđủ. Source168/187A/A,204/206Masani,validate0/8. Bảyrefindexresolved,189English/180Japaneseromaji;khôngsửaFidgettingthựcin. Toàn30PDFtrêndĩakhớpqueue,khôngnguồnchưagiao. Khôngfinalchođếnhếtphạmvihoặcgiớihạnthật. Skilldocs6ca79cb,codekhôngđổi.

## QA đang diễn ra — snapshot mới nhất

Cả ba assignment đã được guard SHA/page count. Dùng COORDINATOR và resume thật lấy tiến độ, không dựa số snapshot cũ.

- 超ミニフレーズ200:root22 ảnh toàntrang1/10–14/16–18/20–21/23/28/83–84/115–116/146/216–217/224–225 (216/217 mới preflight, chưa sooutput). Root đọc mẫu nhiềuđầu mục/toànessay146. Các sửaprocess-note/essayđãreadback. Root còn mở4contactsheet200gócaudio,không phải200trangsemanticQA:CD1/1–99ở16–114,115blank;CD2/01–30ở116–145,31–99ở148–216,217blank. Mãgiả100đãgỡkhỏichapter/audio/evidence;hai guide12/13minhhọahead22nhưnginCD1/16,ghioccurrencesriêngkhôngremapmain22. Cầnđọcoutput199/200 khiwriterđếnvàđốichiếusource216/217,bảo toàn2politeformsromajitrongPOINT199. Chỉ mục218–223 chưarootmở. Báocáo reviews/mini200-root-sampled.md.
- Roleplay上級:root30ảnh1/15–30/79–88/187/197–198. So toàn bài1 và6/frontmẫu. Mọi lỗi logic,flow/nhãn,companymembership/đườnggiao,本当ですか/はず,謝罪vàbảngGL73/GL78,JP修復/ngoặclồngđãsửa/readback. Writer ràcase2–7,thêm97sửa1時間頃→1時頃 theo nguồn,rootchưamở97. Cácflow32/44/46writerphụchồiJP;rootchưamởnhữngtrangấy. Giữcácdividerthực,vàthứtựbiệtsách7–8in011–012nằmchươngcuốisau189–198,khôngtheooffsetpreflightcũ. CuốicầnQAđápán7/8và189;ảnhđãrender7/8nhưngrootCHƯAmở. Báocáo reviews/roleplay-advanced-root-sampled.md.
- Feelings180:bookmới209/24chương,rootchỉ3ảnhpreflight,đangđợifront/AđểQAsongsong. ĐãnhắcdistinguishtwoexpressionsperUnit,Listen&Speak/Words/50columns,cue/datareadings,indexkhôngbỏkeysdoOCR,audiolabelsCD1/CD2cóthểchỉtrackkhôngphảidisc.

Còn2PDF:worker200xonggiao210pháttriển233;Roleplay上級xonggiaoonomatopoeia220(tùytìnhhìnhrảnhthực). Rootpreflightonomatopoeiađãmở1/3/4/8/12/219/220,4Part,2thoạihoặcđộcthoại/mục+SmallSteps/gloss,downloadinstructions219/220URLhttp://audiobook.jp/exchange/jresearch/code23874. ChưarootchốtISBN/colophon;đừngbỏhaipagecuối. Last2corpusdirectorykhôngtồntạilúckiểm,godirectkhôngrawmới.

Skillcommits:eec34decueROMAJI,dda893eaudioiconvsheadword/guideoccurrences;code0.4.10khôngđổi. RoottiếptụcQA/chốtvàgiaobookkế,khôngfinalpartial.

## Đã chốt

Mới nhất **必須700**,208 trang/8 chương/110unit,commit836c853,BookSHA6942a05723dc132f151e0d901feff6d432ffe0176c98fb777f73aca8e86c5a82. Root26source1/2/9/11–13/15–16/21/26/28/44/49/51–53/115/177–178/183/203–208;toànFeatures1–4/table70 vàcácmẫubài. 91practiceUnits/727prompt/727targetrows/70lookup;rootcountmatched,khôngsuy700. Source2/207needs_review,206checked/6chchecked/108unitschecked+2needs;rootbuildvalidate0/4aftercoordinatorfix28alternativesandguide12audiolocation. Handoffhash0e36a1f013d53b675a67e17dbf3555a3fba4d7b8064a7a1bc28aceea67604062khácfinalrootđãsửa,giữminhbạch trongJSON.2CD/91mainpairsCD1-2–46/CD2-1–46,guide12CD1/6lặpriêng,filesnot_checked. Workerđãfeel180.

**25 sách/3512 trang đã chốt**. Bảy bản đầu501trangfullindependent;18bảnsauthorfull/rootsampled. XemCOORDINATOR/README vàtừngreviewhash,khôngngầmcoi26trangrootthànhfullsemantic.


Mới nhất **Roleplay sơ–trung**,227trang/25chương/172unit,commit09c08fc,BookSHAcd59d0e61fcc795142690aa362cca57d18633dc9aa4d174f5008667b542c6c06. Root33ảnh:1/4/8/11/24–39/185/191–193/202–203/206/215–216/221/223/226–227. Toànbài1soảnh; mẫuCan-do/index/answers/scriptssoảnh. SửaAfirstspeaker/Đạt/companyrelations/teacheraccent/choiceshints/answergenericmeaningsđãđọclại. Index226,14script/42questions; toànindexauthoraudit,rootchỉ33khóaở193/202. 223–224duplicate221–222 (rootso221/223),192nhảy7→9,204adsexcluded. Strictvalidate0/0,no pending/draft/stale.34audio01–34/14scriptrefs/WebURL4008,discunknown/filesnot_checked. WorkerđãRoleplay上級.

Mới nhất **接客700**,225trang/12chương/127unit,commitae73d29,BookSHAebdacfc1060eb913374fb0c5962e0cdbd230599df77138b69779335160e01ef6. Root18ảnh1/8/9/11/13–17/98/178–179/210–211/219/223–225. So đủkeigoUnit1/karaokeUnit1/earthquakeUnit3,36gloss98,19rows219/toàn223. Sửaguidestages/gloss身/readings私đãđọclại. Rootfalsepositiveいたしましょうかđãrút,cropnguồninいたしますか;khôngsửaNhật. Sourceiconvai178–179giữneeds_reviewhẹp. Rootvalidateallow0/4;223checked+2needs,11chapterschecked+1needs.92Units/723prompt/723JPtargetrowsrootđếmkhớp.2CD/92disc-trackpairsCD1-2–47/CD2-1–46,nosuyCD1-1,nodownloadURLfound/filesnot_checked. Workerđã必須700.

24 sách/3304 trang đã chốt;7bảnđầu501trangfullindependent,17bảnsauauthorfull/rootsampled. Khôngcoiđâylàchứngnhậnnguồnhoànhảo.


Mới nhất **お決まり表現180**,209 trang/31 chương/200unit,commitffae3af,BookSHAc2471ee9c12370f449810a53b8dc8bbec34065dfc17ca0d491f321920b96f5b5.180 đầu mục/50mini; root24 ảnh,so trọn Englishindex200–204 và sửa6khóa OCR bỏ,218khóa(43/43/42/45/45),Japaneseindex180mục. Cảhaiindexphủ180headwords/trang,hướngdẫnnguồn đượcgiữ.207pages/29chapters/198units checked+2needs_review ở53/168,vaiNhậtA/A soAnhA/B. Rootbuild/validateallow0/4 sau sửa,khôngpending/draft/stale.90sốtrack,91occurrences vìguideCD6 lặp,sốđĩa chưa xácnhận,filesnot_checked;khôngthấyURLdownloadriêng. Root sở hữu,writerđãsách200. Chi tiết_meta/coordinator-review vàclean/reviews/okimari180-root-sampled.md.

Mới nhất **Shadowing中～上級編** bảnIndonesia–Thai–Việt168 trang/10 chương/93unit,commit0feafae,BookSHAcaddf9c8beada3cb90b0935557653f4bc95d7995078046326e5eb13bdd53c6e7. Root36 trang mẫu;232 thoại ngắn(38/39/39/23/42/30/21)+8section dài.167pages/9chapters/92units checked+1needs_review doA/B/A/A70;khôngpending/draft/stale. Rootvalidateallow0/2 chỉ cùngsourceissue70; giữ cảnh báo trong bản đọc.2CD/DISK1labels02–33,DISK2labels02–31,62cặp đĩa-track,file not_checked. Root đã sửa3時に ở150khôngchoJPkhớpVI;front/hướngdẫn vàcácmẫutheobáocáo đãđọclại. Root sở hữu,writer sang接客700225 trang.

Mới nhất **にほんごで働く！ビジネス日本語30時間**,181 trang/15 chương/171 unit,commit62fd98b,BookSHA82bc042a6dfeb1fbadb47d132bdfbcfec9934c76ea908a293f08355b1a4770ce. Root40 trang mẫu; strictvalidate0/0;181pages/15chapters/171units author_checked,khôngpending/draft/stale/needs_review. Giữ đáp án/script/index và biệt冊162–181; writer audit395 hàng index,root chỉ mẫu.1CD/57labels01–57,script15→145/28→147/37→149/44→151,file not_checked. Root sở hữu, writer đã giao Roleplay sơ–trung227. Chi tiết trong_meta/coordinator-review vàclean/reviews/business30-root-sampled.md.

Mới nhất **5500 câu...hằng ngày**,136 trang/9ch/141unit,commit6f689ed. Root17pages1–8/10/16/38/66/99/128/132/135/136; đọc toànfront vàVậnchuyển nhưngnguồn chỉQAmẫu.76checked/60needs_review,66sourceissues/25pagescắtche;rootvalidateallow0/132. Khôngfullindependentsemanticreview, khôngcoinguồnNhậtchuẩntoànbộ. Đã sửaViệt sai/headingvậnchuyểnII-IV/lặp貸切131, đủ33glossrowscuối. Authorđếm1188câumẫuđánh số,1697JP/VIlabel+2inline, khôngsuy5500từtitle. CDMP3 source1/2/5,khôngtrack/sốdisc/filethật. BookSHA9a9b6267c45252b07bc179efef6c7458cbdc1bb473fe7df04e3b93be66af2152. RootgiữQA/Git, writerđãShadowing168. Cataloghelperignored .cache/root-live-qa/sync_catalog.py --release BOOKDIR COMMIT --assign WORKER BOOKID sauquyếtđịnhQAexplicit,khôngtựnghiệmthu. Scriptverifyreviewhash/errors,refreshaudio/README/COORD;STATUS/HANDOFF cậpnhậttay.

Mới thêm **Denwa** full162/38ch/259unit commit49b0926,root27 trang gồm trọnUnit1/17/35; source83 Note⑧ dở,0/2allow;70CDlabels,file not_checked. Root đã sửa hạn ngàymai, trả mô tả tôngABC xuống script/đápán thay lộởđề Unit1/35; tácgiảràUnit3. **発展文型125** full225/30ch/143unit commit89f4c0f,root29 trang+toànindex125dòng;125model cóluyện,mạchđãtrảvềnguồn,119ba nhánh khung giữrõ. Source120 thiếuA NhậtgiữViệtriêng,0/2allow;99CDlabels,file not_checked. BookSHA71e9ba82546f8db41e3be73583da56dd057cccf7b785bf1ca014cf694fa9c5f1. Báocáo trong_meta/coordinator-review, root sởhữu, workersđãsáchkế.

24 sách/3304 trang; danh sách/commit trong COORDINATOR.released_supplied_pdf_scope và knowledge/README. Bảy bản đầu501 trang full independent review; mười bảy bản sau author full/root sampled. Full là PDF được cung cấp, không dựng trang thiếu.

Shadowing **初～中級編** bản Indonesia–Thai–Việt145 trang, dca0eff: root34 trang1–4/8–9/20–21/23/25–26/37–38/43–45/63–64/81–82/107–114/131–134/138–139. So trọn Unit1sections1/7/10, Unit2/3section cuối, Unit5sections1/2/7,cột③; front/guide đọc toàn, nguồn QA mẫu.42section/411hội thoại/950JP+950VI.420 từ bàn giao đã đính chính vì section cuốiUnit2 chỉ5/Unit3 chỉ6; không thiếu9thoại. Root crop2/139 xác nhận **初～中級編**, lần đầu ảnh nhỏ đọc nhầm・; đã sửa folder/front/title/audio, lưu lịch sử. Colophon〜 là đúng. Validate0/0;42labels02–43, số đĩa chưa xác nhận, filesnot_checked. BookSHA a7434c89ff818087a03a1941d0191a0ed77b73452f6fad63cd711f46d5d1dc37. Root sở hữu, worker đã sách kế.

Nama2 1e29c64 full152/26ch/227unit,root27 trang; nguồn83/119 và9placeholderwarnings đã so nguồn,0/13allow;2CD/82labels. Manners136 nguồn23/28/69/105/106, thiếu trang in104–105;88patterns96 nguồn9/28;Nameraka163 nguồn32 bị che. Giữ source-warning trong bản đọc, không đoán. BJT本文冊 có rebase byte-identical;88 có migration/history1c2d7c0, không reset/init hoặc sửa pin né stale. Chi tiết từng_meta/coordinator-review và clean/reviews.

## Công cụ và môi trường

0.4.10,80 test fork+17 direct PASS. Regression18 bản đã chốt0/33, cache .cache/validator-regression/v0410-18-results.json; cảnhbáonguồn+9placeholderNama2 đãkiểm. Không lặp rộng khi không đổi công cụ/quan ngại. Skill mới thêm so Việt in sẵn và giữ miêu tả ngữ điệu sau đề nghe, không có code đổi.

CLI direct init/checkpoint/resume/build/validate/extend-scope; build không cóallow-source-issues, validate có. Scopefull dở dùng checkpoint/resume, không fake evidence/thu scope. needs_review chỉ lỗi nguồn thực đúngpage/block/unit. Parser không chứng minh nghĩa/đủ học liệu; không ép layout đểqua. Builder tạo book/search, không sửa book.md tay.

Git dùng chung ingest: exactpaths, commit --only; không add.,reset,push hoặc stage PDF/corpus/bunpou/production. Chỉroot Git. GiữCRLF/hardbreakspaces khi chỉnh nhỏ; check core.whitespace=-blank-at-eol,-blank-at-eof,cr-at-eol. Output chỉmd/json/jsonl; renders/helpers ở ignored.cache. Dùng py -B/PYTHONUTF8=1/pymupdf as fitz. exec_command cósession_id thì poll write_stdin; functions.wait chỉ khi functions.exec báo runningcell. Không wait/sleep chặn quá60giây. Trao đổi tiếng Việt có khoảng trắng rõ.

Không final trạng thái này; tiếp QA và điều phối tới hết phạm vi.
