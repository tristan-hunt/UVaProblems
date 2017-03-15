import time

import sys
class Graph:
	def __init__(self, map, node_char):
		"""
		Given a list of strings which represent a grid, 
		Make a graph. 
		node_char is the char which represents a node. 
		"""
		self.vertices = list()
		for i in range(0, len(map)):
			row = map[i]
			for j in range(0, len(row)):
				if row[j] == node_char:
					node = Node(i, j)
					self.vertices.append(node)
					for v in self.vertices:
						vm = v.m
						vn = v.n
						if (vm == i-1 or vm == i + 1) and vn == j :
							v.add_neighbour(node)
						elif (vn == j-1 or vn == j+1) and vm == i:
							v.add_neighbour(node)

	def find_components(self):
		num_components = 0
		sys.stdout.write("Components: ")
		for vertex in self.vertices:
			if vertex.visited == False:
				num_components = num_components + 1
				vertex.dfs_flood()
				sys.stdout.write("||")
		sys.stdout.write("\n")
		return num_components							
		
	def reset_components(self):
		for v in self.vertices:
			self.vertices[v].visited = False	

	def print_graph(self):
		sys.stdout.write("Vertices: ")
		for v in self.vertices:
			sys.stdout.write("({},{})".format(v.m, v.n))
		for v in self.vertices:
			v.print_neighbours()

		sys.stdout.write("\n")

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

	def dfs_flood(self):
		"""
		Depth-first search algorithm
		"""
		self.visited = True
		sys.stdout.write("({}, {}) ".format(self.m, self.n))
		for vertex in self.neighbours:
			if vertex.visited == False:
				vertex.dfs_flood()	
		# sys.stdout.write("{}".format(u))

	def __repr__(self):
		return("({}, {})".format(self.m, self.n))

	def __str__(self):
		return("({}, {})".format(self.m, self.n))

	def print_neighbours(self):
		sys.stdout.write("Node ({}, {}) has neighbours: ".format(self.m, self.n))
		for node in self.neighbours:
			sys.stdout.write("({},{})".format(node.m, node.n))
		sys.stdout.write("\n")



def load(num_cases):

	for case in range(0, num_cases+1):
		map = list()
		cells = list()
		while(1):
			next_line = next(sys.stdin)
			if next_line[0] == 'L' or next_line[0] == 'W':
				map.append(next_line)
			else: 
				line = (next_line.split())
				break
		
		while(1):
			try:
				i = int(line[0]) 
			except IndexError:
				break
			j = int(line[1]) 
			cells.append((i, j))
			line = next(sys.stdin).split()
		yield(map, cells)

def main():
	num_cases = int(next(sys.stdin))
	next(sys.stdin)
	case = 1
	for (map, cells) in load(num_cases):	
		if case == 0:
			sys.stdout.write("\n")
		case = 0
		for node in cells:
			sys.stdout.write("{}\n".format(5))
main()
