from pathlib import Path
import json,re

root=Path(__file__).resolve().parent.parent
tex=root/'chapter03_slides.tex'
s=tex.read_text(encoding='utf8')
assert '\\originalfigure{' not in s
# figure number | insert after topic | Chinese figure title | reading cue
data='''1|升力與阻力的兩種描述|翼面壓力分布|比較上、下翼面的壓力分布，並將分布力連到合升力。
2|升力與阻力的兩種描述|气流動量與反作用力|觀察氣流偏轉與動量改變，這與壓力分布是同一氣動作用的兩種描述。
3|迎角、姿態與航跡角|迎角、升力與阻力方向|迎角以翼弦與相對氣流為基準，升力方向未必等於機體向上方向。
4|升力曲線與失速|升阻力係數與迎角|注意失速附近的升力曲線轉折，以及大迎角下阻力的增加。
5|阻力極線與高升力裝置|前緣縫翼與後緣襟翼|比較高升力裝置伸出與收回時，升力係數對迎角的變化。
6|尾翼如何平衡俯仰力矩|主翼與尾翼的配平作用|依 CG、機翼氣動中心與尾翼力臂，逐項核對力矩正負號。
7|配平的代價與幾何量提醒|機翼與尾翼力矩的疊加|合成曲線的零點決定配平迎角，斜率則反映靜恢復作用。
8|靜穩定與動穩定|穩定、中性與不穩定的類比|比較小球離開平衡位置後，受到的作用是否促使它回到原處。
9|靜穩定與動穩定|靜穩定與動穩定|分別觀察初始恢復趨勢，以及時間響應的振幅是否衰減。
10|縱向靜穩定判據|俯仰力矩係數的斜率|原圖同時比較正、零、負斜率，對應不同的縱向靜穩定情況。
11|中性點與靜裕度|陣風與自然恢復力矩|比較向上陣風、配平及向下陣風時，迎角與恢復力矩的方向。
12|不穩定配置與主動穩定|不穩定飛機的配平配置|注意 CG 與氣動中心的相對位置，以及尾翼升力的方向。
13|不穩定配置與主動穩定|倒著騎自行車的控制類比|教材用此圖說明不穩定配置需要快速、持續的修正。
14|不穩定配置與主動穩定|Tornado 與 FBW Jaguar|教材以編隊照片比較配平尾翼力方向不同的兩種配置。
15|六自由度與機體座標|機體軸、速度與操縱面|對照軸向、角速度與控制面符號，尤其注意 z 軸朝下。
16|旋轉座標系中的加速度|座標旋轉造成的速度變化|將圖上的微小向量變化連到角速度與速度向量的叉積項。
17|Euler 角與旋轉次序|Euler 姿態角|區分姿態角與機體角速度，並留意旋轉次序的重要性。
18|小擾動線性化的起點|飛機受到的外力|配平時各方向的合力為零，擾動模型處理的是力的增量。
19|小擾動力與力矩方程|氣動力、推力與重力分量|對照重力投影與三軸力矩，核對運動方程中的符號。
20|俯仰阻尼的來源|俯仰率造成的尾翼阻尼|尾翼切向速度改變局部迎角，其力矩反抗原來的俯仰運動。
21|側滑力與風向標穩定|側滑與側向力|區分機身側力和垂尾側力，以及它們關於 CG 的力矩。
22|側滑如何產生滾轉|上反角與側滑的作用|側滑改變左右翼有效迎角，升力差因而產生滾轉力矩。
23|角速度導數與橫向耦合|滾轉率造成的阻尼力矩|比較左右翼的局部速度與升力變化，辨認反抗滾轉的力矩。
24|升降舵輸入如何改變飛行路徑|縱向機動的建立過程|從尾翼力矩、迎角變化，依序追到主翼升力與航跡彎曲。
25|完整縱向響應的兩個時間尺度|短週期與長週期響應|上方是俯仰率，下方是尾翼輸入，留意兩種時間尺度。
26|短週期近似的假設|穩定軸下的縱向力與力矩|核對迎角、俯仰率與尾翼偏轉在受力圖中的作用。
27|正負號統一：帶符號導數與正大小值|俯仰運動的方塊圖|保留教材原符號；求和點的負號與導數大小值须搭配前頁約定閱讀。
28|正負號統一：帶符號導數與正大小值|迎角運動的方塊圖|觀察俯仰率、直接尾翼力與迎角回授如何共同影響迎角變化率。
29|消去迎角，得到俯仰角速度傳遞函數|一般負回授關係|辨認前向路徑與回授路徑，再將此關係套用到飛機內部動態。
30|與教材時間常數寫法的對照|簡化後的縱向回授模型|兩個一階環節與迎角恢復回授，構成短週期二階動態。
31|與教材時間常數寫法的對照|俯仰率與迎角的傳遞關係|原圖以 D 表示微分算子；俯仰率與迎角共享極點，但零點不同。
32|二階極點、自然頻率與阻尼比|二階系統的自由響應|這張原圖是初始擾動的自由響應，不能直接當作所有輸出的階躍過衝圖。
33|坡度轉彎的力平衡|協調水平轉彎的受力|水平升力提供向心力，垂直分量平衡重量。
34|純滾轉的一階近似|副翼階躍與滾轉率|將原圖的時間常數與漸近穩態值，對照一階響應公式。
35|Power Control Unit 的作用|機械傳令的動力操縱系統|從飛行員操縱器沿連桿追到各操縱面的 PCU。
36|PCU 位置回授的幾何關係|PCU 閥口與活塞回授|先辨認輸入、閥芯、液壓腔及活塞，再核對機械回授路徑。
37|SAS 以回授建立額外阻尼|簡單穩定增強系統|比較飛行員輸入和角速度回授如何在差動機構中合成。
38|Wash-out 為何讓偏航阻尼器不抵抗轉彎？|洗出與高頻截止的頻率特性|低頻抑制持續轉彎成分，高頻截止降低雜訊與結構模態的影響。
39|俯仰 SAS 的閉迴路推導|俯仰率增穩回路|追蹤飛行員指令、俯仰率量測與增穩舵角的負回授。
40|極點改善不等於所有輸出都同樣改善|加入增穩前後的響應|此圖為教材示意，用來比較振盪衰減，不當作本筆記重算模型的數值曲線。
41|旋翼使空氣流過翼面|固定翼與旋翼的升力來源|比較兩種飛行器如何讓空氣流過翼面。
42|旋翼配置與反扭矩|單主旋翼配置|教材照片為 AgustaWestland AW159 Lynx Wildcat，注意主旋翼與尾旋翼。
43|旋翼配置與反扭矩|同軸反轉與推進螺旋槳|教材以 S97 概念配置圖說明同軸反轉旋翼及額外推進裝置。
44|旋翼配置與反扭矩|縱列反轉旋翼|前後兩組旋翼共同支撐重量，並以反向旋轉處理主要反作用扭矩。
45|旋翼配置與反扭矩|交叉嚙合反轉旋翼|注意兩個旋翼軸的位置與相互交错的旋轉區域。
46|旋翼接頭：揮舞與擺振|鉸接旋翼的揮舞與擺振|在原圖定位兩種鉸，區分平面外揮舞和平面內擺振。
47|旋翼剛性如何影響機身響應|教材的半剛性旋翼示意|依實際柔性部位理解載荷與運動，不僅依賴分類名稱。
48|旋翼剛性如何影響機身響應|剛性旋翼示意|比較前圖的連接方式，留意葉片仍可能有彈性變形。
49|斜盤把機身指令送到旋轉葉片|斜盤機構|沿致動器、斜盤與槳距連桿追蹤輸入，分辨整體升降與傾斜。
50|總距、週期變距與腳踏板|直升機飛行員的操縱器|辨認總距桿、週期變距操縱桿和腳踏板的對應控制軸。
51|縱向 cyclic 與向前飛行|直升機縱向力與力矩|觀察旋翼力的作用線與 CG，理解盤面傾斜如何影響俯仰。
52|縱向 cyclic 與向前飛行|穩態前飛的力平衡|旋翼力的垂直分量支撐重量，水平分量平衡阻力。
53|直升機增穩的冗餘架構|直升機 SAS 的冗餘配置|比較各獨立通道與致動器的連接方式，失效行為取決於合成及監控機制。
54|直升機俯仰增穩：CG 變動與配平|直升機俯仰增穩通道|辨識桿位置前饋、姿態與角速度回授，以及配平和限制器。
55|滾轉增穩：小坡度與大坡度|直升機滾轉增穩通道|觀察 wash-out、限制器、相位超前與致動器各自所在的位置。
56|偏航與總距通道|直升機偏航增穩通道|偏航率提供基本阻尼，圖中虛線表示可加入的側向加速度訊號。
'''
mapping={}
for line in data.strip().splitlines():
    n,anchor,title,note=line.split('|')
    mapping[int(n)]=(anchor,title.replace('气','氣'),note.replace('须','須').replace('交错','交錯'))
