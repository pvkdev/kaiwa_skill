# Changelog

## 0.4.3 — 2026-11-11

- Từ scan Nameraka PDF32: hỗ trợ needs_review cho unit/trang/chapter có chữ in bị ghi tay che. Issue phải gắn vùng thật; checkpoint/resume không coi nó là đã xác nhận.
- Strict validate từ chối unresolved; --allow-source-issues giữ cảnh báo và không bỏ qua pending/draft/stale/missing. Build thêm cảnh báo nguồn và hồ sơ source-issues.
- Giữ tương thích bản pilot đã nghiệm thu trước trường review_state khi không có source issue; không bắt viết lại output chỉ để đổi metadata schema.16 test direct và30 test fork cũ đạt.

## 0.4.2 — 2026-11-11

- Thêm `extend-scope` cho pilot cùng sách: chỉ mở rộng trang/chapter, lưu scope-history và giữ checkpoint còn hợp lệ; trang mới pending, không chứng nhận lại phần stale hoặc xóa dấu vết pilot.
- 10 test PDF-direct đạt, gồm giữ checkpoint cũ khi mở rộng và từ chối dùng đổi scope để che nội dung đã sửa.

## 0.4.1 — 2026-11-11

- Sửa skill theo lỗi pilot thật: mọi câu/lượt Nhật đã in trong bài tập phải có bản Việt, không thay bằng tóm tắt; giữ ô trống và phần đáp án tách riêng.
- Pilot trực tiếp Wakaru đã được root đọc ảnh/output độc lập, sửa và kiểm lại: 6 trang nguồn + PDF9 chứng cứ CD, 4 chapter/10 unit. Lưu PASS với hash hiện tại; không nghiệm thu toàn sách152trang. Mở dispatch full direct cho PDF chưa ingest.

## 0.4.0 — 2026-11-11

- Thêm `kaiwa-pdf-knowledge`: PDF chưa ingest đi thẳng bản sách Nhật–Việt; nguồn raw hoàn chỉnh tiếp tục dùng fork clean. Giữ nguyên mạch riêng, ví dụ, thực hành, đáp án và phụ lục của từng sách.
- PDF-native provenance theo trang/block, hash PDF, kiểm kê vùng giữ/bỏ, coverage, unit/search, checkpoint và resume phát hiện phần stale; không tạo raw giả. Dùng lại builder và kiểm tra text của fork.
- Bổ sung danh mục CD/audio, dẫn trang/vùng, trạng thái file thực có và bằng chứng bổ sung ngoài scope pilot. Thêm yêu cầu inventory cho bản clean cũ.
- 8 test mới và30 test fork cũ đạt; pilot ngữ nghĩa đang thực hiện, chưa mở full direct chỉ nhờ test qua.

## 0.3.8 — 2026-11-11

- Cảnh báo heuristic về số ô trống ở cặp JP/VI, sau khi QA phát hiện khung tự giới thiệu ba ô bị dịch thành bốn. Không ép cách ghi hoặc coi cảnh báo là kết luận ngữ nghĩa.
- Thêm bốn ca hồi quy về thừa/thiếu ô và khác độ dài/ký hiệu;30 kiểm thử đạt. Bảy bản full hiện có và pilot đều qua validator không lỗi/cảnh báo.

## 0.3.7 — 2026-11-11

- Làm rõ mọi đáp án Nhật in sẵn cần bản Việt ở đúng phần đáp án; review cũ phần Nhật không xác nhận bản dịch mới.
- Phân biệt lỗi raw đã được sửa và reviewer xác nhận từ PDF với nghĩa/công thức nguồn còn đáng ngờ; giữ log/provenance, không đánh dấu gloss phổ thông là lỗi khi thiếu căn cứ.

## 0.3.6 — 2026-11-11

- Cập nhật kế hoạch pilot theo rà bảo toàn: giữ trang mở PART1 và mã CD01–03, hội thoại trước giải thích, MEMO đúng thứ tự nguồn. Chín unit trong cùng scope PDF7–12; review mới tách khỏi lịch sử cũ, không đổi thành full sách.

## 0.3.5 — 2026-11-11

- Validator chấp nhận vai Nhật được dịch/phiên âm trong lượt Việt liền kề và số ví dụ không lặp ở nhãn vai. Kiểm sai vai A/B, thiếu lượt Việt và nhầm tag vẫn giữ; parser không xác minh ngữ nghĩa tên vai đã dịch.
- Thêm sáu ca hồi quy từ bản clean kính ngữ; tổng 26 kiểm thử đạt.

## 0.3.4 — 2026-11-11

- Validator nhận cặp Nhật–Việt trong danh sách đánh số/gạch đầu dòng, vai nói có tên Nhật và đoạn Nhật không nhãn, tránh bắt đổi bố cục sách chỉ vì giới hạn parser. Kiểm thiếu bản dịch hoặc sai vai rõ ràng vẫn giữ.
- Thêm kiểm thử hồi quy từ bố cục gặp khi clean hàng loạt; thông báo validator xuất UTF-8.

## 0.3.3 — 2026-11-11

- CLI tiến độ clean xuất UTF-8 trên Windows để tên sách Nhật không làm lệnh báo lỗi mã hóa sau khi checkpoint đã ghi thành công.

## 0.3.2 — 2026-11-11

