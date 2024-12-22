from itertools import chain, combinations
from collections import defaultdict
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
        tree[towel[:1]] = dict()
    if towel[1:]:
        tree[towel[:1]] = add_towel(towel[1:], tree[towel[:1]])
    else:
        tree[towel[:1]]['towel'] = True
    return tree

print(towels)

for towel in towels:
    # print(towel)
    add_towel(towel, tree)

print(json.dumps(tree, indent=2))

def find_towels(design, tree, subtree=None, t=None):
    if t == None:
        t = []
    if subtree == None:
        subtree = tree
    towels = 0

    print(" " * (7 - len(design)), design[0], list(design))

    # dead end
    if design[0] not in subtree:
        print(" " * (5 - len(design)), 'false')
    else:
        # do we have a towel?
        if subtree[design[0]].get('towel'):
            # is this the last towel?
            if len(design) == 1:
                # done
                # print('done')
                print(t + [design[0]])
                towels += 1
            else:
                print('more')
                # find more towels
                towels += find_towels(design[1:], tree, t=t + [design[0]])

        if len(design) > 2:
            print("more more", len(design), list(design))
            towels += find_towels(design[1:], tree, tree[design[0]], t=t + [design[0]])


            # for k in tree[design[0]]:
            #     if k == 'towel':
            #         continue

            #     towels += find_towels(design[1:], tree[k], t)

        # for k in tree[design[0]]:
        #     # print(" " * (5 - len(design)), k)
        #     towels += find_towels(design, k, t)
        # # find more towels
        # towels += find_towels(design[1:], tree[design[0]], t)

    print(" " * (7 - len(design)), design[0], design, towels)
    return towels

# for design in designs:
#     print()
#     print(design)
#     print(find_towels(design, tree))
# print()
# assert find_towels('ubwu', tree) == 0
# print()
# assert find_towels('bbrgwb', tree) == 0
# print()
# assert find_towels('bggr', tree) == 1
# print()
# assert find_towels('brwrr', tree) == 2
# print()
# assert find_towels('gbbr', tree) == 4
print()
assert find_towels('rrbgbr', tree) == 6
print()
assert find_towels('bwurrg', tree) == 1
print()
assert find_towels('brgr', tree) == 2
