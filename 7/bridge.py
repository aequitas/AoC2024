from pdb import pm
from itertools import *
i = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

i = open("input.txt").read()

x = []

def zip_longest(*iterables, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D-

    iterators = list(map(iter, iterables))
    num_active = len(iterators)
    if not num_active:
        return

    while True:
        values = []
        for i, iterator in enumerate(iterators):
            try:
                value = next(iterator)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)

for line in i.splitlines():
    a, n = line.split(':')
    x.append((int(a), list(map(int, n.split()))))


# out = []

def do(i):
    s,n = i
    c = set(product(['*', '+', '||'], repeat=len(n)-1))
    # c = set(product(['*', '+', '||'], repeat=len(n)-1))
    # print(c)
    # breakpoint()
    # print(s,n,c)
    # continue
    for m in c:
        # print(m)
        o = list(chain(*zip_longest(n,m, fillvalue="")))

        z = [i for i in o if i]
        p=z[0]

        a=None
        # breakpoint()
        for q in z:
            if isinstance(q, int):
                if a == '+':
                    p = p + q
                if a == '*':
                    p = p * q
                if a == '||':
                    # print(a,p,q)
                    p = int(f"{p}{q}")

                # u = f"{p} {a} {str(q)}"
                # print(z, 'p', p, 'a', a, 'q', q,'u', u)
                # p = eval(u)
            else:
                a = q

        # for

        if p == s:
            # print('!')
            return s
            # out.append(s)
            # break
    return 0

# print('sum', sum(out))


# def do(i):
#     x = y = i
#     return x + y

if __name__ == "__main__":
    import multiprocessing

    with multiprocessing.Pool(10) as p:
        print(sum(p.map(do, x)))
