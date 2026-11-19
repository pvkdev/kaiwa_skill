# Bàn giao chat Trung — shadowing V13

Ngày làm việc: 2026-11-19 (Asia/Tokyo). Phần Trung đã hoàn tất soạn/đọc duyệt/xuất.
Đang chờ hai chat còn lại hoàn tất để chốt tổng hợp 293 topic.

Đúng ba worker `gpt-6.2-sol`, reasoning `high`, không thêm worker:

- Worker 1: T-001–T-033.
- Worker 2: T-034–T-066.
- Worker 3: T-067–T-098.

Thứ tự theo `stages` topic của V11. T-099–T-115 thuộc chat Sơ; T-116–T-148 thuộc
chat Thượng. Worker chạy `pilot.py brief <code>` trước từng chặng, đọc nhóm V12 và
toàn bộ hội thoại V11, ghi nguyên tử `v13/stages/<code>/draft.json` với pins thực.
Chỉ điều phối đọc duyệt rồi check/publish/checkpoint bằng `--target stages`.

## Đã nghiệm thu

98/98 chặng, 2.140 câu. Mới: 95; dùng lại pilot: 3 (T-002, T-008, T-044).

- T-001–T-033: 744 câu (31 mới, 2 pilot).
- T-034–T-066: 723 câu (32 mới, 1 pilot).
- T-067–T-098: 673 câu (32 mới).

Mỗi chặng 19–24 câu, theo nhu cầu thực. Không còn mã chờ hoặc mã vướng trong phạm vi
Trung. Ba worker đã quét chỉ đọc toàn bộ dải sau nghiệm thu; root kiểm lại toàn bộ 98.
Kết quả máy đọc tại [trung-checkpoints.json](trung-checkpoints.json).

Điều phối đã đọc các cặp Nhật–Việt, rà độc lập, vai và nhịp luyện. Các sửa nổi bật:
T-002 giữ sắc thái ngỏ ý mang đồ/giúp dọn; T-003 giữ rõ cách tự sửa chị/em gái;
T-005 gọi rõ đổi lượt dùng chỗ phơi khi câu đứng riêng; T-037 phân biệt xin phép quyết
định sau với hỏi đủ điều kiện; T-068 sửa lời tự nhận việc; T-069 giữ chủ thể chủ trì
tự chuyển nghị trình. Ghi chú cụ thể nằm trong checkpoint từng chặng.

## Danh sách chờ và phần tiếp tục

Quét đầu vào ban đầu: T-031–T-036 thiếu `v12/stages/<code>/vocabulary.json`.
Quét sau lô 1: T-031–T-032 đã sẵn sàng; T-033 có bản thảo V12 nhưng nhóm g01–g05
chưa có review hiện hành; T-034–T-036 vẫn thiếu file. Chưa được phép soạn mã chưa qua gate.
Quét sau lô 2: T-033 và T-034 đã sẵn sàng, worker 2 quay lại T-034; T-035–T-036
vẫn thiếu vocabulary.json. T-031–T-032 đã sẵn từ lô trước.
Quét sau lô 3: T-035–T-036 đã sẵn sàng, worker 2 quay lại soạn. Hiện không còn mã
chờ V12 trong phạm vi Trung ở các lượt quét tương ứng; vẫn kiểm lại brief và pins từng chặng.

Trong khi xuất lô 5, T-024 bị chặn vì V12 đổi hash. Worker đã lấy brief mới, đối chiếu
đầy đủ 5 nhóm từ và V11: chỉ pins thay, mặt chữ/nghĩa/thứ tự không đổi; rà lại 23 câu,
terms rồi xuất checkpoint mới. T-093 cũng đã lấy brief mới sau khi V12 sửa Hán Việt
`欠席する` thành `KHUYẾT TỊCH`; từ này không dùng trong câu V13. Không chỉ thay pins
để bỏ qua gate. Hai chặng hiện đã nghiệm thu.

Lượt precheck phát hiện T-013 đã xuất nhưng V12 đổi hash sau đó; đã lấy brief mới,
đối chiếu nhóm từ/V11 không đổi, đọc lại 22 câu và terms, làm rõ Việt 012 rồi xuất lại.
T-054–T-056 cũng đã đối chiếu brief mới và metadata sửa Hán Việt/nguồn cho 欠;
các câu dùng 欠席/欠席連絡 vẫn đúng nghĩa, giữ câu và ghim pins mới sau review.
T-029 lấy lại brief sau đổi hash, các trường nội dung không đổi, đã đọc lại 23 câu
và làm rõ số bữa cho hai người trước khi xuất. Các checkpoint này hiện đã kiểm lại đạt.

Đối chiếu văn bản cuối tìm hai câu trùng nguyên văn V11: T-012-002 và T-096-004.
Đã lấy brief lại và viết mới: T-012 cho người nghe quyền thu xếp được mới giúp,
T-096 tổng hợp ý kiến với mẫu số/nhóm khách rõ, giữ nguyên số liệu nguồn. Root đọc duyệt,
xuất lại và cập nhật preview. Sau sửa: 0 câu Nhật trùng nguyên văn giữa 98 bài và 0 câu
trùng nguyên văn V11/shadowing cũ cùng chặng (chuẩn hóa NFKC, khoảng trắng, dấu kết câu).
Quét lại sau mỗi lô và trước khi kết thúc. Các mã còn lại đang
soạn theo thứ tự dải; bản thảo chưa có checkpoint hợp lệ chưa được tính đã hoàn thành.

## Công cụ và tổng hợp liên chat

Chat Trung đã thêm `--target stages` cho check/publish, giữ pilot mặc định, và lệnh
`checkpoint` chỉ đọc. Có `audit.py` đối chiếu đủ 293 mã topic, chỉ đếm checkpoint
sản xuất hợp lệ; xem [TOOLS.md](TOOLS.md). Tám kiểm thử với bản sao/thư mục tạm đạt,
bao gồm kiểm đủ phân vùng 98/98/97 và audit không ghi/không tính checkpoint lỗi.
Commit công cụ riêng: `97ddd578`.
[Preview Trung riêng](trung-preview.html) đã đối chiếu đủ 98 chặng, 2.140 cặp Nhật–Việt
và vai/giọng với gói xuất theo đúng thứ tự, bao gồm hai câu vừa sửa cuối.

Chat Sơ đã báo hoàn tất 98/98 chặng, 2.134 câu. Chat Thượng đã hoàn tất 64 chặng H và
đang làm phần Trung của mình. Chưa kết luận toàn bộ ba chat hoàn thành. Khi đủ đầu ra,
chạy lại audit toàn bộ 293 mã và báo số chặng đã duyệt, tổng số câu, mã còn vướng.
Phần tổng hợp liên chat đang chạy; không tính draft chưa duyệt vào tổng.
Giữ nguyên SKILL.md, chín snapshot pilot, V11/V12 và `docs/index.html`; đầu ra V13 riêng.
Không push/deploy trong lượt soạn.
