import sys
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

def neighbours(node, s1, s2, v):
	for i in range(0, 2):
		for j in range(0, 2):
			try:
				adj = grid[node.x+i][node.y+j]
				if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
					yield(adj)
			except IndexError:
				pass

def create_graph():
	for row_num in range(0, len(grid)):
		gridline = grid[row_num]
		for y in range(0, len(gridline)):
			grid[row_num][y] = Vertex(row_num, y, gridline[y])

def print_grid():
	print("GRID:")
	for g in grid:
		sys.stdout.write("".join([str(i) for i in g])+"\n")
	sys.stdout.write("\n")
	print("ENDGRID")



def dfs(node, enclosure, star = -1):
	node.visited = True
	node.enclosure = enclosure


	if node.symbol == '*':
		star = enclosure
		node.symbol = ' '

	# Debugging : show enclosure
	node.symbol = chr(enclosure+97)
	

	for (adj) in neighbours(node, ' ', '*', False):
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
 				for neighbour in neighbours(gridline[y], 'X', 'X', False):
 					gridline[y].symbol = '#'


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
	new_line = list(next(sys.stdin).strip('\n'))
	new_line.append(' ')
	lines.append(new_line)		
	if '*' in new_line:
		 return True, new_line
	else:
		return False, new_line

def load(num_cases):
	for i in range(0, num_cases):
		lines = list()
		star_found, new_line = get_line(lines)
		contin = cont(new_line)
		while (contin):
			star_found, new_line = get_line(lines)
			contin=cont(new_line)
		yield(lines)

num_cases = int(next(sys.stdin))
for (grid) in load(num_cases):
	maxlen = max(len(i) for i in grid)
	for i in range(0, len(grid)):
		if len(grid[i]) < maxlen:
			diff = maxlen - len(grid[i])
			extension = [' ' * diff]  
			grid[i].extend(extension)

	create_graph()

	star = flood_fill()
	print(star)
	color_graph(star)
	for g in grid:
		sys.stdout.write("".join([str(i) for i in g])+"\n")
	sys.stdout.write("\n")


#def paint_after_first(line):
# 	new_line = ""
# 	painted = False
# 	seen_nonwhite = False
# 	for char in line:
# 		if char == ' ' :
# 			if seen_nonwhite == True and painted == False:
# 				new_line = new_line + '#'
# 				painted = True
# 			else:
# 				new_line = new_line + char
# 		else:
# 			new_line = new_line + char
# 			seen_nonwhite = True

	
# 	return(new_line)

	# try:
	# 	adj = grid[node.x+1][node.y]
	# 	if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
	# 		yield(adj)

	# except AttributeError:
	# 	grid[node.x+1][node.y] = Vertex(node.x+1, node.y, ' ')
	# 	adj = grid[node.x+1][node.y]
	# 	if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
	# 		yield(adj)
	# except IndexError:
	# 	pass

	# try:
	# 	adj = grid[node.x-1][node.y]
	# 	if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
	# 		yield(adj)
	# except AttributeError:
	# 	grid[node.x-1][node.y] = Vertex(node.x-1, node.y, ' ')
	# 	adj = grid[node.x-1][node.y]
	# 	if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
	# 		yield(adj)
	# except IndexError:
	# 	pass
	# try:
	# 	adj = grid[node.x][node.y+1]
	# 	if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
	# 		yield(adj)
	# except AttributeError:
	# 	grid[node.x][node.y+1] = Vertex(node.x, node.y+1, ' ')
	# 	adj = grid[node.x][node.y+1]
	# 	if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
	# 		yield(adj)	

	# except IndexError:
	# 	pass
	# try:
	# 	adj = grid[node.x][node.y-1]
	# 	if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
	# 		yield(adj)
	# except AttributeError:
	# 	grid[node.x][node.y-1] = Vertex(node.x, node.y-1, ' ')
	# 	adj = grid[node.x][node.y-1]
	# 	if (adj.symbol == s1 or adj.symbol == s2) and adj.visited == v:  
	# 		yield(adj)

	# except IndexError:
	# 	pass

