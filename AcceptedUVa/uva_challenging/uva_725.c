# /* UVa problem: 725 
#  * Division
#  * Topic: Other
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *       Find and display all pairs of 5-digit numbers that between them
#  *   use the digits 0 through 9 once each, such that the first divided by
#  *   the second is equal to N. 
#  *   
#  * Solution Summary:
#  *
#  * Problem Strategies: Iterative Complete Search
#  * Find and display all pairs of 5-digit numbers which between them use the digits
#  * 0 through 9 one each, such that the first divided by the second
#  * is equal to an integer N, where 2 <= N<=79
#  *
#  * Algorithm: For each fghij, get abcde from fghij*N
#  * Check if every digit is different
#  *
#  *    
#  * Used Resources:
#  *
#  *    Demonstration of iterative complete search from Competitive Programming 3
#  * Chapter 3
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  * Tristan Hunt (Your Name)
#  */



#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_duplicates(char* full_str){
	int i, j;
	char x;
	for(i = 1; i < 10; i=i+1){
		x = full_str[i];
		j = i-1;
		while(j >=0 && full_str[j] > x){
			full_str[j+1] = full_str[j];
			j = j -1;
		}
		full_str[j+1] = x;
		if (full_str[j+1] == full_str[j]) {
			return 1;
		}
	}
	return 0;
}

int find_pairs(int n){
	char str_numer[6]; /* str_numer = ""*/
	char str_denom[6]; /* str_denom = ""*/
	char full_str[11];
	int solution_found = 0; /* solution_found = False*/
	int denom = 1234;
	int numer;
	int bufsize = 6;
	int duplicates;
	while (denom < 98766){ 							/*for denom in range(1234, 10000):*/
		numer = denom * n; 							/* 	numer = denom*n*/
		if (numer > 1233 && numer < 98766){			/* 	if numer in range(1234, 98765):*/
			if (denom < 10000){
				snprintf(str_denom, bufsize, "0%d", denom);
			} else {
				snprintf(str_denom, bufsize, "%d", denom);	
			}

			if (numer < 10000){
				snprintf(str_numer, bufsize, "0%d", numer);
			} else {
				snprintf(str_numer, bufsize, "%d", numer);	
			}

			/* Concatenate numer and denom*/
			strcpy(full_str, str_denom);
			strcat(full_str, str_numer);

			
			/*Check if there is duplicates in full_str*/
			duplicates = check_duplicates(full_str);


			/* Print out the equation if there are no duplicates */
			if (duplicates == 0){	/*		if len(set(str_numer + str_denom)) == len(str_numer + str_denom):*/
				printf("%s / %s = %d\n", str_numer, str_denom, n);	/* 			sys.stdout.write(str_numer + " / " + str_denom + " = " + str(n) +"\n")*/
				solution_found = 1;							 	/* 			solution_found = True*/
			}
		}
		denom = denom + 1;
	}

	if (solution_found == 0){ 							/* if (solution_found == False):*/
		printf("There are no solutions for %d.\n", n);	/* 	sys.stdout.write("There are no solutions for " + str(n) + ".\n")*/
	}
}

/*// # Each line of input is a valid integer N
// # Input of 0 terminates the program.*/
int main(int argc, char** argv){
	int n;
	int rc;
	if ((rc = scanf("%d", &n)) != 1){
		return(1);
	}
	int first = 0;	
	while(n!=0){ 			/* while (n!= 0):*/
		if (first == 1){
			printf("\n");
		}
		first = 1;
		find_pairs(n);		/* 		pairs = find_pairs(n)*/
		if ((rc = scanf("%d", &n)) != 1){
			return(1);
		}		
	}
}
