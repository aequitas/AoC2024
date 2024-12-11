from audioop import reverse
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

# print("".join(blocks))

files = []
free = []

fileid = None
end = None
for i in list(reversed(range(len(blocks)))) + [-1]:
    # print(i)
    if fileid == None:
        end = i+1
        fileid = blocks[i]
    if blocks[i] != fileid:
        f = (i+1,end,fileid)
        # print(f)
        if fileid == '.':
            free.append(f)
        else:
            files.append(f)
        end = i+1

    fileid = blocks[i]

free = list(reversed(free))

# print(files)
# print(free)
# breakpoint()

for p, file in enumerate(files):
    print(len(files)/(p+1))
    l = file[1] - file[0]

    for i, f in enumerate(blocks):
        if i >= file[0]:
            continue
        # print(file, i,f)
        if f == '.':
            j = i
            # find next start of free space
            while j < len(blocks) and blocks[j] == '.':
                # print(j)
                j += 1
            if l <= j - i:
                for x in range(l):
                    blocks[i+x] = blocks[file[0]+x]
                    blocks[file[0]+x] = '.'

                # print("".join(blocks))
                break

# print(blocks)

# r = len(blocks)
# for i in range(len(blocks)):
#     if blocks[i] == '.':
#         while True:
#             r -= 1
#             if i > r:
#                 break
#             x = blocks[r]
#             if x != '.':
#                 blocks[i] = blocks[r]
#                 blocks[r] = '.'

#                 # print("".join(blocks), len(blocks), r, x, i)

#                 break
#     # if blocks[i] == 'z' and blocks[i+1] == 'z':
#     #     break

# assert blocks == list('0099811188827773336446555566..............')
# print(blocks)


chk = 0
for i,x in enumerate(blocks):
    if x == 'z':
        break
    if x == '.' :
        continue
    chk += i * int(x)

print(chk)
