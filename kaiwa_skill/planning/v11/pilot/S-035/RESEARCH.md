# S-035 — hồ sơ biên soạn và tự rà

## Đầu vào và nguồn

- Mốc: `kaiwa_skill/planning/v10/KAIWA_CHANG_V10.jsonl`, UID chặng `eb72c7c9-57d0-51a3-9260-0dbbc625cdaa`; 20 UID tình huống giữ đúng thứ tự. Đã chạy `dialogue.py S-035` và đối chiếu bốn sự kiện, các nhánh `continues_from`.
- Catalog: đọc `kaiwa_skill/planning/catalog27/BOOK_GUIDE.md`, `manifest.json`, tra `source_index.jsonl` theo 依頼, 頼, 手伝, お願い, 写真, 断る, ちょっといい, 受け取る, thời điểm và cách nói với người quen/người lạ. Rà các đầu mối B01, B02, B07, B08, B11, B14, B17, B24, B26, B27; mở sâu những đoạn được ghi `admin_sources`. B02 là bối cảnh công việc nên chỉ rút nguyên tắc hỏi hạn và nêu giới hạn, không mang vai công sở sang cảnh bạn bè.
- Nguồn sách thực đọc: B07 `06-part1-requests.md` dòng 18–27 và 58–67, `10-part2-routines.md` dòng 387–397; B08 `02-part2-kinou.md` dòng 100–126; B26 `01-bai-1.md` dòng 256–304 và `06-bai-6.md` dòng 193–218; B02 `08-依頼する.md` dòng 299–348. Đường dẫn đầy đủ, nhan đề theo manifest, phạm vi và mục đích sử dụng nằm trong `dialogues.json`. Các lời thoại đều là `original_extension`: không nhận là câu trích sách.
- Chuyên đề liền trước `sj-so-08`: đã đọc `lesson.md`, `manifest.json`, `practice.json`. `ちょっといいですか` được dùng ở S001, S002, S007; `～んです` nêu hoàn cảnh ở S006. Bài luyện có dẫn UID S002/S007 và mẫu hỏi đường S001, mở cửa S006. Đoạn thực được viết lại cho đúng nhánh V10. Các ID chuyên đề chỉ gắn nơi câu thực sự biểu hiện cách dùng.
- Điều tra thực tế: đây là giao tiếp xã hội ở lớp, công viên và trung tâm sinh hoạt giả định. Không có khẳng định về phí, quyền, giờ mở cửa hay thủ tục. Giờ 2:55, 2:58, 3:00, 3:05 và 3:30 là dữ kiện kịch bản, nhất quán trong từng chuỗi. Vì vậy không đưa URL web vào hồ sơ.

## Ba lượt rà theo UID

Mỗi dòng ghi (1) lượt người học thực hiện mục tiêu và lời đáp, (2) nghĩa Nhật–Việt và tính tiếp nối, (3) kết quả khi thử nói cả hai vai. Hash nội dung từng cảnh đã duyệt nằm trong `status.json`; sửa cảnh phải rà lại và cập nhật hash. `reviewed` ở đây là **tự rà của worker**, root còn `pending`.

