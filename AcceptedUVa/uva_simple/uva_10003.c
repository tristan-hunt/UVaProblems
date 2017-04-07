/* UVa problem: 10003
#  * Cutting Sticks
#  * Topic: Dynamic Programming
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *	Given a stick, and coordinates at which it should be cut, 
#  *      find the minimum cost to cut it, where cutting cost is dependent on
#  *    the length of the stick being cut (so that the order in which it is cut matters)
#  *  
#  * Solution Summary:
#  *  Simple application of Dynamic Programming and memoization. Using a 2-D array
#  *   to keep track of the minimum cost of cutting at coordinates [left][right],
#  *    with left, right corresponding to indexes into the array of coordinates which need
#  *    to be cut. 
#  *  
#  * Used Resources:
#  * 
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <values.h>

#define inf MAXLONG
const int M = 100;

int cut(long left, long right, int *coord, long memo[M][M]){
    int i, j;
    long a;
    /*printf("Computing cost of cutting from %ld to %ld\n", left, right);*/


    if (memo[left][right] != inf){
    	/*printf("%ld %ld already computed:", left, right);*/
    	/*printf(" %ld\n", memo[left][right]);*/
        return memo[left][right];
    }

    if (left+1 == right){
    	/*printf("%ld %ld are adjacent\n", left, right);*/
        memo[left][right] = 0;
        return 0;
    }


    long cost = inf;
    int term = coord[right] - coord[left];
    /*printf("Cost of cutting from %ld to %ld\n", left, right);*/
    for (i=left+1; i < right; i++){
        if (memo[left][i] == inf){
            memo[left][i] = cut(left, i, coord, memo);
        }
        if (memo[i][right] == inf){
            memo[i][right] = cut(i, right, coord, memo);
        }
        

        a = memo[left][i] + memo[i][right] + term;
        if (a < cost){
        	cost = a;
        }
    }
    memo[left][right] = cost;
    return cost;
}

int main(int argc, char** argv){
    int n, i, j, rc;
    long l;
    while(1){	
    	rc = scanf("%ld", &l); /* length of the stick to be cut*/
    
        if (l == 0){
            return 0;
        }
        
        rc = scanf("%d", &n); /* the number of cuts to be made*/
        
        int coord[n+1]; /* Scan in the positions of the cuts, making sure to include 0 and length.*/
        coord[0] = 0;
        for (i=1; i < n+1; i++){
            rc = scanf("%d", &coord[i]);    
        }
        coord[n+1] = l;

        /* Create memo - initialize it to be inf*/
        long memo[M][M];
        for (i=0; i < n+2; i++){
            for (j=0; j < n+2; j ++){
                if ((i==j)||(abs(i-j)==1)){
                    /*printf("memo[%d][%d]= 0\n", i, j);*/
                    memo[i][j] = 0;
                } 
                else{
                    /*printf("memo[%d][%d]= %ld\n", i, j, inf);*/
                    memo[i][j] = inf;
                }
            }
        }
        for (i=0;i<n+2;i++){
        	/*printf("coord[%d] = %d\n", i, coord[i]);*/
        }

        /* Compute the cost of cutting:*/
        long cost = cut(0, n+1, coord, memo);
        printf("The minimum cutting is %ld.\n",cost);
    }
}