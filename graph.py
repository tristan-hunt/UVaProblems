import time

import sys

class Graph:
	def __init__(self, map, node_char):
		"""
		The dictionary keys are the tuples (i, j), the value
		is the Node object that is represented.
	
		Given a list of strings which represent a grid, 
		Make a graph. 
		node_char is the char which represents a node. 
		"""
		self.vertices = dict()
	
		for i in range(1, len(map)+1):
			row = map[i-1]
			for j in range(1, len(row)+1):
				if row[j-1] == node_char:
					self.vertices[(i, j)] = Node(i, j)
					for v in self.vertices:
						vm = self.vertices[v].m
						vn = self.vertices[v].n
						if abs(vm -i) <2 and abs(vm-j) <2:
							self.vertices[v].add_neighbour(self.vertices[(i, j)])
					
		
	def reset_components(self):
		for v in self.vertices:
			self.vertices[v].visited = False	

class Node:
	def __init__(self, m, n):
		self.m = m
		self.n = n
		self.neighbours = list()
		self.visited = False
		self.size = 1
	
	def add_neighbour(self, V):
		if V is not self and V not in self.neighbours:
			self.neighbours.append(V)
			V.add_neighbour(self)	


	def find_size(self):
		self.visited = True
		size = 1
		for vertex in self.neighbours:
			if vertex.visited == False:
				size = size + vertex.find_size()
		return(size)

	def dfs(self):
		"""
		Depth-first search algorithm
		"""
		self.visited = True
		for vertex in u.neighbours:
			if vertex.visited == False:
				vertex.dfs()	
		# sys.stdout.write("{}".format(u))

	def __repr__(self):
		return("({}, {})".format(self.m, self.n))

	def __str__(self):
		return("({}, {})".format(self.m, self.n))

	def print_neighbours(self):
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
