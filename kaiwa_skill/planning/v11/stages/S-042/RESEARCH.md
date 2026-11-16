# S-042 — Gọi điện cho bạn, thầy cô & đặt chỗ

Đọc brief đủ 20 UID, bốn sự kiện và các nhánh S004→S005, S008→S009, S013→S014, S018→S019→S020. Tra 27 sách theo `電話をかける`, `伝言`, `予約`; đọc trực tiếp:

- B27 *聞いて覚える話し方 日本語生中継 初中級編２*, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/07-bai-06-denwa-o-kakeru.md`, dòng 170–211: hỏi đúng người, nhắn lời, tự gọi lại và kết thúc điện thoại.
- B08 *どんどん話せる！日本語会話フレーズ大特訓 必須700*, `kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/02-part2-kinou.md`, dòng 400–428: mở lời đặt chỗ và đổi đặt chỗ.
- B05 *すぐに使える 接客日本語会話大特訓［英語版］決まり文句700*, `kaiwa_skill/knowledge/すぐに使える 接客日本語会話大特訓［英語版］決まり文句700/chapters/03-ch2-inshokuten.md`, dòng 43–62: xác nhận đặt chỗ theo tên khi tới quán.

Đọc `kaiwa_skill/planning/v10/stages/sj-so-10/lesson.md` và tra UID trong `practice.json`. Hina, các chỗ trống, giờ 19/19:30 và việc không giữ được bàn cũ đều là dữ kiện của nhà hàng hư cấu, không gán chính sách giữ bàn cho nơi khác. Lời hỏi còn chỗ chưa tự tạo đặt chỗ; chỉ khi nhân viên đọc lại tên, giờ và số người thì mới chốt.

Tự đọc JA và VI riêng từng cảnh, rồi đọc các mạch. Mai bận nên hẹn 19 giờ, tới S005 mới bàn được giờ gặp. Ở nhà cô Mori, mẹ cô chỉ nhận lời nhắn rằng người học tự gọi lại 18 giờ; S009 đúng người mới hỏi nội dung. Nhánh nghe nhầm ba người được sửa thành hai trước khi S014 xác nhận đủ thứ Sáu 19 giờ, hai người, tên Nguyễn. Ở S018 bàn 19 giờ đã mất và bàn 19:30 chỉ đang kiểm; S019 nhân viên mới xác nhận đổi, S020 khách đến theo giờ mới. Các lượt là `original_extension`; `dialogue.py --check` đạt. Độc lập biên tập còn chờ root.
