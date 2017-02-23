# UVa 714 - Copying Books
# Difficulty: Challenging
# Strategies: Binary Search, Divide and Conquer
# Category: Search
import sys
import math


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

def greedy(time_est, k, p):
	"""
	Return 1 if successful; 0 if undershoot; 2 if overshoot
	Note : An array for scribe times is probably unessasary
	Note : My logic here is probably bad, considering how hard it was
	to get it to print properly. 
	"""
	# scribe = 0
	# over = 0

	scribe_times = [0]*k # to contain the total time for each of the k scribes
	max_time = time_est
	zero = False

	# i = 0 # index for p 
	# for j in range(0, k):
	# 	while(i < len(p)):
	# 		if (scribe_times[j] + p[i] <= time_est):
	# 			scribe_times[j] = scribe_times[j] + p[i]
	# 			i = i + 1
	# 		else:	# Moving to next scribe
	# 			if (scribe_times[j] == time_est):
	# 				zero = True				
	# 			if j == k-1: # if it's the last scribe: 
	# 				if i < len(p)-1 :  # if we have under-estimated, then we will 
	# 					return(0) # i will be less than len(p)-1
	# 				if (zero):
	# 					return(1)
	# 				else:
	# 					return(2)
	# 			break 
	# return(2)


	i = 0 # index for p 
	for j in range(0, k):
		while(i < len(p)):
			if (scribe_times[j] + p[i] <= time_est):
				scribe_times[j] = scribe_times[j] + p[i]
				i = i + 1
			else:	# Moving to next scribe
				# if scribe_times[j] > max_time:
				# 	max_time = scribe_times[j]
				if (scribe_times[j] == time_est):
					zero = True				
				if j == k-1: # if it's the last scribe: 
					if i < len(p)-1 :  # if we have under-estimated, then we will 
						return(0) # i will be less than len(p)-1
					if (zero):
						return(1)
					else:
						return(2)
				break 
	# if max_time > time_est:
	return(2)
	# else:
	# 	return(1)



	# scribe_times = [0]*k # to contain the total time for each of the k scribes
	# max_time = 0
	# zero = False

	# i = 0 # index for p 
	# for j in range(0, k):
	# 	while(i < len(p)):
	# 		if (scribe_times[j] + p[i]) <= time_est:
	# 			sys.stdout.write("scribe_times["+str(j)+"] + p["+str(i)+"] <= "+ str(time_est) + "\n")
	# 			scribe_times[j] = scribe_times[j] + p[i]
	# 			i = i + 1
	# 			sys.stdout.write("scribe_times["+str(j)+"] = " + str(scribe_times[j]) + " i = " + str(i) + "\n")

	# 		else:	# Moving to next scribe
	# 			print("max time: " + str(max_time) +"\n")
	# 			if (scribe_times[j] > max_time):
	# 				print("scribe_times j is larger " + str(j) + str(max_time)+"\n" )
	# 				max_time = scribe_times[j]
	# 			sys.stdout.write("else.... j = " + str(j) + " and k = " + str(k)+"\n")
	# 			if (scribe_times[j] == time_est):
	# 				zero = True				
	# 			if j == k-1: # if it's the last scribe: 
	# 				if i <= len(p)-1 :  # if we have under-estimated, then we will 
	# 					return(0) # i will be less than len(p)-1
	# 				if (zero):
	# 					return(1)
	# 				else:
	# 					return(2)
	# 			break 
	
	# if max_time < time_est:
	# 	return(1)
	# else:
	# 	return(2)

def load():
	n = int(next(sys.stdin))
	for i in range(0, n):
		mk = next(sys.stdin).split()
		(m, k) = int(mk[0]), int(mk[1])
		p = next(sys.stdin).split()
		for j in range(0, m):
			p[j] = int(p[j])
		yield(m, k, p)

for (m, k, p) in load():
	max_time = sum(p)
	min_time = min(p)
	time_est = max_time

	while(1):
		result = greedy(time_est, k, p)
		print("result: "+str(result)+" time est was: " + str(time_est) + " k: " + str(k) + " p: " +str(p))
		if result == 0: # we undershot in our estimate
			min_time = time_est
			adjust = int(math.floor((max_time - min_time)/2)) 
			time_est = time_est  + adjust
			if adjust == 0:
				result = 1
			
		elif result == 2: # we overshot
			max_time = time_est
			adjust = int(math.floor((max_time - min_time)/2))
			time_est = time_est - adjust
			if (adjust == 0):
				result = 1

		if result == 1: # jjuuuusssttt right
			print_pretty(time_est, p, k)
			break

