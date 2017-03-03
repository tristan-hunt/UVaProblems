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
#  *  Notice that easiest case is when p is a power of 2 -> repeated squaring
#  *  Can easily be implemented by bit shifting right, once.
#  *  Therefore, if we represent p as a series of powers of 2
#  *  e.g. 5 = 1*2^2 + 0*2^1 + 1*2^0 = c2*2^2 + c1*c^1 + c0*2^0
#  *  Then we can use repeated squaring of b to efficiently calculate
#  *   a^2^i. When c(i) is 1, simply multiply b^2^i into the answer.
#  *  Keep taking mod on every step to keep the numbers low, and avoid overflow.
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
