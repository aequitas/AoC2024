left = open('left.s').readlines()
right = open('right.s').readlines()

cum = 0
for x,y in zip(left,right):
    cum += abs(int(y) - int(x))

print(cum)
