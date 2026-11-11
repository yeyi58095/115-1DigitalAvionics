from pathlib import Path
p=Path('HW2/digitalAvionics_hw2_solutions.tex'); s=p.read_text(encoding='utf-8')
s=s.replace('\\maketitle\n\\begin{center}CA7528\\quad Fall 2026\\end{center}',r'''\begin{center}
{\LARGE Digital Avionics --- Homework 2}\\[0.7em]
葉彥辰\quad P46154345\\[0.4em]
CA7528\quad Fall 2026
\end{center}''')
for name,width in [('k1','1.5cm'),('k2','0.65cm'),('k3','1.5cm'),('act','1.5cm'),('plane','2.4cm')]:
 s=s.replace('\\node[block] ('+name+')','\\node[block,text width='+width+'] ('+name+')')
s=s.replace('node[above] {$e_', 'node[above=5pt] {$e_').replace('node[above] {$\\theta_c$}', 'node[above=5pt] {$\\theta_c$}').replace('node[above] {$\\phi_c$}', 'node[above=5pt] {$\\phi_c$}').replace('node[above] {$\\delta$}', 'node[above=5pt] {$\\delta$}')
p.write_text(s,encoding='utf-8')
