# /* UVa problem: 729 
#  * The Hamming Distance Problem
#  * Topic: Other (Recursion)
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *
#  *   The hamming distance between two bit-strings is the number of
#  *    of 1s in the XOR string.
#  *   Given N, H, print all the bit strings of length N with hamming
#  *   distance H from the bit-string of all 0s.
#  *
#  * Solution Summary:
#  *
#  *   1. Treat the bit string as a list of which positions contain 1s
#  *   2. Generate a generic list (x) of all positions. (x has length n) 
#  *   3. Use itertools.combinations to generate all choices of choosing
#  *         h digits from x (call the choice of positions p)
#  *   4. For each position in p, print a 1 in the corresponding position
#  *        Else, print 0 in that position. 
#  *
#  *   5. Some reversals so that program would output results in the order expected.
#  * 
#  * Used Resources:
#  *  http://stackoverflow.com/questions/6534430/why-does-pythons-itertools-permutations-contain-duplicates-when-the-original
#  *   I consulted stack overflow heavily to learn how to use itertools
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
import itertools

num_cases = int(next(sys.stdin)) 
while(num_cases):
	next(sys.stdin)
	nh = next(sys.stdin).split()
	n = int(nh[0])
	h = int(nh[1]) # the hamming distance ( # of 1s)

	x = [n-x for x in range(1, n+1)]
	for p in reversed(list(itertools.combinations(x, h))):
		total = 0 
		for i in p:
			bit = 1 << i 
			total = total + bit
		string = '{0:0' + str(n) + 'b}'
		sys.stdout.write((string.format(total))+"\n")
		
	num_cases = num_cases-1
	if (num_cases):
		sys.stdout.write("\n")
