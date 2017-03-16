import sys
import time

class Graph:
	def __init__(self, grid, node_char):
		"""
		The dictionary keys are the tuples (i, j), the value
		is the Node object that is represented.
	
		Given a list of strings which represent a grid, 
		Make a graph. 
		node_char is the char which represents a node. 
		"""
		m = len(grid)
		n = len(grid[0]) 
		self.nodes = [[0 for x in range(m)]for y in range(n)]
	
		self.vertices = dict()
		for i in range(1, len(grid)+1):
			row = grid[i-1]
			for j in range(1, len(row)+1):
				if row[j-1] == node_char:
					self.nodes[i][j] = Node(i, j)
					self.vertices[(i, j)] = Node(i, j)
					for v in self.vertices:
						vm = self.vertices[v].m
						vn = self.vertices[v].n
						if vm == i or vm == i-1 or vm == i+1:
							if vn == j or vn == j-1 or vn == j+1: 
								self.vertices[v].add_neighbour(self.vertices[(i, j)])
					
		

	def count_components(self):	
		num_components = 0
		for vertex in self.vertices:
			if vertex.visited == False:
				num_components = num_components + 1
				dfs(vertex)
		return num_components

	def reset_components(self):
		for v in self.vertices:
			self.vertices[v].visited = False	

	def add_node(self, node):
		self.vertices.append(node)

	def print_graph(self):
		sys.stdout.write("All nodes in graph: ")
		sys.stdout.write("[")
		for v in self.vertices:
			sys.stdout.write("({},{})".format(self.vertices[v].m, self.vertices[v].n))
		sys.stdout.write("]\nNeighbours:\n")
		for v in self.vertices:
			sys.stdout.write("FOR NODE ({}, {}): ".format(self.vertices[v].m, self.vertices[v].n))
			self.vertices[v].print_neighbours()					


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
	for case in range(0, num_cases):
		grid = list()
		cells = list()
		while(1):
			next_line = next(sys.stdin)
			if next_line[0] == 'L' or next_line[0] == 'W':
				grid.append(next_line)
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
		yield(grid, cells)

def main():
	num_cases = int(next(sys.stdin))
	next(sys.stdin)
	case = 0
	for (grid, cells) in load(num_cases):	
		if case != 0:
			sys.stdout.write("\n")
		case = case + 1
		graph = Graph(grid, 'W')
		
		for node in cells:
			size = graph.vertices[node].find_size()
			sys.stdout.write("{} ".format(size))
			graph.reset_components()
		sys.stdout.write("\n")

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
