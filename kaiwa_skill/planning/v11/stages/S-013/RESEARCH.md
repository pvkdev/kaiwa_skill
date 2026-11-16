# S-013 — nghiên cứu và tự rà

Ngày đọc: 2026-11-16. Đã chạy dialogue.py và theo đủ 25 UID/tình huống V10 theo thứ tự. Tất cả lời thoại là sáng tác mới (`original_extension`); nguồn sách ở cấp cảnh chỉ là căn cứ ngữ dụng. Đã tra BOOK_GUIDE, manifest và source_index trong phạm vi B01–B27 theo chức năng nói, quan hệ và các cụm Nhật; đọc sâu đúng các dải dưới đây. Không tuyên bố đã đọc toàn văn 27 sách.

## Mạch, chuyên đề và phạm vi thực tế

Đã đọc `sj-so-03/lesson.md` và practice các UID hỏi hướng. Catalog 27 tìm 自転車, 駐輪, 修理, 鍵, 防犯登録; đọc B26/B08/B27 các dải ghi dưới. [Cảnh sát Tokyo — đăng ký xe](https://www.keishicho.metro.tokyo.lg.jp/kurashi/higai/guard/bicycle.html) ngày 2026-11-16 xác nhận đăng ký xe và giấy lưu tại cửa hàng được ủy nhiệm; S005 chỉ hỏi nhân viên hướng dẫn, S013 hỏi cách xác minh, không tự bẻ khóa. [Suginami — hướng dẫn gửi xe](https://www.city.suginami.tokyo.jp/documents/1601/jitensyaannnai5_1.pdf) xác nhận có loại gửi theo lượt và theo tháng tại quận, **không** xác nhận quy tắc bãi Aoba trong bài. Bãi Aoba, nhân viên, dãy A/B/C/D, giờ mở, phí, chuyển xe nội bộ, lịch sửa và giá xe/sửa đều hư cấu. E01 S004→S005 chọn xe đen sau khi màu xanh hết. E02 S008→S009→S010 tìm xe ở dãy B, không gán trộm. E03 S014→S015 quầy kiểm xe chuyển nội bộ rồi khách tự kiểm tình trạng. E04 S018→S020 đổi B sang C từ thứ Hai; S019 chọn C vì mở 6 giờ. E05 S021–S025 giữ lỗi phanh và xe cũ, không hứa bảo hành hay an toàn khi chưa thử.

## Đoạn sách đã đọc

- repair: 聞いて覚える話し方 日本語生中継 初中級編 1, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/05-bai-5.md` dòng 33–50. Cách hỏi sửa, thời gian và món kèm; tự viết cuộc thoại xe đạp.
- shop: どんどん話せる！日本語会話フレーズ大特訓 必須700, `kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md` dòng 183–207. Nói nhu cầu, hỏi giá/màu/đồ phù hợp ở cửa hàng.
- missing: 聞いて覚える話し方 日本語生中継 初中級編２, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/06-bai-05-shippai.md` dòng 209–225. Người không thấy xe hỏi trước khi kết luận; lời thoại được viết mới.

## Tự rà từng cảnh

- S001 `1d8dac57-c73a-591d-915a-3ad56f0a301f` (routine): Nêu quãng đường hằng ngày, nhân viên chuyển sang kiểm cỡ xe.
- S002 `428bc415-cb9e-5e83-8cf1-23db5a56b72d` (routine): Nói yên cao, nhân viên hạ và người học thử lại.
- S003 `3e7aed4e-35ff-5649-813c-b58cf99884c3` (routine): Hỏi giỏ và khóa theo mục đích mang túi, xin cả giá.
- S004 `01640fc4-ffd4-521c-9027-3ebed2cd770b` (conditional): Màu xanh chưa biết ngày về, người học chọn xem màu đen.
- S005 `be9cabc5-9580-5d6b-885f-505a94e86ee4` (resolved, nối S004): Tiếp S004, xác nhận xe đen 25.000 yên có khóa, giỏ riêng, hỏi đăng ký.
- S006 `3284ec51-42df-51c2-97a6-2e8c510148c9` (routine): Hỏi gửi một ngày, được chỉ kiểm phí tại lối vào bãi giả định.
- S007 `18dc4c23-5ef0-5251-a1de-780d66059885` (routine): Hỏi khu xe thường, nhận dãy A.
- S008 `23e1ab03-9c52-5214-862e-bc9dba8d175d` (problem): Không thấy xe, tả màu/khóa để nhân viên kiểm.
- S009 `c941500f-ca38-59c1-8ac6-ce19c6184041` (misunderstanding): Xe được chuyển dãy B bởi nhân viên, người học kiểm lại lý do.
- S010 `8db7c9a5-9ae0-5521-9f14-d261cd1d4a39` (resolved, nối S009): Tiếp S009, tìm thấy xe và hỏi vị trí hôm nay/lần sau.
- S011 `25a23798-8571-5f2a-9f67-f4a20d26718b` (routine): Lốp xẹp, hỏi sửa hôm nay; thợ cần xem trước.
- S012 `6b3d0bb1-14d3-5adb-ad45-3436d0affc1d` (conditional): Thiếu ruột, không hứa sửa tạm; người học dắt về và chờ kiểm hàng.
- S013 `5e8235d6-2dd4-50ef-8e00-776a48de5819` (routine): Mất chìa, hỏi cách xác minh chủ xe, sẽ mang giấy lưu.
- S014 `8d710395-bfe6-52ff-9ce1-553c9264e10f` (pending): Xe chưa thấy, quầy cần kiểm chuyển nội bộ; chốt bốn giờ gọi lại.
- S015 `93f8a7c6-12b1-57b0-9bbc-7592962380a0` (follow_up, nối S014): Tiếp S014, đến khu giữ và hỏi tình trạng/phí, tự kiểm thêm.
- S016 `8a617379-bcb4-5dc0-9db8-410748d4fa62` (routine): Hỏi gửi tháng và dãy gần lối bắc, yêu cầu kiểm chỗ.
- S017 `5c54a2a0-cb2b-5179-be73-548557fcbf12` (conditional): Vắng một tuần, phân biệt giữ chỗ tháng này và hạn dừng tháng sau đang kiểm.
- S018 `ba58e0d2-0848-543b-81ea-6e1b8be246ba` (problem): Dãy B sửa, nhận dãy C từ thứ Hai.
- S019 `5a8a7696-c8e1-5c60-9599-9323b1c6d67b` (alternative): So giờ mở hai khu và chọn C hợp mốc sáu rưỡi.
- S020 `7abb179b-dad8-557a-a4b8-c3e1076d9fcb` (follow_up): Sau đổi khu, kiểm xe ở C; không suy chỗ B vẫn dùng.
- S021 `8d35072d-47a3-59ed-8fa9-cda6728ca326` (problem): Phanh còn tiếng, dừng đi và yêu cầu kiểm lại.
- S022 `5a453864-f891-5dd0-80fb-d859646abbf1` (routine): Nhắc lỗi đầu và miếng phanh đã thay, tránh kiểm nhầm.
- S023 `ef51456a-372b-5de2-9de0-291c8cb867e0` (misunderstanding): Thợ tưởng mua mới, người học chỉ rõ xe cũ.
- S024 `1e777468-c79b-5f45-9fbb-3355156e6f11` (conditional): Chấp nhận để xe một ngày, hẹn ba giờ, phí sẽ báo sau.
- S025 `67f06f1f-1de3-5862-a521-d34bdfe66ae9` (resolved): Khi nhận, hỏi phanh và phí 1.000 yên, xin thử tại chỗ.
