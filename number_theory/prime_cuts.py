import sys
import math

primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def bin_search(n, index, maxi, mini):
	if (primes[index] >= n) and (primes[index-1] < n):
		#sys.stdout.write("P[{}] = {} --> JUST RIGHT\n".format(index, primes[index]))
		return index

	elif primes[index] > n:
		#sys.stdout.write("P[{}] = {} --> TOO BIG\n".format(index, primes[index]))
		maxi = index
		index = math.floor((maxi+mini)/2)
		return bin_search(n, index, maxi, mini)

	else:
		#sys.stdout.write("P[{}] = {} --> TOO SMALL\n".format(index, primes[index]))
		mini = index
		index = math.floor((maxi+mini)/2)
		return bin_search(n, index, maxi, mini)

def load():
	while(1):
		line = next(sys.stdin).split()
		n = int(line[0])
		c = int(line[1])
		yield(n, c)

for (n, c) in load():
	# find list of primes between 1 and n:
	if n == 1:
		index = 1
	elif n == 1000:
		index = len(primes)
	else:
		index = bin_search(n, 0, len(primes), 0)
	p = primes[:index]

	if len(p)%2 == 0:
		i = int(len(p)/2)
		start = i-c
		if start < 0 :
			start = 0
		end = i+c
		if end > len(p):
			end = len(p)
		p = p[start:end]
	

	else:
		i = int(len(p)/2)
		start = i-c+1
		if start < 0 :
			start = 0
		end = i+c
		if end > len(p):
			end = len(p)
		p = p[start:end]

	sys.stdout.write("{} {}: ".format(n, c))
	sys.stdout.write(" ".join(str(i) for i in p))
	sys.stdout.write("\n\n")
