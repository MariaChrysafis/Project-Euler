import copy
import math

import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

n = 200000
def combo (x: int) :
    arr = [1, x]
    while arr[-1] * x <= n :
        arr.append(arr[-1] * x)
    return arr
def best (x: int, y: int) :
    if x == 0 :
        return combo(y)[-1]
    if y == 0 :
        return combo(x)[-1]
    ans = 0
    for a in combo(x) :
        for b in combo(y) :
            if a * b <= n :
                ans = max(ans, a * b)
    return ans
def is_prime (x : int) :
    if x == 1 :
        return False
    for div in range(2, x) :
        if div * div > x :
            return True
        if x % div == 0 :
            return False
    return True
g = nx.Graph()
primes = []
for i in range(1, n + 1) :
    print(i)
    if is_prime(i) :
        primes.append(i)
# print(primes)
print("DONE")
# primes.append(0)
for x in primes :
    if x * x > n :
        continue
    for y in primes :
        if y * y <= n :
            continue
        if x != y and x * y <= n :
            b1 = best(x, y)
            b2 = combo(x)[-1] + combo(y)[-1]
            if b1 >= b2 :
                g.add_edge(x, y, weight=best(x, y) - combo(x)[-1] - combo(y)[-1])

l1 = []
for node in g.nodes :
    if node * node <= n :
        l1.append(node)
pos = nx.bipartite_layout(g, nodes=l1)
# nx.draw(g, pos=pos, with_labels=True)
labels = {e: g.edges[e]['weight'] for e in g.edges}
# print(labels)
# nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels)
# plt.savefig('plotgraph.png', dpi=300, bbox_inches='tight')
# plt.show()
# print(g.edges)
print(len(g.edges))
# print(nx.max_weight_matching(g))
ans = 0
for p in primes :
    ans += combo(p)[-1]
    # print(combo(p)[-1])
for e in nx.max_weight_matching(g) :
    if ((e[1], e[0])) in labels :
        ans += labels[(e[1], e[0])]
    else :
        ans += labels[e]
    print(e)
print(ans + 1)
