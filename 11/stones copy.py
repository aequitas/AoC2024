IN = "125 17"
try:
    import json
    s, stones = json.loads(open("stones").read())
    c = 75
except:
    IN = "5910927 0 1 47 261223 94788 545 7771"
    s = 0
    c = 75
    stones = [int(x) for x in IN.split()]


def do(stones):
    i = 0
    while i < len(stones):
        stone = stones[i]
    # for i, stone in range(len(stones)):
        # print(i, stone)
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

    return stones

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def flatten(xss):
    return [x for xs in xss for x in xs]

if __name__ == "__main__":
    try:
        import multiprocessing

        with multiprocessing.Pool(20) as p:
            for _ in range(s, c):
                print(_)
                stones = flatten(p.map(do, split(stones, 10)))

            # print(stones)

            # print(stones)
        # if _ == 1:
        #     break
        # print(stones)
        # breakpoint()

            print(_, 'stones', len(stones))
        print('stones', len(stones))
    except KeyboardInterrupt:
        import json
        open("stones", "w").write(json.dumps([_, stones]))
