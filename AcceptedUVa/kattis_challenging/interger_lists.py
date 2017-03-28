import time
import sys
from collections import deque


def load():
	num_cases = int(next(sys.stdin))
	for i in range(0, num_cases):
		command = next(sys.stdin)
		length = int(next(sys.stdin))
		input_str = next(sys.stdin).strip().strip('[').strip(']')
		input_str = deque(input_str.split(','))
		
		#input_str = input_str.split(',')
		yield(command, length, input_str)

def main():
	for (command, length, input_str) in load():
		reverse = False
		d = command.count('D')
		if d > length:
			sys.stdout.write("error\n")
		else:
			for char in command:
				if char == 'D':
					if (reverse):
						input_str.pop()
					
					else:						
						input_str.popleft()
				
				elif char == 'R':
					if reverse == True:
						reverse = False
				
					elif reverse == False:
						reverse = True 
				

			sys.stdout.write("[")
			if reverse:
				input_str.reverse()
			
			sys.stdout.write(",".join(input_str))
			sys.stdout.write("]\n")
main()


# start_time = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))

