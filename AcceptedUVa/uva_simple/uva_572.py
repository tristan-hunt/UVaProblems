# /* UVa problem: 572
#  * Oil Deposits
#  * Topic: Other (Straightforward)
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *	This is another graph connectivity problem, with the graph
#  *  		input as a grid of characters. 
#  * Solution Summary:
#  *  Used DFS to find number of connected components. 
#  *  
#  * Used Resources:
#  * 
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import sys

class Graph:
	def __init__(self):
		self.vertices = list()
	
	def add_node(self, node):
		self.vertices.append(node)

	def print_graph(self):
		sys.stdout.write("All nodes in graph: ")
		sys.stdout.write("[")
		for v in self.vertices:
			sys.stdout.write("({},{})".format(v.m, v.n))
		sys.stdout.write("]\nNeighbours:\n")
		for v in self.vertices:
			sys.stdout.write("FOR NODE ({}, {}): ".format(v.m, v.n))
			v.print_neighbours()					


class Node:
	def __init__(self, m, n):
		self.m = m
		self.n = n
		self.neighbours = list()
		self.visited = False
	
	def add_neighbour(self, V):
		if V is not self and V not in self.neighbours:
			self.neighbours.append(V)
			V.add_neighbour(self)	

	def __repr__(self):
		return("(m, n)".format(self.m, self.n))

	def __str__(self):
		return("(m, n)".format(self.m, self.n))

	def print_neighbours(self):
		for node in self.neighbours:
			sys.stdout.write("({},{})".format(node.m, node.n))
		sys.stdout.write("\n")

def dfs(u):
	"""
	Depth-first search algorithm
	"""
	u.visited = True
	for vertex in u.neighbours:
		if vertex.visited == False:
			dfs(vertex)	
	# sys.stdout.write("{}".format(u))

def load():
	while(1):
		lines = list()
		size = next(sys.stdin).split()
		m = int(size[0])
		n = int(size[1])
		if m == 0:
			break
		for i in range(m):
			lines.append(next(sys.stdin))
		yield(m, n, lines)

for (m, n, lines) in load():
	graph = Graph()
	for i in range(m):
		line = lines[i]
		for j in range(n):
			if line[j] == '@':
				node = Node(i, j)
				graph.add_node(node)
				for v in graph.vertices:
					vm = v.m
					vn =  v.n
					if vm == i or vm == i-1 or vm == i+1:
						if vn == j or vn == j-1 or vn == j+1: 
							v.add_neighbour(node)
	num_components = 0
	for vertex in graph.vertices:
		if vertex.visited == False:
			num_components = num_components + 1
			dfs(vertex)
	sys.stdout.write("{}\n".format(num_components))

