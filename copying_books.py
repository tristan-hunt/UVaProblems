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

def scribes_remaining(k, scribe, m):

	# Calculate if all remaining scribes will be used:
	# this is so hacky
	temp_k = k
	temp_scribe = scribe
	temp_m = m
	while (temp_m+1):
		temp_scribe = temp_scribe + p[m]
		if temp_scribe <= time or k ==1: pass
		else: 
			temp_scribe = p[m]
			temp_k = temp_k -1
		temp_m = temp_m -1 

	if temp_k == 0:
		return True
	else:
		return False
def reverse_string(string):
	"""
	At this point I just want something functional :'(
	"""
	return(string[::-1])

def print_pretty(time, p, k, m):
	scribe = p[m]
	string = str(p[m])
	m = m - 1

	while(m+1):
		scribe = scribe + p[m]
		
		if scribe <= time or k == 1:
			string = str(p[m]) + " " + string
			p.remove(p[m])

		else:
			scribe = p[m]
			string = str(p[m]) + " / " + string
			p.remove(p[m])
			k = k - 1



			# Calculate if all remaining scribes will be used:
			# this is so hacky
			temp_k = k
			temp_scribe = scribe
			temp_m = m
			while (temp_m+1):
				temp_scribe = temp_scribe + p[m]
				if temp_scribe <= time or k ==1: pass
				else: 
					temp_scribe = p[m]
					temp_k = temp_k -1
				temp_m = temp_m -1 

			if temp_k > 1:
				# do it again, differently
				time = binarySearch(k, m+1, p) # use binary search to find best time
				string = reverse_string(print_pretty(time, p, k, m)) + " / " + string # display the result to the screen
				return(string)
				
				

		m = m - 1
	return(string)


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
	logging.debug("Est {}, K {} M {} BOOKS {}".format(est, K, M, books))
	k = 0 # counter for scribes
	m = 0 # counter for books
	times = [0]* K # time taken for current scribe (in pages)
	maxt = 0 # max time taken of all the scribes 

	while (m < M):
		if(times[k] + books[m] <= est) or (k == K-1):
			times[k] = times[k] + books[m]
			m = m + 1
		
		else:
			if (times[k] > maxt) : 
				maxt = times[k]
			if times[k] == 0: # The scribe k is doing 0 work, which means we've underestimated
				return(-1)
			k = k + 1

	if times[k] > maxt:
		maxt = times[k]
	

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
	past_result = -3

	logging.debug("Entering while loop with min_max: {}, lo: {}, hi: {}, books: {}".format(min_max, lo, hi, books))
	while(1):
		result = greedy(estimate, K, M, books)
		logging.debug("Greedy found result {} for estimate {}".format(result, estimate))
		
		if past_result == result:
			logging.debug("No change in estimate... good enough!")
			return(result)
		past_result = result

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
			if result < min_max: #and result <= estimate:
				min_max = result
				best_estimate = estimate
				result_found = True # this is full of lies

			if result > estimate:
				logging.debug("Estimate too low!! Estimate: {}, Result: {}".format(estimate, result))
				lo = estimate
				estimate = estimate + math.floor((hi-lo)/2)
	
			if result <= estimate:
				hi = estimate
				estimate = estimate - math.floor((hi-lo)/2)
				logging.debug("Estimate might be too high...")

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
	string = print_pretty(time, p, k, m-1) # display the result to the screen
	string = string + ("\n")
	sys.stdout.write(string)
