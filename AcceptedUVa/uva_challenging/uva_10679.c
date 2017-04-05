 /* UVa problem: 10679 
#  * I Love Strings!!
#  * Topic: Strings
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *   Given a large string S, are q other query strings 
#  *   a substring of S?
#  *
#  * Solution Summary:
#  *
#  *   Use C's built-in strstr function to see if 
#  *     T is a substring of S. 
#  *
#  * Used Resources:
#  *
#  *   StackOverflow to learn of the existance of strstr().
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  *
#  * Tristan Hunt (Your Name)
#  */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv){
    int BUFFSIZE = 200000;
    char buffer[BUFFSIZE];
    int rc;
    if (fgets(buffer, BUFFSIZE, stdin) == NULL){
        printf("Failure to read k from stdin\n");
        return 0;
    }
    
    int k, i;
    sscanf(buffer, "%d", &k);
    for (i=0; i<k;i++){
        if (fgets(buffer, BUFFSIZE, stdin) == NULL){
            printf("Failure to read S from stdin\n");
            return 0;
        }

        char S[200000];
        sscanf(buffer, "%s", S);

        if (fgets(buffer, BUFFSIZE, stdin) == NULL){
            printf("Failure to get number of query strings\n");
            return 0;
        }
        int q, j;
        sscanf(buffer, "%d", &q);
        for(j=0;j<q;j++){
            if (fgets(buffer, BUFFSIZE, stdin) == NULL){
                printf("Failure to read T from stdin\n");
                return 0;
            }

            char T[2000];
            /* Try to read into query(if there is a string*/
            sscanf(buffer, "%s", T);



            /*printf("comparing %s to %s\n", S, T);*/
            if (strstr(S, T) != NULL){
                printf("y\n");
            } 
            else{
                printf("n\n");
            }
        }
    }
    return 0;
}