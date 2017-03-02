import sys

coinValue = [1, 5, 10, 25, 50]
memo = dict

# def coin1(n):
# 	if n == 0:
# 		return 0
# 	if n < 0:
# 		return 5000

# 	minc = 5000
# 	for i in coinValue:
# 		ans = coin(n - i)
# 		if ans < minc:
# 			minc = ans
# 	return 1 + minc

def coin(n, memo):
	

	if n == 0:
		return 0
	if n < 0:
		return 5000

	minc = 5000
	
	for i in coinValue:
		ans = coin(n - i)
		if ans < minc:
			minc = ans
	
	
	return(1 + minc)

def load():
	while(1):
		n = int(next(sys.stdin))
		yield(n)

for n in load():
	memo = dict()
	sys.stdout.write(str(coin(n)))
	sys.stdout.write("\n")