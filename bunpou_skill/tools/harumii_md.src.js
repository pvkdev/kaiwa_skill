(async () => {
  const say = (m) => alert('Harumii → Markdown\n\n' + m);
  try {
    // 1) id mẫu ngữ pháp lấy từ URL: /admin/grammar-pool/<level>/<id>
    const m = location.pathname.match(/\/grammar-pool\/[^/]+\/([0-9a-f]{8}-[0-9a-f-]{27})/i);
    if (!m) return say('Hãy mở trang xem một mẫu ngữ pháp\n(…/admin/grammar-pool/n3/<id>?mode=view) rồi bấm lại.');
    const id = m[1];

    // 2) Địa chỉ API: tìm trong các request mà trang đã gọi (NEXT_PUBLIC_API_URL được build sẵn vào FE)
    let base = null;
    const urls = performance.getEntriesByType('resource').map((e) => e.name);
    for (const key of ['/api/learning/', '/api/identity/', '/api/']) {
      const u = urls.find((x) => x.includes(key));
      if (u) { base = u.slice(0, u.indexOf('/api/')); break; }
    }
    if (!base) {
      try { base = localStorage.getItem('harumii_md_api'); } catch (e) {}
    }
    if (!base) {
      base = (prompt('Không tự dò được địa chỉ API.\nNhập địa chỉ backend (vd https://api.xxx.com):') || '').trim().replace(/\/$/, '');
      if (!base) return;
      try { localStorage.setItem('harumii_md_api', base); } catch (e) {}
    }

    // 3) Access token (giống apiFetch của app: hết hạn thì refresh)
    const expired = (t) => {
      try { return JSON.parse(atob(t.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'))).exp * 1000 <= Date.now() + 30000; }
      catch (e) { return true; }
    };
    let token = localStorage.getItem('accessToken');
    const refresh = async () => {
      const rt = localStorage.getItem('refreshToken');
      if (!rt) return null;
      const r = await fetch(base + '/api/identity/auth/refresh', {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ refreshToken: rt }),
      });
      if (!r.ok) return null;
      const d = await r.json();
      localStorage.setItem('accessToken', d.accessToken);
      localStorage.setItem('refreshToken', d.refreshToken);
      return d.accessToken;
    };
    if (!token || expired(token)) token = await refresh();
    if (!token) return say('Chưa đăng nhập hoặc phiên đã hết hạn. Hãy đăng nhập lại rồi bấm lại.');

    // 4) Lấy mẫu ngữ pháp
    const url = base + '/api/learning/admin/grammar-pool/' + id;
    let res = await fetch(url, { headers: { Authorization: 'Bearer ' + token } });
    if (res.status === 401) {
      token = await refresh();
      if (token) res = await fetch(url, { headers: { Authorization: 'Bearer ' + token } });
    }
    if (!res.ok) return say('API trả lỗi ' + res.status + ' ' + res.statusText);
    const d = await res.json();

    // 5) Nội dung = đúng thứ trang đang hiển thị: explanation, rỗng thì rawContent
    const md = ((d.explanation || '').trim() || (d.rawContent || '').trim());
    if (!md) return say('Mẫu này không có nội dung markdown.');

    // 5b) ĐỐI CHIẾU với nội dung trang đang hiển thị (trang có thể render từ explanationHtml thay vì markdown).
    //     So chữ/số thuần (bỏ ký hiệu markdown, thẻ HTML, furigana) của markdown với của bài giảng trên trang.
    const art = document.querySelector('article.grammar-markdown');
    if (!art) return say('Chưa thấy phần bài giảng trên trang (trang chưa tải xong?). Đợi trang hiện đủ rồi bấm lại.');
    const clone = art.cloneNode(true);
    clone.querySelectorAll('rt,rp').forEach((n) => n.remove());
    const norm = (s) => s.replace(/<[^>]*>/g, '').replace(/&[a-z#0-9]+;/gi, '').replace(/[^\p{L}\p{N}]+/gu, '');
    const a1 = norm(md), a2 = norm(clone.textContent || '');
    if (a1 !== a2) {
      let i = 0;
      while (i < a1.length && i < a2.length && a1[i] === a2[i]) i++;
      const ok = confirm('CẢNH BÁO: markdown từ API KHÁC nội dung đang hiển thị trên trang.\n\n' +
        'Độ dài chữ: markdown ' + a1.length + ' / trang ' + a2.length + '\n' +
        'Bắt đầu lệch tại ký tự #' + i + ':\n  markdown: …' + a1.slice(Math.max(0, i - 10), i + 25) + '\n  trang:    …' + a2.slice(Math.max(0, i - 10), i + 25) +
        '\n\nOK = vẫn tải file markdown, Cancel = không tải.');
      if (!ok) return;
    }

    // 6) Tên file: bỏ ~ ～ 〜, "/" "／" → "・", giữ nguyên tiếng Nhật; bỏ ký tự Windows cấm
    let name = String(d.name || document.title || id)
      .replace(/[~～〜]/g, '')
      .replace(/[\/／]/g, '・')
      .replace(/[\\:*?"<>|\u0000-\u001f]/g, '')
      .replace(/\s+/g, ' ')
      .trim()
      .replace(/[. ]+$/, '');
    if (!name) name = id;

    // 7) Tải về (UTF-8, không BOM)
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([md.endsWith('\n') ? md : md + '\n'], { type: 'text/markdown;charset=utf-8' }));
    a.download = name + '.md';
    document.body.appendChild(a);
    a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
    const t = document.createElement('div');
    t.textContent = (a1 === a2 ? '✓ Khớp 100% với trang: ' : '⚠ Đã tải (CÓ LỆCH so với trang): ') + a.download;
    t.style.cssText = 'position:fixed;right:16px;bottom:16px;z-index:99999;padding:10px 14px;border-radius:8px;color:#fff;font:14px sans-serif;background:' + (a1 === a2 ? '#16a34a' : '#d97706');
    document.body.appendChild(t);
    setTimeout(() => t.remove(), 4000);
  } catch (e) {
    say('Lỗi: ' + (e && e.message ? e.message : e));
  }
})();
