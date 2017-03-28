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
def load():
	num_cases = int(next(sys.stdin))
	for i in range(0, num_cases):
		info = next(sys.stdin).split()
		n = int(info[0])
		g = Graph(n)
		m = int(info[1])
		for j in range(0, m):
			edge = next(sys.stdin).split()
			g.addEdge(int(edge[0])-1, int(edge[1])-1) #since we use these as indexes
			try:
				assert(len(g.graph) == n)
			except AssertionError:
				for u in range(0, n):
					if u not in g.graph:
						g.graph[u] = list()
		print(g.graph)
		yield(g)



for g in load(): 
	sys.stdout.write("Following are strongly connected components in given graph\n")
	num = g.SCC()



