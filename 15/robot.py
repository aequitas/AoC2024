def printgrid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()

## small
grid = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######"""

moves = "<vv<<^^<<^^"

## large
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

## input
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

## process

grid = grid.replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")

moves = moves.replace("\n", "")

grid = [list(line) for line in grid.splitlines()]

printgrid(grid)

def find_robot(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '@':
                return y,x

def can_move(y, x, d, grid):
    if d == '^':
        if grid[y-1][x] == "[" :
            print('can push')
            return can_move(y-1, x, d, grid) and can_move(y-1, x+1, d, grid)
        if grid[y-1][x] == "]" :
            print('can push')
            return can_move(y-1, x-1, d, grid) and can_move(y-1, x, d, grid)

        if grid[y-1][x] == "]" :
            print('can push')
            return can_move(y-1, x-1, d, grid) and can_move(y-1, x, d, grid)
        if grid[y-1][x] == "]" :
            print('can push')
            return can_move(y-1, x, d, grid) and can_move(y-1, x-1, d, grid)

        if grid[y-1][x] == '#':
            print('wall')
            return False
        if grid[y-1][x] == '.':
            return True

    if d == 'v':
        if grid[y+1][x] == "[":
            print('can push')
            return can_move(y+1, x, d, grid) and can_move(y+1, x+1, d, grid)

        if grid[y+1][x] == "]":
            print('can push')
            return can_move(y+1, x-1, d, grid) and can_move(y+1, x, d, grid)

        if grid[y+1][x] == '#':
            print('wall')
            return False
        if grid[y+1][x] == '.':
            print('move')
            return True


def move(y, x, d, grid):
    if d == '^':
        if grid[y-1][x] == "[" :
            print('push')
            if can_move(y-1, x, d, grid) and can_move(y-1, x+1, d, grid):
                move(y-1, x, d, grid)
                move(y-1, x+1, d, grid)
        if grid[y-1][x] == "]" :
            print('push')
            if can_move(y-1, x-1, d, grid) and can_move(y-1, x, d, grid):
                move(y-1, x-1, d, grid)
                move(y-1, x, d, grid)
        if grid[y-1][x] == '#':
            print('wall')
            return
        if grid[y-1][x] == '.':
            print('move')
            grid[y-1][x] = grid[y][x]
            grid[y][x] = "."

    if d == 'v':
        if grid[y+1][x] == "[":
            print('push')
            if can_move(y+1, x, d, grid) and can_move(y+1, x+1, d, grid):
                move(y+1, x, d, grid)
                move(y+1, x+1, d, grid)
        if grid[y+1][x] == "]":
            print('push')
            if can_move(y+1, x-1, d, grid) and can_move(y+1, x, d, grid):
                move(y+1, x-1, d, grid)
                move(y+1, x, d, grid)
        if grid[y+1][x] == '#':
            print('wall')
            return
        if grid[y+1][x] == '.':
            print('move')
            grid[y+1][x] = grid[y][x]
            grid[y][x] = "."

    if d == '<':
        if grid[y][x-1] in "[]":
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
        if grid[y][x+1] in "[]":
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

    # print(d)

    move(y, x, d, grid)

printgrid(grid)

gps = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == '[':
            assert line[x+1] == ']'
            gps += 100 * y + x

# print(105)
print(9021)
print('????')
print(gps)
