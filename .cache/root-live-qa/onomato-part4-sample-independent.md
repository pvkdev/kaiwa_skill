# Independent Part 4 sample QA (heads 1–15)

Source SHA-256: `458b548674d123f0e35c8df67395c3e569eab80ffa6e9c4a7848a8489547d439`
Output SHA-256 at review: `e9aa62273f71ec997006c5fe0f7ee55dbe2566845e1b29a0cfddfe6405fff487`

Opened full images PDF165–179 and compared the 15 head sections to the current chapter. Checked Japanese, Vietnamese meaning, conditions/negation, both activities per head, Typical Forms, Point, Small Steps, visible CD markers, and image facts represented in the output. Four source-specific findings follow.

## 1. PDF169 / Part 4 head 5 — image_context_inaccurate

- Source: Hình ドキドキ cho thấy một người đeo tai nghe/đứng cạnh bục có micro trước khán giả; điện thoại chỉ xuất hiện ở hội thoại 1 bên dưới.
- Output: Tranh vẽ người hồi hộp chờ một cuộc gọi.
- Suggested correction: Sửa mô tả hình thành bối cảnh đứng trước bục/micro và khán giả, hoặc bỏ mô tả tranh; không gắn cuộc gọi của ví dụ 1 vào hình.

## 2. PDF174 / Part 4 head 10 — image_context_inaccurate

- Source: Hình グッと cho thấy người cầm tờ giấy trước thiết bị/bảng có các ô ghi No.1–No.4; không thấy bảng thông báo.
- Output: Tranh vẽ người cầm tờ giấy trước một bảng thông báo, cảm động đến nghẹn ngào.
- Suggested correction: Mô tả trung tính người cầm giấy trước các ô No.1–No.4, hoặc bỏ chi tiết tranh; đừng xác quyết đây là bảng thông báo.

## 3. PDF176 / Part 4 head 12 — printed_japanese_omitted

- Source: Point in hai cụm trích nguyên dạng: 「心に響く」「胸が熱くなる」.
- Output: **Point:** Cảm giác vang trong lòng hoặc ngực nóng lên.
- Suggested correction: Giữ hai cụm Nhật in sẵn cạnh nghĩa Việt: 「心に響く」— chạm/vang vào lòng; 「胸が熱くなる」— ngực/lòng nóng lên vì xúc động.

## 4. PDF177 / Part 4 head 13 — translation_meaning_shift

- Source: Lượt B: 「うん。自分でもよくやったと、しみじみ思うよ。」; cột Anh nêu 'I did a good job'.
- Output: Ừ. Chính tôi cũng thấy thấm thía rằng mình đã cố gắng rất nhiều.
- Suggested correction: Giữ đánh giá kết quả よくやった: 'Ừ. Chính tôi cũng ngẫm lại và thấy mình đã làm rất tốt.' Không đổi câu Nhật.

## Limit

This is a bounded sample review of 15 full pages. Heads 16–45 and the rest of the book were not independently reviewed here. The writer retains ownership of any corrections; this QA only wrote cache artifacts.

## Bounded recheck after writer edits

Chapter SHA-256 at recheck: `02d3ad244131e56c5ae10e95404b9eba5a63286da9264789890d5141213cfe03`

Read only the four passages at PDF169/174/176/177 against the previously opened source images. All four original findings are resolved:

- PDF169 / head 5: illustration description now says podium and audience.
- PDF174 / head 10: description now says paper and numbered No.1–No.4 cells.
- PDF176 / head 12: both printed Japanese Point phrases are present with Vietnamese meanings.
- PDF177 / head 13: よくやった now means having done well.

Pending original findings: 0. This recheck does not expand the original 15-head QA scope.
