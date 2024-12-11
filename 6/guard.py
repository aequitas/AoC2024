from collections import defaultdict
import copy

kaart = [list(x) for x in """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()]
kaart = [list(x) for x in open('input.txt').readlines()]


kaart.append([' '] * len(kaart[0]))
kaart.insert(0, [' '] * len(kaart[0]))
for x, line in enumerate(kaart):
    kaart[x] = [' '] + line + [' ']

def printkaart(k):
    print("   ", end="")
    for x in range(len(k[0])):
        print(x, end="")
    print()
    for y, line in enumerate(k):
        print(str(y).rjust(2), end=" ")
        for c in line:
            print(c, end="")
        print()


def do(k):
    been = list()

    pos = (-1,-1)

    for y,line in enumerate(k):
        if not '^' in line:
            continue
        x = line.index('^')
        pos = (y,x)
        break

    # print('pos: ', pos)

    while True:
        y,x = pos
        g = k[y][x]

        # print(y,x,g)

        if g == '^':
            n = k[y-1][x]
            # print(n)
            if n == ' ':
                k[y][x] = 'X'
                k[y-1][x] = '^'
                break
            if n == '#' or n == 'O':
                k[y][x] = '>'
            else:
                k[y][x] = 'X'
                k[y-1][x] = '^'
                pos = (y-1, x)
        if g == '>':
            n = k[y][x+1]
            # print(n)
            if n == ' ':
                k[y][x] = 'X'
                k[y][x+1] = '>'
                break
            if n == '#' or n == 'O':
                k[y][x] = 'v'
            else:
                k[y][x] = 'X'
                k[y][x+1] = '>'
                pos = (y, x+1)
        if g == 'v':
            n = k[y+1][x]
            # print(n)
            if n == ' ':
                k[y][x] = 'X'
                k[y+1][x] = 'v'
                break
            if n == '#' or n == 'O':
                k[y][x] = '<'
            else:
                k[y][x] = 'X'
                k[y+1][x] = 'v'
                pos = (y+1, x)
        if g == '<':
            n = k[y][x-1]
            # print(n)
            if n == ' ':
                k[y][x] = 'X'
                k[y][x-1] = '<'
                break
            if n == '#' or n == 'O':
                k[y][x] = '^'
            else:
                k[y][x] = 'X'
                k[y][x-1] = '<'
                pos = (y, x-1)

        # import time
        # time.sleep(0.01)
        steps = (((x,y),g),(pos, k[pos[0]][pos[1]]))
        # print(steps)
        # print(been)
        if steps in been:
            print('paradox!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            # printkaart(k)

            return True

        been.append(steps)

    # printkaart(k)

    return False

def par(i):
    kaart,y,x = i
    kaart2 = copy.deepcopy(kaart)
    kaart2[y][x] = 'O'

    # printkaart(kaart2)
    if do(kaart2):
        return 1
    else:
        return 0

if __name__ == "__main__":
    import multiprocessing
    paradox = 0
    for y in range(len(kaart[1:-1])):
        with multiprocessing.Pool(10) as p:
            # paradox += sum(p.map(int, range(len(kaart[y][2:-1]))))
            paradox += sum(list(p.map(par, [(kaart, y, x) for x in range(len(kaart[y][2:-1]))])))


    total = 0
    for line in kaart:
        total += line.count('X')

    print('total', total)
    print('paradox', paradox)
