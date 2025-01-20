"""
Sample input:

Test Case                      buch       | F4         | GB
----------------------------------------------------------------------
FK2.in                         0.00s      | 0.01s      | 1.70s
FK3.in                         0.00s      | 0.01s      | 0.80s
FK4.in                         0.01s      | 0.08s      | 0.87s
tri1.in                        0.26s      | 0.08s      | 0.98s
tri10.in                       0.01s      | 0.01s      | 0.85s
tri11.in                       0.03s      | 0.02s      | 0.88s
tri12.in                       3.27s      | 0.21s      | 1.04s
tri13.in                       0.01s      | 0.01s      | 0.83s
tri2.in                        6.01s      | 0.29s      | 1.16s
tri3.in                        0.02s      | 0.04s      | 0.90s
tri4.in                        0.04s      | 0.07s      | 0.94s
tri5.in                        0.01s      | 0.02s      | 0.87s
tri6.in                        6.53s      | 1.78s      | 1.27s
tri7.in                        33.33s     | 1.81s      | 1.45s
tri8.in                        0.09s      | 0.06s      | 0.91s
tri9.in                        0.00s      | 0.01s      | 0.82s
trit3.in                       0.01s      | 0.05s      | 0.87s
trit4.in                       0.14s      | 0.49s      | 1.04s
trit5.in                       77.16s     | 207.84s    | 5.21s
"""

import sys


input()
input()

lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

data: list[tuple[str, str, str, str]] = []

for line in lines:
    name, buch, _, f4, _, gb = line.split()
    name = name.split('.')[0]
    buch = buch[:-1]
    f4 = f4[:-1]
    gb = gb[:-1]
    data.append((name, buch, f4, gb))

out: str = ""

out += "\\addplot coordinates {"
for name, buch, f4, gb in data:
    out += f"({name}, {buch}) "
out = out[:-1]
out += "};\n"

out += "\\addplot coordinates {"
for name, buch, f4, gb in data:
    out += f"({name}, {f4}) "
out = out[:-1]
out += "};\n"

out += "\\addplot coordinates {"
for name, buch, f4, gb in data:
    out += f"({name}, {gb}) "
out = out[:-1]
out += "};\n"

print(out)
