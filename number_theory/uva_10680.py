# Note #1 - TLE 
# Note #2 - Results in Overflow Error (cannot convert float infinity to an int)
# Note #3 - Look up alternate definition of LCM, look at the max powers that each
# prime factor can be raised to (and still be less than n)

import sys

def gcd(a, b):
	if b== 0:
		return a
	return gcd(b, a%b)

def lcm(a, b):
	return (a* (b/gcd(a, b)))	

def load():
	n = int(next(sys.stdin))
	if n == 0:
		break
	yield(n)

for n in load():
	l = 1
	for i in range(1, n+1):
		l = lcm(l, i)
		while (l%10) == 0:
			l = int(l/10)
	sys.stdout.write("{}\n".format(l))
