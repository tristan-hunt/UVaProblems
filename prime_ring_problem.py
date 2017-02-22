#http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python/38793421

import sys


primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}


def permutations(iterable, r=None):
	# Modified from the inbuilt function 'itertools.permutations()'
	# In order to prune early
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))


    yield tuple(pool[i] for i in indices[:r])
    
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
    
                # yield tuple(pool[i] for i in indices[:r])
    
                break
        else:
            return

def is_prime_order(ring, n):
	sum = ring[n-1] + ring[0]
	if sum not in primes:
		return(False)

	for i in range(0, n-2):
		sum = ring[i] + ring[i+1]
		if sum not in primes:
			return(False)
	return(True)



def prime_order(ring, n):
	# Try every permutation

	# Then check it
	for order in permutations(ring):
		if (is_prime_order(order, n)):
			sys.stdout.write(" ".join(str(x) for x in order) + "\n")



def load_input():
	while(1):
		try:
			n = int(next(sys.stdin))
			yield(n)
		except(ValueError):
			break


def perm(a,k=0):
	if(k==len(a)):
		print(a)

	else:
		for i in range(k,len(a)):
			a[k],a[i] = a[i],a[k]
			perm(a, k+1) # recursively build up longer and longer permutations
			a[k],a[i] = a[i],a[k]


def test():
	n = 5
	ring = [x for x in range(1, n+1)]
	perm(ring)

def main():
	for n in load_input():
		sys.stdout.write("Case " + str(n) + ":\n")
		ring = [x for x in range(1, n+1)]
		prime_order(ring, n)
		sys.stdout.write("\n")
#main()
test()

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

