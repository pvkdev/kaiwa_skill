---
name: jlpt-listening
description: Khôi phục script tiếng Nhật và mốc nghe mondai, nhóm, câu trên một audio tổng JLPT bằng dữ liệu SingleFile hoặc Groq Whisper Turbo. Dùng khi chuẩn bị phần choukai cho migration Harumi.
---

# Script và mốc nghe JLPT

Chạy ở gốc kho `JLPT/`. Đọc [hợp đồng audio](../../../contracts/v1/CONTRACT.md) để ghi dữ liệu đúng UUID, đúng đơn vị và đúng nguồn. Audio phát trên Harumi luôn là một bản thu hoàn chỉnh. Các mảnh FLAC chỉ phục vụ nhận dạng.

## Xác định phần việc của một đề

1. Đọc HTML nghe mới nhất đúng kỳ và MP3 tương ứng. Đối chiếu `data-start`, `data-end`, script, phụ lục, câu có hình và các câu dùng chung một đoạn. Mốc nguồn tính bằng giây thì đổi sang mili giây đúng một lần. Đồng hồ cục bộ của một player ghi 00:00 không xác định được vị trí trong đề. Đối chiếu thời lượng bằng ffprobe. Khi đổi bản thu/RSS, đối chiếu nếu cùng MP3 (SHA-256), hoặc thử tín hiệu đầu, giữa, cuối trên enclosure. Bản thêm quảng cáo/intro có thể lệch dù cùng tên.
2. Chạy `py -3 tools/align_listening.py packages/N3/2018-12/package.json` (thay kỳ thật). Lệnh **không gọi API**. File xuất nằm ở `work/stt/<packageId>/alignment-review.json`. Đọc `rows[].number`, UUID, `role`, `sourceCues`, `hasScript` và `needs`. Nếu nguồn đã có đủ bằng chứng, dùng trực tiếp. Chỉ chạy STT khi cần khôi phục script hoặc biên mốc chưa có nguồn. Trước khi gửi track lớn, xem có bản supplement/script đúng kỳ tại chỗ hay chưa.

## STT có thể chạy tiếp

```powershell
py -3 tools/listening_stt.py "N3/1812/JLPT-N3-2018-12.mp3" --max-chunks 1
py -3 tools/listening_stt.py "N3/1812/JLPT-N3-2018-12.mp3"
py -3 tools/align_listening.py packages/N3/2018-12/package.json --timeline "<đường dẫn timeline.json đã in>"
```

- Cần Python 3.11+, `requests`, ffmpeg và ffprobe trên PATH. Key lấy từ `GROQ_API_KEY`, kế đến `D:/JLPT/groq/groq_api_key.txt`. Có thể truyền đường dẫn bằng `--key-file`. Giữ key ngoài repo và ngoài log.
- Mỗi lần gửi tối đa 300 giây FLAC mono 16 kHz, tuần tự, tiếng Nhật, model `whisper-large-v3-turbo`, `verbose_json` với cả `word` và `segment`. Raw trả về chỉ lưu sau khi đã kiểm timestamps. `--max-chunks` giới hạn số mảnh **mới** mỗi lượt. Hạn mức dài, HTTP lỗi hoặc mất kết nối thì chạy lại cùng lệnh sau khi điều kiện đã phục hồi. Cache khóa theo SHA của toàn audio, model, ngôn ngữ và cách chia. [Groq Speech to Text](https://console.groq.com/docs/speech-to-text)
- `timeline.json` có `words` và `segments` trên đồng hồ tổng. `masterMs = chunkStartMs + round(localSeconds * 1000)`. Câu nối qua biên 5 phút có thể bị ngắt tiếng ở hai phía. Đọc segment hai phía, nghe lại vài giây trước/sau, dùng word timestamps để khôi phục câu. Sửa tại biên tập riêng và giữ raw để đối chiếu.

## Giao kết quả để import

1. Công cụ align giữ nguyên từng cue hiện có của nguồn. Khi cần suy biên, nó dùng trình tự thông báo đầy đủ trong cùng mondai hoặc neo hai đầu script qua chuỗi words. Biên cuối lấy tới thông báo kế tiếp có thể bao gồm im lặng, phần kết hoặc cả hướng dẫn. Mọi `timelineCandidate` đều cần nghe kiểm. Với mốc ứng viên không duy nhất, rà theo lời mở đầu, câu lệnh, hai từ neo, mốc của câu kề, track tổng và bản ghi đầy đủ. Với script thiếu, `scriptJaCandidate` lấy từ segment trong khoảng, dùng word ở biên. Đối chiếu từ đồng âm, tên, số tiền/ngày giờ, phủ định, người nói, câu hỏi lặp; sửa script theo âm nghe được. Nếu chưa có cả audio lẫn script, ghi việc admin cần cung cấp theo kỳ/mondai/câu.
2. Trong bản sửa gói, đối chiếu `packageSha256`, `revision` và `audioSha256` một lần nữa. Với bằng chứng STT cần cho bản đã duyệt, lưu phần trích raw, ID chunk, biên tổng cụ thể, SHA-256 master, word/segment tham chiếu và quyết định người rà vào JSON bổ sung bên cạnh gói (đường dẫn tương đối, hash bytes qua `sources[]`). Raw tạm trong `work/stt/` có thể tái dùng tại máy đó. Bản import phải kiểm được cả khi di chuyển repo sang máy mới.
3. Ghi cue bằng `annotations.audioSegments`: `role:mondai` với mảng `questionIds` rỗng, `question` một UUID, `shared` nhiều UUID. Biên [startMs,endMs) trên master. Cặp mốc chung nhiều câu giữ ở role shared. Mỗi câu chỉ nhận cue riêng khi có bằng chứng về biên riêng; vẫn có thể luyện với đoạn chung khi chưa xác định được biên riêng. Khi dùng khoảng từ câu đầu tới cuối làm phạm vi luyện mondai, ghi rõ locator là bao các câu và giữ cue hướng dẫn nếu nguồn có. Bằng chứng chỉ có start thì giữ `endMs:null`.
4. Script riêng ghi `question.jlptListenScript.scriptJaMd`. Script dùng chung ghi `block.mediaItems[].audio.scriptJaMd` đúng nhóm. Giữ script nguồn nguyên văn. Với script phục hồi từ âm thanh ghi annotation `origin:stt`, SHA master/đầu vào, source ID, model, runId, locator bằng chứng và trạng thái review. Với từng câu/lượt lời, chuyển cho người biên tập để điền cặp JA/VI trên ID chủ sở hữu và ghép `scriptViMd` đúng quy tắc. Khi nguồn sẵn script mà thiếu bản dịch, dùng script ấy để dịch.
5. Giữ lại UUID khi tăng revision. Sau **mỗi lần** sửa hoặc ghép script/cue vào gói, chạy [jlpt-exam-review](../jlpt-exam-review/SKILL.md) trên package cuối: rà từng UUID câu/nhóm/media, nghe đầu/cuối mọi cue trên master đúng hash, đối chiếu script, cặp JA/VI và nguồn timing. Chạy validator của hợp đồng và checklist; ghi checkpoint với revision/SHA-256 bytes package, phạm vi đã/chưa rà và mọi issue theo UUID/locator. Chưa rà hết thì giữ draft, không duyệt release. Những việc tự xác minh được bằng MP3/snapshot là việc biên tập; chỉ yêu cầu admin bổ sung đúng hiện vật thật sự thiếu.
