# Git và phiên bản

- Skill version trong VERSION; thay đổi hành vi ghi CHANGELOG.md.
- `.gitattributes` giữ nguyên byte trong corpus để Git checkout trên Windows không đổi LF/CRLF và làm sai hash bằng chứng. Không tự normalize corpus đã verified.
- Chỉ coordinator commit, tuần tự. Worker không dùng git add/commit.
- Trước commit: git status --short, staged diff và validator; stage đường dẫn cụ thể. Không chứa bunpou, source PDF mới ngoài yêu cầu, cache ảnh tái tạo, lock hay file tạm.
- Skill và output là các commit riêng. Ví dụ `feat(skill): add resumable page-verified PDF ingestion`; `data(pilot): verify selected pages of BOOK_ID`; `data(book): complete BOOK_ID`.
- Output gồm manifest, Markdown trang, review/checkpoint bền vững, assets được tham chiếu, bản ghép và chỉ mục. Ảnh nguồn QA cần giữ hoặc có khả năng render lại với hash, phiên bản render và tham số ghi rõ; không tuyên bố verified nếu asset bắt buộc chưa có.
- Checkpoint trên đĩa ngay mỗi trang. Commit output sau từng đơn vị nghiệm thu (pilot hoặc sách). Khi phải dừng một sách dài, có thể commit WIP với số trang đã đạt, không dùng thông điệp completed.
- Sau commit ghi hash commit vào báo cáo phiên; không sửa file để tự chứa hash của chính commit đó.
- Commit local là mặc định. Push remote chỉ khi người dùng yêu cầu rõ.
