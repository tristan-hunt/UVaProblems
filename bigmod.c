#include <stdio.h>
#include <stdlib.h>

int fmodexp(int a, int b, int m){
	int ans = 1; 
	int pow2 = a;
	while(b){
		if (b&1) {
			ans = (ans*pow2) %m; // if c_1 ==1
		}
		pow2 = (pow2*pow2)%m;
		b >>=1;
	}
	return ans;
}

int bigmod(int b, int p, int m){
	int ans;
	ans  =  b % m;
	for(int i =0; i < p-1; i++){
		ans = ans * b;
		ans = ans%m;
	}
	return(ans);
}

int main(int argc, char** argv){
	// int a = 3;
	// int b = 18132;
	// int m = 17;

	//char * input = stdin();
	int a;
	int b;
	int m;
	char string[256];

	while (1){
		printf("Enter a: ");
		scanf("%d", &a);

		printf("Enter b: ");
		scanf("%d", &b);
	
		printf("Enter m: ");
		scanf("%d", &m);	

		printf("%d\n", fmodexp(a, b, m));

		fgets(string, 256, stdin);
		fflush(stdin);

		//scanf("%s", string);
	}
}