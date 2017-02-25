# /* UVa problem: 374
#  *
#  * Topic: Number Theory
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *
#  *   Big Mod: Given b, p, and m, efficiently compute b^p mod m
#  *
#  * Solution Summary:
#  *
#  *	Algorithmic idea, data structures ...
#  *
#  * Used Resources:
#  *
#  * 	Slides from Number Theory presentation
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

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
