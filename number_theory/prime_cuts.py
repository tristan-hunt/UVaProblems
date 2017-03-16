import sys
import math

#primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
def load():
	while(1):
		line = next(sys.stdin).split()
		n = int(line[0])
		c = int(line[1])
		yield(n, c)

for (n, c) in load():
	primes = [i for i in range(1, n+1)]	
	i = 1
	sqrt = math.sqrt(n)
	while (i<len(primes)):
		d = primes[i]
		if d < sqrt:
			for j in range(1, len(primes)):
				if j < len(primes):
					if primes[j]%d == 0 and primes[j] != d:            
						primes.pop(j)
		i = i + 1	

	if len(primes)%2 == 0:
		i = int(len(primes)/2)
		start = i-c
		if start < 0 :
			start = 0
		end = i+c
		if end > len(primes):
			end = len(primes)
		primes = primes[start:end]
	

	else:
		i = int(len(primes)/2)
		start = i-c+1
		if start < 0 :
			start = 0
		end = i+c
		if end > len(primes):
			end = len(primes)
		primes = primes[start:end]

	sys.stdout.write("{} {}: ".format(n, c))
	sys.stdout.write(" ".join(str(p) for p in primes))
	sys.stdout.write("\n")
