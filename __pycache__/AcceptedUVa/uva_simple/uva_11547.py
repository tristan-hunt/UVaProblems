# /* UVa problem: 11547
#  * Automatic Answer
#  * Topic: Other (Straightforward)
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *
#  *   Given a series of inputs, t, calculate the answer to the
#  *    skill testing question: Multiply n
#  *     by 567, then divide the result by 9, then add 7492, then multiply by 235, then divide
#  * by 47, then subtract 498. What is the digit in the tens column?
#  *
#  * Solution Summary:
#  *
#  *  Straightforward implementation of the problem question. Algo:
#  *   take t, calculate the result, and print it. 
#  *
#  * Used Resources:
#  *  ---
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * Tristan Hunt
#  */

import sys
import math

def calculate(n):
	n = n * 567
	n = n / 9
	n = n + 7492

	n = n * 235

	n = n / 47

	n = n - 498
	
	n = abs(n)


	n = n % 100

	n = math.floor(n/10)

	return(n)
	#return(math.floor(((((((n*567/9)+7492)*235)/47)-498)%100)/10))


num_cases = int(next(sys.stdin))
while(num_cases):
#	next(sys.stdin) # eat the blank line
	n = int(next(sys.stdin))
	sys.stdout.write(str(calculate(n))+"\n")

	num_cases = num_cases-1
	# if (num_cases):
	# 	sys.stdout.write("\n")
