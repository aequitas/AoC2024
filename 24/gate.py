import re
from queue import Queue

IN = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
VALUE = 4

IN = open("input.txt").read()

answer = re.compile(r"([a-z0-9]+): ([01])")
logic = re.compile(r"([a-z0-9]+) (AND|XOR|OR) ([a-z0-9]+) -> ([a-z0-9]+)")

operators = {
    'AND': '&',
    'OR': '|',
    'XOR': '^',
}

answers = {}

for match in answer.findall(IN):
    var, val = match
    answers[var] = val

gates = {}

for match in logic.findall(IN):
    # print(match)
    gates[match[3]] = match[:3]


# def xor(z):
#     if gates[z][1] != 'XOR':
#         # print(gates[z])
#         print(z, 'not xor')
#         invalid.add(z)

    # print(gates[gates[z][0]])
    # print(gates[gates[z][2]])

# xor('z00')

# for i in range(1, 45):
#     xor(f'z{i:02d}')

invalid = set()

# # find all XOR without 2 inputs
# for z, g in [(z,g) for z,g in gates.items() if g[1] == 'AND']:
#     if g[0][0] in ['x', 'y']:
#         if g[2][0] not in ['x', 'y']:
#             print(z, 'xor with only 1 input')
#             invalid.add(z)

# # find all OR without 2 inputs
# for z, g in [(z,g) for z,g in gates.items() if g[1] == 'OR']:
#     if g[0][0] in ['x', 'y']:
#         if g[2][0] not in ['x', 'y']:
#             print(z, 'or with only 1 input')
#             invalid.add(z)

# # find all AND gates not input of an OR gate
# for z, g in [(z,g) for z,g in gates.items() if g[1] == 'AND']:
#     for g2 in gates.values():
#         if z in g2 and g2[1] != 'OR':
#             print(z, g, 'and not -> or')
#             invalid.add(z)


# for z, g in [(z,g) for z,g in gates.items() if g[1] == 'XOR']:
#     # find all XOR gates with x|y inputs that don't feed into another XOR or AND
#     if g[0][0] in ['x', 'y'] and g[2][0] in ['x', 'y']:

#         down_gates = [g2 for g2 in gates.values() if z in g2]
#         # if len(down_gates) != 2 and z != 'z00':
#         #     print(z, g, down_gates, 'invalid downstream gates for xor with inputs')
#         #     invalid.add(z)
#         # for g2 in down_gates:
#         #     # print(g2)
#         #     if g2[1] not in  ['XOR', 'AND']:
#         #         print(z, g, g2, 'not xor and for xor with input')
#         #         invalid.add(z)
#     # else:
#     #     if z[0] != 'z':
#     #         print(z, g, 'invalid')
#     #         invalid.add(z)
# #         down_gates = [g2 for g2 in gates.values() if z in g2]
# #         # print(z, g, len(down_gates))
# #         if len(down_gates) == 1:
# #             print(z, g, down_gates, 'invalid downstream gates 2')
# #             invalid.add(z)



# # find all OR gates that don't feed into another XOR output gate
# for z, g in [(z,g) for z,g in gates.items() if g[1] == 'OR']:
#     # if g[0][0] in ['x', 'y'] and g[2][0] in ['x', 'y']:
#     if z == 'z45':
#         continue

#     down_gates = [g2 for g2 in gates.values() if z in g2]
#     # if len(down_gates) != 2:
#     #     print(z, g, 'invalid downstream gates')
#     #     invalid.add(z)

#     for z2, g2 in gates.items():
#         if z in g2 and g2[1] == 'XOR':
#             if z2[0] != 'z':
#                 print(z, g, 'not xor output')
#                 invalid.add(z)


# # find all OR gates that feed into another AND with input
# for z, g in [(z,g) for z,g in gates.items() if g[1] == 'OR']:
#     # if g[0][0] in ['x', 'y'] and g[2][0] in ['x', 'y']:

