import sys
memo = dict()
buttonValues = list()
def buttonPress(i, n):
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
		memo[(i-1, n)] = buttonPress(i-1, n)

	# Second term
	if (i, n-buttonValues[i-1]) not in memo:
		memo[(i, n-buttonValues[i-1])] = buttonPress(i, n-buttonValues[i-1])

	return memo[(i-1, n)]+memo[(i, n-buttonValues[i-1])]


def load():
	num_cases = int(next(sys.stdin))
	for i in range(0, num_cases):
		info = next(sys.stdin).split()
		n = int(info[0])
		t = int(info[1])
		cooking_times = next(sys.stdin).split()
		cooking_times = [int(j) for j in cooking_times]
		yield(n, t, cooking_times)

for (n, t, cooking_times) in load():
	buttonValues = cooking_times
	for i in range(0, t):
		buttonPress(n, i)
	sys.stdout.write(str(buttonPress(n, t)))
	sys.stdout.write("\n")