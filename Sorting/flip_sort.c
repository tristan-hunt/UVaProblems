/* UVA 10327 - Flip Sort
* Uses same concepts as Frosh Week, Ultra-Quicksort
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>


/* Step 2: Helper function*/
int merge(int *lhs, int len_left, int *rhs, int len_right, int n, long *inv, int *merge){
	/*Given two sorted lists, merge them*/
	int i;

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
			*inv = *inv + len_left - l; /*add number of remaining elements in left array*/
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

	
	/* Debugging*/
	if (*inv < 0){
		printf("overflow detected!\n");
	}

	return 0;
}


/* Step 1: Split, count inversions*/
int split_and_count(int *items, int n, long *inv){
	/* Number of swaps = number of swaps to left 
	* + Number of swaps to the right
	* + Number of swaps which go across
	*/

	/* Don't forget the base case!*/
	if (n == 1){
		*inv = 0;
		return 0;
	}
	
	
	/* Split the array into 2*/
	/* g, h contain lengths of lhs, rhs*/
	int i, g, h; /* ASCII value of g is half that of n*/
	g = (int)floor(n/2); /*Convert to an int!*/
	h = g;

	/* Special case if n is odd*/
	if (n%2==1){
		h = h + 1;
	}

	/* Fill up the left-hand side and rhs*/
	int left_hand[h];
	int right_hand[g];
	

	for (i = 0; i < h; i++){
		left_hand[i] = items[i];
		right_hand[i] = items[h+i];
	}
	
	if (n%2 == 1){
		left_hand[h] = items[h];
	}

	long x, y, z; /* Number of inversions to left, right, and across of the centre*/
	z = 0;
	split_and_count(left_hand, h, &x); /* left-hand is now sorted; x contains the number of inversions it took*/
	split_and_count(right_hand, g, &y); /* right-hand is now sorted; y contains the number of inversions it took*/
	merge(left_hand, h, right_hand, g, n, &z, items); /* z = number of splits between a and b */

	*inv = x + y + z;
	return 0;
}

int main(int argc, char** argv){
	/* Get the input*/
	/* First line: n, the number of students*/
	int i, n, item_num;
	int rc;
	while(1){
		if((rc = scanf("%d", &n)) != 1){
			return 0;
		}
		int items[n];
		for (i = 0; i < n; i++){
			/* Following lines: The number of each student*/
			if((rc=scanf("%d", &item_num)) != 1){
				return(1);
			}
			items[i]= item_num;
		}

		/*Now compute the number of swaps necessary*/
		long inv;
		split_and_count(items, n, &inv);
		printf("Minimum exchange operations : %ld\n", inv);
	}

	return(0);
}