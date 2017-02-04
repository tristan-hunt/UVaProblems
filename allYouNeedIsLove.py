#allYouNeedIsLove (problem 10193)
from fractions import gcd

def findLove(string1, string2):
	# convert strings of binary digits to integers
	x = int(string1, 2)
	y = int(string2, 2)

	if gcd(x, y) == 0:
		return(0)
	else:
		return(1)

num_cases = int(input())
for i in range(1, num_cases+1):
	string1 = input()
	string2 = input()
	love = findLove(string1, string2)
	if(love):
		print("Pair #", i, ": All you need is love!")
	else:
		print("Pair #", i, ": Love is not all you need!")