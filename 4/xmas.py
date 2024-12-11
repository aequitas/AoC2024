import re
# i = "\n".join([l for l in open("test.txt").readlines()])
# k = [i]

# i = "\n".join([l[::-1] for l in open("test.txt").readlines()])
# k.append(i)

import numpy

k = open("input.txt").readlines()
# k.append("." * (len(k[0])-1))
# m = numpy.array([[x for x in l.strip()] for l in k])
m = [[x for x in l.strip()] for l in k]
# print(len(m), len(m[0]))
xmas = 0
for y in range(len(m)-2):
    for x in range(len(m[y])):
        sam = [
            m[y][x:x+3],
            m[y+1][x:x+3],
            m[y+2][x:x+3]
        ]
        if len(sam[0]) < 3:
            continue
        # print(sam)
        sam[0][1] = "."
        sam[1][0] = "."
        sam[1][2] = "."
        sam[2][1] = "."
        print(sam)

        if sam == [['M', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'S']]:
            xmas += 1
            print('mas')
        if sam == [['S', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'M']]:
            xmas += 1
            print('sam')
        if sam == [['M', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'S']]:
            xmas += 1
            print('sam')
        if sam == [['S', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'M']]:
            xmas += 1
            print('sam')

print(xmas)
# m = [[x for x in l.strip()] for l in open("test.txt").readlines()]
# print(m)

# xmas=0

# from scipy.ndimage import rotate

# import numpy as np  # type: ignore

# import functools
# from typing import Any, Tuple

# # for i in [0,90]:
#     # m = rotate(m, angle=i, reshape=False)
#     # m = numpy.rot90(m)

#     # print(m)
#     # for l in m:
#     #     # print(l)
#     #     n = "".join([chr(c) for c in l])
#     #     print(n)
#     #     r = re.findall('XMAS', n)
#     #     xmas += len(r)

# a = m
# a = [np.diag(a[-1:-a.shape[0]-1:-1,:], i).tolist() for i in range(-a.shape[0]+1,a.shape[0])]
# print(a)
# for l in a:
#     # print(l)
#     n = "".join([chr(c) for c in l])
#     print(n)
#     r = re.findall('MAS|SAM', n)
#     xmas += len(r)


# # a=m

# # for i in [0,90,180,360]:
# #     m = a
# #     # m = rotate(m, angle=i, reshape=False)
# #     # a = numpy.rot90(a)

# #     print(m)
# #     for l in m:
# #         # print(l)
# #         n = "".join([chr(c) for c in l])
# #         print(n)
# #         r = re.findall('XMAS', n)
# #         xmas += len(r)


# # n = "\n".join(["".join(x) for x in l] for l in m)
# # print(n)
# # k.append(n)


# # import re
# # xmas = 0
# # for p in k:
# #     r = re.findall('XMAS', p)
# #     xmas += len(r)

# print(xmas)

# # # for z in i:
# # #     for x in z:
# # #         if x == "X":
