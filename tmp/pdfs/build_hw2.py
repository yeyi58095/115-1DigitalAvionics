from pathlib import Path
base=Path('HW1/digitalAvionics_hw1_solutions.tex').read_text(encoding='utf-8')
head=base.split('\\section*{Question 1}')[0].replace('Homework 1','Homework 2')
head=head.replace('\\usepackage{enumitem}', '\\usepackage{enumitem}\n\\usepackage{graphicx,tikz}\n\\usetikzlibrary{arrows.meta}\n\\tikzset{block/.style={draw,minimum height=0.85cm,align=center,font=\\small},sum/.style={draw,circle,inner sep=1pt,minimum size=0.42cm},arr/.style={-{Stealth[length=2mm]},thick}}')
def diagram(heading=False):
    a,b,c,d,e,f=('\\psi','\\phi','p','Heading','Roll','Aileron') if heading else ('H','\\theta','q','Height','Pitch','Elevator')
    sensor='AHRS / INS' if heading else 'Air data computer'
    return r'''\begin{center}
\resizebox{\textwidth}{!}{%
\begin{tikzpicture}
\node (in) at (-0.2,0) {$A_c$};
\node[sum] (s1) at (0.8,0) {$+$};
\node[block] (k1) at (2.2,0) {D law\\$K_A$ + limit};
\node[sum] (s2) at (3.8,0) {$+$};
\node[block] (k2) at (5,0) {$K_B$};
\node[sum] (s3) at (6.2,0) {$+$};
\node[block] (k3) at (7.5,0) {E rate\\controller};
\node[block] (act) at (9.5,0) {F\\servo};
\node[block] (plane) at (12,0) {Aircraft dynamics\\and kinematics};
\draw[arr] (in)--(s1);
\draw[arr] (s1)--node[above] {$e_A$}(k1);
\draw[arr] (k1)--node[above] {$B_c$}(s2);
\draw[arr] (s2)--(k2);
\draw[arr] (k2)--node[above] {$c_c$}(s3);
\draw[arr] (s3)--(k3);
\draw[arr] (k3)--(act);
\draw[arr] (act)--node[above] {$\delta$}(plane);
\draw[arr] (plane.east)--(14.2,0) node[right] {$A$};
\node[block] (rate) at (9.5,-1.3) {Rate gyro: $c$};
\node[block] (att) at (9.5,-2.5) {AHRS / INS: $B$};
\node[block] (height) at (9.5,-3.7) {SENSOR: $A$};
\draw[arr] (12,-0.43)--(12,-1.3)--(rate.east);
\draw[arr] (rate.west)-|node[pos=0.94,left] {$-$}(s3.south);
\draw[arr] (12.6,-0.43)--(12.6,-2.5)--(att.east);
\draw[arr] (att.west)-|node[pos=0.95,left] {$-$}(s2.south);
\draw[arr] (13.7,0)--(13.7,-3.7)--(height.east);
\draw[arr] (height.west)-|node[pos=0.96,left] {$-$}(s1.south);
\end{tikzpicture}}
\end{center}
'''.replace('SENSOR',sensor).replace('A',a).replace('B',b).replace('D',d).replace('E',e).replace('F',f).replace('$c', '$'+c).replace('AHRS', 'AHRS')
# Use token replacement rather than single-letter replacement inside words.
def diagram(heading=False):
    vals=([r'\psi',r'\phi','p','Heading','Roll','Aileron','AHRS / INS'] if heading else ['H',r'\theta','q','Height','Pitch','Elevator','Air data computer'])
    s=r'''\begin{center}
\resizebox{\textwidth}{!}{%
\begin{tikzpicture}
\node (in) at (-0.2,0) {$@A@_c$};
\node[sum] (s1) at (0.8,0) {$+$};
\node[block] (k1) at (2.2,0) {@D@ law\\$K_{@A@}$ + limit};
\node[sum] (s2) at (3.8,0) {$+$};
\node[block] (k2) at (5,0) {$K_{@B@}$};
\node[sum] (s3) at (6.2,0) {$+$};
\node[block] (k3) at (7.5,0) {@E@ rate\\controller};
\node[block] (act) at (9.5,0) {@F@\\servo};
\node[block] (plane) at (12,0) {Aircraft dynamics\\and kinematics};
\draw[arr] (in)--(s1);
\draw[arr] (s1)--node[above] {$e_{@A@}$}(k1);
\draw[arr] (k1)--node[above] {$@B@_c$}(s2);
\draw[arr] (s2)--(k2);
\draw[arr] (k2)--node[above] {$@C@_c$}(s3);
\draw[arr] (s3)--(k3);
\draw[arr] (k3)--(act);
\draw[arr] (act)--node[above] {$\delta$}(plane);
\draw[arr] (plane.east)--(14.2,0) node[right] {$@A@$};
\node[block] (rate) at (9.5,-1.3) {Rate gyro: $@C@$};
\node[block] (att) at (9.5,-2.5) {AHRS / INS: $@B@$};
\node[block] (height) at (9.5,-3.7) {@S@: $@A@$};
\draw[arr] (12,-0.43)--(12,-1.3)--(rate.east);
\draw[arr] (rate.west)-|node[pos=0.94,left] {$-$}(s3.south);
\draw[arr] (12.6,-0.43)--(12.6,-2.5)--(att.east);
\draw[arr] (att.west)-|node[pos=0.95,left] {$-$}(s2.south);
\draw[arr] (13.7,0)--(13.7,-3.7)--(height.east);
\draw[arr] (height.west)-|node[pos=0.96,left] {$-$}(s1.south);
\end{tikzpicture}}
\end{center}
'''
    for k,v in zip(['A','B','C','D','E','F','S'],vals): s=s.replace('@'+k+'@',v)
    return s
