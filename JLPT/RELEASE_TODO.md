# Kế hoạch bàn giao kho JLPT và đưa đề vào Harumi

Mốc kiểm kê 28/11/2026. Tất cả thao tác triển khai và nghiệm thu diễn ra trên dev local. Mục tiêu là chuẩn bị skill và ứng dụng trong khi admin tải raw. Chỉ mở hàng đợi biên soạn toàn kho sau khi admin báo đã tải xong. Trong tài liệu này, “publish” là cho phép người học dùng đúng revision đã duyệt trong Harumi.

**Quyết định hiện hành.** Claude Opus triển khai admin M4.1 theo [hợp đồng admin](../../harumi/design/jlpt/ADMIN_IMPLEMENTATION_CONTRACT.md). Codex phụ trách repo dữ liệu. M4.2 và mọi nghiệm thu bằng tài khoản người học được hoãn tới sau khi chủ kho xác nhận dữ liệu đạt. “Publish” trong giai đoạn này chỉ ghi nhận revision đã duyệt ở admin dev.

## Bàn giao phía dữ liệu

- Đã có lệnh `tools/batch_job.py` nhận việc, kiểm xung đột worker, thay đổi nguồn và revision khi tiếp tục. Cách ghi checkpoint và ghép từng kỳ nằm trong skill ingest.
- Đã có `tools/build_publish_ready.py` kiểm release, đối chiếu raw, biên nhận SHA của reviewer, gom các cấp và dùng chung asset. Lần xuất kho thật có 0 gói approved. [Bundle tổng hợp để Claude kiểm đường thành công](work/evidence/admin-contract-fixture/publish-ready/catalog.json) có hai gói N3/N5 và một ảnh dùng chung, nằm ngoài kho thật.
- Đã chạy lại đối chiếu HTML của ba pilot trên công cụ hiện hành. Bản staging mới là [12/2018 r5](work/evidence/admin-readiness/2018-12/packages/N3/2018-12/checkpoint.md), [12/2024 r3](work/evidence/admin-readiness/2024-12/packages/N3/2024-12/checkpoint.md) và [12/2025 r6](work/evidence/admin-readiness/2025-12/packages/N3/2025-12/checkpoint.md). Kiểm tĩnh qua renderer Harumi cho 432 + 422 + 390 điểm bấm, bảng JA/VI tương ứng 4×6, 3×5 và 3×3, 3×5 (cột × hàng). Các issue nguồn, nghe cue thật và preview vẫn theo hồ sơ từng kỳ.

## Mốc đối chiếu trước triển khai

| Hạng mục | Đã có | Phần còn thiếu |
|---|---|---|
| Biên soạn | Bốn skill ingest, editorial, listening, review. 30/30 nguồn viết N3 trong danh mục có mapping khớp SHA. Ba pilot giữ 304 lời giải nguồn và 1.244 cặp JAVI căn được bằng mã Harumi. | Kiểm mẫu thật N1/N2/N4/N5 theo workflow mới, hợp nhất checkpoint của các worker và sửa cờ sai ở nhãn hình, ranh giới bảng, câu trích dẫn. |
| Dữ liệu phát hành | Sáu gói trong `packages/` đều là draft tại thời điểm kiểm. Ba revision đã sửa nằm ở staging. N3 12/2024 r2 đủ khóa để nhập thử, 12/2018 r4 và 12/2025 r5 mỗi gói có một câu chưa thể chấm. | Chưa có gói pilot nào đạt release. `tools/build_catalog.py` lọc approved và chạy validator release. `tools/build_pilot_bundle.py` gom asset nhưng chấp nhận draft. Cần bộ xuất release có cả hai tính chất. |
| Admin / BE | Admin có nhập thư mục, chọn đề, preview, chỉnh sửa, furigana. Import API có quyền Admin, giới hạn Development, một transaction/đề, đối soát sau ghi, kiểm version khi ghi đè. Schema JSON ở hai repo trùng SHA. | Cần phân biệt quyền nhập draft và điều kiện xuất hiện cho người học. Reader hiện yêu cầu khóa cho từng câu và dùng đường dẫn media pilot local. |
| DB và người học | `JlptExamSet.IsPublished`, `JlptMondai`, bảng nối theo thứ tự và metadata import đã tồn tại. Preview có làm bài, nộp, summary và lưu phiên bằng sessionStorage. | `ExamPracticePage.tsx` dùng `jlptPracticeMock`. Cần nối danh sách đề đã publish, tạo/lưu/khôi phục lượt thật theo user, chấm và xem lại trên API/DB. |

Kiểm tra đã chạy trên working tree ngày 28/11: 12 test Python của pipeline nghe/RSS, 23 test FE của importer, lượt preview và căn câu, 8 test BE của importer đều đạt. BE chạy bằng SDK .NET 9 trong Docker trên bản sao tạm. Đợt này chưa chạy round-trip PostgreSQL hoặc thử tài khoản người học trong trình duyệt. Restore BE có cảnh báo NuGet NU1902/NU1903 cho ImageSharp 2.1.13.

