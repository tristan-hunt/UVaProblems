# Notation:
# n = number of disks
# disks = [1, 2, 3, 4...] i.e d[i] for 0<i<n+1
# M total moves = 2^n - 1
# mth move state = ?
# A = list of integers (disks) on A 

# Algorithm:
# m odd: move smallest disk to next on sequence: A, B, C, A, B...
# m even: move not involving smallest disk.

import sys

disks = list() # [i for i in range(0, n+1)]

def print_status_254(A, B, C):
	"""
	Print the status of the towers (as specified in 254)
	"""
	sys.stdout.write("{} {} {}\n".format(len(A), len(B), len(C)))

def print_transition(A, B, m):
	"""
	Print the transition that just happened
	"""
	sys.stdout.write("{} --> {} ".format(A, B))
	if m%6 == 0:
		sys.stdout.write("\n")
	else:
		sys.stdout.write("\t")

def print_status_10017(A, B, C):
	"""
	Print the status of the towers (as specified in 10017)
	"""
	# Print the list for A:
	sys.stdout.write("A=>")
	if len(A) > 0:
		sys.stdout.write("  ")
		for i in range(0, len(A)):
			sys.stdout.write(" {}".format(A[i]))
	sys.stdout.write("\n")

	# Print the list for B:
	sys.stdout.write("B=>")
	if len(B) > 0:
		sys.stdout.write("  ")
		for i in range(0, len(B)):
			sys.stdout.write(" {}".format(B[i]))
	sys.stdout.write("\n")

	# Print the list for C:
	sys.stdout.write("C=>")
	if len(C) > 0:
		sys.stdout.write("  ")
		for i in range(0, len(C)):
			sys.stdout.write(" {}".format(C[i]))
	sys.stdout.write("\n")

	# Print a final blank line to leave a space between sets. 
	sys.stdout.write("\n")

def movable(A):
	if len(A) > 0 and A[-1] != 0:
		return True
	else:
		return False

def move_odd(A, B):
	"""
	Move disk 1 to next stack on the cycle:
	"""
	B.append(A.pop())

def move_even(A, B, C, m):
	"""
	Do a move not involving disk[1]
	"""
	# Check if any are empty:
	if len(A) == 0:
		if B[-1] == 1:
			A.append(C.pop())
			print_transition("C", "A", m)
			return
		else:
			A.append(B.pop())
			print_transition("B", "A", m)
			return

	if len(B) == 0:
		if A[-1] == 1:
			B.append(C.pop())
			print_transition("C", "B", m)

			return
		else:
			B.append(A.pop())
			print_transition("A", "B", m)
			return

	if len(C) == 0:
		if A[-1] == 1:
			C.append(B.pop())
			print_transition("B", "C", m)
			return
		else:
			C.append(A.pop())
			print_transition("A", "C", m)
			return


	if A[-1] == 1:
		if B[-1] < C[-1] and movable(B): 
			C.append(B.pop())
			print_transition("C", "B", m)
			return
		elif C[-1] < B[-1] and movable(C): 
			B.append(C.pop())
			print_transition("B", "C", m)
			return
		
	if B[-1] == 1:
		if A[-1] < C[-1]: 
			C.append(A.pop())
			print_transition("C", "A", m)
		else: 
			A.append(C.pop())
			print_transition("A", "C", m)
		return


	if C[-1] == 1:
		if A[-1] < B[-1]: 
			B.append(A.pop())
			print_transition("A", "B", m)
		else: 
			A.append(B.pop())
			print_transition("B", "A", m)
		return
	raise RuntimeError("Disk 1 is not at the top of any stack!")

def load_254():
	"""
	Load data from stdin as specified in problem 254
	"""
	while(1):
		input = next(sys.stdin).split()
		n = int(input[0])
		m = int(input[1])
		if m != 0 and n != 0:
			yield(n, m)
		else:
			break

def move_counterclockwise(A, B, C, m):
	if m%2 == 0:
		move_even(A, B, C, m)
	else:
		if m%6 == 1:
			move_odd(A, C)
			print_transition("A", "C", m)
		if m%6 == 3:
			move_odd(C, B)
			print_transition("C", "B", m)
		if m%6 == 5:
			move_odd(B, A)
			print_transition("B", "A", m)


def move_clockwise(A, B, C, m):
	if m%2 == 0:
		move_even(A, B, C, m)
	else:
		if m%6 == 1:
			move_odd(A, B)
			print_transition("A", "C", m)

		if m%6 == 3:
			move_odd(B, C)
			print_transition("A", "C", m)

		if m%6 == 5:
			move_odd(C, A)
			print_transition("A", "C", m)


def init_254():
	for (n, M) in load_254():
		A = [n-i for i in range(0, n)]
		B = list()
		C = list()
		if n%2==0:
			for m in range(1, M+1):
				move_clockwise(A, B, C, m)
		else:
			for m in range(1, M+1):
				move_counterclockwise(A, B, C, m)
		sys.stdout.write("\n\n\n")
		#print_status_254(A, B, C)


def init_10017():
	i = 1

	for (n, M) in load_254():
		sys.stdout.write("Problem #{}\n\n".format(i))
		A = [n-i for i in range(0, n)]
		B = list()
		C = list()
		print_status_10017(A, B, C)
		if n%2 == 0:
			for m in range(1, M+1):
				move_clockwise(A, B, C, m)
				print_status_10017(A, B, C)
		else:
			for m in range(1, M+1):
				move_counterclockwise(A, B, C, m)
				print_status_10017(A, B, C)
		i = i + 1


