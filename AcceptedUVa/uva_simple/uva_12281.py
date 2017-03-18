# /* UVa problem: 12281 
#  * One-Two-Three
#  * Topic: Other (Straightforward)
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *	Given inputs that are possible mispellings of
#  *     'one', 'two', or 'three' (with max. one character incorrect)
#  *     Print what the original word was. 
#  * 
#  * Solution Summary:
#  *  Check if the length is the same as three 
#  *    otherwise, check if it has two characters matching with 'two'
#  *    or two characters matching with 'one'
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
	for i in range(0, num_cases):
		word = next(sys.stdin).strip()
		yield(word)

for word in load():
	if len(word) == 5:
		sys.stdout.write('3\n')
	

	elif word == 'one' or (word[0] == 'o' and word[1] == 'n') or (word[0] == 'o' and word[2] == 'e') or (word[1] == 'n' and word[2] == 'e'):
		sys.stdout.write("1\n")
	elif word == 'two' or (word[0] == 't' and word[1] == 'w') or (word[0] == 't' and word[2] == 'o') or (word[1] == 'w' and word[2] ==  'o'):
		sys.stdout.write('2\n')
