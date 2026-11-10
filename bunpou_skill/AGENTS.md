# AGENTS.md – Quy tắc bắt buộc cho mọi AI làm việc trong dự án này

> File này là điểm vào chung cho Codex, Cursor, Gemini CLI, Claude Code và mọi AI agent khác.
> Phiên bản quy tắc: xem file `VERSION`.

## 1. Dự án này làm gì

Biến **một bài giảng ngữ pháp tiếng Nhật thô** + **cấp độ mục tiêu (N5–N1)** thành **bộ file đầu vào cho NotebookLM**
để NotebookLM dựng video bài giảng tiếng Việt: thân mật, hài hước, nhịp nhanh, **ví dụ phủ hết mọi cách dùng và mọi dạng cấu trúc**, nghe một lần là nhớ.
Thời lượng không giới hạn. Lộ trình video: intro → tình huống → **giới thiệu & mô tả mẫu** → **mỗi cách dùng một chương** Ý nghĩa (giảng kỹ) → Cách chia → toàn bộ ví dụ → bẫy → tổng kết.
**Sản xuất hàng loạt (kit 7):** bài giảng thô nằm ở `source/<cấp>/<cấp>_<mẫu>_vNN.md` (quản lý phiên bản + trạng thái trong
`source/<cấp>/_quan_ly.json`), output nằm ở `work/<cấp>/<ID>/` với `<ID>` = tên nguồn + `_rNN`. Mọi thao tác trên source/work
đi qua `tools/nguon.py` (nhập nguồn, hàng đợi, bắt đầu bài). Bài làm trước kit 7 nằm trong `old/` (không dùng nữa).
Mỗi bài AI chỉ viết **2 file**: `work/<cấp>/<ID>/KichBan_<ID>.md` (file duy nhất tải lên NotebookLM)
và `work/<cấp>/<ID>/_phu/GhiChu_<ID>.md`. Bài gốc do `nguon.py bat-dau` chép sẵn; các file phụ còn lại do `tools/validate.py` tự sinh.
Dùng chung cho mọi bài, nằm ở gốc dự án: `guide.md` (quy tắc dựng video, người dùng tải lên NotebookLM 1 lần) và
`HuongDan.html` (trang làm video: danh sách bài theo cấp độ, tìm kiếm, nút copy). Không chép 2 file này vào thư mục bài.

AI **không** làm video. AI chỉ nhập nguồn vào `source/` (qua `nguon.py them`) và sản xuất bộ file trong `work/<cấp>/<ID>/`.

**Chế độ tự quyết:** người dùng trao toàn quyền để sản xuất nhanh. AI không hỏi lại, không yêu cầu duyệt;
tự quyết theo phương án an toàn nhất, tự thẩm định độ chính xác, ghi quyết định vào Ghi chú biên tập.
Chỉ hỏi lại khi người dùng muốn nhập nguồn mà tin nhắn không có bài giảng.

## 2. Khi nào kích hoạt quy trình

- Người dùng dán bài giảng → **Chế độ A – Nhập nguồn** (chỉ lưu vào `source/`, chưa viết kịch bản – trừ khi người dùng nói "làm luôn").
- "chạy hàng đợi", "chạy hàng loạt", "chạy N2", `/bunpou-video chạy` → **Chế độ B – Hàng đợi**, rồi **Chế độ C** cho từng mẫu.
- Viết kịch bản cho một mẫu (Chế độ C) → **bắt buộc** làm đúng `core/WORKFLOW.md` từ Bước 1 đến Bước 7. Không rút gọn, không đổi thứ tự.

## 3. Thứ tự đọc file (bắt buộc trước khi viết bất cứ thứ gì)

1. `core/WORKFLOW.md` – quy trình từng bước
2. `core/rules/01_noi-dung.md` – độ chính xác nội dung
3. `core/rules/02_giong-van.md` – giọng giảng
4. `core/rules/03_vi-du.md` – định dạng ví dụ
5. `core/rules/04_tieng-nhat.md` – quy tắc câu tiếng Nhật
6. `core/rules/05_cap-do.md` – hồ sơ cấp độ N5–N1
7. `core/rules/06_nhan-vat.md` – chọn nhân vật mới cho mỗi bài (`nguon.py bat-dau` in sẵn gợi ý)
8. `core/templates/` – mọi template đầu ra
9. `core/examples/N3_tokoro-ni-he-wo-de/` – **ví dụ chuẩn (gold standard)**. Đầu ra phải ngang chất lượng và đúng định dạng như ví dụ này.

