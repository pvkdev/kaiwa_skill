# Ghi chú biên tập – N1_ずには・ないではすまない_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜ずにはすまない／ないではすまない – Không làm thì không xong
- Cấp độ: N1
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜ずにはすまない／ないではすまない – Không làm thì không xong
- Các dòng cấu trúc trong bài gốc, chuẩn hóa và gán thẻ: 1: Vない bỏ ない ＋ ずにはすまない; 2: Vない ＋ ではすまない; 3: Vない bỏ ない ＋ ずにはすむまい.
- Các cách dùng và cách nói thường gặp: Không làm thì không giải quyết ổn thỏa.
- Bảng phủ được lập trước khi viết Kịch bản; chọn ví dụ theo thứ tự gốc trong từng chương, [MỚI] đặt cuối.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Không làm thì không giải quyết ổn thỏa | 4 | 3 | 1 | 4 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu 2 |
| 2 | 3.1 | 2 | Bài gốc câu 3 |
| 3 | 3.1 | 3 | Bài gốc câu 4 |
| 4 | 3.1 | 2 | MỚI – câu gốc 1 nhầm mẫu いられない được lược |

## 2. Lỗi đã tự sửa trong bài gốc

- Câu 1 dùng mẫu いられない được lược, không coi câu Nhật đó tự thân là sai và không thay đuôi. Câu mới khác tình huống bù tối thiểu. Không phát hiện lỗi cần sửa trong ba câu gốc được chọn.
- Bản dịch giữ だろう、と思います、でしょう、まい là sắc thái nhận định/dự đoán.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | マスコミに知られてしまった以上、事実を公表せずにはすまないと思います。 | Bài gốc câu 2 |
| Chọn | 多くの人に期待されているので、彼としてもその仕事を引き受けないではすまないでしょう。 | Bài gốc câu 3 |
| Chọn | これほど不祥事が続いては、管理職も責任を取らずにはすむまい。 | Bài gốc câu 4 |
| MỚI | 会社に迷惑をかけた以上、謝らないではすまない。 | MỚI – câu gốc 1 nhầm mẫu いられない được lược |
| Lược | 実際に損害を与えたのだから、弁償しないではいられないだろう。 | Ngoài tập chọn; ưu tiên dạng khác và tình huống không trùng |

## 4. Quyết định đã tự đưa ra

- Đổi Đức thành Hạnh, giữ học sinh, tai nghe, khách và bến xe.
- Lược câu 1 vì dùng いられない, vốn có thể đúng khi nói thôi thúc nhưng không minh họa mẫu nghĩa vụ của bài. Không sửa đuôi để ép ví dụ vào mẫu; thêm một câu mới khác tình huống ở cuối.
- Giữ すむまい ở câu 4 như biến thể dự đoán phủ định, không sửa sai thành dạng khác.
- Nhân vật Việt chỉ dùng một tên gọi ngắn, không thêm họ hoặc tên đệm theo yêu cầu người dùng.

- Rà soát mở màn 7.2.0: Việc làm hỏng hộp tạo trách nhiệm xin lỗi cụ thể; hành động sửa sai xuất phát hoàn cảnh chứ không phải cảm xúc tự bật ra. Giữ nguyên câu Nhật, bản dịch và toàn bộ ví dụ; chỉ dẫn ngoại hình không liên quan được bỏ khỏi lời kể.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã đối chiếu 4 câu ví dụ với bài gốc, kiểm cách chia, nghĩa, thứ tự và phần tô màu; đã soát câu mẫu, bẫy và câu kết.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.

- Tự thẩm định mở màn 7.2.0: đã đối chiếu động cơ, diễn biến, sắc thái mẫu, phần giới thiệu và câu kết; lời kể tự nhiên khi đọc thành tiếng.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
