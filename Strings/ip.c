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

void printSuffArr(char* text, int *suffArr, int n){
    int i, j;
    /*printf("suffArr: \n");
    for (i=0; i<n; i++){
        for (j=suffArr[i]; j < n; j++){
            printf("%c ",text[j]);
        }printf("\n");
    }*/
    printf("suffArr: ");
    for (i=0; i<n; i++){
        printf("%d ",suffArr[i]);
    }printf("\n");
}

void printLCP(int *lcp, int lcp_len){
    int i, j;
    printf("LCP arr:   ");
    for(i=0;i<lcp_len;i++){
        printf("%d ", lcp[i]);
    }
    printf("\n");
}

void removeLCP(char *str1, char* lcs, int len1, int max_lcp){
                        /* Remove lcs (len = max_lcp) from str1*/
                        char *result = strstr(str1, lcs); /* pointer to pos of lcs in str1*/
                        int pos = result - str1; /* int representing offset of lcs from start of str1*/
                        char buffer1[60000];
                        /*printf("Result: %s, pos: %d\n", result, pos);*/
                        /*printf("str1: %s\n", str1);*/
                        strncpy(buffer1, str1, pos); /* copy first 'pos' chars from start of string to end*/
                        /*printf("buffer1: %s\n", buffer1);*/
                        buffer1[pos] = '\0';

                        /* Now copy the end of the string into 2nd buffer*/
                        char buffer2[60000];
                        result = result + max_lcp;
                        strncpy(buffer2, result, len1);
                        /*printf("buffer2: %s\n", buffer2);*/
                        buffer2[len1-pos+max_lcp] = '\0';

                        /* Finally, concatenate to form a new str1*/
                        strcpy(str1, buffer1);
                        strcat(str1, buffer2);

}


void findLCS(char * str1, char *str2, int len1, int len2, int K){
    int i, j;
    char text[100000];
    
    printf("%s\n", str1);

    /* Save copies of tdp, jnc codebase in order to find new positions in them.*/
    char tdp[90000];
    char jnc[90000];
    strcpy(tdp, str1);
    strcpy(jnc, str2);
    int tdp_len = len1;
    int jnc_len = len2;

    int k =0;
    while(k < K){
        /* Once LCS has been found, remove it from str1 and str2, and find the next largest LCS
        Until we've printed out K LCSs*/

        sprintf(text, "%s#%s", str1, str2);
        /*printf("text: %s\n", text);*/
        int n = len1+len2+1;

        /* Step 1: Find the suffix array*/
        int *suffArr = malloc(sizeof(int) * n);
        for (i=0; i<n; i++){
            suffArr[i] = -1;
        }
        buildSuffixArray(text, n, suffArr);
        /*printSuffArr(text, suffArr, n);*/


        /* Step 2: Find the LCP*/
        int lcp_len = n -1;   
        int lcp[lcp_len];
        kasai_lcp(text, lcp, suffArr, n);
        /*printLCP(lcp, lcp_len);*/

        /* Step 3: Find the LCS by looking at the LCP*/
        
            /* 3a - find index of lcs with max value*/
        int max_i = 0; /* Index of LCS with maximum value*/
        int max_lcp = 0;
        for (i=0; i<n; i++){
            if (i > 0){
                if ((lcp[i-1] > max_lcp)&&(isValid(i, suffArr[i], suffArr[i-1], len1))){
                    max_lcp =  lcp[i-1];
                    max_i = i;}}
        }

        if (max_lcp == 0){ int z;}
        else{ /* Print lcs without duplicates*/
            int jnc_pos = 0;
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
                        char *result = strstr(jnc, lcs);
                        int pos = result - jnc;
                        jnc_pos = pos;
                        printf("INFRINGING SEGMENT %d LENGTH %d POSITION %d\n", k+1, max_lcp, jnc_pos);
                        printf("%s\n", lcs);
                        
                        /* Remove lcp from both str1 and str2*/
                        /* This is okay to do here because str1, str2 only needed again at top of while loop*/
                        /*removeLCP(str1, lcs, len1, max_lcp);*/
                        removeLCP(str2, lcs, len2, max_lcp);
                        /*printf("new str1: %s\n", str1);
                        printf("new str2: %s\n", str2);*/

                        len1 = len1 - max_lcp;
                        len2 = len2 - max_lcp;

                        sprintf(prev, "%s", lcs);
                    
                    }
                }
            }
        }
    
        /* Finished printing lcp #k*/
        k = k + 1;
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
    int BUFFSIZE = 100000;
    char *buffer = malloc(BUFFSIZE*sizeof(char));
    char *cdbs1 = malloc(BUFFSIZE*sizeof(char));
    char *cdbs2 = malloc(BUFFSIZE*sizeof(char));
    
    char* substring = malloc(BUFFSIZE*sizeof(char));
    int sub_len;
    int cdbs1_len;
    int cdbs2_len;
    int i;
    int first = 1;
    int k;
    char begin_tdp[20];
    char end_tdp[20];
    strcpy(begin_tdp,"BEGIN TDP CODEBASE");
    strcpy(end_tdp,"END TDP CODEBASE");

    char begin_jcn[20];
    char end_jcn[20];
    strcpy(begin_jcn, "BEGIN JCN CODEBASE");
    strcpy(end_jcn, "END JCN CODEBASE");
    char newline[2] = "\n";
