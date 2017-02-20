# Big Mod:
# Result: Time Limit Exceeded
# Callculate R = B^p mod M
# For large values of B, P and M
# using an efficient algorithm

import sys
import math

	
def fmodexp(a, b, m):
	ans = 1
	pow2 = a
	while (b):
		if (b&1):
			ans = (ans*pow2) %m
		pow2 = (pow2*pow2) %m
		b >>=1
	return ans



while(1):
	try:
		B = int(input())
		P = int(input())
		M = int(input())
		result = fmodexp(B, P, M)
		print(result, end="")
		line = input()
	except ValueError:
		break


def bigmod(B, P, M):
	result = B%M
	for i in range(0, P-1):
		result = result * B
		result = result%M
	return(result)