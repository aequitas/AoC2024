from queue import PriorityQueue
from collections import defaultdict
import sys
sys.setrecursionlimit(50000)

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

def find(grid, c):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == c:
                return (y, x)
    return (-1,-1)

def printgrid(grid):
    # print(" ".ljust(size), end="")
    # for x in range(len(grid[0])):
    #     print(str(x).center(size), end=" ")

    for y, line in enumerate(grid):
        print(str(y).rjust(len(str(len(grid)))), end=" ")
        for char in line:
            print(char, end="")
        print()

grid = IN
grid = [list(line) for line in grid.splitlines()]

start = find(grid, START)
end = find(grid, END)

# printgrid(grid)

nodes = defaultdict(dict)

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if not char in ['.', START, END]:
            continue

        if grid[y][x+1] in ['.', START, END]:
            nodes[(y,x)][(y, x+1)] = 1

        if grid[y][x-1] in ['.', START, END]:
            nodes[(y,x)][(y, x-1)] = 1

        if grid[y-1][x] in ['.', START, END]:
            nodes[(y,x)][(y-1, x)] = 1

        if grid[y+1][x] in ['.', START, END]:
            nodes[(y,x)][(y+1, x)] = 1

nodes = dict(nodes)
# print()
# print('nodes', len(nodes), nodes)

longest = 0
def dijkstra_all_paths(graph, start, node_direction):
    queue = PriorityQueue()
    queue.put([0, (start, node_direction)])

    # Distance and predecessors
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = defaultdict(list)

    final = float("inf")

    while not queue.empty():
        current_distance, (node, node_direction) = queue.get()
        grid[node[0]][node[1]] = "\033[94m" + '.' + "\033[0m"

        # if current_distance < final:
        #     continue

        char = grid[node[0]][node[1]]
        if char == END:
            final = current_distance

        for neighbor, weight in graph[node].items():
            # if neighbor[0] < node[0]:
            neighbor_direction = '^'
            if neighbor[0] > node[0]:
                neighbor_direction = 'v'
            if neighbor[1] < node[1]:
                neighbor_direction = '<'
            if neighbor[1] > node[1]:
                neighbor_direction = '>'

            corner_penalty = 0
            if neighbor_direction != node_direction:
                corner_penalty = 1000

            distance = current_distance + weight + corner_penalty

            # if distance >= final:
            #     continue

            # print(node, distances[node], distance, neighbor, distances[neighbor])
            # if neighbor_direction != node_direction:
                # distances[node] += 1000
                # print(distances)
                # breakpoint()

            # if  neighbor == (97,12):
            #     print(node, distances[node], distance, neighbor, distances[neighbor])
            # #     print(distance - 1000 == distances[neighbor])
            # #     print(distance < distances[neighbor])

            # if distance - 1000 == distances[neighbor]:
            #     print(distance - 1000 == distances[neighbor])
            #     print(distance < distances[neighbor])

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor].append(node)
                queue.put([distance, (neighbor, neighbor_direction)])
            if distance - 1000 == distances[neighbor]:
                # distances[neighbor] = distance
                predecessors[neighbor].append(node)
                queue.put([distance, (neighbor, neighbor_direction)])
            # if distance == distances[neighbor]:
                # distances[neighbor] = distance
                # predecessors[neighbor].append(node)
                # queue.put([distance, (neighbor, neighbor_direction)])
            # if distance - 999 == distances[neighbor]:
            #     distances[neighbor] = distance
            #     predecessors[neighbor].append(node)
            #     queue.put([distance, (neighbor, neighbor_direction)])


            # if neighbor == (1,14):
            #     print(node, distance < distances[neighbor], distance, distances[neighbor])
                # print(node, distances[node], distance, neighbor, distances[neighbor], distance < distances[neighbor])
            #     print(predecessors[node])
                # if neighbor_direction != node_direction:
                #     if distances[node] < distances[node] + 1000:
                #         distances[node] += 1000

            # elif distance - 1000 == distances[neighbor]:
            #     # predecessors[neighbor].append(node)
            #     # distances[node] = distance
            #     distances[neighbor] = distance

            # if node == (7,5):
            #     print('pred', predecessors[neighbor])

    return distances, predecessors

def reconstruct_paths(predecessors, target):
    paths = []

    def backtrack(path, node):
        grid[node[0]][node[1]] = "\033[91m" + 'X' + "\033[0m"
        if not predecessors[node]:
            # print('end')
            paths.append([target] + path[::-1])
            return
        for pred in predecessors[node]:
            # grid[pred[0]][pred[1]] = "\033[91m" + grid[pred[0]][pred[1]] + "\033[0m"
            if pred in path:
                return
            backtrack(path + [pred], pred)

        # if len(path) > 10000:
        #     return
        # print(len(path), len(paths))

    backtrack([], target)
    return paths

distances, predecessors = dijkstra_all_paths(nodes, start, DIR)
# print()
print('shortest', end, distances[end])

def printdistances(distances):
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
                print(str(distances[(y,x)]).center(size), end=" ")
            else:
                print(char*size, end=" ")
        # print(str(y).ljust(size), end="")

        print()

# print()
# printdistances(distances)

# breakpoint()

paths = reconstruct_paths(predecessors, end)
# queue = PriorityQueue()
# queue.put(end)
# paths = []
# while not queue.empty():
#     node = queue.get()
#     if not predecessors[node]:
#         paths.append(path[::-1])
#     for pred in predecessors[node]:
#         queue.put(path + [pred])

# print()
# print('paths', len(paths), paths)
# print('paths', len(paths))
# for path in paths:
#     print(len(path))

spots = set()
for path in paths:
    for spot in path:
        spots.add(spot)
        grid[spot[0]][spot[1]] = "\033[92m" + 'O' + "\033[0m"

        # grid[spot[0]][spot[1]] = 'O'

# print()
printgrid(grid)

# print()
print('spots', len(spots), "<593", "!492", "!461", "!490", "!487", "!549", "!544", "!543")
print(str(grid).count('O'))
# print()
# print('done')
