# Clean song song với ingest và tiếp tục sau gián đoạn

## Phân tách công việc

Ingest ghi vào `kaiwa_skill/corpus/`; clean chỉ đọc nguồn và ghi vào `kaiwa_skill/knowledge/`. Có thể ingest sách B trong lúc clean sách A. Một tác nhân clean sở hữu một sách; coordinator không giao trùng sách hoặc vượt ngân sách worker của phiên. Không coi file `book.md` xuất hiện là sách đã hoàn tất.

Hai chat trong cùng checkout vẫn dùng chung Git index. Chọn một coordinator chịu trách nhiệm Git cho cả hai luồng; clean có thể checkpoint xuống đĩa mà không stage/commit cạnh một phiên ingest đang dùng index. Nếu cần commit từ nhiều phiên, dùng checkout/worktree riêng hoặc commit giới hạn đường dẫn cụ thể, kiểm cả index và HEAD trước khi ghi; không reset lịch sử để tách một commit của phiên khác đã nhận các file đang stage.

`clean_progress.py scan --repo-root <repo>` đọc trạng thái để tìm ứng viên. Chỉ đưa sách vào `ready_for_fork` khi nguồn hiện tại có đủ trang verified, bằng chứng/hash trang hợp lệ, không có issue mở, PDF và bản ghép/chỉ mục khớp build marker, không có claim/write lock ingest đang hoạt động. Trạng thái này có nghĩa nguồn sẵn sàng cho bước fork có đối chiếu PDF; không tự nâng nghiệm thu coordinator của ingest. Sách còn làm dở hoặc bản build cũ ở trạng thái chờ, không chặn các sách độc lập.

Lệnh scan chỉ quan sát và trả danh sách; kết quả có thể kèm tiến độ clean đã lưu cho cùng nguồn. Coordinator đối chiếu phạm vi ledger để chọn resume hoặc việc mới, không suy một pilot hoàn tất là đã clean cả sách. Chính tác nhân làm công việc đọc PDF, lọc, dịch và biên soạn. Không có daemon dịch tự động, không cài lịch chạy nền. Trong một lượt được giao xử lý hàng đợi, coordinator quét lại sau mỗi sách/lần bàn giao và nhận sách sẵn sàng tiếp theo trong phạm vi đã giao.

## Khởi tạo và giữ phiên bản nguồn

1. Chọn sách từ danh sách sẵn sàng; mở bìa xác nhận title, lập thư mục tên thật và `_meta/book.json` theo output contract. Chia chapters theo cấu trúc thật của sách, không theo số trang tùy tiện.
2. Chạy `init <book_dir> --repo-root <repo>` để lưu `_meta/clean-state.json` và snapshot văn bản nguồn thuộc phạm vi trong `kaiwa_skill/source_snapshots/<mã nguồn>/<hash bản ghép>/<hash phạm vi>/`. Tách snapshot khỏi `knowledge/` để tìm kiếm toàn bộ thư mục kiến thức không gặp lại bản raw. Lệnh kiểm hash nguồn trước/sau sao lưu; nếu nguồn đổi trong lúc đọc thì không xác nhận snapshot hoàn tất. PDF gốc vẫn chỉ đọc và được ghim bằng hash, không chép thêm PDF vào knowledge.
3. Với sách mới, dùng snapshot làm nguồn Markdown cho phần biên soạn: cập nhật `book.json.source_markdown.path` và `units[].source[].raw_page` sang đường dẫn snapshot tương đối repo; hash nội dung không đổi. `clean-state.json` giữ đường dẫn nguồn live ban đầu để phát hiện bản mới. Không đổi toàn bộ provenance của pilot cũ một cách âm thầm; khi tiếp quản pilot cũ, dùng snapshot để khôi phục/đối chiếu và xử lý rebase có ghi log nếu nguồn live đổi. Snapshot chỉ là hồ sơ nguồn, không đưa vào chỉ mục text sạch.
4. `init` không ghi đè ledger đã có. Khi có ledger, dùng `resume` và đọc trạng thái hiện tại.

