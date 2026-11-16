# T-044 — nghiên cứu và tự rà hội thoại V11

Ngày đọc: 2026-11-16 (Asia/Tokyo). Phạm vi: 25 tình huống S001–S025 của chặng Trung “Gửi bưu kiện cá nhân và hỏi hàng quốc tế”. Đây là hội thoại mới do AI biên soạn; không có câu nào gán là lời nguyên văn từ sách. `dialogues.json` giữ riêng `ja`/`vi`, mã lượt, vai và nguồn quản trị.

## V10 và kế hoạch lời nói

Đã chạy `dialogue.py T-044` và đọc mục tiêu, 5 sự kiện, 25 tình huống, các nhánh/quan hệ `continues_from`, hai chặng liên quan trong brief. E01 hỏi trước khi gửi; E02 chốt kiện/địa chỉ/giá; E03 đổi thông tin sau gửi; E04 theo dõi và yêu cầu điều tra; E05 trả về hoặc hỏng. Những sự kiện này cùng khai thác quà cá nhân Nhật → Canada, ngoại trừ nhánh S023–S025 nói rõ một kiện khác Canada → Nhật để người học luyện vai người nhận.

- S001: Người gửi hỏi dịch vụ và theo dõi; quầy chưa biết khối lượng; kết quả là chọn hai phương án để cân và so.
- S002: Người gửi hỏi áo, sổ và nước hoa; nhân viên biết quy định cấm nước hoa; người gửi quyết định bỏ lọ ra.
- S003: Người gửi xử lý lời từ chối; nhân viên cần số lượng còn lại; hai bên thống nhất hàng và nhãn điện tử.
- S004: Người gửi ưu tiên giá/thời gian linh hoạt; quầy kiểm dịch vụ tại thời điểm gửi; quầy xác nhận hiện nhận gửi, người gửi chọn đường biển và đồng ý chờ lâu.
- S005: Sau S003, người gửi nhắc lại hàng và Canada; nhân viên kiểm tra quà/nhãn; chốt nội dung để xét điều kiện.
- S006: Người gửi ước lượng kích cỡ, cân nặng; nhân viên cân 1,8 kg; chuyển sang mức cước đến 2 kg.
- S007: Người gửi hỏi tổng cước, thời gian; nhân viên có kết quả tra bảng; chọn đường hàng không và xác nhận khoản trả tại quầy.
- S008: Nhân viên nhầm Australia; người gửi sửa thành Canada/Toronto; nhân viên tra lại và người gửi xin kiểm nhãn.
- S009: Địa chỉ thiếu số nhà; người gửi chưa biết; nhân viên yêu cầu hỏi người nhận trước khi gửi.
- S010: Sau S009, Sarah đã trả lời; người gửi đọc số nhà/phòng/mã bưu chính; hai bên đối chiếu tên, quốc gia, nhãn.
- S011: Người gửi báo Sarah sắp vắng hoặc đổi địa chỉ; nhân viên cần mã và giai đoạn vận chuyển; chưa hứa sửa được.
- S012: Nhân viên chưa rõ khả năng can thiệp; người gửi hỏi bộ phận và thời điểm; nhân viên ghi số gọi lại.
- S013: Nhân viên xác nhận kiện đã ra khỏi Nhật và phía Nhật không sửa được; người gửi hỏi Sarah liên hệ đầu mối nào.
- S014: Người gửi hỏi phát lại hay trả về; nhân viên giới hạn theo nước/dịch vụ; người gửi nhờ Sarah hỏi phía phát tại Canada.
- S015: Tiếp S012, nhân viên gọi lại với kết quả không sửa được; người gửi báo Sarah mã và tình trạng.
- S016: Người gửi nêu 2/10, trạng thái cuối 9/10 tại Canada và mã đủ 13 ký tự; nhân viên xác nhận lịch sử, gợi yêu cầu điều tra.
- S017: Nhân viên nhầm chiều Canada → Nhật; người gửi sửa Nhật → Canada, đọc mã/ngày; nhân viên tra đúng hồ sơ.
- S018: Tại quầy, người gửi yêu cầu điều tra; nhân viên chưa hứa hạn kết quả; hai bên thống nhất mốc hỏi tiến độ.
- S019: Sau hai tuần chưa có trả lời; người gửi dùng mã theo dõi trên liên gửi hỏi tiến độ rồi nhờ Sarah kiểm phía phát; nhân viên xin chia sẻ thông tin mới.
- S020: Sau S019, người gửi đọc lại việc từng phía làm; nhân viên nhắc giữ liên gửi và chờ đối chiếu kết quả.
- S021: Kiện gửi Canada đã trả về, dấu “UNCLAIMED”; người gửi hỏi nghĩa; nhân viên giải thích nghĩa thường gặp và kiểm hồ sơ riêng.
- S022: Sau S021, người gửi muốn gửi lại; nhân viên yêu cầu xác nhận người nhận/nhãn/cước tại lần gửi mới.
- S023: Nhánh khác, người nhận tại Nhật thấy cốc vỡ; tổng đài hỏi tình trạng hộp, hướng dẫn báo bưu cục phát và giữ chứng cứ.
- S024: Tiếp S023 tại tổng đài, người nhận hỏi có cần mang riêng chiếc cốc đến không; nhân viên yêu cầu giữ cả hộp/chèn/nhãn và báo sẽ có người đến kiểm tra.
- S025: Sau S024, tổng đài xác nhận bưu cục phát phụ trách, mốc liên hệ về chuyến kiểm tra và chỉ nói bồi thường sau khi có kết quả.

