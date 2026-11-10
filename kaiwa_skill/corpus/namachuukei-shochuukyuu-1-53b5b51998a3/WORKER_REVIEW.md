# Rà mở rộng furigana p0024–p0040

- Worker: `production_book_05_resume`; nguồn PDF SHA-256 `53b5b51998a3d426fcdbd24e3fe029ed62823255a3de9a431caf50fc33e703d8`.
- Đã mở ảnh toàn trang riêng từng p0024–p0040, so lại danh sách furigana theo lần xuất hiện và thứ tự các vùng nguồn. Crop riêng các hàng bài nghe p0035, bài tập p0037 và nhãn nhân vật p0038; coordinator cũng báo crop reminder p0034. Cache ảnh chỉ để rà, không thuộc sản phẩm text.
- Giữ nguyên bytes p0024–p0025, p0027–p0030, p0032–p0033, p0040: không thấy sai khác mới trong lượt rà. Các trang này vẫn verified theo evidence cũ.
- p0026 và p0034: bỏ `一度／聞` lần 2 trong lời nhắc `もう一度聞きましょう`; chỉ lần đầu có ruby in. Record và reverify.
- p0035: crop các hàng ①–④ xác nhận ruby lặp không in. Hàng ① bỏ `韓国` lần 2, `韓国語`, `通` lần 2; hàng ② bỏ `高木` lần 2 và ba `行` sau lần đầu; hàng ③ bỏ `初／何度／行`; hàng ④ bỏ `行`. Giữ các map có chữ in. Record và reverify.
- p0031: crop `領収書` xác nhận nguồn in `りょうしゅうしょ`; sửa ký tự `ょ` cuối bị thiếu. Record và reverify.
- p0036: crop dictation xác nhận `乗` lần 2 không in ruby; crop point instruction xác nhận `話＝はなし` và chỉ `楽` ở (a) có ruby. Sửa cả ba, record và reverify.
- p0037: hàng ④ `友人` không có ruby, bỏ map lần 2. Sau kiểm chéo của coordinator, crop formal xác nhận dòng `あんなにすばらしい景色を見たのは、初めてでしたよ。` chỉ `見` có ruby, nên bỏ `景色／初`; crop bài tập xác nhận hàng ① `人が少ない` không in ruby `人`, hàng ③ `日本らしい` không in ruby `日本`. Record và reverify. p0038: nhãn ② `友人` không có ruby, bỏ map lần 2; record và reverify.
- p0039: crop option f xác nhận `言葉` không in ruby, chỉ `通` có `つう`; bỏ map `言葉` ở option f, giữ map trong prompt đầu. Record và reverify.

Hash Markdown sau lượt rà, lấy từ checkpoint hiện tại:

```text
p0024 ed17e4ec8de93dc75b64f524d768b1fc88ff547bacd3851de722a3455634e7ae
p0025 87640e6e7693895d8c42ff4fe3edd1125f38b2a5ca65a9a862ea0d6fc34305cd
p0026 e5a1b10a9201d93e31bf4f8d8511129313db543441997d4aa1ab51e93ec62d35
p0027 a7da4074afe311d96b13f9ff8e56fcd464cd3c10481269c6d1ec40ad2427d757
p0028 9f9f0cc6b87959fe02b058ada48803f009d6570676ff38410086ea34c0b75c36
p0029 efc0deb9a533569e1d6ca083fb5fef3297ff21c5caf57e1a1ec56232e64e55e6
p0030 6c28cfd9222e80a4638fd9de9df6bd3765d7d67ece84db6a89aa39d30c99194e
p0031 42a91870d5fd5f66dfbd993c082b1c6597ac997cdba271530246875379320128
p0032 3d306d7de26758e2801990abd91ad34d6db2de585946e2a626393071ba41a6e3
p0033 1cabfed60ad913646b15964116f2405432b43aed4dab522db1492981b29c3628
p0034 3ce3c5f43920546795814accdf7e3e0e4adbb3df91cfce8954246ff75e6fcf39
p0035 8c197921ed41e3ffe39c37b691cd74d47f374c31d3cb1a13ba9bdcaa528c9d40
p0036 5814e1c1a23635ec3918d2fb87e34c0ce5cb7ac9b340bc96a95118cab76ac4c0
p0037 8e0e4646c601c5b689e328ca99de6cc1ff39dc2aa0225a92f2c74141beefa38f
p0038 26b5ee12191c913b0b3c3f6572acaddcb7016d17b341618d3fbba0ae1b0d9a72
p0039 be905289f5b4a27c88fc628cbb981b42f82ab01901ad99edb02e20b2437d2926
p0040 9e9c66961eb99ec93e8d944511701443dce4c5039307b951d03dd9cc25f861ec
```

