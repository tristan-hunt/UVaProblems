import sys

def load():
	num_cases = next(sys.stdin)
	for i in range(0, num_cases):
		command = next(sys.stdin)
		length = int(next(sys.stdin))
		input_str = next(sys.stdin).strip('[]')
		print(input_str)

		yield(command, input_str)

for (command, input_str) in load():
	print(case)