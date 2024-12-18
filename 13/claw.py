import re
import math

IN = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

IN = open("input.txt").read()

machines = re.findall(r"Button A: X\+([0-9]+), Y\+([0-9]+)\nButton B: X\+([0-9]+), Y\+([0-9]+)\nPrize: X=([0-9]+), Y=([0-9]+)", IN)
# print(machines)
print(len(machines))
tokens = 0

for machine in machines:
    print(machine)
    a = list(map(int, machine[0:2]))
    b = list(map(int, machine[2:4]))
    p = list(map(lambda x: int(x) + 10000000000000, machine[4:6]))
    # p = list(map(lambda x: int(x), machine[4:6]))

    if p[0] % math.gcd(a[0], b[0]) != 0 or p[1] % math.gcd(a[1], b[1]) != 0:
        print("skip")
        continue

    A = (p[0]*b[1] - p[1]*b[0]) / (a[0]*b[1] - a[1]*b[0])
    B = (p[1]*a[0] - p[0]*a[1]) / (a[0]*b[1] - a[1]*b[0])
    if int(A) == A and int(B) == B:
        tokens += A*3 + B

    # possible = []

    # imax = math.ceil(max(p[0] / a[0],p[0] / b[0]))
    # jmax = math.ceil(max(p[1] / a[1],p[1] / b[1]))
    # print(imax, jmax)
    # over = False
    # for i in range(imax):
    #     print(i)

    #     A0 = a[0] * i
    #     A1 = a[1] * i
    #     for j in range(jmax):
    #         x = A0 + b[0] * j == p[0]
    #         if x:
    #             y = A1 + b[1] * j == p[1]
    #             if y:
    #                 print("prize a: ", i, "b:", j)
    #                 possible.append(i*3+j)
    #                 break
    #     if possible:
    #         break

    # if possible:
    #     tokens += min(possible)

print("tokens", tokens)

assert tokens < 147339522990830
