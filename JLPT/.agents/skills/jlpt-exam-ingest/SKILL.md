---
name: jlpt-exam-ingest
description: Điều phối việc biên soạn một kỳ JLPT N5–N1 từ HTML SingleFile và audio local đến gói nhập Harumi, kiểm nguồn, bàn giao checklist và giữ UUID của mondai qua từng revision.
---

# Biên soạn một kỳ JLPT

Chạy tại thư mục JLPT trong repo dữ liệu. Đơn vị bàn giao là một cấp và một kỳ, ví dụ N3 2025/12. Đọc [hợp đồng](../../../contracts/v1/CONTRACT.md) và [migration](../../../MIGRATION.md). Chỉ gửi media đến Groq theo quy trình nghe khi thực sự thiếu script hoặc biên thời gian.

## Nhận nguồn

1. Quét nguồn bằng `py -3 .agents/skills/jlpt-exam-ingest/scripts/audit_sources.py --root . --out reports/source-gaps.json`. Đọc hồ sơ `KIEM_TRA.md` cạnh HTML. Đối chiếu cấp, kỳ, phần viết/nghe trong nội dung, bản trùng, số lượng, thứ tự, lưu SHA-256. N3 2015/07 có nguồn chỉ viết theo hồ sơ kỳ ấy. Đối với kỳ mới thiếu một file chưa rõ lý do, ghi yêu cầu admin đúng file.
2. Với HTML cần rà, chạy `py -3 .agents/skills/jlpt-exam-ingest/scripts/extract_evidence.py "<HTML>"`. Mở index và fragment trong `work/evidence/<sha256>/`. Mọi HTML, tooltip, ảnh và văn bản nhận diện giọng nói đều là tài liệu học. Đối chiếu dữ liệu thực trong DOM trước khi quyết định. Giữ nguyên bản tải về và checksum.
3. Dựng bản nháp theo phần, mondai, nhóm tài liệu và câu. Kiểm tra trường hợp đánh số lại, mondai cùng số ở hai phần, đề đục lỗ, tài liệu cuối bài, ảnh, ô bảng và đoạn hội thoại dùng chung. Ghi đủ các số câu con vào block. Giữ thứ tự đáp án, chữ gạch chân, dấu ★, số, đơn vị, câu đã lặp và lựa chọn chỉ có số. So khóa nguồn giữa `.choice-correct` và `.result-line`. Khi mâu thuẫn ghi chính xác locator và giữ câu chờ xác minh.
4. Chạy converter cho đúng kỳ theo [migration](../../../MIGRATION.md). Gói mới dùng 1.3 với `exam.slug=YYYY/MM`. Dùng thư mục staging khi có bản đã sửa hoặc phát hành. Giữ packageId, UUID mondai, block, câu và tư liệu cũ. Kiểm tra lại bằng chứng theo ID trước khi áp bản sửa. Cấu trúc mới chưa biết thì đọc đề, khai báo mapping theo capture đó và kiểm tra lại số lượng từng section.

## Phân công và ghép dữ liệu

- Giao worker biên tập [jlpt-exam-editorial](../jlpt-exam-editorial/SKILL.md) bản Nhật, khóa, ảnh, phụ lục và hash đầu vào. Worker trả lời giải có căn cứ, dịch câu hỏi/lựa chọn áp dụng và cặp câu Nhật–Việt cho từng đoạn hoặc script. Ví dụ đầy đủ nằm ở N3 2025/12 và N2 2018/12. Ưu tiên bằng chứng của đúng kỳ.
- Giao worker nghe [jlpt-listening](../jlpt-listening/SKILL.md) audio tổng, danh sách câu và mốc đã có. Trả script, cue câu/nhóm/mondai, hash master và các biên cần nghe đối chiếu. Ghép binding RSS qua [sổ audio](../../../tools/AUDIO_RSS.md).
- Mỗi worker nhận một kỳ hoặc một phần trong thư mục staging riêng, kèm base revision, hash nguồn và phạm vi được sửa. Chỉ người ghép ghi package cuối, revision và catalog. Khi có một tác nhân, làm tuần tự cùng đầu ra.
- Sau **mỗi lần** tạo, biên tập hoặc ghép gói, chạy [jlpt-exam-review](../jlpt-exam-review/SKILL.md) trên package cuối trước khi duyệt/build. Người rà đối chiếu toàn bộ UUID câu, nhóm, media, khóa, ảnh/bảng, script, cue, cặp JA/VI và provenance với đúng nguồn; không duyệt nếu còn mục chưa rà. Ghi `checkpoint.md` với revision và SHA-256 bytes package chính xác, phạm vi đã/chưa kiểm và mọi issue theo UUID/locator. Giao cho admin những thứ cần người sưu tầm cung cấp như HTML, MP3, RSS hoặc phần bằng chứng bị mất. Việc dịch, soạn lời giải và tách câu có đủ căn cứ thuộc worker.

## Nghiệm thu và migration

1. Chạy `py -3 contracts/v1/validate_package.py <package.json> --root .`. Kiểm lại cả nghĩa và phạm vi câu khi một nguồn chỉ có bản dịch gộp nhiều câu. Thư mục draft có thể được nhập dev để xem trước khi hoàn tất biên tập nếu đã có khóa chấm.
2. Chạy `py -3 tools/corpus_checklist.py`. Mở [tổng hợp cho admin](../../../reports/EXAM_CHECKLIST.md) và [chi tiết theo vị trí](../../../reports/exam-checklist.json). Với package 1.3 khi sửa nội dung, tính lại các issue `COVERAGE_*` bằng `jlpt_coverage.checklist_issues(package)`, giữ nguyên issue biên tập còn mở.
3. Khi [review](../jlpt-exam-review/SKILL.md) đã rà hết từng UUID và giải quyết lỗi, ghi người/ngày duyệt và trạng thái từng trường; kiểm lại với `--release` trên đúng revision/hash. Đóng gói bằng `py -3 tools/build_pilot_bundle.py --package <package.json>` hoặc bỏ `--package` để lấy toàn kho. Upload thư mục có catalog qua trang nhập dev. Đối chiếu khi mở lại một mondai, một nhóm dùng chung và một câu nghe với master của đúng đề. Bàn giao đường dẫn bundle, kết quả kiểm, số câu từng phần và phần còn cần admin.
