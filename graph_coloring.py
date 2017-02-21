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
#  *   Algorithmic idea, data structures ...
#  *
#  * Used Resources:
#  *
#  *   ...
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  *
#  * --------------------- Tristan Hunt
#  *
import sys


class Node:
	def __init__(self, index):
		self.index = index
		self.neighbours = set()
		# self.color = "black"
		# self.isBlack = True
		# self.isWhite = False


	def add_neighbour(self, neighbour):
		self.neighbours.add(neighbour)
		# if (self.isBlack and neighbour.isBlack):
		# 	return(1)
		# else:
		# 	return(0)

	def neighbours(self):
		return(self.neighbours)

	# def setBlack(self, color):
	# 	self.color = "black"
	# 	self.isBlack = True
	# 	self.isWhite = False

	# def setWhite(self, color):
	# 	self.color = "white"
	# 	self.isBlack = False
	# 	self.isWhite = True

	def print_neighbours(self):
		index_str = str(self.index)
		node_str = ("Index: " + index_str + "\tNeighbours: ") 
		for neighbour in self.neighbours:
			node_str = node_str + str(neighbour.index) + " "
		return(node_str)

	def __repr__(self):
		return str(self.index)

	def __str__(self):
		return self.__repr__()

def add_edge(n1, n2):
	nodes[n1-1].add_neighbour(nodes[n2-1])
	nodes[n2-1].add_neighbour(nodes[n1-1])

	if n1 in black and n2 in black:
		white.add(n1)
		black.remove(n1)



num_graphs = int(sys.stdin.readline())

for i in range(0, num_graphs):
	black = set() # of integers
	white = set() # of integers
	nodes = list() #list of Node Objects


	info = sys.stdin.readline().split(' ')
	num_edges = int(info[1])
	num_nodes = int(info[0])

	for j in range(1, num_nodes+1):
		nodes.append(Node(j)) # NOTE: node 1 has index 0, etc. 
		black.add(j) 


	for j in range(0, num_edges):
		edge = sys.stdin.readline().split(' ')
		n1 = int(edge[0])
		n2 = int(edge[1])

		add_edge(n1, n2)
		
	print(len(black))
	print(" ".join(str(x) for x in black))

	for node in nodes:
		print(node.print_neighbours())