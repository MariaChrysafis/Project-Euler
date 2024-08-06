import copy
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict


class Tree:
    def get_total (self, arr) :
        self.vis = set()
        ans = 0
        for key in arr :
            if key in self.vis :
                continue
            ans += sum(self.dfs(key, key)) - 1
        return ans
    def components(self, arr):
        self.path = []
        ans = self.get_total(arr)
        self.path = arr
        for i in arr:
            if i not in self.adj:
                continue
            for j in self.adj[i]:
                if j not in arr:
                    ans -= sum(self.dfs(j, i)) - 1
        self.path = []
        return ans

    def dfs(self, cur, prev) -> list[int]:  # [with root, without root]
        self.vis.add(cur)
        self.vis.add(prev)
        ans = [1, 1]
        pos = []
        if cur not in self.adj :
            return ans
        for x in self.adj[cur]:
            if x not in self.path and x != prev:
                pos.append(x)
        if len(pos) == 0:
            return [1, 1]
        # print(cur, pos)
        ans[1] = 1
        ans[0] = 1
        for x in pos:
            res = self.dfs(x, cur)
            # print("WHOO " + str(res[1]))
            ans[0] *= res[0] + 1
            ans[1] += res[1] + res[0] - 1
        # print(cur, ans)
        return ans

    def add_edge(self, u: int, v: int):
        # print(u, v)
        if u not in self.adj:
            self.adj[u] = tuple()
        if v not in self.adj:
            self.adj[v] = tuple()
        self.adj[u] = (*self.adj[u], v)
        self.adj[v] = (*self.adj[v], u)

    def __init__(self):
        self.path = None
        self.adj = dict()  # maps an element to a tuple of adjacent neighbors
        self.vis = set()


class Main:
    def __init__(self):
        self.runner()

    def runner(self):
        N = 1000000
        pos = set()
        pos.add(1)
        pos.add(2)
        is_prime = [True] * (N + 1)
        is_prime[2] = False
        pos = [False] * (N + 1)
        pos[1] = pos[2] = True
        for p in range(2, N + 1):
            q = 2 * p
            while q <= N:
                is_prime[q] = False
                q += p
            if is_prime[p]:
                res = 1
                while res * p <= N:
                    res *= p
                    # print(p, res)
                    pos[res] = True
                    if res * 2 <= N:
                        pos[2 * res] = True
        # print(pos)
        pp = set()
        for x in range(N + 1):
            pp.add(x * x + 1)

        tot = []
        for x in range(N + 1):
            if pos[x]:
                tot.append(x)

        self.G = nx.Graph()
        # print(len(tot))
        for i in tot:
            for j in tot:
                if i * j in pp and i != j:
                    self.G.add_edge(i, j)
        # nx.draw(G,node_size=20, with_labels=True)
        # plt.savefig("basicgraph1.png")
        q = []
        for x in self.G.nodes():
            if self.G.degree(x) == 1:
                q.append(x)

        while len(q) != 0:
            x = q[0]
            q = q[1::]
            neighbors = copy.copy(self.G.neighbors(x))
            for y in neighbors:
                self.G.remove_edge(x, y)
                if self.G.degree(y) == 1:
                    q.append(y)
            self.G.remove_node(x)
        mst = nx.minimum_spanning_tree(self.G)
        # print(nx.bridges(G))
        for e in nx.bridges(self.G):
            self.G.remove_edge(e[0], e[1])
        # print(len(G.edges))
        # print(len(G.nodes))
        # nx.draw_planar(G,node_size=20, with_labels=True, node_color = node_colors)
        # plt.savefig("basicgraph2.png")

        triangle_to_id = dict()
        id_to_triangle = dict()
        # print(G.edges)
        for e in self.G.edges:
            for n in self.G.nodes:
                if e[0] == n or e[1] == n:
                    continue
                if n * e[0] not in pp or n * e[1] not in pp:
                    continue
                triangle = tuple(sorted([e[0], e[1], n]))
                if triangle in triangle_to_id:
                    continue
                id_to_triangle[len(triangle_to_id)] = triangle
                triangle_to_id[triangle] = len(triangle_to_id)
                # print(sorted(tuple([e[0], e[1], n])))
        # print(triangle_to_id)
        # print(id_to_triangle)
        tree = Tree()
        h = nx.Graph()
        for t1, _ in triangle_to_id.items():
            for t2, _ in triangle_to_id.items():
                if t1 > t2:
                    continue
                if len(set(t1).intersection(set(t2))) == 2:
                    tree.add_edge(triangle_to_id[t1], triangle_to_id[t2])
                    h.add_edge(triangle_to_id[t1], triangle_to_id[t2])
        # nx.draw_planar(h, node_size=20, with_labels=True)
        # plt.savefig("basicgraph2.png")
        # print(tree.adj)
        # print(tree.components({0}))
        # print(id_to_triangle)
        paths = dict()
        for i in range(len(id_to_triangle)):
            for kk in range(3):
                if id_to_triangle[i][kk] not in paths:
                    paths[id_to_triangle[i][kk]] = []
                paths[id_to_triangle[i][kk]].append(i)
        ans = 0
        # print(tree.adj)
        for key, value in paths.items():
            res = tree.components(set(value))
            # print(key, res, set(value))
            ans += key * res
        print(ans)


m1 = Main()
# t1 = Tree()
# t1.add_edge(1, 0)
# t1.add_edge(1, 2)
# t1.add_edge(1, 3)
# t1.add_edge(5, 4)
# t1.add_edge(5, 6)
# t1.add_edge(5, 7)
# print(t1.components([2, 4]))
