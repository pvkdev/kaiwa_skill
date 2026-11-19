# Bàn giao V12 cho ba chat song song

Đã dừng ba worker của lần chạy trước. Có 27/293 chặng đã xuất với 1.540 mục. Kết quả gồm 12/81 Sơ, 7/148 Trung và 8/64 Thượng. Checkpoint đã xuất khớp với JSON dùng trong preview. [Mở preview hiện tại](ROADMAP.html).

Mở ba chat **Local** trỏ đến cùng một repo `D:/CODE/git/kaiwa_skill`. Mỗi chat nhận ba worker. Các dải mã bên dưới phủ đúng **266 chặng còn lại**, mỗi mã thuộc một worker. Chat Sơ phụ trách 89 chặng, chat Trung 89 chặng, chat Thượng 88 chặng. Các dải đều tính cả hai đầu.

## Prompt chat Sơ

```text
Mở repo Local dùng chung D:/CODE/git/kaiwa_skill. Việc của chat này là điều phối 3 sub gpt-6.2-sol/high. Bạn giữ chat điều phối và giao mỗi sub đúng một hàng bên dưới. Mỗi sub làm tuần tự theo mảng stages trong kaiwa_skill/planning/v11/learner.json. Có mã được chèn giữa lộ trình, như S-081 và T-146. Dải mã phân quyền ai được ghi, còn thứ tự thực hiện lấy từ learner.json.

Đọc AGENTS.md, .agents/skills/kaiwa-topic-vocabulary/SKILL.md và references/draft.md của skill. Chọn từ cho toàn bộ chủ đề theo V12.0, tham khảo hội thoại và shadowing, thêm vốn từ giúp người học nói về hoàn cảnh của họ. Mốc 40–100 mục tùy chặng. Dữ liệu có ja, reading, han_viet, vi và metadata nguồn. Từ không chứa kanji để han_viet rỗng. Kiểm âm Hán Việt và nghĩa Việt theo ngữ cảnh. Với thuật ngữ thủ tục, pháp lý, y tế, dùng nguồn phù hợp theo skill.

Phạm vi ghi của mỗi worker chỉ gồm vocabulary.json và status.json trong kaiwa_skill/planning/v12/stages/<mã được giao>/. Lưu nguyên tử từng file và chạy --check-checkpoint sau mỗi chặng. Nếu checkpoint hợp lệ thì bỏ qua. Nếu có bản dở, giữ các nhóm đã duyệt và còn khớp hash rồi làm tiếp. Sau mỗi 5 chặng, báo số mục, lỗi còn mở, mã cuối, rồi tiếp tục. Chat điều phối nghiệm thu từng lô, gồm chất lượng từ, tiếng Việt, Hán Việt, nguồn và việc phủ các nhóm chủ đề. Worker dừng ở ranh giới mã được giao. Nếu worker hết lượt thì tiếp quản đúng vùng mã của worker đó từ checkpoint.

Dùng thư mục tạm riêng cho từng chat và worker. Cả ba chat dùng cùng repo Local. Giữ quyền ghi theo bảng phân công. Giữ nguyên các file nguồn, skill, script dùng chung và HTML trong lúc các chat đang soạn. Chỉ chat Trung chạy bộ dựng preview và Git sau khi đủ 293 checkpoint đã nghiệm thu. Mọi lỗi cần sửa ngoài vùng giao báo chat điều phối, tránh sửa cùng file ở hai chat. Không push.

Chat này sở hữu 69 chặng Sơ và 20 chặng Trung. Chạy hết Sơ trước, sau đó dùng lại ba sub theo cùng số thứ tự để làm phần Trung.

- Sub 1. S-012–S-035, bỏ S-024 đã nghiệm thu. Sau khi cả chat xong Sơ, làm T-128–T-134.
- Sub 2. S-036–S-057 và S-081. S-081 nằm ngay sau S-056. Sau khi cả chat xong Sơ, làm T-135–T-141.
- Sub 3. S-058–S-080. Sau khi cả chat xong Sơ, làm T-147, T-148 rồi T-142–T-145 theo thứ tự trong learner.json.

Khi đủ phần Sơ và phần Trung được giao, báo kết quả và các checkpoint đã nghiệm thu để chat Trung tổng hợp.
```

## Prompt chat Trung

