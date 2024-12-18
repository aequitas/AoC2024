from collections import defaultdict
import sys
# sys.setrecursionlimit(5000)

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

# IN = """#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################"""

# IN = """
# #####
# #...E#
# #.#..#
# #S...#
# #####"""

# IN = open("input.txt").read()

def find(grid, c):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == c:
                return (y, x)
    return (-1,-1)

def printgrid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()

grid = IN
grid = [list(line) for line in grid.splitlines()]

printgrid(grid)

nodes: defaultdict[tuple[int, int], dict[tuple[int,int], int]] = defaultdict(dict)

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if not char in ['.', START, END]:
            continue
        # print(y,x)
        if grid[y][x+1] in ['.', START, END]:
            nodes[(y,x)][(y, x+1)] = 1

        if grid[y][x-1] in ['.', START, END]:
            nodes[(y,x)][(y, x-1)] = 1

        if grid[y-1][x] in ['.', START, END]:
            nodes[(y,x)][(y-1, x)] = 1

        if grid[y+1][x] in ['.', START, END]:
            nodes[(y,x)][(y+1, x)] = 1

        if char == '.':
            nodes[(y,x)]

for node in nodes.items():
    print(node)
# sys.exit(0)

start = find(grid, START)
end = find(grid, END)

# print(start, end)

# print(nodes[start])
from queue import PriorityQueue

queue = PriorityQueue()
queue.put((0, (start, DIR)))
distances: defaultdict[tuple[int,int], list] = defaultdict(list)
distances[start] = [0]
visited = defaultdict(list)
print()
while not queue.empty():
    prio, (node, d) = queue.get()
    # print()
    # print('c', node, d)
    # if node in visited:
    #     continue

    for neighbor in nodes[node]:
        distance = prio + nodes[node][neighbor]
        if d in ['<', '>'] and neighbor[0] != node[0]:
            distance += 1000
        if d in ['^', 'v'] and neighbor[1] != node[1]:
            distance += 1000

        # if neighbor[0] < node[0]:
        nd = '^'
        if neighbor[0] > node[0]:
            nd = 'v'
        if neighbor[1] < node[1]:
            nd = '<'
        if neighbor[1] > node[1]:
            nd = '>'

        if neighbor == (7,3):
            print('node', node)
        print('d', distance, distances[neighbor], neighbor, visited[neighbor])
        if len(distances[neighbor]) == 0:
            distances[neighbor] = [distance]
            visited[neighbor] = [node]
            queue.put((distance, (neighbor, nd)))
        elif distance <= max(distances[neighbor]):
            distances[neighbor].append(distance)
            visited[neighbor] += [node]
            queue.put((distance, (neighbor, nd)))



        # if distance < distances[neighbor]:
        #     distances[neighbor] = distance
        #     visited[neighbor] = [(node, distance)]
        #     queue.put((distance, (neighbor, nd)))
        # elif distance == distances[neighbor]:
        #     visited[neighbor].append((node, distance))



        # print('n', neighbor, nd, distance)
    # print("node", grid[node[0]][node[1]])
    # if grid[node[0]][node[1]] == END:
    #     break


# print()
# for distance in sorted(distances.items(), key=lambda x: x[0][0]*1000 + x[0][1]):
#     print(distance)
# print()

def printdistances(distances):
    print(distances.values())
    # size = len(str(max(distances.values())))+1
    size = 5

    print(" ".ljust(size), end="")
    for x in range(len(grid[0])):
        print(str(x).center(size), end=" ")
    print()
    for y, line in enumerate(grid):
        print(str(y).ljust(size), end="")
        for x, char in enumerate(line):
            if char == '.':
                # print(str(distances[end] - distances[(y,x)]).center(size), end=" ")
                print(str(max(distances[(y,x)])).center(size), end=" ")
            else:
                print(char*size, end=" ")

        print()

printdistances(distances)

# print(distances[(7,5)])
# assert distances[(7,5)] == 4010
# assert 0

# print(distances[end])
assert min(distances[end]) == 7036

def find_spot(path, node):
    print('pn', path, node)
    grid[node[0]][node[1]] = 'O'
    # printgrid(grid)
    # print()
    # print(node, visited[node])
    if not visited[node]:
        # print('not', path[::-1])
        paths.append(path[::-1])
        return
    for x in visited[node]:
        # print('recurse')
        find_spot(path + [x], x)

for x in visited:
    print(x == end, x, visited[x])
# # print(len(visited))

paths = list()
find_spot(paths, end)
for path in paths:
    print('path', path)

# printgrid(grid)
