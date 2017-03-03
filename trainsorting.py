
import logging
logging.basicConfig(filename='11456_log_file.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('\n\n----------------------------------------------------')
logging.debug('Starting computation\n----------------------------------------------------')


import sys

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

	return(mlis[i] + mlds[i] - 1)	


test_cases = int(next(sys.stdin))
for i in range(0, test_cases):
	num_cars = int(next(sys.stdin))
	seq = list()
	lisseq = [1]
	ldsseq = [1]

	mlis = dict()
	mlds = dict()

	# maxlen = 0
	# maxlis = 0
	# maxlds = 0

	for j in range(0, num_cars):
		a = int(next(sys.stdin))
		seq.append(a)
		lisseq.append(lis(j, mlis))
		ldsseq.append(lds(j, mlds))

		# if max(lisseq) > maxlis:
		# 	maxlis = max(lisseq)

		# if (maxlis + maxlds -1) > maxlen:
		# 	maxlen = (maxlis + maxlds -1)
		# # if (trainlen(j, mlis, mlds) > maxlen):
		# # 	maxlen = (trainlen(j, mlis, mlds))
		# 	logging.debug("New maxlen: {} = {} + {} - 1".format(maxlen, maxlis, maxlds))
	# lisseq.append(1)
	# ldsseq.append(1)

	maxlen = max(lisseq) + max(ldsseq) - 1
	
	logging.debug(seq)
	logging.debug(lisseq)
	logging.debug(ldsseq)

	logging.debug("Final MAXLEN:{} = {} + {} - 1".format(maxlen, max(lisseq), max(ldsseq)))
	sys.stdout.write("{}\n".format(maxlen))
