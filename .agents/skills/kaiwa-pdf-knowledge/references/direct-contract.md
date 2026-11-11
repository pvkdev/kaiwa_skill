# PDF → knowledge: hợp đồng dữ liệu

Đường dẫn ở `source_pdf.path` tính từ gốc repo. Đường dẫn chapter tính từ thư mục sách. Trang PDF là số vật lý 1-based. Mọi file text dùng UTF-8. Script mới chỉ áp dụng khi `_meta/book.json.source.mode = "pdf_direct"`; không sửa hay giả lập `source_markdown`/raw corpus. `book.md`, `_meta/search.jsonl` do builder fork hiện hành tạo từ chapter và units, không sửa tay.

## Khởi tạo và checkpoint

```powershell
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py init "kaiwa_skill/knowledge/<tên sách>" --repo-root . --source-pdf "kaiwa_skill/book/<PDF>.pdf" --title "<nhan đề đã xem trên PDF>" --pages "1,17-18,23,149,152" --chapters "chapters/00-bia.md,chapters/01-bai.md,chapters/02-dap-an.md" --status pilot_partial
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py resume "kaiwa_skill/knowledge/<tên sách>" --repo-root .
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py checkpoint "kaiwa_skill/knowledge/<tên sách>" --repo-root . --page 17 --status author_checked --note "Đã mở ảnh p17 và đối chiếu từng block với chapter/units, gồm bài tập và JP–VI."
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py checkpoint "kaiwa_skill/knowledge/<tên sách>" --repo-root . --chapter "chapters/01-bai.md" --status author_checked --note "Đã đối chiếu mạch trang 17–18, ví dụ, bài tập và dịch Việt."
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py build "kaiwa_skill/knowledge/<tên sách>" --repo-root .
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py validate "kaiwa_skill/knowledge/<tên sách>" --repo-root .
```

`init` dùng `pdfinfo` xác nhận tổng trang, ghi `_meta/book.json`, `_meta/direct-state.json`, `_meta/audio.json` ở trạng thái chưa kiểm. Không chạy `init` lại để ghi đè. `checkpoint` không tự đọc ảnh; `author_checked` chỉ ghi sau khi worker thực sự mở ảnh gốc và đối chiếu. Mỗi chương phải có checkpoint của tất cả trang mà units trỏ đến. `resume` so sánh hash nguồn, chapter, units **thuộc chương**, và trang evidence liên quan; sửa nội dung hoặc nguồn làm checkpoint tương ứng stale, còn thêm một unit ở chương khác không làm stale chương đã xong. Audio có hash riêng trong `book.build`: sửa audio bắt buộc build/validate lại nhưng không làm stale xác nhận nội dung của các chương không liên quan. `validate` mặc định yêu cầu tất cả trang/chương trong **scope khai báo** đã author_checked hiện hành; `--allow-draft` chỉ để kiểm tra cấu trúc lúc đang làm, không nghiệm thu.

`build` cần evidence cho toàn scope và mọi chapter đã khai báo. Full book còn pending thì dùng checkpoint/resume và đọc từng chapter để QA, chưa build toàn sách. `--allow-draft` không cho phép bỏ qua evidence/chapters bị thiếu; nó chỉ hạ yêu cầu author_checked của dữ liệu đã có. Không tạo file trang giả hoặc đổi phạm vi để né lỗi thiếu dữ liệu.

### Chữ nguồn bị che/không đọc chắc (`needs_review`)

Chỉ dùng khi đã **mở ảnh gốc**, thấy vấn đề cụ thể trong chính PDF, và không thể phục hồi chắc chắn. Không đoán chữ/đáp án. Page evidence có `review_status: "needs_review"`, `review_note` ghi đã mở ảnh và phạm vi chưa rõ, `issues` chứa ít nhất một `{ "pdf_block": "p0032-b005", "description": "Chữ in ... bị ghi tay che ..." }` trỏ block có thật trong `blocks`. `checks.visual_review` và `checks.reading_order` phải `true`; cả bốn checks phải là boolean; `text_complete`/`japanese_accuracy` có thể `false` đúng thực tế. Nếu block đó vào unit, unit có `review_status: "needs_review"` và `issues` chứa `{ "pdf_page": 32, "pdf_block": "p0032-b005", "description": "..." }` đúng source mapping. Issue unit phải khớp issue trang cùng block. Giữ `issues` cụ thể; không dùng status này cho phần chỉ chưa làm.

