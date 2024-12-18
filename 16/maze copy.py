import sys
sys.setrecursionlimit(5000)

START = 'S'
DIR = '>'
END = 'E'

MOVE_POINT = 1
TURN_POINT = 1000

IN = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

IN = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

IN = open("input.txt").read()

def find_start(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == START:
                return y, x, DIR

def printgrid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()

grid = IN
grid = [list(line) for line in grid.splitlines()]

printgrid(grid)

def find_end(y,x,d, steps, path, paths):
    if (y,x) in steps:
        # print('dead end')
        return

    steps = steps +[(y, x)]
    path = path + [(y,x,d)]
    # print(steps)
    # print(y, x, d)

    if grid[y][x+1] == ".":
        find_end(y, x+1, '>', steps, path, paths)

    if grid[y-1][x] == ".":
        find_end(y-1, x, '^', steps, path, paths)

    if grid[y+1][x] == ".":
        find_end(y+1, x, 'v', steps, path, paths)

    if grid[y][x-1] == ".":
        find_end(y, x-1, '<', steps, path, paths)

    if grid[y][x+1] == "E":
        # steps = steps + [(y, x, d)]
        paths.append(path)
        return

    if grid[y-1][x] == "E":
        # steps = steps + [(y, x, d)]
        paths.append(path)
        return

    if grid[y+1][x] == "E":
        # steps = steps + [(y, x, d)]
        paths.append(path)
        return

    if grid[y][x-1] == "E":
        # steps = steps + [(y, x, d)]
        paths.append(path)
        return

        # if grid[y][x+1] == '#':
        #     print('wall')
        #     return
        # if grid[y][x+1] == '.':
        #     print('move')
        #     grid[y][x+1] = grid[y][x]
        #     grid[y][x] = "."

    # if d == '^':
    #     if grid[y-1][x] == "#":
    #         print('push')
    #         move(y-1, x, d, grid)
    #     if grid[y-1][x] == '#':
    #         print('wall')
    #         return
    #     if grid[y-1][x] == '.':
    #         print('move')
    #         grid[y-1][x] = grid[y][x]
    #         grid[y][x] = "."

    # if d == 'v':
    #     if grid[y+1][x] == "O":
    #         print('push')
    #         move(y+1, x, d, grid)
    #     if grid[y+1][x] == '#':
    #         print('wall')
    #         return
    #     if grid[y+1][x] == '.':
    #         print('move')
    #         grid[y+1][x] = grid[y][x]
    #         grid[y][x] = "."

    # if d == '<':
    #     if grid[y][x-1] == "O":
    #         print('push')
    #         move(y, x-1, d, grid)
    #     if grid[y][x-1] == '#':
    #         print('wall')
    #         return
    #     if grid[y][x-1] == '.':
    #         print('move')
    #         grid[y][x-1] = grid[y][x]
    #         grid[y][x] = "."


y, x,d = find_start(grid)
paths = []
find_end(y,x,d, [], [], paths)
print(len(paths))

start_d = d
scores = []
for path in paths:
    score = 0
    prev_d = start_d
    for y,x,d in path:
        # print(d, end="")
        if prev_d == d:
            score += 1
        else:
            score += 1001
        prev_d = d
    # print()
    # print(score)
    scores.append(score)
print()
print(min(scores))

# ^^^>>^^>>>>>>>>vvvvvv>>^^^^^^^^^^^^
