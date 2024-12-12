def calculate(data):
    gardens = [list(x) for x in data.splitlines()]

    seen = set()

    def plot(y,x, plant):
        # print(y,x)
        if (y,x) in seen:
            return (0,0)

        seen.add((y,x))

        sides = 0
        area = 1

        no = 0
        # map borders have 1 fence
        if y - 1 >= 0 and gardens[y - 1][x] == plant:
            (a, s) = plot(y - 1,x, plant)
            sides += s
            area += a
        else:
            no += 1


        if y + 1 < len(gardens) and gardens[y + 1][x] == plant:
            (a, s) = plot(y + 1,x, plant)
            sides += s
            area += a
        else:
            no += 1

        if x + 1 < len(gardens) and gardens[y][x + 1] == plant:
            (a, s) = plot(y, x + 1, plant)
            sides += s
            area += a
        else:
            no += 1

        if x - 1 >= 0 and gardens[y][x - 1] == plant:
            (a, s) = plot(y, x - 1, plant)
            sides += s
            area += a
        else:
            no += 1

        left = lambda y,x, plant: x - 1 >= 0 and gardens[y][x - 1] == plant
        right = lambda y,x, plant: x + 1 < len(gardens[0]) and gardens[y][x + 1] == plant
        top = lambda y,x, plant: y - 1 >= 0 and gardens[y - 1][x] == plant
        bottom = lambda y,x, plant: y + 1 < len(gardens) and gardens[y + 1][x] == plant

        topleft = lambda y,x,plant: y - 1 >= 0 and x - 1 >= 0 and gardens[y - 1][x - 1] == plant
        bottomleft = lambda y,x,plant: y + 1 < len(gardens) and x - 1 >= 0 and gardens[y + 1][x - 1] == plant

        topright = lambda y,x,plant: y - 1 >= 0 and x + 1 < len(gardens[0]) and gardens[y - 1][x + 1] == plant
        bottomright = lambda y,x,plant: y + 1 < len(gardens) and x + 1 < len(gardens[0]) and gardens[y + 1][x + 1] == plant

        p = plant

        if not top(y,x,p) and not left(y,x,p): #and not topleft(y,x,p):
            sides += 1
        if not bottom(y,x,p) and not left(y,x,p): # and not bottomleft(y,x,p):
            sides += 1
        if not top(y,x,p) and not right(y,x,p): #and not topright(y,x,p):
            sides += 1
        if not bottom(y,x,p) and not right(y,x,p): #and not bottomright(y,x,p):
            sides += 1

        if top(y,x,p) and right(y,x,p) and not topright(y,x,p):
            sides += 1
        if top(y,x,p) and left(y,x,p) and not topleft(y,x,p):
            sides += 1
        if bottom(y,x,p) and right(y,x,p) and not bottomright(y,x,p):
            sides += 1
        if bottom(y,x,p) and left(y,x,p) and not bottomleft(y,x,p):
            sides += 1

        # print('p', 'corners', sides)
        print(y,x, plant, area, sides)

        return (area, sides)

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
    return total_price

assert calculate("""AAAA
BBCD
BBCC
EEEC""") == 80

assert calculate("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""") == 436

assert calculate("""EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""") == 236

print()
print()
print()
print()
print()
print()

assert calculate("""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""") == 368

print()
print()
print()
print()
print()
print()

assert calculate("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""") == 1206


print("total: ", calculate(open("input.txt").read()))
