#http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python/38793421

import sys


primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}



def grow(ring, new, n):
	perm = list()
	perm = ring[:]
	perm.append(new)

	if len(perm) == n:
		if perm[-1] + perm[0] in primes:
			sys.stdout.write(" ".join(str(x) for x in perm) + "\n")
	for i in range(1, n+1):
		if i not in perm:
			if ((perm[-1] + i) in primes):
				grow(perm, i, n)

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
	sys.stdout.write("Case " + str(index) + ":\n")
	ring = list()
	ring.append(1)
	for i in range(2, n+1):
		if ((1+i) in primes):
			grow(ring, i, n)
	sys.stdout.write("\n")
	index = index + 1

