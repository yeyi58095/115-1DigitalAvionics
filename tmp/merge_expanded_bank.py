from pathlib import Path
from math import sqrt, tan, pi, cos

root = Path(__file__).resolve().parents[1]
bank = root / 'flashcard_app/alias.txt'
original = bank.read_text(encoding='utf-8-sig')
extra = (root / 'tmp/expanded_questions.txt').read_text(encoding='utf-8')
assert '[11 ' not in original, 'Already merged: refusing to duplicate cards'
assert sum(line.startswith('? ') for line in extra.splitlines()) == 300
assert sum(line.startswith('[') for line in extra.splitlines()) == 20
combined = original.rstrip() + '\n\n' + extra.strip() + '\n'
for target in [bank, root / 'alias.txt']:
    target.write_text(combined, encoding='utf-8')
print('Merged 152 + 300 = 452 cards in 30 units.')
print('Sea-level stall speed:', sqrt(2*30000*9.81/(1.225*75*1.2)))
print('High-altitude stall speed:', sqrt(2*30000*9.81/(0.4583*75*1.2)))
print('Turn deg/s:', 9.81*tan(20*pi/180)/100*180/pi)
print('Longitude increment deg:', 80*60/(6.371e6*cos(25*pi/180))*180/pi)