#     for z2, g2 in gates.items():
#         if z in g2 and g2[1] == 'AND':
#             if g2[0][0] in ['y', 'x']:
#                 print(z, 'not and without input')
#                 invalid.add(z)
#             if g2[2][0] in ['y', 'x']:
#                 print(z, 'not and without input')
#                 invalid.add(z)
#         if z in g2 and g2[1] == 'OR':
#             print(z, 'OR -> OR')
#             invalid.add(z)
#         if z in g2 and g2[1] == 'XOR':
#             if g2[0][0] in ['x', 'y'] or g2[2][0] in ['x', 'y']:
#                 print(z, g, 'invalid')
#                 invalid.add(z)
#             if z2[0] != 'z':
#                 print(z, g, 'OR output ')
#                 invalid.add(z)

for z, g in gates.items():
    if z[0] == 'z':
        if z == 'z45':
            continue

        if g[1] != 'XOR':
            print(z, g, 'z output not XOR gate')
            invalid.add(z)

    else:
        if g[0][0] not in ['x', 'y'] and g[2][0] not in ['x', 'y']:
            if g[1] == 'XOR':
                print(z, g, 'z output is XOR gate')
                invalid.add(z)

    if g[0][0] in ['x', 'y'] and g[2][0] in ['x', 'y'] and g[1] == 'XOR':
        if z == 'z00':
            continue
        for z2,g2 in gates.items():
            if z in g2 and g2[1] == 'XOR':
                break
        else:
            print(z,g, 'z outputs is missing XOR')
            invalid.add(z)

    if g[1] == 'AND':
        if 'x00' in g:
            continue
        for z2,g2 in gates.items():
            if z in g2 and g2[1] == 'OR':
                break
        else:
            print(z,g, 'z outputs is missing OR')
            invalid.add(z)




print(len(invalid))
# assert len(invalid) == 8
print(",".join(sorted(invalid)))

    # print(g)
    # if g[0][0] not in ['x', 'y']:
    #     print(g)
    #     if gates[g[0]][1] != 'OR':
    #         print('not or')
    # if g[2][0] not in ['x', 'y']:
    #     if gates[g[2]][1] != 'OR':
    #         print('not or')

# for g in [g for g in gates if g[1] == 'OR']:


# queue = Queue()
# for gate in gates:
#     queue.put(gate)




# graph = {}

# for match in answer.findall(IN):
#     var, val = match
#     graph[var] = var

# # while not queue.empty():
# #     x, op, y, z = queue.get()
# #     # print(z)
# #     if x in graph and y in graph:
# #         graph[z] = f"{graph[x]} {operators[op]} {graph[y]}"
# #     else:
# #         queue.put((x, op, y, z))

# # for x in sorted(sorted(graph, key=lambda x: graph[x]), key=lambda x: len(graph[x])):
# #     print(graph[x])


#     x, op, y, z = queue.get()
#     if x in answers and y in answers:
#         answers[z] = eval(f"{answers[x]} {operators[op]} {answers[y]}")
#     else:
#         queue.put((x, op, y, z))

# print(answers)

# queue = Queue()
# for gate in gates:
#     queue.put(gate)

# while not queue.empty():
#     x, op, y, z = queue.get()
#     if x in answers and y in answers:
#         answers[z] = eval(f"{answers[x]} {operators[op]} {answers[y]}")
#     else:
#         queue.put((x, op, y, z))

# print(answers)

# x = int("".join([str(answers[v]) for v in sorted([k for k in answers if k.startswith('x')], reverse=True)]), 2)
# y = int("".join([str(answers[v]) for v in sorted([k for k in answers if k.startswith('y')], reverse=True)]), 2)
# z = int("".join([str(answers[v]) for v in sorted([k for k in answers if k.startswith('z')], reverse=True)]), 2)
# print(x)
# print(y)
# print(x+y)
# print(z)
# print()
# print("".join([str(answers[v]) for v in sorted([k for k in answers if k.startswith('x')], reverse=True)]))
# print("".join([str(answers[v]) for v in sorted([k for k in answers if k.startswith('y')], reverse=True)]))
# print("{0:b}".format(x+y))
# print("".join([str(answers[v]) for v in sorted([k for k in answers if k.startswith('z')], reverse=True)]))
