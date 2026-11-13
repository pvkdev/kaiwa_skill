# Nghiên cứu nhóm hỗ trợ đời sống V5

Ngày 2026-11-13. Đây là bản thiết kế **tình huống nói**, chưa phải hội thoại, bài học hay hướng dẫn thủ tục. Phạm vi: y tế, an toàn, hành chính/tài chính, gia đình/trẻ/người cao tuổi, cộng đồng hỗ trợ. Các chuỗi dưới đây là **đề xuất biên tập bằng AI** dựa trên preview V5, V4.1, đọc chọn nguồn sách và đối chiếu nguồn ngoài; không gán các chuỗi này cho sách. Nguồn ngoài lưu trong `support_web_sources.json`. Không buộc người học kể chuyện riêng thật, nhất là bệnh, bạo lực, ly thân, tang. Ở Sơ luôn có đường nói ngắn để nhờ người giúp, xin phiên dịch, hỏi lại và xác nhận nơi cần tới.

## Ranh giới lớn cần chốt

- `S-34` giữ bản đồ câu sinh tồn; V5P-057/058/059/060/061/062 đi sâu theo **đầu mối, diễn biến và kết quả khác nhau**. Không tập tình huống nguy hiểm bằng kết quả người tiếp nhận tùy tiện từ chối giúp; nhánh từ chối chỉ ở sai đầu mối, thiếu thông tin, hoặc dịch vụ không phù hợp, rồi chuyển tiếp an toàn.
- `S-44`, `T-03`, `H-54` sau tách phải thu hẹp/gộp thành tổng hợp. Shiyakusho, Nyukan, quầy thuế, nenkin, bảo hiểm y tế và ngân hàng không phải một “làm giấy tờ” chung. Chỉ luyện trao đổi mặt đối mặt/điện thoại về giấy tờ, thông báo và bước tiếp; không dạy viết/điền mẫu.
- `T-63/H-09` giữ khám thông thường, triệu chứng và trao đổi sức khỏe gia đình; răng, khám định kỳ, nhập viện, tư vấn tâm lý và nhận thuốc theo đơn có logic khác. Không dạy tự chẩn đoán, tự chọn thuốc hay diễn giải kết quả y khoa.
- `T-50/T-51` giữ trò chuyện gia đình và trường học; nhà trẻ, juku và đầu mối phát triển/học tập khác người đối thoại, mục tiêu và nhịp theo dõi. Trẻ em không là cái cớ để ép người học tiết lộ chuyện con thật.
- `V5P-073` là kỹ năng **định tuyến hỗ trợ** khi chưa biết hỏi ai; các chặng chuyên môn giữ việc giải quyết ở quầy chuyên môn. Hỏi lại, xác nhận và kết nối nhiều bên là phần giao tiếp, không là bài quy trình pháp lý.

## Sổ sách đã đối chiếu

Đã tra `planning/catalog27/BOOK_GUIDE.md`, `planning/v2/index/HEADINGS_27.jsonl` và đọc trực tiếp các đoạn sau trong bản `kaiwa_skill/knowledge/` (bản clean, không kiểm lại ảnh PDF trong lượt này):

- **B08 必須700, `chapters/04-part4-bamen.md`, Unit 11–14, 29:** câu nói tại hiệu thuốc, bệnh viện, ngân hàng/quầy, koban. Phần mở lời, mô tả triệu chứng, hỏi cách dùng, nói mất đồ dùng được làm **chức năng nói**. Unit 14 trộn ngân hàng, 役所 và câu `在留カードの更新をしたい`; không đủ căn cứ lấy câu đó làm mẫu đúng quầy/đúng thủ tục Nyukan. Thông tin `保険証` có thể cũ theo thời điểm, nên soạn bài mới theo câu hỏi “hiện cần xuất trình gì”.
- **B05 接客700, `chapters/09-ch8-kinkyu.md`, Unit 1–6:** nhân viên tiếp khách phát hiện người cần cấp cứu, hướng dẫn khách khi động đất/cháy/sơ tán, và tiếp nhận đồ thất lạc. Vai người học trong cuộc gọi 119 hoặc người dân đi nơi sơ tán **khác vai gốc**; chỉ mượn lối nói rõ, ngắn, không chép logic phục vụ thành quy trình ứng cứu. Một số mẹo an toàn trong sách cần kiểm theo hướng dẫn hiện hành, không dùng như lời khuyên độc lập.
- **B02 BJT, `chapters/11-相談する.md`, Scene 29–30; `chapters/13-確認する.md`, Scene 35:** đã đọc lời thoại/mẫu đầu các phần để nhận chức năng hỏi cách xử lý và kiểm lịch thay đổi; bối cảnh công việc, không chứng minh nội dung sức khỏe hay quyền lợi. Scene 31 và 36–37 mới thấy ở mục lục, cần đọc khi chọn.
- **B01 5500, `chapters/06-dien-thoai.md`, mục đầu chương:** đã đọc các câu mở đầu/chuyển máy; cần chọn chính xác mục khi biên soạn. B01 có nhiều unit cần review, không coi toàn chương là đã xác minh.

