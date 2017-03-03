# /* UVa problem: 441
#  * Lotto
#  * Topic: Combinatorics
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *
#  *   List all possible subsets of length 6 for a given set 
#  *    of length 6 < k < 13. 
#  *
#  * Solution Summary:
#  *
#  *	Complete Search: Use 6 nested for loops to choose 6 elements from the set.
#  *
#  * Used Resources:
#  *
#  *   Textbook: Competitive Programming 3
#  *   Python docs
#  *   StackOverflow for general python implementation issues.
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import sys

def read_input():
	line = next(sys.stdin)
	line = [int(x) for x in line.split(" ")]
	while (line[0] != 0):
		yield(line)
		line = next(sys.stdin)
		line = [int(x) for x in line.split(" ")]

first = True
for line in read_input():
	if (first == False):
		sys.stdout.write("\n")
	first = False

	k = line[0]
	for i in range(1, k-4):
		for j in range(i+1, k-3):
			for l in range(j+1, k-2):
				for m in range(l+1, k-1):
					for n in range(m+1, k):
						for o in range(n+1, k+1):
							numbers = str(line[i]) + " " + str(line[j]) + " " + str(line[l]) + " " + str(line[m]) + " " + str(line[n]) + " " + str(line[o])
							sys.stdout.write(numbers + "\n")
