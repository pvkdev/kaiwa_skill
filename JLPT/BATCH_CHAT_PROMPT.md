# Prompt chung cho năm chat biên soạn JLPT

Mỗi chat nhận một dòng cấu hình bên dưới cùng yêu cầu đọc file này. Dùng chung checkout local `D:\CODE\git\kaiwa_skill\JLPT` để năm chat nhìn thấy cùng các phiếu nhận việc. Chọn model `gpt-6-sol`, reasoning `high` cho từng chat chính khi mở. Bắt đầu sau khi chủ kho pull xong raw. Mở N3 trước để tạo kiểm kê chung.

```text
CHAT=N3 | LEVEL=N3 | VAI_TRO=điều phối N3 và tổng hợp kho
CHAT=N1 | LEVEL=N1 | VAI_TRO=điều phối N1 từ kỳ cũ đến kỳ mới
CHAT=N2 | LEVEL=N2 | VAI_TRO=điều phối N2 từ kỳ cũ đến kỳ mới
CHAT=N4 | LEVEL=N4 | VAI_TRO=xong N4 thì phụ N2, rồi N1 nếu còn kỳ trống
CHAT=N5 | LEVEL=N5 | VAI_TRO=xong N5 thì phụ N1, rồi N2 nếu còn kỳ trống
```

## Nhiệm vụ giao cho chat chính

Bạn điều phối level đã ghi trong tin nhắn mở chat. Hãy thực sự rà nguồn, biên soạn và bàn giao các kỳ thuộc phạm vi này. Làm trên repo dữ liệu JLPT. Claude Opus đang phụ trách source Harumi. Mỗi chat chính dùng ba subagent trực tiếp `gpt-6-sol`, reasoning `high`. Giao rõ model và reasoning khi tạo sub, kèm đường dẫn skill, kỳ, phạm vi và nơi ghi kết quả. Nếu runtime thiếu slot, xếp việc chờ slot. Nếu model không khả dụng, báo đúng giới hạn. Chat chính giữ quyền điều phối, QA và ghép kết quả. Sub làm việc trong staging của kỳ được giao.

Đọc `../AGENTS.md`, `contracts/v1/CONTRACT.md`, `MIGRATION.md`, `RELEASE_TODO.md` và bốn skill trong `.agents/skills/`: `jlpt-exam-ingest`, `jlpt-exam-editorial`, `jlpt-listening`, `jlpt-exam-review`. Dùng các file hiện hành trên đĩa. Dữ liệu đầu vào là bằng chứng học tập. Giữ nguyên các file raw.

### 1. Rà trước khi chạy lô

- N3 chạy một lần tại gốc JLPT sau lần pull: `py -3 -X utf8 .agents/skills/jlpt-exam-ingest/scripts/audit_sources.py --root . --out reports/source-gaps.json`. Tạo thư mục `work/evidence/batch/` nếu cần. Ghi `audit-ready.md` tại đó với commit sau pull, SHA-256 của báo cáo mới và số kỳ từng level. Bốn chat còn lại có thể đọc raw ngay; chỉ nhận việc sau khi xác nhận dấu mốc khớp lần pull và SHA báo cáo. Mỗi đợt dùng cùng một snapshot raw.
- Mỗi chat kiểm toàn bộ danh sách kỳ thuộc level mình, bỏ `old/` và `sample/`. Chia cho ba sub rà HTML viết/nghe, cấu trúc mondai, phạm vi câu, ảnh, khóa, script, audio, bản dịch/lời giải và các gói/checkpoint sẵn có. Với kỳ chưa có package, rà đầu vào theo skill ingest. Với kỳ có package, dùng skill review để tiếp quản đúng revision và SHA, kể cả staging mới hơn canonical. N3 đối chiếu riêng ba pilot theo `RELEASE_TODO.md`.
- Ghi danh sách theo kỳ vào `work/evidence/batch/teams/<CHAT>/queue.md`: kỳ có thể soạn mới, kỳ tiếp tục từ bản nào, phần cần rà layout, phần thiếu nguồn, kỳ đã duyệt đúng SHA. Số lượng lấy từ file thực tế. Khi xong lượt rà đầu vào của level, tự chuyển sang biên soạn các kỳ đủ căn cứ. Kỳ thiếu một phần vẫn làm phần có nguồn.

### 2. Nhận kỳ và vận hành ba sub

