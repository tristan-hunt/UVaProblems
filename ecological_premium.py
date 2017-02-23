import sys

num_cases = int(next(sys.stdin))
for i in range(num_cases):
	budget = 0
	num_farmers = int(next(sys.stdin))
	for i in range(0, num_farmers):
		info = next(sys.stdin).split()
		budget = budget + (int(info[0]) * int(info[2]))
	sys.stdout.write(str(budget)+"\n")
