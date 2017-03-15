# Find number of maximal connected subgraphs

import sys
import string

class Node:
	def __init__(self, name):
		self.name = name
		self.neighbours = list()
		self.visited = False
	
	def add_neighbour(self, V):
		if V is not self and V not in self.neighbours:
			self.neighbours.append(V)
			V.add_neighbour(self)	

	def dfs(self):
		"""
		Depth-first search algorithm
		"""
		self.visited = True
		for vertex in self.neighbours:
			if vertex.visited == False:
				vertex.dfs()	

	def __repr__(self):
		return("({})".format(self.name))

	def __str__(self):
		return("({})".format(self.name))

	def print_neighbours(self):
		for node in self.neighbours:
			sys.stdout.write("({},{})".format(node.m, node.n))
		sys.stdout.write("\n")

def load_edges():
	edges = list()
	while(1):
		edge = next(sys.stdin).strip()
		try:
			if ord(edge[0]) <= 90 and ord(edge[0]) >= 65:
				edges.append(edge)
		except Exception:
			break
		yield(edges)


def load(num_cases):
	while(num_cases):
		largest = next(sys.stdin).strip()
		edges = list()
		for e in load_edges():
			edges = e
		
		yield(largest, edges)
		num_cases = num_cases -1
						
num_cases = int(next(sys.stdin))
next(sys.stdin)
case = 0
for (largest, edges) in load(num_cases):
	if case == 1:
		sys.stdout.write("\n")
	case = 1
	num_components = 0
	vertices = list(string.ascii_uppercase)[:ord(largest)-64]
	vertices = [Node(i) for i in vertices]
	for edge in edges:
		n1 = ord(edge[0])-65
		node1 = vertices[n1]

		n2 = ord(edge[1])-65
		node2 = vertices[n2]
		node1.add_neighbour(node2)
	for vertex in vertices:
		if vertex.visited == False:
			num_components = num_components + 1
			vertex.dfs()
	sys.stdout.write("{}\n".format(num_components))
