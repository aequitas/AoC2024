import sys
import time
import re
import timeit

def _run(a,b,c, program, check=False, seen=None):
    output = []

    ip = 0

    while ip < len(program):

        # x = str((a,b,c,ip,output))
        # if x in seen:
        #     # print("seen")
        #     return {}, None
        # seen.add(x)

        opcode = program[ip]

        if opcode in [0,2,5,6,7]:
            combo = program[ip+1]
            if combo == 4:
                combo = a
            elif combo == 5:
                combo = b
            elif combo == 6:
                combo = c

        # o = []
        # 2,4 => b = a % 8
        # 1,1 => b = b & 1
        # 7,5 => c = a // 2**b
        # 0,3 => a = a // 2**3
        # 1,4 => b = b & 4
        # 4,5 => b = b & c
        # 5,5 => o <- b % 8
        # 3,0 => a != 0 GOTO a

        match opcode:
            case 0: #adv
                a = a // (1 << combo)
            case 1:
                b ^= program[ip+1]
            case 2: #bst
                b = (combo % 8) & 1
                ip += 4
                continue
            case 3: #jnz
                if not a == 0:
                    ip = program[ip+1]
                    continue
            case 4:
                b ^= c
            case 5:
                if check and combo % 8 != program[len(output)]:
                    return {}, output

                output.append(combo % 8)
                # if check:
                #     if len(output) > len(program):
                #         return {}, output
                #     for i in range(len(output)):
                #         if output[i] != program[i]:
                #             return {}, output

            case 6: #bdv
                b = a // (1 << combo)

            case 7: #cdv
                c = a // (1 << combo)

        ip += 2

    return {'A':a, 'B': b, 'C':c}, output

def run(input):
    registers = {}
    program = []

    for line in re.findall("(.+?) ?([A-Z])?: (.+)", input):
        if line[0] == 'Register':
            registers[line[1]] = int(line[2])
        if line[0] == 'Program':
            program += [int(x) for x in line[2].split(",")]

    seen = set()
    registers, output = _run(*registers.values(), program, False, seen)

    return registers, output

def find(input, start, limit):
    registers = {}
    program = []

    for line in re.findall("(.+?) ?([A-Z])?: (.+)", input):
        if line[0] == 'Register':
            registers[line[1]] = int(line[2])
        if line[0] == 'Program':
            program += [int(x) for x in line[2].split(",")]

    i = 0
    try:
        seen = set()
        for i in range(start, limit, 8):
            registers, output = _run(i, 0, 0, program, True, seen)
            if output == program:
                print('answer', i)
                break
        else:
            print('fail')
    except:
        print()
        print(i)
        open("state",'w+').write(str(i-1))
        print()
        raise



# registers, output = run("""
# Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0""")
# print(output)
# assert output == [int(x) for x in "4,6,3,5,6,3,5,2,1,0".split(',')]

# registers, output = run("""
# Register A: 0
# Register B: 0
# Register C: 9

# Program: 2,6""")
# print(registers)
# assert registers['B'] == 1

# registers, output = run("""
# Register A: 10
# Register B: 0
# Register C: 0

# Program: 5,0,5,1,5,4""")
# print(output)
# assert output == [int(x) for x in "0,1,2".split(',')]

# registers, output = run("""
# Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0""")
# print(output)
# assert output == [int(x) for x in "4,2,5,6,7,7,7,7,3,1,0".split(',')]

# registers, output = run("""
# Register A: 0
# Register B: 29
# Register C: 0

# Program: 1,7""")
# print(registers)
# assert registers['B'] == 26

# IN = open("input.txt").read()
# registers, output = run(IN)
# print(output)
# assert output == [int(x) for x in "4,0,4,7,1,2,7,1,6".split(',')]

# registers, output = run("""
# Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0""")
# print(output)
# assert output != [int(x) for x in "0,3,5,4,3,0".split(',')]

# registers, output = run("""
# Register A: 117440
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0""")
# print(output)
# assert output == [int(x) for x in "0,3,5,4,3,0".split(',')]



speed = 0
for i in range(10):
    start = time.time()
    find("""
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""", 0, 117441)
    stop = time.time()
    speed += (stop - start) / 10
print("speed", speed)

start = time.time()
i = int(open("state",'r').read())
registers, output = run(open("input.txt").read())
print(registers, output)
assert registers == {'A': 0, 'B': 6, 'C': 0}
assert output ==  [4, 0, 4, 7, 1, 2, 7, 1, 6]

print(i)
print()
print()
print()
find(open("input.txt").read(), i, int(sys.maxsize))
stop = time.time()
print("speed", stop - start)
