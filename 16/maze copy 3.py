from queue import PriorityQueue
from collections import defaultdict

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

nodes = defaultdict(dict)

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

nodes = dict(nodes)
print(nodes)

def dijkstra_all_paths(graph, start):
    # Priority queue for maintaining the minimum distance nodes
    queue = PriorityQueue()
    queue.put([0, start])

    # Distance and predecessors
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = defaultdict(list)

    while not queue.empty():
        current_distance, current_node = queue.get()
        print(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = [current_node]  # Clear and add new predecessor
                queue.put([distance, neighbor])
            elif distance == distances[neighbor]:
                predecessors[neighbor].append(current_node)  # Add another path

    return distances, predecessors

def reconstruct_paths(predecessors, target):
    paths = []

    def backtrack(path, node):
        if not predecessors[node]:
            paths.append(path[::-1])  # Add reversed path
            return
        for pred in predecessors[node]:
            backtrack(path + [pred], pred)

    backtrack([], target)
    return paths

# Example usage

distances, predecessors = dijkstra_all_paths(nodes, (13,1))
paths = reconstruct_paths(predecessors, (1,13))
for path in paths:
    print(path)
print(len(paths))

spots = set()
for path in paths:
    for spot in path:
        spots.add(spot)
        grid[spot[0]][spot[1]] = 'O'

printgrid(grid)

print(len(spots))
print('done')
# for node in nodes.items():
#     print(node)
