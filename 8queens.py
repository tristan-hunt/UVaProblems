# 8 Queens Chess Problem */


import sys

x = [None]*9

def place(queen, row):
	for prev in range(1, queen+1): #check previously placed queens
		if (x[prev] == row or (abs(x[prev]-row) == abs(prev-queen))):
			return False
	return True

def NQueens(queen):
	for row in range(1, 9):
		if(place(queen, row)):
			x[queen] = row
			if (queen == 8 and x[b] == a):
				print("something")
				for j in range(2, 9):
					print("something else")
			else:
				NQueens(queen + 1) # recursively try next position

def main()
	

main()


