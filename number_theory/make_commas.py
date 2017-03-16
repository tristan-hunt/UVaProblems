import sys
def load():
	while(1):
		line = next(sys.stdin).split()
		yield(line)

sys.stdout.write("primes = [")
for line in load():
	for l in line:
		sys.stdout.write(",{}".format(l))
sys.stdout.write("]\n")