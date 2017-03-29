import sys

memo = dict()

def cut(left, right, coord):
	if (left, right) in memo:
		return memo[(left, right)]

	if left+1 == right:
		memo[(left, right)] = 0
		return 0

	cost = 100001
	term = coord[right] - coord[left]
	for i in range(left+1, right):
		if (left, i) not in memo:
			memo[(left, i)] = cut(left, i, coord)
		if (i, right) not in memo:
			memo[(i, right)] = cut(i, right, coord)
		

		a = memo[(left, i)] + memo[(i, right)] + term
		cost = min(cost, a)
	memo[(left, right)]= cost
	return cost

def load():
	while(1):
		l = int(next(sys.stdin)) # length of the stick to be cut
		if l == 0:
			break
		else:
			n = int(next(sys.stdin)) # the number of cuts to be made
			coord = next(sys.stdin).split()  # an array representing the places the cuts have to be done 
			coord = [int(c) for c in coord]
			coord.insert(0, 0)
			coord.append(l)
			yield(l, n, coord)

for (l, n, coord) in load():
	memo = dict()
	cost = cut(0, n+1, coord)
	sys.stdout.write("The minimum cutting is {}.\n".format(cost))
