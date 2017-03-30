/* UVA 11858 - Frosh Week
 * Use Merge-Sort to count inversions. 
 * Compile with: gcc -o frosh frosh_week.c -lm -lcrypt -O2 -pipe -ansi -DONLINE_JUDGE
 NOTE - Merging favors rhs , not lhs 
 Q - does that make a difference?

 Q - Am I keeping track of inversions correctly?

 Trace through carefully this case, print after 
 Every step. 
 1. Trace through by hand until correct algo. (see animation)
 2. Print every step of split / merge until correct. 

 ... if it can work for this case, it will *probably* be correct. 

 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


/* Step 2: Helper function*/
void merge(int *lhs, int len_left, int *rhs, int len_right, int n, int *inv, int *merge){
	/*Given two sorted lists, merge them*/
	int i;
	/* Debugging: Is Merge Working?
	printf("LHS:");
	for (i=0; i < len_left; i++){
		printf(" %d", lhs[i]);
	}
	printf("   RHS:");
	for (i=0; i < len_right; i++){
		printf(" %d", rhs[i]);
	}printf("\n");*/


	/*n is the length of the full array*/
	/* Positional counters for lhs, rhs, and merge*/
	int l, r;
	l = 0;
	r = 0; 
	i = 0;

	/* While there is still an element left in both rhs, lhs*/
	while((l < len_left) && (r < len_right)){
		/* Compare lowest value of lhs, rhs, add appropriate val to merge*/
		if (rhs[r] < lhs[l]){
			merge[i] = rhs[r];
			r = r+1;
			i = i+1;
			*inv = *inv + 1;
		}else{
			merge[i] = lhs[l];
			l = l + 1;
			i = i + 1;
		}
	}
	while (l < len_left){
		merge[i] = lhs[l];
		l = l + 1;
		i = i + 1;
	}
	while (r < len_right){
		merge[i] = rhs[r];
		r = r + 1;
		i = i + 1;
	}

	/* Debugging: 
	printf("students: ");
	for (i=0; i < n; i++){
		printf(" %d", merge[i]);
	}
	printf("\n");*/
	return;
}


/* Step 1: Split, count inversions*/
void split_and_count(int *students, int n, int *inv){
	/* Number of swaps = number of swaps to left 
	* + Number of swaps to the right
	* + Number of swaps which go across
	*/

	int i;

	/*DEBUGGING*/
	/*printf("STUDENTS: ");*/
	for (i=0; i < n; i++){
		printf(" %d", students[i]);
	}
	printf("\n");
	

	/* Don't forget the base case!*/
	if (n == 1){
		*inv = 0;
		return;
	}
	
	
	/* Split the array into 2*/
	/* g, h contain lengths of lhs, rhs*/
	int g, h; /* ASCII value of g is half that of n*/
	g = (int)floor(n/2); /*Convert to an int!*/
	h = g;

	/* Special case if n is odd*/
	if (n%2==1){
		h = h + 1;
	}

	/* Fill up the left-hand side and rhs*/
	int right_hand[h];
	int left_hand[g];
	
	for (i = 0; i < g; i++){
		left_hand[i] = students[i];
		right_hand[i] = students[g+i];
	}
	if (n%2 == 1){
		right_hand[g] = students[n-1];
	}


	/*DEBUGGING*/
	for (i = 0; i < g; i++){
		printf(" %d", left_hand[i]);
	}
	printf("\t ");
	for (i= 0; i< h; i++){
		printf(" %d", right_hand[i]);
	}
	printf("\n\n");	
	

	int x, y, z; /* Number of inversions to left, right, and across of the centre*/
	z = 0;
	split_and_count(left_hand, g, &x); /* left-hand is now sorted; x contains the number of inversions it took*/
	split_and_count(right_hand, h, &y); /* right-hand is now sorted; y contains the number of inversions it took*/
	merge(left_hand, g, right_hand, h, n, &z, students); /* z = number of splits between a and b */

	/* Questions: 1) why are we passing pointers to ints to fill but trying to return arrays?
	*			2) Do we want merge() to work in-place? Answer: Yes. 
	*/

	*inv = x + y + z;
	return;
}



int main(int argc, char** argv){
	/* Get the input*/
	/* First line: n, the number of students*/
	int i, n, student_num;
	int rc;
	while(1){
		if((rc = scanf("%d", &n)) != 1){
			return(0);
		}
		int students[n];
		for (i = 0; i < n; i++){
			/* Following lines: The number of each student*/
			if((rc=scanf("%d", &student_num)) != 1){
				return(1);
			}
			students[i]= student_num;
		}

		/*Now compute the number of swaps necessary*/
		int inv;
		split_and_count(students, n, &inv);
		printf("students: %d swaps: %d\n", n, inv);
	}
	return(0);
}

