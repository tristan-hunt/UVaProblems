#include <stdio.h>
#include <values.h>

#define MAX 60
#define inf MAXLONG

int main()
{
	long L,N,i,j,n,x,y,q,l,k,t,sum,m[MAX][MAX],p[MAX];
	int rc;
	while(scanf("%ld",&L)==1 && L){
		rc = scanf("%ld",&N);
		y = 0;
		for(i=1;i<=N;i++) {
			rc = scanf("%ld",&x);
			p[i] = x - y;
    		y = x;
        }
    p[i] = L - y;

    n = i;

    for(i=0;i<=n;i++)
		m[i][i] = 0;
	
	for(l=2;l<=n;l++){
   		for(i=1;i<=n-l+1;i++){
   			j = i + l - 1;
      		m[i][j] = inf;

			for(k=i;k<=j-1;k++) {
				q = m[i][k] + m[k+1][j] ;
				sum = 0;

				for(t=i;t<=j;t++)
        			sum += p[t];

				q += sum;

			if(q<m[i][j])
				m[i][j] = q;
        	}
    	}
    }

    printf("The minimum cutting is %ld.\n",m[1][n]);
 }
 return 0;
}
