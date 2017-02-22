import sys
import math

def calculate(n):
	n = n * 567
	n = n / 9
	n = n + 7492

	n = n * 235

	n = n / 47

	n = n - 498
	
	n = abs(n)


	n = n % 100

	n = math.floor(n/10)

	return(n)
	#return(math.floor(((((((n*567/9)+7492)*235)/47)-498)%100)/10))


num_cases = int(next(sys.stdin))
while(num_cases):
#	next(sys.stdin) # eat the blank line
	n = int(next(sys.stdin))
	sys.stdout.write(str(calculate(n))+"\n")

	num_cases = num_cases-1
	# if (num_cases):
	# 	sys.stdout.write("\n")