# /* UVa problem: 11727
#  * Cost Cutting
#  * Topic: Other (Straightforward)
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *
#  *   Given 3 numbers, return the middle number
#  * Solution Summary:
#  *  
#  * Used Resources:
#  * 
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import sys

def load():
	num_cases = int(next(sys.stdin))
	for i in range(num_cases):
		line = next(sys.stdin).split()
		line = [int(i) for i in line]
		yield(line)
case = 1
for (line) in load():
	line.remove(max(line))
	line.remove(min(line))
	sys.stdout.write("Case {}: {}\n".format(case, line[0]))
	case = case + 1