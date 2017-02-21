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

	def add_neighbour(self, neighbour):
		self.neighbours.add(neighbour)

	def neighbours(self):
		return self.neighbours

	def __repr__(self):
		return str(self.index)

	def __str__(self):
		return self.__str__()

num_graphs = int(sys.stdin.readline())
black = set() # of integers
white = set() # of integers
nodes = list() #list of Node Objects
for i in range(0, num_graphs):
	info = sys.stdin.readline().split(' ')
	num_edges = int(info[1])
	num_nodes = int(info[0])

	for j in range(1, num_nodes+1):
		nodes.append(Node(j))
		black.add(j) 

	for j in range(0, num_edges):
		edge = sys.stdin.readline().split(' ')
		n1 = int(edge[0])
		n2 = int(edge[1])
		
		nodes[n1].add_neighbour(nodes[n2])
		nodes[n2].add_neighbour(nodes[n1])


		if n1 in black and n2 in black:
			black.remove(n1)
			white.add(n1)

print(len(black))
print(" ".join(str(x) for x in black))

for node in nodes:
	print("Neighbours of node %d", str(node), end = '')
	for neighbour in node.neighbours():
		print(neighbour, end = '')
	print("")