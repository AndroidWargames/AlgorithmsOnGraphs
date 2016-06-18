#Uses python3

import sys

sys.setrecursionlimit(200000)


class Tree:
    def __init__(self, adj):
        self.preOrd = [-1] * len(adj)
        self.postOrd = [-1] * len(adj)
        self.found = [False] * len(adj)
        self.adj = adj
        self.count = 0
        self.size = len(adj)
        self.cyclic = False
        self.adjR = [[] for i in range(self.size)]
        self.SCCs = []

    def explore(self, i):
        self.found[i] = True
        self.preOrd[i] = self.count
        self.count += 1
        news = [i]
        for j in self.adj[i]:
            if not self.found[j]:
                news.extend(self.explore(j))
            elif self.postOrd[j] == -1:
                self.cyclic = True
        self.postOrd[i] = self.count
        self.count += 1
        return news

    def cycle(self):
        for i in range(self.size):
            if not self.cyclic:
                if not self.found[i]:
                    self.explore(i)
            else:
                break
        return self.cyclic

    def exploreAll(self):
        for i in range(self.size):
            if not self.found[i]:
                self.explore(i)

    def explored(self):
        return self.count == self.size

    def getRG(self):
        for i in range(len(self.adj)):
            for j in self.adj[i]:
                self.adjR[j].append(i)

    def getSCCs(self):
        self.preOrd = [-1] * len(adj)
        self.postOrd = [-1] * len(adj)
        self.found = [False] * len(adj)
        self.getRG()
        t = Tree(self.adjR)
        t.exploreAll()
        ords = sorted(range(t.size), key=lambda k: t.postOrd[k])
        ords = ords[::-1]
        for i in ords:
            if not self.found[i]:
                self.SCCs.append(self.explore(i))


def number_of_strongly_connected_components(adj):
    t = Tree(adj)
    t.getSCCs()
    scc = t.SCCs
    return len(scc)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
