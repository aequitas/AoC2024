from collections import defaultdict
#
# IN = "5910927 0 1 47 261223 94788 545 7771"
IN = "125 17"

stones = [int(x) for x in IN.split()]

cache = defaultdict(defaultdict)

for _ in range(25):
    i = 0
    while i < len(stones):
        stone = stones[i]
        if stone == 0:
            stones[i] = 1
            i += 1
        elif len(str(stone)) % 2 == 0:
            del stones[i]
            s = str(stone)
            mid = int(len(s)/2)
            left, right = s[:mid], s[mid:]
            stones.insert(i, int(right))
            stones.insert(i, int(left))
            i += 2
        else:
            stones[i] = stone * 2024
            i += 1

print('stones', len(stones))
assert len(stones) == 229557103025807
