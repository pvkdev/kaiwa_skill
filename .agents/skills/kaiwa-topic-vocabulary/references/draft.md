# Bản thảo từ vựng V12 cho một chặng

Pilot nằm ở `kaiwa_skill/planning/v12/pilot/<stage_code>/vocabulary.json`. Bản sau duyệt hàng loạt nằm ở `kaiwa_skill/planning/v12/stages/<stage_code>/vocabulary.json`. Đầu vào là chặng trong `kaiwa_skill/planning/v11/learner.json`. Mỗi thư mục chặng có `vocabulary.json` và `status.json`.

## vocabulary.json

```json
{
  "stage_uid": "…",
  "stage_code": "T-044",
  "admin_sources": {
    "jp-post-intl": {"kind": "web", "title": "国際郵便 | 日本郵便", "url": "https://www.post.japanpost.jp/int/", "accessed": "2026-11-18",
                     "use_vi": "Tên dịch vụ EMS, 国際小包 và giấy tờ 税関告知書"},
    "mimi-n3": {"kind": "book", "book_id": "VOCAB-N3", "path": "kaiwa_skill/knowledge/…/chapters/tu-vung-0187-0376.md",
                "start_line": 10, "end_line": 40, "use_vi": "Cặp 包む/届く và nghĩa"}
  },
  "dropped_topics": {},
  "groups": [
    {
      "id": "g01",
      "title_vi": "Nội dung và nơi đến kiện quốc tế",
      "v10_topic": "Nội dung và nơi đến kiện quốc tế",
      "terms": [
        {"id": "T-044-v001", "ja": "送る", "reading": "おくる", "vi": "gửi", "pos": "verb",
         "level_hint": "N5", "origin": "dialogue",
         "evidence": [{"utterance_id": "2da66c90-…-u01", "surface": "贈りたい"}]},
        {"id": "T-044-v002", "ja": "税関告知書", "reading": "ぜいかんこくちしょ", "vi": "tờ khai hải quan (gửi kèm bưu kiện)",
         "pos": "noun", "level_hint": "none", "origin": "topic_extension",
         "level_note_vi": "Tên giấy tờ bắt buộc khi gửi hàng quốc tế, nhân viên sẽ nhắc đến.",
         "source_refs": ["jp-post-intl"]}
      ]
    }
  ]
}
```

### Gốc

- `stage_uid`, `stage_code` khớp chặng V11.
- `admin_sources`: object theo mã cục bộ, có thể rỗng. Nguồn sách có `kind: book`, `book_id` (B01–B27 theo manifest catalog27, hoặc `VOCAB-N3`, `VOCAB-N2`, `VOCAB-N1` cho ba bảng từ), `path` Markdown từ gốc repo, `start_line`, `end_line` (tính từ 1, gồm hai đầu), `use_vi`. Nguồn web có `kind: web`, `title`, `url`, `accessed` dạng YYYY-MM-DD, `use_vi`.
- `dropped_topics`: object `{nhóm V10: lý do}` cho nhóm V10 không giữ lại. Thường rỗng.
- `groups`: mảng nhóm theo thứ tự học.

### Nhóm

- `id` ổn định trong chặng (`g01`, `g02`… cấp một lần, không đánh lại khi sắp xếp).
- `title_vi`: tên nhóm hiện cho người học.
- `v10_topic`: đúng chuỗi nhóm V10 mà nhóm này phủ, hoặc `null` cho nhóm thêm mới. Nhóm thêm mới có `added_reason_vi`.
- `terms`: mảng mục từ, không rỗng.

### Mục từ

- `id`: ổn định, duy nhất trong chặng. Đề xuất `<stage_code>-v001`. Cấp một lần; sửa nghĩa hay chuyển nhóm vẫn giữ ID; mục mới lấy số tiếp theo.
- `ja`: dạng mục từ (động từ thể từ điển, tính từ い dạng cơ bản, tính từ な không kèm な/だ). Không có dấu câu kết câu.
- `reading`: chỉ kana (hiragana, katakana, ー). Không ghi romaji.
- `vi`: nghĩa tiếng Việt theo chủ đề.
- `pos`: `noun`, `verb`, `i_adj`, `na_adj`, `adverb`, `expression` (cụm cố định), `counter`, `other`.
- `level_hint`: `N5`, `N4`, `N3`, `N2`, `N1` hoặc `none`.
- `level_note_vi`: bắt buộc khi `level_hint` khó hơn trần của cấp chặng hoặc là `none`.
- `origin`: `dialogue` hoặc `topic_extension`.
- `evidence`: bắt buộc với `dialogue`, 1–2 mục `{utterance_id, surface}` (ID lượt hội thoại V11) hoặc `{shadowing_item, surface}` (ID mục shadowing, ví dụ `S-001-SH-003`). `surface` phải có trong câu Nhật đó.
- `source_refs`: tùy chọn, mã trong `admin_sources`. Nên có với thuật ngữ thủ tục, y tế, pháp lý.
- `note_vi`: tùy chọn, ghi chú biên tập nội bộ (không hiện cho người học).

### Gói xuất

`--export` tạo một node vocabulary cho mỗi nhóm: `{node_id: "<stage_code>-<group id>", title_vi, terms_ja}` với `terms_ja` là các chuỗi `ja` theo đúng thứ tự. Đúng hợp đồng Harumii Exchange: app chỉ nhận chữ Nhật. `reading`, `vi`, `pos`, `level_hint`, nguồn và bằng chứng ở lại tầng biên tập và preview.

## status.json

```json
{
  "stage_uid": "…",
  "stage_code": "T-044",
  "owner": "tên phiên/người làm",
  "learner_sha256": "hash của v11/learner.json lúc lấy brief",
  "skill_sha256": "hash của SKILL.md",
  "vocabulary_sha256": "hash của vocabulary.json đã lưu",
  "groups": {
    "g01": {"state": "reviewed", "sha256": "hash nội dung nhóm", "reviewed_sha256": "hash lúc duyệt", "note_vi": "…"}
  },
  "open_issues": [{"term_id": "T-044-v014", "issue_vi": "…"}],
  "next_action": "Rà lượt 2 nhóm g03"
}
```

- `state`: `drafted`, `needs_fix` hoặc `reviewed`. Hash nhóm là SHA-256 của JSON nhóm với `sort_keys=True` và `ensure_ascii=False`. Chỉ giữ `reviewed` khi hash hiện tại khớp `reviewed_sha256`; sửa nhóm thì trạng thái quay về `drafted`.
- Lưu `vocabulary.json` trước, rồi `status.json`, đều bằng file tạm và thay thế nguyên tử. Nếu `vocabulary_sha256` lệch file trên đĩa vì dừng giữa hai lần ghi, tin file từ vựng trên đĩa và dựng lại tiến độ theo hash từng nhóm.
- Khi `learner_sha256` đổi (hội thoại V11 được sửa), chạy lại `--check` để bắt bằng chứng không còn đúng, rồi rà lại các nhóm có mục bị ảnh hưởng.