- Làm rõ clean là biên tập dễ đọc, giữ đầy đủ nội dung, mạch triển khai, bài tập và các phần đặc trưng từng sách; không tuyển chọn kiến thức hoặc ép khuôn bài học.
- Tách quy ước file/provenance khỏi hình thức trình bày; JP/VI là một cách trình bày, không phải template bắt buộc. Giữ mã track, dữ kiện, đáp án nguồn và sự lặp có chủ đích; QA kiểm cả mạch và độ đầy đủ.

## 0.3.1 — 2026-11-11

- Bổ sung workflow clean song song ingest: phát hiện nguồn sẵn sàng, snapshot văn bản và checkpoint từng chương.
- Tiếp quản sau gián đoạn giữ chương hợp lệ, phát hiện thay đổi nguồn/đầu ra và nêu phần cần đối chiếu lại; không tự chạy nền hoặc ghi vào corpus.

## 0.3.0 — 2026-11-11

- Thêm skill `kaiwa-fork-knowledge`: biên soạn tầng kiến thức Nhật–Việt từ corpus, đối chiếu PDF, tách provenance và giữ nguyên ingest.
- Thêm kế hoạch pilot, hợp đồng đầu ra, công cụ build bản đọc/chỉ mục và validator cấu trúc; không dùng script để chứng nhận dịch đúng hoặc đã đọc trang.
- Pilot tách riêng trong `knowledge/`, tên thư mục theo bìa sách; chưa triển khai làm sạch toàn kho hoặc thiết kế lộ trình.

## 0.2.5 — 2026-11-11

- Root trực tiếp đảm nhiệm điều phối/QA/Git theo yêu cầu người dùng; dừng sub điều phối riêng và tăng ba worker Sol/high song song trong giới hạn bốn tác nhân của phiên.

## 0.2.4 — 2026-11-11

- Theo yêu cầu mới của người dùng, toàn bộ điều phối, QA, sửa skill và chuyển đổi sách dùng `gpt-6-sol/high`. Cập nhật cấu hình và hướng dẫn vận hành; không thay đổi schema, CLI, corpus đã nghiệm thu hoặc bằng chứng QA lịch sử.

## 0.2.3 — 2026-11-10

- Cụ thể hóa bước đối chiếu trước verify thành hai chiều ảnh → Markdown và Markdown → ảnh, sau khi QA production phát hiện cả ruby thiếu và ruby tự thêm.
- Nhắc kiểm từng kana nhỏ/cuối chuỗi và đúng occurrence/span bằng crop rõ, đồng thời kiểm nhãn bảng. Không đổi quy tắc nguyên văn, schema hay CLI; nội dung pilot giữ nguyên. Nhóm trang production bị ảnh hưởng được rà mở rộng và reverify các trang sửa, với hash/readback trong báo cáo từng sách.

## 0.2.2 — 2026-11-10

- Làm rõ quy tắc furigana đã có: chỉ giữ cách đọc thực in ở từng lần xuất hiện và map đúng phần chữ được chú âm, không điền cách đọc cho từ lặp.
- Làm rõ dòng nối trong bảng/danh sách và nhãn cột biên tập sau QA sách Shadowing. Không đổi schema, CLI hay nội dung pilot; đây là ví dụ áp dụng yêu cầu bảo toàn nguồn, không thêm chuẩn phiên âm mới.

## 0.2.1 — 2026-11-10

- Làm rõ kiểm header/footer và ranh giới bảng theo từng trang, không dùng số hàng hoặc nội dung lặp mặc định.
- Khi quan sát ảnh toàn trang và crop không khớp, đối chứng trước khi sửa; không suy nguyên nhân hiển thị khi chưa xác định. Không đổi CLI, schema hoặc quy tắc text-only.
- Áp dụng sau audit production N2: sửa dải chia bảng; phản ánh riêng các nhận định thiếu header đã được rút sau khi crop xác nhận nguồn có chữ. Nội dung pilot giữ nguyên, không mở rộng nghiệm thu pilot sang sách khác.

## 0.2.0 — 2026-11-10

- Theo yêu cầu người dùng, corpus và bài luyện kaiwa chỉ có text; hình mang nghĩa được diễn đạt bằng văn bản có nhãn biên tập.
- Ảnh render chỉ là cache phục vụ đối chiếu PDF. Giữ hồ sơ hash bằng text, cho phép dọn cache sau xác nhận và tạo lại khi cần.
- Chuyển pilot hiện có sang chế độ text-only; bỏ PNG khỏi cây Git hiện tại, giữ lịch sử commit cũ.

## 0.1.2 — 2026-11-10

- Sau rà soát pilot, chuẩn hóa nhãn biên tập cho chữ trong hình, tiêu đề lề và tiêu đề nối trang; phân biệt rõ phần thêm để tổ chức Markdown với nguyên văn sách.

## 0.1.1 — 2026-11-10

- Chỉ mục giữ ngữ cảnh unit/trang cho từng khối nội dung.
- Hash tài sản liên kết được ràng buộc vào hồ sơ đối chiếu và bản build; sửa crop làm mất hiệu lực xác nhận cũ.
- Bổ sung kiểm thử tương thích hồ sơ trang chỉ có chữ và phục hồi sau thay đổi asset.

## 0.1.0 — 2026-11-10

- Hai skill điều phối và xử lý từng sách, Astra/high xây dựng và Sol/high chuyển đổi.
- Quy trình đối chiếu từng trang, trạng thái bền vững, phục hồi và kiểm tra hash.
- Markdown bảo toàn nguyên văn, nguồn truy ngược, pilot trước production và commit riêng từng output.
