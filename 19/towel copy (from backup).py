from itertools import chain

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

designs = IN.splitlines()[1:]

mint = min([len(t) for t in towels])
maxt = max([len(t) for t in towels])

def combinations(iterable, r):
    # combinations('ABCD', 2) → AB AC AD BC BD CD
    # combinations(range(4), 3) → 012 013 023 123

    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))

    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def partition(s):
    n = len(s)
    b, mid, e = [0], list(range(1, n)), [n]

    splits = list(d for i in range(n) for d in combinations(mid, i))
    print(splits)
    return ((s[sl] for sl in map(slice, chain(b, d), chain(d, e)))
        for d in splits)

is_printable = 0
not_printable = 0
total = 0
t = set(towels)
for design in designs:
    print()
    print(design)
    printable = 0

    for p in partition(design):
        p = list(p)
        # print(p)
        if set(p) <= t:
            # print(p)
            printable += 1
            break
    print(design, printable)
    total += printable
    if printable:
        is_printable += 1
    else:
        not_printable += 1

print()
print(is_printable, not_printable, total)
assert total > 13058
