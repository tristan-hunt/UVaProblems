import sys

seq = [-7, 10, 9, 2, 3, 8, 8, 6]
seq2 = [389, 207, 155, 300, 299, 170, 158, 65]
seq = [25,5,4,3,2,1,0,2,23,22,21,3,2,1,24,24,24,24,24]

def lds(i):
	if i == 0:
		return([seq[i]])
	else:
		ans = [seq[i]]
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				L = lds(j)
				if len(L)+1 > len(ans):
					ans = L[::1]
					ans.append(seq[i])
		return(ans)


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

def int_lis(i):
	if i == 0:
		return(1)
	else:
		ans = 1
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				ans = max(ans, 1+int_lis(j))
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

def memo_int_lis(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i == 0:
		if i not in memo:
			memo[i] = 1
		
	else:
		ans = 1
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = memo_int_lis(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	return(memo[i])


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

def memo_lds(i, memo = 0):
	if memo == 0:
		memo = dict() 

	if i == 0:
		if i not in memo: #if memo[i] == None:
			memo[i] = ([seq[i]])
		
		return([seq[i]])
	else:
		ans = [seq[i]]
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				if j not in memo: #if (memo[j] == None):
					memo[j] = memo_lds(j, memo)

				if len(memo[j])+1 > len(ans):
					ans = memo[j][::1]
					ans.append(seq[i])
		
		memo[i] = ans
		return(memo[i])

def memo_int_lds(i, memo = 0):
	if memo == 0:
		memo = dict()

	if i == 0:
		if i not in memo:
			memo[i] = 1
		
	else:
		ans = 1
		for j in range(0, i):
			if seq[i] < seq[j]: # We can add seq[i] after seq[j]
				if j not in memo:
					memo[j] = memo_int_lds(j)
				ans = max(ans, 1+memo[j])
		memo[i] = ans
	
	return(memo[i])

#print(memo_int_lds(0))
