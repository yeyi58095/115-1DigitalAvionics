from pathlib import Path
import re
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent.parent
pdf=root/'chapter03_slides.pdf'
r=PdfReader(pdf);d=pdfium.PdfDocument(str(pdf))
assert len(r.pages)==177
selected=[i for i,p in enumerate(r.pages) if '課本原圖' in p.extract_text()]
assert len(selected)==59
log=(root/'build/chapter03_slides.log').read_text(encoding='utf8',errors='replace')
assert 'Overfull' not in log
assert 'Missing character' not in log
for i in selected:
    im=d[i].render(scale=2).to_pil().convert('RGB')
    im.save(root/f'build/original-slide-{i+1:03}.png')
for k in range((len(selected)+11)//12):
    canvas=Image.new('RGB',(1800,1200),'#dfe5e8');draw=ImageDraw.Draw(canvas)
    for j,i in enumerate(selected[k*12:k*12+12]):
        im=Image.open(root/f'build/original-slide-{i+1:03}.png');im.thumbnail((575,270))
        x=10+(j%3)*600;y=22+(j//3)*295
        canvas.paste(im,(x,y));draw.text((x,y-17),f'SLIDE {i+1}',fill='black')
    canvas.save(root/f'build/inserted-contact-{k+1}.png')
print('Verified 177 pages, 59 original-image pages, no overflow/missing glyphs.')
print('Inserted slide numbers:',[i+1 for i in selected])
print('File size MB:',round(pdf.stat().st_size/1e6,2))
