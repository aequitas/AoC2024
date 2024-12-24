import json
from collections import defaultdict
from itertools import combinations, pairwise
from itertools import permutations

IN = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

IN = open('input.txt').read()

nodes = defaultdict(list)

for line in IN.splitlines():
    node1, node2 = line.split('-')

    nodes[node1].append(node2)
    nodes[node2].append(node1)

# print(json.dumps(nodes, indent=2))

longest = max(len(conns) for conns in nodes.values())

# print(longest)

networks = {}
notworks = set()

def find_network(node, nodes, network):
    # print(node, nodes[node], network)
    for n in network:
        if not node in nodes[n]:
            return

    network.add(node)
    if len(network) == longest:
        print(",".join(sorted(network)))
        return
    else:
        for node2 in nodes[node]:
            if node2 in network:
                continue
            find_network(node2, nodes, network)

for node in nodes:
    if node in notworks:
        continue

    network = set()
    find_network(node, nodes, network)


# games = set()
# gamest = set()

# # for node, conns in nodes.items():
# #     print(node, )

# def find_network(node, nodes, network):
#     network.add(node)
#     for node2 in nodes[node]:
#         if not node2 in network:
#             find_network(node2, nodes, network)

# for i in range(4,13):
#     print()
#     print(i)
#     # for c in combinations(nodes, i):
#         # print()
#     for d in permutations(set(nodes), i):
#         # print(d)
#         y=d
#         # if not x in nodes[y]:
#             # break
#     else:
#         print(",".join(sorted(c)))
#         # print(sorted(c))

# # for node in nodes:
# #     network = set()
# #     find_network(node, nodes, network)
# #     print(network)
# #     print(len(network))


# for g in games:
#     print(g)
