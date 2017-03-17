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
import itertools

sys.stdin = open('input.txt') # For testing on Windows
class Graph:
	def __init__(self, V, E):
		self.graph = defaultdict(list)
		self.V = V
		self.E = E

	def deleteVertex(self, v):
		self.graph.pop(v)

	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def find_independent_set(self, order):
		"""
		Given an order of vertices, find an independent set. 
		"""
		l = list() #initialize l to an empty set
		order = list(order)
		while (len(order) > 0): # while v is not empty:
			u = order.pop()
			l.append(u)
			for v in self.graph[u]:
				try:
					order.remove(v) # remove from list by value
				except ValueError:
					pass
		return l

	#def find_independent_set(self, order):

	def find_max(self):
		"""
		Sequential Algorithm as described on wikipedia
		"""
		self.vertices = [v for v in self.graph]

		# now find all permutations 
		max_size = 0
		max_set = list()
		for order in itertools.permutations(self.vertices):
			new_set = self.find_independent_set(order) 
			if len(max_set) > max_size:
				print('found solution')
				max_set = new_set
				max_size = len(max_set)
		return (max_set)

def minus(graph, v, flag):
	if flag: # take away v *and all it's neighbours*
		for u in graph[v]:
			graph.deleteVertex(u)
		graph.deleteVertex(v)
		sys.stdout.write("Found graph minus v and neighbours: ")
		return graph
	else: #just return without v
		sys.stdout.write("Found graph minus v: {}")
	graph.deleteVertex(v)
	sys.stdout.write("{}\n".format(graph))
	return(graph)

def maxIndSet(graph):
	sys.stdout.write("Finding maxIndSet of graph: {}\n".format(graph))
	if len(graph) == 0:
		return 0

	else:
		v = next(iter(graph)) #presumably any node in graph
		with_v = 1 + maxIndSet(minus(graph, v, True))
		without_v = maxIndSet(minus(graph, v, False))
		return(max(with_v, without_v))

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
	# degrees = [dict] # containing vertex : degree pairs
	# for u in graph:
	# 	degrees[u] = len(graph[u])
	
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