Nguồn web chính thức W01–W21 gợi đúng **đầu mối và loại trao đổi**. `support_web_sources.json` ghi `read_status` riêng từng trang: tám trang đã mở, phần còn lại mới đọc trích đoạn tìm kiếm; W01/W03 trả 403 khi thử mở trực tiếp. Chúng không tự xác nhận câu Nhật từ sách, độ tự nhiên hội thoại, điều kiện hồ sơ từng người, mức phí, quyền lợi, lịch địa phương hay kết quả xử lý.

## Bản đồ sự kiện đề xuất theo chặng

Mỗi chuỗi dưới đây cần được mở thành vài tình huống có outcome riêng trong roadmap. Dấu `→` là diễn biến một việc nói qua nhiều lượt/cuộc gặp, không phải thứ tự học bắt buộc.

### Hành chính, cư trú, tài chính

**V5P-025 — Shiyakusho sau chuyển đến/đổi thông tin.** Người mới đến hỏi quầy → nhân viên phân loại chuyển đến hay thay đổi thông tin → nghe tên giấy cần mang → người học phát hiện tên/địa chỉ không khớp → hỏi cách sửa và xác nhận cơ quan nào giữ dữ liệu gốc → thiếu giấy nên hẹn quay lại và nhắc lại danh sách. Nhánh riêng: đến đúng quầy nhưng chưa có phiên dịch; người học nhờ câu dễ hiểu hoặc lịch có người hỗ trợ. Ranh giới: không biến thành bài điền tờ khai. W01.

**V5P-027 — Nyukan.** Gọi trước để nói hoàn cảnh đã thay đổi và hỏi đúng đầu mối → gặp trực tiếp, kể mốc công việc/học tập và điều đã biết → nhân viên hỏi thêm hoặc trả lời có điều kiện → người học phân biệt “được nhận hồ sơ” với “đã được chấp thuận” → bổ sung giấy, xác nhận cách nhận tin; nếu chưa hiểu thông báo thì gọi hỏi lại. Nhánh sai hẹn: người học tưởng tới lấy kết quả, quầy cho biết còn chờ; tập xin mốc liên hệ tiếp. B08 chỉ có chức năng mở lời, W01–W02 cho phân ranh.

**V5P-028 — Cư trú cho vợ/chồng/con.** Cặp đôi trình bày ai đang ở Nhật, ai ở ngoài → quầy hỏi quan hệ/giấy gốc; tên phiên âm hai hệ thống không khớp → nhờ chỉ rõ cần kiểm chỗ nào → người nhà đổi kế hoạch đi/đến → hỏi việc đang chờ có bị ảnh hưởng và được chuyển chuyên viên khi vượt thẩm quyền quầy. Giữ riêng với chặng kết hôn V5P-069: đây là trao đổi tình trạng cư trú, không phải bàn lễ cưới. W01–W02.

**V5P-030 — Quầy thuế.** Người học cầm thông báo hỏi kỳ/khoản nào → nhân viên hỏi loại thu nhập, cơ quan phát thông báo → người học kể có hai nguồn nhưng không suy kết luận thuế → phát hiện số/tên khác giấy đang có → xin giải thích và hỏi nơi xác nhận → hẹn mang thêm chứng từ, sau đó gọi kiểm đã được tiếp nhận chưa. Có nhánh thông báo của thuế địa phương nhưng người học đến quầy thuế quốc gia, được chuyển đúng cơ quan. Tách rõ “giải thích thông báo” khỏi “tư vấn mức phải nộp”. W20; không dựng mức tiền hoặc miễn giảm.

