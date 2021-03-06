/*http://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


/* Struct to store information about the suffix*/
struct suffix{
    int index; /* Stores the original index*/
    int rank[2]; /* Stores the rank of the suffix*/
    char* suff;
};


/* Comparison function used by sort() to compare two suffixes*/
/* Compares two pairs - returns 1 if first pair is smaller*/
int cmp(const void * x, const void * y){
    struct suffix *i;
    i = (struct suffix*)x;
    struct suffix *j;
    j = (struct suffix*)y;
    struct suffix a = *i;
    struct suffix b = *j;
    if(a.rank[0] == b.rank[0]){
        if (a.rank[1] < b.rank[1]){
            return 0;
        }
        else{
            return 1;
        }
    }
    if (a.rank[0] < b.rank[0]){
        return 0;
    }
    else{
        return 1;
    }
    /*return (a.rank[0] == b.rank[0])? (a.rank[1] > b.rank[1] ?1: 0):
        (a.rank[0] > b.rank[0] ?1: 0);*/
}

/* This is the main function that takes a string 'txt' of size n as an*/
/* argument, builds and return the suffix array for the given string*/
int *buildSuffixArray(char *txt, int n, int *suffixArr)
{

    /*printf("Building suffix array for %s\n", txt);*/
    int i;
    /* A structure to store suffixes and their indexes*/
    struct suffix suffixes[n];
 
    /* Store suffixes and their indexes in an array of structures.*/
    /* The structure is needed to sort the suffixes alphabatically*/
    /* and maintain their old indexes while sorting*/
    for (i = 0; i < n; i++)
    {
        suffixes[i].index = i;
        suffixes[i].rank[0] = txt[i] - 'A';
        suffixes[i].rank[1] = ((i+1) < n)? (txt[i + 1] - 'A'): -1;
    }
 
    /*printf("Suffixes: \n");
    for (i = 0; i < n; i++)
    {
        printf("%d: ",suffixes[i].index);
        printf("%d ",suffixes[i].rank[0]);
        printf("%d \n",suffixes[i].rank[1]);
    }*/



    /* Sort the suffixes using the comparison function*/
    /* defined above.*/
    qsort(suffixes,n, sizeof(struct suffix), cmp);

    /*printf("Suffixes: \n");
    for (i = 0; i < n; i++)
    {
        printf("%d: ",suffixes[i].index);
        printf("%d ",suffixes[i].rank[0]);
        printf("%d \n",suffixes[i].rank[1]);
    }*/




    /* At his point, all suffixes are sorted according to first*/
    /* 2 characters.  Let us sort suffixes according to first 4*/
    /* characters, then first 8 and so on*/
    int ind[n];  /* This array is needed to get the index in suffixes[]*/
                 /* from original index.  This mapping is needed to get*/
                 /* next suffix.*/

    int k;
    for (k = 4; k < 2*n; k = k*2)
    {
        /*
        printf("Suffixes: k= %d\n", k);
        for (i = 0; i < n; i++)
        {
            printf("%d: ",suffixes[i].index);
            printf("%d ",suffixes[i].rank[0]);
            printf("%d \n",suffixes[i].rank[1]);
        }*/
        
        /* Assigning rank and index values to first suffix*/
        int rank = 0;
        int prev_rank = suffixes[0].rank[0];
        suffixes[0].rank[0] = rank;
        ind[suffixes[0].index] = 0;
 
        /* Assigning rank to suffixes*/
        for (i = 1; i < n; i++)
        {
            /* If first rank and next ranks are same as that of previous*/
            /* suffix in array, assign the same new rank to this suffix*/
            if (suffixes[i].rank[0] == prev_rank &&
                    suffixes[i].rank[1] == suffixes[i-1].rank[1])
            {
                prev_rank = suffixes[i].rank[0];
                suffixes[i].rank[0] = rank;
            }
            else /* Otherwise increment rank and assign*/
            {
                prev_rank = suffixes[i].rank[0];
                suffixes[i].rank[0] = ++rank;
            }
            ind[suffixes[i].index] = i;
        }
 
        /* Assign next rank to every suffix*/
        for (i = 0; i < n; i++)
        {
            int nextindex = suffixes[i].index + k/2;
            suffixes[i].rank[1] = (nextindex < n)?
                                  suffixes[ind[nextindex]].rank[0]: -1;
        }
 
        /* Sort the suffixes according to first k characters*/
        qsort(suffixes, n, sizeof(struct suffix), cmp);
    }
 
    /* Store indexes of all sorted suffixes in the suffix array*/
    for (i = 0; i < n; i++)
        suffixArr[i] = suffixes[i].index;
 
    /* Print out the final suffix array*/
    /*int j;
    for (i=0; i< n; i++){
        for(j=suffixArr[i];j<n;j++){
            printf("%c",txt[j]);
        }printf("\n");
    }*/


    /* Return the suffix array*/
    return  0;
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

void longest_substring(char* string, int len){
    /*printf("DNA: %s %d\n", string, len);*/
    int i;
    /* Step 1: Find the suffix array*/
    int *suffArr = malloc(sizeof(int) * len);
    for (i=0; i<len; i++){
        suffArr[i] = -1;
    }

    buildSuffixArray(string, len, suffArr);

    /*printf("suffArr: ");
    for (i=0; i<len; i++){
        printf("%d ", suffArr[i]);
    }printf("\n");*/

    /* Step 2: Build the LCP*/ 
    int lcp_len = len -1;   
    int lcp[lcp_len];
    kasai_lcp(string, lcp, suffArr, len);
    
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
    int start_idx = suffArr[max_i];
    int end_idx = suffArr[max_i] + max_val -1;
    int sub_len = end_idx-start_idx;
    /*printf("longest repeating: ");*/
    if (max_val == 0){
        printf("No repetitions found!\n");
    }
    else{
        char substring[sub_len];
        char temp[2];
        sprintf(substring, "%c", string[start_idx]);
        for (i=start_idx+1; i < end_idx+1; i++){
            sprintf(temp, "%c", string[i]);
            strcat(substring, temp);
        }
        int count = 0;
        const char *tmp = string;
        while(tmp = strstr(tmp, substring)){
            count++;
            tmp++;
        }

        printf("%s %d\n",substring, count);
    }

    free(suffArr);
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
        dna_len = strlen(DNA);
        if (dna_len == 1){
            printf("No repetitions found!\n");
        }
        else{
            /*printf("DNA: %s %d\n", DNA, dna_len);*/
            longest_substring(DNA, dna_len);
        }

    }
    free(buffer);
    free(DNA);
    return(0);
}
