import sys

def dfs(i, j, grid):
	neighbours = list()
	if grid[i][j] == 'W':
		size = 1
		grid[i][j]= 'w' #mark as visited 

		for x in range(-1, 2):
			for y in range(-1, 2):
				if i-x >= 0 and j-y >= 0 and i-x < len(grid) and j-y < len(grid[0]):
					if grid[i-x][j-y] == 'W': # if it's unvisited
						n_size, n = dfs(i-x, j-y, grid)
						size = size + n_size
						neighbours.append((i-x, j-y))
						for o in n:
							neighbours.append(o)
		return(size, neighbours)	
	else:
		return grid[i][j], 0


def load(num_cases):
	for case in range(0, num_cases+1):
		grid = list()
		cells = list()
		while(1):
			next_line = next(sys.stdin)
			if next_line[0] == 'L' or next_line[0] == 'W':
				grid.append(list(next_line))
			else: 
				line = (next_line.split())
				break
		
		while(1):
			try:
				i = int(line[0]) 
			except IndexError:
				yield(grid, cells)
				break
			j = int(line[1]) 
			cells.append((i, j))
			line = next(sys.stdin).split()

def main():
	num_cases = int(next(sys.stdin))
	next(sys.stdin)
	case = 1
	for (grid, cells) in load(num_cases):	
		if case == 0:
			sys.stdout.write("\n")
		case = 0
		for cell in cells:
			i = cell[0]-1
			j = cell[1]-1
			s, neighbours = dfs(i, j, grid)
			grid[i][j] = s
			if neighbours != 0:
				for (x, y) in neighbours:
					grid[x][y] = s
			sys.stdout.write("{}\n".format(s))
main()