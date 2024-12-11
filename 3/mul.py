i = open("input.txt").read()

# i = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

import re

enable = True
s = 0
for z in re.findall(r"(mul\(([0-9]{1,3}),([0-9]{1,3})\))|(do(n't)?)\(\)", i):
    print(z)
    if z[3] == "do":
        print("enable")
        enable = True
        continue
    if z[3] == "don't":
        print("disable")
        enable = False
        continue

    if enable:
        x,y = z[1:3]
        print(f"{x}*{y}")
        s += int(x)*int(y)

print(s)
