#Uses python3

import sys


class BFSTree:
    # This class defines the connections of the tree.
    # It requires no initialization node, as the starting
    # point is arbitrary for bipartite graphs.
    # We assume the graph is bipartite, negating that
    # value when we find an instance where the difference
    # between two nodes' distances from the starting
    # node mod 2 = 0.

    def __init__(self, adj):
        self.size = len(adj)
        self.dist = [self.size] * self.size
        self.adj = adj
        self.queue = []
        self.bipartite = True

    def explore(self, s):
        self.dist[s] = 0
        self.queue = [s]
        while len(self.queue) > 0:
            u = self.dequeue()
            for i in self.adj[u]:
                if self.dist[i] == self.size:
                    self.queue.append(i)
                    self.dist[i] = self.dist[u] + 1
                elif (self.dist[i] - self.dist[u]) % 2 == 0:
                    self.bipartite = False

    def dequeue(self):
        x = self.queue[0]
        self.queue.pop(0)
        return x


def bipartite(adj):
    t = BFSTree(adj)
    for i in range(len(adj)):
        if t.dist[i] == len(adj):
            t.explore(i)
    if t.bipartite:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
