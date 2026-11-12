# V4.1 — gói sửa nguồn và thống kê sau nghiệm thu

Ngày: 2026-11-12. Phạm vi chỉ là khung và metadata; không viết bài học hoặc chạy pilot. Skill V3 và các thiết kế V1/V2 giữ nguyên để người dùng xem/feedback.

## Kết quả

- Giữ nguyên 194 chặng, UID, mã hiển thị, tiêu đề chặng, track, cụm và thứ tự. Registry không đổi byte nào.
- Giữ 645 hạt giống tình huống, 39 cụm. Phân loại sau sửa: **212 sách / 139 memo / 294 AI**; trước sửa: 211 / 140 / 294.
- Hai mục H-56/T-52 đổi từ memo sang sách nhờ nguồn cụ thể; mục hiệu thuốc T-63 đổi từ sách về memo vì bỏ con trỏ sai. Các ngân hàng thêm vào T-23/T-56/H-33 không đổi nhãn AI của tình huống.
- 23 chặng có `fact_check=true`, tăng 10. Đây là yêu cầu đối chiếu dữ kiện khi viết bài, chưa phải xác nhận dữ kiện và không phải cổng học.

## Nguồn đã đối chiếu

Đã đọc các đoạn **Markdown clean và memo** nêu dưới đây để sửa con trỏ. Không gọi đây là lượt đối chiếu lại PDF hay kiểm nghĩa toàn bộ 645 tình huống.

- **T-23:** ngân hàng có B21:L8, B22:L8, B23:L8. [B21 bài 8](<../../knowledge/日本語でビジネス会話 中級編 本文冊/chapters/08-shain-ryokou.md>) dòng 55–113; [B22 bài 8](<../../knowledge/日本語でビジネス会話 中級編 練習冊/chapters/08-shain-ryokou.md>) dòng 179–224; [B23 bài 8](<../../knowledge/日本語でビジネス会話 中級編 英訳・語い冊/chapters/08-bai-8-chuyen-di-cong-ty.md>) dòng 11–42, 79–112. Nguồn hỗ trợ hỏi thông tin/đăng ký chuyến đi; không chứng minh mọi hạt giống như chọn điểm đến/chia việc đã có nguyên văn.

- **T-56:** thay S16:STAGE1/2 bằng `S16:1/STAGE1/社内|社外/1–3` và `S16:1/STAGE2/社内|社外` (ký hiệu gộp trong ghi chú này; JSONL ghi riêng từng token). **H-33:** dùng `S16:2/STAGE3/1`, `/2`, `/3`. [Memo S16](../WEB_COURSE_TOPICS_MEMO.md), dòng 754–773: giải thích/hỏi lại/so sánh, báo cáo khảo sát; chào dịch vụ thuê máy, giảm chi phí, giá buôn máy pha cà phê.

- **H-56:** bỏ S08:19 (nhờ/được nhờ), dùng `B18:P2-1#scene4`; thu hẹp nhãn tình huống thành trao đổi dàn ý bài nghiên cứu. [B18 phần tình huống](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md>) dòng 47–55.

- **T-52:** bỏ S08:5 (mua vé), dùng B18 P2-1 scene 1/2/3 cho hỏi giáo viên, xin giải thích và hẹn tư vấn. [B18 phần tình huống](<../../knowledge/外国人のための日本語敬語の使い方 基本表現85/chapters/07-PART2-場面別.md>) dòng 8–45. S08:10 chỉ hỗ trợ chức năng giải thích hoàn cảnh/nhờ giúp. Ghi rõ phần thủ tục du học chưa có nguồn trực tiếp; không khẳng định đã phủ phần đó.

- **T-34:** giữ B02:S34 cho xin dùng phòng họp, bổ sung B02:S32 cho xin nghỉ; ghi rõ hai bối cảnh trong tên hạt giống. [B02 phần xin phép](<../../knowledge/「BJTビジネス日本語能力テスト」入門 わかるビジネス日本語（新装版）/chapters/12-許可を求める.md>) dòng 7–33 và 153–170.

