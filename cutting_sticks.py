import sys

def compute_cost(l, n, cuts):
	cost = 100000
	return 1

def load():
	while(1):
		l = int(next(sys.stdin))
		n = int(next(sys.stdin))
		cuts = next(sys.stdin).split()
		cuts = [int(c) for c in cuts]
		yield(l, n, cuts)
for l, n, cuts in load():
	cost = compute_cost(l, n, cuts)
	sys.stdout.write("The minium cost of cutting is {}.\n".format(cost))