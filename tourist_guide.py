import sys

# Code borrowed from: http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
# Python program to find articulation points in an undirected graph
  
from collections import defaultdict
  
#This class represents an undirected graph 
#using adjacency list representation

#possible optimizations:
# modify graph to deal with strings as vertices directly, instead of converting before/after processing.

class Graph:
  
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.Time = 0

	def addEdge(self,u,v):
		"""
		function to add an edge to graph
		"""
		self.graph[u].append(v)
		self.graph[v].append(u)

	def APUtil(self,u, visited, ap, parent, low, disc):
		"""
  		A recursive function that find articulation points 
    	using DFS traversal
    	u --> The vertex to be visited next
    	visited[] --> keeps tract of visited vertices
    	disc[] --> Stores discovery times of visited vertices
    	parent[] --> Stores parent vertices in DFS tree
    	ap[] --> Store articulation points
    	"""
        #Count of children in current node 
		children = 0
 
        # Mark the current node as visited and print it
		visited[u]= True
 
        # Initialize discovery time and low value
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1
 
        #Recur for all the vertices adjacent to this vertex
		for v in self.graph[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
			if visited[v] == False :
				parent[v] = u
				children += 1
				self.APUtil(v, visited, ap, parent, low, disc)
 
                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
				low[u] = min(low[u], low[v])
 
                # u is an articulation point in following cases
                # (1) u is root of DFS tree and has two or more chilren.
				if parent[u] == -1 and children > 1:
					ap[u] = True
 
                #(2) If u is not root and low value of one of its child is more
                # than discovery value of u.
				if parent[u] != -1 and low[v] >= disc[u]:
					ap[u] = True   
                     
                # Update low value of u for parent function calls   
			elif v != parent[u]: 
				low[u] = min(low[u], disc[v])
 
 
    #The function to do DFS traversal. It uses recursive APUtil()
	def AP(self):
  
        # Mark all the vertices as not visited 
        # and Initialize parent and visited, 
        # and ap(articulation point) arrays
		cameras = list()
		visited = [False] * (self.V)
		disc = [float("Inf")] * (self.V)
		low = [float("Inf")] * (self.V)
		parent = [-1] * (self.V)
		ap = [False] * (self.V) #To store articulation points
 
        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
		for i in range(self.V):
			if visited[i] == False:
				self.APUtil(i, visited, ap, parent, low, disc)
 
		for index, value in enumerate (ap):
			if value == True: 
				cameras.append(index)
		return(cameras)

def load():
	# Create a graph given in the above diagram
	while(1):
		size = int(next(sys.stdin))
		if size == 0:
			break
		g1 = Graph(size)
		locations = list()
		for i in range(size):
			locations.append(next(sys.stdin).strip())
		num_routes = int(next(sys.stdin))
		for i in range(num_routes):
			route = next(sys.stdin).split()
			g1.addEdge(locations.index(route[0]), locations.index(route[1]))
		yield(g1, locations)

case_num = 1
for g, locations in load():
	cameras =  g.AP()
	if case_num != 1:
		sys.stdout.write("\n")
	sys.stdout.write("City map #{}: {} camera(s) found\n".format(case_num, len(cameras)))
	cameras = [locations[c] for c in cameras]
	cameras.sort()
	for c in cameras:
		sys.stdout.write("{}\n".format(c))
	case_num = case_num + 1

	# g1 = Graph(6)
	# locations = ["sugarloaf",'macarena', "copacabana", "ipanema", "corcovado", "lapa", "madeUpTown"] 

	# g1.addEdge(3, 2)
	# g1.addEdge(2, 0)
	# g1.addEdge(3, 0)
	# g1.addEdge(1, 5)
	# g1.addEdge(0, 1)
	# g1.addEdge(4, 0)
	# g1.addEdge(5, 4)
	# yield(g1, locations)

	# g2 = Graph(4)
	# g2.addEdge(0, 1)
	# g2.addEdge(1, 2)
	# g2.addEdge(2, 3)
	# yield(g2, locations)


	# g3 = Graph (7)
	# g3.addEdge(0, 1)
	# g3.addEdge(1, 2)
	# g3.addEdge(2, 0)
	# g3.addEdge(1, 3)
	# g3.addEdge(1, 4)
	# g3.addEdge(1, 6)
	# g3.addEdge(3, 5)
	# g3.addEdge(4, 5)
	# yield(g3, locations)