## Tra cứu kho 27 sách

Đã mở `BOOK_GUIDE.md` và `manifest.json`, quét toàn bộ `source_index.jsonl`: 27 sách, 22.110 entry. Tìm theo cả dịch vụ và hành vi giao tiếp: 郵便, 小包, 国際, 発送, 配達, 返送, 追跡, 住所, 荷物, 届か, 破損, 聞き返, 確認, 宅配, 送る, 届ける, 送り状, 郵便局, package, parcel, delivery; có 174 nhãn khớp. Chỉ mục chủ yếu là nhãn/heading nên đã đọc Markdown thật và đoạn trước/sau, không coi kết quả tìm là chứng cứ đủ.

Nguồn đã mở sâu (đường dẫn/dải dòng chính xác nằm trong `admin_sources`):

- B08, *どんどん話せる！日本語会話フレーズ大特訓 必須700*, `chapters/04-part4-bamen.md` dòng 255–405; phần bưu điện 356–383 có mở lời gửi hàng, hỏi thời gian bằng đường hàng không. Dùng chức năng nói, không chép nguyên câu.
- B05, *すぐに使える 接客日本語会話大特訓［英語版］決まり文句700*, `chapters/05-ch4-konbini.md` dòng 125–170; xem giọng nhân viên quầy và liên gửi. Đây là dịch vụ nội địa tại cửa hàng tiện lợi, **không** dùng làm căn cứ quy tắc bưu kiện quốc tế.
- B04, *しごとの日本語 電話応対 基礎編*, `chapters/32-Unit31-名前などを確認する（聞き取れているとき）.md` dòng 78–112; đọc cách nhắc lại số/chữ khi nghe thông tin. Dùng cho S008/S010/S017.
- B25, *聞いて覚える話し方 日本語生中継 中～上級編*, `chapters/02-bai-1-dengon.md` dòng 155–220; bài nghe nhắc số phiếu gửi và việc hỏi vì sao hàng chưa đến. Đoạn này là đề/ngữ liệu mục đích giao tiếp, không phải script lời thoại để trích.
- B09, *なめらか日本語会話*, `chapters/09-08-短縮句.md` dòng 38–68; xem cách hỏi lại thân mật nhưng không đưa vào lời nhân viên quầy do sắc thái không hợp. Không gán source ref cho cảnh.

## Chuyên đề gần trước

Đã đọc `kaiwa_skill/planning/v10/stages/sj-trung-11/lesson.md` và toàn bộ `practice.json`, đặc biệt các ví dụ gắn UID S005/S010/S020 cho ちなみに và S012 cho とりあえず. Bài `sj-trung-11-b12-39` được vận dụng ở S005/S010/S020, `sj-trung-11-b07-108` ở S012. Không gán `それが`, `一応`, `今日はここまでにしましょう` vì lời thoại hiện tại không dùng đúng những mục này. Ví dụ practice về “chỉ khi có phiếu báo vắng” ở S020 không được xem là chính sách áp dụng cho Canada.

## Xác minh nghiệp vụ Nhật Bản

Nguồn trực tiếp đều là Japan Post, truy cập 2026-11-16. URL, phạm vi và mục đích riêng ở `admin_sources`; các điểm ảnh hưởng quyết định đã được kiểm:

- [Loại không thể gửi](https://www.post.japanpost.jp/service/send/oversea/use/howto/index_en.html): nước hoa không thể gửi quốc tế, kể cả khi lọ nhỏ; các món khác vẫn cần kiểm nước đến.
- [Dịch vụ bưu kiện](https://www.post.japanpost.jp/service/send/oversea/list/delivery/i_parcel_en.html) và [bảng nhận gửi theo nước](https://www.post.japanpost.jp/service/send/oversea/information/overview_en.html): Canada hiện có bưu kiện air/surface, SAL không nhận; điều kiện có thể đổi nên nhân viên kiểm tại quầy.
- [Bảng cước 01/01/2026](https://www.post.japanpost.jp/assets/docs/service/send/oversea/charges_en.pdf): Canada là Zone 3; bưu kiện ≤2 kg surface 3.100 yên, air tổng 6.000 yên (có khoản thêm ghi trong bảng). Dùng ở S007 như kết quả nhân viên vừa tra, không áp thành giá bất biến. [So sánh phương thức](https://www.post.japanpost.jp/service/send/oversea/list/compare/index_en.html) cho surface khoảng 1–3 tháng; air nhanh hơn. Mọi ngày đến trong lời thoại là ước lượng. [Bảng ngày bưu kiện từ Tokyo](https://www.post.japanpost.jp/send/oversea/date/parcel/tokyo_en.html) ghi Vancouver/Montreal khoảng 9 ngày và cảnh báo không bảo đảm; không có dòng Toronto. Vì vậy mốc khoảng 10 ngày ở S007 là **ước tính giả định của nhân viên trong bài luyện cho Toronto**, được nêu rõ ở bối cảnh và trong lời, không phải số công bố riêng cho Toronto.
- [EAD/nhãn](https://www.post.japanpost.jp/question/oversea/153_en.html): hàng hóa cần dữ liệu điện tử; nhãn viết tay không dùng cho hàng hóa. [Thông quan](https://www.post.japanpost.jp/service/send/oversea/use/howto/ems_customs_en.html): khai đúng nội dung; quyết định nhập thuộc phía nước đến. [Địa chỉ](https://www.post.japanpost.jp/question/oversea/176_en.html): số điện thoại người nhận được khuyến nghị; không tự bảo đảm giao được khi thiếu số nhà.
- [Sửa địa chỉ EMS](https://www.post.japanpost.jp/question/oversea/135_en.html): FAQ áp cho EMS, minh họa giới hạn can thiệp trước khi xong chuẩn bị đi quốc tế. Hội thoại dùng **bưu kiện quốc tế**, nên nhân viên kiểm hồ sơ cụ thể rồi mới nói không sửa được tại phía Nhật; không suy quyền chuyển địa chỉ toàn cầu từ FAQ EMS.
- [Điều tra bưu gửi](https://www.post.japanpost.jp/question/oversea/18_en.html) và [cách nộp yêu cầu](https://www.post.japanpost.jp/service/send/oversea/use/download/chousa_en.html): bưu kiện gửi ra nước ngoài có thủ tục yêu cầu điều tra tại quầy; không biến cuộc gọi hỏi tiến độ thành nộp đơn qua điện thoại. [Web điều tra](https://www.post.japanpost.jp/service/send/oversea/mypage/web-inquiry/) đang thí điểm hẹp và phản hồi nước đến có thể kéo dài; không hứa hạn kết luận.
- [Ký hiệu trả về](https://www.post.japanpost.jp/question/oversea/22_en.html): UNCLAIMED = không được nhận trong thời hạn; lời thoại vẫn kiểm hành trình riêng. [Hàng hỏng](https://www.post.japanpost.jp/question/oversea/16_en.html): người nhận tại Nhật báo bưu cục phát ngay và giữ cả vật bên trong lẫn bao bì; bồi thường chỉ sau kiểm tra, không hứa quyền/mức trả.

## Tự rà và bàn giao

Đã đọc nối toàn bộ 25 bối cảnh, 151 lượt Nhật–Việt ở cả hai vai; sửa các cảnh nhân viên mở lời S008/S013/S015/S017 để `speaker_id` đúng vai, sửa xưng hô Việt theo giọng nữ người gửi/nhận và giọng nam nhân viên. S007 bổ sung cước và so thời gian có nguồn; S016 đọc đủ mã ví dụ 13 ký tự và nêu trạng thái cụ thể; S023–S025 giữ một tổng đài hỗ trợ đến khi xác định bưu cục phát và thống nhất kiểm tra tại nơi nhận; S013 sửa thì hiện tại 日本を出ています, S019 dùng mã theo dõi nhất quán. Những con số địa chỉ/tên người/mã chỉ là dữ kiện hư cấu của bài luyện, không phải địa chỉ thật; không có hứa bảo đảm phát, chuyển tiếp hay bồi thường. Tất cả `turn_origins` là `original_extension`.

Đã chạy `py -X utf8 .agents/skills/kaiwa-topic-dialogue/scripts/dialogue.py T-044 --check kaiwa_skill/planning/v11/pilot/T-044/dialogues.json` và nhận `OK T-044 25`. Kiểm đó chỉ xác nhận cấu trúc; root cần đọc độc lập nội dung/nguồn và xem preview. `status.json` đánh dấu “reviewed” ở phạm vi **tác giả tự rà**, root review vẫn pending.