| Cảnh | Lượt việc đích và kết quả tự rà |
|---|---|
| S001 | Người học u01 nhờ chỉ đường; bạn u02/u04 cho tầng, lối rẽ. u03 hỏi đúng chi tiết thiếu, u05 xác nhận rẽ phải; hai ngôn ngữ đều chưa ngụ ý đã đến nơi. |
| S002 | u01 nhờ trông túi năm phút thôi. Ở u02 và u03 hai bên vẫn đang đợi kết quả xem lịch. |
| S003 | Bạn u01 nhận trông năm phút; người học u02 tự chốt 3:00, bạn u03 nhắc lại. u04 giao việc sau khi đã nhận lời; không lặp lời xin ở S002. |
| S004 | Bạn phải đi lúc 2:58. Người học u05 hỏi có thể để túi đến 2:57 để sang đặt tờ giấy. Bạn u06 nhận lời, người học u07 xác nhận quay lại ngay. |
| S005 | Bạn u01 phải đi ngay. Người học u02 tự mang túi theo. Hai bạn chào nhau ở u05 và u04. |
| S006 | Người học u01 nói rõ mở cửa và lý do đang bê hộp; người kia u02 mở, u03 cảm ơn. Vai người lạ dùng lịch sự, không thêm quy tắc địa điểm. |
| S007 | Người học u01 nhờ đúng một ảnh, u03 chỉ vị trí; người kia u04 bắt đầu chụp. Điện thoại chưa được trả trong cảnh này, để S010 xử lý. |
| S008 | Người học u01 nhờ ảnh; người kia u02 có điều kiện làm nhanh. u03 thu hẹp còn một tấm và u04 nhận đúng phạm vi; không suy là người kia rảnh lâu. |
| S009 | Người học u01 nhờ; người kia u02 từ chối mềm, u03 tự chụp và cảm ơn. Việt giữ mức từ chối, không tự bịa lý do. |
| S010 | Người kia u01 trả điện thoại; người học u02 nhận điện thoại và cảm ơn, người kia u03 hỏi về ảnh, u04 khen ảnh và cảm ơn. Không xin phép xem ảnh trên điện thoại mình. Cảnh chỉ mở sau nhánh S007. |
| S011 | Người học u01 báo kéo dài và nhờ thêm năm phút, u03 cho phép từ chối; bạn u02 chưa nhận lời. Giờ 3:05 là hạn đề nghị, không phải cam kết. |
| S012 | Bạn u01 từ chối vì phải đi 3:00; người học u02 hỏi điểm lấy túi, u04 xác nhận đến cửa ngay. Việc nhận túi chưa bị suy là đã xong. |
| S013 | Người học u01 nói 3:00, bạn u02 nói 3:30; người học u03 nhận hiểu sai và hỏi giờ tiện, bạn u04 đáp. Hai bản đều phân biệt 3:00 với 3:30. |
| S014 | Chính người học u01 chốt đầy đủ 3:30 + cửa vào trung tâm; bạn u02 nhắc lại. u03 nói sẽ gọi nếu muộn, không hứa chắc đến trễ. |
| S015 | Người học u01 hỏi nhận lại túi tại điểm hẹn, bạn u02 trao; u03 cảm ơn. Nhánh S013→S014 đã chốt giờ nên không hỏi lại vô ích. |
| S016 | Bạn u01 nhờ chung, người học u02 hỏi việc cụ thể; bạn u03 nói hai ghế, người học u04 nhận đúng hai ghế. Người học không nhận việc mơ hồ trước khi hỏi. |
| S017 | Bạn u01 nhờ ba hộp; người học u02 nêu chỉ mang được một, bạn u03 tự nhận hai hộp còn lại. u04 bắt đầu phần đã nhận; JA–VI cùng phạm vi. |
| S018 | Bạn u01 nhờ chuyển ghế hôm nay; người học u02 từ chối ngắn vì bận, u04 để ngỏ nếu lần khác có việc. Không hứa giúp hôm nay hay buộc bạn chờ. |
| S019 | Bạn u01 thêm giấy khi đang xếp ghế; người học u02 hỏi ưu tiên, bạn u03 chọn giấy, u04 nhắc lại. Trình tự việc đổi đúng theo câu đáp. |
| S020 | Người học u01 tự bàn giao giấy đã dán và hai ghế chưa xếp; bạn u02 nhờ nốt hai ghế, u03 nhận. Không báo hoàn thành toàn bộ khi chưa xong. |

## Checkpoint và giới hạn

`status.json` giữ SHA-256 V10, skill, từng trích đoạn sách, bản JSON và từng cảnh. Không có `needs_fix` sau tự rà. Cần root đọc preview trên PC/mobile, kiểm vai/giọng, Nhật–Việt, nhánh và việc metadata không hiện cho học viên; chưa có quyền phê duyệt hàng loạt.
