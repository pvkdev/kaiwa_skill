# Xem lộ trình trên GitHub Pages

Trang xuất bản là `docs/index.html`, gồm giao diện và toàn bộ dữ liệu cần đọc. Có thể mở trực tiếp file hoặc xem qua GitHub Pages.

1. Push nhánh `main` lên `origin`.
2. Mở repo `pvkdev/kaiwa_skill`, chọn **Settings → Pages**.
3. Trong **Build and deployment**, chọn **Source → Deploy from a branch**.
4. Chọn **Branch → main**, thư mục **/docs**, rồi **Save**.
5. Chờ tác vụ Pages trong **Actions** hoàn tất. Mở `https://pvkdev.github.io/kaiwa_skill/`.

Hướng dẫn xuất bản theo [GitHub Docs](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Bản hiện tại đã được commit ở máy. Để đưa lên GitHub, chạy từ thư mục repo:

```powershell
git push -u origin main
```

Sau khi thay đổi lộ trình và xuất lại JSON, chạy bộ dựng trang trước khi commit và push:

```powershell
py -X utf8 tools/build_review_site.py
git add docs/index.html docs/.nojekyll
git commit -m "Update Kaiwa review site"
git push
```

Bộ dựng đọc `CURRENT_ROADMAP.json` và xác minh các bản Markdown theo manifest. GitHub chỉ phục vụ thư mục docs đã dựng sẵn. Trang ghi nhớ theme, bộ lọc và chặng gần nhất trên trình duyệt đang dùng.
