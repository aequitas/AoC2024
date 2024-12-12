IN = """AAAA
BBCD
BBCC
EEEC"""

IN = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

IN = open("input.txt").read()

gardens = [list(x) for x in IN.splitlines()]

seen = set()

def plot(y,x, plant):
    if (y,x) in seen:
        return (0,0, 0 )

    seen.add((y,x))

    fences = 0
    area = 1
    sides = 0

    # map borders have 1 fence
    if y - 1 < 0:
        fences += 1
    elif gardens[y - 1][x] == plant:
        (a, f, s) = plot(y-1,x,plant)
        fences += f
        area += a
        sides += s
    else:
        fences += 1

    if y + 1 >= len(gardens):
        fences += 1
    elif gardens[y + 1][x] == plant:
        (a, f, s) = plot(y + 1,x,plant)
        fences += f
        area += a
        sides += s
    else:
        fences += 1

    if x + 1 >= len(gardens):
        fences += 1
    elif gardens[y][x + 1] == plant:
        (a, f, s) = plot(y,x + 1,plant)
        fences += f
        area += a
        sides += s
    else:
        fences += 1

    if x - 1 < 0:
        fences += 1
    elif gardens[y][x - 1] == plant:
        (a, f, s) = plot(y,x - 1,plant)
        fences += f
        area += a
        sides += s
    else:
        fences += 1

    print(y,x, plant, area, fences)

    return (area, fences, sides)



plots = []

for y, line in enumerate(gardens):
    for x, char in enumerate(line):
        if (y,x) in seen:
            continue

        plots.append(plot(y,x, char))

print(len(seen), seen)
print(len(plots), plots)

total_price = 0
for area, perimeter in plots:
    total_price += area * perimeter

print(total_price)
assert total_price in [140, 1930]
