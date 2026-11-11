from pathlib import Path
from PIL import Image
import re
root=Path('tmp/pdfs')
for src,box,out in [('crop-altitude-430.png',(120,130,930,625),'altitude'),('crop-heading-432.png',(120,135,930,535),'heading'),('crop-redundancy-41.png',(115,265,1260,780),'redundancy')]:
 im=Image.open(root/src); im.crop(tuple(int(v*2) for v in box)).save('HW2/images/'+out+'.png')
p=Path('HW2/digitalAvionics_hw2_solutions.tex');s=p.read_text(encoding='utf-8')
for q,name,width in [(1,'altitude','12.0cm'),(2,'heading','14cm'),(5,'redundancy','12cm')]:
 start=s.index('\\section*{Question '+str(q)+'}')
 a=s.index('\\begin{center}',start); b=s.index('\\end{center}',a)+len('\\end{center}')
 s=s[:a]+'\\begin{center}\n\\includegraphics[width='+width+']{HW2/images/'+name+'.png}\n\\end{center}'+s[b:]
a=s.index('The altitude autopilot keeps');b=s.index('\\newpage',a)
image=s[s.index('\\begin{center}',a):s.index('\\end{center}',a)+len('\\end{center}')]
s=s[:a]+r'''The altitude autopilot adjusts pitch to keep the selected altitude. The inner pitch-rate and pitch-attitude loops respond faster than the outer altitude loop.
'''+image+r'''
\begin{enumerate}[itemsep=0.1em,topsep=0.2em]
\item \textbf{Altitude command and feedback:} $H_{\mathrm{Ref}}$ is the selected altitude. The air data system (ADS) measures altitude $H$ and vertical speed $\dot H$. The $K_{\dot H}\dot H$ feedback helps reduce overshoot during a climb or descent.
\item \textbf{Height gain $K_H$:} The altitude error is converted to a pitch command:
$\theta_D=K_H(H_{\mathrm{Ref}}-H-K_{\dot H}\dot H)$.
\item \textbf{Attitude loop:} The AHRS measures pitch angle $\theta$. The gain $K_\theta$ gives the pitch-rate command $q_D=K_\theta(\theta_D-\theta)$.
\item \textbf{Rate loop:} The pitch-rate gyro measures $q$. The gain $K_q$ acts on $q_D-q$ to make the pitch response fast and well damped.
\item \textbf{Servo and aircraft dynamics:} The servo moves the tailplane/elevator by angle $\eta$. This changes the aircraft's pitch rate, pitch angle, and angle of attack $\alpha$.
\item \textbf{Flight-path kinematics:} Pitch and angle of attack determine the flight-path angle. For small angles and nearly constant speed $V$,
$\dot H\approx V(\theta-\alpha)$. Integrating vertical speed gives altitude, which is fed back through the ADS.
\end{enumerate}
If the aircraft is below the selected altitude, the system commands a climb. As it approaches the target, the feedback reduces the pitch command so that it levels off. Thrust/speed control maintains the required airspeed.
'''+s[b:]
a=s.index('The heading autopilot turns');b=s.index('\\newpage',a)
image=s[s.index('\\begin{center}',a):s.index('\\end{center}',a)+len('\\end{center}')]
s=s[:a]+r'''The heading autopilot turns the aircraft toward the selected heading by controlling bank angle. In the diagram, $\Psi$ is heading, $\Phi$ is bank angle, and $p$ is roll rate.
'''+image+r'''
\begin{enumerate}
\item \textbf{Heading command and $K_\Psi$:} The selected heading $\Psi_{\mathrm{Ref}}$ is compared with measured heading. The controller gives $\Phi_D=K_\Psi\Psi_e$. The error is taken in the shorter direction; for example, $350^\circ$ to $10^\circ$ is a $20^\circ$ right turn.
\item \textbf{Bank-angle controller $K_\Phi$:} The AHRS measures $\Phi$. The bank error produces a roll-rate command $p_D=K_\Phi(\Phi_D-\Phi)$.
\item \textbf{Roll-rate controller $K_p$:} The roll-rate gyro measures $p$. Feedback of $p_D-p$ gives a fast, well-damped roll response.
\item \textbf{Aileron servo and aircraft dynamics:} The servo moves the ailerons by angle $\xi$. The resulting rolling moment changes roll rate and bank angle.
\item \textbf{Flight-path kinematics:} Banking tilts the lift vector and causes a turn. For a coordinated level turn at forward speed $u$,
\[
\dot\Psi=\frac{g}{u}\tan\Phi\approx\frac{g}{u}\Phi
\quad\text{for small }\Phi.
\]
The $g/u$ block and integrator convert bank angle into heading.
\item \textbf{AHRS feedback:} The AHRS supplies bank angle and heading to the two outer comparison points. These measurements let the autopilot correct the remaining error.
\end{enumerate}
As the heading error decreases, the commanded bank angle returns toward zero and the aircraft rolls level. Rudder coordination helps reduce sideslip, while the altitude loop maintains height. Practical systems also limit bank commands. Holding heading alone does not hold ground track in a crosswind.
'''+s[b:]
start=s.index('\\section*{Question 5}')
a=s.index('\\begin{center}',start)
s=s[:a]+'The diagram below shows the four parallel channels of a quadruplex system.\n\n'+s[a:]
p.write_text(s,encoding='utf-8')
