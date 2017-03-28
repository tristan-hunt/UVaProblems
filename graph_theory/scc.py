import sys
# Resource Used:
#http://www.geeksforgeeks.org/strongly-connected-components/# Python program to find articulation points in an undirected graph
# https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm 
from collections import defaultdict
  
class Graph:
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph
		self.Time = 0
		self.visited = [False]*self.V
		self.stack = list()
		self.components = list()

	def reset_dfs(self):
		self.visited = [False]*self.V

	def addEdge(self,u,v):
		"""
		function to add an edge to graph
		"""
		self.graph[u].append(v)

	def dfsUtil(self, u):
		self.visited[u] = True
		if u not in self.components:
			self.components.append(u)
			sys.stdout.write("{} ".format(u))
		for v in self.graph[u]: # for neighbours of u
			if self.visited[v] == False:
				self.dfsUtil(v)
			
	def fillStack(self, u):
		
		self.visited[u] = True
		for v in self.graph[u]: # for neighbours of u
					
			if self.visited[v] == False:
				self.fillStack(v)
		
			
		self.stack.append(u) #when applying SCC

	def transpose(self):
		
		rg = Graph(self.V)
		for u in self.graph:
				
			for v in self.graph[u]:
				rg.addEdge(v, u)
			

		return rg


	def SCC(self):
		num_scc = 0
		for u in self.graph:
			
			if self.visited[u] == False:
				
				self.fillStack(u)
					
		gr = self.transpose()
		self.reset_dfs()
		
		while len(self.stack) > 0:
			v = self.stack.pop()
			if self.visited[v] == False:
				gr.dfsUtil(v)
				sys.stdout.write("\n")
				num_scc = num_scc + 1
		return num_scc


# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.graph[4] = list()
assert(len(g.graph) == 5)

print ("Following are strongly connected components " +
						"in given graph")
num = g.SCC()













# def APUtil(self,u, visited, ap, parent, low, disc):
# 	"""
#  		A recursive function that find articulation points 
#     	using DFS traversal
#     	u --> The vertex to be visited next
#     	visited[] --> keeps tract of visited vertices
#     	disc[] --> Stores discovery times of visited vertices
#     	parent[] --> Stores parent vertices in DFS tree
#     	ap[] --> Store articulation points
#     	"""
#         #Count of children in current node 
# 		children = 0
 
#         # Mark the current node as visited and print it
# 		visited[u]= True
 
#         # Initialize discovery time and low value
# 		disc[u] = self.Time
# 		low[u] = self.Time
# 		self.Time += 1
 
#         #Recur for all the vertices adjacent to this vertex
# 		for v in self.graph[u]:
#             # If v is not visited yet, then make it a child of u
#             # in DFS tree and recur for it
# 			if visited[v] == False :
# 				parent[v] = u
# 				children += 1
# 				self.APUtil(v, visited, ap, parent, low, disc)
 
#                 # Check if the subtree rooted with v has a connection to
#                 # one of the ancestors of u
# 				low[u] = min(low[u], low[v])
 
#                 # u is an articulation point in following cases
#                 # (1) u is root of DFS tree and has two or more chilren.
# 				if parent[u] == -1 and children > 1:
# 					ap[u] = True
 
#                 #(2) If u is not root and low value of one of its child is more
#                 # than discovery value of u.
# 				if parent[u] != -1 and low[v] >= disc[u]:
# 					ap[u] = True   
                     
#                 # Update low value of u for parent function calls   
# 			elif v != parent[u]: 
# 				low[u] = min(low[u], disc[v])
 
 
#     #The function to do DFS traversal. It uses recursive APUtil()
# 	def AP(self):
  
#         # Mark all the vertices as not visited 
#         # and Initialize parent and visited, 
#         # and ap(articulation point) arrays
# 		articulation_points = list()
# 		visited = [False] * (self.V)
# 		disc = [float("Inf")] * (self.V)
# 		low = [float("Inf")] * (self.V)
# 		parent = [-1] * (self.V)
# 		ap = [False] * (self.V) #To store articulation points
 
#         # Call the recursive helper function
#         # to find articulation points
#         # in DFS tree rooted with vertex 'i'
# 		for i in range(self.V):
# 			if visited[i] == False:
# 				self.APUtil(i, visited, ap, parent, low, disc)
 
# 		for index, value in enumerate (ap):
# 			if value == True: 
# 				articulation_points.append(index)
# 		return(articulation_points)