# 8 Queens Chess Problem */


import sys

lineCounter= None
x = [None]*9

def place(queen, row):
	global x

	for prev in range(1, queen): #check previously placed queens
		if (x[prev] == row or (abs(x[prev]-row) == abs(prev-queen))):
			return False
	return True

def NQueens(queen, init_row, init_col):
	global x
	global lineCounter

	for row in range(1, 9):
		if(place(queen, row)):
			x[queen] = row
			if (queen == 8 and x[init_col] == init_row):
				msg = str(lineCounter) + "      " + str(x[1])
				if (lineCounter < 10):
					msg = " " + msg
				sys.stdout.write(msg)
				
				for j in range(2, 9):
					sys.stdout.write(" " +str(x[j]))
				lineCounter = lineCounter + 1

				sys.stdout.write("\n")
			else:
				NQueens(queen + 1, init_row, init_col) # recursively try next position

def main():
	global lineCounter

	num_cases = int(next(sys.stdin)) 
	while(num_cases):
		next(sys.stdin) # eat the blank line
		init_queen = next(sys.stdin).split()
		init_row = int(init_queen[0])
		init_col = int(init_queen[1])
		lineCounter = 1

		sys.stdout.write("SOLN       COLUMN\n")
		sys.stdout.write(" #      1 2 3 4 5 6 7 8\n\n")
		NQueens(1, init_row, init_col)

		num_cases = num_cases-1
		if (num_cases):
			sys.stdout.write("\n")

main()