q1=r'''\section*{Question 1}
Please draw the block diagram of the altitude autopilot for an aircraft and then explain the functions of every part.

\textbf{Solution}

A typical altitude-hold autopilot uses an outer height loop, a pitch-attitude loop, and an inner pitch-rate loop. The diagram below shows a simplified FBW implementation [1, \S8.2.2]. Signals are perturbations about a trimmed flight condition.
'''+diagram()+r'''
\begin{enumerate}
\item \textbf{Reference and error comparison:} The selected altitude $H_c$ is compared with measured altitude $H$, giving $e_H=H_c-H$. Each summing junction subtracts its measured feedback from its command.
\item \textbf{Height law:} The gain $K_H$ converts height error into a pitch-attitude command, $\theta_c=K_He_H$. A limiter bounds the pitch command to avoid excessive manoeuvres.
\item \textbf{Pitch-attitude loop:} AHRS/INS measures $\theta$. The gain $K_\theta$ converts attitude error into demanded pitch rate: $q_c=K_\theta(\theta_c-\theta)$.
\item \textbf{Pitch-rate loop:} The rate gyro measures $q$. The rate controller acts on $q_c-q$ to produce a rapid, well-damped response and suppress pitch disturbances.
\item \textbf{Servo and aircraft:} The servo moves the elevator (or controlled tailplane). Aerodynamic forces and moments change pitch attitude, angle of attack, and flight path, thereby changing altitude.
\item \textbf{Altitude feedback:} The air data computer derives barometric altitude from static pressure. This closes the outer loop. The gyro and attitude outputs can come from the same inertial unit.
\end{enumerate}
For small flight-path angles and approximately constant speed $V$,
\[
\dot H=V\sin\gamma\approx V(\theta-\alpha),\qquad
H=H(0)+\int\dot H\,dt.
\]
Thus, when the aircraft is below the selected altitude, the system commands a climb and reduces the command as the error disappears. The inner loops must be faster than the height loop. Thrust/speed control maintains the energy needed for the manoeuvre.
'''
q2=r'''\newpage
\section*{Question 2}
Please draw the block diagram of the heading autopilot for an aircraft and then explain the functions of every part.

\textbf{Solution}

An aircraft normally changes heading by banking into a coordinated turn. A heading autopilot therefore uses an outer heading loop, a bank-angle loop, and an inner roll-rate loop [1, \S8.2.3].
'''+diagram(True)+r'''
\begin{enumerate}
\item \textbf{Heading reference and comparator:} The selected heading $\psi_c$ is compared with measured heading $\psi$. The error is wrapped to $(-180^\circ,180^\circ]$ so that crossing north does not produce a nearly full-circle turn command.
\item \textbf{Heading law and bank limiter:} $\phi_c=\operatorname{sat}(K_\psi e_\psi)$ converts heading error into bank-angle demand. The limiter restricts bank angle and manoeuvre severity.
\item \textbf{Bank-angle loop:} AHRS/INS supplies $\phi$. The gain $K_\phi$ generates the roll-rate command $p_c=K_\phi(\phi_c-\phi)$.
\item \textbf{Roll-rate loop:} A rate gyro measures $p$. The controller uses $p_c-p$ to give a fast, well-damped roll response and resist disturbances.
\item \textbf{Aileron servo:} The actuator converts the electrical command into aileron deflection $\delta_a$, producing a rolling moment. Some aircraft also use spoilers.
\item \textbf{Aircraft and heading feedback:} Bank tilts the lift vector and produces the lateral force required for a turn. The AHRS/INS heading output closes the outer loop. Sensor blocks are shown separately for clarity.
\end{enumerate}
For a steady, coordinated, approximately level turn at speed $V$,
\[
\dot\psi=\frac{g}{V}\tan\phi\approx\frac{g}{V}\phi
\quad\text{for small }\phi.
\]
As heading approaches its command, the demanded bank returns toward zero and the aircraft rolls level. A yaw damper/rudder coordination function suppresses sideslip; the pitch/altitude loop compensates for the loss of vertical lift during banking. Heading hold alone does not hold a ground track in crosswind.
'''
q3=r'''\newpage
\section*{Question 3}
Please describe the relationship between stability margin and neutral point.

\textbf{Solution}

Here, stability margin means the \textbf{longitudinal static margin}. The neutral point (NP) is the centre-of-gravity location at which the pitching-moment coefficient does not change with a small change in angle of attack:
\[
C_{m_\alpha}=\frac{\partial C_m}{\partial\alpha}=0.
\]
Let $x_{CG}$ and $x_{NP}$ be measured aft from the same reference, and let $\bar c$ be the mean aerodynamic chord. The nondimensional positions are $h=x_{CG}/\bar c$ and $h_n=x_{NP}/\bar c$. Then
\[
\boxed{SM=h_n-h=\frac{x_{NP}-x_{CG}}{\bar c}.}
\]
Using positive nose-up pitching moment and $C_{L_\alpha}>0$, the linear relation is
\[
\boxed{C_{m_\alpha}=C_{L_\alpha}(h-h_n)=-C_{L_\alpha}SM.}
\]
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[arr] (0,0)--(11,0) node[right]{Aft};
\draw (3,-0.15)--(3,0.2) node[above]{CG};
\draw (7,-0.15)--(7,0.2) node[above]{NP};
\draw[<->] (3,-0.65)--node[below]{$x_{NP}-x_{CG}>0$}(7,-0.65);
\end{tikzpicture}
\end{center}
\begin{itemize}
\item \textbf{$SM>0$: CG ahead of NP.} An increase in $\alpha$ produces a restoring nose-down pitching moment. The aircraft is longitudinally statically stable.
\item \textbf{$SM=0$: CG at NP.} There is no first-order restoring moment due to $\alpha$. The aircraft is neutrally stable in this static sense.
\item \textbf{$SM<0$: CG behind NP.} An increase in $\alpha$ produces a nose-up moment that tends to increase the disturbance. The unaugmented aircraft is statically unstable.
\end{itemize}
For example, if the NP is at $40\%$ MAC and the CG at $30\%$ MAC, then $SM=0.10$, or $10\%$ MAC. Moving the CG aft toward the NP reduces static stability and generally reduces the control effort required to manoeuvre. A larger positive margin increases restoring tendency, but can increase trim and control demands.

The NP depends on the aircraft configuration and on whether the controls are fixed or free. A stick-free analysis must use the stick-free NP, which is generally farther forward for a conventional freely floating elevator. Static margin describes the initial restoring tendency; it does not by itself guarantee adequate dynamic damping or closed-loop gain and phase margins [1, Ch.~3; 2].
'''
q4=r'''\newpage
\section*{Question 4}
Describe the differences between MCAS (Maneuvering Characteristic Augmentation System) and SAS (Stability Augmentation System) of longitudinal motion.

\textbf{Solution}

Both systems automatically modify longitudinal control, but their primary objectives and control actions differ.

\textbf{MCAS} on the Boeing 737 MAX is a specific handling-quality augmentation function. It reduces the high-angle-of-attack pitch-up tendency and provides the intended pitch handling characteristics. It operates under defined conditions: manual flight, flaps retracted, and elevated angle of attack. Its corrective action is a nose-down command through the horizontal-stabilizer trim system [3].

\textbf{Longitudinal SAS} is a general class of feedback systems that improves pitch stability and damping. A typical pitch damper senses pitch rate $q$ and commands the elevator or tailplane so that the resulting moment opposes unwanted pitch motion. More advanced SAS can also use angle of attack and normal acceleration, with gains scheduled by flight condition [1, \S3.8].

\small
\begin{tabular}{@{}P{2.5cm}P{6.0cm}P{6.8cm}@{}}
\toprule
Feature & MCAS (737 MAX) & Longitudinal SAS \\
\midrule
Main objective & Shape high-AOA pitch handling and reduce pitch-up tendency. & Improve stability and damp unwanted longitudinal motion, especially short-period oscillation. \\
\addlinespace
Key inputs & AOA and flight-condition/enabling information. & Typically pitch rate; possibly AOA and normal acceleration. \\
\addlinespace
Control action & Commands nose-down stabilizer trim when its activation conditions are met. & Modulates elevator/tailplane to create stabilizing moments; correction can be in either direction. \\
\addlinespace
Operating scope & A specific augmentation law active in a restricted flight regime. & A broader stabilization function operating throughout its designed and enabled envelope. \\
\addlinespace
Autopilot relation & Operates in manual flight, rather than tracking an autopilot altitude command. & Can support manual flight and provide an inner stabilization loop for an autopilot. \\
\bottomrule
\end{tabular}
\normalsize

With $M$ positive nose-up, the idealized moment contribution of a pitch-rate damper is
\[
M_{\mathrm{SAS}}=-K_q q,\qquad K_q>0.
\]
Thus a nose-up angular rate generates a nose-down damping moment. The required surface-deflection sign depends on the aircraft's aerodynamic sign convention.

MCAS belongs broadly to augmentation, but is not simply a conventional pitch-rate damper or an altitude-hold autopilot. It should also not be described as a complete stall-prevention system. In Boeing's updated MCAS design, both AOA inputs are compared, activation is limited to one input per elevated-AOA event, and command authority is limited so the pilot can counter it [3].
'''
q5=r'''\newpage
\section*{Question 5}
Explain what is triple redundant system and compare the differences between quadruplex and triple redundant systems.

\textbf{Solution}

A \textbf{triple redundant (triplex) system} has three parallel channels performing the same function. Their outputs are compared, and a majority vote or suitable signal-selection algorithm supplies the usable output. For example, if channels A and B agree while C differs beyond an allowed tolerance, C can be identified and isolated. For continuous sensor signals, a median selector can reject an extreme erroneous value.

\begin{center}
\begin{tikzpicture}[node distance=1cm]
\node[block] (a) at (0,1.1) {Channel A};
\node[block] (b) at (0,0) {Channel B};
\node[block] (c) at (0,-1.1) {Channel C};
\node[block] (v) at (4,0) {Cross-comparison\\voting / selection\\and fault isolation};
\node (o) at (8,0) {Control output};
\draw[arr] (a.east)--(v.north west);
\draw[arr] (b.east)--(v.west);
\draw[arr] (c.east)--(v.south west);
\draw[arr] (v.east)--(o.west);
\end{tikzpicture}
\end{center}

\small
\begin{tabular}{@{}P{3.0cm}P{5.9cm}P{6.4cm}@{}}
\toprule
Feature & Basic triplex & Quadruplex \\
\midrule
Channel count & Three. & Four. \\
\addlinespace
First independent failure & Two healthy channels identify the outlier; isolate it and retain two. & Three healthy channels identify the outlier; isolate it and retain three. \\
\addlinespace
Second sequential failure & Two remaining channels can disagree, but comparison alone cannot tell which is correct. & After the first failed channel is removed, two of the remaining three identify the next outlier; two healthy channels remain. \\
\addlinespace
Typical failure survival & One arbitrary channel failure using voting alone. & Two sequential, independently detectable failures with timely isolation. \\
\addlinespace
Implementation tradeoff & Less channel hardware, weight, and power. & More hardware and interconnection, but retains voting after the first failure. \\
\bottomrule
\end{tabular}
\normalsize

\textbf{Important distinction: monitored triplex.} If each channel has sufficiently reliable independent, dissimilar monitoring, a failed channel can be identified without relying only on inter-channel voting. A monitored triplex system can therefore survive two detectable failures and continue on one healthy channel [1, \S4.4.2]. This capability does not follow from having three channels alone.

Quadruplex survival also requires isolating the first failure before a second creates a two-good/two-bad split; it does not guarantee tolerance of any two simultaneous arbitrary failures. Both architectures require suitable redundancy in sensors, actuators, and power supplies, fault containment, and reliable selection logic. Identical software errors or a shared power failure may defeat multiple channels together [1, \S4.4; 4].

\newpage
\section*{References}
\begin{enumerate}[label={[\arabic*]}]
\item R. P. G. Collinson, \textit{Introduction to Avionics Systems}, 3rd ed., 2011. Course textbook: Ch.~3 (static stability and SAS), \S4.4 (redundancy), and \S\S8.2.1--8.2.3 (autopilot control). The autopilot diagrams are simplified redrawings of the control structure described in these sections.
\item CA7528, \textit{Digital Avionics Handout \#3}, updated September 23, 2026, slides 57--60 (neutral point and longitudinal static stability).
\item Boeing, \textit{737 MAX Software Update}, sections ``Overview'' and ``Key Definitions.''\\
\href{https://www.boeing.com/commercial/737max/737-max-update/737-max-software-updates}{Boeing: 737 MAX software update and MCAS protections}.
\item CA7528, \textit{Digital Avionics Handout \#5: FBW}, September 30, 2026, redundancy and system-architecture material.
\end{enumerate}
\end{document}
'''
Path('HW2/digitalAvionics_hw2_solutions.tex').write_text(head+q1+q2+q3+q4+q5,encoding='utf-8')
