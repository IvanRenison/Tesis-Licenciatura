"""
Sample input:

Test Case                      1 threads  | 2 threads  | 4 threads  | 6 threads  | 8 threads  | 16 threads
-------------------------------------------------------------------------------------------------------------
FK2.in                         0.00s      | 0.00s      | 0.00s      | 0.00s      | 0.00s      | 0.00s
FK3.in                         0.00s      | 0.00s      | 0.00s      | 0.00s      | 0.00s      | 0.00s
FK4.in                         0.07s      | 0.06s      | 0.06s      | 0.06s      | 0.07s      | 0.07s
tri1.in                        0.10s      | 0.08s      | 0.07s      | 0.06s      | 0.06s      | 0.06s
tri10.in                       0.01s      | 0.01s      | 0.01s      | 0.01s      | 0.01s      | 0.01s
tri11.in                       0.02s      | 0.02s      | 0.01s      | 0.01s      | 0.01s      | 0.01s
tri12.in                       0.32s      | 0.28s      | 0.22s      | 0.22s      | 0.20s      | 0.20s
tri13.in                       0.01s      | 0.00s      | 0.00s      | 0.01s      | 0.00s      | 0.00s
tri2.in                        0.53s      | 0.42s      | 0.36s      | 0.32s      | 0.31s      | 0.29s
tri3.in                        0.03s      | 0.03s      | 0.03s      | 0.03s      | 0.03s      | 0.03s
tri4.in                        0.07s      | 0.06s      | 0.06s      | 0.06s      | 0.06s      | 0.05s
tri5.in                        0.01s      | 0.01s      | 0.01s      | 0.01s      | 0.01s      | 0.01s
tri6.in                        2.20s      | 1.98s      | 1.82s      | 1.86s      | 1.83s      | 1.79s
tri7.in                        2.19s      | 2.02s      | 1.92s      | 1.84s      | 1.81s      | 1.80s
tri8.in                        0.07s      | 0.06s      | 0.06s      | 0.05s      | 0.05s      | 0.05s
tri9.in                        0.00s      | 0.00s      | 0.00s      | 0.00s      | 0.00s      | 0.00s
trit3.in                       0.04s      | 0.04s      | 0.04s      | 0.04s      | 0.04s      | 0.04s
trit4.in                       0.47s      | 0.47s      | 0.45s      | 0.45s      | 0.45s      | 0.46s
trit5.in                       213.58s    | 212.76s    | 209.93s    | 212.14s    | 208.28s    | 208.62s
"""

import sys


input()
input()

lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

data: list[tuple[str, str, str, str, str, str, str]] = []

for line in lines:
    name, th1, _, th2, _, th4, _, th6, _, th8, _, th16 = line.split()
    name = name.split('.')[0]
    th1 = th1[:-1]
    th2 = th2[:-1]
    th4 = th4[:-1]
    th6 = th6[:-1]
    th8 = th8[:-1]
    th16 = th16[:-1]
    data.append((name, th1, th2, th4, th6, th8, th16))

out: str = ""

out += "\\addplot coordinates {"
for name, th1, th2, th4, th6, th8, th16 in data:
    out += f"({name}, {th1}) "
out = out[:-1]
out += "};\n"

out += "\\addplot coordinates {"
for name, th1, th2, th4, th6, th8, th16 in data:
    out += f"({name}, {th2}) "
out = out[:-1]
out += "};\n"

out += "\\addplot coordinates {"
for name, th1, th2, th4, th6, th8, th16 in data:
    out += f"({name}, {th4}) "
out = out[:-1]
out += "};\n"

out += "\\addplot coordinates {"
for name, th1, th2, th4, th6, th8, th16 in data:
    out += f"({name}, {th6}) "
out = out[:-1]
out += "};\n"

out += "\\addplot coordinates {"
for name, th1, th2, th4, th6, th8, th16 in data:
    out += f"({name}, {th8}) "
out = out[:-1]
out += "};\n"

out += "\\addplot coordinates {"
for name, th1, th2, th4, th6, th8, th16 in data:
    out += f"({name}, {th16}) "
out = out[:-1]
out += "};\n"

print(out)
