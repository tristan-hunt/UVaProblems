import sys

def load():
	num_cases = int(next(sys.stdin))
	for i in range(num_cases):
		line = next(sys.stdin).split()
		line = [int(i) for i in line]
		yield(line)
case = 1
for (line) in load():
	line.remove(max(line))
	line.remove(min(line))
	sys.stdout.write("Case {}: {}\n".format(case, line[0]))
	case = case + 1