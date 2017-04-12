# Another N-Queen Problem

import sys

sys.stdin = open("input.txt")
import sys

lineCounter = None
x = [None]

def place(queen, row, bad):
	global x
	#print(x)
	for prev in range(1, queen): #check previously placed queens
		if (x[prev] == row or (abs(x[prev]-row) == abs(prev-queen))):
			return False
	for i, j in bad:
		if queen == i and row == j:
			return False
	return True

def NQueens(queen, dim, bad_squares):
	global x
	global lineCounter

	for row in range(1, dim+1):
		if(place(queen, row, bad_squares)):
			x[queen] = row
			if (queen == dim):
				#msg = str(lineCounter) + "      " + str(x[1])
				#if (lineCounter < 10):
				#	msg = " " + msg
				#sys.stdout.write(msg)
				
				#for j in range(2, dim+1):
				#	sys.stdout.write(" " +str(x[j]))
				lineCounter = lineCounter + 1

				#sys.stdout.write("\n")
			else:
				NQueens(queen + 1, dim, bad_squares) # recursively try next position

	return (lineCounter-1)

def load():
	dim = int(next(sys.stdin))
	while (dim != 0):
		board = list()
		for i in range(0, dim):
			line = next(sys.stdin)
			j = 0
			for char in line:
				if char == '*':
					board.append((i+1, j+1))
				j = j + 1
		yield(dim, board)
		dim = int(next(sys.stdin))

def main():
	global lineCounter
	global x 
	i = 1
	for dim, board in load():
		x = [None]* (dim+1)
		#print("Board: "+ str(board))
		placement = [i for i in range(0, dim)]
		lineCounter = 1
		#sys.stdout.write("SOLN       COLUMN\n")
		#sys.stdout.write(" #      1 2 3 4 5 6 7 8\n\n")
		total = NQueens(1, dim, board)
		sys.stdout.write("Case {}: {}\n".format(i, total))
		i = i + 1
		#make nqueens accept generic input
		#make nqueens care about board size
		#make nqueens care about bad spaces

main()