macro=r'''
% Original images extracted losslessly from the supplied textbook PDF.
\newcommand{\originalfigure}[6]{
\begin{frame}[t]{課本原圖 #1：#2}
\centering
\includegraphics[width=.94\linewidth,height=5.05cm,keepaspectratio]{figures/#4}\par
\vspace{2mm}\raggedright\small #5\par
\vfill{\scriptsize\color{teal}原圖：Collinson, 第 3 版，Fig. #1，p. #3。#6}\par
\end{frame}}
'''
s=s.replace('\\begin{document}',macro+'\n\\begin{document}',1)
rows=json.loads((root/'figures/sources.json').read_text(encoding='utf8'))
additions={}
for row in rows:
    n=row['number']; part=row['part'];anchor,title,note=mapping[n]
    if n==9:title={'a':'靜穩定的初始趨勢','b':'動穩定的振幅變化'}[part]
    if n==53:title={'a':'Duplex 雙通道','b':'Dual-dual 雙重雙通道','c':'Triplex 三通道'}[part]
    ident=f'3.{n}'+(f'({part})' if part else '')
    credit={14:'Photo: Arthur Gibson / British Aerospace Defence Ltd.',35:'Courtesy of BAE Systems.',42:'Courtesy of AgustaWestland.'}.get(n,'')
    block=f'\n\\originalfigure{{{ident}}}{{{title}}}{{{row["page"]}}}{{{row["file"]}}}{{{note}}}{{{credit}}}\n'
    additions.setdefault(anchor,[]).append(block)
