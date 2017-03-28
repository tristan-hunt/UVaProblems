# /* UVa problem: 674 
#  *  Coin Change
#  * Topic: Other 
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *	Given an amount (in coins), output the amount of ways one can 
#  *     make change from the coins. 
#  *   
#  * Solution Summary:
#  *  Simple application of dynamic programming.
#  *  
#  * Used Resources:
#  * 	Competitive Programming 3 - Textbook
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import sys
memo = dict()
coinValues = [1, 5, 10, 25, 50]

def coin_change(i, n):

	if n == 0:
		memo[(n)] = 1
		return 1

	if n < 0:
		memo[(n)] = 0
		return 0

	if i <= 0 and n >=1:
		return 0

	# First Term
	if (i-1, n) not in memo:
		memo[(i-1, n)] = coin_change(i-1, n)

	# Second term
	if (i, n-coinValues[i-1]) not in memo:
		memo[(i, n-coinValues[i-1])] = coin_change(i, n-coinValues[i-1])

	return memo[(i-1, n)]+memo[(i, n-coinValues[i-1])]



def load():
	while(1):
		n = int(next(sys.stdin))
		yield(n)

for n in load():
	# for i in range(0, n):
	# 	coin_change(5, i)
	sys.stdout.write(str(coin_change(5, n)))
	sys.stdout.write("\n")