```powershell
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py checkpoint "kaiwa_skill/knowledge/<tên sách>" --repo-root . --page 32 --status needs_review --note "Đã mở ảnh p32; chữ in tại p0032-b005 bị ghi tay che, chưa đọc chắc."
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py checkpoint "kaiwa_skill/knowledge/<tên sách>" --repo-root . --chapter "chapters/<chương>.md" --status needs_review --note "Đã đối chiếu chương; còn vấn đề nguồn p32-b005."
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py build "kaiwa_skill/knowledge/<tên sách>" --repo-root .
py .agents/skills/kaiwa-pdf-knowledge/scripts/direct_progress.py validate "kaiwa_skill/knowledge/<tên sách>" --repo-root . --allow-source-issues
```

Checkpoint chapter `needs_review` chỉ ghi khi **mọi trang mà unit của chương trỏ đến** đã có checkpoint `author_checked` hoặc `needs_review` hiện hành, unit không còn draft, và ít nhất một page/unit có issue. `resume` hiển thị nhóm `needs_review` riêng, không tính nó là completed. Build viết notice ngay đầu `book.md` liên kết `_meta/source-issues.md`, ghi `book.build.review_state: "source_issues_unresolved"` và trả warnings; status scope `full` chỉ nói phạm vi trang, không có nghĩa clean đã hoàn tất. `validate` mặc định fail nếu còn issue. `--allow-source-issues` chỉ cho cấu trúc/coverage đã hoàn tất với warning hiển thị; pending, draft, stale, thiếu trang/chapter, source hash sai hoặc issue thiếu bằng chứng vẫn fail. Sửa nội dung/evidence sau checkpoint làm trạng thái stale; phải mở ảnh và checkpoint lại. Khi giải quyết issue, đổi page/unit sang `author_checked` chỉ sau đối chiếu thật, cập nhật checks, checkpoint lại rồi build/validate mặc định.

## Nguồn và trang

Khi coordinator giao mở rộng pilot sang full **cùng sách**, không init lại, sao chép thư mục tên khác hoặc sửa hash/scope bằng tay. Dùng `extend-scope <book_dir> --repo-root . --pages "1-N" --chapters "<toàn bộ thứ tự chapter, gồm chapter cũ>" --status full --note "<scope mới đã được giao>"`. Lệnh chỉ thêm trang/chapter, giữ thứ tự tương đối chapter cũ và checkpoint còn hợp lệ, lưu metadata/state cũ trong `_meta/scope-history/`. Trang mới luôn pending, kể cả trước đó đã được xem riêng cho CD. Chapter sửa nội dung sau mở rộng vẫn stale bình thường. Build cũ mất hiệu lực; báo cáo pilot trước đó chỉ là chứng cứ lịch sử của phạm vi và hash cũ. Mở rộng không có nghĩa đã hoàn thành full.

`_meta/book.json` có `schema_version: 1`, `title` thật, `status: pilot_partial|partial|full`, `source: {"mode":"pdf_direct"}`, `source_pdf: {"path":"...", "sha256":"..."}`, `pdf_page_count`, `scope: {"pdf_pages":[...], "chapters":[...]}`. `full` bắt buộc chứa toàn bộ trang PDF 1..N. Pilot chỉ xác nhận đúng các trang được nêu, không ngầm nhận đã bao phủ sách.

Mỗi trang trong scope có `_meta/pdf-pages/pNNNN.json`:

```json
{
  "schema_version": 1,
  "pdf_page": 17,
  "source_pdf_sha256": "<SHA-256 PDF>",
  "render_sha256": "<SHA-256 ảnh trang đã mở>",
  "review_status": "author_checked",
  "review_note": "Đã mở ảnh p17 và đối chiếu toàn bộ phần chữ, thứ tự, Nhật–Việt.",
  "checks": {"visual_review": true, "text_complete": true, "reading_order": true, "japanese_accuracy": true},
  "blocks": [
    {"id": "p0017-b001", "label": "Đầu bài/giới thiệu", "disposition": "included", "unit_ids": ["u-bai-01"]},
    {"id": "p0017-b002", "label": "Chân trang trang trí", "disposition": "excluded", "reason": "Không mang nội dung học"}
  ]
}
```

