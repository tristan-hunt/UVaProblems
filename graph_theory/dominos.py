import sys

def load():
	num_cases = int(next(sys.stdin))
	for i in range(0, num_cases):
		info = next(sys.stdin).split()
		n = int(info[0])
		g = Graph(n)
		m = int(info[1])
		for j in range(0, m):
			edge = next(sys.stdin).split()
			g.addEdge(int(edge[0])-1, int(edge[1])-1) #since we use these as indexes
			try:
				assert(len(g.graph) == n)
			except AssertionError:
				for u in range(0, n):
					if u not in g.graph:
						g.graph[u] = list()
		print(g.graph)
		yield(g)



for g in load(): 
	sys.stdout.write("Following are strongly connected components in given graph\n")
	num = g.SCC()