import timeit
from collections import defaultdict

IN = "125 17"
test = [int(x) for x in IN.split()]
IN = "5910927 0 1 47 261223 94788 545 7771"
stones = [int(x) for x in IN.split()]

cache = defaultdict(defaultdict)

def blink(stones, blinks):
    if blinks == 0:
        return len(stones)

    count = 0
    for stone in stones:
        if stone in cache[blinks]:
            count += cache[blinks][stone]
        elif stone == 0:
            count += blink([1], blinks -1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            mid = int(len(s)/2)
            left, right = s[:mid], s[mid:]
            count += blink([int(left)],blinks -1)
            count += blink([int(right)],blinks -1)
        else:
            i  = blink([stone * 2024], blinks -1)
            cache[blinks][stone] = i
            count += i

    return count

print(timeit.timeit(lambda: print(blink(test, 6), end=" "), number=1), 'ms')
print(timeit.timeit(lambda: print(blink(test, 25), end=" "), number=1), 'ms')
print(timeit.timeit(lambda: print(blink(stones, 25), end=" "), number=1), 'ms')
print(timeit.timeit(lambda: print(blink(stones, 75), end=" "), number=1), 'ms')