/* begin while loop*/ 
    while(1){    
        if (fgets(buffer, BUFFSIZE, stdin) == NULL){
            return(0);
        }
        sscanf(buffer, "%d", &k);
        if (k==0){
            /*printf("k=0, quit\n");*/
            return 0;
        }
        
        /* Get one line of input*/
        if(fgets(buffer, BUFFSIZE, stdin)==NULL){
            printf("error!\n");
            return 1;
        }
        buffer[strcspn(buffer, "\n\r")]= '\0';

        /* Check if we've begun reading TDP codebase*/
        if (strcmp(buffer, begin_tdp) == 0){
            if(fgets(buffer, BUFFSIZE, stdin) == NULL){
                printf("error!\n");
                return 1;
            }
            buffer[strcspn(buffer, "\n\r")]= '\0';


            /* Read from stdin until we hit END TDP CODEBASE*/
            int first = 1;
            while(strcmp(buffer, end_tdp) != 0){
                strcat(buffer, newline);
                if (first==1){
                strcpy(cdbs1, buffer);
                    first = 0;
                }
                else{
                    strcat(cdbs1, buffer);
                }

                if(fgets(buffer, BUFFSIZE, stdin) == NULL){
                    printf("error!\n");
                    return 1;
                }
                buffer[strcspn(buffer, "\n\r")]= '\0';
            }
        }
        /*printf("TDP Codebase: \n%s", cdbs1);*/
    

        /* Get another line  of input*/
        if(fgets(buffer, BUFFSIZE, stdin) == NULL){
            printf("error!\n");
            return 1;
            }
        buffer[strcspn(buffer, "\n\r")]= '\0';

    
        /* Check if we've begun reading JCN codebase*/
        if (strcmp(buffer, begin_jcn) == 0){
            if(fgets(buffer, BUFFSIZE, stdin) == NULL){
                printf("error reading 'begin jcn'\n");
                return 1;
            }
            buffer[strcspn(buffer, "\n\r")]= '\0';


            /* Read from stdin until we hit END JCN CODEBASE*/
            int first = 1;
            while(strcmp(buffer, end_jcn) != 0){
                strcat(buffer, newline);
                if (first==1){
                    strcpy(cdbs2, buffer);
                    first = 0;
                }
                else{
                    strcat(cdbs2, buffer);
                }



                if(fgets(buffer, BUFFSIZE, stdin) == NULL){
                    printf("error reading next line of input!\n");
                    return 1;
                }
                buffer[strcspn(buffer, "\n\r")]= '\0';
            }
        }
        /*printf("JCN Codebase: \n%s", cdbs2);*/

        cdbs1_len = strlen(cdbs1);
        cdbs2_len = strlen(cdbs2);
    
        /* Execute code to find LCS*/
        if (first == 0){
            printf("\n");
        }
        first = 0;
        findLCS(cdbs1, cdbs2, cdbs1_len, cdbs2_len, k);
    }

    free(buffer);
    free(cdbs1);
    free(cdbs2);
    return(0);
}