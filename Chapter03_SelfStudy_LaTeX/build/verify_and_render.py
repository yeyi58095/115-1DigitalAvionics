from pathlib import Path
import math, json, re
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent.parent
tex = root / 'chapter03_slides.tex'
# Keep Traditional Chinese consistent throughout the authored text.
s = tex.read_text(encoding='utf-8')
for a,b in {'资料':'資料','取决':'取決','機头':'機頭','側力':'側力','垂尾侧力':'垂尾側力','對称':'對稱','改变':'改變','實际':'實際','实际':'實際','依赖':'依賴','结构':'結構','飞行':'飛行','系統':'系統','系统':'系統','滤波':'濾波','独':'獨','与':'與','關系':'關係','关系':'關係'}.items():
    s = s.replace(a,b)
tex.write_text(s, encoding='utf-8')

g=9.81
A1=1/.55+1/.67
A2=2e7/6e5+1/(.55*.67)
K=3.5e7/(6e5*.67)
z=A1/(2*math.sqrt(A2))
qa=(K*.67)**2
qb=2*A1*K*.67-1.96*K
qc=A1*A1-1.96*A2
gain=(-qb+math.sqrt(qb*qb-4*qa*qc))/(2*qa)
exercise_gain=(-304+math.sqrt(304**2+4*2500*45.56))/(2*2500)
results={'A1':A1,'A2':A2,'K':K,'omega_n':math.sqrt(A2),'damping_ratio':z,
 'SAS_gain':gain,'SAS_frequency':math.sqrt(A2+K*gain),
 'standard_overshoot':math.exp(-math.pi*z/math.sqrt(1-z*z)),
 'turn_60_degrees_rate_deg_s':g*math.tan(math.pi/3)/100*180/math.pi,
 'exercise_stall_1g':math.sqrt(2*30000*g/(1.225*75*1.2)),
 'exercise_stall_2g':math.sqrt(4*30000*g/(1.225*75*1.2)),
 'exercise_turn_radius':10000/(g*math.tan(math.pi/6)),
 'exercise_roll_angle_1sec':20*(1-.5*(1-math.exp(-2))),
 'exercise_SAS_gain':exercise_gain}
assert abs(A1-3.3107)<1e-4
assert abs(gain-.1045)<1e-4
assert abs((A1+K*.67*gain)/(2*math.sqrt(A2+K*gain))-.7)<1e-10
assert abs((5+50*exercise_gain)/(2*math.sqrt(36+100*exercise_gain))-.7)<1e-10
(root/'build/numerical_checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))

pdfpath=root/'build/chapter03_slides.pdf'
doc=pdfium.PdfDocument(str(pdfpath))
reader=PdfReader(str(pdfpath))
titles=[]
for i,page in enumerate(reader.pages):
    lines=(page.extract_text() or '').splitlines()
    titles.append({'slide':i+1,'heading':lines[0] if lines else ''})
(root/'build/slide_index.json').write_text(json.dumps(titles,ensure_ascii=False,indent=2),encoding='utf-8')
for batch in range((len(doc)+11)//12):
    canvas=Image.new('RGB',(1800,1160),'#dfe5e8')
    draw=ImageDraw.Draw(canvas)
    for j in range(12):
        idx=batch*12+j
        if idx>=len(doc):break
        page=doc[idx].render(scale=1.5).to_pil().convert('RGB')
        page.save(root/f'build/slide-{idx+1:03}.png')
        page.thumbnail((580,326))
        x=10+(j%3)*600;y=22+(j//3)*288
        page.thumbnail((580,258))
        canvas.paste(page,(x,y))
        draw.text((x,y-16),f'SLIDE {idx+1}',fill='black')
    canvas.save(root/f'build/contact-{batch+1:02}.png')
print('Rendered',len(doc),'slides')
