# http://stackoverflow.com/questions/6534430/why-does-pythons-itertools-permutations-contain-duplicates-when-the-original

import sys
import itertools

num_cases = int(next(sys.stdin)) 
while(num_cases):
	next(sys.stdin)
	nh = next(sys.stdin).split()
	n = int(nh[0])
	h = int(nh[1])

	x = [n-x for x in range(1, n+1)]
	for p in reversed(list(itertools.combinations(x, h))):
		total = 0 
		for i in p:
			bit = 1 << i 
			total = total + bit
		string = '{0:0' + str(n) + 'b}'
		sys.stdout.write((string.format(total))+"\n")
		
	num_cases = num_cases-1
	if (num_cases):
		sys.stdout.write("\n")
