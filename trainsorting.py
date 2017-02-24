def memo_int_lds(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i == 0:
		if i not in memo:
			memo[i] = 1
		
	else:
		ans = 1
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = memo_int_lds(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	
	return(memo[i])


def memo_int_lis(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i == 0:
		if i not in memo:
			memo[i] = 1
		
	else:
		ans = 1
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = memo_int_lis(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	return(memo[i])


def max_length(n):
	"""
	get max(LIS(i) + LDS(i)-1) for all i in range(0, n-1)
	"""

	memo_lis = dict()
	memo_lds = dict()
	