ID block là vị trí/nhóm nội dung do worker lập bằng cách đọc ảnh, không phải ID do OCR tự chứng thực. Chia đủ nhỏ để truy ngược mọi phần có nghĩa: hướng dẫn, hội thoại, ví dụ, giải thích, bài tập, lựa chọn, đáp án, mã audio/CD, hình/bảng có thông tin. Một block `included` phải có `unit_ids` khớp ngược với units; block `excluded` phải có lý do cụ thể. Trang thật sự trống dùng `blocks: []`, `page_disposition: "blank"`, `review_note` giải thích. Builder kết xuất `_meta/page-coverage.json` theo các evidence files và lưu hash. Không nhúng ảnh vào output; ảnh chỉ là cache tạm.

`_meta/units.jsonl` có một JSON mỗi unit: `unit_id`, `chapter`, `heading`, `source`, `review_status`, `issues`. Mỗi source là `{ "pdf_page": 17, "pdf_blocks": ["p0017-b001"] }`. Anchor `<a id="u-..."></a>` phải có trong chapter. Một unit có thể trỏ nhiều trang/blocks; mọi block included phải được ít nhất một unit trỏ đến. Giữ mạch và đủ nội dung sách; validator chỉ kiểm cấu trúc, không chứng minh độ đúng dịch/đủ ngữ nghĩa.

## Audio/CD

`_meta/audio.json` và `_meta/audio.md` bắt buộc trong mode mới. JSON chứa `book_title`, `source_pdf`, `book_identity` (title, edition, contributors, publisher, isbn, evidence_pages), `inventory_status`, `checked_pdf_pages`, `supplemental_evidence_pages`, `discs`, `tracks`, `locations`, `actual_files_status`, `notes`. `book_identity.evidence_pages` phải có ít nhất một trang đã kiểm, thường là bìa hoặc trang nhan đề. Markdown tóm tắt bằng lời những gì đã thấy và giới hạn phần chưa kiểm; builder lưu hash cả hai file. Danh sách `discs`/`tracks`/`locations` ghi các mục thật nhìn thấy trên PDF, mỗi mục có `label`, `pdf_page`, `pdf_block`; có thể thêm `note`, `disc_label`, `track_number`, `asset_path` khi có bằng chứng. Không suy ra track hoặc tệp âm thanh từ số bài. `inventory_status` là `unknown` khi chưa có tham chiếu, `documented` khi có tham chiếu cụ thể, `not_seen` chỉ khi đã kiểm **toàn bộ PDF** và không thấy tham chiếu. `actual_files_status`: `not_checked`, `not_provided`, `found`; `found` cần `actual_files` chứa đường dẫn tương đối repo và SHA-256 của file thật, script kiểm hash. Sự hiện diện của mã CD trên trang không chứng minh file audio đã có.

Nếu kiểm kê dùng trang ngoài scope học, liệt kê nó trong `supplemental_evidence_pages` và `checked_pdf_pages`, tạo `_meta/pdf-pages/pNNNN.json` tương tự nhưng block liên quan có `disposition: "audio_evidence"`; trang này không được xuất hiện trong units hay page-coverage học. Với pilot giới hạn, những trang chưa xem vẫn là `unknown`/chưa kiểm, không khẳng định cả sách không có audio. Mọi tham chiếu audio phải trỏ đến block có trong evidence trang đã kiểm.

## Giới hạn xác nhận

Script xác nhận hash, phạm vi, quan hệ block↔unit, coverage, trạng thái/checkpoint và một số lỗi text. Nó không thể chứng minh người làm đã thực sự xem ảnh hoặc rằng bản Việt, đáp án, mạch sách đúng. Root kiểm độc lập pilot trước khi scale; phần chưa xem luôn ở trạng thái chưa xác nhận.

Sách đã clean qua raw có thể dùng cùng các trường inventory trong `audio.json`, nhưng tham chiếu nên có thêm `raw_page` và `raw_anchors` bên cạnh `pdf_page`/vùng nguồn. Sách đó giữ `source.mode`/schema cũ của pipeline fork, không gắn `pdf_direct` và không tạo page evidence giả theo hợp đồng này. Inventory cũ chưa làm thì ghi pending/unknown rõ ràng tới khi được kiểm từ PDF; validator PDF-direct này không áp vào sách cũ.
