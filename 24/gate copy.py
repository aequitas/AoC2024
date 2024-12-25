import re

IN = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""
VALUE = 4

IN = open("input.txt").read()

logic = re.compile(r"([a-z0-9]+) (AND|XOR|OR) ([a-z0-9]+) -> ([a-z0-9]+)")

operators = {
    'AND': '&',
    'OR': '|',
    'XOR': '^',
}

def topython(input):
    output = ""
    zs = []
    for line in input.splitlines():
        if ':' in line:
            output += line.replace(":", " =")

        if match := logic.match(line):
            print(match)
            x, op, y, z = match.groups()
            output += f"{z} = {x} {operators[op]} {y}"
            if z.startswith('z'):
                zs.append(z)


        output += "\n"
    for z in zs:
        output += f"print({z})\n"
    return output
print(topython(IN))
eval(topython(IN))
