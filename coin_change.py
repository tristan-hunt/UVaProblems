# UVA Problem #674 (Mandatory)

import sys




def coin_change(n):
	# Base Case:
	q = n
	if n == 0:
		return 1
	if n == 1:
		return 1

	ans = 0
	if n >= 50:
		ans = ans + coin_change(n-1) 
		n = n - 50
		if n == 0: 
			ans = ans + 1
		print("{} ways of making {}".format(ans, q))
		return ans

	if n >= 25: 
		ans = ans + coin_change(n-1)
		n = n - 25
		if n == 0: 
			ans = ans + 1
		print("{} ways of making {}".format(ans, q))
		return ans

	if n >= 10:
		ans = ans + coin_change(n-1)
		n = n - 10
		if n == 0: 
			ans = ans + 1
		print("{} ways of making {}".format(ans, q))
		return ans


	if n >= 5:
		ans = ans + coin_change(n-1)
		n = n - 5
		if n == 0: 
			ans = ans + 1
		print("{} ways of making {}".format(ans, q))
		return ans

	if n >= 1:
		ans = ans + coin_change(n-1) 
		n = n - 1
		if n == 0: 
			ans = ans + 1
		print("{} ways of making {}".format(ans, q))
		return ans

	print("{} ways of making {}".format(ans, q))
	return ans


def coin_change2(n, memo=None):
	"""
	Return the amount of ways that change that can be made 
	From 1c, 5c, 10c, 25c and 50c pieces
	"""
	sys.stdout.write("Calculating # of ways to make change for {} ...\n".format(n))
	if memo == None:
		memo = dict()

	if n in memo:
		return memo[n]

	# Base Case:
	if n == 0:
		memo[n] = 1
		return memo[n]

	if n == 1:
		memo[n] = 1

	# if n == 5:
	# 	memo[n] = 1

	# if n == 10:
	# 	memo[n] = 1

	# if n == 25:
	# 	memo[n] = 1

	# if n == 50:
	# 	memo[n] = 1



	# coins = [1, 5, 10, 25, 50]
	# ans = 0
	# for i in range(0, 5):
	# 	if n >= coins[i]:
	# 		ans = ans + coin_change(n-coins[i])
	# 		n = n - coins[i]
	
	# return ans
	# memo[n] = ans


	if n > 50:
		memo[n] = coin_change(n-50, memo)
	if n > 25:
		memo[n] = coin_change(n-25, memo)
	if n > 10:
		memo[n] = coin_change(n-10, memo)
	if n > 5:
		memo[n] = coin_change(n-5, memo)
	if n > 1:
		memo[n] = coin_change(n-1, memo)
	
	sys.stdout.write("{} ways to make change for {}\n".format(memo[n], n))
	return memo[n]

def load():
	while(1):
		n = int(next(sys.stdin))
		yield(n)

for n in load():
	memo = dict()
	sys.stdout.write(str(coin_change(n)))
	sys.stdout.write("\n")