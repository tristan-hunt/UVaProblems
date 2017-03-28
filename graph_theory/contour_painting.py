class Vertex:
	def __init__(self, x, y, symbol):
		self.x = x
		self.y = y
		self.symbol = symbol
		self.visited = False
		self.enclosure = 0

	def __str__(self):
		return self.symbol
	def __repr__(self):
		return(self.symbol)

import sys

def print_grid():
	print("GRID:")
	for g in grid:
		sys.stdout.write("".join([str(i) for i in g])+"\n")
	sys.stdout.write("\n")
	print("ENDGRID")

def create_graph():
	for row_num in range(0, len(grid)):
		gridline = grid[row_num]
		for y in range(0, len(gridline)):
			grid[row_num][y] = Vertex(row_num, y, grid[row_num][y])


def neighbours(node):
	i = 1
	j = 0
	try:
		adj = grid[node.x+i][node.y+j]
		yield(adj)
	except IndexError:			
		pass

	i = -1
	j = 0
	try:
		adj = grid[node.x+i][node.y+j]
		yield(adj)
	except IndexError:			
		pass


	i = 0
	j = 1
	try:
		adj = grid[node.x+i][node.y+j]
		yield(adj)
	except IndexError:			
		pass


	i = 0
	j = -1
	try:
		adj = grid[node.x+i][node.y+j]
		yield(adj)
	except IndexError:			
		pass



def dfs(node, enclosure, star = -1):
	node.visited = True
	node.enclosure = enclosure


	if node.symbol == '*':
		star = enclosure
		node.symbol = ' '

	# Debugging : show enclosure
	# node.symbol = chr(enclosure+96)
	
	for (adj) in neighbours(node):
		if (adj.symbol == ' ' or adj.symbol == '*') and adj.visited == False:  
			star = dfs(adj, enclosure, star)

	if (star != -1 and star != None):
		return (star)
	else:
		return -1	

def flood_fill():
	enclosure = 0
	star = -1
	for row_num in range(len(grid)):
		gridline = grid[row_num]
		for y in range(len(gridline)):
			if gridline[y].visited == False and gridline[y].symbol == ' ':
				enclosure = enclosure + 1
				st = dfs(gridline[y], enclosure)
				if (st != -1 and st != None):
					star = st
	return star

def color_graph(star):
	for row_num in range(len(grid)):
		gridline = grid[row_num]
		for y in range(len(gridline)):
			if gridline[y].enclosure == star:
 				for neighbour in neighbours(gridline[y]):
 					if neighbour.symbol == 'X':
 						gridline[y].symbol = '#'

def add_spaces():
	maxlen = max(len(i) for i in grid)
	for i in range(0, len(grid)):
		if len(grid[i]) < maxlen:
			diff = maxlen - len(grid[i])
			for j in range(0, diff):
				grid[i].append(' ')



def cont(new_line):
	try:
		first_char = new_line[0]
	except IndexError:
		first_char = " "
	if first_char != '_':
		return True
	else:
		return False		

def get_line(lines):
	try:
		new_line = list(next(sys.stdin).strip('\n'))
	except EOFError:
		return None
	except StopIteration:
		return None	
	new_line.append(' ')
	lines.append(new_line)		
	return (new_line)

def load(num_cases):
	for i in range(0, num_cases):
		lines = list()
		new_line = get_line(lines)
		if new_line == None:
			yield(lines)
			break 
		contin = cont(new_line)
		while (contin):
			new_line = get_line(lines)
			contin=cont(new_line)
		yield(lines)

num_cases = int(next(sys.stdin))
for (grid) in load(num_cases):
	add_spaces()	

	create_graph()
	star = flood_fill()
	#print(star)
	
	color_graph(star)
	for g in grid:
		gridline_str = "".join([str(i) for i in g]).rstrip()
		sys.stdout.write(gridline_str+"\n")