- **T-63, sửa thêm trong cùng lượt nguồn:** bỏ B13:U4a khỏi cảnh hiệu thuốc. [B13 Unit 4](<../../knowledge/シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版/chapters/04-unit-4-bac-si-cua-hang.md>) dòng 19–144 là các cảnh khác; cảnh xin thuốc sau sáu tháng nằm ở mục ②, scene 12 (dòng 316–333), vẫn thuộc hạt giống khám/tái khám đầu tiên. Cảnh hiệu thuốc chỉ giữ S01:B1-4 và đổi `kind` về memo; không chuyển nhầm cảnh ở cơ sở khám thành nguồn hiệu thuốc.

## Rà cờ và dẫn chiếu

Bổ sung cờ, kèm `fact_check_notes` theo đúng phạm vi cần kiểm tra: S-07, S-38, T-01, T-48, T-49, T-68, H-03, H-10, H-15, H-32. Các câu nói thông thường không trở thành bài pháp luật/y tế; chỉ dữ kiện cụ thể mới cần đối chiếu.

Sửa dẫn chiếu điện thoại S-29 thành S-30 ở mục 7; bỏ cách diễn đạt điều kiện đạt/prerequisite bắt buộc khỏi phần này theo yêu cầu học tự do. Phần R3/chấm điểm/vượt cổng của V2 được đánh dấu đã bị yêu cầu mới thay thế, không triển khai lại. Không sửa skill V3.

## Một nguồn dữ liệu cho thống kê

- `KAIWA_CHANG_V4_1.jsonl`: nội dung khung.
- `chang_registry.json`: danh tính đã chấp nhận, giữ nguyên.
- `KAIWA_CHANG_V4_1_META.json`: mô tả 39 cụm, tập mục tiêu chỉ mục cho 47 nhóm nguồn, dấu vân tay ID/UID/thứ tự và các quy tắc chống tái xuất hiện lỗi đã sửa.
- `KAIWA_CHANG_V4_1.md`, mục 1–6: dựng lại bằng script; phần 0/7/8 là ghi chú biên tập. Không sửa tay số liệu hoặc hàng chặng trong vùng dựng lại.

Tập mục tiêu được khai báo rõ thay vì lấy số token đang có làm mẫu số, nên có thể báo thiếu thật. Chi tiết scene/STAGE quy về mục cha trước khi đếm; token phần/mục không phải các bài độc lập cùng độ sâu. B08 sửa 58 thành 61 nhãn hiện dùng; B14 được thêm vào bảng với U1–U5. B22/B23 hiện 20/20 **ở mức gắn chỉ mục**, chưa phải 20 bài đã khai thác.

## Chạy kiểm tra và render

Chạy từ gốc repo; mặc định chỉ kiểm tra, không ghi file.

```powershell
py -B -X utf8 kaiwa_skill/tools/roadmap_v4_1.py
py -B -X utf8 kaiwa_skill/tools/roadmap_v4_1.py --write
py -B -X utf8 -m unittest discover -s kaiwa_skill/tests -p test_roadmap_v4_1.py
```

Script kiểm tra ID/UID/registry, thứ tự và số chặng/cụm, phân loại nguồn, hợp nhất con trỏ, cờ đã rà, các hồi quy nguồn cụ thể và sự đồng bộ Markdown. Nó không xác minh ngữ nghĩa mọi token, chất lượng hội thoại hay việc đọc sách thật.

## Dấu vết trước sửa

SHA-256 của JSONL nhận từ V4.1 trước sửa: `4dea3e20cae52e43cb0f8f61967c5ae487a3a3fddc74dda31214340560115c58`. Bản sao phục vụ đối chiếu ở cache cục bộ `kaiwa_skill/.cache/v4_1-before-source-fixes-20261112/`; không thay thế Git/backup.
