#Uses python3

import sys


class DijkstraTree:
    def __init__(self, adj, cost):
        self.size = len(adj)
        self.lim = sum(sum(i) for i in cost) + 1
        self.dist = [self.lim] * self.size
        self.adj = adj
        self.prev = [-1] * self.size
        self.unknown = [True] * self.size
        self.cost = cost

    def distance(self, s, g):
        self.dist[s] = 0
        self.unknown[s] = False
        for i in range(self.size):
            self.relax(s)
            p = s
            s = self.extractMin()
            if s == -1:
                break
            self.prev[s] = p
        if self.dist[g] == self.lim:
            return -1
        else:
            return self.dist[g]

    def extractMin(self):
        min = self.lim
        ind = -1
        for i in range(self.size):
            if self.unknown[i]:
                if self.dist[i] < min:
                    ind = i
                    min = self.dist[i]
        self.unknown[ind] = False
        return ind

    def relax(self, x):
        dis = self.dist[x]
        for i in range(len(self.adj[x])):
            if self.cost[x][i] + dis < self.dist[adj[x][i]]:
                self.dist[adj[x][i]] = self.cost[x][i] + dis


def distance(adj, cost, s, t):
    tree = DijkstraTree(adj, cost)
    return tree.distance(s, t)


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