## Rà mở rộng furigana p0041–p0055

- Worker `production_book_05_resume` đã mở lại toàn trang và các crop chữ Nhật cỡ nhỏ p0041–p0055, so từng map furigana với đúng lần xuất hiện và span in; giữ bytes các trang không phát hiện khác biệt. Các ảnh crop nằm ở `.cache/work/production_book_05/`; coordinator kiểm độc lập một số trang và cung cấp crop chặt khi cần.
- p0043: option ③b chỉ `上＝じょう`, không phủ `級用`; sửa và reverify. p0046: panel trang trọng cuối không in ruby trên `気`, bỏ map `気＝き` ở panel này; panel thân mật vẫn có, giữ. Reverify.
- p0052: bảng sáu hàng không có header trong nguồn; xóa hai nhãn header đã thêm, giữ ba ô header trống để biểu diễn bảng Markdown. Reverify.
- p0054: bubble ① chỉ chữ `月` trong `9月` có `がつ`, sửa span; bubble ④ `病院＝びょういん`, sửa thiếu `ん`. Reverify.
- p0055: bài 2 hàng ④ `月曜` trong dòng `店員` có `げつよう`, bổ sung; lần `月曜` dòng `店長` không có ruby. Reverify.
- p0041–p0042, p0044–p0045, p0047–p0051, p0053: lượt rà không phát hiện sai khác mới. Các trang đã verified trước đó giữ nguyên.

Hash Markdown sau rà:

```text
p0041 cd77ce8aaac86578b249f11f30272a55cdf5f3aaf79e59af6ab19e92710fa278
p0042 2af957cdf4140f4be2d8944581f198c54229e796888f23ecfed8ab7a4fe994a2
p0043 2c2e47a4332a26f35a72415da4756ee925dd38ea0ccf9286ca2364664a57b35b
p0044 0a38d6ca2b4fdd460f5a3560648f85c46949038b5cda8b79c09c6313cb368cc4
p0045 f3eecd78e944f38bb5144e753bfecf455089deab52099985415e0f7a8648a563
p0046 af8fe539ad6f9159a496416daf048df3ad0a81269dddf2c88084f6a59109df6f
p0047 913cb8b9b4372ef01b737f572e3424d08ef9cf7076dba4436a07040487146720
p0048 675d5d0182b00544ef536a1dbc411873fdf69af19ee2afabf2880c2afcc51b69
p0049 e9f1a6d6675d165881d06736c7c094984076bbc528b71dabb774a12bd41e853b
p0050 55799f3819812983ca969b6a38d2e4be65392ea185858cea54acd2e3de6567ea
p0051 c5d78f3e342587cf181b19c2a2538a8886fe2cb6d3d605ada2c64a80cbd0e3a3
p0052 553549d5c57d31aa252e722a139dcc754e95fc62d91f79d5bc4f7066225beb0b
p0053 d4dadba412d40738af6dd4fdb36c8b328d9966175e855249da0d822e4ecc0843
p0054 800abcdff9b267590ea212af68b112e940f1ae2229a8dc4c2b153c021d75df18
p0055 c3fc32e4000b5ade73b76485ed6d3dabc8002fe18792a88d93130dec231d2484
```
