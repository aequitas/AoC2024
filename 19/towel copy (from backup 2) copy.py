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

# IN = open("input.txt").read()

towels = set(IN.splitlines()[0].split(", "))

designs = IN.splitlines()[2:]

min = min([len(t) for t in towels])
max = max([len(t) for t in towels])

def sliceable(xs):
    '''Return a sliceable version of the iterable xs.'''
    try:
        xs[:0]
        return xs
    except TypeError:
        return tuple(xs)

def partition(iterable):
    s = sliceable(iterable)
    n = len(s)
    # n = max
    b, mid, e = [0], list(range(1, n)), [n]
    # getslice = s.__getitem__
    splits = (d for i in range(n) for d in combinations(mid, i))
    return [[s[sl] for sl in map(slice, chain(b, d), chain(d, e))]
            for d in splits]

is_printable = 0
not_printable = 0
total = 0
for design in designs:
    # print(design)
    printable = 0
    for p in partition(design):
        # print(p)
        if set(p) <= set(towels):
            printable += 1
            # break
            #
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
