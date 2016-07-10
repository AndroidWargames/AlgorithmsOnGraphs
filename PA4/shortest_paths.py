#Uses python3

import sys
import queue

class ShortestPathTree:
    def __init__(self, adj, cost):
        self.size = len(adj)
        self.reachable = [0] * self.size
        self.shortest = [1] * self.size
        self.lim = sum(sum(abs(j) for j in i) for i in cost) + 1
        self.dist = [self.lim] * self.size
        self.adj = adj
        self.prev = [-1] * self.size
        self.cost = cost

    def sPath(self, s):
        self.dist[s] = 0
        self.reachable[s] = 1
        for i in range(self.size*2):
            r = False
            for j in range(self.size):
                r = r or self.relax(j, i >= self.size)
            if not r:
                break

    def relax(self, x, r2):
        rel = False
        dis = self.dist[x]
        for i in range(len(self.adj[x])):
            node = adj[x][i]
            if self.cost[x][i] + dis < self.dist[node]:
                self.dist[node] = self.cost[x][i] + dis
                rel = True
                if r2:
                    self.shortest[node] = 0
                else:
                    self.reachable[node] = 1
        return rel


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
    s = data[0]
    s -= 1
    t = ShortestPathTree(adj, cost)
    t.sPath(s)
    for x in range(n):
        if t.reachable[x] == 0:
            print('*')
        elif t.shortest[x] == 0:
            print('-')
        else:
            print(t.dist[x])

