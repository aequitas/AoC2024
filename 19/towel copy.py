from itertools import chain, pairwise

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

tmin = min([len(t) for t in towels])
tmax = max([len(t) for t in towels])

def combinations(iterable, r):
    # print('r', r)
    # combinations('ABCD', 2) → AB AC AD BC BD CD
    # combinations(range(4), 3) → 012 013 023 123

    pool = tuple(iterable)

    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    # print(r, indices)

    if r > 1:
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
    n = tmax
    b, mid, e = [0], list(range(1, n)), [n]

    # print(n, n/2, tmax, n / 2 <= tmax -1)
    # splits = list(d for i in range(0, n) for d in combinations(mid, i) if n / i <= tmax -1)

    # splits = (d for i in range(0, n) for d in combinations(mid, i))
    # splits = (s for s in splits if s and n / len(s) < tmax)
    # for d in splits:
        # print(d)

    for i in range(1,n):
        # if n / i > tmax:
        #     continue

        for d in combinations(mid, i):
            # if not d:
            #     continue
            # if n - d[-1] > tmax:
            #     continue
            # if d[0] > tmax:
            #     continue

            # for x,y in pairwise(d):
            #     if y - x > tmax:
            #         # print(y-x, d)
            #         break
            # else:
                yield (s[sl] for sl in map(slice, chain(b, d), chain(d, e)))


is_printable = 0
not_printable = 0
total = 0
t = set(towels)
for design in designs:
    # print()
    print(design)
    printable = 0

    for p in partition(design):
        # p = list(p)
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
