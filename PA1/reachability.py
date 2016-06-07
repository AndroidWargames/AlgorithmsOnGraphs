#Uses python3

import sys


def reach(adj, x, y):
    nodes = [Node(i) for i in range(len(adj))]
    for i in range(len(nodes)):
        for j in adj[i]:
            nodes[i].a.append(nodes[j])
    nodes[x].explore()
    if nodes[y].found:
        return 1
    else:
        return 0


class Node:
    def __init__(self, index):
        self.a = []
        self.x = index
        self.found = False

    def explore(self):
        self.found = True
        for i in self.a:
            if not i.found:
                i.explore()


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
