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

## Rà ba bước từng tình huống sau chỉnh sửa

Mỗi `uNN` bên dưới là hậu tố của turn ID `<situation_uid>-uNN`. Ba cột ghi lần lượt: đích/kết quả do đúng vai thực hiện; JA–VI và nối cảnh/nhánh; đọc hai vai theo cấp Thượng. Đây là tự rà của tác giả, không phải nghiệm thu của root.

| Tình huống / UID | Đích và kết quả | JA–VI, quan hệ cảnh | Hai vai và nhịp |
| --- | --- | --- | --- |
| S001 `fdf8e35f-25b4-5ae8-bad7-59e5d63f50da` | A-u03 mời vào việc; B-u07 nêu vướng; A-u05 nhận bước trình bày. | A-u01/u03 nói về bên mình bằng 弊社; B-u07 dùng 弊社 cho công ty mình. JA–VI và đáp trước/sau khớp. | Nakamura chủ nhà, Sasaki khách; người chủ nhà mở cuộc nói, nhịp Thượng vừa phải. |
| S002 `45c0d1ff-ab93-59f3-be7e-e42686921e4b` | B-u02 sửa đúng 企画課長; A-u03 xác nhận, B-u06 trở về tài liệu. | B-u04 gọi cấp trên phía mình là 部長の西村 theo chức danh mô tả, không nâng; bản Việt đúng chức vụ. | Hai vai vẫn lịch sự sau sai sót, không kéo dài xin lỗi. |
| S003 `3b84d201-24a4-57ef-991c-7107ec1b0ea4` | A-u01 xin lượt hỏi, B-u04 chưa chốt ngày, A-u05 hỏi số chuyến, B-u06 đáp dự kiến. | 伺う là hành động A; 御社 là phía B. VI giữ “dự kiến”, không biến thành quyết định. | Mỗi lượt hỏi một chi tiết; B trả lời đủ để A hỏi tiếp. |
| S004 `75c1c79b-c2ec-524e-b158-a092ea8b48f0` | A-u07 chọn thời điểm chuyến đầu vì chỉ còn năm phút; B-u08 nói nửa đầu tháng sau nhưng chưa chốt. | A-u09 giữ nửa đầu tháng là mốc tham khảo; không hỏi lại số chuyến đã có ở S003. JA–VI khớp. | B nêu giới hạn thời gian, A đáp gọn; chuyển sang lần sau hợp nhịp. |
| S005 `e19b81bb-0568-530e-ba6c-407be7e7f486` | A-u03 chuyển cảm ơn, A-u05 chuyển mong muốn gặp tháng sau; B-u07 cho biết phía mình đang chuẩn bị. | と申しておりました nói về Tanaka phía mình trước khách; B-u07 là chuẩn bị phía B, chưa phải đồng thuận hai bên. | Lời xã giao và thông tin chuẩn bị mở ra câu hỏi S006, không chốt hộ Tanaka. |
| S006 `9d44b6f7-9fe5-5bf0-829f-9c861f8ff449` | B-u01 suy thành hai bên đã đồng ý; A-u03 sửa “mong trao đổi” khác “đồng ý bắt đầu”; B-u06 rút cách hiểu. | A-u03 và VI đều giữ mức chắc chắn; B-u04 nói “hai bên” thống nhất, không đảo thành chỉ phía A. | Lượt sửa bảo toàn thiện chí, nêu bước xác nhận lại thay vì kết thúc bằng cam kết. |
| S007 `a07c6266-6f43-5868-a02c-0664d983a577` | B-u02 muốn giá tham khảo trước; B-u04 chưa yêu cầu báo giá; A-u05 nhắc lại ranh giới. | A-u03 nâng hành động muốn biết của B, A-u05 dùng いただいていない cho yêu cầu chưa nhận; VI không hứa giá. | Hai vai không lẫn “ước lượng” với “báo giá chính thức”; nối S008. |
| S008 `c78d02f7-0bb8-5324-86a3-85a2b6c569d7` | A-u03/u04 chuyển đủ hai ý từ S007, B-u05 nhận trách nhiệm phản hồi; A-u06 xác nhận chưa hứa số tiền. | 田中部長 và 佐々木課長 hợp khi A nói với Tanaka trong nội bộ; JA–VI giữ người chịu trách nhiệm. | Chuyển từ khách sang sếp đổi đúng lối xưng; cuộc thoại nội bộ ngắn. |
| S009 `1969ec01-e4bd-5f52-937d-0ad5da03dab4` | B-u01 chỉ nói xem xét; A-u03 hỏi mốc liên hệ; B-u06 nói mốc chưa bảo đảm có kết luận. | A-u07 chỉ xin cập nhật tình hình; VI không đổi 検討 thành chấp thuận. | B hạn chế mức cam kết, A tiếp nhận và chốt cách gọi lại. |
| S010 `6e69a888-899b-5ee9-94a6-baf6ee28a81e` | B-u01 rút mốc thứ Sáu đã nêu ở S009; A-u04 xin gọi sau hai tuần; B-u05 đồng ý điều kiện. | JA–VI giữ “chỉ hỏi tiến độ” và khả năng B báo sớm, không biến thành hứa quyết định. | Hai vai thương lượng thời điểm mới, nhánh pending kết thúc đúng trạng thái. |
| S011 `6f84117b-e8ce-509b-bf92-027c0d391755` | A-u01 hỏi có lời phản hồi; B-u02 đáp まだです, chỉ cho biết đã đọc; A-u03 kiểm lại chưa có ý kiến. | B-u02 dùng 西村 trần cho cấp trên cùng công ty trước khách; A-u03 nâng Nishimura phía đối tác. VI không nói “rồi”. | B trả lời trực tiếp câu hỏi trước khi giải thích, A thôi hỏi kết luận. |
| S012 `afa921b0-18ec-5c4e-a3d2-6dc195f5b608` | B-u01 cập nhật đã xem lại; A-u02 hiểu nhầm đã duyệt; B-u03 phủ định; A-u06 không báo nội bộ là đã quyết. | B gọi 西村 trần, A dùng 西村部長 cho phía khách. Bản Việt phân biệt xem tài liệu/phê duyệt. | Cảnh nối S011 là lượt liên hệ sau, không có phê duyệt bị suy diễn từ cảnh trước. |
| S013 `0a8d88be-6e6b-5d5f-a3fa-78a1d103ec12` | A-u01 tự sửa 田中部長 thành 弊社の田中; B-u02 hỏi thêm chi phí; A-u05 sẽ báo giờ gặp sau. | Không tôn kính hành động Tanaka phía mình; B-u04 それまでに được dịch là trước buổi trao đổi. | Sai sót có thật rồi sửa ngay, không kéo dài giải thích về kính ngữ trong lời thoại. |
| S014 `8d736f4a-07ff-59f5-abe2-c081fa8ca4fc` | B-u02 hỏi rõ あちら; A-u03 nêu Yoshida, A-u05 chia phần chi phí/hợp đồng. | VI giữ đại từ mơ hồ “bên ấy” rồi nêu người; Tanaka/Yoshida đều là phía A nên không kèm kính xưng trong lời A. | B có lượt hỏi tiếp để xác định đúng phạm vi, dẫn vào cuộc gọi S015. |
| S015 `f1252e1b-8415-5cbe-8180-1ae1da72a503` | B-u02 nhắc Yoshida sẽ gọi; A-u03 phân rõ hai đầu mối; B-u04 nói lại để kiểm. | A gọi Yoshida/Tanaka trần với khách, B dùng さん; VI khớp người đợi và người trả lời chi phí. | Cuộc gọi sau có mục đích xác nhận, không lặp cả lời S014; kết quả rõ cho hai vai. |

Đọc liên sự kiện: E01 tách giới thiệu/chức danh, quyền xin hỏi, giới hạn thời gian; E02 tách chuyển lời ra ngoài, sửa mức cam kết, nhận lời khách và báo nội bộ; E03 tách mốc hẹn, rút mốc, hỏi người quyết và sửa suy diễn; E04 tách sửa kính xưng, sửa người chịu trách nhiệm và xác nhận sau gặp. Các câu cuối theo đúng kết quả: chưa chốt vẫn để mở, người nhận trách nhiệm được nêu tên.

Sau chỉnh sửa, đã đọc nối cả hai vai của cả 15 cảnh và đối chiếu từng cặp JA–VI. `dialogue.py H-004 --check` được chạy lại; kết quả ghi trong bàn giao. `status.json` do root cập nhật theo hash nội dung mới.

Ở lượt rà cuối, điều phối viên sửa bản Việt của lời nhắn về chi phí (S007–S008), lời đáp đang chờ ý kiến (S011–S012) và câu xác nhận thỏa thuận ở S006. Đã đọc lại từng cặp trước/sau bằng cả hai ngôn ngữ. Các lượt đổi hẳn nội dung ở S001, S004 và S005 có ID mới.
