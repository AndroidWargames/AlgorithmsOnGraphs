#Uses python3
import sys
import math


def clustering(x, y, k):
    bt = BinTree()
    find = list(range(len(x)))
    lists = [[i] for i in range(len(x))]

    # this will find distances for every unique combination of points,
    # create edge objects for each, and then add that edge object and distance
    # to the binary tree as a node
    for i in range(len(x) - 1):
        for j in range(i+1,len(x)):
            d = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            e = Edge(d, i, j)
            bt.addNode(e, e.dist)

    # this loop will iterate until a number of edges k fewer than the
    # number of points (n) is discovered. this will create k clusters
    # because we begin with n clusters. in each subtree/cluster
    # merge operation, the number of subtrees is subtracted by 1.
    z = 0
    while z < len(x) - k:
        # get minimum value, end points
        e = bt.popMin()
        d, a, b = e.dist, e.a, e.b
        # test if nodes are part of same subtree/cluster, merge subtrees
        if find[a] != find[b]:
            # add dist to result

            # lists[] contains a list of subtree contents. Initially, all
            # elements belong to their own subtree. When subtrees are merged,
            # the index of the subtree value for each vertex (stored in find[])
            # in the 'b' subtree is updated to match those of the 'a' subtree.
            # Then, each vertex of 'b' is added to 'a'. Deleting the 'b' subtree
            # isn't necessary, as the find[] list will no longer reference that
            # subtree's index.
            for i in lists[find[b]]:
                lists[find[a]].append(i)
                find[i] = find[a]
            z += 1
    # once we've discovered k clusters, we simply extract the next smallest
    # distance between two points that would span between two clusters
    while True:
        # get minimum value, end points
        e = bt.popMin()
        d, a, b = e.dist, e.a, e.b
        # test if nodes are part of same sub tree, merge subtrees
        if find[a] != find[b]:
            break
    return e.dist


class Edge:
    def __init__(self, d, a, b):
        self.a = a
        self.b = b
        self.dist = d

# basic, unbalanced binary sort tree; worst case is as slow as array implementation
# nodes of tree represent edges sorted by distance. Each node holds key value
# that references an object in BinTree's 'objs' list


class BinTree:
    def __init__(self):
        self.count = 0
        self.root = self.Node
        self.objs = []

    class Node:
        def __init__(self, val, k):
            self.val = val
            self.key = k
            self.parent = -1
            self.left = -1
            self.right = -1

    def addNode(self, obj, val):
        n = self.Node(val, self.count)
        self.objs.append(obj)
        self.pushNode(n)
        self.count += 1

    def pushNode(self, n):
        if self.count == 0:
            self.root = n
        else:
            x = self.root
            a = self.root
            while a != -1:
                if n.val >= x.val:
                    a = x.right
                    if a == -1:
                        x.right = n
                        n.parent = x
                else:
                    a = x.left
                    if a == -1:
                        x.left = n
                        n.parent = x
                x = a

    def popMin(self):
        if self.root.left == -1:
            n = self.root
            if self.root.right != -1:
                self.root = self.root.right
                self.root.parent = -1
            else:
                self.root = -1
            return self.objs[n.key]
        else:
            n = self.root
            while n.left != -1:
                n = n.left
            if n.right != -1:
                n.right.parent = n.parent
                n.parent.left = n.right
            else:
                n.parent.left = -1
            return self.objs[n.key]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
