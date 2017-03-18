# /* Kattis problem: Adjoin
#  * 
#  * Topic: Graphs
#  *
#  * Level: challenging
#  * 
#  * Brief problem description:  
#  *
#  *   Given a disconnected (acyclic) graph as a list of edges
#  *   Connected all the components in such a way that the graph
#  *   a) remains Acyclic
#  *   b) Minimizes the maximum length between two nodes. 
#  *
#  * Solution Summary:
#  *
#  *   1. Find the number of connected components, n, using modified DFS
#  *   2. We will need n-1 new edges to connect them all
#  *   3. The minimum maximum distance between any two vertices within a 
#  *    component is that component's diameter. Calculate this using floyd-warshall 
#  *   4. each component will contribute (dia/2)+1 to the final diameter of the
#  *    graph (except for the last component added in this way.)  
#  *
#  * Used Resources:
#  *
#  *   Textbook: Competitive Programming 3
#  *   Python docs
#  *   StackOverflow for general python implementation issues.
#  * https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  *
#  * Tristan Hunt
#  */

import sys
import math
from collections import defaultdict


def addEdge(graph, u, v):
		graph[u].append(v)
		graph[v].append(u)
		
def dfs(graph, visited, u):	
	global curr_comp, components
	visited[u] = 1
	components[curr_comp].append(u)
	for v in graph[u]: #for neighbours v of u
		if visited[v] == 0:
			#sys.stdout.write(" {} ".format(v))
			dfs(graph, visited, v)

def connected_components(graph, visited):
	global components, curr_comp
	for u in graph:
		if visited[u] == 0:
			#sys.stdout.write("visiting u (new component): {} ".format(u))
			curr_comp = curr_comp + 1
			dfs(graph, visited, u)
			#sys.stdout.write("\n")
	return(components)										

def floyd_warshall(component, graph):
	"""
	Find the diameter using floyd-warshall 
	For component i of the graph (i.e. for 
	vertices v for which components[v] = i
	"""
	#1 let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
	V = len(component)
	dist = [[0 for i in range(V)] for j in range(V)]

	#2 for each vertex v
	for v in component:
		#4 for each edge (u,v)
		for i in range(V):
			for j in range(V):
				if i != j:
					#5    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
					dist[i][j] = 1
				else:
					#3   dist[v][v] ← 0
					dist[i][j] = 0	
		max_dist = 0
		for k in range(1, V):
			for i in range(1, V):
				for j in range(1, V):
					#sys.stdout.write("{}>{}+{}\n".format(dist[i][j], dist[i][k], dist[k][j]))
					if dist[i][j] >= dist[i][k] + dist[k][j]:
						dist[i][j] = dist[i][k] + dist[k][j]
						if dist[i][j] > max_dist:
							max_dist = dist[i][j]
		return(max_dist)

def load():
	info = next(sys.stdin).split()
	c = int(info[0]) # computers = number of nodes
	l = int(info[1]) # cables = number of edges
	edges = list()
	for i in range(0, l):
		edge = next(sys.stdin).split()
		edge = [int(e) for e in edge]
		edges.append(edge)
	yield(c, l, edges)

for (c, l, edges) in load():
	# Make the graph
	graph = defaultdict(list)

	#print(edges)
	for u, v in edges:
		graph[u].append(v)
		graph[v].append(u)
	
	visited = [0]*c
	curr_comp = 0
	components = defaultdict(list)
	# Step 1 : Find connected components: 
	components = connected_components(graph, visited)

	num_components = len(components)
	# Step 2: find diameter of each component:
	# dia = [0]*num_components
	# print(dia)	
	total_dia = 0
	for comp in components:
		dia = floyd_warshall(components[comp], graph)	
		total_dia = total_dia + math.ceil(dia/2) 
	total_dia = total_dia + num_components-1
	sys.stdout.write("{}".format(total_dia))