## Thư mục bàn giao

Quy ước đang dùng dưới `JLPT/`. Ví dụ dưới đây minh họa tên thư mục. Một kỳ chỉ xuất hiện khi đúng revision đã qua release.

```text
publish-ready/
  catalog.json
  N3/
    JLPT-N3-2024-12-r02/
      package.json
  assets/
    sha256/…
```

Các cấp N5, N4, N3, N2, N1 dùng cùng quy ước. Mỗi kỳ xuất một revision đang được duyệt. `catalog.json` trỏ tới đường dẫn tương đối, lưu packageId, revision và SHA đúng bytes. Asset giữ nguyên đường dẫn trong package và được dùng chung theo SHA. Admin chọn thư mục gốc để nhập cả kho hoặc chọn một đề trong danh sách preview. Lịch sử biên tập và chứng cứ nguồn ở kho tác giả. Hash là định danh kỹ thuật, tên thư mục giúp người dùng tìm theo cấp và kỳ. Ví dụ r02 trong sơ đồ chưa phải bản được phép publish.

## TODO theo thứ tự phụ thuộc

### A. Skill và đầu ra phát hành · repo JLPT

- [x] **A1 · Sửa các phép kiểm đã báo nhầm.** Dùng đúng hai bài nghe chỉ có nhãn hình, poster 12/2024 và câu trích dẫn trong bài súp 12/2025 làm mẫu hồi quy. Kiểm bảng theo nội dung ô, thứ tự và ranh giới bảng từ DOM. Kiểm quote có ngữ cảnh. Chạy thêm ca đối chứng cố ý mất một ô, một câu dịch hoặc sai nhãn. Điều kiện đạt là chấp nhận mẫu đúng và vẫn báo đúng vị trí của mẫu sai.
- [x] **A2 · Chuẩn hóa vận hành nhiều kỳ.** Cập nhật skill ingest/review với hàng đợi theo level/kỳ, SHA nguồn, base revision, người phụ trách, thư mục staging và checkpoint. Mỗi worker sở hữu một kỳ. Coordinator ghép và chỉ đưa đúng bytes đã review sang kho canonical. Chạy lại sau gián đoạn phải tiếp tục được, phát hiện nguồn vừa đổi, tránh ghi đè bản biên tập và báo riêng việc AI sửa được với tư liệu cần admin. Giữ lời giải nguồn, bản Việt đã điền đáp án ở summary, ánh xạ JA/VI, nhóm câu và timestamp trên master theo hợp đồng.
- [x] **A3 · Dựng bộ xuất `publish-ready/`.** Dùng lại kiểm tra của catalog và bundle. Yêu cầu approved, review đúng SHA/revision, validator release đạt, khóa chấm đủ, nguồn và asset khớp. Build vào staging rồi chuyển cả bộ sau khi kiểm xong. Khi rút duyệt, loại revision khỏi danh mục mới. Nếu toàn kho chưa có đề đạt, báo rõ kho rỗng và xử lý riêng thao tác rút bản cũ để tránh đưa nhầm catalog cũ lên app. Kiểm tình huống lỗi giữa chừng, cùng asset nhiều đề, trùng kỳ, đổi revision, chọn nhập riêng và nhập cả kho. Bộ bàn giao chỉ chứa catalog, package và media cần dùng.
- [ ] **A4 · Chốt nghiệm thu skill.** Chạy lại ba pilot bằng quy trình chung, thêm fixture gói đạt và gói lỗi để thử cả hai nhánh xuất. Khi có raw của cấp mới, đối chiếu một kỳ thật mỗi cấp, gồm N1 thiếu lời giải và trường hợp cần STT. Ghi số câu theo nguồn, tỷ lệ lời giải gốc/AI, UUID còn mở, kiểm bản dịch, ảnh, bảng, cue và bằng chứng nghe/preview. Chỉ công bố mức hỗ trợ đã kiểm của từng cấp.

### B. Harumi M4.1 · nhập, lưu và publish

- [ ] **B1 · Chốt hợp đồng nhập và hiển thị.** Dùng schema 1.3 hiện có làm điểm xuất phát. Kiểm FE và BE với đường dẫn mới, slug dữ liệu `YYYY/MM` và slug route hiện hành, level, revision, số câu từng phần, master và cue theo UUID. Giữ luồng nhập draft riêng cho admin. BE phải tự kiểm điều kiện publish trên revision thực tế, kể cả khi client gửi trực tiếp hoặc admin vừa sửa đề. Chốt hành vi đối với một revision mới của đề đang publish để bản sửa chưa duyệt không xuất hiện cho người học.
- [ ] **B2 · PostgreSQL và media.** Giữ đơn vị lưu `JlptMondai` và liên kết nhóm câu. Kiểm schema/indices hiện hành trước khi thêm migration. Ràng buộc danh tính đề, revision đã publish và nguồn media của từng mondai trong đề trộn. Dùng presigned upload hiện có cho ảnh trên R2 khi cấu hình, RSS cho bản thu đã đối chiếu và nguồn local cho dev. Retry upload/transaction theo hash. Nghiệm thu bằng PostgreSQL thử nghiệm với nhập mới, nhập lại, nhập đồng thời, đổi thứ tự, ghi đè sau chỉnh tay và lỗi giữa gói. Kiểm readback UUID, ảnh, full master, script, cue, bảng và cặp dịch.
- [ ] **B3 · Admin.** Trên route nhập mới cho xem level/kỳ/revision, kết quả từng đề, lý do bị chặn, retry riêng đề lỗi, mở preview và publish đúng revision. Giữ editor, nút tạo lại furigana và luồng pool cũ. Test qua Swagger và trình duyệt với tài khoản admin và người học. Dev local là môi trường nghiệm thu.