**V5P-031 — Nenkin.** Đặt lịch tư vấn → hỏi quá trình tham gia ghi nhận ra sao → nhân viên xác nhận có khoảng chưa khớp → người học kể lúc đổi việc và hỏi tài liệu để đối chiếu → hỏi lựa chọn khi khó khăn, yêu cầu giải thích tác động của từng lựa chọn từ chuyên viên → nhắc lại mốc tiếp theo. Nhánh quầy đông/chưa tới lượt: chuyển lịch và xác nhận phiên dịch. W06.

**V5P-032 — Bảo hiểm y tế.** Người học vừa đổi công ty/trạng thái, hỏi quầy phụ trách → gặp khó vì dữ liệu chưa cập nhật trong lúc cần khám → hỏi có thể xác nhận tình trạng bằng cách nào và ai giải thích phần chi phí → thông báo phí đến nhưng chưa hiểu kỳ tính → gọi lại sau khi quầy liên hệ cơ quan khác. Không tự nói ai có quyền lợi gì. W05.

**V5P-033 — Ngân hàng: tài khoản.** Tại quầy, tài khoản không dùng được → xác minh danh tính qua trao đổi tên cũ/tên mới, địa chỉ → nhân viên chuyển bộ phận hoặc đề nghị giấy khác → người học xin lý do dễ hiểu và hẹn gặp lại → một giao dịch cũ chưa phản ánh; phân biệt đó là cuộc hỏi tiến độ mới. Không dạy cách vượt xác minh. B08 U13–14 chỉ cung cấp mở lời, W16 bối cảnh.

**V5P-034 — Chuyển tiền quốc tế.** Hỏi dịch vụ, người nhận và tổng phí → nhân viên yêu cầu giải thích mục đích giao dịch; trả lời đúng phần biết, xin nhắc câu chưa hiểu → ngân hàng tạm giữ/chờ kiểm → sau ngày dự kiến người nhận chưa nhận, người học báo mã tham chiếu và hỏi bước tra soát → phát hiện tên nhận sai thì xin hướng dẫn sửa theo quy trình đơn vị. Không hứa tỷ giá, phí hoặc thời gian.

**V5P-035 — Thẻ và giao dịch lạ.** Một khoản bị tính hai lần hoặc không nhận ra → người học gọi đúng kênh phát hành, xác minh an toàn → mô tả khoản theo ngày/số tiền mà không đọc bí mật không cần thiết → nhân viên giải thích đang chờ xử lý, cần thêm thông tin hoặc chuyển bộ phận → người học nhắc lại việc cần làm, mã tham chiếu và khi nào liên hệ lại. Tách nhánh mất thẻ với giao dịch đáng ngờ, tránh giảng quy tắc bồi hoàn chung.

**V5P-039 — Hủy dịch vụ/tư vấn tiêu dùng.** Người học nhắc lần thử và mốc đã yêu cầu hủy → nhà cung cấp nói phí vẫn tính, viện điều kiện người học chưa rõ → hỏi giải thích, xác nhận họ có thể làm gì ngay và điều cần chờ → khi không giải quyết, tóm tắt sự việc với quầy tư vấn tiêu dùng, nhắc lại đầu mối tiếp theo. W15 chỉ chứng minh có đường tư vấn; không hứa hoàn phí.

**V5P-040 — Bảo hiểm bồi thường.** Báo sự việc theo thời gian và điều chắc chắn biết → nhân viên hỏi hợp đồng nào/phạm vi nào → người học sửa một chi tiết đã báo nhầm, tách lời chứng kiến và suy đoán → hỏi giấy/chứng cứ cần, nhận kết quả “chưa đủ để kết luận” hoặc “không thuộc đơn vị này” → hỏi cách được giải thích quyết định và chốt liên hệ tiếp. Không đoán mức bồi thường.

**V5P-080 — Rời Nhật dài hạn.** Nói ngày dự định với chủ nhà/công ty dịch vụ/quầy hỗ trợ → hẹn bàn giao, một bên chỉ có lịch sau ngày bay → thương lượng người liên hệ thay và cách nhận thông tin cuối → kiểm còn khoản/hồ sơ đang xử lý ở cơ quan khác → gọi xác nhận từng đầu mối. Đây là điều phối nói đa bên; không dạy danh sách thủ tục bắt buộc chung.

