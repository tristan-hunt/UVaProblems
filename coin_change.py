# UVA Problem #674 (Mandatory)

import sys
memo = dict()
coinValues = [1, 5, 10, 25, 50]
def coin_change(i, n):

	if n == 0:
		memo[(n)] = 1
		return 1

	if n < 0:
		memo[(n)] = 0
		return 0

	if i <= 0 and n >=1:
		return 0

	# First Term
	if (i-1, n) not in memo:
		# a = coin_change(i-1, n, memo)
		memo[(i-1, n)] = coin_change(i-1, n)


	# Second term
	if (i, n-coinValues[i-1]) not in memo:
		memo[(i, n-coinValues[i-1])] = coin_change(i, n-coinValues[i-1])

	return memo[(i-1, n)]+memo[(i, n-coinValues[i-1])]



def load():
	while(1):
		n = int(next(sys.stdin))
		yield(n)

for n in load():
	for i in range(0, n):
		coin_change(5, i)
	sys.stdout.write(str(coin_change(5, n)))
	sys.stdout.write("\n")