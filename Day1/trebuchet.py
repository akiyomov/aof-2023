import re

with open("input.txt") as f:
    text = f.read().strip()

def fl_number(text):
    fl = text.split("\n")
    ns = [re.findall("\d", x) for x in fl]
    return sum(int(n[0] + n[-1]) for n in ns)

print(fl_number(text))
# result Total Calibration: 54667