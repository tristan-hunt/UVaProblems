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
#  *   Sequential Algorithm - runs in O(n) time (for finding ANY independent set)
#  *   Find all independent sets, then choose one of the largest ones. 
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

#sys.stdin = open('input.txt') # For testing on Windows
class Graph:
	def __init__(self, V, E):
		self.graph = defaultdict(list)
		self.V = V
		self.E = E

	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

def min_degree(graph, k):
	"""
	Find the vertex of minimal degree
	"""
	min_degree = k+1
	#sys.stdout.write("finding the degrees of: {}; min_degree = {}\n".format(graph, min_degree))
	for v in graph:
		#sys.stdout.write(" vertex {} has degree: {}".format(v, len(graph[v])))
		deg = len(graph[v])
		if deg < min_degree:
			#sys.stdout.write(" It's smaller! {} < {}; so vertex {} is minimal \n".format(deg, min_degree, v))
			min_degree = deg
			u = v
	#sys.stdout.write("\t the min degree is vertex {}\n".format(u))
	return u

def greedy(graph, k):
	S = list()
	
	while(len(graph) > 0):
		# find u --> vertex of minimal degree
		u = min_degree(graph, k)
		S.append(u)
		for neighbour in graph[u]:
			graph.pop(neighbour, None)
		graph.pop(u)
	return S

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
			for u in range(0, num_nodes):
				if u not in g.graph:
					g.graph[u] = list()
		yield(g, num_edges)
		next(sys.stdin)

for g, k in load():
	max_ind_set = greedy(g.graph, k)
	sys.stdout.write("{}\n".format(len(max_ind_set)))
	for element in max_ind_set:
		sys.stdout.write("{} ".format(element))