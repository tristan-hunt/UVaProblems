import sys
seq = list()

class Box:
	def __init__(self, dimensions, n):
		dimensions.sort()
		self.dim = dimensions
		self.n = n

	def __str__(self):
		string = "B:("
		for i in range(0, n):
			if i == 0:
				string = string + str(self.dim[i])
			else:
				string = string + ", " + str(self.dim[i])
		string = string + ")"
		return string

	def __repr__(self):
		string = "B:("
		for i in range(0, n):
			if i == 0:
				string = string + str(self.dim[i])
			else:
				string = string + ", " + str(self.dim[i])
		string = string + ")"
		return string

	def __lt__(self, other):
		if self.n != other.n:
			return NotImplemented
		for i in range(0, self.n):
			if self.dim[i] >= other.dim[i]:
				return False
		return True

	def __eq__(self, other): 
		if self.n != other.n:
			return NotImplemented
		for i in range(0, self.n):
			if self.dim[i] != other.dim[i]:
				return False
		return True

def memo_lis(i, memo = 0):
	if memo == 0:
		memo = dict() 

	if i == 0:
		if i not in memo: #if memo[i] == None:
			memo[i] = ([seq[i]])
		
		return([seq[i]])
	else:
		ans = [seq[i]]
		for j in range(0, i):
			if seq[i] > seq[j]: # We can add seq[i] after seq[j]
				
				
				if j not in memo: #if (memo[j] == None):
					memo[j] = memo_lis(j, memo)

				if len(memo[j])+1 > len(ans):
					ans = memo[j][::1]
					ans.append(seq[i])
		
		memo[i] = ans
		return(memo[i])

def load():
	while(1):
		kn = next(sys.stdin).split()
		k = int(kn[0])
		n = int(kn[1])
		this_seq = list()
		for i in range(0, k):
			dim = next(sys.stdin).split()
			dim = [int(j) for j in dim]
			this_seq.append(Box(dim, n))
		yield(k, n, this_seq)

for (k, n, this_seq) in load():
	seq = this_seq

	maxlen = 0
	biggest_seq = list()
	memo = dict()
	
	a = seq[::1]
	seq.sort()

	for i in range(0, k):
		if len(memo_lis(i, memo)) > maxlen:
			biggest_seq = memo_lis(i, memo)
			maxlen = len(biggest_seq)
	sys.stdout.write("{}\n".format(maxlen))

	# sys.stdout.write("K: {} len(seq): {} len(biggest_seq): {}\n".format(k, len(seq), len(biggest_seq)))


	
	# sys.stdout.write(str(seq[0]))
	# sys.stdout.write("\n")

	# sys.stdout.write(str(seq[1]))
	# sys.stdout.write("\n")
	# sys.stdout.write(str(seq[2]))
	# sys.stdout.write("\n")
	# sys.stdout.write(str(seq[3]))
	# sys.stdout.write("\n")
	# sys.stdout.write(str(seq[4]))
	# sys.stdout.write("\n")

	b = [a.index(x)+1 for x in biggest_seq]
	
	# b wouldn't be empty, would it? No, since maxlen starts at 0, no matter what it will have something on the first iter
	
	sys.stdout.write("{}".format(b[0]))
	for i in range(1, len(biggest_seq)):
		sys.stdout.write(" {}".format(b[i]))		
		# sys.stdout.write(str(biggest_seq[i]))
		# sys.stdout.write(" ")
	sys.stdout.write("\n")