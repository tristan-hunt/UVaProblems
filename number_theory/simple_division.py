import sys

def gcd(a, b):
	if b== 0:
		return a
	return gcd(b, a%b)

def lcm(a, b):
	return (a* (b/gcd(a, b)))	

def load():
	while(1):
		line = next(sys.stdin).split()
		line = [int(x) for x in line]
		line.pop(-1)
		if len(line) == 0:
			break
		yield(line)

for (sequence) in load():
	n = len(sequence)
	
	diff = list()
	for i in range(0, n-1):
		# Now find gcd of all the differences:
		diff.append(abs(sequence[i+1] - sequence[i])) #compute the differences

	if n == 2:
		sys.stdout.write("{}\n".format(diff[0]))
	else:
		# Compute gcd of the differences
		#print(diff)
		#sys.stdout.write("gcd({}, {}) = {}\n".format(diff[0], diff[1], gcd(diff[0], diff[1])))
		m = gcd(diff[0], diff[1])
		for i in range(2, n-1):
			#sys.stdout.write("gcd({}, {}) = {}\n".format(m, diff[i], gcd(m, diff[i])))
			m = gcd(m, diff[i])
		sys.stdout.write("{}\n".format(m))





