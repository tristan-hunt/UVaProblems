# /* UVa problem: 10300 
#  * Ecological Premium
#  * Topic: Other (Straightforward)
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *
#  *   Given s = size of field, n = number of animals, e = ecological rating
#  *   Calculate the premium the farmer will be given.
#  *   Premium = avg space per animal * e * n
#  * Solution Summary:
#  *  Since we divide by n to get average space and then multiply n back in
#  *  the answer is simply e * s
#  *  
#  * Used Resources:
#  *
#  * 
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import sys

num_cases = int(next(sys.stdin))
for i in range(num_cases):
	budget = 0
	num_farmers = int(next(sys.stdin))
	for i in range(0, num_farmers):
		info = next(sys.stdin).split()
		budget = budget + (int(info[0]) * int(info[2]))
	sys.stdout.write(str(budget)+"\n")
