# /* UVa problem: 10407 
#  * Simple Division
#  * Topic: Number Theory
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *
#  *   Given n-dimensional boxes, we define a box to be smaller than another
#  *   if there is a configuration of each of the dimensions in which each dimension of
#  *    box A is smaller than the corresponding dimension of box B.
#  *   Given a set of boxes, what is the longest string of boxes which can fit into eachother?
#  *    i.e. what is the longest increasing subsequence (not necessarily of the original input
#  *   order)
#  *
#  * Solution Summary:
#  *
#  *   DP using memoization (implemented with python's dict() class) to find LIS
#  *   Introduce a class Box to minimize the editing of the orignal algo.
#  *   Sort box dimensions to make comparing them easier; implement __lt__
#  *   in order to use the < operator and to be able to sort boxes by size before processing
#  *   them as a group. 
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
#  *
#  *
#  * Tristan Hunt (Your Name)
#  */

import sys

def gcd(a, b):
	if b== 0:
		return a
	return gcd(b, a%b)

def lcm(a, b):
	return (a* (b/gcd(a, b)))	

def load():
	while(1):
		line = next(sys.stdin).split()
		line = [int(x) for x in line]
		line.pop(-1)
		if len(line) == 0:
			break
		yield(line)

for (sequence) in load():
	n = len(sequence)
	
	diff = list()
	for i in range(0, n-1):
		# Now find gcd of all the differences:
		diff.append(abs(sequence[i+1] - sequence[i])) #compute the differences

	if n == 2:
		sys.stdout.write("{}\n".format(diff[0]))
	else:
		# Compute gcd of the differences
		#print(diff)
		#sys.stdout.write("gcd({}, {}) = {}\n".format(diff[0], diff[1], gcd(diff[0], diff[1])))
		m = gcd(diff[0], diff[1])
		for i in range(2, n-1):
			#sys.stdout.write("gcd({}, {}) = {}\n".format(m, diff[i], gcd(m, diff[i])))
			m = gcd(m, diff[i])
		sys.stdout.write("{}\n".format(m))





