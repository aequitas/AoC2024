def printgrid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()

grid = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########"""

moves = list("<^^>>>vv<v>>v<<")

grid = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########"""

moves = """<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

grid = ""
moves = ""
isgrid = True
for line in open("input.txt").readlines():
    if line.strip() == "":
        isgrid = False
        continue
    if isgrid:
        grid += line
    else:
        moves += line

moves = moves.replace("\n", "")

grid = [list(line) for line in grid.splitlines()]


printgrid(grid)

def find_robot(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '@':
                return y,x

def move(y, x, d, grid):
    if d == '^':
        if grid[y-1][x] == "O":
            print('push')
            move(y-1, x, d, grid)
        if grid[y-1][x] == '#':
            print('wall')
            return
        if grid[y-1][x] == '.':
            print('move')
            grid[y-1][x] = grid[y][x]
            grid[y][x] = "."

    if d == 'v':
        if grid[y+1][x] == "O":
            print('push')
            move(y+1, x, d, grid)
        if grid[y+1][x] == '#':
            print('wall')
            return
        if grid[y+1][x] == '.':
            print('move')
            grid[y+1][x] = grid[y][x]
            grid[y][x] = "."

    if d == '<':
        if grid[y][x-1] == "O":
            print('push')
            move(y, x-1, d, grid)
        if grid[y][x-1] == '#':
            print('wall')
            return
        if grid[y][x-1] == '.':
            print('move')
            grid[y][x-1] = grid[y][x]
            grid[y][x] = "."

    if d == '>':
        if grid[y][x+1] == "O":
            print('push')
            move(y, x+1, d, grid)
        if grid[y][x+1] == '#':
            print('wall')
            return
        if grid[y][x+1] == '.':
            print('move')
            grid[y][x+1] = grid[y][x]
            grid[y][x] = "."


for d in moves:
    y,x = find_robot(grid)

    move(y, x, d, grid)

    # print(d)
    # printgrid(grid)

gps = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 'O':
            gps += 100 * y + x

print(gps)
assert gps > 10906