=======
# Notation:
# n = number of disks
# disks = [1, 2, 3, 4...] i.e d[i] for 0<i<n+1
# M total moves = 2^n - 1
# mth move state = ?
# A = list of integers (disks) on A 

# Algorithm:
# m odd: move smallest disk to next on sequence: A, B, C, A, B...
# m even: move not involving smallest disk.

import sys

disks = list() # [i for i in range(0, n+1)]

def print_status_254(A, B, C):
	"""
	Print the status of the towers (as specified in 254)
	"""
	sys.stdout.write("{} {} {}\n".format(len(A), len(B), len(C)))

def print_transition(A, B, m):
	"""
	Print the transition that just happened
	"""
	sys.stdout.write("{} --> {} ".format(A, B))
	if m%6 == 0:
		sys.stdout.write("\n")
	else:
		sys.stdout.write("\t")

def print_status_10017(A, B, C):
	"""
	Print the status of the towers (as specified in 10017)
	"""
	# Print the list for A:
	sys.stdout.write("A=>")
	if len(A) > 0:
		sys.stdout.write("  ")
		for i in range(0, len(A)):
			sys.stdout.write(" {}".format(A[i]))
	sys.stdout.write("\n")

	# Print the list for B:
	sys.stdout.write("B=>")
	if len(B) > 0:
		sys.stdout.write("  ")
		for i in range(0, len(B)):
			sys.stdout.write(" {}".format(B[i]))
	sys.stdout.write("\n")

	# Print the list for C:
	sys.stdout.write("C=>")
	if len(C) > 0:
		sys.stdout.write("  ")
		for i in range(0, len(C)):
			sys.stdout.write(" {}".format(C[i]))
	sys.stdout.write("\n")

	# Print a final blank line to leave a space between sets. 
	sys.stdout.write("\n")

def movable(A):
	if len(A) > 0 and A[-1] != 0:
		return True
	else:
		return False

def move_odd(A, B):
	"""
	Move disk 1 to next stack on the cycle:
	"""
	B.append(A.pop())

def move_even(A, B, C, m):
	"""
	Do a move not involving disk[1]
	"""
	# Check if any are empty:
	if len(A) == 0:
		if B[-1] == 1:
			A.append(C.pop())
			print_transition("C", "A", m)
			return
		else:
			A.append(B.pop())
			print_transition("B", "A", m)
			return

	if len(B) == 0:
		if A[-1] == 1:
			B.append(C.pop())
			print_transition("C", "B", m)

			return
		else:
			B.append(A.pop())
			print_transition("A", "B", m)
			return

	if len(C) == 0:
		if A[-1] == 1:
			C.append(B.pop())
			print_transition("B", "C", m)
			return
		else:
			C.append(A.pop())
			print_transition("A", "C", m)
			return


	if A[-1] == 1:
		if B[-1] < C[-1] and movable(B): 
			C.append(B.pop())
			print_transition("C", "B", m)
			return
		elif C[-1] < B[-1] and movable(C): 
			B.append(C.pop())
			print_transition("B", "C", m)
			return
		
	if B[-1] == 1:
		if A[-1] < C[-1]: 
			C.append(A.pop())
			print_transition("C", "A", m)
		else: 
			A.append(C.pop())
			print_transition("A", "C", m)
		return


	if C[-1] == 1:
		if A[-1] < B[-1]: 
			B.append(A.pop())
			print_transition("A", "B", m)
		else: 
			A.append(B.pop())
			print_transition("B", "A", m)
		return
	raise RuntimeError("Disk 1 is not at the top of any stack!")

def load_254():
	"""
	Load data from stdin as specified in problem 254
	"""
	while(1):
		input = next(sys.stdin).split()
		n = int(input[0])
		m = int(input[1])
		if m != 0 and n != 0:
			yield(n, m)
		else:
			break

def move_counterclockwise(A, B, C, m):
	if m%2 == 0:
		move_even(A, B, C, m)
	else:
		if m%6 == 1:
			move_odd(A, C)
			print_transition("A", "C", m)
		if m%6 == 3:
			move_odd(C, B)
			print_transition("C", "B", m)
		if m%6 == 5:
			move_odd(B, A)
			print_transition("B", "A", m)


def move_clockwise(A, B, C, m):
	if m%2 == 0:
		move_even(A, B, C, m)
	else:
		if m%6 == 1:
			move_odd(A, B)
			print_transition("A", "C", m)

		if m%6 == 3:
			move_odd(B, C)
			print_transition("A", "C", m)

		if m%6 == 5:
			move_odd(C, A)
			print_transition("A", "C", m)


def init_254():
	for (n, M) in load_254():
		A = [n-i for i in range(0, n)]
		B = list()
		C = list()
		if n%2==0:
			for m in range(1, M+1):
				move_clockwise(A, B, C, m)
		else:
			for m in range(1, M+1):
				move_counterclockwise(A, B, C, m)
		sys.stdout.write("\n\n\n")
		#print_status_254(A, B, C)


def init_10017():
	i = 1

	for (n, M) in load_254():
		sys.stdout.write("Problem #{}\n\n".format(i))
		A = [n-i for i in range(0, n)]
		B = list()
		C = list()
		print_status_10017(A, B, C)
		if n%2 == 0:
			for m in range(1, M+1):
				move_clockwise(A, B, C, m)
				print_status_10017(A, B, C)
		else:
			for m in range(1, M+1):
				move_counterclockwise(A, B, C, m)
				print_status_10017(A, B, C)
		i = i + 1

init_254()