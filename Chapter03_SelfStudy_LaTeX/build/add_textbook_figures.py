from pathlib import Path
import re,json
from pypdf import PdfReader
import pdfplumber
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parent.parent
source=root.parent/'textbook.pdf'
assets=root/'figures'
assets.mkdir(exist_ok=True)
r=PdfReader(source)
pl=pdfplumber.open(source)
rows=[]
for i in range(115,192):
    p=pl.pages[i]
    caps=[w for w in p.extract_words() if re.fullmatch(r'Fig\.3\.\d+',w['text'])]
    if not caps: continue
    # The original diagrams are embedded raster images. Ignore thin equation bars.
    significant=[im for im in p.images if im['width']>80 and im['height']>20]
    significant.sort(key=lambda x:x['top'])
    names={im.name.split('.')[0]:im for im in r.pages[i].images}
    for j,im in enumerate(significant):
        cap=next(c for c in caps if c['top']>=im['bottom']-1)
        n=int(cap['text'].split('.')[-1])
        siblings=[x for x in significant if x['bottom']<=cap['top']+1 and not any(c['top']<cap['top'] and c['top']>=x['bottom']-1 for c in caps)]
        part=chr(97+siblings.index(im)) if len(siblings)>1 else ''
        name=f'fig-3-{n:02}{part}.png'
        raw=names[im['name']].image.convert('RGB')
        raw.save(assets/name)
        # Capture original caption and any attribution lines, until a paragraph gap.
        chars=[c for c in p.chars if c['top']>=cap['top']-.5 and c['top']<cap['top']+55]
        lines=[]
        for top in sorted(set(round(c['top'],1) for c in chars)):
            if lines and top-lines[-1][0]>13:break
            txt=''.join(c['text'] for c in sorted([c for c in chars if abs(c['top']-top)<.06],key=lambda c:c['x0']))
            lines.append((top,txt))
        caption=' '.join(t for _,t in lines)
        rows.append(dict(number=n,part=part,page=i-14,pdf_page=i+1,file=name,caption=caption,size=raw.size))

assert sorted(set(x['number'] for x in rows))==list(range(1,57))
assert len(rows)==59
(assets/'sources.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
for k in range((len(rows)+11)//12):
    canvas=Image.new('RGB',(1600,1250),'#e4e8eb');draw=ImageDraw.Draw(canvas)
    for j,row in enumerate(rows[k*12:k*12+12]):
        im=Image.open(assets/row['file']);im.thumbnail((510,270))
        x=10+(j%3)*530;y=30+(j//3)*310
        canvas.paste(im,(x,y));draw.text((x,y-20),f"Fig. 3.{row['number']}{row['part']} / p.{row['page']}",fill='black')
    canvas.save(root/f'build/original-figures-{k+1}.png')
print('Extracted',len(rows),'panels, covering all 56 numbered figures')