for anchor,blocks in additions.items():
    match=re.search(r'\\slide\{'+re.escape(anchor)+r'\}[\s\S]*?\n\}',s)
    assert match,anchor
    s=s[:match.end()]+''.join(blocks)+s[match.end():]
tex.write_text(s,encoding='utf8')
# Create an index tied to the new actual slide order.
sections=[];figindex=[];slide=1
for line in s.splitlines():
    if line.startswith('\\section{'):
        sections.append([re.match(r'\\section\{(.*?)\}',line)[1],slide+1,None])
    if line.startswith('\\slide{') or line.startswith('\\originalfigure{'):
        slide+=1
        if sections:sections[-1][2]=slide
        if line.startswith('\\originalfigure{'):
            args=re.findall(r'\{([^{}]*)\}',line)
            figindex.append((args[0],args[1],args[2],slide,args[3]))
assert slide==177
md=['# 課本原圖索引','','第三章全部 Fig. 3.1–3.56，按講解主題插入投影片。Fig. 3.9 與 3.53 的分圖各占一頁，共 59 張原圖頁。圖片直接擷取 PDF 內嵌影像，以原解析度存為無損 PNG，沒有重繪或改寫圖內標籤。','','| 圖號 | 主題 | 教材頁 | 投影片 | 圖片 |','|---|---|---|---|---|']
for ident,title,page,num,file in figindex:md.append(f'| {ident} | {title} | {page} | {num} | [原圖](figures/{file}) |')
md+=['','所有原圖來源：R. P. G. Collinson, Introduction to Avionics Systems, 3rd ed., Springer, 2011。照片及廠商圖仍依教材標示原提供者。','','## 原文圖說紀錄','']
seen=set()
for row in rows:
    if row['number'] in seen:continue
    seen.add(row['number']);md.append(f"- p. {row['page']}: {row['caption']}")
(root/'FIGURE_INDEX.md').write_text('\n'.join(md)+'\n',encoding='utf8')
readme=(root/'README.md').read_text(encoding='utf8').replace('共 118 頁','共 177 頁').replace('圖表直接寫在 LaTeX 中，沒有外部圖片依賴。','包含原有推導與圖表，並引用 `figures/` 的課本原圖；搬移時請保留該資料夾。')
start=readme.index('| 投影片 |');end=readme.index('\n\n建議',start)
table='| 投影片 | 內容 |\n|---|---|\n'+'\n'.join(f'| {a}–{b} | {title} |' for title,a,b in sections)
readme=readme[:start]+table+readme[end:]
readme=readme.replace('- `build/`', '- `figures/`：59 張課本原始分圖與來源資料。\n- `FIGURE_INDEX.md`：原圖、教材頁碼與更新後投影片頁碼的對照。\n- `build/`')
readme=readme.replace('原始檔保留於內建編輯器，可繼續修改。','原始檔保留於內建編輯器，可繼續修改。加入原圖後需使用本機編譯，內建編譯器也不支援這類多檔圖片專案。')
(root/'README.md').write_text(readme,encoding='utf8')
print('Inserted 59 original-image slides; total',slide)
print(sections)
