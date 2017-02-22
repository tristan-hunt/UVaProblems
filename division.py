# Demonstration of iterative complete search from Competitive Programming 3
# Chapter 3
# Problem Category: Arithmetic
# Problem Strategies: Iterative Complete Search
# Find and display all pairs of 5-digit numbers which between them use the digits
# 0 through 9 one each, such that the first divided by the second
# is equal to an integer N, where 2 <= N<=79

# Algorithm: For each fghij, get abcde from fghij*N
# Check if every digit is different

import sys

def find_pairs(n):
	str_numer = ""
	str_denom = ""
	solution_found = False
	for denom in range(1234, 10000):
		str_denom = '0' + str(denom)
		numer = denom*n
		if numer in range(1234, 98765):
			str_numer = str(numer)
			if len(str_numer) == 4: str_numer = '0' + str_numer

			if len(set(str_numer + str_denom)) == len(str_numer + str_denom):
				sys.stdout.write(str_numer + " / " + str_denom + " = " + str(n) +"\n")
				solution_found = True


	for denom in range(10000, 98765):
		str_denom = str(denom)
		
		numer = denom*n
		if numer in range(1234, 98765):
			str_numer = str(numer)
			if len(str_numer) == 4: str_numer = '0' + str_numer

			if len(set(str_numer + str_denom)) == len(str_numer + str_denom):
				sys.stdout.write(str_numer + " / " + str_denom + " = " + str(n) +"\n")
				solution_found = True
	
	if (solution_found == False):
		sys.stdout.write("There are no solutions for " + str(n) + ".\n")


# Each line of input is a valid integer N
# Input of 0 terminates the program.
n = int(next(sys.stdin))
while (n!= 0):
	pairs = find_pairs(n)
	sys.stdout.write("\n")
	n = int(next(sys.stdin))

