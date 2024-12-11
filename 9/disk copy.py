IN = '2333133121414131402'
IN = open('input.txt').read().strip()

# print(len(IN))

IN = IN + '0'

blocks = []

for i, (d,f) in enumerate(zip(IN[::2], IN[1::2])):
    # print(i, d,f)
    blocks.append([str(i)] * int(d))
    blocks.append(['.'] * int(f))

def flatten(xss):
    return [x for xs in xss for x in xs]

blocks = flatten(blocks)
# blocks = "".join(blocks)
# print("".join(blocks))
# assert blocks == list('00...111...2...333.44.5555.6666.777.888899')

r = len(blocks)
for i in range(len(blocks)):
    if blocks[i] == '.':
        while True:
            r -= 1
            if i > r:
                break
            x = blocks[r]
            if x != '.':
                blocks[i] = blocks[r]
                blocks[r] = '.'

                # print("".join(blocks), len(blocks), r, x, i)

                break
    # if blocks[i] == 'z' and blocks[i+1] == 'z':
    #     break

# assert blocks == list('0099811188827773336446555566..............')
print(blocks)


chk = 0
for i,x in enumerate(blocks):
    if x == 'z':
        break
    if x == '.' :
        continue
    chk += i * int(x)

print(chk)


assert chk > 6418173468687
assert chk > 6418438212939
assert chk < 16381045199376
# assert chk == 1928
