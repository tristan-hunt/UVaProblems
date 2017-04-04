/*http://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/*/
/*http://www.geeksforgeeks.org/%C2%AD%C2%ADkasais-algorithm-for-construction-of-lcp-array-from-suffix-array*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* Struct to store information about the suffix*/
struct suffix{
    int index; /* Stores the original index*/
    int rank[2]; /* Stores the rank of the suffix*/
    char* suff;
};

struct entry {
    int nr[2], p;
};

int cmp2(const void * x, const void * y){
    struct entry *i;
    i = (struct entry*)x;
    struct entry *j;
    j = (struct entry*)y;
    struct entry a = *i;
    struct entry b = *j;
    return a.nr[0] == b.nr[0] ? (a.nr[1] < b.nr[1] ? 1:0) : (a.nr[0] < b.nr[0] ? 1: 0);

}

/*void create_suff_arr(char* text, int* suffArr, int n){
    int logn = (int)log2(n);
    struct entry L[n];
    int P[logn][n];
    int i;
    for (i = 0; i<n; i++){
        P[0][i] =text[i] - 'A';
    }
    int stp, cnt;
    for (stp = 1, cnt = 1; cnt >> 1 <n; stp++, cnt <<= 1){
        for (i=0; i < n; i++){
            L[i].nr[0] = P[stp-1][i];
            L[i].nr[1] = i + cnt < n ? P[stp -1][i + cnt] : -1;
            L[i].p = 1;
        }
        qsort(L, sizeof(struct entry), n, cmp);
        for (i = 0; i < n; i++){
            P[stp][L[i].p] = i > 0 && L[i].nr[0] == L[i-1].nr[0] && L[i].nr[1] == L[i-1].nr[1] ?P[stp][L[i-1].p] : i;
        }
    }                                             
}*/




/* Comparison function used by sort() to compare two suffixes*/
/* Compares two pairs - returns 1 if first pair is smaller*/
int cmp(const void * x, const void * y){
    struct suffix *i;
    i = (struct suffix*)x;
    struct suffix *j;
    j = (struct suffix*)y;
    struct suffix a = *i;
    struct suffix b = *j;
    if (a.rank[0] < b.rank[0]){
        return 1;
    }
    if (a.rank[0] == b.rank[0]){
        if (a.rank[1] < b.rank[1]){
            return(1);
        }else{
            return 0;
        }
    }else{
        return 0;
    }
    /*return (a.rank[0] == b.rank[0])? (a.rank[1] < b.rank[1] ?1: 0):
        (a.rank[0] < b.rank[0] ?1: 0);*/
}



void create_suff_arr3(char* text, int* suffArr, int n){
    /*printf("create suff arr: %s, mem&:%d, len:%d\n", text, *suffArr, n);*/
    struct suffix suffixes[n];


    int i,j;

    /*printf("Finding rank 0 and 1...\n");*/
    for (i = 0; i < n; i++){
        suffixes[i].index = i;
        suffixes[i].rank[0] = text[i] - 'A';
        suffixes[i].rank[1] = ((i+1) < n)? (text[i+1] - 'A'): -1;
    }

    printf("Suffixes: \n");
    for (i = 0; i < n; i++)
    {
        printf("%d: ",suffixes[i].index);
        printf("%d ",suffixes[i].rank[0]);
        printf("%d \n",suffixes[i].rank[1]);
    }

    printf("Sorting suffixes by rank... \n");
    /* Sort suffixes using comparison function defined above*/
    qsort(suffixes, n, sizeof(struct suffix), cmp);

    printf("Suffixes: \n");
    for (i = 0; i < n; i++)
    {
        for (j=i; j<n; j++){
            printf("%c", text[j]);
        }
        printf(" %d: ",suffixes[i].index);
        printf("%d ",suffixes[i].rank[0]);
        printf("%d \n",suffixes[i].rank[1]);
    }

    printf("done printing suffixes\n");

    /* So far, they are sorted according to first 2 characters*/
    /* Now we can sort them according to first 4, 8, ... characters*/
    int ind[n];
    int k;

    for (k = 4; k < 2*n; k = k*2){
        /* Assigning rank, index values to first suffix*/
        /*printf("Assigning rank, index values to first suffix\n");*/
        int rank = 0;
        int prev_rank = suffixes[0].rank[0];
        suffixes[0].rank[0] = rank;
        ind[suffixes[0].index] = 0;
    
        /*printf("Assigning rank to suffixes!\n");*/
        for (i = 1; i < n; i++){
            if (suffixes[i].rank[0] == prev_rank && suffixes[i].rank[1] == suffixes[i-1].rank[1]){
                /*printf("first, next rank are same as a previous suffix\n");*/
                prev_rank = suffixes[i].rank[0];
                suffixes[i].rank[0] = rank;
            } else{
                /*printf("increment rank and assign\n");*/
                /*printf("i: %d, suffixes[i].rank[0]:%d\n", i, suffixes[i].rank[0]);*/
                prev_rank = suffixes[i].rank[0];
                suffixes[i].rank[0] = ++rank;
            }
            ind[suffixes[i].index] = i;
        }
        /*printf("Second for loop... \n");*/
        for (i = 0; i < n; i++){
            int nextindex = suffixes[i].index + k/2;
            suffixes[i].rank[1] = (nextindex < 2)?
                                    suffixes[ind[nextindex]].rank[0]: -1;
        }
        qsort(suffixes, n, sizeof(struct suffix), cmp);
    }

    /*printf("Storing indexes in a suffix array...\n");*/
    /* Store indexes of all sorted suffixes in the suffix array*/
    for(i = 0; i < n; i++){
        suffArr[i] = suffixes[i].index;
    }

    /*printf("suffix array:\n");
    for(i=0; i < n; i++){
        printf("(%d, %d, %d), ", suffixes[i].index, suffixes[i].rank[0], suffixes[i].rank[1]);
    }
    printf("....Done! Returning to whence I came!\n");*/
    return;

}

