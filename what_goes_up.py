import sys

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
