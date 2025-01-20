"""
./Buchberger.run < ../commonTestCases/testCases/FK2.in
Normal time: 0ms
Reconstruction time: 0ms
./Buchberger.run < ../commonTestCases/testCases/FK3.in
Normal time: 0ms
Reconstruction time: 0ms
./Buchberger.run < ../commonTestCases/testCases/FK4.in
Normal time: 7ms
Reconstruction time: 11ms
./Buchberger.run < ../commonTestCases/testCases/tri1.in
Normal time: 238ms
Reconstruction time: 383ms
./Buchberger.run < ../commonTestCases/testCases/tri10.in
Normal time: 6ms
Reconstruction time: 7ms
./Buchberger.run < ../commonTestCases/testCases/tri11.in
Normal time: 26ms
Reconstruction time: 35ms
./Buchberger.run < ../commonTestCases/testCases/tri12.in
Normal time: 2990ms
Reconstruction time: 4260ms
./Buchberger.run < ../commonTestCases/testCases/tri13.in
Normal time: 5ms
Reconstruction time: 16ms
./Buchberger.run < ../commonTestCases/testCases/tri2.in
Normal time: 5497ms
Reconstruction time: 8544ms
./Buchberger.run < ../commonTestCases/testCases/tri3.in
Normal time: 16ms
Reconstruction time: 22ms
./Buchberger.run < ../commonTestCases/testCases/tri4.in
Normal time: 30ms
Reconstruction time: 52ms
./Buchberger.run < ../commonTestCases/testCases/tri5.in
Normal time: 6ms
Reconstruction time: 9ms
./Buchberger.run < ../commonTestCases/testCases/tri6.in
Normal time: 5929ms
Reconstruction time: 7749ms
./Buchberger.run < ../commonTestCases/testCases/tri7.in
Normal time: 30415ms
Reconstruction time: 101729ms
./Buchberger.run < ../commonTestCases/testCases/tri8.in
Normal time: 83ms
Reconstruction time: 113ms
./Buchberger.run < ../commonTestCases/testCases/tri9.in
Normal time: 0ms
Reconstruction time: 1ms
./Buchberger.run < ../commonTestCases/testCases/trit3.in
Normal time: 8ms
Reconstruction time: 11ms
./Buchberger.run < ../commonTestCases/testCases/trit4.in
Normal time: 126ms
Reconstruction time: 173ms
./Buchberger.run < ../commonTestCases/testCases/trit5.in
Normal time: 70421ms
Reconstruction time: 94521ms
"""

import sys

lines: list[str] = []
for line in sys.stdin:
    lines.append(line.strip())

data: list[tuple[str, str, str]] = []

for i in range(0, len(lines), 3):
    name = lines[i].split('/')[-1].split('.')[0]
    normal = lines[i+1].split()[-1][:-2]
    reconstruction = lines[i+2].split()[-1][:-2]
    normal = str(float(normal) / 1000)
    reconstruction = str(float(reconstruction) / 1000)
    data.append((name, normal, reconstruction))

out: str = ""

out += "\\addplot coordinates {"
for name, normal, reconstruction in data:
    out += f"({name}, {normal}) "
out = out[:-1]
out += "};\n"

out += "\\addplot coordinates {"
for name, normal, reconstruction in data:
    out += f"({name}, {reconstruction}) "
out = out[:-1]
out += "};\n"

print(out)
