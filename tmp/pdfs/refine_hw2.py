from pathlib import Path
p=Path('HW2/digitalAvionics_hw2_solutions.tex')
s=p.read_text(encoding='utf-8').replace('P{6.8cm}','P{6.6cm}').replace('P{6.4cm}','P{6.2cm}')
a=s.index('\\begin{enumerate}',s.index('\\section*{Question 1}'))
b=s.index('\\newpage',a)
s=s[:a]+r'''\begin{enumerate}[itemsep=0.15em,topsep=0.2em]
\item \textbf{Reference and comparators:} The pilot selects $H_c$. The outer comparator forms $e_H=H_c-H$; the inner comparators subtract measured attitude and rate from their respective commands.
\item \textbf{Height law:} $\theta_c=K_He_H$ converts altitude error into pitch demand. The limiter prevents excessive pitch commands.
\item \textbf{Attitude loop:} AHRS/INS measures $\theta$. The gain generates demanded pitch rate $q_c=K_\theta(\theta_c-\theta)$.
\item \textbf{Rate loop:} The gyro measures $q$. The rate controller acts on $q_c-q$ to produce a fast, well-damped pitch response.
\item \textbf{Servo and aircraft:} The servo moves the elevator/tailplane. The resulting aerodynamic forces and moments change attitude and flight path, and hence altitude.
\item \textbf{Altitude sensor:} The air data computer derives barometric altitude from static pressure and closes the height loop. The attitude and rate sensors can share one inertial unit.
\end{enumerate}
For small flight-path angles and approximately constant speed $V$,
\[
\dot H=V\sin\gamma\approx V(\theta-\alpha),\qquad
H=H(0)+\int\dot H\,dt.
\]
If altitude is too low, the autopilot commands a climb and reduces the command as the error disappears. Inner loops must respond faster than the height loop. Thrust/speed control maintains the energy required for the manoeuvre.

'''+s[b:]
s=s.replace('at (9.5,-1.3)','at (9.5,-1.0)').replace('(12,-1.3)','(12,-1.0)').replace('at (9.5,-2.5)','at (9.5,-2.0)').replace('(12.6,-2.5)','(12.6,-2.0)').replace('at (9.5,-3.7)','at (9.5,-3.0)').replace('(13.7,-3.7)','(13.7,-3.0)')
p.write_text(s,encoding='utf-8')
