from itertools import chain, combinations

IN = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


towels = set(IN.splitlines()[0].split(", "))

designs = [x for x in IN.splitlines()[1:] if x]

# mint = min([len(t) for t in towels])
# maxt = max([len(t) for t in towels])

print(towels)

# def combinations(iterable, r):
#     # combinations('ABCD', 2) → AB AC AD BC BD CD
#     # combinations(range(4), 3) → 012 013 023 123

#     pool = tuple(iterable)
#     print(pool)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))

#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)

def partition(s):
    n = len(s)
    # print(n)
    b, mid, e = [0], list(range(1, n)), [n]
    # print(b,mid,e)

    splits = (d for i in range(1, n) for d in combinations(mid, i))

    # for d in splits:
    #     # print(d)
    #     p = []
    #     for sl in map(slice, chain(b,d), chain(d,e)):
    #         # print(sl)
    #         p.append(s[sl])
    #     yield p

    p =  [[s[sl] for sl in map(slice, chain(b, d), chain(d, e))]
        for d in splits]
    # # print(p)
    return p

total = 0

for design in designs:
    print()
    # print(design)
    printable = 0
    count = 0
    # count += len(partition(design))
    # for p in partition(design):
        # pass
        # if max(len(x) for x in p) > 3:
            # print(p)
            # raise Exception()
        # count += 1
        # if set(p) <= set(towels):
            # printable += 1
    print(printable, design, count)
    total += printable

print(total)
# assert total == 16

IN = open("input.txt").read()
designs = [x for x in IN.splitlines()[1:] if x]
for design in designs:
    print(design)
    printable = 0
    partition(design)
    # for p in partition(design):
        # if max(len(x) for x in p) > 3:
            # continue
        # print(p)
        # if set(p) <= set(towels):
            # print('p')
            # printable += 1
    # print(printable)
    total += printable
        # if not p in towels:
        #     not_printable += 1
    # break
# else:
#     printable += 1

print(total)
