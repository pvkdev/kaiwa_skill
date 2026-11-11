# Rà soát độc lập pilot

Ngày: 2026-11-11. Phạm vi rà mẫu: PDF trang vật lý 9–12 (trang in 16, 18–23), các đơn vị `u-intro-05`, `u-part1-01`, `u-part1-02`, `u-part1-03`. Tôi đã **mở ảnh toàn trang** `kaiwa_skill/.cache/fork-pilot/page-09.png` đến `page-12.png`, đối chiếu các đoạn dưới đây với PDF, raw Markdown trang tương ứng và bốn chapter. PDF nguồn có SHA-256 `4f47df1cc97a4b27ba61d05850633ea73466e48c03a20b48e927f351435f3256`.

| PDF / unit | Đoạn đã đối chiếu | Kết quả |
| --- | --- | --- |
| 9 / `u-intro-05` | Các cặp biến âm, nhất là `来てはだめ→来ちゃだめ`, `日本では→日本じゃ`, `飲んでしまう→飲んじゃう`; raw `p0009-b005`. | Khớp ảnh. Sách in công thức `～では→～ちゃ` trái với ví dụ cùng dòng; chapter giữ ví dụ, bỏ công thức và editorial log ghi rõ. Không thấy lỗi mới. |
| 10 / `u-part1-01` | Hội thoại donut; các ví dụ nhóm A/B/C và sắc thái `ね`, gồm `もう３個食べちゃったよ`, lời nhắc `野菜もちゃんと食べてね`; raw `p0010-b001`, `p0010-b005`–`b007`. | Câu Nhật và bản Việt ở các đoạn rà giữ đúng tình huống/sắc thái; không thấy lỗi mới. |
| 11 / `u-part1-02` | Hội thoại mở đầu, ví dụ mượn bút, `もう帰ろう`, cảnh báo `触っちゃだめだよ`, MEMO 4 về giọng lên; raw `p0011-b001`, `p0011-b005`, `p0011-b006`. | Câu Nhật và MEMO khớp ảnh; bản dịch không làm đổi ý chính ở các đoạn rà. Không thấy lỗi mới. |
| 12 / `u-part1-03` | Hội thoại lễ hội, ví dụ `３万円だって`, `いやになるね`, MEMO 8 về `いやんなる`; raw `p0012-b001`, `p0012-b005`, `p0012-b006`. | Câu Nhật, bản Việt và MEMO khớp ảnh ở các đoạn rà. Không thấy lỗi mới. |

Ảnh đã mở (SHA-256): PDF 9 `f547639c52cca5d469943cc7b309c0b2bc4f5fe2fbe43faf8506b6517ffc71ab`; PDF 10 `99cdced4f6e493ff415ca0b999e97cf094c6d2661ca4d0343bcb25412056bb3c`; PDF 11 `a845592fed2b51475e87825dade51f1166c5e55005013c677b5e17aecbf0f0c4`; PDF 12 `636432e95ee45166769179fbe1de3f92f3382057a198005663df635b05be053a`.

Raw Markdown đã dùng (SHA-256): p0009 `5a828c66eb5b091267e3dc02d0ce89b821a351145973e613dedc7f0a80f4f922`; p0010 `6c360a3976aff32a73cece7812b951e8a762827e90f33615fb214dda92ee2b29`; p0011 `f60cb821171158015c1020b56df0fd37e3f6ac798f51c8b63419c7a93ee3f2a7`; p0012 `ab795fd019fa93cdde375ba7e5caee38a55c683686b66b90ca4ae8ea22abdd06`.

Chapter đã đọc (SHA-256): `00-mo-dau.md` `b9e11367e4db8fb0439cc85f217ebd3eff738b66944a0264e5ec5a6859a99ca2`; `01-ne.md` `c321941e2fa3fb6791257ab37bcaa7480f5ecdccca7e36ee25622c237017f612`; `02-yo.md` `1174ea56a076ba04d7a9ba11933be1fffa1f9fad96e6a751d1a723637c2d078a`; `03-yone.md` `71b282f7b326b43d4daf13e542eae98176db5041aa26821643bca147bb0374f0`.

`validate_fork.py` trên bản build hiện tại: **0 lỗi, 0 cảnh báo**. Kết luận này chỉ xác nhận các đoạn đã rà và cấu trúc được script kiểm; không nâng trạng thái của toàn bộ PDF 7–12 hoặc các trang ngoài pilot. Nếu chapter/raw/PDF đổi byte, cần rà lại phần liên quan.
