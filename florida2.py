import sys

def dfs(i, j, map):
	neighbours = list()
	if map[i][j] == 'W':
		s = 1
		map[i][j]= 'w' #mark as visited 

		for x in range(-1, 2):
			for y in range(-1, 2):
				if i-x >= 0 and j-y >= 0 and i-x < len(map) and j-y < len(map[0]):
					if map[i-x][j-y] == 'W': # if it's unvisited
						n_size, n = dfs(i-x, j-y, map)
						s = s + n_size
						neighbours.append((i-x, j-y))
						for o in n:
							neighbours.append(o)
		return(s, neighbours)	
	else:
		return map[i][j], 0


def load(num_cases):
	for case in range(0, num_cases+1):
		map = list()
		cells = list()
		while(1):
			next_line = next(sys.stdin)
			if next_line[0] == 'L' or next_line[0] == 'W':
				map.append(list(next_line))
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
		for cell in cells:
			i = cell[0]-1
			j = cell[1]-1
			s, neighbours = dfs(i, j, map)
			dfs(i,j, map)
			map[i][j] = s
			sys.stdout.write("{}\n".format(s))
main()