**V5P-124 — Về Việt Nam tạm thời rồi quay lại.** Bàn lịch nghỉ và người thay việc với công ty → hỏi đúng cơ quan về mục chưa chắc trước khi đi, không tự suy điều kiện tái nhập → nhờ người quen/chủ nhà liên hệ khi có thư quan trọng → chuyến quay lại đổi ngày, gọi cập nhật hẹn làm/đón con/dịch vụ → sau về xác nhận lịch mới. Khác V5P-080 ở ý định tiếp tục đời sống tại Nhật.

**V5P-125 — Mất thẻ cư trú hoặc hộ chiếu.** Xác định món nào mất và thời điểm cuối còn thấy → hỏi nơi tiếp nhận trình báo, giữ số tham chiếu → liên hệ đúng cơ quan cấp lại thẻ hoặc cơ quan của quốc tịch về hộ chiếu → nói đang thiếu giấy khi có cuộc hẹn khác, xin đổi hẹn → nếu tìm lại đồ, báo cập nhật cho đầu mối liên quan. W03 cho luồng thẻ cư trú, **không** suy hộ chiếu cũng cùng quầy/thủ tục. B08 U29 là chức năng mô tả mất đồ.

### Y tế và an toàn

**V5P-049 — Nha sĩ.** Gọi đặt lịch vì đau/miếng trám gặp vấn đề → tại quầy nói lần khám trước và lo lắng → nha sĩ trình bày vài cách; người học hỏi lại mục tiêu, số lần, chi phí dự kiến trước quyết định → khi đau/không chịu được trong buổi khám xin dừng và báo cảm giác → sau đó hỏi dấu hiệu cần liên hệ lại, đổi lịch tái khám. Không mô tả lựa chọn điều trị là lời khuyên. B08 U12 chỉ nền mô tả triệu chứng, không là nha khoa.

**V5P-051 — Khám sức khỏe định kỳ.** Hỏi nơi đặt lịch và hướng dẫn chuẩn bị → tại tiếp nhận xác nhận loại lịch, nói điều kiện cá nhân cần chuyên viên biết → bị gọi nhầm quầy nên hỏi lại → khi nhận kết quả, chỉ hỏi thuật ngữ và ai có thể giải thích, không tự giải nghĩa chỉ số → phối hợp lịch gặp tiếp với công ty/gia đình nếu cần. Tránh lẫn với khám vì triệu chứng T-63.

**V5P-052 — Nhập viện/ra viện.** Trước nhập viện hỏi lịch, người liên hệ và hỗ trợ ngôn ngữ → trao đổi với chuyên viên về phần giải thích chưa rõ trước quyết định → trong viện báo nhu cầu cụ thể và thay đổi triệu chứng cho nhân viên → kế hoạch ra viện đổi, người học gọi người đón/người chăm ở nhà → hỏi lịch tái khám và cách liên hệ khi cần. Không dựng quyết định điều trị. Nhánh người nhà không tới được, cần hỗ trợ phối hợp.

**V5P-054 — Xin tư vấn sức khỏe tinh thần.** Mở lời xin cuộc gặp riêng bằng một tình huống giả định nhẹ → nói ảnh hưởng lên ngủ/học/làm ở mức người học chọn → hỏi tính riêng tư và hình thức hỗ trợ → nói “hiện tôi chưa sẵn sàng kể thêm” → xác nhận nơi hẹn tiếp. Nhánh trao đổi với quản lý chỉ nói nhu cầu điều chỉnh công việc, không bắt tiết lộ chẩn đoán. W13.

**V5P-056 — Nhận thuốc theo đơn lâu dài.** Đưa thông tin thuốc đang dùng cho dược sĩ → hỏi lại liều/cách dùng do chuyên viên đã chỉ, báo đơn không đủ hàng hoặc khác lần trước → dược sĩ cần xác nhận bác sĩ, người học hỏi phương án trong lúc chờ → nếu có biểu hiện bất thường, báo đúng triệu chứng và xin nói với chuyên viên → xác nhận lần nhận tiếp. Không cho AI chỉ định liều hay bảo người học tự ngừng thuốc. B08 U11 là câu hỏi cơ bản, cần phân biệt thuốc kê đơn với bán lẻ.

