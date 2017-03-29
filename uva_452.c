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