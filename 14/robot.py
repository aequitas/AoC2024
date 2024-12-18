import re

IN = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

W = 11
T = 7


W = 101
T = 103
IN = open("input.txt").read()

COUNT = 100

ROBOTS = """1.12.......
...........
...........
......11.11
1.1........
.........1.
.......1..."""

AFTER100 = """......2..1.
...........
1..........
.11........
.....1.....
...12......
.1....1...."""


robots = [list(map(int, r)) for r in re.findall(r"p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)", IN)]
# print(robots)

def robots_to_hallway(robots, y, x):
    hallway = []
    for _ in range(y):
        hallway.append([0]*x)
    for robot in robots:
        hallway[robot[1]][robot[0]] = hallway[robot[1]][robot[0]] + 1
    return hallway

def printgrid(grid):
    for line in grid:
        count = 0
        for char in line:
            if char:
                print('8', end="")
                count += 1
            else:
                print(' ', end="")
            # print(char, end="")
        print(count)


hallway = robots_to_hallway(robots, T, W)
# printgrid(hallway)

# hallway = [[int(char) for char in line] for line in ROBOTS.replace('.', '0').splitlines()]

import os

i=0
# while True:
#     i+=1
#     for j, robot in enumerate(robots):
#         x,y,h,v = robots[j]

#         x = (x + h) % W
#         y = (y + v) % T
#         # print(x,y)
#         robots[j] = (x,y,h,v)

#     if i == 7603:
#         os.system('clear')
#         hallway = robots_to_hallway(robots, T, W)
#         printgrid(hallway)

#         break

# sys.exit(0)

# time.sleep(1)
card = []

while True:
    i+=1
    for j, robot in enumerate(robots):
        x,y,h,v = robots[j]

        x = (x + h) % W
        y = (y + v) % T
        # print(x,y)
        robots[j] = (x,y,h,v)


    hallway = robots_to_hallway(robots, T, W)
    for line in hallway:
        if i % 101 == 28:
        # if i % 103 == 84:
        # if sum(line) == 32:
            os.system('clear')
            printgrid(hallway)
            import time
            card.append(i)
            print(card)
            time.sleep(0.2)
            break


# hallway = [[int(char) for char in line] for line in AFTER100.replace('.', '0').splitlines()]

# print(hallway)
quadrants = [
    [hallway[i][:W//2] for i in range(T//2)],
    [hallway[i][(W//2)+1:] for i in range(T//2)],
    [hallway[i+1][:W//2] for i in range(T//2, T-1)],
    [hallway[i+1][(W//2)+1:] for i in range(T//2, T-1)],
]
# print(quadrants)
# for q in quadrants:
#     print()
#     for line in q:
#         print(line)

def flatten(xss):
    return [x for xs in xss for x in xs]

robots_per_quadrant = [sum(flatten(quadrant)) for quadrant in quadrants]

# print(robots_per_quadrant)

from math import prod
sf = prod(robots_per_quadrant)

SF = 12

print(sf)
assert sf == SF