**V5P-057 — Báo khẩn cấp với cảnh sát.** Người học xin người gần đó gọi giúp vì không nói được → nói vị trí qua ga/tòa/mốc nhìn thấy, kể điều đang diễn ra và điều chưa biết → tổng đài hỏi lại, người học sửa điểm nghe nhầm và xin hỗ trợ ngôn ngữ → chốt nơi an toàn để gặp đơn vị đến. Nhánh nếu sau đó cần trình báo chi tiết, chuyển cuộc tiếp theo; koban mất đồ ở V5P-060, không hòa thành một. W18 phân biệt 110 với tư vấn không khẩn cấp; không đưa một sự việc không khẩn cấp vào cuộc gọi 110.

**V5P-058 — Gọi hỗ trợ y tế khẩn cấp.** Nói cần xe cấp cứu và nơi → mô tả quan sát ở người cần giúp, không tự chẩn đoán → trả lời câu hỏi điều phối, hỏi lại một từ không hiểu → nhờ người khác đón ở lối vào → khi đội đến, bàn giao diễn biến đã biết và điều chưa biết. Cấp Sơ phải có câu cực ngắn gọi người giúp. W07–W09; B05 U1–2 là vai nhân viên tại chỗ.

**V5P-059 — Báo cháy.** Báo vị trí, tầng, khói/lửa quan sát được → người tiếp nhận hỏi có ai còn bên trong, người học trả lời trong giới hạn biết → nhận hướng dẫn, lặp lại chỗ cần di chuyển → gặp lối dự kiến không dùng được, báo vị trí mới → liên hệ người phụ trách nơi ở sau khi an toàn. W08–W09; B05 U4–5 vai nhân viên hướng dẫn khách, không mặc nhiên là lời gọi 119.

**V5P-060 — Koban/đồ thất lạc.** Người mất kể thời gian và nơi cuối còn đồ, mô tả đặc điểm, giấy bên trong → koban cho biết chưa thấy và hỏi cách liên hệ → sau đó có đồ tương tự, người học đến đối chiếu nhưng có chi tiết không khớp → hỏi tiếp cách theo dõi. Nếu đồ mất có thẻ/điện thoại, người học còn phải gọi đơn vị phát hành/cung cấp để hỏi cách bảo vệ tài khoản; không kỳ vọng koban làm hộ. Nhánh khác: người học nhặt được đồ, trình bày chỗ nhặt và bàn giao; không trộn với sự việc khẩn cấp. B08 U29; B05 U6 khác vai (cửa hàng); W19.

**V5P-061 — Đe dọa/theo dõi/bạo lực.** Nhân vật giả định xin nói nơi riêng và người hỗ trợ ngôn ngữ → nói mức nguy cơ hiện tại và cách liên lạc **an toàn** → người tiếp nhận hỏi chi tiết, nhân vật có quyền chưa kể phần không sẵn sàng → được giới thiệu đầu mối khác, nhắc lại cách tới đó và giờ liên hệ → đổi cách liên hệ khi hoàn cảnh thay đổi. Khi nguy cấp, dùng đường nhờ giúp Sơ trước mọi cuộc kể dài. W14/W17; không hứa bảo mật tuyệt đối hay kết quả pháp lý.

**V5P-062 — Nơi sơ tán.** Hỏi nơi tiếp nhận, báo số người đi cùng và nhu cầu cụ thể (ngôn ngữ, thuốc đang cần, trẻ/già) → người phụ trách hướng dẫn chỗ ở tạm và quy tắc → vật dụng cần chưa có, hỏi ai phụ trách/khi nào hỏi lại → người thân mất liên lạc, nói điều biết và chưa biết → khi chuyển nơi, xác nhận đầu mối và cách báo người nhà. W10; B05 U5 chỉ là vai người dẫn khách.

**V5P-063 — Ổn định sau thiên tai.** Nhà hoặc việc làm bị ảnh hưởng; người học tóm tắt sự việc với quầy hỗ trợ → quầy chỉ sang đơn vị khác hoặc cần chứng cứ chưa có → hỏi cách tiếp cận chỗ ở tạm/sửa chữa qua người phụ trách → chủ nhà và công ty đưa hai lịch trái nhau, người học điều phối lại → hẹn cập nhật khi có thông tin. Không gán sẵn quyền được trợ cấp hay lịch sửa.

### Gia đình, trẻ em, người cao tuổi và cộng đồng

