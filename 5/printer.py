
import math
import functools

rules = [list(map(int, x.split('|'))) for x in open("test.txt").readlines()]
rules = [list(map(int, x.split('|'))) for x in open("input.txt").readlines()]

updates = [list(map(int, x.split(','))) for x in open("testupdates.txt").readlines()]
updates = [list(map(int, x.split(','))) for x in open("updates.txt").readlines()]

sum = 0
sumfixed = 0

def compare(x,y):
    result = 0
    for first,last in rules:
        if x == first and y == last:
            result -= 1
    return result



for update in updates:
    good = True
    fixed = False
    fixes = []

    if not update == sorted(update, key=functools.cmp_to_key(compare)):
        good = False
    # for pos, _ in enumerate(update):
    #     first, page, last = update[:pos], update[pos], update[pos+1:]
    #     print(first, page, last)

        # for before, after in rules:
        #     if page == before:
        #         if not after in update:
        #             continue
        #         # print(page, before, after)
        #         if not after in last:
        # #             print('false')
        #             good = False
        #             fixes.append((before,after))

    if good:
        print('good')
        # print(update, math.ceil(len(update)/2))
        middle = update[math.floor(len(update)/2)]
        # print(middle)
        # print('middle', middle)
        sum += middle
    else:
        fixed = sorted(update, key=functools.cmp_to_key(compare))

        print('fixed', fixed)
        # print(update, math.ceil(len(update)/2))
        middle = fixed[math.floor(len(fixed)/2)]
        print(len(fixed), middle)
        # print(middle)
        # print('middle', middle)
        sumfixed += middle

print(sum)
# assert sum == 143
print('sumfixed', sumfixed)
assert sumfixed < 7365
assert sumfixed == 123
