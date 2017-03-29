/*# Notation:
# n = number of disks
# disks = [1, 2, 3, 4...] i.e d[i] for 0<i<n+1
# M total moves = 2^n - 1
# mth move state = ?
# A = list of integers (disks) on A 

# Algorithm:
# m odd: move smallest disk to next on sequence: A, B, C, A, B...
# m even: move not involving smallest disk.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int print_status_254(int* A, int *len_a, int* B, int *len_b, int* C, int *len_c){
	/*
	Print the status of the towers (as specified in 254)
	We will store the size of the array on each tower as the
	first element of the tower, so that it is easily accessible.
	*/
	printf("%d %d %d\n", *len_a, *len_b, *len_c);
	return(0);
}

int print_status(int *A, int *len_a, int *B, int *len_b, int *C, int *len_c){
	printf("len_a:%d len_b:%d len_c%d\n", *len_a, *len_b, *len_c);
	printf("A top: %d, B top: %d, C top: %d", A[*len_a], B[*len_b], C[*len_b]);
	return(0);

}

int move_odd(int *A, int *len_a, int *B, int *len_b){
	/*
	Move disk 1 to next stack on the cycle:
	B.append(A.pop())
	*/
	int disk = A[*len_a];
	A[*len_a] = 0;
	*len_a = *len_a - 1;
	*len_b = *len_b + 1;
	B[*len_b] = disk;
	return(0);
}

int move_even(int *A, int *len_a, int *B, int *len_b, int *C, int *len_c){
	/*Do a move not involving disk[1]*/
	/*# Check if any are empty:*/
	
	int disk;
	if (*len_a == 0) {
		if (B[*len_b] == 1){
			disk = C[*len_c];
			C[*len_c] = 0;
			*len_c = *len_c -1;

			*len_a = *len_a + 1;
			A[*len_a] = disk;
			return(0);
		} else{
			disk = B[*len_b];
			B[*len_b] = 0;
			*len_b = *len_b - 1;
			*len_a = *len_a + 1;
			A[*len_a] = disk;
			return(0);
		}
	}


	if (*len_b == 0){
		if (A[*len_a] == 1){
			disk = C[*len_c];
			C[*len_c] = 0;
			*len_c = *len_c -1;
			*len_b = *len_b + 1;
			B[*len_b] = disk;
			return(0);
		}else{
			disk = A[*len_a];
			A[*len_a] = 0;
			*len_a = *len_a -1;
			*len_b = *len_b + 1;
			B[*len_b] = disk;
			return(0);
		}
	}

	if (*len_c == 0){
		if (A[*len_a] == 1){
			disk = B[*len_b];
			B[*len_b] = 0;
			*len_b = *len_b - 1;
			*len_c = *len_c + 1;
			C[*len_c] = disk;
			return(0);
		}else{
			disk = A[*len_a];
			A[*len_a] = 0;
			*len_a = *len_a - 1;
			*len_c = *len_c + 1;
			C[*len_c] = disk;
			return(0);
		}

	}


	if (A[*len_a] == 1){
		if (B[*len_b] < C[*len_c]){
			disk = B[*len_b];
			B[*len_b] = 0;
			*len_b = *len_b - 1;
			*len_c = *len_c + 1;
			C[*len_c] = disk;
			return(0);
		}
		if (C[*len_c] < B[*len_b]) {
			disk = C[*len_c];
			C[*len_c] = 0;
			*len_c = *len_c - 1;
			*len_b = *len_b + 1;
			B[*len_b] = disk;
			return(0);
		}
	}

	if (B[*len_b] == 1){
		if (A[*len_a] < C[*len_c]){
			disk = A[*len_a];
			A[*len_a] = 0;
			*len_a = *len_a - 1;
			*len_c = *len_c + 1;
			C[*len_c] = disk;
			return(0);
		}else{
			disk = C[*len_c];
			C[*len_c] = 0;
			*len_c = *len_c - 1;
			*len_a = *len_a + 1;
			A[*len_a] = disk;
			return(0);
		}
	}

	if (C[*len_c] == 1){
		if (A[*len_a] < B[*len_b]){
			disk = A[*len_a];
			A[*len_a] = 0;
			*len_a = *len_a - 1;
			*len_b = *len_b + 1;
			B[*len_b] = disk;
			return(0);
		}else{
			disk = B[*len_b];
			B[*len_b] = 0;
			*len_b = *len_b - 1;
			*len_a = *len_a + 1;
			A[*len_a] = disk;
			return(0);
		}
	}

	/*
	raise RuntimeError("Disk 1 is not at the top of any stack!")*/
	
	printf("Disk 1 is not at the top of any stack! ");
	print_status(A, len_a, B, len_b, C, len_c);
	printf("\n");
	return(1);
}

int move_counterclockwise(int *A, int *len_a, int *B, int *len_b, int *C, int *len_c, int m){

	if (m%2 == 0){ 
		/*Even moves: Take disk 1 and move it to the next 
		 * Peg in circular sequence ABC ABC ABC ...*/
		move_even(A, len_a, B, len_b, C, len_c);
	}else{ /* Only possible move not involving disk 1*/
		if (m%6 == 1){
			move_odd(A, len_a, C, len_c);
		}
		if (m%6 == 3){
			move_odd(C, len_c, B, len_b);
		}
		if (m%6 == 5){
			move_odd(B, len_b, A, len_a);
		}
	}
	return(0); /*Method completely successfully*/
}

int move_clockwise(int *A, int *len_a, int *B, int *len_b, int *C, int *len_c, int m){
	if (m%2 == 0){
		move_even(A, len_a, B, len_b, C, len_c);
	}else{
		int r = m%6;
		if (r == 1){
			move_odd(A, len_a, B, len_b);
		}
		if (r == 3){
			move_odd(B, len_b, C, len_c);
		}
		if (r == 5){
			move_odd(C, len_c, A, len_a);
		}
	}
	return(0); /*Function completed successfully*/
}


int main(int argc, char** argv){
	/*Load the input from stdin*/

	int n, m, i, rc;
	if ((rc = scanf("%d %d", &n, &m)) != 2){
		return(1); /*Input failed*/
	}
	
	int len_a, len_b, len_c;
	while(n != 0 && m!=0){
		/* Fill A with every disk from n to 1:*/
		int A[n];
		int B[n];
		int C[n];

		/*Initialize arrays A, B, C*/
		for (i=0; i<n; i++){
			A[i] = n-i; /* Fills A with numbers 1 to n, decreasing order*/
			B[i] = 0;  	/*Let B, C be empty- */ 
			C[i] = 0;	/*let an empty space be represented by 0*/
		}
		

		/*Extra Bookkeeping:*/
		len_a = n;
		len_b = 0;
		len_c = 0;

		if (n%2 == 0){
			for(i = 1; i<m+1; i = i+1){
				move_clockwise(A, &len_a, B, &len_b, C, &len_c, i);
			}
		}else{
			for (i =1; i <m+1; i = i+1){
				move_counterclockwise(A, &len_a, B, &len_b, C, &len_c, i);
			}
		}

		print_status_254(A, &len_a, B, &len_b, C, &len_c);
		/*Get the next input from stdin*/
		if ((rc = scanf("%d %d", &n, &m)) != 2){
			return(1); /* Input failed */
		}
	}

	return(0);
}
