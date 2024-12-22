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
    if not tree.get(towel[0]):
        tree[towel[0]] = {-1: False}
    if towel[1:]:
        tree[towel[0]] = add_towel(towel[1:], tree[towel[0]])
    else:
        tree[towel[0]][-1] = True
    return tree

print(towels)

for towel in towels:
    add_towel([ord(x) for x in towel], tree)

print(json.dumps(tree, indent=2))

def find_towels(design, fulltree, tree=None):
    towels = 0

    d = design[0]

    if d in tree:
        if tree[d][-1]:
            if len(design) == 1:
                towels += 1
            else:
                towels += find_towels(design[1:], fulltree, fulltree)

        if design[1:]:
            if design[1] in tree[d]:
                towels += find_towels(design[1:], fulltree, tree[d])


    return towels

print()
x = find_towels([ord(x) for x in 'ubwu'], tree, tree)
print(x)
assert x == 0
print()
x = find_towels([ord(x) for x in 'bbrgwb'], tree, tree)
print(x)
assert x == 0
print()
x = find_towels([ord(x) for x in 'bggr'], tree, tree)
print(x)
assert x == 1
print()
x = find_towels([ord(x) for x in 'bwurrg'], tree, tree)
print(x)
assert x == 1
print()
x = find_towels([ord(x) for x in 'brwrr'], tree, tree)
print(x)
assert x == 2
print()
x = find_towels([ord(x) for x in 'gbbr'], tree, tree)
print(x)
assert x == 4
print()
x = find_towels([ord(x) for x in 'rrbgbr'], tree, tree)
print(x)
assert x == 6
print()
x = find_towels([ord(x) for x in 'brgr'], tree, tree)
print(x)
assert x == 2
print()
total = 0
start = time.time()
for design in designs:
    print(design)
    arrangements = find_towels(design, tree, tree)
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
    add_towel([ord(x) for x in towel], tree)
# print(json.dumps(tree, indent=2))

total = 0
for design in designs:
    print(design)
    arrangements = find_towels([ord(x) for x in design], tree, tree)
    print(arrangements)
    total += arrangements
print(total)
