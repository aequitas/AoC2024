import os
from dijkstra import *

def makegrid(size, char='.'):
    grid = []
    for y in range(size):
        grid.append([char]*size)
    return grid

def printgrid(grid):
    print("  ", end=" ")
    for x, char in enumerate(grid[0]):
        print(x % 10, end="")
    print()
    for y, line in enumerate(grid):
        print(str(y).rjust(2), end=" ")
        for char in line:
            print(char, end="")
        print()

def fillmemory(grid, limit,  input, start=0):
    # newgrid = makegrid(len(grid))
    newgrid = grid

    for i, (x,y) in enumerate((x.split(',') for x in input.splitlines()[start:limit])):
        # if i > limit :
        #     break

        newgrid[int(y)+1][int(x)+1] = "\033[94m" + '#' + "\033[0m"

    return newgrid

def circumfence(grid, wall='#'):
    newgrid = makegrid(len(grid)+2, wall)

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            newgrid[y+1][x+1] = grid[y][x]

    return newgrid

W = 6+1
N = 12

IN = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

# grid = makegrid(W)
# printgrid(grid)
# grid = fillmemory(grid, N, IN)

# grid = circumfence(grid)

# printgrid(grid)

# nodes = get_nodes(grid)
# print(nodes)

# distances, predecessors = dijkstra_all_paths(nodes, (1,1))

# paths = reconstruct_paths(predecessors, (W-1, W-1))

# print(paths)

# spots = set()
# for path in paths:
#     grid = circumfence(fillmemory(makegrid(W), N, IN))
#     for spot in path:
#         # spots.add(spot)
#         grid[spot[0]][spot[1]] = "\033[92m" + 'O' + "\033[0m"
#     printgrid(grid)
#     print(len(path))

# print()

# for i in range(len(IN.splitlines())):
#     print()
#     coords = IN.splitlines()[i]
#     print(i, coords)
#     grid = circumfence(fillmemory(makegrid(W), i, IN))
#     nodes = get_nodes(grid)
#     distances, predecessors = dijkstra_all_paths(nodes, (1,1))
#     print(distances[(W,W)])
#     if distances[(W,W)] == float("inf"):
#         print('answer', coords)
#         grid[int(coords.split(',')[1])+1][int(coords.split(',')[0])+1] = "\033[91m" + '#' + "\033[0m"
#         printdistances(distances, grid)
#         break
#     printdistances(distances, grid)

    # os.system('clear')
    # printgrid(grid)


W = 71
N = 1024
IN = open("input.txt").read()

grid = circumfence(makegrid(W))
nodes = get_nodes(grid)
for i in range(len(IN.splitlines())):
    # print()
    # printgrid(grid)
    coords = IN.splitlines()[i]
    # print(i, coords)
    grid = fillmemory(grid, i, IN, i-1)
    # printgrid(grid)
    distances, predecessors = dijkstra_all_paths(nodes, (1,1))
    # print(distances[(W,W)])
    if distances[(W,W)] == float("inf"):
        os.system('clear')
        printdistances(distances, grid)
        print('answer', "\033[92m" + coords + "\033[92m" )
        grid[int(coords.split(',')[1])+1][int(coords.split(',')[0])+1] = "\033[91m" + '#' + "\033[0m"
        break
    # if not i % 10 :
    #     os.system('clear')
    #     printdistances(distances, grid)
    #     print(i, coords)


# for i in range(len(IN.splitlines())):
#     grid = circumfence(fillmemory(makegrid(W), i, IN))
#     nodes = get_nodes(grid)
#     distances, predecessors = dijkstra_all_paths(nodes, (1,1))
#     print(i, IN.splitlines()[i])
#     print(distances[(71,71)])
#     if distances[(71,71)] == float("inf"):
#         print('answer', i)
#     os.system('clear')
#     printdistances(distances, grid)








# printgrid(grid)
# paths = reconstruct_paths(predecessors, (71, 70))

# spots = set()
# for path in paths:
#     grid = circumfence(fillmemory(makegrid(W), N, IN))
#     for spot in path:
#         # spots.add(spot)
#         grid[spot[0]][spot[1]] = "\033[92m" + 'O' + "\033[0m"
#     printgrid(grid)
#     print(len(path))

# # print(len(paths[0]))
