#http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python/38793421
# Result: time limit exceeded

import sys

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}


def grow(ring, new, n):
	ring.append(new)
	if len(ring) == n:
		if ring[-1] + ring[0] in primes:
			sys.stdout.write(" ".join(str(x) for x in ring) + "\n")
	for i in range(1, n+1):
		if i not in ring:
			if ((ring[-1] + i) in primes):
				grow(ring, i, n)
	ring.remove(new)

def load_input():
	n = int(next(sys.stdin))
	while(n):
		yield(n)
		try:
			n = int(next(sys.stdin))
		except(ValueError):
			break

index = 1
for n in load_input():
	if index != 1:
		sys.stdout.write('\n')
	sys.stdout.write("Case " + str(index) + ":\n")
	if n == 1:
		sys.stdout.write("1\n")
	
	ring = list()
	ring.append(1)
	for i in range(2, n+1):
		if ((1+i) in primes):
			grow(ring, i, n)
	index = index + 1