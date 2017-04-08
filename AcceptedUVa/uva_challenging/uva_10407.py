# /* UVa problem: 10407 
#  * Simple Division
#  * Topic: Number Theory
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *	Given a list of numbers, a1, a2, a3.... an compute a number m such that 
#  *   ai mod m = x for some arbitrary x for all ai. 
#  *	In other words, find a congruence class modulo m to which each number belongs
#  * Solution Summary:
#  *	Compute the differences of each of the numbers, then find the gcd
#  *		of all of the differences. 
#  * Used Resources:
#  *
#  *   Textbook: Competitive Programming 3
#  *   Hints given on 'Spanish Problem Archive'
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  * Tristan Hunt
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





