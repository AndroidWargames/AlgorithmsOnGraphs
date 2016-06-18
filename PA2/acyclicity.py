#Uses python3

import sys


def acyclic(adj):
    t = Tree(adj)
    if t.cycle():
        return 1
    else:
        return 0


class Tree:
    def __init__(self, adj):
        self.preOrd = [-1] * len(adj)
        self.postOrd = [-1] * len(adj)
        self.found = [False] * len(adj)
        self.adj = adj
        self.count = 0
        self.size = len(adj)
        self.cyclic = False

    def explore(self, i):
        self.found[i] = True
        self.preOrd[i] = self.count
        self.count += 1
        for j in self.adj[i]:
            if not self.found[j]:
                self.explore(j)
            elif self.postOrd[j] == -1:
                self.cyclic = True
        self.postOrd[i] = self.count
        self.count += 1

    def cycle(self):
        for i in range(self.size):
            if not self.cyclic:
                if not self.found[i]:
                    self.explore(i)
            else:
                break
        return self.cyclic

    def explored(self):
        return self.count == self.size

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
