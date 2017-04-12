/* Another N-Queen Problem*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

long long lineCounter;
//int board;

int place(int queen, int col, int dim, int *x, int bad[], int board[]){
	int maxX = 1 << dim;
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

	/* Okay, lets try this a different way:*/
	int prev;
	int bitCol = maxX >> col ;
	int total =0;

	for (i = 1; i < queen; i ++ ){
		total = total + board[i] ;
	}
	if (bitCol&total){
		return 0;
	}

	//printf("board: %d\n", this_board);
	//printf("x:");
	//for (i=1; i< queen; i++){
	//	printf(" %d", x[i]);
	//}printf("\n\n"); 	
	
	for (prev = 1; prev < queen; prev++){
		if ((abs(x[prev]-col) == abs(prev-queen))){			
			printf("x:");
			for (i = 1; i<queen; i++){
				printf(" %d", x[i]);
			} printf("\n");
			printf("q: %d; col: %d\n", queen, col);


			return 0;
		}
	}
	//printf("Succeeded!\n");
	return 1;	
}

int NQueens(int queen, int dim, int *x, int bad[], int *board){
	int i, j, row;
	int maxX = 1 << dim -1 ;
	for (row = 1; row < dim+1; row++){
		if((place(queen, row, dim, x, bad, board)== 1)){
			//printf("x[%d] = %d\n", queen, row);
			x[queen] = row;
			board[queen] = maxX >> row - 1;

			if (queen == dim){				
				lineCounter = lineCounter + 1;
			}
			else{
				NQueens(queen + 1, dim, x, bad, board); /*recursively try next position*/
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
			//board = 0;
			int board[dim];
			total = NQueens(1, dim, x, bad, board);
			printf("Case %d: %d\n", case_num, total);
		}
		rc = scanf("%d", &dim);
		case_num = case_num + 1;
	}
	return 0;
}