### C. Hoãn theo yêu cầu · Harumi M4.2, sau khi dữ liệu đã đạt

- [ ] **C1 · DB và slice lượt làm.** Đối chiếu `UserExamAttempt` trong M4 và migration thực tế. Thiết kế dữ liệu tiến độ theo user, phạm vi đề/mondai, revision cố định, đáp án chọn, phần đã nộp, thời hạn và kết quả. Lượt cũ phải xem lại đúng bộ câu/đáp án sau khi nhập revision mới. Chốt chiến lược snapshot hoặc tham chiếu revision bất biến trước migration. Viết và thử migration trên DB trống và bản sao DB dev đang có đề.
- [ ] **C2 · API thật.** Liệt kê đề đã publish, khởi tạo theo bộ đề hoặc mondai, lưu lựa chọn, tiếp tục, thoát, nộp từng phần, hoàn thành, xem lại, làm lại. BE xác nhận user sở hữu lượt, thời gian và trạng thái, tính điểm, xử lý retry sau mất kết nối. Khi đang làm chỉ trả đề và tư liệu hợp lệ cho chế độ đó. Chỉ trả khóa chấm, lời giải, bản dịch và script học tập khi đã nộp phần tương ứng. Kiểm luyện thường tiếp tục từ DB, thi thử thoát có xác nhận và hủy lượt theo quy tắc đã chốt. Hai đồng hồ đọc/nghe độc lập. Đối chiếu đủ các mode được giao trong checkpoint M4.2, kể cả luồng thi thử theo lịch nếu dùng cùng bộ đề.
- [ ] **C3 · FE người học.** Thay dữ liệu mẫu tại route luyện liên quan bằng API, tái dùng phần đề/summary đã làm trong preview. Đề đầy đủ đi từ phần đọc sang nghe; hỗ trợ phạm vi riêng và nhóm mondai dùng chung tài liệu. Audio chạy liên tục theo phạm vi, nút câu hiện tại seek tới mốc. Khi chuyển giữa mondai khác bản thu thì đổi đúng master. Kiểm trên mobile/PC, theme, toolbar, grid, timer, thoát/tiếp tục và xem lịch sử. Summary kiểm dịch câu đã điền, JA/VI/JAVI, tra từ, furigana, script hội thoại, ảnh và bảng.

### D. Nghiệm thu tích hợp và mở hàng đợi

- [ ] **D1 · Nghiệm thu admin trên dev.** Chạy quy trình nhập, sửa, furigana, preview, kiểm điều kiện publish và thu hồi bằng fixture riêng, thử RSS và seek qua UI admin; ghi revision/SHA, log PostgreSQL, Swagger và desktop/mobile. Các bước người học thuộc C và nghiệm thu sau khi dữ liệu đạt.
- [ ] **D2 · Bắt đầu chạy kho raw** sau khi admin xác nhận hoàn tất tải và các bước nghiệm thu liên quan đạt. Gom các đề đã duyệt vào đúng cấp trong `publish-ready/`. Một đề đang chờ nguồn giữ checkpoint riêng và các đề khác tiếp tục được.

**Việc tiếp theo:** Claude Opus thực hiện B1–B3 và D1 trên Harumi. Repo dữ liệu tiếp tục A4 khi có nguồn cấp mới. D2 chờ chủ kho hoàn tất tải raw.

## Điểm vào khi tiếp quản

- Repo dữ liệu dùng [skill điều phối](.agents/skills/jlpt-exam-ingest/SKILL.md), [skill review](.agents/skills/jlpt-exam-review/SKILL.md), [hợp đồng](contracts/v1/CONTRACT.md), [catalog release](tools/build_catalog.py) và [migration hiện tại](MIGRATION.md).
- Repo Harumi dùng [hướng dẫn JLPT](../../harumi/JLPT_EXAM/MIGRATION.md), [thiết kế M4](../../harumi/design/old/m4_exam.md), [checklist milestone](../../harumi/design/old/milestones_detail.md), [handler nhập](../../harumi/backend/src/Harumi.Exam/Features/ImportJlptPackage/ImportJlptPackageSlice.cs) và [route luyện đang dùng dữ liệu mẫu](../../harumi/frontend/src/components/exam/practice/ExamPracticePage.tsx).
