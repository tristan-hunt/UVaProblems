#include <stdio.h>
#include <string.h>
#include <stdlib.h>
/*http://www.geeksforgeeks.org/suffix-tree-application-5-longest-common-substring-2/*/
#define MAX_CHAR 256


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

int isValid(int i, int idx1, int idx2, int n){
    /* Returns 1 if one of idx1, idx2 is higher than
    n, and the other is lower. Otherwise, returns false*/

    if (idx1 > n){
        if (idx2 <n){
            return 1;
        }
        else{
            return 0;
        }
    }if (idx2 > n){
        return 1;
    }
    return 0;
}

void findLCS(char * str1, char *str2, int len1, int len2){
    int i, j;
    char text[1000];
    sprintf(text, "%s#%s", str1, str2);
    int n = len1+len2+1;

    /* Step 1: Find the suffix array*/
    int *suffArr = malloc(sizeof(int) * n);
    for (i=0; i<n; i++){
        suffArr[i] = -1;
    }

    buildSuffixArray(text, n, suffArr);
    /*printf("suffArr: \n");
    for (i=0; i<n; i++){
        for (j=suffArr[i]; j < n; j++){
            printf("%c ",text[j]);
        }printf("\n");
    }*//*
    printf("suffArr: ");
    for (i=0; i<n; i++){
        printf("%d ",suffArr[i]);
    }printf("\n");*/


    /* Step 2: Find the LCP*/
    int lcp_len = n -1;   
    int lcp[lcp_len];
    kasai_lcp(text, lcp, suffArr, n);
    
    /*printf("LCP arr:   ");
    for(i=0;i<lcp_len;i++){
        printf("%d ", lcp[i]);
    }
    printf("\n");*/

    /* Step 3: Find the LCS by looking at the LCP*/
    /*printf("len1: %d\n", len1);
    printf("suffArr: \n");*/

    int max_i = 0; /* Index of LCS with maximum value*/
    int max_lcp = 0;
    for (i=0; i<n; i++){
        /*
        for (j=suffArr[i]; j < n; j++){
            printf("%c ",text[j]);

        }*/

        if (i > 0){
           /* printf("\t\tlcp[i-1]: %d suffArr[i]:%d ", lcp[i-1], suffArr[i]);*/
            if ((lcp[i-1] > max_lcp)&&(isValid(i, suffArr[i], suffArr[i-1], len1))){
                max_lcp =  lcp[i-1];
                max_i = i;
                
            }


        }
        /*printf("\n");*/
    }

    if (max_lcp == 0){
        printf("No common sequence.\n");
    }else{

        /* Print lcs without duplicates*/
        char lcs[max_lcp+1];
        char prev[max_lcp+1];
        char tmp[2];
        for (i=0; i< n; i++){
            if ((lcp[i-1]==max_lcp)&&(isValid(i, suffArr[i], suffArr[i-1], len1))){
                sprintf(lcs, "%c", text[suffArr[i-1]]);
                for (j=suffArr[i-1]+1; j < suffArr[i-1]+max_lcp; j++){
                    sprintf(tmp, "%c", text[j]);
                    strcat(lcs,tmp);
                }
                /* Compare lcs, prev. Print lcs if different and then store it in prev.*/
                if (strcmp(prev, lcs)!=0){
                    printf("%s\n", lcs);
                    sprintf(prev, "%s", lcs);
                }
            }
        }
    }




    /* Print every LCS found:
    for (i=0; i< n; i++){
        if ((lcp[i-1]==max_lcp)&&(isValid(i, suffArr[i], suffArr[i-1], len1))){
            for (j=suffArr[i-1]; j < suffArr[i-1]+max_lcp; j++){
                printf("%c",text[j]);
            }printf("\n");
        }
    }printf("\n");*/

}  


int main(int argc, char** argv){
    int rc;
    int BUFFSIZE = 10000;

    char *dna1 = malloc(BUFFSIZE*sizeof(char));
    char *dna2 = malloc(BUFFSIZE*sizeof(char));
    
    char* substring = malloc(BUFFSIZE*sizeof(char));
    int sub_len;
    int dna1_len;
    int dna2_len;
    int i;
    int first = 1;
    while(1){
        if (fgets(dna1, BUFFSIZE, stdin) == NULL){
            /*printf("Failure to read DNA sequence!\n");*/
            return(0);
        }
        if (fgets(dna2, BUFFSIZE, stdin) == NULL){
            /*printf("Failure to read DNA sequence!\n");*/
            return(0);
        }

        /* Strip the newline, find the size*/    
        dna1[strcspn(dna1, "\n\r")]= '\0';
        dna2[strcspn(dna2, "\n\r")]= '\0';
        dna1_len = strlen(dna1);
        dna2_len = strlen(dna2);
    
        /* Execute code to find LCS*/
        if (first == 0){
            printf("\n");
        }
        first = 0;
        findLCS(dna1, dna2, dna1_len, dna2_len);
        
    
        if (fgets(dna1, BUFFSIZE, stdin) == NULL){
            /*Read the newline*/
            return(0);
        }
    }

    free(dna1);
    free(dna2);
    return(0);
}