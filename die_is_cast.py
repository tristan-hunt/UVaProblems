import sys

class Graph:
	def __init__(self, map, node_char1, node_char2):
		"""
		Given a list of strings which represent a grid, 
		Make a graph. 
		node_char is the char which represents a node. 
		"""
		self.vertices = list()
		for i in range(0, len(map)):
			row = map[i]
			for j in range(0, len(row)):
				if row[j] == node_char1 or row[j] == node_char2:
					node = Node(i, j, row[j])
					self.vertices.append(node)
					for v in self.vertices:
						vm = v.m
						vn = v.n
						if (vm == i-1 or vm == i + 1) and vn == j :
							v.add_neighbour(node)
						elif (vn == j-1 or vn == j+1) and vm == i:
							v.add_neighbour(node)

	def find_dots(self, vertex, number):
		num_components = 0
		for vertex in self.vertices:
			if vertex.number == number:
				if vertex.symbol == 'X':
					if vertex.visited_twice == False:
						num_components = num_components + 1
						vertex.dfs_dot(number)
		return(num_components)		


	def find_components(self):
		num_components = 0
		new = list() # returns one 'node' for every new component
		for vertex in self.vertices:
			if vertex.visited == 0:
				num_components = num_components + 1
				vertex.dfs_flood(num_components)
				new.append(vertex)
		return(num_components, new)							
		
	def reset_components(self):
		for v in self.vertices:
			self.vertices[v].visited = 0	

	def print_graph(self):
		sys.stdout.write("Vertices: ")
		for v in self.vertices:
			sys.stdout.write("({},{})".format(v.m, v.n))
		for v in self.vertices:
			v.print_neighbours()

		sys.stdout.write("\n")

class Node:
	def __init__(self, m, n, symbol):
		self.m = m
		self.n = n
		self.neighbours = list()
		self.visited = 0
		self.visited_twice = False
		self.symbol = symbol
		self.number = 0

	def add_neighbour(self, V):
		if V is not self and V not in self.neighbours:
			self.neighbours.append(V)
			V.add_neighbour(self)	

	def dfs_dot(self, number):
		self.visited = 2
		self.visited_twice = True
		for vertex in self.neighbours:
			if vertex.number == number:
				if vertex.visited_twice == False and vertex.symbol == 'X':
					vertex.dfs_dot(number)	

	def dfs_flood(self, number):
		self.visited = 1
		self.number = number
		for vertex in self.neighbours:
			if vertex.visited == 0:
				vertex.dfs_flood(number)	

	def __repr__(self):
		return("({}, {})".format(self.m, self.n))

	def __str__(self):
		return("({}, {})".format(self.m, self.n))

	def print_neighbours(self):
		sys.stdout.write("Node ({}, {}) has neighbours: ".format(self.m, self.n))
		for node in self.neighbours:
			sys.stdout.write("({},{})".format(node.m, node.n))
		sys.stdout.write("\n")




def load():
	dimensions = next(sys.stdin).split()
	w = int(dimensions[0])
	h = int(dimensions[1])
	while(w and h):
		lines = list()
		for i in range(0, h):
			lines.append(next(sys.stdin).strip())
		yield(lines)
		dimensions = next(sys.stdin).split()
		w = int(dimensions[0])
		h = int(dimensions[1])


def main():
	case = 1
	for lines in load():
		if case != 1:
			sys.stdout.write("\n")
		sys.stdout.write("Throw {}\n".format(case))
		graph = Graph(lines, 'X', '*')
		components, dice= graph.find_components()
		# for l in lines:
		# 	print(l)
		first = 0
		for d in dice:
			if first == 1:
				sys.stdout.write(" ")
			sys.stdout.write("{}".format(graph.find_dots(d, d.number)))
			first = 1
		
		sys.stdout.write("\n")
		case = case + 1
	sys.stdout.write('\n')
main()