
import logging
logging.basicConfig(filename='111_log_file.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('\n\n----------------------------------------------------')
logging.debug('Starting computation\n----------------------------------------------------')

import sys

def lis(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i == 0:
		if i not in memo:
			memo[i] = 1
		
	else:
		ans = 1
		for j in range(0, i):
			if student[i] > student[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = lis(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	return(memo[i])

def load():
	end = False
	num_events = int(next(sys.stdin))
	while(1):
		good = next(sys.stdin).split(" ")
		good = [int(i) for i in good]
		students = list()
		while(1):
			student = next(sys.stdin).split(" ")
			if (len(student) == 1 ):
				if student[0] == '\n':
					end = True
					break
				new = int(student[0])
				break
			else:
				student = [int(i) for i in student]
				students.append(student)
		yield(num_events, good, students)
		if end == True:
			break
		num_events = new


for (events, good, students) in load():
	a = [i for i in range(1, events+1)]
	case = 1
	for student in students:
		s = [student.index(i) for i in a]
		g = [good.index(i) for i in a]
		student = [g.index(i) for i in s]

		memo = dict()
		max_lis = 0
		for i in range(0, events):
			if lis(i, memo) > max_lis:
				max_lis = memo[i]
		if(case):
			sys.stdout.write("{}".format(max_lis))
			case = 0
		else:
			sys.stdout.write("\n{}".format(max_lis))


