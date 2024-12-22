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

# {
#   "r": {
#     "towel": true,
#     "b": {
#       "towel": true
#     }
#   },
#   "w": {
#     "r": {
#       "towel": true
#     }
#   },
#   "b": {
#     "towel": true,
#     "w": {
#       "u": {
#         "towel": true
#       }
#     },
#     "r": {
#       "towel": true
#     }
#   },
#   "g": {
#     "towel": true,
#     "b": {
#       "towel": true
#     }
#   }
# }
# IN = open("input.txt").read()

towels = IN.splitlines()[0].split(", ")

designs = [x for x in IN.splitlines()[1:] if x]

# tree {'b': {'r' : {'w' : {'r' : {'r' : {}}}}}


tree = dict()

def add_towel(towel, tree):
    # print(towel, tree)

    if not tree.get(towel[:1]):
        tree[towel[:1]] = {'towel': False}
    if towel[1:]:
        tree[towel[:1]] = add_towel(towel[1:], tree[towel[:1]])
    else:
        tree[towel[:1]]['towel'] = True
    return tree

print(towels)

for towel in towels:
    add_towel(towel, tree)

print(json.dumps(tree, indent=2))

def find_towels(design, fulltree, tree=None):
    if not tree:
        tree = fulltree

    towels = 0

    if design[0] in tree:
        if tree[design[0]].get("towel"):
            if len(design) == 1:
                towels += 1
            else:
                towels += find_towels(design[1:], fulltree)

        if design[1:]:
            if tree[design[0]].get(design[1]):
                towels += find_towels(design[1:], fulltree, tree[design[0]])


    return towels

print()
x = find_towels('ubwu', tree)
print(x)
assert x == 0
print()
x = find_towels('bbrgwb', tree)
print(x)
assert x == 0
print()
x = find_towels('bggr', tree)
print(x)
assert x == 1
print()
x = find_towels('bwurrg', tree)
print(x)
assert x == 1
print()
x = find_towels('brwrr', tree)
print(x)
assert x == 2
print()
x = find_towels('gbbr', tree)
print(x)
assert x == 4
print()
x = find_towels('rrbgbr', tree)
print(x)
assert x == 6
print()
x = find_towels('brgr', tree)
print(x)
assert x == 2
print()
total = 0
start = time.time()
for design in designs:
    print(design)
    arrangements = find_towels(design, tree)
    print(arrangements)
    total += arrangements
print((time.time() - start)*1000, "ms")
print(total)
print()

IN = open("input.txt").read()
towels = IN.splitlines()[0].split(", ")
designs = [x for x in IN.splitlines()[1:] if x]
tree = dict()
for towel in towels:
    add_towel(towel, tree)
# print(json.dumps(tree, indent=2))

# total = 0
# for design in designs:
#     print(design)
#     arrangements = find_towels(design, tree)
#     print(arrangements)
#     total += arrangements
# print(total)
