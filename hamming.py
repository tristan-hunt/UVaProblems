# http://stackoverflow.com/questions/6534430/why-does-pythons-itertools-permutations-contain-duplicates-when-the-original


import sys
import itertools

def hamming_distance(a):
	count = 0
	while(a):
		if a%2 == 1:
			count += 1
		a = a >> 1
	return(count)

def unique(iterable):
	seen = set()
	for x in iterable:
		if x in seen:
			continue
		seen.add(x)
		yield(x)

def main():

	num_cases = int(next(sys.stdin)) 
	while(num_cases):
		next(sys.stdin)
		nh = next(sys.stdin).split()
		n = int(nh[0])
		h = int(nh[1])

		# generate smallest number of h 1s:
		if h == 0:
			a = '0'*h
			sys.stdout.write(a + "\n")
		else:
			a = '0'*(n-h) + '1'*h 

		print(a)
		
		for p in unique(itertools.permutations(a)):
			for digit in p:
				sys.stdout.write(digit)
			sys.stdout.write("\n")


		num_cases = num_cases-1
		if (num_cases):
			sys.stdout.write("\n")

main()