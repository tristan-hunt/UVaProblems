
import sys

sys.stdin = open("input.txt") #DELETE BEFORE SUBMITTING

def load():
	num_cases = int(next(sys.stdin))
	for i in range(num_cases):
		next(sys.stdin)
		num_jobs = int(next(sys.stdin))
		times = list() # times[i] = time it takes to do job i
		fines = list() # fines[i] = daily fine for not doing job i
		for j in range(num_jobs):
			line = next(sys.stdin).split()
			times.append(int(line[0]))
			fines.append(int(line[1]))
		yield(times, fines, num_jobs)

for (times, fines, num_jobs) in load():
	# Hint: Sort by ratios??
	sum_fines = sum(fines)
	min_fine = sum_fines * max(times)
	min_idx = -1
	jobs = num_jobs


	while(jobs):
		# Find the minimum cost job
		for i in range(0, jobs):
			time = times[i]
			fine = fines[i]
			cost = time * (sum_fines-fine)
			#sys.stdout.write("Job {} has time {}, fine {}, cost {}".format(i, time, fine, cost))
			if cost < min_fine:
				min_fine = cost
				min_idx = i
				#sys.stdout.write(" and is minimal. ")
			#sys.stdout.write("\n")

		# Complete that job:
		t = times.pop(min_idx)
		f = fines.pop(min_idx)
		sum_fines = sum_fines - f
		jobs = jobs-1
		#sys.stdout.write("Completing job {} which had a fine of {}\n".format(t, f))

		sys.stdout.write("{}".format(t))
		if jobs != 0:
			sys.stdout.write(" ")
	sys.stdout.write("\n")

