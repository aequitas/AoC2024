import json
from collections import defaultdict

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

games = set()
gamest = set()

for node, conns in nodes.items():
    print(node, len(conns))

# def find_network(node, nodes, network):
#     network.add(node)
#     for node2 in nodes[node]:
#         if not node2 in network:
#             find_network(node2, nodes, network)




# for node in nodes:
#     network = set()
#     find_network(node, nodes, network)
#     print(network)
#     print(len(network))

#     # if not node.startswith('t'):
#     #     continue
#     for node2 in nodes[node]:
#         for node3 in nodes[node2]:
#             if node in nodes[node3]:
#                 games.add(str(sorted([node, node2, node3])))
#                 if node.startswith('t'):
#                     gamest.add(str(sorted([node, node2, node3])))

# print(len(games))
# print(len(gamest))
