from pathlib import Path
import fitz

repo = Path('D:/CODE/git/kaiwa_skill')
pdf = repo / 'kaiwa_skill/book/Kaiwa/210-additional-super-miniature-phrases-for-immediate-use-in-japanese-conversation-4863922639-9784863922631_compress.pdf'
out = repo / '.cache/root-live-qa'
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
for head in range(1, 211):
    page_no = head + 15
    page = doc[page_no-1]
    r = page.rect
    box = fitz.Rect(r.width*.82, r.height*.018, r.width, r.height*.135)
    page.get_pixmap(matrix=fitz.Matrix(4,4), clip=box, alpha=False).save(out/f'mini210-icon-h{head:03}-p{page_no:03}.png')
for start in range(1, 211, 30):
    heads = list(range(start, min(start+30, 211)))
    tile_w, tile_h = 310, 324
    contact = fitz.open()
    sheet = contact.new_page(width=tile_w*5,height=tile_h*6)
    for i,head in enumerate(heads):
        page_no = head+15
        x=(i%5)*tile_w;y=(i//5)*tile_h
        sheet.insert_text((x+10,y+24),f'head {head:03} / PDF {page_no:03}',fontsize=19,color=(0,0,0))
        image_path=out/f'mini210-icon-h{head:03}-p{page_no:03}.png'
        sheet.insert_image(fitz.Rect(x+8,y+36,x+tile_w-8,y+tile_h-8),filename=str(image_path),keep_proportion=True)
        sheet.draw_rect(fitz.Rect(x,y,x+tile_w,y+tile_h),color=(.6,.6,.6),width=1)
    sheet.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).save(out/f'mini210-audio-sheet-{start:03}-{heads[-1]:03}.png')
    contact.close()
print('crops',210,'sheets',7)
