IN = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

IN = open("input.txt").read()

grid = [list(map(int, list(l))) for l in IN.splitlines()]

def printgrid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()

printgrid(grid)


def walk(y,x, h):
    # print(" " * h, y,x,h)
    # if (y,x) == (2,4):
    #     breakpoint()


    trials = []

    if h == 9:
        return [(y,x)]

    if y-1 >= 0:
        if grid[y-1][x] == h+1:
            trials.extend(walk(y-1, x, h+1))

    if x + 1 < len(grid[0]):
        if grid[y][x+1] == h+1:
            trials.extend(walk(y,x+1,h+1))

    if y+1 < len(grid):
        if grid[y+1][x] == h+1:
            trials.extend(walk(y+1, x, h+1))

    if x - 1 >= 0:
        if grid[y][x-1] == h+1:
            trials.extend(walk(y,x-1,h+1))

    return trials

scores = []

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 0:
            trials = walk(y,x, 0)
            print(trials)
            trials = set(trials)
            print(trials)
            score = len(trials)
            print(score)
            scores.append(score)


print(scores)
print('scores', len(scores))
out = sum(scores)
print('out', out)
assert out == 36