/* Create the lcp.*/
void kasai_lcp(char* text, int* lcp, int* suffArr, int n){
    int i;
    /*printf("kasai lcp: %s, suffArr: ", text);
    for(i=0; i<n;i++){
        printf("%d ",suffArr[i]);
    }
    printf("&lcp: %d, len(n)=%d\n", *lcp, n);*/

    /* Auxialliary array to store inverse of suffix array elements*/
    /* eg. suffArr[0] = 5 --> suffArr[5] = 0*/
    int invSuff[n];
    for (i = 0; i < n; i++){
        invSuff[suffArr[i]] = i;
    }

    /* Initialize length of previous LCP*/
    int k = 0;

    /* Process all suffixes one by one starting from first suffix in txt[]*/
    for (i = 0; i < n; i++){
        /* If current suffix is at n-1, then don't have to consider next substring*/
        /* Since LCP isn't defined, we put 0*/
        if (invSuff[i] == n-1){
            k=0;
            continue;
        }

        /* j contains index of next substring to be considered to compare*/
        /* with the present substring*/
        int j = suffArr[invSuff[i] + 1];

        /* Directly start matching from kth index as at least k-1 chars will match*/
        while( i+k<n && j+k<n && text[i+k] == text[j+k] ){
            k++;
        }
        lcp[invSuff[i]] = k; /* LCP for present suffix*/

        /* Delete starting character from the string*/
        if (k>0){
            k--;
        }
    }

    return;
}

/* Suffix array based search function 
void search(char* pat, char* text, int *suffArr, int n){
    int m = strlen(pat); /* length of pattern - needed for strncmp

    int l = 0, r = n-1;  /* Initilize left and right indexes
    while (l <= r)
    {
        /* See if 'pat' is prefix of middle suffix in suffix array
        int mid = l + (r - l)/2;
        int res = strncmp(pat, txt+suffArr[mid], m);
        
        /* If match is found at middle, print and return
        if (res == 0){

        }




    }
}*/

void longest_substring(char* DNA, int dna_len){
    printf("LSS: %s, %d\n", DNA, dna_len);  
    int i;
    int suff_arr[dna_len];
    
    /* Step 1: Create the Suffix Array*/
    create_suff_arr3(DNA, suff_arr, dna_len);
    printf("Suff_arr: ");
    for(i=0; i<dna_len;i++){
        printf("%d ", suff_arr[i]);
    }printf("\n");    
    /* Print the suffix arrays*/
    int j;
    for(i=0; i<dna_len; i++){
        for(j=suff_arr[i]; j<dna_len;j++){
            printf("%c", DNA[j]);
        }
        printf("\n");
    }

    /* Step 2: Create the LCP */
    int lcp_len = dna_len -1;   
    int lcp[lcp_len];
    kasai_lcp(DNA, lcp, suff_arr, dna_len);
    
    /*printf("LCP arr: ");
    for(i=0;i<lcp_len;i++){
        printf("%d ", lcp[i]);
    }
    printf("\n");*/

    /* Step 3: Find Longest Repeating Substring*/

    /* Step 3a: Find the max value of lcp and its index*/
    int max_val = -1;
    int max_i = -1;
    for(i=0; i < lcp_len; i++){
        if (lcp[i] > max_val){
            max_val = lcp[i];
            max_i = i;
        }
    }
    /*printf("max lcp: %d @ %d\n", max_val, max_i);*/

    /* Step 3b: Find longest substring*/
    int start_idx = suff_arr[max_i];
    int end_idx = suff_arr[max_i] + max_val -1;
    int sub_len = end_idx-start_idx;
    /*printf("longest repeating: ");*/
    for (i=start_idx; i < end_idx+1; i++){
        printf("%c", DNA[i]);
    }
    if (max_val == 0){
        printf("No repetitions found!\n");
    }else{
        printf(" %d\n", sub_len+1);
    }
    return;
}

int main(int argc, char** argv){
    int T;
    int rc;
    int bufsize = 5;
    int BUFFSIZE = 2000;
    char *buffer = malloc(bufsize*sizeof(char));
    if (fgets(buffer, bufsize, stdin) == NULL){
        printf("Failure to read T\n");
        return(1);
    }
    sscanf(buffer, "%d", &T);
    /*printf("%d\n", T);*/
    char *DNA = malloc(BUFFSIZE*sizeof(char));
    char* substring = malloc(BUFFSIZE*sizeof(char));
    int sub_len;
    int dna_len;
    int i;
    for (i=0; i < T; i++ ){
        if (fgets(DNA, 2000, stdin) == NULL){
            printf("Failure to read DNA sequence!\n");
            return(1);
        }
        DNA[strcspn(DNA, "\n\r")]= '\0';
        printf("DNA: %s\n", DNA);
        dna_len = strlen(DNA);
        longest_substring(DNA, dna_len);

    }
    free(buffer);
    free(DNA);
    return(0);
}



void create_suff_arr2(char* text, int* suffArr, int n){
    struct suffix suffixes[n];
    int i;
    for(i =0; i<n; i++){
        suffixes[i].index = i;
        suffixes[i].suff = (text+i);
    }

    qsort(suffixes, n, sizeof(struct suffix), cmp);

    for(i=0; i < n; i++){
        suffArr[i] = suffixes[i].index;
    }
}

