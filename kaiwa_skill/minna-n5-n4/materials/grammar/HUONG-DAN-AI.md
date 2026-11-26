# HỢP ĐỒNG DỮ LIỆU — Bài giảng ngữ pháp Harumii (dành cho AI biên soạn)

Tài liệu này là quy ước BẮT BUỘC để file bạn trả về upload ngược được vào Harumii. File sai quy ước sẽ bị từ chối
(trang admin hiện lý do từng file). Hệ thống chỉ ĐỌC file; không có gì được ghi vào bài đang dùng cho tới khi admin
so sánh và bấm "Áp dụng".

## 1. Đơn vị dữ liệu
- MỘT file `.md` = MỘT mẫu ngữ pháp. Mã hoá UTF-8. Nén tất cả thành MỘT file `.zip` để upload.
- Thư mục theo cấp: `N5/`, `N4/`, … (khuyến nghị, không bắt buộc).
- `README.md` và `HUONG-DAN-AI.md` bị bỏ qua khi upload; file có tên bắt đầu bằng `_` cũng bị bỏ qua (dùng cho nháp).

## 2. Tên file
- Mẫu đã có: GIỮ NGUYÊN tên file đã xuất, dạng `<tên mẫu>__<8 ký tự id>.md`.
- Mẫu MỚI: `<tên mẫu>__new.md`, đặt trong thư mục cấp tương ứng, ví dụ `N4/〜ながら__new.md`.

## 3. Đầu file (front matter) — bắt buộc
Dòng đầu tiên của file là `---`, tiếp theo mỗi dòng một khoá `khoá: giá trị`, đóng bằng `---`.
Giá trị là chuỗi trong ngoặc kép kiểu JSON (escape `\"` và `\\`), luôn nằm trên MỘT dòng.

| Khoá | Mẫu đã có | Mẫu MỚI | Ghi chú |
|---|---|---|---|
| `id` | BẮT BUỘC, giữ nguyên tuyệt đối | ghi `new` | Dùng để ghép với mẫu trong hệ thống |
| `jlpt` | giữ nguyên (không đổi cấp được) | BẮT BUỘC: `N5`/`N4`/`N3`/`N2`/`N1` | |
| `name` | được sửa | BẮT BUỘC | Tên mẫu, ví dụ `"〜てから"`, tối đa 256 ký tự |
| `description` | được sửa | nên có | Nghĩa ngắn tiếng Việt, tối đa 2048 ký tự |
| `conjugation` | được sửa | nên có | Cách chia / cấu trúc ngắn, tối đa 1024 ký tự |

- Mẫu đã có: XOÁ hẳn một dòng (trừ `id`) = giữ nguyên giá trị hiện tại trong hệ thống.
- Không thêm khoá khác; khoá lạ bị bỏ qua.

## 4. Thân bài (sau dòng `---` đóng) — giữ đúng cấu trúc của editor
1. `#` (H1): ĐÚNG 1 lần, là tên mẫu ngữ pháp (trùng `name`), không kèm nghĩa trên cùng dòng.
2. Ngay dưới H1: blockquote nghĩa ngắn `> …`, rồi một dòng `---`.
3. `## Cấu trúc ngữ pháp`: blockquote, mỗi dòng cấu trúc in đậm toàn bộ, kết thúc bằng `<br>` (trừ dòng cuối):
   ```
   > **Vて ＋ から**<br>
   > **N ＋ の後で**
   ```
   Không dùng code block cho cấu trúc.
4. `##` (H2): các mục lớn có thật trong bài (Cách dùng / Ý nghĩa, Cách dùng 1/2…, Chú ý, NÂNG CAO, Tổng kết…).
   `###` (H3): mục con. KHÔNG dùng `####` (H4) ở bất kỳ đâu.
5. Ví dụ — mỗi câu đúng 2 dòng liền nhau:
   ```
   ##### 1. ご飯を食べてから、歯を磨きます。
   ###### → Ăn cơm xong rồi đánh răng.
   ```
   - `#####` (H5) CHỈ chứa số thứ tự + nguyên văn câu tiếng Nhật (hệ thống sinh furigana từ các dòng H5).
   - `######` (H6) CHỈ chứa `→` + bản dịch tiếng Việt.
   - Không in đậm/in nghiêng trong dòng H5/H6; chú thích thêm đặt ở dòng văn bản thường (in nghiêng) bên dưới H6.
   - Hội thoại: mỗi lượt thoại là một cặp H5/H6 riêng. Đánh số `1.` `2.` … liên tục trong mỗi mục ví dụ.
6. Được dùng: in đậm, in nghiêng, danh sách `-`, bảng markdown, `---` ngăn phần, ảnh `![](url)` đã có sẵn.
7. KHÔNG dùng: emoji, HTML khác ngoài `<br>`, code block, H4, nhiều H1.

## 5. Quy tắc nội dung
- Sửa/kiểm tra chính xác: giữ nguyên văn các câu tiếng Nhật đúng; nếu sửa câu sai, sửa cả bản dịch tương ứng.
- Không tạo mẫu MỚI trùng tên với mẫu đã có ở cùng cấp — muốn sửa mẫu đó thì sửa file của nó.
- Không tạo 2 file cho cùng một mẫu (cùng `id`, hoặc cùng `jlpt` + `name` với mẫu mới).
- Không đổi `id`, không chép `id` của mẫu này sang file khác.

## 6. Hệ thống kiểm tra khi upload (file vi phạm sẽ bị từ chối, file khác vẫn nhận)
- Có front matter và đóng đúng `---`.
- `id` hợp lệ và tồn tại; hoặc `id: new` kèm `jlpt` hợp lệ và `name` không rỗng.
- Mẫu mới không trùng tên với mẫu đã có cùng cấp, không trùng với file mới khác trong cùng lần upload.
- Thân bài không rỗng và editor đọc được markdown.

## 7. Ví dụ
Sửa mẫu đã có:
```
---
id: 3f2a9c1e-5b7d-4c11-9a0e-2d6f8b1c4e77
jlpt: N5
name: "〜てから"
description: "Sau khi làm A rồi mới làm B"
conjugation: "Vて ＋ から"
---

# 〜てから

> Sau khi làm A rồi mới làm B

---

## Cấu trúc ngữ pháp

> **Vて ＋ から**

## Cách dùng

Diễn tả **trình tự** hai hành động.

##### 1. ご飯を食べてから、歯を磨きます。
###### → Ăn cơm xong rồi đánh răng.
```

Thêm mẫu mới (`N4/〜ながら__new.md`):
```
---
id: new
jlpt: N4
name: "〜ながら"
description: "Vừa làm A vừa làm B"
conjugation: "Vます(bỏ ます) ＋ ながら"
---

# 〜ながら

> Vừa làm A vừa làm B

---

## Cấu trúc ngữ pháp

> **Vます ＋ ながら**

## Cách dùng

Hai hành động diễn ra **đồng thời**, hành động chính ở vế sau.

##### 1. 音楽を聞きながら、勉強します。
###### → Vừa nghe nhạc vừa học bài.
```

## 8. Checklist trước khi nén zip
- [ ] Mọi file đều bắt đầu bằng `---` và có `id` (hoặc `id: new` + `jlpt` + `name`).
- [ ] Không đổi `id`, không đổi tên file của mẫu đã có.
- [ ] Mỗi bài đúng 1 H1, không có H4, ví dụ đúng cặp H5/H6.
- [ ] Không emoji, không code block, không HTML ngoài `<br>`.
- [ ] Không mẫu mới nào trùng mẫu đã có.