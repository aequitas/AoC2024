left = (int(x) for x in open('left.s').readlines())
right = (int(x) for x in open('right.s').readlines())

from collections import Counter

counts = Counter(right)

a = 0
for x in left:
  a += x * counts[x] 
print(a)
