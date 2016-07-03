#Uses python3

import sys


class NegCycleTree:
    def __init__(self, adj, cost):
        self.size = len(adj)
        self.edges = sum(len(i) for i in adj)
        self.dist = [sum(sum(abs(j) for j in i) for i in cost) + 1] * self.size
        self.adj = adj
        self.unknown = [True] * self.size
        self.cost = cost
        self.cycle = False

    def nc(self):
        self.dist[0] = 0
        for i in range(self.size + 1):
            r = False
            for j in range(self.size):
                r = r or self.relax(j)
            if not r:
                return 0
            elif i == self.size:
                return 1

    def relax(self, x):
        rel = False
        dis = self.dist[x]
        for i in range(len(self.adj[x])):
            if self.cost[x][i] + dis < self.dist[adj[x][i]]:
                self.dist[adj[x][i]] = self.cost[x][i] + dis
                rel = True
        return rel


def negative_cycle(adj, cost):
    t = NegCycleTree(adj, cost)
    return t.nc()



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
