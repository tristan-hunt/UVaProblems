# Big Mod:
# Result: Time Limit Exceeded
# Callculate R = B^p mod M
# For large values of B, P and M
# using an efficient algorithm

import sys
import math

def load():
	while(1):
		B = int(next(sys.stdin))
		P = int(next(sys.stdin))
		M = int(next(sys.stdin))
		
		yield(B, P, M)

		next(sys.stdin)

for a, b, m in load():
	ans = 1
	pow2 = a
	while (b):
		if (b&1):
			ans = (ans*pow2) %m
		pow2 = (pow2*pow2) %m
		b >>=1
	print(ans)
	


def bigmod(B, P, M):
	result = B%M
	for i in range(0, P-1):
		result = result * B
		result = result%M
	return(result)

	
def fmodexp(a, b, m):
	ans = 1
	pow2 = a
	while (b):
		if (b&1):
			ans = (ans*pow2) %m
		pow2 = (pow2*pow2) %m
		b >>=1
	print(ans)

