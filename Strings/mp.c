#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*Returns index of the given character in English, counting from 0*/
int alphabet_index(char c){
    int i = tolower(c);
    i = i - 97; /* 97 is ASCII for a*/
}

/*Returns the length of the match of the substrings of S beginning at idx
 and idx2*/
int match_length(char * S, int s_len, int idx1, int idx2){
    if (idx1 == idx2){
        return (s_len) - idx1;
    }
    int match_count = 0;
    while((idx1 < s_len) && (idx2 < s_len) && (S[idx1] == S[idx2])){
        match_count = match_count + 1;
        idx1++;
        idx2++;
    }
    return match_count;

}

/* Fills Z, the fundamental preprocessing of S. Z[i] is the length of the 
beginning at i which is also a prefix of S. This pre-processing is done
in O(n) time, where n is the length of S*/
void fundamental_preprocess(char *S, int len_s, int* z, int len_z){
    if (len_s == 0){
        len_z = 0; /* Harmless case of empty string*/

    }
    if (len_s == 1){ /* Harmless case of single-character string*/
        len_z = 1;
        z[1] = 1;
    }
    z[0] = len_s;
    z[1] = match_length(S, len_s, 0, 1);
    int i;
    for(i=2; i< 1+z[1]; i++){ /* Optimization*/
        z[i] = z[1] -i + 1;
    }

    /* Define upper, lower limits of the z-box*/
    int l = 0;
    int r = 0;
    int k, b, a;
    for(i=2+z[1]; i< len_s; i++){
        if (i <= r){ /* i falls withint existing z-box*/
            k = i-l;
            b = z[k];
            a = r-i+1;
            if ( b < a){/*b ends within existing z-box*/
                z[i] = b;
            }
            else{ /* b ends at or after the end of the z-box, we need to do*/
                z[i] = a+match_length(S, len_s, a, r+1); /*an exlpicit match to the right of the z-box*/
                l = i;
                r = i + z[i] -1;
            }            
        }
        else{
            z[i] = match_length(S, len_s, 0, i);
            if (z[i] > 0){
                l = i;
                r = i + z[i] - 1;
            }
        }
    }
    return;
}

/*
Generates F for S, an array used in a special case of the good suffix rule in the Boyer-Moore
string search algorithm. F[i] is the length of the longest suffix of S[i:] that is also a
prefix of S. In the cases it is used, the shift magnitude of the pattern P relative to the
text T is len(P) - F[i] for a mismatch occurring at i-1.
*/
void full_shift_table(char* S, int len_s, int* F, int len_f){
    int i, zv, j;
    int Z[len_s];
    int len_z = len_s;
    for(i = 0; i < len_s; i++){
        Z[i] = 0;
    }
    fundamental_preprocess(S, len_s, Z, len_z);
    int longest = 0;
    for (i = 0; i< len_z; i++){
        for(j = len_z-1; j > -1; j--){
            zv = Z[j];

        }
    }

}
/*  Generates R for S, which is an array indexed by the position of some character c in the 
    English alphabet. At that index in R is an array of length |S|+1, specifying for each
    index i in S (plus the index after S) the next location of character c encountered when
    traversing S from right to left starting at i. This is used for a constant-time lookup
    for the bad character rule in the Boyer-Moore string search algorithm, although it has
    a much larger size than non-constant-time solutions.
*/
    bad_character_table(P, len_p, R, len_r);



/*
Implementation of the Boyer-Moore string search algorithm. This finds all occurrences of P
in T, and incorporates numerous ways of pre-processing the pattern to determine the optimal 
amount to shift the string and skip comparisons. In practice it runs in O(m) (and even 
sublinear) time, where m is the length of T. This implementation performs a case-insensitive
search on ASCII alphabetic characters, spaces not included.
*/
int string_search(char* P, int len_p, char* T, int len_t){
    int i;
    if (len_p == 0 || len_t == 0 || len_t < len_p){
        return 0;
    }
    char* matches;

    /*Preprocessing*/
    
    int R[len_p]; 
    int L[len_p];
    int F[len_p];
    for (i = 0; i < len_p; i++){
        R[i] = 0;
        L[i] = 0;
        F[i] = 0;
    }
    int len_r = len_p, len_l =len_p, len_f=len_p;

    bad_character_table(P, len_p, R, len_r);
    good_suffix_table(P, len_p, L, len_l);
    full_shift_table(P, len_p, F, len_f); 
    /*...*/


}

int main(int argc, char** argv){
    /* Get the input from stdin*/
    int rc;
    int N; /* Song length*/
    int M; /* Snippet length*/
    if ((rc=scanf("%d %d", &N, &M)) != 2){
        return(1);
    }
    while((N != 0) &&(M != 0)){
        char* song;
        char* snippet;
        if ((rc=scanf("%s", song))!= 1){
            return(1);
        }
        if ((rc = scanf("%s", snippet)) != 1){
            return(1);
        }
        /* Process the song, snippet, and check for a match*/

        /* Convert the sequence of notes into a sequence of intervals*/

        /* Use fast pattern-matching algorithm to test for match*/

        /* Scan for next input*/
        if ((rc=scanf("%d %d", &N, &M)) != 2){
            return(1);
        }
    }
    return(0);
}