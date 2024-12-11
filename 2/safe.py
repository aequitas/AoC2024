safe = []

def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG

    iterator = iter(iterable)
    a = next(iterator, None)

    for b in iterator:
        yield a, b
        a = b

def issafe(x):
    if x != sorted(x) and x != sorted(x, reverse=True):
        print('skip')
        return False

    for a,b in pairwise(x):
        # print(abs(a - b))
        if abs(a - b) > 3 or abs(a - b) < 1:
            break
    else:
        print('safe')
        return True

for line in open('input.txt').readlines():
    x = list(map(int, line.split()))
    print()
    print(x)
    if issafe(x):
        safe.append(x)
        print('first')
        continue

    for d in range(len(x)):
        z = x.copy()
        del(z[d])
        print(z)
        if issafe(z):
            safe.append(x)
            break

print(len(safe))
# reports = (map(int, x) for y in  for x in y.split())

# print(list(next(reports)))