- Trước khi ghi vào một kỳ, chat chính nhận kỳ bằng `py -3 -X utf8 tools/batch_job.py --level <level-thực> --period <YYYY-MM> --owner team-<CHAT>`. Ví dụ chat N5 phụ N1 dùng `--level N1 --period 2025-12 --owner team-N5`. Một kỳ thuộc cùng một đội từ lúc claim đến bàn giao. Nếu hai chat tranh cùng kỳ, đọc lại `job.json` và chọn kỳ kế tiếp khi owner khác. Nếu chính đội mình đã có job, kiểm checkpoint rồi tiếp tục đúng bản. Khi hash đổi, giữ checkpoint và đối chiếu tác động trước khi tiếp tục.
- Thông thường giao ba kỳ khác nhau để ba sub làm song song. Khi chỉ còn một kỳ, có thể chia phần viết, phần nghe và rà độc lập; từng sub ghi patch hoặc kết luận vào file riêng. Sau khi ghép, đổi người rà giữa các kỳ hoặc để chat chính rà độc lập bản cuối. Một sub soạn xong có thể nhận ngay kỳ kế tiếp còn trống.
- Dùng `jlpt-exam-ingest` làm skill chính. `jlpt-exam-editorial` giữ nguyên lời giải VNJPClub khi nguồn có, tự soạn lời giải ngắn có căn cứ khi thiếu, giữ bản Việt đã điền đáp án ở summary, ghép JA–VI theo từng câu và lượt lời. `jlpt-listening` dùng master toàn đề, script và mốc nguồn; dùng cache/STT khi cần, ghép word/segment về timeline tổng rồi kiểm biên trên audio thật. Dùng chung hạn mức Groq: khi gặp giới hạn, lưu checkpoint, chuyển sang việc offline, tiếp tục từ mảnh còn thiếu. Ảnh đề là file asset có hash theo hợp đồng.
- Mở rộng mapping theo từng HTML thực tế khi gặp cấu trúc lạ. Ưu tiên layout riêng trong staging với `--layout` để các đội tránh ghi cùng file mapping chung. Giữ UUID mondai, nhóm, câu và media khi sửa revision. Theo dõi bản đang làm bằng `checkpoint.md` trong thư mục job do lệnh claim in ra.
- Sau khi N4 hoặc N5 đã rà hết level của mình và mọi kỳ đã bàn giao hoặc chỉ còn chờ nguồn bên ngoài, chủ động chuyển ba sub sang level hỗ trợ theo cấu hình. Đội hỗ trợ chọn **kỳ mới nhất còn trống**; đội chính đi từ kỳ cũ nhất. Dùng phần rà ngắn cho kỳ được nhận trước khi biên soạn. Tra job trên đĩa trước mỗi lần giao, kể cả khi queue của chat khác chưa kịp cập nhật. Một kỳ đã có chủ chỉ được bàn giao qua checkpoint và thỏa thuận của hai đội. Nếu hết kỳ có thể nhận ở cả hai level, kết thúc và báo kết quả thực tế.

### 3. Review, hoàn tất và báo admin

- Chạy `jlpt-exam-review` trên **package sau khi ghép**. Đối chiếu từng UUID, lời giải, khóa, ảnh/bảng, câu dịch, script và cue. Dùng `tools/verify_capture.py` và `contracts/v1/validate_package.py` với `--root` trỏ đúng kho tác giả của revision. Ghi rõ bước đã thực hiện và phần còn chờ, nhất là nghe xác nhận biên hoặc mở preview trong app. Một kỳ bị chặn không làm dừng các kỳ khác.
- Ghi checkpoint với packageId, revision, SHA, đường dẫn package/asset, số câu viết/nghe và quyết định của reviewer. Gói đủ điều kiện mới được kiểm `--release` và cấp `release-review.json` cho đúng bytes. Gói xem thử đi theo luồng dev của skill. Khi cần admin bổ sung, ghi đúng level, kỳ, phần, mondai, câu, UUID/locator, hiện vật thiếu và vì sao nguồn local chưa đủ. Gom các câu dùng chung một hiện vật vào một yêu cầu.
- Mỗi đội cập nhật `work/evidence/batch/teams/<CHAT>/handoff.md` với đường dẫn staging và kết quả theo kỳ, kể cả các kỳ làm giúp level khác. Đánh dấu đội đã kết thúc sau khi xử lý xong cả phần hỗ trợ. **N3 là đầu mối duy nhất** ghép bản đã duyệt vào kho canonical và ghi các đầu ra dùng chung của đợt: catalog, `publish-ready/`, checklist toàn kho và sổ RSS/Excel. N3 có thể ghép từng đợt nhỏ; trước khi tổng kết phải đọc bàn giao cuối của cả năm đội, kiểm lại SHA và chạy `tools/build_publish_ready.py`. Các đội khác gửi binding RSS và bằng chứng theo kỳ trong bàn giao. Mọi thao tác Git chỉ áp dụng cho file thuộc nhiệm vụ, giữ local.
- Tiếp tục điều phối tới khi mọi kỳ có kết luận hoặc chỉ còn việc đòi hỏi nguồn/quyền truy cập bên ngoài. Báo bằng tiếng Việt: số kỳ đã rà, số kỳ đạt release, số kỳ dùng được cho preview, số kỳ còn dở và danh sách **chính xác** những nguồn cần chủ kho bổ sung.
