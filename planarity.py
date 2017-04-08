import sys
from collections import defaultdict
#This class represents an undirected graph 
#using adjacency list representation

sys.stdin = open("input.txt") #dont forget to remove before submitting

class Graph:
  
	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

	def __str__(self):
		string = ""
		for u in self.graph:
			string = string + "{}: ".format(u)
			for v in self.graph[u]:
				string = string + "{} ".format(v)
			string = string + "\n"
		return string

	def removeVertex(self, v):
		"""
		function to remove a vertex v from the graph
		"""
		for u in self.graph[v]:
			self.graph[u].remove(v)
			self.graph.pop(v)
		self.V = self.V - 1

	def removeAndJoin(self, v):
		"""
		function to remove a vertex and join its two neighbours, instead
		"""
		n1 = self.graph[v][0]
		n2 = self.graph[v][1]
		self.graph[n1].remove(v)
		self.graph[n2].remove(v)
		self.addEdge(n1, n2)
		self.V = self.V - 1
		self.graph.pop(v)


	def addEdge(self,u,v):
		"""
		function to add an edge to graph
		"""
		self.graph[u].append(v)
		self.graph[v].append(u)
    
	def isK33(self):
		"""
		Checks if it is K33
		"""
		if self.V != 6:
			return False
		for v in self.graph:
			if len(self.graph[v]) != 3:
				return False
		return True

	def isK5(self):
		"""
		A very introspective method. Am I non-planar?
		"""
		if self.V != 5:
			return False
		for v in self.graph:
			if len(self.graph[v]) != 4:

				return False
		return True

	def rule1(self):
		"""
		Attempts to remove a vertex of degree 1 and its incident edge
		Returns 1 on success, 0 otherwise
		"""
		for u in self.graph:
			if len(self.graph[u]) == 1:
				self.removeVertex(u)
				return 1
		return 0

	def rule2(self):
		"""
		Attempts to remove a vertex of degree 2 and its incident edge, and 
		replace with a new edge that joins the two nodes adj. to v. 
		Returns 1 on success, 0 otherwise
		"""
		for u in self.graph:
			if len(self.graph[u]) == 2:
				self.removeAndJoin(u)
				return 1
		return 0



def load():
	while(1):
		try:
			line = next(sys.stdin).split()
		except StopIteration:
			break

		n = int(line[0])
		m = int(line[1])
		g = Graph(n)
		for i in range(0, m):
			edge = next(sys.stdin).split()
			v1 = int(edge[0])
			v2 = int(edge[1])
			g.addEdge(v1, v2)
		yield(g)

for (g) in load():   			
	while(1):
		r1 = g.rule1()
		r2 = g.rule2()
		if (r1 == 0) and (r2 == 0):
			break

	if g.isK5() == True:
		sys.stdout.write("NO\n")
	
	elif g.isK33() == True:
		sys.stdout.write("NO\n")
	else:
		sys.stdout.write("YES\n")
