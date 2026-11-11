from pathlib import Path
import re
p=Path('HW2/digitalAvionics_hw2_solutions.tex')
s=p.read_text(encoding='utf-8')
s=s.split('\\newpage\n\\section*{References}')[0]+'\\end{document}\n'
s=re.sub(r' \[(?:1|3)[^\]]*\]', '', s)
s=s.replace('A typical altitude-hold autopilot uses an outer height loop, a pitch-attitude loop, and an inner pitch-rate loop. The diagram below shows a simplified FBW implementation. Signals are perturbations about a trimmed flight condition.', 'The altitude autopilot keeps the aircraft at the selected altitude by adjusting its pitch. It has an altitude loop outside the pitch-attitude and pitch-rate loops. The diagram shows small changes from steady, trimmed flight.')
s=s.replace('Reference and comparators:', 'Altitude command and comparison:').replace('The outer comparator forms $e_H=H_c-H$; the inner comparators subtract measured attitude and rate from their respective commands.', 'The difference between the selected and measured altitude is $e_H=H_c-H$. The other two comparison points work in the same way for pitch angle and pitch rate.')
s=s.replace('converts altitude error into pitch demand.', 'gives the pitch angle needed to correct the altitude error.').replace('The resulting aerodynamic forces and moments change attitude and flight path, and hence altitude.', 'This changes the pitch and flight path, causing the aircraft to climb or descend.')
s=s.replace('An aircraft normally changes heading by banking into a coordinated turn. A heading autopilot therefore uses an outer heading loop, a bank-angle loop, and an inner roll-rate loop.', 'The heading autopilot turns the aircraft toward the selected heading. It does this by controlling the bank angle, with a roll-rate loop inside the bank-angle loop.')
s=s.replace('The error is wrapped to $(-180^\\circ,180^\\circ]$ so that crossing north does not produce a nearly full-circle turn command.', 'The heading error is taken in the shorter direction. For example, changing from $350^\\circ$ to $10^\\circ$ requires a $20^\\circ$ right turn.')
s=s.replace('The limiter restricts bank angle and manoeuvre severity.', 'The limiter keeps the commanded bank angle within a suitable range.')
s=s.replace('A yaw damper/rudder coordination function suppresses sideslip; the pitch/altitude loop compensates for the loss of vertical lift during banking. Heading hold alone does not hold a ground track in crosswind.', 'The rudder helps keep the turn coordinated, while the altitude loop adjusts pitch to maintain height. In a crosswind, holding heading does not necessarily keep the aircraft on the same ground track.')
s=s.replace('Here, stability margin means the \\textbf{longitudinal static margin}.', 'The stability margin here is the \\textbf{longitudinal static margin}, which tells us how far the CG is ahead of the neutral point.')
s=s.replace('The unaugmented aircraft is statically unstable.', 'Without stability augmentation, the aircraft is statically unstable.')
a=s.index('The NP depends on the aircraft configuration')
b=s.index('\\newpage',a)
s=s[:a]+'''The neutral point can change with the aircraft configuration and whether the elevator is fixed or free. The same condition must be used when calculating the static margin. A positive static margin means there is a restoring tendency, but it does not tell us how quickly an oscillation will die out.
'''+s[b:]
a=s.index('Both systems automatically modify longitudinal control')
b=s.index('\\newpage',a)
s=s[:a]+r'''MCAS and longitudinal SAS both affect the aircraft's pitch motion, but they are used for different purposes.

\textbf{MCAS} is used on the Boeing 737 MAX to reduce the pitch-up tendency at high angle of attack and give the aircraft the intended handling characteristics. It works during manual flight with the flaps up when the angle of attack is high. It commands nose-down stabilizer trim.

\textbf{SAS} improves the aircraft's stability and damping. For example, a pitch-rate gyro detects an unwanted pitching motion, and the SAS moves the elevator or tailplane to oppose it. This helps reduce pitch oscillations after a disturbance.

The main differences are:
\begin{enumerate}
\item \textbf{Purpose:} MCAS mainly changes the handling characteristics at high angle of attack. SAS mainly improves stability and reduces unwanted motion.
\item \textbf{Input:} MCAS uses angle of attack and flight-condition information. A basic longitudinal SAS uses pitch rate $q$. More advanced SAS may also use angle of attack or normal acceleration.
\item \textbf{Output:} MCAS commands nose-down stabilizer trim when its operating conditions are met. SAS commands elevator or tailplane movement in the direction needed to oppose the disturbance.
\item \textbf{Operation:} MCAS works only under specific conditions. SAS provides feedback while it is engaged within its designed operating range, and can also work as an inner loop for an autopilot.
\end{enumerate}
For a simple pitch damper, the stabilizing moment can be represented by
\[
M_{\mathrm{SAS}}=-K_q q,\qquad K_q>0,
\]
where nose-up moment and pitch rate are positive. When the aircraft pitches up, the SAS produces a nose-down moment. When it pitches down, the correction is in the opposite direction.

Therefore, MCAS is a specific handling-augmentation function, while SAS is a more general stability-augmentation system. MCAS is not an altitude-hold autopilot or a complete stall-prevention system.
'''+s[b:]
s=s.replace('Their outputs are compared, and a majority vote or suitable signal-selection algorithm supplies the usable output. For example, if channels A and B agree while C differs beyond an allowed tolerance, C can be identified and isolated. For continuous sensor signals, a median selector can reject an extreme erroneous value.', 'The system compares their outputs and uses majority voting to reject a faulty channel. For example, if A and B give similar outputs but C gives a very different output, C is treated as faulty and disconnected. The other two channels can continue operating.')
s=s.replace('Two healthy channels identify the outlier; isolate it and retain two.', 'Two good channels agree, so the faulty one can be disconnected. Two channels remain.').replace('Three healthy channels identify the outlier; isolate it and retain three.', 'Three good channels agree, so the faulty one can be disconnected. Three channels remain.').replace('After the first failed channel is removed, two of the remaining three identify the next outlier; two healthy channels remain.', 'After the first faulty channel is removed, the remaining three can vote again. A second faulty channel can be removed, leaving two.').replace('One arbitrary channel failure using voting alone.', 'One channel failure by majority voting.').replace('Two sequential, independently detectable failures with timely isolation.', 'Two separate failures, if each is detected and disconnected in time.').replace('Implementation tradeoff', 'Weight and cost').replace('Less channel hardware, weight, and power.', 'Less hardware, weight, power use, and cost.').replace('More hardware and interconnection, but retains voting after the first failure.', 'More hardware, weight, and cost, but voting is still available after the first failure.')
a=s.index('\\textbf{Important distinction: monitored triplex.}')
s=s[:a]+r'''A \textbf{monitored triplex} system is different from basic triplex voting. Each channel has an independent monitor that can identify its own failure. If these monitors are reliable enough, two faulty channels can be disconnected and the system can continue with one good channel.

For quadruplex, the first faulty channel must be removed before the second failure creates a two-against-two situation. Thus, four channels do not automatically protect against any two simultaneous failures. Both systems also need independent power supplies and suitable sensor and actuator redundancy. A common software error or a shared power failure can affect several channels at once.
\end{document}
'''
p.write_text(s,encoding='utf-8')
