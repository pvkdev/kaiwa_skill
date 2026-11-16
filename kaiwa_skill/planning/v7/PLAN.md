# Kế hoạch V7 · Xen chuyên đề Speak Japanese vào lộ trình Kaiwa

**Mục tiêu của V7 là quyết định dạy kiến thức nào cùng nhau, ở cấp nào và ngay trước những chặng topic nào.** Sản phẩm để review là một lộ trình có hai loại chặng, cùng chỉ mục để mở từng bài sách và từng cơ hội áp dụng. Nội dung bên trong chặng chuyên đề sẽ được thiết kế sau khi nhìn thấy bản đồ này.

## Điểm xuất phát

V6.5 có 289 chặng topic theo thứ tự Sơ 80, Trung 145 và Thượng 64. Có 125 chặng đã tuyển được bài shadowing, 164 chặng đi tiếp với phần thực hành tình huống. V6.4 giữ 1.592 lượt gán cũ của chín sách. Catalog V6.3 có **1.124 đơn vị nguồn duy nhất** gồm bài chính và tài liệu hỗ trợ. Đây là mẫu số để rà kho tư liệu. Số chuyên đề học được quyết định sau khi đọc và gom theo chức năng nói.

| Sách | Đơn vị nguồn | Chất liệu cần chú ý khi đọc |
|---|---:|---|
| B05 | 120 | Cách nhân viên tiếp khách mở lời, xác nhận và giải thích |
| B06 | 203 | Câu ngắn nâng cao, sắc thái và quan hệ giữa hai bên |
| B07 | 207 | Câu ngắn thường dùng, vào lời và phản hồi trong đối thoại |
| B11 | 109 | Chức năng của mẫu cơ bản, các cặp ví dụ dễ nhầm |
| B12 | 104 | Mẫu nâng cao và tác dụng của việc chọn cách diễn đạt |
| B18 | 104 | Kính ngữ, hướng hành động, vị trí người nói và người nghe |
| B19 | 89 | Từ tượng thanh/tượng hình dùng trong lời nói thực |
| B20 | 94 | Cách nói cố định và hoàn cảnh dùng tự nhiên |
| B24 | 94 | Biểu đạt cảm xúc và đáp lại cảm xúc |

B08 必須700 tiếp tục thuộc nguồn shadowing topic. [Dữ liệu V6.5](../v6_5/STATUS.json) · [Catalog nguồn](../v6_3/coverage) · [Hồ sơ vị trí cũ](../v6_4/admin)

## Các mốc thực hiện

1. **Đối soát đầu vào.** Root ghim hash lộ trình V6.5 và chín catalog. Gom các lượt gán cũ về khóa nguồn duy nhất, lập chỉ mục bài → chặng cũ, đồng thời lập chỉ mục topic → tình huống V6.5. Gặp nhiều bản sao cùng bài thì dùng một ghi chú đọc. Kết quả là hàng đợi có thể tiếp tục theo từng sách.
2. **Pilot ba đoạn ngắn trên lộ trình.** Đề xuất xem quanh S-003, T-012 và H-050. Với mỗi đoạn, đọc những bài có triển vọng rồi thử đặt chuyên đề ngay trước một cơ hội vận dụng. Mở được bài nguồn, nhìn được topic trước/sau và giải thích được người học sẽ dùng kiến thức ở lượt nào. Chọn một trường hợp đa sách và một trường hợp dễ lặp giữa các cấp để kiểm cách gom và gối đầu. Bàn giao ba đoạn preview, nguồn đã đọc, phương án từng cân nhắc và lý do chọn. Khi lệnh chỉ giao pilot, dừng ở bản pilot để chủ dự án review.
3. **Đọc toàn bộ chín sách và lập danh sách ứng viên.** Nếu chạy ba worker Sol/high, có thể chia B05/B07/B11, B06/B12/B18, B19/B20/B24. Chia theo sách ở bước đọc giúp tránh đọc một nguồn nhiều lần. Mỗi worker có thể đề xuất vị trí ở cả ba cấp. Root gom trùng ứng viên giữa các nhóm rồi trả lại những mục chưa có nơi dùng rõ ràng. Kiểm kê cả lời dẫn có nội dung học, bảng đối chiếu và ví dụ đặc trưng.
4. **Xen chuyên đề theo từng level.** Với danh sách ứng viên chung, xét lại nội dung thực, quan hệ và độ khó. Đặt chuyên đề trước các tình huống vận dụng được, giữ thứ tự tương đối của topic. Đọc lại từng cụm như một người học đi từ đầu đến cuối. Nếu kiến thức dồn quá dày, xem lại điểm vận dụng gần nhất, tách phần nâng cao để dùng sau hoặc gộp các ý bổ sung cho nhau. Tái dùng có lý do, gối đầu tùy ngữ cảnh, người học tự chọn chặng.
5. **Nghiệm thu và phát hành.** Tạo JSON lộ trình V7, learner JSON và HTML ba tab, hồ sơ admin truy ngược từng sách, báo cáo số chuyên đề/chặng theo cấp, kiểm kê ý đã dùng/chưa dùng và các giới hạn nguồn. So lại 289 topic V6.5, chạy kiểm tham chiếu và phục hồi. Sau nghiệm thu phiên bản, root commit riêng V7 và cập nhật con trỏ lộ trình. Skill biên soạn bài bên trong chuyên đề là quyết định của pha kế tiếp.

