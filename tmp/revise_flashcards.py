from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'flashcard_app/alias.txt'
questions = '''
航電（Avionics）涵蓋哪些機載電子功能？請舉例。
Digital Avionics 如何用數位設備整合機載資訊與功能？
A/D 在感測訊號進入電腦時做什麼？請說出英文全名與轉換方向。
D/A 在數位命令送往類比設備時做什麼？請說出英文全名與轉換方向。
在空氣資料系統中，ADC 的英文全名、輸入量測與主要輸出是什麼？
CPU 的英文全名與工作是什麼？其時脈能直接視為控制更新率嗎？
航電設備之間的 Bus 有什麼用途？
航電標準名稱中的 ARINC 原英文名稱是什麼？與設備規格有何關係？
ARINC 429 是哪一類航電介面？其傳輸方向有何特徵？
ARINC 629 如何讓多個航電終端交換資料？
IMA 的英文全名是什麼？如何在共用運算平台上承載不同功能？
LRU 的英文全名是什麼？這種設計對現場維修有什麼好處？
VLSI 的英文全名是什麼？與晶片整合程度有何關係？
EMI 的英文全名是什麼？會如何影響航電設備？
BIT 的英文全名是什麼？能如何協助設備監視與維修？
航電系統的 Redundancy 是什麼？為什麼需要額外通道？
Common-Mode Failure 是什麼？為何可能讓多個備援通道同時失去作用？
航電架構中的 CNS 代表哪三項功能？請說出英文全名與各自用途。
ATM 的英文全名是什麼？如何使用 CNS 資訊協調航空交通？
以美國為例，NAS 的英文全名是什麼？包含哪些運作要素？
ICAO 的英文全名是什麼？在國際民航中扮演什麼角色？
ATC 的英文全名是什麼？主要提供哪些服務？
航空通訊中的 HF 英文全名是什麼？常用於何種距離的通訊？
航空通訊中的 VHF 英文全名是什麼？傳播距離主要受什麼條件限制？
航空通訊中的 UHF 英文全名是什麼？常見於何種航空環境？
SATCOM 的英文全名是什麼？如何支援遠距離連線？
航空通訊標記 A/G 的英文全名是什麼？兩端分別是誰？
航空通訊標記 A/A 的英文全名是什麼？兩端分別是誰？
ADS-B 的英文全名是什麼？航空器廣播的資訊從哪裡取得？
TCAS 的英文全名與主要用途是什麼？
ELT 的英文全名是什麼？在什麼情況提供何種協助？
PBN 的英文全名是什麼？導航要求以什麼為依據？
CNS 中的 Surveillance 要取得哪些航空器資訊？提供給誰使用？
National Airspace 指什麼？包含哪些空域運作要素？
在飛行任務中，Guidance 要根據目標與目前狀態決定什麼？
Navigation 要估計哪些航空器狀態？
Radio Navigation 利用什麼外部訊號提供哪些導航資訊？
在基本導航分類中，Dead Reckoning 如何由起點推算位置？主要限制是什麼？
本題庫的 Fixed-Point Positioning 指利用外部來源取得地球參考位置；這與單靠推算有何不同？
GNSS 的英文全名是什麼？請舉出所包含的衛星星系。
GPS 的英文全名是什麼？它與 GNSS 是什麼關係？
VOR 的英文全名是什麼？提供航空器相對導航台的哪種資訊？
DME 的英文全名是什麼？量測原理與距離種類是什麼？
ADF 的英文全名是什麼？它接收什麼訊號、指示什麼資訊？
TACAN 的英文全名是什麼？主要使用對象與提供的導航量是什麼？
ILS 的英文全名是什麼？提供哪兩個方向的進場引導？
VFR 的英文全名是什麼？飛行依據的條件與程序是什麼？
IFR 的英文全名是什麼？飛行依據的設備與程序是什麼？
GNSS/INS Integration 中，兩種導航來源如何互補？
Navigation Aid 可以如何修正或驗證導航狀態？請舉例。
GNC 的英文全名是什麼？三個部分各自回答哪一類問題？
Control 如何利用目標命令與實際回授產生操縱輸入？
FBW 的英文全名是什麼？飛行員輸入如何傳到操縱面？
FCC 的英文全名是什麼？利用哪些資料計算操縱命令？
飛控中的 Control Law 把哪些輸入轉成什麼輸出？
Autopilot 可以自動維持或改變哪些飛行狀態？
閉迴路系統中的 Controller 如何決定控制命令？
Actuator 如何把控制命令轉成實際動作？請舉例。
操縱面驅動系統中的 PCU 英文全名與功能是什麼？
在飛控回授架構中，SAS 的英文全名是什麼？如何改善穩定性或阻尼？
737 MAX 飛控中的 MCAS 英文全名與主要功能是什麼？
在飛控回授中，Rate Gyro 量測什麼？
控制方塊圖的 Error Summing Junction 如何產生誤差訊號？
Closed-Loop Control 如何利用輸出回授修正輸入？
Pitch Rate 代表哪種旋轉、繞哪個機體軸？常用符號是什麼？
Roll Rate 代表哪種旋轉、繞哪個機體軸？常用符號是什麼？
Heading 描述航空器的什麼方向？通常以什麼為參考？
Elevator 是哪個操縱面？主要控制哪種旋轉運動？
Aileron 是哪個操縱面？主要控制哪種旋轉運動？
Rudder 是哪個操縱面？主要控制哪種旋轉運動？
Airfoil 描述機翼的哪種幾何形狀？主要用途是什麼？
AOA 的英文全名是什麼？它是由哪兩條方向線定義的角度？
Wing Incidence 是哪兩條基準線的夾角？一般會隨飛行姿態改變嗎？
Lift 的方向相對來流如何定義？
Drag 的方向相對航空器穿越空氣的運動如何定義？
Thrust 由什麼產生？在飛行中主要有何作用？
Weight 由什麼作用產生？方向大致指向哪裡？
Center of Pressure 是什麼作用點？位置是否固定？
Aerodynamic Center 以哪個力矩特徵定義？低速薄翼型常近似在哪裡？
Free Stream 指哪一部分氣流？為什麼可作分析參考？
Relative Wind 的方向與飛機相對空氣的速度有何關係？
Air Density 的定義是什麼？會影響哪些氣動性能？
Lift Coefficient 表示什麼？升力以哪些量作無因次化？
CLmax 的英文名稱與物理意義是什麼？
在固定翼幾何中，Angle of Incidence 與 AOA 的參考方向有何不同？
本題庫的 Slip Angle 指飛機側滑角 β；它描述速度向量相對機體哪個平面的偏離？
Static Stability 判斷小擾動後的哪一種初始反應？
Dynamic Stability 判斷擾動後運動隨時間的哪幾種趨勢？
Neutral Point 是什麼位置？重心在其前方通常表示什麼縱向穩定性？
Static Margin 如何由中性點與重心位置定義？通常如何表示？
Center of Gravity 是什麼位置？與中性點的相對位置為何重要？
飛機達到 Trim 時，主要力與力矩須滿足什麼條件？
Stall 的直接氣動條件是什麼？升力與阻力通常如何變化？
基本飛行力學中的 Load Factor 如何定義？平飛與轉彎時如何解讀？
本卡的 Accelerating Flight 指速率大小改變；沿運動方向的合力有何條件？
Turning Flight 即使速率不變，為什麼仍需要合力？
Thrust-to-Throttle Mapping 描述哪兩者的對應？是否可隨飛行階段調整？
從飛行操縱特性來看，SAS 的英文全名是什麼？如何藉小幅回授修正改善穩定性？
從縱向操縱特性來看，MCAS 的英文全名是什麼？在特定條件下扮演何種角色？
Aircraft Dynamics 研究操縱與外力如何影響哪些運動狀態？
飛機的 Equation of Motion 連結哪些力學量與運動量？
Nonlinear Model 保留什麼關係？適用範圍與計算負擔如何？
Linear Model 通常在哪種飛行狀態附近建立？適合分析什麼？
Body Frame 如何固定在飛機上？軸向會如何隨機體運動？
Earth-Fixed Frame 固定於什麼？軸向是否跟著飛機轉動？
Inertial Frame 需滿足哪些理想參考系條件？
Stability Axes 以哪個平衡飛行方向建立？常用於哪種分析？
在機體座標系中，線速度分量 u（本題庫索引 U）沿哪個軸？常見 x 向前、y 向右、z 向下的約定中，正方向為何？
在機體座標系中，線速度分量 v（本題庫索引 V，非總空速）沿哪個軸？常見 x 向前、y 向右、z 向下的約定中，正方向為何？
在機體座標系中，線速度分量 w（本題庫索引 W，非重量）沿哪個軸？常見 x 向前、y 向右、z 向下的約定中，正方向為何？
在機體座標系中，角速度分量 p（本題庫索引 P）代表哪種旋轉？繞哪個軸？
在機體座標系中，角速度分量 q（本題庫索引 Q，非動壓）代表哪種旋轉？繞哪個軸？
在機體座標系中，角速度分量 r（本題庫索引 R，非旋轉矩陣）代表哪種旋轉？繞哪個軸？
Euler Angles 如何表示三維姿態？為何必須指定旋轉軸序？
Quaternion 如何表示三維旋轉？相較 Euler 角可避免什麼問題？
Direction Cosine Matrix 連結什麼座標關係？可用來做什麼轉換？
Control Surface 如何改變飛機的力與力矩？請舉例。
INS 的英文全名是什麼？由慣性量測推算哪些導航狀態？
IMU 的英文全名與主要量測是什麼？一定會直接輸出位置嗎？
慣性感測器架構中的 ISA 英文全名是什麼？本卡不是指標準大氣；它提供哪類資料？
Strapdown INS 的感測器如何安裝？如何把量測轉到導航座標系？
Platform INS 的感測器如何保持參考方向？
Gyroscope 可量測或提供什麼慣性資訊？
Accelerometer 實際量測什麼？在慣導中有何用途？
RLG 的英文全名是什麼？用哪種光學差異量測旋轉？
FOG 的英文全名是什麼？用哪種光學差異量測旋轉？
HRG 的英文全名是什麼？利用哪種結構與物理現象量測旋轉？
MEMS 的英文全名是什麼？整合了哪兩類元件？
Sagnac Effect 發生在何種光路？反向傳播光束會有什麼差異？
Specific Force 與包含重力的運動加速度有何關係？
在慣性感測器分類中，Rate Gyro 的直接輸出量是什麼？
Gyro Bias 是什麼量測誤差？為何積分後會造成姿態漂移？
Scale Factor Error 描述感測器輸入與輸出間的哪種誤差？
Gyro Noise 是什麼？會如何影響積分角度與慣導精度？
Accelerometer Bias 經過一次與兩次積分，分別造成什麼誤差？
Misalignment 是哪些軸之間的誤差？如何影響量測分量？
慣性導航中的 Drift 指什麼現象？可能由哪些誤差造成？
從誤差累積的角度看，Dead Reckoning 如何推算位置？為何長時間後需要外部修正？
INS 的 Initial Alignment 在開始導航前要估計哪些初始資訊？
慣性感測器的 Calibration 要估計並補償哪些誤差？
Complementary Filter 如何利用不同感測器的頻率特性互補？請舉例。
Kalman Filter 如何結合模型預測、量測與不確定度估計狀態？
EKF 的英文全名是什麼？如何把卡爾曼濾波延伸到非線性系統？
Aided INS 如何利用外部量測限制長期漂移？請舉例。
Radio Altimeter 量測相對哪個表面的高度？使用什麼訊號？
Barometric Altitude 由哪些量測與模型推算？
TMR 的英文全名是什麼？有幾個通道、多數決通常可容忍幾個故障？
QMR 的英文全名是什麼？有幾個通道、可採用哪些表決方法？
Voting Logic 如何比較多個通道？要選擇或辨識什麼？
Fault Tolerance 描述系統在什麼情況下仍維持何種能力？
Fail-Operational 要求故障後仍維持什麼能力？實際可容忍故障數由什麼決定？
Fail-Safe 要求故障後系統轉入什麼狀態？
'''.strip().splitlines()

