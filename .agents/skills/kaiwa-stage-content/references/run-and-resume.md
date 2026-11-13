# Chạy và phục hồi biên soạn nội dung

Phạm vi: lộ trình, nội dung và gói dữ liệu xuất. Không làm feature/DB/engine Harumii. Chất lượng ưu tiên hơn tốc độ/quota; không giảm độ phủ hoặc bỏ nguồn cần thiết để vừa một lượt chat. Chia lượt và checkpoint, giữ phần chưa làm rõ trong next action.

## Một bản nội dung gốc

Lượt mới dùng canonical mode mặc định. **Chỉ soạn lời bài học trong `harumii-stage.json`.** Nguồn/nguồn gốc nội dung ở `sources.json`, `source-map.json`; bằng chứng đọc bài trước và tái dùng ở `learning-map.json`; quyết định/chỗ còn thiếu ở `editorial.md`.

`stage_work.py sync/validate/finalize` tự sinh `stage.json` và các file knowledge/vocabulary/grammar/situation/shadowing/live. Mở `kaiwa_skill/PREVIEW.html` để xem JSON export. Các file Markdown xuất kèm do Python render tại máy, không gọi model. Khi sửa câu, chỉ sửa bản canonical rồi sinh lại; không yêu cầu model viết thêm bản Markdown, chép nguyên JSON vào báo cáo hoặc đọc lại toàn bộ các bản dẫn xuất. Vocabulary item ID dẫn xuất là hash từ theo node, không đổi vì sắp lại list. Turn ID dẫn xuất có prefix node; review metadata có thể tham chiếu whole node nếu không cần pin từng lượt.

`source-map.json.nodes` có đúng một mục cho mỗi material node: `{authorship: source_quote|source_adaptation|original_extension, source_refs: [...]}`; nhãn từng câu nằm trong canonical. `vocabulary_evidence` ghi dấu vết trích từ; `sequence_units` khai báo đơn vị sách đã chọn; `audio_packs` liên kết lời Nhật với pack/CD/track. Phần giữ nguyên/chuyển soạn phải có nguồn đã đọc trong sổ nguồn; phần AI viết mới không gán thành nguyên văn sách. Compiler không chứng minh tiếng Nhật hoặc bản dịch đúng.

## Trình tự

1. Đọc AGENTS, SKILL và các reference được chỉ định; xác định UID/phạm vi được giao.
2. `status` kiểm owner/current trước; không mở trùng một chặng. `begin` cho chặng mới; `begin --from-current` cho nâng cấp.
3. Xem chỉ mục và các gợi ý phân bổ nếu có. Chọn theo topic và cấp, đọc phần nguồn và ghi tra cứu CD của pack đã chọn. Có thể bắt đầu từ bất kỳ bài nguồn phù hợp nào.
4. Đọc chỉ mục 27 sách và phần nguồn được chọn theo topic; cân nhắc kiến thức cũ phù hợp khi viết mới. Không bắt đọc/tái dùng đủ hai bài trước hoặc ghi debt nếu chúng chưa có. Nếu ghi đã tham khảo thì phải đọc thật.
5. Viết từng cụm trong canonical source, giữ ID, nghĩa Việt, nhánh và gối đầu tự nhiên nếu phù hợp. Gói mới có source_registry và authorship/source_refs từng utterance; từ vựng trích ngược ở dạng từ điển, ghi một vài dấu vết trong source-map.vocabulary_evidence. Chạy `sync` khi JSON/schema đủ; bản nháp chưa parse được vẫn checkpoint/recover giữ nguyên byte.
6. Checkpoint sau cụm đáng kể: ghi node/sự kiện vừa xong, nguồn vừa đọc, điều cần đọc lại và next action cụ thể. Pause khi cần nghỉ; không chốt bài để né quota.
7. Đọc lại toàn chặng theo danh sách “Trước khi chốt” của `editorial-workflow.md`: hội thoại, độ vừa sức, dịch, nguồn từng câu, pack CD, challenge và free talk. `validate` (đọc cả các dòng `Note:` về kế hoạch), rồi `finalize --editor-reviewed` với nhận xét thật. Script không thay review.
8. `kaiwa_exchange.py pack` từ canonical file của snapshot chốt, vào thư mục xuất mới. Có `stage-preview.md`, knowledge MD, hai phần challenge theo variant, free talk, manifest. Không chạy DB/TTS.

## Tác nhân khác, Codex hoặc Claude Code tiếp tục

Không cần lịch sử chat còn nguyên. Prompt khởi động phải chỉ rõ repo, SKILL, UID và run; không giả định công cụ tự đọc đúng folder skill. Model/reasoning là cấu hình của runner, không phải điều kiện giải mã checkpoint. Không tự spawn hoặc đổi model nếu chưa được yêu cầu.

Đọc `stage_work.py status`, checkpoint, `editorial.md`, source canonical, nguồn/spec đã pin. Nếu paused và file/spec không đổi, dùng `resume`. Nếu tiến trình cũ chết, quota hết hoặc file/spec đã đổi, xác nhận nó đã dừng rồi `recover --run RUN --ack-stopped`; bản cũ được giữ, run mới có draft riêng. Không xóa owner/lock để chạy nhanh; không sửa hash để che thay đổi nguồn.

Sau recovery, đọc phần chưa checkpoint, sửa JSON dở nếu có, tái đối chiếu phần spec/nguồn thay đổi rồi tiếp từ next action. `--clear-stale-guard` chỉ dùng khi guard còn lại từ tiến trình đã dừng. Bảo đảm chỉ một tác nhân đang viết UID đó.

Byte chưa từng ghi xuống đĩa không thể cứu. Checkpoint/status là trạng thái biên soạn, không là bằng chứng nội dung đạt chất lượng; không tự đánh finalized hoặc editor-reviewed khi chỉ thấy script chạy thành công.

Prompt mẫu:

> Làm tại D:\CODE\git\kaiwa_skill. Đọc AGENTS.md và .agents/skills/kaiwa-stage-content/SKILL.md, đặc biệt references/run-and-resume.md. Tiếp chặng UID …, run …, từ checkpoint/next_action thực tế. Tác nhân cũ đã dừng. Giữ nội dung đã ghi, không làm lại từ đầu, không sửa bunpou/knowledge/PDF hoặc repo Harumi. Chọn pack theo chủ đề và cấp. Giữ nguyên lời Nhật, thứ tự trong track và thông tin tra CD. Review nguồn; chỉ chốt phạm vi được giao sau khi đọc lại nội dung.
