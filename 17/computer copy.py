import re
from queue import Queue

def run(registers, program, expected_output: str = ""):
    output = []
    ia = registers['A']

    ip = 0
    # count = 0
    lp = len(program)
    while True:
        lo = len(output)
        if lo > lp:
            return None, None
        elif lo <= lp:
            for i in range(lo):
                if output[i] != program[i]:
                    # print("non")
                    return None, None

        # out = ",".join([str(x) for x in output])
        # if not expected_output.startswith(out):
        #     # print(out)
        #     # print('not')
        #     return None, None

        # if ip >= len(program):
        # if ip >= 2:
        if lp == 1:
            out = ",".join([str(x) for x in output])
            # print(",".join([str(x) for x in program]))
            print(out, ia, "done")
            # print("regist", registers)
            # print("HaltAndCatchFire()")
            return registers, out

        # if count > 1:
        #     # print("long")
        #     return None, None
        # count += 1

        opcode = program[ip]
        operand = program[ip+1]

        # print()
        # print("ip", ip)
        # print("r", registers)
        # print("o o", opcode, operand)
        # print("out", output)
        # print("c", combo)


        # print("c", combo)

        # breakpoint()
        combo = operand
        if combo == 4:
            combo = registers['A']
        elif combo == 5:
            combo = registers['B']
        elif combo == 6:
            combo = registers['C']


        match opcode:
            case 0: #adv
                registers['A'] = registers['A'] // (2**combo)
            case 1:
                registers['B'] ^= operand
            case 2: #bst
                registers['B'] = combo % 8
            case 3: #jnz
                if not registers['A'] == 0:
                    ip = operand
                    continue
            case 4:
                registers['B'] ^= registers["C"]
            case 5:
                output.append(combo % 8)
            case 6: #bdv
                registers['B'] = registers['A'] // (2**combo)
            case 7: #cdv
                registers['C'] = registers['A'] // (2**combo)
            case _:
                raise Exception("invalid opcode: " + str(opcode))

        ip += 2

cache = [
    (117440,0,0,[0,3,5,4,3,0],[0,3,5,4,3,0])
]

# registers, output = run("""
# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0""")
# assert output == "4,6,3,5,6,3,5,2,1,0"

# registers, output = run("""
# Register A: 0
# Register B: 0
# Register C: 9

# Program: 2,6""")
# assert registers['B'] == 1

# registers, output = run("""
# Register A: 10
# Register B: 0
# Register C: 0

# Program: 5,0,5,1,5,4""")
# assert output == "0,1,2"

# registers, output = run("""
# Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0""")
# assert output == "4,2,5,6,7,7,7,7,3,1,0"

# registers, output = run("""
# Register A: 0
# Register B: 29
# Register C: 0

# Program: 1,7""")
# assert registers['B'] == 26

# IN = open("input.txt").read()
# print()
# registers, output = run(IN)
# assert output == "4,0,4,7,1,2,7,1,6"

# registers, output = run("""
# Register A: 117440
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0""")
# assert output == "0,3,5,4,3,0"

IN = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
OUTPUT = "0,3,5,4,3,0"

# def do(i):
#     registers, output = run(IN, i,  "0,3,5,4,3,0")
#     print(output)
#     if output == "0,3,5,4,3,0":
#         print("answer", i)
#         return i

# if __name__ == "__main__":
#     import multiprocessing

#     with multiprocessing.Pool(20) as p:
#         out = p.map(do, range(117439, 117442))
#         print(out)
#         print()
#         print(min(x for x in out if x))


IN = open("input.txt").read()
OUTPUT = "2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0"

registers = {}

program = []


for line in re.findall("(.+?) ?([A-Z])?: (.+)", IN):
    if line[0] == 'Register':
        registers[line[1]] = int(line[2])
    if line[0] == 'Program':
        program += [int(x) for x in line[2].split(",")]

def do(i):
    # if not i % 10000:
    # print(i)
    #

    _, output = run({"A": i, "B":0,"C":0}, program, OUTPUT)
    # if output:
    #     print(output, i)
    if output == OUTPUT:
        print("answer", i)
        return i


if __name__ == "__main__":
    import multiprocessing

    with multiprocessing.Pool(10) as p:
        out = float("inf")
        # for i in map(do, range(19999999999999, 2_9999999999999,8)):
        for i in map(do, range(0, 2_9999999999999,8)):
        # for i in map(do, range(0, 9999999999999, 8)):
        # for i in p.map(do, range(117441)):
        # for i in p.map(do, range(917441)):
            if i:
                # print('i', i)
                if i < out:
                    out = i

        # out = p.map(do, range(999999999, flo))
        print("result", out)
        # print()
        # print(min(x for x in out if x))
