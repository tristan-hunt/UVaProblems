/* Another N-Queen Problem*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

long long lineCounter;

int place(int queen, int col, int dim, int *x, int bad[]){

	int i, j;
	//
	//printf("Bad Squares:");
	//for(i=0; i < dim; i++){
	//	printf(" %d", board[i]);
	//}printf("\n");
	
	int rowBit = 1 << dim - col;
	int badBit = bad[queen-1];
	int result = rowBit & badBit;
	if (result != 0){ /* This is on a *BAD SQUARE!*  */
		return 0;
	}

	
	/* Verify badx, bady*//*
	printf("Bad squares \n");
	for (i = 0; i < bad_len; i++){
		printf(" (%d, %d)", badx[i], bady[i]);
	}printf("\n");*/
	

	int prev;
	for (prev = 1; prev < queen; prev++){
		if ((x[prev] == col) || ((abs(x[prev]-col) == abs(prev-queen)))){			
			if (x[prev] == col){
				//printf("x:");
				//for (i=0; i< queen+1; i++){
				//	printf(" %d", x[i]);
				//}printf("\n"); 	

				//printf("Placing queen %d on col %d...", queen, col);
				//printf("Failed! x[%d]:%d == %d\n\n", prev, x[prev], col);
			}
			//else{
				//printf("failed on diagonal\n");
			//}
			return 0;
		}
	}
	//printf("Succeeded!\n");
	return 1;	
}

int NQueens(int queen, int dim, int *x, int bad[]){
	int i, j, row;
	for (row = 1; row < dim+1; row++){
		if((place(queen, row, dim, x, bad)== 1)){
			x[queen] = row;
			if (queen == dim){				
				/*printf("x:");
				for (i=0; i< queen+1; i++){
					printf(" %d", x[i]);
				}printf("\n");*/
				lineCounter = lineCounter + 1;
			}
			else{				
				NQueens(queen + 1, dim, x, bad); /*recursively try next position*/
			}
		}
	}
	return (lineCounter);
}


int main(int argc, char** argv){
	int rc;
	int dim;
	int case_num = 1;
	rc = scanf("%d", &dim);
	while (dim != 0){
		int i, j, k;
		int bad[dim];
		for (i = 0; i < dim; i++){
			bad[i] = 0;
		}
		/* Zero out x!!*/
		int x[dim+1];
		for (j = 0; j < dim+1; j++){
			x[j] = -1;
		}
		char boardline[dim+1];
		int boardMax = 1 << dim-1;
		//printf("Board Max: %d\n", boardMax);
		int val;
		/* Find the bad squares on the board*/
		for (k = 0; k < dim; k++){
			rc = scanf("%s", boardline);
			char chr;

			for (j = 0; j < dim; j++){
				chr = boardline[j];
				if (chr == '*'){
					val = boardMax >> j;
					bad[k] = bad[k] + val;
				}
			}
		}
		/* Verify board:*//*
		printf("Bad Squares:");
		for(i=0; i < dim; i++){
			printf(" %d", board[i]);
		}printf("\n");*/

		
		lineCounter = 0;
		if (dim == 3){ /* No configurations on a 3x3 board*/
			printf("Case %d: %d\n",case_num, 0);
		}
		else{
			int total;
			total = NQueens(1, dim, x, bad);
			printf("Case %d: %d\n", case_num, total);
		}
		rc = scanf("%d", &dim);
		case_num = case_num + 1;
	}
	return 0;
}