fixes = {
    'Angle of Incidence': '翼安裝角: 在固定翼幾何中指翼弦線與機身縱向基準線的夾角，通常由結構安裝決定，與相對氣流及翼弦之間的攻角 AOA 不同；Wing Incidence 為同義用語。',
    'Load Factor': '載荷因數: 基本協調飛行分析常用 n = L/W，為升力與重量之比，是無因次量，常口語稱幾 g；定常水平直線飛行約為 1，協調水平轉彎通常大於 1。更一般的結構載荷定義須指定所取氣動力分量。',
    'Aerodynamic Center': '氣動中心: 在適用的攻角範圍內，繞此參考點的俯仰力矩隨攻角近似不變；低速薄翼型常近似在弦長四分之一處，位置依翼型與流況而異。',
    'Slip Angle': '側滑角（Sideslip Angle, β）: 速度向量偏離機體 x-z 對稱平面的角度，反映側向速度分量；本題庫沿用 Slip Angle 索引。',
    'U': 'Forward Velocity（u）: 機體 x 軸方向的線速度分量；採 x 向前、y 向右、z 向下的常見機體軸約定時，向前為正。',
    'V': 'Sideways Velocity（v）: 機體 y 軸方向的線速度分量；採 x 向前、y 向右、z 向下的常見機體軸約定時，向右為正，不是總空速大小。',
    'W': 'Vertical Velocity（w）: 機體 z 軸方向的線速度分量；採 x 向前、y 向右、z 向下的常見機體軸約定時，向下為正，不一定等於地球垂直方向的下降率，也不是重量。',
    'P': 'Roll Rate（p）: 機體角速度向量沿 x 軸的分量，即繞機體縱軸的滾轉角速度；正負依右手定則，不可一般性地直接當作 Euler 滾轉角的時間微分。',
    'Q': 'Pitch Rate（q）: 機體角速度向量沿 y 軸的分量，即繞機體橫軸的俯仰角速度；正負依右手定則，不是動壓，也不一般等於 Euler 俯仰角的時間微分。',
    'R': 'Yaw Rate（r）: 機體角速度向量沿 z 軸的分量，即繞機體垂直軸的偏航角速度；正負依右手定則，不是旋轉矩陣，也不一般等於航向角的時間微分。',
    'Fail-Operational': '故障後可運作: 在設計規定的故障情境下，系統仍可持續執行指定功能；可容忍的故障種類與數量由具體系統需求及架構決定。',
}

lines = path.read_text(encoding='utf-8-sig').splitlines()
entries = [line for line in lines if line and not line.startswith(('#', '[', '? '))]
assert len(entries) == len(questions) == 152, (len(entries), len(questions))
out = ['# Digital Avionics 情境式閃卡題庫', '# ? 開頭的行是下一張卡片的題目；答案仍為 詞彙: 全名／解釋。', '# 保留原始詞彙索引以相容歷史錯題。', '']
i = 0
for line in lines:
    if line.startswith('['):
        out.extend(['', line])
    elif line and not line.startswith(('#', '? ')):
        term, answer = line.split(': ', 1)
        out.extend(['? ' + questions[i], term + ': ' + fixes.get(term, answer)])
        i += 1
content = '\n'.join(out).strip() + '\n'
path.write_text(content, encoding='utf-8')
(root / 'alias.txt').write_text(content, encoding='utf-8')
print(f'Updated {i} contextual questions in both banks.')