**V5P-065 — Nhà trẻ.** Hỏi lịch tham quan và nói tuổi/nhu cầu chung → trao đổi thói quen con với giáo viên ở buổi đầu → một ngày con sốt hoặc người đón đổi, gọi báo và xác nhận người được đón → cô giáo nói con khó hòa nhập, người học xin ví dụ cụ thể, chia sẻ điều quan sát ở nhà → thống nhất cách thử và buổi trao đổi lại. Không áp một quy tắc tuyển sinh/đón trẻ cho mọi nơi. W11.

**V5P-067 — Juku/ngoại khóa.** Hỏi lớp phù hợp và xin học thử → nghe giờ, phí và phần phát sinh, hỏi lại mức cam kết → sau buổi thử con không thích hoặc lịch va chạm, trao đổi khả năng đổi/lùi → chọn tiếp, tạm nghỉ hoặc từ chối và chốt điều kiện. Không biến thành kỳ vọng phải cho con học thêm.

**V5P-068 — Hỗ trợ phát triển/học tập cho con.** Cha mẹ giả định xin cuộc nói riêng → kể hai quan sát cụ thể ở nhà/lớp, tránh gắn nhãn chẩn đoán → hỏi mục đích gặp chuyên viên, người có mặt và cách chia sẻ thông tin → nghe vài cách hỗ trợ, hỏi phần gia đình và trường phối hợp được → sau vài tuần báo cái hiệu quả/chưa hiệu quả và hẹn xem lại. W11; không để AI đóng vai bác sĩ chẩn đoán trẻ.

**V5P-069 — Kết hôn/gia đình quốc tế.** Hai người bàn mong muốn và lịch với gia đình hai bên → đến quầy hỏi đầu mối cho giấy tờ từng nước, phát hiện tên/phiên âm khác → xin giải thích nguồn dữ liệu cần đối chiếu, hẹn quay lại → gia đình thay ý định về lễ/nơi ở, cặp đôi thương lượng giữ quan hệ. Phần cư trú của người nhà qua V5P-028; không tự liệt kê giấy bắt buộc.

**V5P-070 — Ly thân/thay đổi gia đình.** Nhân vật giả định xin tư vấn riêng, nói mục tiêu trước mắt (chỗ ở, con, liên lạc) → hỏi cách liên hệ an toàn và chuyên viên phù hợp → quầy hỏi thông tin, nhân vật chưa muốn kể tất cả → được giới thiệu nơi tư vấn pháp lý/gia đình và hỏi cần chuẩn bị gì cho cuộc hẹn → gọi lại khi kế hoạch đổi. W11/W14/W17; tránh lời khuyên pháp lý hoặc ép kể trải nghiệm.

**V5P-071 — Lo tang.** Người thân gọi đơn vị dịch vụ, nói vai trò, ngôn ngữ/tôn giáo/mong muốn gia đình → nghe từng phần dịch vụ và dự toán, xin tách mục chưa hiểu → người nhà ở xa đổi giờ, điều phối với nơi tổ chức → cơ quan khác yêu cầu giấy, người học hỏi đúng đầu mối và hẹn → tổng kết ai liên lạc tiếp. Không suy một nghi thức chuẩn; cho phép tập bằng hoàn cảnh hư cấu.

**V5P-072 — Chăm sóc người cao tuổi.** Gia đình hỏi nơi có thể tư vấn → kể sinh hoạt cụ thể và điều người lớn tuổi tự mong muốn → nghe các hình thức hỗ trợ, hỏi lịch/phần gia đình làm và chi phí cần được chuyên viên giải thích → người chăm không đến được, xin phương án tạm và cập nhật tình trạng → cùng xem lại kế hoạch khi không phù hợp. W12. Giữ tiếng nói của người cần chăm, không để con cháu quyết thay mặc định.

**V5P-073 — Trung tâm hỗ trợ người nước ngoài.** Người học nói vấn đề bằng 2–3 mốc → xin nói chậm/phiên dịch → nhân viên phân loại và chỉ quầy chuyên môn → lần đầu chỉ nhận được lịch chờ, hỏi việc có thể làm trước → lần sau mang thông báo để hỏi ý nghĩa và nhắc lại đầu mối/bước tiếp. W04. Đây là kỹ năng tìm đúng người, không thay lời chuyên môn.

