# Least common ancestor Problem
#http://www.ics.uci.edu/~eppstein/261/BenFar-LCA-00.pdf
# Store Arrays: Parents: P[i] is the parent of i
#               Weights: W[i] is the length of tunnel i
#  Linearize the tree:
#   1. Store nodes visited on an Eulerian tour of the tree: E[i] O(n)
#   2. Node level: distance from the root. Compute L[i]          O(n)
#   3. Representative of a node: first visit in the Eulerian tour. Compute R[i].    O(n)

import sys
class Graph:
    def __init__(self,vertices):
        self.V = vertices #No. of vertices
        self.weight = [0] * self.V # An array. length[i] = length of tunnel from node i to its parent
        self.parent = [-1] * self.V # Another array.  Parent[i] = parent hill of hill i.
        self.E = [-1] * self.V # nodes visited on the Eulerian tour of the tree
        self.L = [-1] * self.V # Distance from the node to the root
        self.R = [-1] * self.V # First visit of i on the Eulerian tour



    def lca(self, node1, node2, q):
        """
        Find the lcs of node1, node2
        q - index of the query
        """
        #print("Find length from {} to {}".format(node1, node2))
        if node1 == 0:
            node1, node2 = node2, node1
        if node2 == 0:
            #print("node 2 is root!")
            path = self.ancestors[node1]
            path_length = 0
            #print("Path length: {}".format(path_length))
            for v in path:
                path_length = path_length + g.weight[v]
                #print("Path length: {}".format(path_length))

            return path_length


        path1 = self.ancestors[node1]
        path2 = self.ancestors[node2]
        i = 0
        j = 0
        while((i < len(path1)) and (j < len(path2)) and (path1[i] == path2[j])):
            i = i + 1
            j = j + 1

        path_length = 0
        while (i < len(path1)):
            path_length = path_length + self.weight[path1[i]]
            i = i + 1

        while (j < len(path2)):
            path_length = path_length + self.weight[path2[j]]
            j = j + 1

        return path_length



    def dfs(self, node):
        """
        Depth-first search algorithm
        """
        self.Time = self.Time + 1

        self.visited = True     
        for vertex in self.neighbours:
            if vertex.visited == False:
                vertex.dfs()    

    def print_neighbours(self, v):
        for node in self.graph[v]:
            sys.stdout.write("({},{})".format(v, node))
        sys.stdout.write("\n")


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
            g.weight[i] = weight
            g.addEdge(i, parent)
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
    for v in range(0, g.V):
        if v == 0:
            g.ancestors[0] = [0]            
        if v != 0:      
            path = [v]
            parent = g.parent[v]
            path.append(parent)
            while parent != 0: #while we're not yet at the root
                parent = g.parent[parent]
                path.append(parent)
            path = path[::-1]
            g.ancestors[v] = path

    #for v in range(0, len(g.ancestors)):
    #   sys.stdout.write("v: {}: {}\n".format(v, g.ancestors[v]))

    i = 1
    for (q1, q2) in q:
        sys.stdout.write("{} ".format(g.lca(q1, q2, i)))
        i = i + 1
    sys.stdout.write("\n")

