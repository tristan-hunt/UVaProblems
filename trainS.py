
import logging
logging.basicConfig(filename='11456-2_log_file.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('\n\n----------------------------------------------------')
logging.debug('Starting computation\n----------------------------------------------------')


import sys
seq = list()

def lis(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i in memo:
		return(memo[i])

	if i == 0:
		memo[i] = 1
		return(memo[i])

	else:
		ans = 1
		for j in range(0, i):
			try:
				seq[i]
				seq[j]
			except IndexError:
				logging.error("index i:{} index j: {}".format(i, j))
				logging.error(seq)
			
			if seq[i] > seq[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = lis(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	return(memo[i])

def lds(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i in memo:
		return(memo[i])

	if i == 0:
		memo[i] = 1
		return(memo[i])		
	
	else:
		ans = 1
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = lds(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	return(memo[i])

def trainlen(i, mlis, mlds):
	if i not in mlis:
		mlis[i] = lis(i, mlis)
	if i not in mlds:
		mlds[i] = lds(i, mlds)

	# find the maxs individually
	maxi = 0 
	maxd = 0
	

	return(mlis[i] + mlds[i] - 1)