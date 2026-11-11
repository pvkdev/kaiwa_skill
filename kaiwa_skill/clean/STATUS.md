# Clean hàng loạt — đang điều phối

Đã nghiệm thu **28/30 PDF, 4.144/4.597 trang đầu vào**. Bảy bản đầu được rà độc lập toàn phạm vi;21bản sau writer rà toàn nguồn và root QA mẫu. [Thư viện bản đọc](../knowledge/README.md). Phạm vi đủ không chứng nhận mọi chữ nguồn hoàn hảo; vấn đề nguồn được giữ và khoanh rõ.

Bản vừa chốt: **気持ちが伝わる 日本語会話 基本表現180**, commit7f22d1d.209trang/24chương/201unit;180biểuđạt,90Unit theo cặp,360hoạtđộng,50Hints,189khóaEnglish và180khóaJapaneseromaji. Root43ảnh nguồn, gồm toànintro/guide và cả8trangindex; main chỉ QA mẫu. Bảyref sai đã có sốin+vịtrí/link đúng. Bốn trang168/187/204/206 còn nhãnA/A hoặc khóaMasani không khớp đầu mục; validate0lỗi/8cảnhbáo cùng4vấnđề. BookSHA8211e098a36f3ee17c876abd9188effa2f73c53a797ba24f70ca8202d0d68641.

Còn hai sách đang viết, đều **gpt-6-sol/high**:

- /root/clean_keigo: **すぐに使える 日本語会話 超ミニフレーズ 発展210**,233trang. Main đã đến mục108/PDF123; TOC4–9 còn draft để ghi đủ210khóa. Root17ảnh nguồn, toàn10mục đầu vàmục60; lỗi chữいや đã sửa. Source75 giữA/A vàcảnhbáohẹp. Audio dùng chung mã giữa các head, không suy từ số mục.
- /root/clean_namachuukei_sho: **日本人がよく使う 日本語会話 オノマトペ基本表現180**,220trang. Đã xong front/intro/Part1/Part2, Part3 quaPDF111; Part3 vẫn draft đến khi đủ163. Root31ảnh nguồn,so toànfront+intro và6headmẫu Part1. Sửa nghĩa/ngoạingữ/ghi chú sản xuất đã đọc lại.185slot trong4Part có từlặp, không ép sốslot thành180.

Worker thứba /root/clean_namachuukei_chu đang **QA chỉ đọc** index210–216 của cuốn onomatopoeia, chỉ ghi cache. Trước đó đã độc lập mở210crop audio của cuốn210:210occurrences,198mã disc-track,12cặp head dùng chung,khôngmờ; đây chỉ là QAicon, khôngrà nghĩa210trang. Root đã kiểm hashreportfe3f28b86dc17164136c0dcd1ed2c984bc42ea72552be8a0b8d80933e27ff161. Một sách mộtwriter; không ghi chồng.

Đã kiểm danh sách thực:30PDF trongbook/vocab khớp đủ30nguồn/4597trang củaqueue,khôngthiếu hoặcngoàiqueue. MọiPDFđãgiao. Ba worker được khôi phục sauquota theo yêu cầu, đều sol/high; worker medium khôngchạy.

Công cụ0.4.10:80testfork+17directPASS; regression18bản trước0lỗi/33cảnhbáo,10bản mới đượcvalidate riêng. Skilldocs6ca79cb bổsung đốichiếu keyindex thay vì join sốtrang và khôngcắtgiữacâu Việt; codekhôngđổi,khônglặptestkhôngcầnthiết.

[CD,băng và nguồn nghe](../knowledge/AUDIO_INDEX.md) ghi thông tin thực in; filethật not_checked,chưa tìm/tải audio. [COORDINATOR](COORDINATOR.json) và[HANDOFF](HANDOFF.md) giữ tiến độ để nối saugiánđoạn. Dùngcheckpoint thật thay sốsnapshot. Tiếp điều phối tới30PDF; không códaemon khiđóng ứngdụng.
