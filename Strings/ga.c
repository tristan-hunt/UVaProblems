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
    return (a.rank[0] == b.rank[0])? (a.rank[1] < b.rank[1] ?1: 0):
        (a.rank[0] < b.rank[0] ?1: 0);
}

/* This is the main function that takes a string 'txt' of size n as an*/
/* argument, builds and return the suffix array for the given string*/
int *buildSuffixArray(char *txt, int n, char *suffixArr)
{

    printf("Building suffix array for %s\n", txt);
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
 
    printf("Suffixes: \n");
    for (i = 0; i < n; i++)
    {
        printf("%d: ",suffixes[i].index);
        printf("%d ",suffixes[i].rank[0]);
        printf("%d \n",suffixes[i].rank[1]);
    }



    /* Sort the suffixes using the comparison function*/
    /* defined above.*/
    qsort(suffixes, sizeof(struct suffix), n, cmp);

    printf("Suffixes: \n");
    for (i = 0; i < n; i++)
    {
        printf("%d: ",suffixes[i].index);
        printf("%d ",suffixes[i].rank[0]);
        printf("%d \n",suffixes[i].rank[1]);
    }




    /* At his point, all suffixes are sorted according to first*/
    /* 2 characters.  Let us sort suffixes according to first 4*/
    /* characters, then first 8 and so on*/
    int ind[n];  /* This array is needed to get the index in suffixes[]*/
                 /* from original index.  This mapping is needed to get*/
                 /* next suffix.*/

    int k;
    for (k = 4; k < 2*n; k = k*2)
    {
        
        /* Assigning rank and index values to first suffix*/
        int rank = 0;
        int prev_rank = suffixes[0].rank[0];
        suffixes[0].rank[0] = rank;
        printf("suffixes[0].index = %d\n", suffixes[0].index);
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
 
        printf("5\n");

        /* Assign next rank to every suffix*/
        for (i = 0; i < n; i++)
        {
            int nextindex = suffixes[i].index + k/2;
            suffixes[i].rank[1] = (nextindex < n)?
                                  suffixes[ind[nextindex]].rank[0]: -1;
        }
 
        /* Sort the suffixes according to first k characters*/
        qsort(suffixes, sizeof(struct suffix), n, cmp);
    }
 
    printf("3\n");

    /* Store indexes of all sorted suffixes in the suffix array*/
    for (i = 0; i < n; i++)
        suffixArr[i] = suffixes[i].index;
 
    /* Return the suffix array*/
    return  0;
}

void longest_substring(char* string, int len){
    printf("DNA: %s %d\n", string, len);
    int i;
    /* Step 1: Find the suffix array*/
    char *suffArr = malloc(sizeof(char) * len);
    for (i=0; i<len; i++){
        suffArr[i] = -1;
    }

    buildSuffixArray(string, len, suffArr);

    printf("suffArr: ");
    for (i=0; i<len; i++){
        printf("%d ", suffArr[i]);
    }printf("\n");

    free(suffArr);
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
        /*printf("DNA: %s %d\n", DNA, dna_len);*/
        
        longest_substring(DNA, dna_len);

    }
    free(buffer);
    free(DNA);
    return(0);
}
