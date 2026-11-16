# S-043 — Điện thoại công sở: nghe & chuyển máy

Đọc brief đủ 12 UID, ba sự kiện và các mạch S001→S002/S003→S004, S005→S006/S007/S008, S009→S010, S011→S012. Tra 27 sách theo `おつなぎします`, `取り次ぐ`, `折り返し`, `間違い電話`; đọc B04 *しごとの日本語 電話応対 基礎編*:

- `kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/05-Unit04-担当者へ取り次ぐ.md`, dòng 5–74: hỏi rõ ai gọi và người cần gặp, báo chuyển, nói tên khách với người nhận.
- `chapters/08-Unit07-担当者が不在のときの対応.md`, dòng 5–10 và 58–80: thông báo người cần gặp chưa nghe được, phân biệt khách tự gọi lại với phía công ty sẽ liên hệ.
- `chapters/11-Unit10-間違い電話を受けたとき.md`, dòng 5–37: nói rõ bộ phận đang nghe và hỏi lại trước khi chuyển.

Đọc `kaiwa_skill/planning/v10/stages/sj-so-10/lesson.md` và tra UID trong `practice.json`. Tsuki, Morita Shōji, các nhân vật, lịch họp và cách chuyển máy là tình huống hư cấu. Không tiết lộ số cá nhân, không dự đoán giờ kết thúc cuộc họp, không hứa người cần gặp sẽ rảnh vào giờ khách tự gọi lại. Chỉ hứa gọi lại sau khi xác nhận được số công ty của khách.

Tự đọc JA và VI riêng từng cảnh, rồi đọc nhánh. S001 nghe công ty và người cần gặp, còn hỏi lại tên Ito; S002 xác nhận tên, S003 có thể chuyển, S004 báo người nhận nội bộ đúng tên. S005 Sato đang họp, không biết giờ xong; S006 chờ một phút nhưng không hứa Sato sẽ nghe, S007 khách tự gọi lại, S008 bên tiếp nhận xác minh rồi liên hệ. S009 là phòng kinh doanh nhận nhầm cuộc gọi dành cho tổng vụ, S010 sửa thành kế toán trước khi chuyển. S011 gọi lại người đã bị ngắt máy, S012 Tanaka đồng ý nhận mới nối. Hai cảnh nói với người nhận nội bộ dùng vai cụ thể thay cho nhãn chung của sự kiện. Các lượt là `original_extension`; `dialogue.py --check` đạt. Độc lập biên tập còn chờ root.
