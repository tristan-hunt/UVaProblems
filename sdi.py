import sys

#seq = list()

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

def print_max():
	best = [seq[0]]
	memo = dict()
	for i in range(0, len(seq)):
		if (len(memo_lis(i, memo)) > len(best)):
			best = memo_lis(i, memo)
	
	sys.stdout.write("Max hits: {}\n".format(len(best)))
	for i in range(0, len(best)):
		sys.stdout.write("{}\n".format(best[i]))



def load():
	this_seq = list()
	next(sys.stdin) #eat the blank line
	while(1):
		a = next(sys.stdin)
		if a == '\n':
			if len(this_seq) == 0: # Handling blank newline cases
				this_seq = [0]
			yield(this_seq)
			this_seq = list()	
		else:
			a = int(a)
			this_seq.append(a)


cases = int(next(sys.stdin))
c = 0
for this_seq in load():
	seq = this_seq
	if (c):
		sys.stdout.write("\n")
	print_max()
	c = c + 1
