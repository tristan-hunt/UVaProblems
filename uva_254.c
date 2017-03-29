#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void print_status_254(int* A, int* B, int* C){
	/*
	Print the status of the towers (as specified in 254)
	We will store the size of the array on each tower as the
	first element of the tower, so that it is easily accessible.
	*/
	int len_a, len_b, len_c;
	len_a = A[0];
	len_b = B[0];
	len_c = C[0];
	printf("%d %d %d\n",len_a, len_b, len_c);
}

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
		print_status_254(A, B, C)