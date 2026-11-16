# H-004 — nhật ký nghiên cứu và tự rà V11 pilot

Ngày đọc: 2026-11-16. Phạm vi: 15 tình huống của topic H-004; 92 lượt thoại. Các lời Nhật–Việt trong `dialogues.json` là sáng tác mới; không gắn nhãn trích dẫn hay chuyển soạn từ sách.

## Đầu vào và tra cứu

- Đọc `AGENTS.md`, skill `kaiwa-topic-dialogue`, hợp đồng `references/draft.md`, brief `dialogue.py H-004`, cả 15 tình huống V10 và các quan hệ `continues_from`.
- Tra `catalog27/BOOK_GUIDE.md`, `manifest.json` và tìm toàn bộ `source_index.jsonl` của 27 sách theo 社外, 社内, 伝言, 申し伝え, 検討, おっしゃる, 伺う, 弊社, 御社, 取り次ぐ, 折り返し, 承認. Chỉ các đoạn dưới đây được đọc sâu để làm căn cứ; không xem một hit chỉ mục là đã đọc chương.
- Đọc chuyên đề gần trước `sj-thuong-01/lesson.md` và lọc `practice.json` theo `topic_uid` H-004. Bài luyện trỏ đúng S003, S002, S009, S011, S012, S014; ID của bài chỉ ghi trong từng cảnh khi biểu thức tương ứng xuất hiện.

## Đoạn sách thực đọc

| Nguồn | Markdown, dòng đã rà | Điều dùng |
| --- | --- | --- |
| B03, *しごとの日本語 ビジネスマナー編* | `chapters/07-Unit06-敬語の使い方.md` 25–29, 37–49, 56–67 | Gọi người trong công ty trước khách và phân biệt hành động của mình/khách. |
| B04, *しごとの日本語 電話応対 基礎編* | `chapters/15-Unit14-伝言を伝える.md` 30–77 | `課長の山田` đối ngoại, `山田課長` nội bộ; chuyển lời bằng `と申しておりました`/`とのこと`. |
| B15, *上級レベル ロールプレイで学ぶ ビジネス日本語* | `chapters/02-bai-02.md` 7–35; `chapters/03-bai-03.md` 26–58 | Nhịp giới thiệu người đi cùng, cảm ơn khách, hỏi và xác nhận lời nhắn. |
| B18, *外国人のための日本語敬語の使い方 基本表現85* | `chapters/03-PART1-丁寧語・美化語.md` 523–564; `chapters/04-PART1-尊敬語.md` 392–407; `chapters/05-PART1-謙譲語・丁重語.md` 61–72 | 御社/弊社, おっしゃる, 伺う và đúng chủ thể. Đoạn B18-C05 chỉ dùng để đối chiếu, không gắn source_ref riêng. |
| B21, *日本語でビジネス会話 ― 中級編 ― 本文冊* | `chapters/14-shotaimen.md` 8–41 | Phân biệt chuyển lời người ngoài và người cùng phía. |

Đường dẫn đầy đủ và dải nguồn dùng trong từng cảnh nằm ở `admin_sources`; các dải bao trùm đoạn đọc. Không lấy lời sách làm lời thoại nguyên văn.

## Nguồn trực tiếp trên web

- [文化庁: 場面で異なる敬語～ウチとソト～](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter7/detail.html), đọc 2026-11-16: người cùng công ty là phía mình khi nói với đối tác, không nâng bằng kính xưng; tên/chức vụ có thể nói theo cách xác định người nhưng tránh `田中部長` như kính xưng. Dùng cho S001, S002, S005, S013–S015.
- [文化庁: 尊敬語 VS 謙譲語I](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/keigo/chapter4/detail.html), đọc 2026-11-16: tôn kính ngữ nâng chủ thể phía được nói tới; không nâng người bên mình. Dùng để rà S003, S011–S012.

Đây là hướng dẫn ngữ dụng tiếng Nhật, không phải quy trình/phí/điều kiện của doanh nghiệp cụ thể. Không có khẳng định về chính sách hay mức giá ngoài đời trong kịch bản. Các tên công ty, nhân sự, số chuyến, lịch và chi phí chưa định là ví dụ hư cấu, thống nhất trong từng nhánh.

## Tự rà theo sự kiện

- E01 S001–S004: giới thiệu Tanaka với khách, sửa chức danh Sasaki từ 部長 sang 企画課長, hỏi xin phép trao đổi, giới hạn cuộc nói còn năm phút và giữ “hai chuyến” là dự kiến.
- E02 S005–S008: lời Tanaka chỉ là mong muốn trao đổi tiếp; S006 sửa hiểu lầm thành cam kết triển khai. S007 ghi đúng yêu cầu chi phí ước lượng trước báo giá; S008 chuyển vào nội bộ, dùng `田中部長` đúng quan hệ và không hứa mức tiền.
- E03 S009–S012: `検討` không thành chấp thuận; S010 rút mốc thứ Sáu và xin phép gọi sau hai tuần. S011 xác định Nishimura đã xem tài liệu nhưng chưa nêu ý kiến. S012 là lượt liên hệ sau đó, sửa suy diễn “đã xem” thành “đã phê duyệt”.
- E04 S013–S015: tự sửa `田中部長` đối ngoại thành `弊社の田中`, nêu đích danh Yoshida và phân vai Yoshida/ Tanaka trong cuộc gọi kiểm lại.

Đã đọc nối toàn bộ 15 cảnh sau khi viết và đọc lại các cảnh sửa. Đã kiểm từng cặp JA–VI, tên/chức vụ, chủ thể của kính ngữ, mức chắc chắn và câu cuối. Bộ kiểm `dialogue.py H-004 --check` trả `OK H-004 15`. Trạng thái trong `status.json` là bản thảo đã tự rà, chờ root đánh giá độc lập; không ghi là root đã nghiệm thu.
