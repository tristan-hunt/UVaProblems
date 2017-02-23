# UVa 714 - Copying Books
# Difficulty: Challenging
# Strategies: Binary Search, Divide and Conquer
# Category: Search
import sys
import math
import logging

logging.basicConfig(filename='714_log_file.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('\n\n----------------------------------------------------')
logging.debug('Starting computation\n----------------------------------------------------')

def print_pretty(time, p, k):
	scribe = p[0]
	sys.stdout.write(str(p[0]))

	for i in range(1, len(p)):
		scribe = scribe + p[i]
		if scribe <= time or k == 1:
			sys.stdout.write(" " + str(p[i]))
		else:
			scribe = p[i]
			sys.stdout.write(" / " + str(p[i]))
			k = k - 1
	

	sys.stdout.write("\n")


def greedy(est, K, M, books):
	"""
	Greedily assigns the work to each scribe, without assigning
		more than est.
	Return -1 if we undershot the estimate
	Return -2 if we didn't even use all our scribes
	Else return the maximum of the work of the scribes
	logging.debug("m {} < M {}".format(m, M))
	logging.debug("time = {}, books[m] = {}, newtime = {}".format(time, books[m], (time+books[m])))
	logging.debug("maxt = {}".format(maxt))
	logging.debug("time = {}, maxt = {}".format(time, maxt))
	logging.debug("time = {}, k = {}".format(time, k))
	logging.debug("m = {}".format(m))

	"""
	k = 0 # counter for scribes
	m = 0 # counter for books
	time = 0 # time taken for current scribe (in pages)
	maxt = 0 # max time taken of all the scribes 

	while (m < M):
		if(time + books[m] <= est):
			time = time + books[m]
			m = m + 1
		else:
			if (time > maxt) : 
				maxt = time

						
			if time == 0: # The scribe k is doing 0 work, which means we've underestimated
				return(-1)
			time = 0
			k = k + 1


	if time > maxt:
		maxt = time
	

	if m < M: # We didn't finish the books
		logging.debug("returning -1")
		return(-1)
	if k > K: # We used too many scribes. Since it's k > K and not k >=K, we can overload the last scribe.
		logging.debug("returns -1")
		return(-1)

	if k < K-1: # Didn't use enough scribes
		logging.debug("returns -2")
		return(-2)
	
	logging.debug("returning MAXT: {}".format(maxt))
	return(maxt)

def binarySearch(K, M, books):
	"""
	Use binary search to find the min of the maximum
	"""
	min_max = sum(books) + 1 # We can definitely do better than this
	result_found = False # This is for debugging, to flag if min_max has changed
	lo = min(books) # We know est will be bigger (or equal) to this (1 scribe per book)
	hi = sum(books) # We know est will be smaller (or equal) to this (1 scribe total)
	
	estimate = lo # set the first estimate 

	logging.debug("Entering while loop with min_max: {}, lo: {}, hi: {}".format(min_max, lo, hi))
	while(1):
		result = greedy(estimate, K, M, books)
		logging.debug("Greedy found result {} for estimate {}".format(result, estimate))
		
		if estimate > 0 and (result - estimate == 0):
			logging.debug("Greedy found this estimate perfect! estimate: {} result: {}".format(estimate, result))
			return(estimate)

		# Evaluate the result, update our estimate
		if result == -1: # we went under
			lo = estimate
			estimate = estimate + math.floor((hi-lo)/2)
			logging.debug("Estimate too low")
		elif result == -2: # we went WAY over
			hi = estimate
			estimate = estimate - math.floor((hi-lo)/2)
			logging.debug("Estimate too hi")

		else: # We *might* have the right answer 
			if result < min_max:
				min_max = result
				best_estimate = estimate
				result_found = True
			hi = estimate
			estimate = estimate - math.floor((hi-lo)/2)
			logging.debug("Estimate too high...")

		# Have we reached the end condition?
		if result == 0 or math.floor((hi-lo)/2) == 0: # perfect answer OR we are not even updating our estimate
			if result == 0:
				logging.debug("result == 0 for result {}".format(result))
			if math.floor((hi-lo)/2) == 0:
				logging.info("hi : {}, lo: {}, (hi-lo) = {}, (hi-lo)/2 = {}, math.floor() = {}".format(hi, lo, (hi-lo), ((hi-lo)/2), math.floor((hi-lo)/2)))
				logging.debug("result = {}".format(result))
			if(result_found):
				logging.debug("Returning best_estimate from greedy : {}".format(best_estimate))
				return(best_estimate)
			else: # should never happen. If so, my logic is flawed.
				logging.debug("Oops! RuntimeError!")
				raise RuntimeError

def load():
	n = int(next(sys.stdin))
	for i in range(0, n):
		mk = next(sys.stdin).split()
		(m, k) = int(mk[0]), int(mk[1])
		p = next(sys.stdin).split()
		for j in range(0, m):
			p[j] = int(p[j])
		yield(m, k, p) # Damn this generator thing is great

for (m, k, p) in load():
	logging.debug("time = binarySearch({}, {}, {})".format(k, m, p))
	time = binarySearch(k, m, p) # use binary search to find best time
	print_pretty(time, p, k) # display the result to the screen

