 # /* UVa problem: 231
#  *
#  * Topic: Dynamic Programming
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *
#  *   Find the longest decreasing subsequence of missile heights
#  *
#  * Solution Summary:
#  *
#  *   Straightforward implementation of LIS algorithm using DP.
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
 # *
 # *
 # * Tristan Hunt (Your Name)
 # */


import sys

def memo_int_lds(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i == 0:
		if i not in memo:
			memo[i] = 1
		
	else:
		ans = 1
		for j in range(0, i):
			if seq[i] <= seq[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = memo_int_lds(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	
	return(memo[i])


seq = list()
a = int(next(sys.stdin))
case = 1
while(a != -1):
	seq.append(a)
	b = int(next(sys.stdin))
	while(b != -1):
		seq.append(b)
		b = int(next(sys.stdin))
	# Find the max result:
	memo = dict()
	max_result = 0
	for i in range(0, len(seq)):
		res = memo_int_lds(i, memo)
		if res > max_result:
			max_result = res
	if (case != 1):
		sys.stdout.write("\n\n")

	sys.stdout.write("Test #{}:\n  maximum possible interceptions: {}".format(case, max_result))
	seq = list()
	case = case + 1
	a = int(next(sys.stdin))

sys.stdout.write("\n")

