import time
import json

IN = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

# >>> print(['b','g','r','u','w'])
# [98, 103, 114, 117, 119]

# IN = open("input.txt").read()

towels = IN.splitlines()[0].split(", ")

designs = [x for x in IN.splitlines()[2:] if x]


print(towels)

# tree = [[] for _ in range(200)]

# def add_towel(towel, tree):
#     if not tree[towel[0]]:
#         tree[towel[0]] = [[] for _ in range(200)]

#     if towel[1:]:
#         tree[towel[0]] = add_towel(towel[1:], tree[towel[0]])
#     else:
#         tree[towel[0]][0] = True
#     return tree

# def to_tuple(lst):
#     return tuple(to_tuple(i) if isinstance(i, list) else i for i in lst)

# for towel in towels:
#     print(towel)
#     ords = towel
#     print(ords)
#     add_towel(ords, tree)

# tree = to_tuple(tree)
# print(tree)

# print(json.dumps(tree, indent=2))

tmax = max(len(x) for x in towels)
cache = dict()

def find_towels(design):
    if len(design) == 0:
        return 1

    if tuple(design) in cache:
        return cache[tuple(design)]

    cache[tuple(design)] = sum(find_towels(design[i:]) for i in range(min(len(design), tmax)+1) if design[:i] in towels)

    # if tree[d]:
    #     if tree[d][0]:
    #         towels += find_towels(design[1:], fulltree, fulltree)

    #     if design[1:]:
    #         if tree[d][design[1]]:
    #             towels += find_towels(design[1:], fulltree, tree[d])

    return cache[tuple(design)]

print()
x = find_towels('ubwu')
print(x, cache)
assert x == 0
print()
x = find_towels('bbrgwb')
print(x, cache)
assert x == 0
print()
x = find_towels('bggr')
print(cache)
print(x, cache)
assert x == 1
print()
x = find_towels('bwurrg')
print(x, cache)
assert x == 1
print()
x = find_towels('brwrr')
print(x, cache)
assert x == 2
print()
x = find_towels('gbbr')
print(x, cache)
assert x == 4
print()
x = find_towels('rrbgbr')
print(x, cache)
assert x == 6
print()
x = find_towels('brgr')
print(x, cache)
assert x == 2
print()
total = 0
start = time.time()
for design in designs:
    print(design)
    arrangements = find_towels(design)
    print(arrangements)
    total += arrangements
print((time.time() - start)*1000, "ms")
print(total)
assert total == 16
print()

IN = open("input.txt").read()
towels = IN.splitlines()[0].split(", ")
designs = [x for x in IN.splitlines()[1:] if x]

# for towel in towels:
#     add_towel(towel, tree)
# # print(json.dumps(tree, indent=2))

# def f(design):
#     print(design)
#     t = find_towels(design)
#     print(design, t)
#     return t

# # if __name__ == "__main__":
# #     import multiprocessing
# #     total = 0
# #     with multiprocessing.Pool(30) as p:
# #         total = sum(p.map(f, designs))
# #     print(total)

# for design in designs:
#     print(design)
#     arrangements = find_towels(design)
#     print(arrangements)
#     total += arrangements
