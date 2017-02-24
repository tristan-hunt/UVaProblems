import sys

seq = [-7, 10, 9, 2, 3, 8, 8, 6, 1, 2, 3, 4, 3, 4, 8, 7, 6, 5, 3]
seq = [389, 207, 155, 300, 299, 170, 158, 65]

def lis(i):
	if i == 0:
		return([seq[i]])
	else:
		ans = [seq[i]]
		for j in range(0, i):
			if seq[i] > seq[j]: # We can add seq[i] after seq[j]
				L = lis(j)
				if len(L)+1 > len(ans):
					ans = L[::1]
					ans.append(seq[i])
		return(ans)

def int_lds(i):
	if i == 0:
		return(1)
	else:
		ans = 1
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				ans = max(ans, 1+int_lds(j))
		return(ans)


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

print(lis(int(sys.argv[1])))
