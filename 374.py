# Calculate R = B^p mod M
# For large values of B, P and M
# using an efficient algorithm

import sys
import math


while(1):
	try:
		B = int(input())
		P = int(input())
		M = int(input())
	except ValueError:
		break

	result = B%M
	for i in range(0, P-1):
		result = result * B
		result = result%M

	print(result, end="")