```text
Mở repo Local dùng chung D:/CODE/git/kaiwa_skill. Việc của chat này là điều phối 3 sub gpt-6.2-sol/high. Bạn giữ chat điều phối và giao mỗi sub đúng một hàng bên dưới. Mỗi sub làm tuần tự theo mảng stages trong kaiwa_skill/planning/v11/learner.json. Có mã được chèn giữa lộ trình, như S-081 và T-146. Dải mã phân quyền ai được ghi, còn thứ tự thực hiện lấy từ learner.json.

Đọc AGENTS.md, .agents/skills/kaiwa-topic-vocabulary/SKILL.md và references/draft.md của skill. Chọn từ cho toàn bộ chủ đề theo V12.0, tham khảo hội thoại và shadowing, thêm vốn từ giúp người học nói về hoàn cảnh của họ. Mốc 40–100 mục tùy chặng. Dữ liệu có ja, reading, han_viet, vi và metadata nguồn. Từ không chứa kanji để han_viet rỗng. Kiểm âm Hán Việt và nghĩa Việt theo ngữ cảnh. Với thuật ngữ thủ tục, pháp lý, y tế, dùng nguồn phù hợp theo skill.

Phạm vi ghi của mỗi worker chỉ gồm vocabulary.json và status.json trong kaiwa_skill/planning/v12/stages/<mã được giao>/. Lưu nguyên tử từng file và chạy --check-checkpoint sau mỗi chặng. Nếu checkpoint hợp lệ thì bỏ qua. Nếu có bản dở, giữ các nhóm đã duyệt và còn khớp hash rồi làm tiếp. Sau mỗi 5 chặng, báo số mục, lỗi còn mở, mã cuối, rồi tiếp tục. Chat điều phối nghiệm thu từng lô, gồm chất lượng từ, tiếng Việt, Hán Việt, nguồn và việc phủ các nhóm chủ đề. Worker dừng ở ranh giới mã được giao. Nếu worker hết lượt thì tiếp quản đúng vùng mã của worker đó từ checkpoint.

Dùng thư mục tạm riêng cho từng chat và worker. Cả ba chat dùng cùng repo Local. Giữ quyền ghi theo bảng phân công. Giữ nguyên các file nguồn, skill, script dùng chung và HTML trong lúc các chat đang soạn. Chỉ chat Trung chạy bộ dựng preview và Git sau khi đủ 293 checkpoint đã nghiệm thu. Mọi lỗi cần sửa ngoài vùng giao báo chat điều phối, tránh sửa cùng file ở hai chat. Không push.

Chat này sở hữu 89 chặng Trung dưới đây và là đầu mối xuất bản cuối.

- Sub 1. T-006–T-036, bỏ T-008 đã nghiệm thu.
- Sub 2. T-037–T-067, bỏ T-044 đã nghiệm thu.
- Sub 3. T-068–T-096.

Các chặng T-097 trở đi do hai chat còn lại phụ trách theo bảng bàn giao. Khi xong phần mình, theo dõi checkpoint để xác nhận hai chat đã nghiệm thu xong. Khi 293/293 chặng đạt, chạy py -X utf8 tools/roadmap_v12_pilot.py --require-complete từ thư mục repo. Kiểm đủ dữ liệu Exchange, 293 bài từ vựng trong preview và bốn cột trên PC/mobile. Sau đó commit chính xác file V12 và docs/index.html. Báo tổng số chặng, mục từ, nhóm, lỗi còn mở và commit. Nếu một vùng chậm, giữ ranh giới giao việc cho đến khi chat sở hữu vùng đó xác nhận bàn giao.
```

## Prompt chat Thượng

```text
Mở repo Local dùng chung D:/CODE/git/kaiwa_skill. Việc của chat này là điều phối 3 sub gpt-6.2-sol/high. Bạn giữ chat điều phối và giao mỗi sub đúng một hàng bên dưới. Mỗi sub làm tuần tự theo mảng stages trong kaiwa_skill/planning/v11/learner.json. Có mã được chèn giữa lộ trình, như S-081 và T-146. Dải mã phân quyền ai được ghi, còn thứ tự thực hiện lấy từ learner.json.

Đọc AGENTS.md, .agents/skills/kaiwa-topic-vocabulary/SKILL.md và references/draft.md của skill. Chọn từ cho toàn bộ chủ đề theo V12.0, tham khảo hội thoại và shadowing, thêm vốn từ giúp người học nói về hoàn cảnh của họ. Mốc 40–100 mục tùy chặng. Dữ liệu có ja, reading, han_viet, vi và metadata nguồn. Từ không chứa kanji để han_viet rỗng. Kiểm âm Hán Việt và nghĩa Việt theo ngữ cảnh. Với thuật ngữ thủ tục, pháp lý, y tế, dùng nguồn phù hợp theo skill.

Phạm vi ghi của mỗi worker chỉ gồm vocabulary.json và status.json trong kaiwa_skill/planning/v12/stages/<mã được giao>/. Lưu nguyên tử từng file và chạy --check-checkpoint sau mỗi chặng. Nếu checkpoint hợp lệ thì bỏ qua. Nếu có bản dở, giữ các nhóm đã duyệt và còn khớp hash rồi làm tiếp. Sau mỗi 5 chặng, báo số mục, lỗi còn mở, mã cuối, rồi tiếp tục. Chat điều phối nghiệm thu từng lô, gồm chất lượng từ, tiếng Việt, Hán Việt, nguồn và việc phủ các nhóm chủ đề. Worker dừng ở ranh giới mã được giao. Nếu worker hết lượt thì tiếp quản đúng vùng mã của worker đó từ checkpoint.

Dùng thư mục tạm riêng cho từng chat và worker. Cả ba chat dùng cùng repo Local. Giữ quyền ghi theo bảng phân công. Giữ nguyên các file nguồn, skill, script dùng chung và HTML trong lúc các chat đang soạn. Chỉ chat Trung chạy bộ dựng preview và Git sau khi đủ 293 checkpoint đã nghiệm thu. Mọi lỗi cần sửa ngoài vùng giao báo chat điều phối, tránh sửa cùng file ở hai chat. Không push.

Chat này sở hữu 56 chặng Thượng và 32 chặng Trung. Chạy hết Thượng trước, sau đó dùng lại ba sub theo cùng số thứ tự để làm phần Trung.

- Sub 1. H-008–H-027, bỏ H-020 đã nghiệm thu. Sau khi cả chat xong Thượng, làm T-097–T-107.
- Sub 2. H-028–H-046. Sau khi cả chat xong Thượng, làm T-108–T-117 và T-146. T-146 nằm ngay sau T-110.
- Sub 3. H-047–H-064. Sau khi cả chat xong Thượng, làm T-118–T-127.

Khi đủ phần Thượng và phần Trung được giao, báo kết quả và các checkpoint đã nghiệm thu để chat Trung tổng hợp.
```
