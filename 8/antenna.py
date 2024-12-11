import sys

test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


# test = """T.........
# ...T......
# .T........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# .........."""

def #printgrid(grid):
    for line in grid:
        for char in line:
            #print(char, end="")
        #print()

inputtxt = open("input.txt").read()

grid = [list(l) for l in inputtxt.splitlines()]
# grid = [list(l) for l in test.splitlines()]

from copy import deepcopy
output = deepcopy(grid)
# output = []
# for y in range(len(grid)):
    # output.append(['.']*len(grid[0]))

##printgrid(grid)
##print()

Y = len(grid)
X = len(grid[0])

pairs = []
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char != '.':
            first = (y, x)
            for x2, char2 in list(enumerate(line))[x+1:]:
                if char2 == char:
                    second = (y, x2)
                    pairs.append((first, second))

            for y2, line2 in list(enumerate(grid))[y+1:]:
                for x2, char2 in list(enumerate(line2)):
                    # ##print(char2, char, y,x, y2 ,x2)
                    if char2 == char:
                        # #print('pair')
                        second = (y2, x2)
                        pairs.append((first, second))

#print(pairs)
#print(len(pairs))

for first, second in pairs:
    y = second[0] - first[0]
    x = second[1] - first[1]
    for i in range(Y):
        a1 = (first[0] - y*i, first[1] - x*i)
        a2 = (second[0]+y*i, second[1] + x*i)
        if a1[0] >= 0 and a1[0] < Y and a1[1] >= 0 and a1[1] < X:
            #print(Y, X, a1)
            output[a1[0]][a1[1]] = '#'
        if a2[0] >= 0 and a2[0] < Y and a2[1] >= 0 and a2[1] < X:
            #print(Y, X, a2)
            output[a2[0]][a2[1]] = '#'

#printgrid(output)
#print('output', str(output).count('#'))

sys.exit(0)










TEST_A = 2
TEST_B = 4

inputtxt = open("input.txt").read()
INPUT_A = 4
INPUT_B = 8

t = test.splitlines()

i = inputtxt.splitlines()

def do_a(x):
    return int(x)

def do_b(x):
    return int(x) * 2

if __name__ == "__main__":
    import multiprocessing

    with multiprocessing.Pool(10) as p:
        s = sum(p.map(do_a, t))
        #print('tA', s)
        assert s == TEST_A

    with multiprocessing.Pool(10) as p:
        s = sum(p.map(do_b, t))
        #print('tB', s)
        assert s == TEST_B

    with multiprocessing.Pool(10) as p:
        s = sum(p.map(do_a, i))
        #print('iA', s)
        assert s == INPUT_A

    with multiprocessing.Pool(10) as p:
        s = sum(p.map(do_b, i))
        #print('iB', s)
        assert s == INPUT_B
