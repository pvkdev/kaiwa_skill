# Dữ liệu và chỉnh sửa V5

- `BUILD_MANIFEST.json`: thứ tự/cấp/cụm, UID, phạm vi và chủ sở hữu chặng; chín chặng gộp có đích chuyển tiếp. Đầu vào thiết kế do root duy trì.
- `work/stages/<stage_key>.json`: mục tiêu nói, kiến thức dự kiến, event/role, tình huống và nhánh. Đây là checkpoint biên tập cho từng chặng.
- `KAIWA_CHANG_V5.jsonl`: dữ liệu đã ghép theo thứ tự, một dòng/chặng. `uid` bất biến; `key` là đầu mối biên tập; `display_code` có thể đổi khi sắp lại. `lesson_status=not_authored` phân biệt roadmap với bài hoàn chỉnh.
- `events[].id`: ID cục bộ trong chặng, có tên và vai. `situations[].event_id` trỏ về họ sự kiện.
- `situations[].id`: ID cục bộ được giữ khi nâng cấp. `uid` của tình huống được dựng ổn định từ UID chặng + ID cục bộ. Không chèn rồi đánh lại ID cũ, không tái sử dụng ID đã bỏ cho tình huống khác.
- `branch`: routine, accepted, declined, conditional, pending, alternative, misunderstanding, problem, resolved, unresolved, follow_up. Nhãn là gợi ý diễn biến, không rubric hoặc điểm người học.
- `continues_from`: ID tình huống có trước trong cùng chặng. Không tự trỏ, không chu trình; có thể nối qua sự kiện khi hợp logic. Không phải cổng bắt người học đi đúng nhánh.
- `origin=ai_authored`: mọi phác thảo tình huống mới là AI biên soạn. Sổ nguồn có thể hỗ trợ bối cảnh/dữ kiện/cách nói; không gán nguyên văn hoặc audio cho phần mới.
- `source_basis`: tách token hạt giống/ngân hàng cũ, sách cần tra, đoạn preview đã đọc và nghiên cứu ngoài. Đầu mối tra khác nguồn đã được dùng cho hội thoại.
- `recommended_previous_stage_uids`: thứ tự chặng gợi ý. Khi viết bài vẫn phải đọc hai bài thực có gần nhất và phần liên quan; không coi roadmap là chứng minh kiến thức đã dạy.
- `related_stage_uids`: liên quan nội dung, không điều kiện mở bài. `cross_stage_refs` giữ key biên tập để tra ngược.
- `chang_registry.json`: chỉ các UID đang hoạt động; dùng cùng `CURRENT_ROADMAP.json` để helper biên soạn tìm đúng phiên bản.
- `MIGRATION_V4_1.json`: đầy đủ 194 mã cũ, giữ UID hoặc nhiều đích nhận nội dung. Không dựng lại chặng đã gộp chỉ bằng mã cũ.
- `TRAVEL_CONTEXTS.json`: 16 lớp bối cảnh địa danh, có host UID; không phải chặng đánh số thêm.
- `SOURCES_EXTERNAL.json`: gộp ledger có namespace daily/support/work; trạng thái mở trang/trích tìm kiếm/chỉ mục và giới hạn đọc phải giữ nguyên.
- `ROOT_ENRICHMENTS.json`, `EDITORIAL_REVIEW.json`: các bổ sung/sửa biên tập và snapshot đã nghiệm thu. `STATS.json`, Markdown và HTML là bản dẫn xuất.

## Tiếp tục hoặc nâng cấp có mục tiêu

1. Đọc BUILD_STATE, assignment của owner, file chặng có sẵn và lý do còn thiếu. Không reset checkpoint hoặc viết đè file đã có bằng helper khởi tạo.
2. Khi đổi phạm vi/thứ tự, sửa manifest; giữ UID. Khi sửa tình huống, sửa đúng file chặng và giữ ID; thêm ID lớn hơn số đã dùng. Nếu bỏ/gộp cần ghi lại đích thay thế và kiểm liên kết đến nó.
3. Chạy `py -B -X utf8 tools/roadmap_v5.py validate`. Bộ kiểm phát hiện ID/nhánh/con trỏ, không chứng minh đủ mọi tình huống hoặc chất lượng ngữ nghĩa.
4. Chạy `render` để xem bản dẫn xuất; đọc lại phần bị ảnh hưởng. `publish` yêu cầu bản ghi review khớp hash manifest, từng file chặng và ledger nguồn. Không tự sửa hash để vượt một thay đổi chưa đọc.
5. Khi bắt đầu viết bài, dùng `.agents/skills/kaiwa-stage-content`. Bài học có hệ revision riêng; không gộp trạng thái roadmap với trạng thái nội dung app.

Mọi chặng mở tự do. Không trường học viết, test, điểm hoặc điều kiện đạt được thêm vào dữ liệu này.