## 4. Mười điều KHÔNG BAO GIỜ được làm

1. Không thay, không viết lại ví dụ bài gốc. Chọn **4–6 ví dụ cho MỖI cách dùng** từ bài gốc, **mọi thẻ Cấu trúc có ít nhất 1 ví dụ**; chỉ viết `[MỚI]` khi bài gốc không đủ.
2. Không bịa ngữ pháp, không thêm cách dùng mà bài gốc không có (trừ mục "Bẫy dễ nhầm" theo `01_noi-dung.md`).
3. Không viết câu tiếng Nhật mà bản thân không chắc là tự nhiên và đúng ngữ pháp.
4. Không đổi tên tiêu đề, nhãn, thứ tự mục so với template.
5. Không để sót placeholder `{{...}}` trong file đầu ra.
6. Không đưa ghi chú biên tập vào file Kịch bản (ghi chú nằm ở `_phu/GhiChu_<ID>.md`). Không đưa câu đố, quiz, hỏi đáp vào Kịch bản.
7. Không dùng romaji trong file Kịch bản. Mọi câu Nhật trên màn hình đi theo 2 dòng: câu Nhật sạch → câu Việt; không dòng cách đọc, không furigana; mẫu cần tô màu ghi ở dòng `**Tô màu:**` (câu Nhật) và `**Tô màu Việt:**` (cụm nghĩa tương ứng trong câu Việt); không ký hiệu 《 》 【 】 hay ngoặc cách đọc; không gạch đầu dòng trước câu Nhật/Việt.
8. Không sửa file trong `core/`, `guide.md`, `HuongDan.html` khi đang làm một bài (chỉ sửa khi người dùng yêu cầu cập nhật quy tắc).
9. Không tự tạo/đổi tên/ghi đè thư mục trong `work/` (dùng `nguon.py bat-dau` – chạy lại tạo `_r02`, `_r03`…); không sửa/xóa file trong `source/`.
10. Không tuyên bố "xong" khi `tools/validate.py` còn báo LỖI.

**Tính di động:** không bao giờ ghi đường dẫn tuyệt đối (`D:\…`, `/Users/…`, `/home/…`, `file:///…`) vào bất kỳ file nào của dự án.
Trong file chỉ dùng đường dẫn tương đối từ thư mục gốc dự án (vd `work/N2/<ID>/KichBan_<ID>.md`). Đường dẫn tuyệt đối chỉ được
xuất hiện trong báo cáo chat (khối "Mở nhanh" do validate.py tính lúc chạy). validate.py báo LỖI nếu vi phạm.

## 5. Kiểm tra trước khi bàn giao

- Chạy: `python tools/validate.py work/<cấp>/<ID>` (Windows có thể dùng `py`). Lệnh này kiểm tra, tự sinh file phụ trong `_phu/`
  ghi trạng thái vào `source/<cấp>/_quan_ly.json` và cập nhật dữ liệu cho `HuongDan.html`. Không tự viết meta, TuyChinh, data.js, HTML hay json.
- Có LỖI → sửa → chạy lại (tối đa 3 vòng). Còn lỗi sau 3 vòng → báo rõ cho người dùng.
- Không chạy được Python → tự kiểm theo "Checklist tự kiểm" trong `core/WORKFLOW.md` và nói rõ là đã kiểm thủ công.
- Báo cáo cuối luôn kèm khối link **"📂 Mở nhanh"** do `validate.py` in ra (xem Bước 7 của `core/WORKFLOW.md`),
  viết bằng markdown thường, không đặt trong khối code, để người dùng bấm vào mở file ngay.
- Không tự mở trình duyệt/thư mục: người dùng giữ sẵn trang `HuongDan.html`, chỉ cần F5 là thấy bài mới.

## 6. Ngôn ngữ

- Trao đổi với người dùng: tiếng Việt.
- File đầu ra: tiếng Việt + câu tiếng Nhật. Mọi file lưu UTF-8.

## 7. Khi người dùng muốn cập nhật quy tắc

Làm theo `docs/CAP_NHAT_QUY_TAC.md`: sửa đúng file rule liên quan, cập nhật ví dụ chuẩn nếu cần, tăng `VERSION`,
ghi `CHANGELOG.md`, chạy lại `python tools/validate.py core/examples/N3_tokoro-ni-he-wo-de` và `python tools/build_bundle.py`.
