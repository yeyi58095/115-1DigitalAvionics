from pathlib import Path
p=Path('HW2/digitalAvionics_hw2_solutions.tex');s=p.read_text(encoding='utf-8')
s=s.replace('\\setlength{\\parskip}{0.5em}','\\setlength{\\parskip}{0.3em}')
s=s.replace('align=center,font=\\small','align=center,font=\\footnotesize')
s=s.replace('Aircraft dynamics\\\\and kinematics','Aircraft\\dynamics / kinematics') if False else s
s=s.replace('Aircraft dynamics\\\\and kinematics','Aircraft\\\\+ kinematics')
s=s.replace('Pitch rate\\\\controller','Pitch-rate\\\\law').replace('Roll rate\\\\controller','Roll-rate\\\\law')
s=s.replace('(12,-0.43)','([xshift=-4mm]plane.south)').replace('(12.6,-0.43)','([xshift=4mm]plane.south)')
s=s.replace('If altitude is too low, the autopilot commands a climb and reduces the command as the error disappears. Inner loops must respond faster than the height loop. Thrust/speed control maintains the energy required for the manoeuvre.', 'Below the selected altitude, the system commands a climb. The inner loops are faster than the height loop; thrust/speed control maintains the required energy.')
p.write_text(s,encoding='utf-8')
