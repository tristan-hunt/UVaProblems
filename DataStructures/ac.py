# Least common ancestor Problem
#http://www.ics.uci.edu/~eppstein/261/BenFar-LCA-00.pdf
# http://code.activestate.com/recipes/498243-finding-eulerian-path-in-undirected-graph/
# http://codereview.stackexchange.com/questions/104074/eulerian-tour-in-python
# Store Arrays: Parents: P[i] is the parent of i
#               Weights: W[i] is the length of tunnel i
#  Linearize the tree:
#   1. Store nodes visited on an Eulerian tour of the tree: E[i] O(n)
#   2. Node level: distance from the root. Compute L[i]          O(n)
#   3. Representative of a node: first visit in the Eulerian tour. Compute R[i].    O(n)
from collections import defaultdict
import sys

class Graph:
    def __init__(self,vertices):
        self.V = vertices #No. of vertices
        self.weight = [0] * self.V # An array. length[i] = length of tunnel from node i to its parent
        self.parent = [0] * self.V # Another array.  Parent[i] = parent hill of hill i.
        self.children = defaultdict(list)
        self.level = [-1]*self.V # Distance from the node to the root
        self.E = list() # nodes visited on the Eulerian tour of the tree
        self.L = list()
        self.R = list() # First visit of i on the Eulerian tour
        self.RMQ = dict()
        self.depth = 0
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def eulerTour(self, current):
        queue = [current]
        self.E = [current]
        current = self.graph[current].pop()
        while(queue):
            if self.graph[current]:
                queue.append(current)
                current = self.graph[current].pop()
            else:
                current = queue.pop()
                self.E.append(current)
        #print(self.E)


    def findDepth(self, curr, level):
        self.level[curr] = level
        for v in self.children[curr]:
            if self.level[v] == -1 :
                self.findDepth(v, level+1)
        self.level

    def makeR(self):
        """
        Create array R
        """
        for v in range(0, self.V):
            self.R.append(self.E.index(v))

    
    def rmq(self, L, j, k):
        """
        Return the index of the of self.L between i and j. 
        First try with DP? 
        """
        if (j, k) in self.RMQ:
            return self.RMQ[(j, k)]

        if (j+1 == k):
            if self.L[j] < self.L[k]:
                self.RMQ[(j, k)] = j
                return j
            else:
                self.RMQ[(j, k)] = k
                return k

        for i in range(j+1, k):
            left = self.rmq(L, j, i)
            right = self.rmq(L, i, k)
            if (L[left] < L[right]):
                self.RMQ[(j, k)] = left
                return left
            else:
                self.RMQ[(j, k)] = right
                return right



    def lca(self, u, v):
        """
        The nodes in the Euler tour between the first visits to u and v are E[R[u], .... E[R[v]]
        The shallowest node in this subtour is at index RMQ(R[u], R[v]) (since L records the level)
        The node at this position is E[RMQ(R[u], R[v])]
        """
        j = self.R[u]
        k = self.R[v]
        if j > k:
            return(self.lca(v, u))
        i = self.rmq(self.L, j, k)
        return i


    def WStr(self):
        string = "W:"
        for i in range(0, len(self.weight)):
            string += " {}".format(self.weight[i])
        return string


    def RStr(self):
        string = "R:"
        for i in range(0, len(self.R)):
            string += " {}".format(self.R[i])
        return string


    def LevelStr(self):
        string = "L:"
        for i in range(0, len(self.L)):
            string += " {}".format(self.L[i])
        return string


    def EulerStr(self):
        string = "E:"
        for i in range(0, len(self.E)):
            string += " {}".format(self.E[i])
        return string

    def parentsStr(self):
        string = "parents: \n"
        for v in range(0, self.V):
            string += "{}: {}, w:{}\n".format(v, self.parent[v], self.weight[v])
        return string

    def childrenStr(self):
        string = "children: \n"
        for v in range(0, self.V):
            string += "{}:".format(v)
            for c in range(0, len(self.children[v])):
                string += " {}".format(self.children[v][c])
            string += "\n"
        return string


def load():
    V = int(next(sys.stdin))
    #sys.stdout.write("V: {}\n".format(V))
    i = 1
    while(V != 0):
        g = Graph(V)
        while(i<V):
            line = next(sys.stdin).split()
            parent = int(line[0])
            weight = int(line[1])
            g.addEdge(i, parent)
            g.parent[i] = parent
            g.children[parent].append(i)
            g.weight[i] = weight
            i = i + 1

        Q = int(next(sys.stdin))
        queries = list()
        i = 0
        while(i < Q):
            line = next(sys.stdin).split()
            q1 = int(line[0])
            q2 = int(line[1])
            queries.append((q1, q2))
            i = i + 1

        yield(g, queries)
        V = int(next(sys.stdin))
        i = 1

for (g, q) in load():
    g.eulerTour(0)
    try:
        g.findDepth(0, 0)
    except Exception:
        quit()

    for e in g.E:
            g.L.append(g.level[e])
    g.makeR()

    for i in range(0, g.V-1):
        for j in range(1, g.V):
            g.lca(j, i)

    first = 0 
    for i in range(0, len(q)):
        v = q[i][0]
        w = q[i][1]
        i = g.lca(v, w)
        ancestor = g.E[i]
        path_length = 0


        curr = v
        while(curr != ancestor):
            child = curr
            parent = g.parent[curr]
            parent_level = g.L[g.R[parent]]
            path_length = path_length + g.weight[curr]
            curr = parent


        curr = w
        while(curr != ancestor):
            child = curr
            parent = g.parent[curr]
            parent_level = g.L[g.R[parent]]
            path_length = path_length + g.weight[curr]
            curr = parent

        if first == 0:
            sys.stdout.write("{}".format(path_length))
            first = 1
        else:
            sys.stdout.write(" {}".format(path_length))

    sys.stdout.write("\n")
