
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

case = 0
for (times, fines, num_jobs) in load():
	if case == 1:
		sys.stdout.write("\n")
	case = 1

	# Hint: Sort by ratios??
	ratios = list()
	for i in range(0, num_jobs):
		ratios.append((times[i]/fines[i], i+1))
	
	result = sorted(ratios, key = lambda x: x[0])
	sys.stdout.write("{}".format(result[0][1]))
	for i in range(1, len(result)):
		sys.stdout.write(" {}".format(result[i][1]))
	sys.stdout.write("\n")
