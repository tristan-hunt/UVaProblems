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

def digits_are_unique(numer, denom, n):
	if (len(numer) == 4):
		numer = '0'+numer
	if (len(denom) == 4):
		denom = '0'+ denom	
	
	string = numer + denom

	if len(set(string)) != len(string):
		return False
	else:	
		msg = numer + " / " + denom + " = " + str(n) +"\n"
		sys.stdout.write(msg)
		return True

def print_no_solution(n):
	message = "There are no solutions for " + str(n) + ".\n"
	sys.stdout.write(message)

def find_pairs(n):
	solution_found = False
	for denom in range(1234, 98765):
		numer = denom*n
		if numer in range(1234, 98765):
			if(digits_are_unique(str(numer), str(denom), n)):
				solution_found = True
	if (solution_found == False):
		print_no_solution(n)

# Each line of input is a valid integer N
# Input of 0 terminates the program.
n = int(next(sys.stdin))
while (n!= 0):
	if n == 1:
		print_no_solution(n)
	else:
		pairs = find_pairs(n)
	sys.stdout.write("\n")
	n = int(next(sys.stdin))

