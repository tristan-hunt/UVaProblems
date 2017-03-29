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

int main(int argc, char**argv){
	int rc;
	char full_str[11];
	strcpy(full_str, "0691874532");
	
	if ((rc = check_duplicates(full_str)) == 1){
		printf("%s contains duplicates\n", full_str);
	}else{
		printf("%s contains no duplicates\n", full_str);
	}


	strcpy(full_str, "0681874132");
	/*1. Sort full_str. Since it's a very short string, use insertion sort (sorting networks??)*/
	if ((rc = check_duplicates(full_str)) ==1 ){
		printf("%s contains duplicates\n", full_str);
	}else{
		printf("%s contains no duplicates\n", full_str);
	}


}