Nếu snapshot đã hoàn tất nhưng lần ghi ledger trước bị gián đoạn, `init` chỉ tái sử dụng snapshot khi mọi byte khớp bộ nguồn hiện tại; không ghi đè snapshot khác. Lock còn sót cần xử lý theo mục khôi phục bên dưới trước khi chạy lại lệnh.

Pilot một phần được đăng ký từ `scope.pdf_pages` của pilot; việc đó không biến nguồn toàn sách chưa xong thành sẵn sàng chạy full. Đối với full, coordinator luôn kiểm kết quả scan trước khi init; mở rộng phạm vi pilot cần kế hoạch mới, không thay phạm vi trong ledger cũ.

## Checkpoint từng chương

Sau khi viết hoặc sửa một chương, lưu file cùng provenance rồi chạy:

```text
py .agents/skills/kaiwa-fork-knowledge/scripts/clean_progress.py checkpoint <book_dir> --repo-root <repo> --chapter chapters/ten-chuong.md --status draft --note "Đã lưu nháp; còn đối chiếu phần ..."
```

Khi đã thật sự mở PDF, kiểm đủ phần chương và bản Việt, dùng `--status author_checked` cùng ghi chú cụ thể. Checkpoint lưu hash chương, những unit của chương và nguồn phụ thuộc. Trạng thái này là rà soát của tác giả, không phải QA độc lập. Chương hoàn tất không được làm lại hoặc sửa chỉ để thay cách trình bày khi đang resume.

Giữ ảnh tạm trong `kaiwa_skill/.cache/`; xóa cache không làm mất checkpoint text. Sau các chương thuộc phạm vi, chạy builder, validator và QA như output contract. File gộp/search là dẫn xuất, có thể build lại từ chapters; không lấy file gộp đang dở làm mốc duy nhất để tiếp tục.

## Mở lại sau khi tắt

Chạy `resume <book_dir> --repo-root <repo>`. Tác nhân mới đọc ledger, nhật ký và các issue trên đĩa trước khi làm tiếp:

- Chương `author_checked` có hash hiện tại khớp và nguồn phụ thuộc còn nguyên được giữ lại.
- Chương nháp hoặc chưa làm được nêu rõ để tiếp tục; nếu file đã lưu nhưng chưa checkpoint, kiểm file đó rồi cứu bản nháp trước khi ghi mới.
- Chương bị sửa ngoài checkpoint hoặc unit liên quan đổi được báo stale; chỉ rà lại phần ảnh hưởng. Không reset toàn sách.
- Nguồn live đổi được báo `needs_rebase`; snapshot và đầu ra cũ vẫn giữ nguyên. Không cập nhật hash để làm biến mất cảnh báo. Coordinator quyết định giữ phiên bản nguồn đã ghim hay đối chiếu/rebase các trang thay đổi, và ghi lại quyết định.
- PDF hoặc snapshot bị sửa/mất là lỗi phụ thuộc cần xử lý trước khi tiếp tục xác nhận nội dung.
- Phạm vi trong `book.json` khác phạm vi ledger làm resume/checkpoint bị chặn. Khi mở rộng pilot sang toàn sách, lập kế hoạch mới, lưu ledger cũ vào lịch sử rồi khởi tạo ledger cho phạm vi mới; kế thừa các chương cũ chỉ sau khi kiểm hash và nguồn. Không tự reset hoặc bỏ qua chương mới thêm.

Nếu gặp lock ghi do lần trước bị ngắt, không xóa/ghi đè lock theo tuổi file hoặc PID của một lệnh CLI đã kết thúc. Coordinator xác nhận tác nhân cũ đã dừng, đọc lock và trạng thái thực rồi mới thu hồi lock theo đúng đường dẫn; sau đó chạy lại resume. Mỗi lần checkpoint ghi atomically: một file đang ghi dở không được coi là chương hoàn tất.

Checkpoint hỗ trợ tiếp tục bằng tác nhân mới hoặc chat mới khi được trỏ vào repo và skill. Tắt phiên làm việc dừng tác nhân; không có cam kết tiếp tục tính toán khi ứng dụng đã đóng.