**V5P-075 — Đào tạo nghề/học lại.** Người đi làm nói mục tiêu đổi/nâng kỹ năng với người tư vấn → nghe chương trình, lịch và điều kiện, hỏi phần còn mơ hồ → thương lượng với quản lý về giờ học/việc bàn giao → trong khóa không theo kịp phần thực hành, xin được hướng dẫn lại hoặc đổi cách học → sau khóa hỏi đầu mối hỗ trợ bước tiếp. Ranh giới với Hello Work tìm việc: đây là **học và phối hợp lịch**, không phải phỏng vấn tuyển dụng.

**V5P-076 — Tình nguyện với vai thành viên.** Hỏi buổi đầu cần tới đâu và có thể làm gì → nhận việc nhỏ, nghe chưa rõ nên hỏi lại người phối hợp → phát sinh không làm được nhiệm vụ, báo sớm và xin đổi → phản hồi sau buổi và hẹn lần tới. H-55 giữ vai điều phối/đại diện cộng đồng.

**V5P-077 — Circle/câu lạc bộ.** Xin đến xem thử → giới thiệu sở thích và kinh nghiệm vừa đủ → hỏi lịch/phí/quy tắc → hôm đầu chưa theo kịp, nhờ thành viên hướng dẫn → vắng buổi sau, báo và hỏi trách nhiệm đã nhận → đề xuất hoạt động tiếp hoặc rời nhóm lịch sự. Khác tình nguyện ở quan hệ tự nguyện duy trì sở thích.

**V5P-078 — Sống cùng thú cưng.** Chủ thú cưng gọi thú y, mô tả thay đổi quan sát được, hỏi lịch khám → bác sĩ giải thích cách chăm, người học hỏi lại trước khi làm → khi đi vắng hỏi dịch vụ trông và điều kiện → ban quản lý/hàng xóm phản ánh tiếng ồn, người học nghe cụ thể, xin thời gian khắc phục và hẹn cập nhật → nếu thú cưng lạc, hỏi đúng đầu mối và cung cấp đặc điểm. H-12 là chặng mẹ được làm rõ, không cộng một chặng mới chỉ vì đổi tên. Không dạy điều trị thú y.

**V5P-128 — Đón người thân đến chơi.** Bàn trước điểm gặp và phương án nếu lạc nhau → tại sân bay/ga không thấy nhau, người học hỏi quầy, gọi lại mô tả vị trí dễ nhận → người thân lớn tuổi/trẻ cần hỗ trợ, người học nói nhu cầu với nhân viên rồi giải thích lại cho người nhà → kế hoạch đi chơi quá sức hoặc thời tiết đổi, cả nhà thương lượng lịch nhẹ hơn → gọi dịch vụ đổi hẹn và xác nhận điểm đón mới. Ranh giới với bài giao thông: trọng tâm là **đi cùng và hỗ trợ người thân**, không phải mua vé lần đầu.

## Lỗ hổng nguồn cần tra ở lượt biên soạn

1. Nguồn sách trực tiếp cho nha khoa điều trị, nhập viện, sức khỏe tinh thần, nhà trẻ, ly thân, chăm sóc cao tuổi, thuế, nenkin, bảo hiểm, chuyển tiền và ngân hàng hiện chưa được đọc đủ; các chuỗi ở trên là AI đề xuất, giữ nhãn đó.
2. W18–W21 đã cho khung cảnh sát/110, koban/đồ thất lạc, thuế và tư vấn dịch vụ tài chính; vẫn cần đối chiếu **trực tiếp cho từng thủ tục** trước khi viết câu có thông số, quyền, thời hạn hoặc số điện thoại. Hộ chiếu Việt Nam, điều khoản ngân hàng/thẻ và giao dịch quốc tế chưa có nguồn tương ứng trong lượt này.
3. Kiểm nguồn chức năng nói B11/B12, B01/B08/B09/B13/B14/B25–B27 theo từng chặng khi viết bài. Có heading không bằng đọc đoạn; có đoạn đúng từ không đồng nghĩa đúng vai hoặc đúng chuỗi sự kiện.
4. Sách là một nguồn. Bối cảnh thực tế còn cần văn bản official địa phương và có thể nguồn cộng đồng đáng tin để thấy vấn đề thường gặp. Không cố dùng đủ 27 sách.
