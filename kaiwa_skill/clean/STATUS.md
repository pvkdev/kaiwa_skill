# Clean hàng loạt — kiểm tra cuốn cuối

Đã nghiệm thu **29/30 PDF, 4.364/4.597 trang nguồn**. Bảy bản đầu được rà độc lập toàn phạm vi; các bản sau được worker đối chiếu toàn nguồn và root QA mẫu. Xem [thư viện](../knowledge/README.md) và hồ sơ nghiệm thu riêng từng sách.

Cuốn áp chót **日本人がよく使う 日本語会話 オノマトペ基本表現180** đã chốt ở commit `38c623b`: 220 trang, 185 đầu mục theo bốn phần, 370 hoạt động, 365 dòng chỉ mục. Root QA 37 trang nguồn; reviewer độc lập kiểm toàn chỉ mục/audio và 15 mục mẫu. PDF38 vẫn giữ vấn đề mã audio nguồn in trùng1; validator 0 lỗi/2 cảnh báo đúng vấn đề này.

Cuốn cuối **すぐに使える 日本語会話 超ミニフレーズ 発展210** đã viết đủ 233 trang. Có 210 đầu mục/926 tình huống; 16 cảnh cuối từng thiếu đã phục hồi, kiểm đếm độc lập và đối chiếu Nhật–Việt lại. Bốn lỗi trong phần phục hồi đã sửa/readback. Chỉ mục 320 dòng đang được reviewer đối chiếu từng dòng trước release. PDF75/207 giữ vấn đề vai A/A trong nguồn.

Ba sub đều `gpt-6-sol/high`: keigo tác giả cuốn210; sho QA chỉ mục; chu đã hoàn thành QA 16 cảnh. Các worker medium vẫn dừng. Root giữ Git và nghiệm thu; một sách một writer. Có checkpoint để khôi phục, không chạy lại phần đã kiểm còn hợp lệ.

Kiểm đếm bổ sung cuốn200: 995/995 tình huống, toàn 200 mục, không lệch số lượng; commit audit `746b475`. Đây không phải rà nghĩa độc lập toàn sách.

Công cụ sửa navigation ở `40eb2c2`, 82 test fork và17 direct PASS; root chạy riêng hai regression navigation PASS. Hai bản125/Feel180 được rebuild chỉ liên kết ở `617d903`; các chapter/units/search/evidence/audio không đổi. Manifest [NAVIGATION_REBUILD.json](NAVIGATION_REBUILD.json).

[Thông tin CD và nguồn nghe](../knowledge/AUDIO_INDEX.md) giữ thông tin in trong sách; chưa kiểm file âm thanh thực tế. Queue khớp đúng 30 PDF/4.597 trang trên đĩa. Tiếp kiểm tra và chốt tới hết phạm vi.
