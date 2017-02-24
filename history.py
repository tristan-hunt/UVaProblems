import sys

def int_lis(i):
	if i == 0:
		return(1)
	else:
		ans = 1
		for j in range(0, i):
			if student[i] < student[j]: # We can add seq[i] after seq[j]
				ans = max(ans, 1+lis(j))
		return(ans)

def lis(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i == 0:
		if i not in memo:
			memo[i] = 1
		
	else:
		ans = 1
		for j in range(0, i):
			if student[i] < student[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = lis(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	return(memo[i])

def load():
	num_events = int(next(sys.stdin))
	while(1):
		good = next(sys.stdin).split(" ")
		if good[0] == '\n':
			break
		good = [int(i) for i in good]
		students = list()
		while(1):
			student = next(sys.stdin).split(" ")
			if (len(student) == 1 ):
				break
			else:
				student = [int(i) for i in student]
				students.append(student)
		yield(num_events, good, students)

for (events, good, students) in load():
	for student in students:
		student = [good.index(i) for i in student]
		max_lis = 0
		memo = dict()
		for i in range(0, events):
			if lis(i) > max_lis:
				max_lis = memo[i]
		sys.stdout.write("{}\n".format(max_lis))

