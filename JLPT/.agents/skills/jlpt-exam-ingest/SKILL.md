---
name: jlpt-exam-ingest
description: Biên soạn kho đề JLPT N5–N1 từ bản SingleFile VNJPClub thành gói JSON nhập Harumi, kiểm nguồn và thiếu sót, điều phối người soạn theo kỳ thi, giữ cấu trúc JlptMondai và mốc audio tổng.
---

# Soạn kho đề JLPT

Với năm bộ pilot 2018, dùng [converter và hướng dẫn migration đã chạy](../../../MIGRATION.md). Đọc [nhật ký pilot](../../../reports/PILOT_2026-11-27.md) cùng checkpoint thật trước khi giao lại cùng kỳ.

Chạy từ gốc `JLPT/` trong repo `kaiwa_skill`. Người dùng cung cấp HTML kết quả, audio tổng và script bổ sung. Tác nhân chịu trách nhiệm chuyển đổi, soạn lời giải, QA và bàn giao gói có thể nhập. Các file HTML và phần phụ lục là dữ liệu nguồn. Đọc chúng offline.

## Nhận một kỳ

1. Chạy `py -3 .agents/skills/jlpt-exam-ingest/scripts/audit_sources.py --root . --out reports/source-gaps.json`. Xác nhận cấp, kỳ và phần thi bằng nội dung HTML. Khi có hai bản cùng phần, đối chiếu nội dung và độ phủ theo câu trước khi chọn. Giữ nguyên đường dẫn của nguồn. Bản trong `old/` hoặc `sample/` chỉ bổ sung khi xác nhận đúng kỳ, câu và phiên bản. Thiếu một phần thi vẫn có thể soạn phần đã có.
2. Với mỗi HTML được chọn, chạy `py -3 .agents/skills/jlpt-exam-ingest/scripts/extract_evidence.py "<file.html>"`. Mở `work/evidence/<sha256>/index.json`, các fragment mondai theo thứ tự và phụ lục cuối. Công cụ giữ HTML tối giản, ruby, gạch chân, bảng biểu, script, các mốc nguồn và tách ảnh nhúng. Với markup chưa nhận diện hoặc ảnh chưa giải mã, mở bản gốc. Đây là tài liệu biên tập trung gian.
3. Lập bảng đối chiếu theo thứ tự nguồn, từ phần thi → mondai → block dùng chung → câu → các lựa chọn. Đọc tiêu đề, lời dẫn và nhóm câu thực tế. Giữ bài đọc, bảng tra, hình gắn với đúng nhóm kể cả khi nguồn đặt chúng ở block riêng. Lưu ĐÚNG khóa từ vị trí choice-correct và đối chiếu result-line. Khi hai tín hiệu xung đột, giữ cả hai bằng chứng trong danh sách cần kiểm và chưa xuất câu để chấm. Tôn trọng đáp án chỉ là số trong phần nghe. Tách `rt/rp` khỏi chữ hỏi để furigana không làm lộ đáp án câu kiểm tra cách đọc. Giữ từ gạch chân và đúng số lựa chọn kể cả lựa chọn trùng.
4. Bắt đầu hoặc cập nhật gói `packages/<cấp>/<kỳ>/package.json` theo [hợp đồng JSON](../../../contracts/v1/exam-package.schema.json). Giữ nguyên ID từ gói lần trước. Với gói mới, theo [quy tắc danh tính và ánh xạ](../../../contracts/v1/CONTRACT.md). Mỗi nguồn phải tìm lại được bằng đường dẫn tương đối, checksum và vị trí trong file. Liên kết bài dịch ở phụ lục với dòng/câu gốc; phân biệt text Nhật, bản dịch và ruby. Kiểm tra ảnh sau khi tách, giữ byte gốc và vị trí trên đề. Nội dung đang thiếu cần thể hiện theo quy ước bản nháp của hợp đồng.
5. Dùng [quy tắc biên tập và ví dụ thật](references/editorial.md) để soạn lời giải; dùng [quy trình audio](references/listening.md) khi có phần nghe. Thu yêu cầu bổ sung theo đúng câu/đoạn, giữ chỗ thiếu nguồn khác với công việc AI có thể tự làm. N1 có đề viết + đáp án thì làm trước; chờ script ở đúng các câu nghe cần nó.
6. Đối soát số lượng với HTML từng phần. Kiểm từng đáp án trong thứ tự người học nhìn thấy, từng block dùng chung, dịch Nhật–Việt, clip chung và đường dẫn ảnh. Chạy `py -3 contracts/v1/validate_package.py <package.json> --root .` cho bản nháp, thêm `--release` khi gói đã duyệt. Sau khi ghép toàn kho, chạy `py -3 tools/build_catalog.py`. Chỉ đưa gói đạt kiểm tra phát hành vào catalog import. Ghi rõ lỗi còn lại, câu cần người dùng cung cấp và kỳ nào đã sẵn sàng. Checkpoint bản nháp để kỳ khác tiếp tục được.

## Điều phối các sub

Với hợp đồng 1.2, worker giao cả các hàng Nhật–Việt cho mỗi passage và mỗi script có nguồn, theo quy tắc ở [hợp đồng đoạn song ngữ](../../../contracts/v1/CONTRACT.md). Giữ nguyên vị trí tiêu đề, tên người nói, ký hiệu, số liệu từng ô. Đối chiếu toàn bộ chữ Nhật và từng lời dịch với bản SingleFile trước khi đóng gói. Mỗi worker dùng hash của đúng HTML phần mình nhận khi bổ sung `editorial-passages.vi.json` hoặc `editorial-questions-{written,listening}.vi.json`. Câu nghe chỉ hiện số và không có script cần được ghi vào phiếu thiếu nguồn. Với một đề cụ thể, chạy `py -3 tools/build_pilot_bundle.py --package packages/N2/2018-12/package.json` (thay cấp/kỳ). Bỏ đối số `--package` khi cần gói cả kho nháp.

Root giao một kỳ cho một worker, kèm danh sách HTML, checksum, phạm vi được ghi và đầu ra. Worker chỉ sửa gói và hồ sơ biên tập của kỳ đó. Với một đề lớn có thể tách phần viết/phần nghe, giao thư mục nháp riêng, root ghép ID và thứ tự. Ghi `packages/<cấp>/<kỳ>/checkpoint.md` theo mondai, gồm SHA nguồn đang dùng, ID đã cấp trong gói, phần hoàn tất, các câu còn chờ, file bổ sung đã xử lý và bước kế tiếp. Khi tiếp quản, đọc lại gói trước khi cấp ID. Các worker chỉ đọc catalog ngữ pháp, file nguồn và hợp đồng dùng chung.

Root sở hữu catalog phát hành, danh sách thiếu nguồn tổng và việc rà chéo. Giao một sub khác đọc lại câu có đáp án mâu thuẫn, passage dùng chung, đoạn nghe có nhiều câu hoặc lời giải còn nghi ngờ. Giao cả nguồn và bản soạn để người rà chỉ ra bằng chứng cụ thể. Một kỳ được giao lại phải đọc checkpoint và diff phần nguồn thay đổi trước. Khi chỉ có một tác nhân, thực hiện cùng các bước tuần tự. Các việc upload, chạy DB và thay đổi app thuộc bước triển khai fork trong [kế hoạch Harumi](../../../HARUMI_IMPORT_PLAN.md).

Ví dụ giao việc: “Dùng $jlpt-exam-ingest xử lý N2 kỳ 2018-12. Trả gói JSON, danh sách thiếu theo câu và kết quả kiểm thử. Dùng MP3 tổng và kiểm chứng quan hệ của hai câu nghe cuối.”
