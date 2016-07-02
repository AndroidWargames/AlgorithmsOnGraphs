#Uses python3

import sys


class BFSTree:
    # This class defines the connections of the tree.
    # It requires an initialization node (s), thereafter
    # (upon exploration) assigns distances and enqueues them
    # for further exploration

    def __init__(self, adj, s):
        self.size = len(adj)
        self.dist = [self.size] * self.size
        self.adj = adj
        self.queue = [s]
        self.s = s
        self.dist[s] = 0

    def explore(self):
        while len(self.queue) > 0:
            u = self.dequeue()
            for i in self.adj[u]:
                if self.dist[i] == self.size:
                    self.queue.append(i)
                    self.dist[i] = self.dist[u] + 1

    def dequeue(self):
        x = self.queue[0]
        self.queue.pop(0)
        return x


def distance(adj, s, t):
    tree = BFSTree(adj, s)
    tree.explore()
    result = tree.dist[t]
    if result == tree.size:
        return -1
    else:
        return result

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
