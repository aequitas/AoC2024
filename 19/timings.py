import timeit

# print(timeit.timeit("d.get(1)", "d = dict.fromkeys(range(1000))"))
# print(timeit.timeit("1 in d", "d = dict.fromkeys(range(1000))"))
print(timeit.timeit("d[1]", "d = dict.fromkeys(range(1000))"))
print(timeit.timeit("d[500]", "d = range(1000)"))
print(timeit.timeit("d[500]", "d = tuple(range(1000))"))
# print(timeit.timeit("1 in d and d[1]", "d = dict.fromkeys(range(1000))"))
# print(timeit.timeit("-1 in d and d[1]", "d = dict.fromkeys(range(1000))"))
# print(timeit.timeit("a[:1]", "a = [1] * 1000"))
# print(timeit.timeit("len(a) > ", "a = [1] * 1000"))
# print(timeit.timeit("d.get('1')", "d = dict.fromkeys(map(str,range(1000)))"))
# print(timeit.timeit("'1' in d", "d = dict.fromkeys(map(str, range(1000)))"))
# print(timeit.timeit("d['1']", "d = dict.fromkeys(map(str, range(1000)))"))
