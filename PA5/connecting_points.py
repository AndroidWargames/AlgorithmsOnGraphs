# Uses python3
import sys
import math


def minimum_distance(x, y):
    bt = BinTree()
    find = list(range(len(x)))
    lists = [[i] for i in range(len(x))]
    result = 0

    # this will find distances for every unique combination of points
    # and then create nodes for the binary tree and add them to the
    # tree
    for i in range(len(x) - 1):
        for j in range(i+1,len(x)):
            d = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            bt.addNode(d, i, j)

    # this loop will iterate until a number of edges 1 fewer than the
    # number of points is discovered
    z = 0
    while z < len(x) - 1:
        # get minimum value, end points
        d, a, b = bt.popMin()
        # test if nodes are part of same sub tree, merge subtrees
        if find[a] != find[b]:
            # add dist to result
            result += d
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
    return result


# basic, unbalanced binary sort tree; worst case is as slow as array implementation
# nodes of tree represent edges sorted by distance. Each node also holds endpoints
# and key values (for some reason)
class BinTree:
    def __init__(self):
        self.count = 0
        self.root = self.Node

    class Node:
        def __init__(self, dist, a, b, k):
            self.dist = dist
            self.a = a
            self.b = b
            self.key = k
            self.parent = -1
            self.left = -1
            self.right = -1

    def addNode(self, dist, a, b):
        n = self.Node(dist, a, b, self.count)
        self.pushNode(n)
        self.count += 1

    def pushNode(self, n):
        if self.count == 0:
            self.root = n
        else:
            x = self.root
            a = self.root
            while a != -1:
                if n.dist >= x.dist:
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
            return [n.dist, n.a, n.b]
        else:
            n = self.root
            while n.left != -1:
                n = n.left
            if n.right != -1:
                n.right.parent = n.parent
                n.parent.left = n.right
            else:
                n.parent.left = -1
            return [n.dist, n.a, n.b]



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
