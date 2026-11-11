# Preflight — 日本語でビジネス会話 中級編 本文冊

Ngày 2026-11-11. Hồ sơ này ghi bản đồ trước khi clean, không phải bản clean hoặc xác nhận đủ nội dung. `clean_progress scan --repo-root .` trả `ready_for_fork`, `reasons=[]` cho corpus `01-yuukibui-b12c61270c7b`; root đã giao full PDF1–138. Raw đang được đọc để lập kế hoạch, bản clean phải ghim snapshot bằng `init` trước khi biên tập.

## Căn cứ tên và vai trò tập

- Bìa PDF1 in `日本語でビジネス会話` và `中級編`; trang nhan đề PDF2 in thêm `本文冊`. Tên metadata: **日本語でビジネス会話 ― 中級編 ― 本文冊**; thư mục Windows: `kaiwa_skill/knowledge/日本語でビジネス会話 中級編 本文冊/`.
- PDF5–6 ghi bộ sách có ba tập `本文冊`, `練習冊`, `英訳・語い冊`; tập đang clean có 20課. Tập `英訳・語い冊` là tài liệu bổ trợ, không dùng để suy nội dung Nhật hay bổ sung câu thoại cho tập này. PDF10–11 mô tả cách dùng từng tập và quan hệ giữa `談話型`, `本文会話`, `類話`, `語句の使い方` và luyện tập ở tập khác.
- PDF3 là thông tin xuất bản; PDF136 và PDF138 là trang trắng/watermark; PDF137 có `あとがき`. Đánh dấu phạm vi và lý do ở page coverage, không bỏ khỏi scope PDF1–138.

## Chapterplan cố định theo mục lục và ranh giới trang

Trang PDF là số vật lý 1-based. Trang in bài học bắt đầu từ 1 ở PDF14, chênh 13 trang. Mục lục PDF12–13 và đầu mỗi bài trong raw cùng khớp ranh giới dưới đây; mở ảnh từng trang khi clean để xác nhận nội dung chi tiết.

| Chapter dự kiến | Nội dung nguồn | PDF |
|---|---|---:|
| `00-mo-dau.md` | Bìa, nhan đề, lời tựa, đặc điểm ba tập, hướng dẫn sử dụng, mục lục | 1–13 |
| `01-jiko-shoukai.md` | 第一課 自己紹介 | 14–17 |
| `02-wakaranai-nihongo.md` | 第二課 わからない日本語を聞く | 18–23 |
| `03-irai.md` | 第三課 依頼 | 24–29 |
| `04-kotowari.md` | 第四課 断り | 30–35 |
| `05-michi-o-kiku.md` | 第五課 道を聞く | 36–41 |
| `06-aisatsu.md` | 第六課 あいさつ | 42–49 |
| `07-shagai-denwa.md` | 第七課 社外からかかって来た電話 | 50–55 |
| `08-shain-ryokou.md` | 第八課 社員旅行 | 56–61 |
| `09-yoyaku.md` | 第九課 予約 | 62–67 |
| `10-omiyage.md` | 第十課 お土産 | 68–75 |
| `11-renraku.md` | 第十一課 連絡 | 76–81 |
| `12-owabi.md` | 第十二課 おわび | 82–87 |
| `13-hyougen-yarikata.md` | 第十三課 表現、やり方を聞く | 88–93 |
| `14-shotaimen.md` | 第十四課 初対面の人と | 94–101 |
| `15-toiawase.md` | 第十五課 問い合わせ | 102–105 |
| `16-houmon.md` | 第十六課 訪問 | 106–113 |
| `17-keigo.md` | 第十七課 敬語 | 114–119 |
| `18-apointmento.md` | 第十八課 アポイントメント | 120–125 |
| `19-chuui-o-ukeru.md` | 第十九課 注意を受ける | 126–129 |
| `20-mensetsu-shiken.md` | 第二十課 面接試験 | 130–135 |
| `21-atogaki.md` | Trang trắng, あとがき, trang cuối trắng | 136–138 |

## Mạch cần giữ khi clean

- Mỗi 課 đi theo các phần thật trên trang: mục đích, khung `談話型` và blanks, `本文会話`, `類話` nếu có, rồi `語句の使い方` với mẫu và ví dụ. Bài1 PDF14–16 đã xác nhận thứ tự này; lời thoại tự giới thiệu PDF15 và các blanks trong khung PDF14 cùng mẫu PDF16 có chức năng khác nhau, không gộp hoặc điền lời giải.
- Các trường hợp riêng trong TOC: bài2 có tám nhánh 類話; bài7 nhiều tình huống điện thoại; bài9 có `応用会話` đặt sau 類話; bài14 có các nhánh truyền lời; bài15/17/19/20 chỉ liệt kê 本文会話 ở TOC nhưng vẫn phải đọc từng trang để giữ phần khác thực in.
- Số lề dẫn dòng, tham chiếu trang/dòng (`p.2 l.6`), chữ đậm trong mẫu, vai nói, tình huống và điều kiện của câu mẫu cần giữ bằng text khi phục vụ bài học. Không tự suy đáp án/audio. PDF6 nhắc luyện bằng tape trong tập 練習冊; chưa thấy mã track trên các ảnh đã mở, sẽ kiểm từng bài.
- Bản dịch Anh ở PDF7–9 là phần hướng dẫn tương ứng với lời tựa/đặc điểm Nhật. Khi clean phải kiểm ý nào chỉ có ở Anh để chuyển sang Việt; phần lặp đồng nghĩa có thể gộp và ghi lý do. Không áp nội dung từ companion `英訳・語い冊` vào hội thoại nguồn.

## Ảnh đã thực sự mở tại preflight

PDF1, 2, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16 từ cache render của corpus. PDF3, 7–9, 17–138 chưa được mở trong lượt preflight này; cần mở khi xử lý từng trang, kể cả trang trắng và hậu từ. Các ranh giới sau bài1 hiện dựa trên TOC ảnh PDF12–13 và heading raw, chưa thay cho rà ảnh toàn bộ.
