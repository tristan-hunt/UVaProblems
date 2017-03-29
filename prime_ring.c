/*http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python/38793421
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isPrime(int p){
	if (p == 2)
		return(1);
	if (p == 3)
		return(1);
	if (p == 5)
		return(1);
	if (p == 7)
		return(1);
	if (p == 11)
		return(1);
	if (p == 13)
		return(1);
	if (p == 17)
		return(1);
	if (p == 19)
		return(1);
	if (p == 23)
		return(1);
	if (p == 29)
		return(1);
	if (p == 31)
		return(1);
	return(0);
}

int iInRing(int *ring, int end, int p){
	int i = 0;
	while(i <= end){
		if (ring[i] == p)
			return(1);
		i = i + 1;
	}
	return(0);
}

/*def grow(ring, new, n):
	ring.append(new)
	if len(ring) == n:
		if ring[-1] + ring[0] in primes:
			sys.stdout.write(" ".join(str(x) for x in ring) + "\n")
	for i in range(1, n+1):
		if i not in ring:
			if ((ring[-1] + i) in primes):
				grow(ring, i, n)
	ring.remove(new)
*/

int grow(int *ring, int new, int n){
	int sum, j, rc; 
	int i = 0;
	
	/*
	for (i=0; i<n; i=i+1){
		printf("ring[%d]:%d  ", i, ring[i]);
	}printf("\n");
	*/

	/* Find the end of the array */
	int end = -1;
	while(end < 0){
		if (ring[i] == 0)
			end = i;		
		i = i + 1;
	}
	ring[end] = new;
	
	
	/*for (i=0; i<n; i=i+1){
		printf("ring[%d]:%d;  ", i, ring[i]);
	}printf("\tn:%d\n", n);*/
	

	/*Check if ring is full-sized*/
	if (end == n-1){
		/*Check if ring[n] + ring[0] are in 'primes'*/
		/* If so, print out the array */
		if ((rc=isPrime(ring[n-1] + ring[0])) == 1){
			printf("%d", ring[0]);
			for (j =1; j<n; j=j+1){
				printf(" %d", ring[j]);
			}
			printf("\n");
		}
	}

	/*Try to append each new i to the ring.*/
	for (i=1; i< n+1; i=i+1){
		/*python: if i not in ring: if ring[-1] + i in primes: grow(ring, i, n)*/
		if ((rc = iInRing(ring, end, i)) == 0){
			if ((rc = isPrime(ring[end]+i)) == 1){
				grow(ring, i, n);
			}
		}
	}
	ring[end] = 0;
}

/*
python driver:
	ring = list()
	ring.append(1)
	for i in range(2, n+1):
		if ((1+i) in primes):
			grow(ring, i, n)
*/

int main(int argc, char** argv){
	int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
	int n;
	int rc;
	int case_num = 1;
	int i;


	while((rc = scanf("%d", &n) == 1)) {
		if (case_num != 1){
			printf("\n");
		}
		
		printf("Case %d:\n", case_num);
		
		/* Initialize array to all 0s*/
		int ring[n];
		for (i = 0; i<n; i++){
			ring[i] = 0;
		}

		/*Check that array has been initialized properly
		for(i=0; i<n; i++){
			printf("ring[%d]:%d  ", i, ring[i]);
		}printf("\n");*/
	



		if (n==1){ /*Special Case: n == 1*/
			printf("1\n");
		}

		ring[0] = 1;
		for (i = 2; i< n+1; i=i+1){
			if ((rc = isPrime(1+i)) == 1){
				grow(ring, i, n);
			}
		}

		case_num = case_num + 1;
	}
	return(0);
}