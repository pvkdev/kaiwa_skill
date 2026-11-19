# Nghiệm thu pilot shadowing V13

[Mở chín bài trong preview](pilot/PREVIEW.html) · [Skill soạn bài](../../../.agents/skills/kaiwa-topic-shadowing/SKILL.md)

Ba worker Sol/high, mỗi worker phụ trách một cấp. Điều phối đọc các bản thảo, sửa skill sau vòng 1 và vòng 2, xóa dữ liệu pilot của vòng đó rồi giao lại từ đầu. Cả chín chặng đều có checkpoint từ vựng V12 hợp lệ và hội thoại tình huống V11. Thư mục pilot lưu lần soạn cuối.

## Thay đổi qua ba vòng

- **Vòng 1 — 3 chặng, 72 câu.** Mỗi chặng có 24 câu. S-011 có câu hỏi lồng hai cấu trúc như 「切符を見てもらうには、どの窓口に行けばいいですか。」. H-020 mở đầu đã yêu cầu người học xử lý cả phạm vi quyết định lẫn phương án gộp đầu mối. T-008 còn thiên về nhắn tin ở phần hỏi thăm. Bổ sung bước đọc ba câu đầu, thử cách hỏi đơn giản hơn ở Sơ và xác định lúc nào có thể thực sự nói từng câu. Bản thảo ghim phiên bản nguồn và skill ngay khi lấy brief.
- **Vòng 2 — 6 chặng, 135 câu.** Soạn lại ba chặng cũ rồi thêm S-024, T-044, H-004. S-011 giảm xuống 21 câu với nhịp mở ngắn. Một số câu như hỏi hoãn việc ghi chép trong T-008 cần nhìn ngữ cảnh mới thấy ý giúp đỡ. T-044 còn dịch lời nhờ kiểm tra kiện hàng thành “đề nghị điều tra”. Bổ sung hai lượt đọc riêng. Lượt Nhật che vai và tiêu đề để tự xác định mục đích nói. Lượt Việt đọc thành tiếng rồi đối chiếu vai, mức cam kết và độ lịch sự.
- **Vòng 3 — 9 chặng, 199 câu.** Soạn lại sáu chặng, thêm S-003, T-002 và H-002. T-008 dành 19 câu cho việc lắng nghe và đề nghị hỗ trợ. T-044 có 24 câu, trong đó yêu cầu tra soát đã thành lời người gửi có thể dùng ở quầy. H-020 mở bằng 「今日の会議で決めたいことは何ですか。」 rồi mới tới phân biệt chủ trương, phê duyệt và phạm vi thử nghiệm.

## Chín bài để duyệt

“Cảnh” đếm mã tình huống V11 riêng biệt mà người soạn liên kết với ít nhất một câu. “Từ” đếm mục từ V12 riêng biệt được đánh dấu trong bản thảo. Đây là chỉ số truy nguồn. Mỗi bài tự chọn các động tác nói quan trọng để luyện. “Mẫu lặp” đếm nhãn mẫu xuất hiện từ hai lần trong cùng một bài.

| Chặng | Số câu | Nhóm | Cảnh liên kết / có trong V11 | Từ V12 | Mẫu lặp |
| --- | ---: | ---: | ---: | ---: | ---: |
| [S-003](pilot/S-003/shadowing.json) | 20 | 5 | 15/15 | 27 | 4 |
| [S-011](pilot/S-011/shadowing.json) | 22 | 5 | 15/15 | 26 | 4 |
| [S-024](pilot/S-024/shadowing.json) | 24 | 5 | 20/20 | 40 | 3 |
| [T-002](pilot/T-002/shadowing.json) | 23 | 5 | 22/25 | 19 | 2 |
| [T-008](pilot/T-008/shadowing.json) | 19 | 5 | 13/15 | 13 | 2 |
| [T-044](pilot/T-044/shadowing.json) | 24 | 6 | 21/25 | 26 | 2 |
| [H-002](pilot/H-002/shadowing.json) | 22 | 5 | 16/16 | 20 | 3 |
| [H-004](pilot/H-004/shadowing.json) | 21 | 4 | 15/15 | 21 | 4 |
| [H-020](pilot/H-020/shadowing.json) | 24 | 5 | 20/20 | 22 | 2 |

**Sơ.** Các bài có 20–24 câu. Người học mở bằng một yêu cầu ngắn, sau đó đổi chi tiết hoặc hỏi lại. Trong S-003, 「もう一度言ってください。」 được phát triển thành 「料理の名前だけもう一度言ってください。」 để người nghe biết chính xác phần cần nhắc lại.

**Trung.** Các bài có 19–24 câu. Số câu thay đổi theo số việc cần tập. Trong T-008, người nghe có thể từ chối lời đề nghị giúp mà vẫn thấy thoải mái. Trong T-044, học viên phải làm rõ được món đồ, địa chỉ, điều kiện dịch vụ và việc cần bưu cục kiểm tra.

**Thượng.** Các bài có 21–24 câu. H-002 tập phân biệt một đề xuất với cam kết đã đưa cho khách, H-004 phân biệt xem xét với đồng ý, H-020 chất vấn căn cứ của số liệu mà vẫn duy trì hợp tác. Những câu ngắn vẫn có chỗ ở đầu bài.

## Kiểm tra và điểm cần nghe lại

Đã kiểm tra từng gói xuất có một node shadowing. Cả 199 mục đều có đúng một người nói, một lượt nói, giọng `male` hoặc `female`, cùng hai trường `ja` và `vi`. Đối chiếu 199 mã và cặp Nhật–Việt trong preview theo đúng thứ tự JSON. Đối chiếu bản Nhật nguyên văn với V11 và shadowing cũ cùng chặng cho kết quả 0 câu trùng. Các câu cùng mẫu nhưng khác mục đích vẫn được giữ để luyện lại.

- **S-003.** Khi có âm thanh Harumii, nghe thử câu 009 để xác nhận TTS đọc 角 là かど trong ngữ cảnh chỉ đường.
- **H-004.** Câu 017–019 cùng luyện tự sửa cách xưng hô hoặc người liên hệ. Mỗi câu có cách nói đúng, nhưng ba lượt liền nhau hơi dồn. Khi duyệt để phát hành, cân nhắc giữ hai lượt hoặc đặt cách nhau.
- **T-002.** Câu 002 dùng 持っていきましょうか để ngỏ ý mang đồ. Bản Việt “tôi có cần mang gì theo không” nghiêng về hỏi yêu cầu của chủ nhà. Khi duyệt phát hành, cân nhắc cách nói “Hay là để tôi mang chút gì sang dùng cùng trà nhé?”

Chín bản có thể dùng để duyệt nội dung và nhịp của bài. Ước lượng độ dài dựa trên việc đọc văn bản. Thời lượng audio và cách TTS phát âm thực tế cần được nghe khi Harumii gắn giọng. Preview riêng cho V13 đọc từ gói đã xuất, thuận tiện mở trên máy trong lúc các chat khác tiếp tục làm V12.
