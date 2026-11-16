# Kế hoạch V7 · Xen chuyên đề Speak Japanese vào lộ trình Kaiwa

**Mục tiêu của V7 là quyết định dạy kiến thức nào cùng nhau, ở cấp nào và ngay trước những chặng topic nào.** Sản phẩm để review là một lộ trình có hai loại chặng, cùng chỉ mục để mở từng bài sách và từng cơ hội áp dụng. Nội dung bên trong chặng chuyên đề sẽ được thiết kế sau khi nhìn thấy bản đồ này.

## Điểm xuất phát

V6.5 có 289 chặng topic theo thứ tự Sơ 80, Trung 145 và Thượng 64. Có 125 chặng đã tuyển được bài shadowing, 164 chặng đi tiếp với phần thực hành tình huống. V6.4 giữ 1.592 lượt gán cũ của chín sách. Catalog V6.3 có **1.124 đơn vị nguồn duy nhất** gồm bài chính và tài liệu hỗ trợ. Trong đó, B05 có 120 đơn vị và 159 lượt gán, dùng làm kiến thức tham khảo cho tình huống tiếp khách. Phạm vi chuyên đề gồm **1.004 đơn vị của tám sách**, tương ứng 1.433 lượt gán cũ. Số chuyên đề học được quyết định sau khi đọc và gom theo chức năng nói.

| Sách | Đơn vị nguồn | Chất liệu cần chú ý khi đọc |
|---|---:|---|
| B06 | 203 | Câu ngắn nâng cao, sắc thái và quan hệ giữa hai bên |
| B07 | 207 | Câu ngắn thường dùng, vào lời và phản hồi trong đối thoại |
| B11 | 109 | Chức năng của mẫu cơ bản, các cặp ví dụ dễ nhầm |
| B12 | 104 | Mẫu nâng cao và tác dụng của việc chọn cách diễn đạt |
| B18 | 104 | Kính ngữ, hướng hành động, vị trí người nói và người nghe |
| B19 | 89 | Từ tượng thanh/tượng hình dùng trong lời nói thực |
| B20 | 94 | Cách nói cố định và hoàn cảnh dùng tự nhiên |
| B24 | 94 | Biểu đạt cảm xúc và đáp lại cảm xúc |

B08 必須700 tiếp tục thuộc nguồn shadowing topic. [Dữ liệu V6.5](../v6_5/STATUS.json) · [Catalog nguồn](../v6_3/coverage) · [Hồ sơ vị trí cũ](../v6_4/admin)

[Khảo sát đặc điểm tám sách](NGHIEN_CUU_8_SACH.md).

## Các mốc thực hiện

1. Đối soát 1.004 khóa pack với nguồn V6.3. Ghi hash, phạm vi và các phần đi kèm. Dùng 1.433 lượt gán cũ làm manh mối khi tìm vị trí. Chuẩn bị mỗi pack một phiếu đọc.
2. Pilot đề xuất ở ba vùng Sơ, Trung và Thượng. Với mỗi chuyên đề, bàn giao tên tiếng Việt, mục tiêu ngắn, level, chỗ chèn, danh sách pack nguồn nguyên vẹn theo thứ tự, lý do nhóm và lý do chọn vị trí. Nên xem cả trường hợp hỗ trợ trực tiếp một topic lẫn chuyên đề độc lập có giá trị lâu dài.
3. Khi triển khai toàn bộ, đọc đủ tám sách. Có thể giao worker theo nhóm B07/B11, B06/B12/B18 và B19/B20/B24 rồi điều phối nhóm chuyên đề trên toàn kho. Chọn level theo nội dung thực. Tái dùng nguyên pack ở cấp sau nếu hữu ích. Số pack trong chuyên đề và số chặng mỗi cấp phụ thuộc chất liệu sách.
4. Xen các chuyên đề vào 289 topic V6.5, giữ thứ tự tương đối của topic. Rà độ khó, tên chuyên đề, thứ tự pack, mật độ chặng và lợi ích của các lượt ôn. Khi có topic phía sau phù hợp, ghi rõ tình huống được hỗ trợ. Với kiến thức độc lập, nêu lý do học ở điểm đó.
5. Khi phát hành, xuất JSON, preview và báo cáo truy ngược theo sách. Đếm pack duy nhất và lượt đặt theo level, ghi từng ngoại lệ. Kiểm nguồn nguyên vẹn, khôi phục từ checkpoint, duyệt bản đọc và commit V7. Cách giảng, kết hợp ví dụ trong video và flow luyện thuộc pha sản xuất bài giảng.

## Ví dụ một quyết định để review

**Mở lời khi muốn hỏi hoặc nhờ ai đó** · Trung · dự kiến trước T-012 “Nhờ vả, nhận lời & từ chối khéo”.

1. B11, pack `B11/u-88-part2-61`, bài 61 ちょっと聞きたいんだけど. Đặt trước vì bài giới thiệu cách mở lời bằng ～が／～けど khi muốn hỏi hoặc mong người nghe giúp.
2. B07, pack `B07/u-200-091`, bài 91 悪いんだけど. Đặt tiếp để gặp cách báo trước rằng việc mình sắp nhờ có thể làm phiền người kia. Giữ cả ví dụ từ chối đổi ca cùng những cách nói đi với ちょっと và 急で.

Tên chuyên đề nêu trọng tâm chung. Một pack có thể mang theo nghĩa mở rộng ngoài trọng tâm đó. T-012/S001 và S002 là cơ hội vận dụng sớm. Đây là ví dụ thiết kế dùng hai khóa có thật, chờ so với các pack khác trong pilot. Một chuyên đề về sắc thái biểu cảm cũng có thể chọn vị trí theo độ khó và kiến thức đã làm quen, dù chưa tìm thấy topic liền sau dùng trực tiếp.

## Cách duyệt

Người review nhìn một đoạn lộ trình, đọc tên chuyên đề, mở lần lượt từng pack gốc và quyết định cấp độ, nhóm, thứ tự hoặc vị trí nào cần chỉnh. Khi xong toàn bộ, mỗi pack của tám sách có chuyên đề tiếp nhận hoặc lý do ngoại lệ thực sự bất hợp lý. Lưu nguyên cả các tài liệu hỗ trợ có giá trị và chỉ rõ chúng được đặt ở đâu.

[Skill phân bổ V7](../../../.agents/skills/kaiwa-speak-japanese-roadmap/SKILL.md) · [Quy ước dữ liệu](../../../.agents/skills/kaiwa-speak-japanese-roadmap/references/allocation.md)
