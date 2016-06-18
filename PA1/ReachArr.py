#Uses python3

import sys


class Tree:
    def __init__(self, adj):
        self.preOrd = [-1] * len(adj)
        self.postOrd = [-1] * len(adj)
        self.found = [False] * len(adj)
        self.adj = adj
        self.count = 0
        self.size = len(adj)

    def explore(self, i):
        self.found[i] = True
        self.preOrd[i] = self.count
        self.count += 1
        for j in self.adj[i]:
            if not self.found[j]:
                self.explore(j)
        self.postOrd[i] = self.count
        self.count += 1

    def explored(self):
        return self.count == self.size


def reach(adj, x, y):
    t = Tree(adj)
    t.explore(x)
    if t.found[y]:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