## Ba ví dụ để duyệt tiêu chí pilot

- **Quanh S-003**, V6.4 từng gán B07 mục 146 もう一度いいですか。 và mục 18 どういうことですか？. Thử xem người mới cần học khi nào nên xin nhắc lại vì nghe hụt và khi nào cần hỏi người kia muốn nói gì. Đọc ví dụ trong sách để quyết định cách hỏi nào phù hợp vị trí sớm này.
- **Quanh T-012**, B07 mục 91 悪いんだけど và B11 mục 61 về ～が／～けど có thể hỗ trợ mở lời nhờ. Xem thêm tình huống người nhận cần hỏi rõ phạm vi. Chỉ gom hai phía của cuộc nhờ vả khi người học nhìn thấy được mạch đối đáp.
- **Quanh H-050**, B06 mục 184 難しいです và B18 mục về lời từ chối 申し訳ないのですが là ứng viên cho cách báo giới hạn mà giữ quan hệ. So với nguồn B07 dùng ở chặng trước để xác định điều mới cần dạy, chẳng hạn từ chối yêu cầu của đối tác và mở đường thương lượng. Cả ba ví dụ đều là giả thuyết phân bổ dựa trên hồ sơ cũ. Pilot sẽ kiểm tra bằng việc đọc bài và tình huống thực tế.

## Bao phủ kiến thức

Yêu cầu bao phủ áp dụng đến từng ý học trong nguồn clean. Mục tiêu là mọi kiến thức dạy được của chín sách đều có chỗ học, kể cả nghĩa phụ, sắc thái và ví dụ mở rộng. Có thể ghép cùng ý qua nhiều sách. Mỗi ngoại lệ phải chỉ ra phần bị bỏ và vì sao đưa vào không hợp lý. Số lượt lưu trong kho và số pack đã gắn vào chuyên đề chỉ là số liệu kiểm kê.

## Flow đề xuất để duyệt

1. Mở chặng bằng một mục tiêu nói cụ thể và một lượt thoại ngắn cho thấy người học cần chọn cách nói ở đâu. Có thể dùng chính hội thoại mở đầu của sách trong phần đầu video.
2. Xem video kiến thức dựa trên bài nguồn. Giảng các cách dùng, đối chiếu quan hệ và sắc thái, giữ ví dụ và ghi chú có ý riêng. Nên cho đọc được phần giảng Nhật–Việt khi video chưa sẵn sàng.
3. Ngay sau video, vào shadowing ví dụ tương ứng. Luyện các câu rồi các đoạn đủ ngữ cảnh theo mạch kiến thức vừa học. Hội thoại cho phép nghe/nói toàn đoạn hoặc luyện một vai rồi đổi vai. Câu Nhật có nghĩa Việt, vai và giọng TTS do dữ liệu mô tả. Ví dụ vẫn có thể nằm ở nhà, ở lớp hay ở công ty trong cùng một bài.
4. Một chuyên đề nhỏ có thể có đúng một cặp video → shadowing. Nếu nhiều bài bổ sung cùng mục tiêu nhưng cần hai lần giải thích riêng, có thể lặp cặp này. Nếu giảng liền và đối chiếu trực tiếp dễ hiểu hơn, có thể gom nhiều nguồn vào một cặp. Chỉ rõ bài và ví dụ thuộc cặp nào trong bản thiết kế nội dung sau này.
5. Cuối chuyên đề, gợi chặng topic kế tiếp có cơ hội dùng ngay. Đưa kiến thức vào hội thoại tình huống và Live của chặng topic theo ngữ cảnh. Người học được tự chọn học tiếp hoặc quay lại luyện một vai. Đây là phương án flow để bàn, chưa phải schema node đã chốt.

## Quyết định cần xem ở bản pilot

Xem mục tiêu có vừa một chuyên đề, các bài trong nhóm bổ sung cho nhau ở đâu, người học có sớm gặp dịp dùng lại hay không, và hai cấp liền nhau có khác biệt đáng học hay không. Khi xem phần admin, kiểm khả năng tìm lại toàn bộ ví dụ và kiến thức gốc kể cả những tiểu mục tách ra. Số lượng chuyên đề theo cấp, nhịp xen giữa các topic và cách trình bày bài giảng bên trong vẫn mở cho chủ dự án quyết định dựa trên bản review.

[Skill phân bổ V7](../../../.agents/skills/kaiwa-speak-japanese-roadmap/SKILL.md) · [Quy ước dữ liệu và nghiệm thu](../../../.agents/skills/kaiwa-speak-japanese-roadmap/references/allocation.md)
