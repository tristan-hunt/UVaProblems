# Least common ancestor Problem
#http://www.ics.uci.edu/~eppstein/261/BenFar-LCA-00.pdf
# Store Arrays: Parents: P[i] is the parent of i
#               Weights: W[i] is the length of tunnel i
#  Linearize the tree:
#   1. Store nodes visited on an Eulerian tour of the tree: E[i] O(n)
#   2. Node level: distance from the root. Compute L[i]          O(n)
#   3. Representative of a node: first visit in the Eulerian tour. Compute R[i].    O(n)
from collections import defaultdict
import sys


#sys.stdin = open("input.txt") # DONT FORGET TO REMOVE BEFORE SUBMITTING!!

class Graph:
    def __init__(self,vertices):
        self.V = vertices #No. of vertices
        self.weight = [0] * self.V # An array. length[i] = length of tunnel from node i to its parent
        self.parent = [0] * self.V # Another array.  Parent[i] = parent hill of hill i.
        self.children = defaultdict(list)
        self.E = list() # nodes visited on the Eulerian tour of the tree
        self.L = list() # Distance from the node to the root
        self.R = list() # First visit of i on the Eulerian tour
        self.RMQ = dict()
        self.depth = 0


    def eulerTour2(self, node):
        """
        To be called once weight, parent are created, to create eulerTour.
        """
        self.E.append(node)
        self.L.append(self.depth)
        for c in self.children[node]:
            self.depth += 1
            self.eulerTour1(c)

            self.depth -= 1
            self.E.append(node)
            self.L.append(self.depth)
    

    def eulerTour(self, node):
        """
        To be called once weight, parent are created, to create eulerTour.
        """
        self.E.append(node)
        self.L.append(self.depth)
        for c in self.children[node]:
            self.depth += 1
            self.eulerTour(c)

            self.depth -= 1
            self.E.append(node)
            self.L.append(self.depth)

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


        # sys.stdout.write("E: ")
        # for i in range(j, k+1):
        #     sys.stdout.write("{} ".format(self.E[i]))
        # sys.stdout.write("\nL: ") 
        # for i in range(j, k+1):
        #     sys.stdout.write("{} ".format(self.L[i]))
        # sys.stdout.write("\n") 
        #print(i)
        #print(self.L[i])
        #print(self.E[i])

    def slow_lca(self, node1, node2, q):
        """
        Find the lcs of node1, node2
        q - index of the query
        """
        if node1 == 0: node1, node2 = node2, node1
        if node2 == 0:
            path = self.ancestors[node1]
            path_length = 0
            for v in path:
                path_length = path_length + g.weight[v]
            return path_length
        path1, path2 = self.ancestors[node1], self.ancestors[node2]
        i, j = 0, 0
        while((i < len(path1)) and (j < len(path2)) and (path1[i] == path2[j])):
            i += 1
            j += 1
        path_length = 0
        while (i < len(path1)):
            path_length = path_length + self.weight[path1[i]]
            i += 1
        while (j < len(path2)):
            path_length = path_length + self.weight[path2[j]]
            j += 1
        return path_length

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
	#print(g.parentsStr())
	#print(g.childrenStr())
    g.eulerTour(0)
    g.makeR()
	#print(g.EulerStr())
	#print(g.LevelStr())
	#print(g.RStr())
	#print(g.WStr())


	#print("Q: " + str(q))
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

			#sys.stdout.write("Parent {} has level: {} adding length {}\n".format(parent, parent_level, g.weight[curr]))
            path_length = path_length + g.weight[curr]
			#sys.stdout.write("Path length is now: {}\n".format(path_length))
            curr = parent


        curr = w
        while(curr != ancestor):
            child = curr
            parent = g.parent[curr]
            parent_level = g.L[g.R[parent]]

			#sys.stdout.write("Parent {} has level: {} adding length {}\n".format(parent, parent_level, g.weight[curr]))
            path_length = path_length + g.weight[curr]
			#sys.stdout.write("Path length is now: {}\n".format(path_length))
            curr = parent

        if first == 0:
            sys.stdout.write("{}".format(path_length))
            first = 1
        else:
            sys.stdout.write(" {}".format(path_length))

    sys.stdout.write("\n")




# for (g, q) in load():
#     for v in range(0, g.V):
#         if v == 0:
#             g.ancestors[0] = [0]            
#         if v != 0:      
#             path = [v]
#             parent = g.parent[v]
#             path.append(parent)
#             while parent != 0: #while we're not yet at the root
#                 parent = g.parent[parent]
#                 path.append(parent)
#             path = path[::-1]
#             g.ancestors[v] = path

#     #for v in range(0, len(g.ancestors)):
#     #   sys.stdout.write("v: {}: {}\n".format(v, g.ancestors[v]))

#     i = 1
#     for (q1, q2) in q:
#         sys.stdout.write("{} ".format(g.lca(q1, q2, i)))
#         i = i + 1
#     sys.stdout.write("\n")

