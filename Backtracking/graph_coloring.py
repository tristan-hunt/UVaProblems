# /* UVa problem: <193>
#  *
#  * Topic: Backtracking
#  *
#  * Level: easy/challenging
#  * 
#  * Brief problem description: 
#  *
#  *   ...
#  *
#  * Solution Summary:
#  *
#  *   Sequential Algorithm - runs in O(n) time. 
#  *
#  * Used Resources:
#  *
#  *   https://en.wikipedia.org/wiki/Maximal_independent_set#Finding_a_single_maximal_independent_set
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  *
#  * --------------------- Tristan Hunt
#  *
import sys
from collections import defaultdict

class Graph:
	def __init__(self, V, E):
		self.graph = defaultdict(list)
		self.V = V
		self.E = E

	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def find_max(self):
		"""
		Sequential Algorithm as described on wikipedia
		"""
		self.l = list() #initialize l to an empty set
		self.vertices = [v for v in self.graph]
		while (len(self.vertices) > 0): # while v is not empty:
			u = self.vertices.pop()
			self.l.append(u)
			for v in self.graph[u]:
				try:
					self.vertices.remove(u) # remove from list by value
				except ValueError:
					pass

def load():
	num_cases = int(sys.stdin.readline())
	for i in range(num_cases):
		info = sys.stdin.readline().split(' ')
		num_edges = int(info[1])
		num_nodes = int(info[0])
		g = Graph(num_edges, num_nodes)
		for j in range(0, num_edges):
			edge = next(sys.stdin).split()
			g.addEdge(int(edge[0]), int(edge[1]))
		try:
			assert(len(g.graph) == num_nodes)
		except AssertionError:
			for u in range(0, n):
				if u not in g.graph:
					g.graph[u] = list()
		yield(g)
		next(sys.stdin)

for g in load():
	g.find_max()
	for element in g.l:
		sys.stdout.write("{} ".format(element))