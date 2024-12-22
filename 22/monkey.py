import time
from itertools import zip_longest

def process(input, numbers):
    n = []
    for buyer_nr in (int(x) for x in input.splitlines()):
        nr = buyer_nr
        for i in range(numbers):
            nr = (nr ^ (nr * 64)) % 16777216
            nr = (nr ^ (nr // 32)) % 16777216
            nr = (nr ^ (nr * 2048)) % 16777216
        n.append(nr)

    return sum(n)

TEST = """1
10
100
2024"""
result = process(TEST, 2000)
print(result)
assert result == 37327623

# IN = open("input.txt").read()
# result = process(IN, 2000)
# print(result)
# assert result == 19822877190

def sequences(input, numbers):
    buyers = []
    for buyer_nr in (int(x) for x in input.splitlines()):
        nr = buyer_nr

        nrs = [nr]
        prices = [int(str(nr)[-1])]
        changes = []

        for i in range(numbers):
            nr = (nr ^ (nr * 64)) % 16777216
            nr = (nr ^ (nr // 32)) % 16777216
            nr = (nr ^ (nr * 2048)) % 16777216

            nrs.append(nr)

            price = int(str(nr)[-1])

            if len(prices):
                changes.append(price - prices[-1])
            prices.append(price)

        sequences = dict()
        for i in range(4, len(changes)):
            # print(i-4)
            sequence = tuple(changes[i-4:i])
            # print(sequence, changes[i-1])
            if sequence in sequences:
                continue
            sequences[sequence] = prices[i]

        buyers.append((tuple(nrs), tuple(prices), tuple(changes), sequences))

    return buyers

print()
for i in zip_longest(*sequences("123", 9)[0], [None]):
    print(f"{i[0]}: {i[1]} ({i[2]})")

for b in sequences("123", 9):
    _, _, _ , s = b
    print(s.get((-1,-1,0,2), None))


print("""123: 3
15887950: 0 (-3)
16495136: 6 (6)
527345: 5 (-1)
704524: 4 (-1)
1553684: 4 (0)
12683156: 6 (2)
11100544: 4 (-2)
12249484: 4 (0)
7753432: 2 (-2)""")
print()

TEST = """1
10
100
2024"""
for b in sequences(TEST, 2000):
    print(b[0][-1])
print("""1: 8685429
10: 4700978
100: 15273692
2024: 8667524""")
print()
result = sum([buyer[0][-1] for buyer in sequences(TEST, 2000)])
print(result)
assert result == 37327623

# result = sum([buyer[0][-1] for buyer in sequences(IN, 2000)])
# print(result)
# assert result == 19822877190
# print()

TEST2 = """1
2
3
2024"""
EXPECT = tuple([-2,1,-1,3])
buyers = sequences(TEST2, 2000)
for b in buyers:
    _, _, _ , s = b
    print(s.get(EXPECT, 0))
higest = sum(b[3].get(EXPECT, 0) for b in buyers)
print(higest)
assert higest == 23

IN = open("input.txt").read()
start = time.time()
buyers = sequences(IN, 2000)
print('elapsed: ', time.time() - start)

print('sequences: ', sum(len(b[3]) for b in buyers))
unique_sequences = set(s for b in buyers for s in b[3])
print('unique sequences: ', len(unique_sequences))
ts = []
for s in unique_sequences:
    t = 0
    for b in buyers:
        t += b[3].get(s, 0)
    # print(t)
    ts.append(t)
print(max(ts))
