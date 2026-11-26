# Assessment bài 39 — bản bàn giao cố định

Nguồn: `sources/lesson-39/assessment/857228073a661fac24d50b94e2e7a6364dd6a1a4c16b6b59fdf4cba5541c99a9.json` (snapshot DOM của Mondai 1–6). Bản biên soạn: `authored/lesson-39/assessment.json`. Đầu ra chuyển đổi: `exports/curriculum-exercises/assessment/lesson-39/`.

| Mondai | Section ID | Source IDs | Biên soạn | Hoãn |
| --- | --- | --- | ---: | ---: |
| 1 | `goi-1` | `mt-q-1`–`mt-q-5` | 5 | 0 |
| 2 | `goi-2` | `mt-q-6`–`mt-q-10` | 5 | 0 |
| 3 | `kanji-1` | `mt-q-11`–`mt-q-15` | 5 | 0 |
| 4 | `kanji-2` | `mt-q-16`–`mt-q-20` | 5 | 0 |
| 5 | `bunpo-1` | `mt-q-21`–`mt-q-25` | 5 | 0 |
| 6 | `bunpo-2` | `mt-q-26`–`mt-q-29` | 4 | 0 |
| **Tổng** | **6 sections** | **`mt-q-1`–`mt-q-29`** | **29** | **0** |

Tất cả 29 câu có nội dung và bốn lựa chọn chữ trong DOM. Không câu nào phụ thuộc ảnh hoặc bản ghi âm; `data-tts-base` chỉ là cấu hình đọc TTS chung. Vì vậy không cần biến thể text độc lập. Mỗi câu giữ source ID, có một đáp án theo `data-option` dạng chuỗi và lời giải tiếng Việt riêng. Với Mondai 3–4, từ được gạch dưới trong DOM được nêu rõ bằng `【...】` trong prompt.

**Biên tập để tránh đa nghiệm:** `mt-q-28` có nhiễu `日本語が わからなくて`, cũng có thể dùng để nêu lý do trước lời nhờ. Trong bản biên soạn đổi duy nhất phương án ID `3` thành `日本語が わからないくて` (sai dạng biến đổi), để ID `2` `日本語が わからないので` là đáp án duy nhất. Metadata `adaptation_note` ghi sai khác. Các lựa chọn ở 28 câu khác giữ nguyên nguồn. `mt-q-15` có câu nguồn thiếu tân ngữ rõ ràng ở vế `友達に あげました`, nhưng yêu cầu chỉ đọc `邪魔`; vẫn có đáp án duy nhất và giữ nguyên câu.

**Kiểm chuyển đổi:** `py -X utf8 scripts/curriculum_templates.py authored/lesson-39/assessment.json --out exports/curriculum-exercises/assessment/lesson-39` thành công: 6 section, 29 câu, 6 file `.storage.json`, 1 `index.json`. Đối chiếu 29 source ID đúng thứ tự, không trùng, không thiếu; chỉ số đáp án trong 6 file storage khớp `correct_choice_id` và thứ tự lựa chọn trong authored. Không có source ID hoãn.

**Checksum SHA-256 để đóng băng đầu vào và kết quả:**

- Snapshot nguồn: `8b68eb636a78a954f789bde561f045e8711ae361256b3e3e1d016c8251beca74`
- Authored assessment: `9149a1893c491212b7475f0ab1dc7d8921d4be45aa6fac5d5b46d55325ab1a76`
- Export index: `d50693fafeea888ae9a7b5b87fe7b4eeb52629b07cb650047d344a2b4e589852`

Chỉ các file assessment và báo cáo này được viết trong lượt QA; không sửa skill hoặc preview, không stage/push.
