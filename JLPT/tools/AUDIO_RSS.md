# Ghép audio Spotify RSS vào đề JLPT

Admin dùng [JLPT_AUDIO.xlsx](../JLPT_AUDIO.xlsx). Mỗi dòng ứng với một file nghe tổng của kỳ thi. Cột A dùng cấp độ và năm/tháng để phân biệt các đề. Mỗi thư mục kỳ đang hoạt động có một dòng để theo dõi audio. Thư mục kỳ có dấu `.defer-audio-rss` sẽ xuất hiện lại khi có file audio mới. Riêng N3 tháng 07/2015, nguồn đã xác nhận chỉ cung cấp phần viết. [Kiểm kê nguồn](../N3/1507/KIEM_TRA.md)

1. Đăng tập podcast bằng chính tên file gốc ở cột B, có thể bỏ phần mở rộng trong tiêu đề. Ví dụ file `JLPT-N3-2025-07.mp3` dùng tên tập `JLPT-N3-2025-07`. Dùng đúng cùng bản thu để các mốc đang lưu vẫn trỏ đúng vị trí.
2. Dán **URL của feed RSS** vào ô vàng **B4**, lưu rồi đóng Excel.
3. Tại gốc thư mục `JLPT`, chạy lệnh dưới đây. Workbook lấy lại toàn bộ danh sách theo các file trên đĩa và ghi mỗi URL phát trực tiếp ở cột D, tựa tập ở cột E, trạng thái gói ở cột F. B4 là ô nhập duy nhất. Cột dữ liệu được tạo lại mỗi lần chạy.

```powershell
.\tools\sync_exam_audio.ps1
```

Lệnh dùng Python 3.11+ và `jsonschema` như validator hiện tại, FFprobe (FFmpeg) để kiểm bản audio cũ chưa lưu digest, cùng Node và `@oai/artifact-tool` từ Codex Workspace trên Windows. Máy có nhiều bản runtime sẽ dùng bản mới nhất đã cài. Có thể đặt `JLPT_WORKSPACE_DEPENDENCIES` tới thư mục `dependencies` của runtime.

**Tệp nguồn và cách ghép.** Công cụ lấy tên từ tệp có thật trong thư mục nguồn đang dùng ở `N1` đến `N5`. Thư mục `old/` và gói import lưu từ kỳ cũ không tạo dòng trong sổ. Công cụ so khớp chính xác tên (hoặc tựa bỏ phần mở rộng) sau chuẩn hóa Unicode và chữ hoa/thường. Nếu dịch vụ đổi tên enclosure thành mã nội bộ, tựa episode vẫn dùng được. Các trang tiếp trong RSS được đọc qua liên kết `rel=next`. Candidate phải có một GUID, một enclosure audio HTTPS và chỉ ứng với một kỳ. Nếu tên file theo mẫu JLPT-N3-2025-07 thuộc kỳ khác thư mục đang chứa, dòng đó yêu cầu kiểm tra. Tên giống nhau ở hai tập, một URL/GUID dùng nhiều lần hoặc một kỳ có nhiều file đều hiện thành dòng cần xử lý. Khi có dữ liệu thời lượng, gói bị giữ lại nếu RSS lệch master từ hai giây. Với gói cũ có timeline theo HTML nhưng chưa có digest audio, FFprobe đo file local để kiểm cùng ngưỡng trước khi ghi URL.

**Gói dữ liệu.** Với đề đã biên soạn, công cụ ghi `masterAudio.rss.{feedUrl,episodeGuid,enclosureUrl}`, giữ các UUID, section, digest asset local, thời lượng và mốc câu. Gói thay đổi tăng một revision và được kiểm hợp đồng cùng hash nguồn/assets trước khi thay thế file. Cùng URL và metadata thì revision giữ nguyên. Ở hợp đồng 1.3, checklist COVERAGE được tính lại sau khi gắn URL. Các ghi chú review thủ công và checklist lưu sẵn của gói 1.1/1.2 được bảo toàn. Khi nâng bản cũ, rà lại các ghi chú MISSING_MASTER theo master hiện hành. Sau khi gắn lần đầu hoặc khi thay bản thu, nghe đối chiếu đầu, giữa, cuối trên URL RSS với mốc gốc.

**Đề chưa có gói.** URL vẫn hiện trong Excel. Sau khi tạo `packages/<cấp>/<YYYY-MM>/package.json`, dùng bản feed gần nhất đã lưu để điền các gói mới, kể cả khi đang offline. Feed cache theo chính URL B4 và nằm dưới `work/rss/` cục bộ.

```powershell
.\tools\sync_exam_audio.ps1 -UseSavedFeed
py -3 tools/build_pilot_bundle.py
```

Nhập **thư mục mới được lệnh build in ra** tại `/admin/jlpt-exams/import`. Công cụ đóng gói tự tạo lại hash của catalog và kiểm byte của mỗi package. Các bundle pilot cũ là snapshot bất biến. Với gói approved, tạo catalog release bằng `py -3 tools/build_catalog.py` như quy trình migration. Khi source đã chuyển đường dẫn hoặc đổi nội dung so với SHA lưu trong gói, URL ứng viên vẫn hiện trong Excel, cột F ghi cần kiểm tra và console chỉ ra file lỗi. Cập nhật provenance trong gói rồi chạy lại.

**Khi đổi kênh hoặc thay episode.** Cùng GUID và feed được phép đổi URL enclosure. Đổi GUID hoặc feed cần đối chiếu lại timeline rồi chạy với `-ReplaceEpisode`. Tùy chọn này áp dụng cho mọi dòng khớp trong lần chạy. Có thể dùng `-Root <thư-mục-staging>` để kiểm tra bản sao trước. Để dùng bản XML đầy đủ mà admin đã lưu, truyền `-RssFile <đường-dẫn-xml>` cùng URL gốc trong B4. Khi mạng lỗi, lần chạy báo lỗi và giữ workbook trước đó.

**Kiểm tra.** Chạy `py -3 tools/test_sync_exam_audio.py` để thử ghép theo tên/tựa, URL đã mã hóa, feed nhiều trang, trùng tên, sai thời lượng và chạy lặp. Kiểm tra thủ công bằng cách lọc “Khớp tên”, mở URL audio và so với file có đường dẫn ở cột G.
