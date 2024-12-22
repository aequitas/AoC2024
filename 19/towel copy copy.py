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

IN = open("input.txt").read()

towels = set(IN.splitlines()[0].split(", "))

designs = IN.splitlines()[2:]

mint = min([len(t) for t in towels])
maxt = max([len(t) for t in towels])

def partition(s):
    n = len(s)
    b, mid, e = [0], list(range(1, n)), [n]
    # n = maxt
    # getslice = s.__getitem__
    splits = (d for i in range(n) for d in combinations(mid, i))
    return ((s[sl] for sl in map(slice, chain(b, d), chain(d, e)))
            for d in splits)

is_printable = 0
not_printable = 0
total = 0
for design in designs:
    print(design)
    printable = 0
    x = partition(design)
    # print(len(x))
    for p in x:
        # print(p)
        if set(p) <= set(towels):
            # print(p)
            printable += 1
            break
    print(design, printable)
    total += printable
    if printable:
        is_printable += 1
    else:
        not_printable += 1
        # if not p in towels:
        #     not_printable += 1
        #     break
# else:
#     printable += 1

print(is_printable, not_printable, total)
assert total > 13058
