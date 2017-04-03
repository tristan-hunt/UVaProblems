#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define ALPHABET_LEN 256
#define NOT_FOUND patlen
#define max(a, b) ((a < b) ? b : a)

/* delta1 table: delta1[c] contains the distance between the last
// character of pat and the rightmost occurrence of c in pat.
// If c does not occur in pat, then delta1[c] = patlen.
// If c is at string[i] and c != pat[patlen-1], we can
// safely shift i over by delta1[c], which is the minimum distance
// needed to shift pat forward to get string[i] lined up 
// with some character in pat.
// this algorithm runs in alphabet_len+patlen time.*/
void make_delta1(int *delta1, uint8_t *pat, int32_t patlen) {
    int i;
    for (i=0; i < ALPHABET_LEN; i++) {
        delta1[i] = NOT_FOUND;
    }
    for (i=0; i < patlen-1; i++) {
        delta1[pat[i]] = patlen-1 - i;
    }
}

/* true if the suffix of word starting from word[pos] is a prefix 
// of word*/
int is_prefix(uint8_t *word, int wordlen, int pos) {
    int i;
    int suffixlen = wordlen - pos;
    /* could also use the strncmp() library function here*/
    for (i = 0; i < suffixlen; i++) {
        if (word[i] != word[pos+i]) {
            return 0;
        }
    }
    return 1;
}

/* length of the longest suffix of word ending on word[pos].*/
/* suffix_length("dddbcabc", 8, 4) = 2*/
int suffix_length(uint8_t *word, int wordlen, int pos) {
    int i;
    /* increment suffix length i to the first mismatch or beginning*/
    /* of the word*/
    for (i = 0; (word[pos-i] == word[wordlen-1-i]) && (i < pos); i++);
    return i;
}

/* delta2 table: given a mismatch at pat[pos], we want to align 
// with the next possible full match could be based on what we
// know about pat[pos+1] to pat[patlen-1].
//
// In case 1:
// pat[pos+1] to pat[patlen-1] does not occur elsewhere in pat,
// the next plausible match starts at or after the mismatch.
// If, within the substring pat[pos+1 .. patlen-1], lies a prefix
// of pat, the next plausible match is here (if there are multiple
// prefixes in the substring, pick the longest). Otherwise, the
// next plausible match starts past the character aligned with 
// pat[patlen-1].
// 
// In case 2:
// pat[pos+1] to pat[patlen-1] does occur elsewhere in pat. The
// mismatch tells us that we are not looking at the end of a match.
// We may, however, be looking at the middle of a match.
// 
// The first loop, which takes care of case 1, is analogous to
// the KMP table, adapted for a 'backwards' scan order with the
// additional restriction that the substrings it considers as 
// potential prefixes are all suffixes. In the worst case scenario
// pat consists of the same letter repeated, so every suffix is
// a prefix. This loop alone is not sufficient, however:
// Suppose that pat is "ABYXCDBYX", and text is ".....ABYXCDEYX".
// We will match X, Y, and find B != E. There is no prefix of pat
// in the suffix "YX", so the first loop tells us to skip forward
// by 9 characters.
// Although superficially similar to the KMP table, the KMP table
// relies on information about the beginning of the partial match
// that the BM algorithm does not have.
//
// The second loop addresses case 2. Since suffix_length may not be
// unique, we want to take the minimum value, which will tell us
// how far away the closest potential match is.
*/
void make_delta2(int *delta2, uint8_t *pat, int32_t patlen) {
    int p;
    int last_prefix_index = patlen-1;

    /* first loop*/
    for (p=patlen-1; p>=0; p--) {
        if (is_prefix(pat, patlen, p+1)) {
            last_prefix_index = p+1;
        }
        delta2[p] = last_prefix_index + (patlen-1 - p);
    }

    /* second loop*/
    for (p=0; p < patlen-1; p++) {
        int slen = suffix_length(pat, patlen, p);
        if (pat[p - slen] != pat[patlen-1 - slen]) {
            delta2[patlen-1 - slen] = patlen-1 - p + slen;
        }
    }
}

uint8_t* boyer_moore (uint8_t *string, uint32_t stringlen, uint8_t *pat, uint32_t patlen) {

    int i;
    int delta1[ALPHABET_LEN];
    int *delta2 = (int *)malloc(patlen * sizeof(int));
    make_delta1(delta1, pat, patlen);
    make_delta2(delta2, pat, patlen);

    /*The empty pattern must be considered specially*/
    if (patlen == 0) {
        free(delta2);
        return string;
    }

    i = patlen-1;
    while (i < stringlen) {
        int j = patlen-1;
        while (j >= 0 && (string[i] == pat[j])) {
            --i;
            --j;
        }
        if (j < 0) {
            free(delta2);
            return (string + i+1);
        }

        i += max(delta1[string[i]], delta2[j]);
    }
    free(delta2);
    return NULL;
}

void intervalize(char* notes, int strlen, char* text,int text_len){
    int i=0;
    int k = 0; /* length of 'intervals'*/

    /* Convert string of notes to semitones*/
    int a;
    int indexes[k+1];
    while (i<strlen){
        if (notes[i] == ' '){
            k = k + 1;
        }
        /*Convert char to int:*/
        a = notes[i];
        a = notes[i] -65; /*65 is ASCII uppercase A*/
        
        /* Now convert to semitones*/
        if (a == 0){
            indexes[i] = 1;
        }
        if (a == 1){
            indexes[i] = 3;
        }
        if (a > 1){
            indexes[i] = a*2;
        }
        if (a > 4){
            indexes[i] = indexes[i] -1;
        }


        /* Account for accidendals*/
        if (notes[i+1] == '#' || notes[i+1] == 'b'){
            if (notes[i+1] == '#'){
                indexes[i] = indexes[i] + 1;
            }
            if (notes[i+1] == 'b'){
                indexes[i] = indexes[i] - 1;
            }
            i = i + 1;
        }
        
        /* And go to the next note.*/
        i = i + 1;    
    }

    /* Now convert semitones to intervals*/
    int intervals[k];
    int dist;
    for (i = 0; i < k; i++){
        dist = indexes[i+1] - indexes[i];
        if (dist < 0){
            dist = dist + 12;
        }
        intervals[i] = dist; 
    }

    /* Finally make a string of ascii characters*/
    for (i=0; i < k; i++){
        text[i] = (char)(intervals[i] +97);/*Convert to string*/
    }
    return;
}

int main(int argc, char** argv){
    /* Get the input from stdin*/
    int rc, i;
    int N; /* Song length*/
    int M; /* Snippet length*/
    if ((rc=scanf("%d %d", &N, &M)) != 2){
        return(1);
    }
    /*printf("Starting while loop\n");*/
    while((N != 0) &&(M != 0)){
        char song[N];
        char snippet[M];
        if ((rc=scanf("%s", song))!= 1){
            printf("rc = %d\n", rc);
            return(1);
        }
        if ((rc = scanf("%s", snippet)) != 1){
            return(1);
        }
        /* Process the song, snippet, and check for a match*/
        /*printf("Converting song& snippet to intervals\n");*/
        /* Convert the sequence of notes into a sequence of intervals*/
        char text[N-1];
        char pattern[M-1];
        int song_len = strlen(song);
        int snippet_len = strlen(snippet);
        intervalize(song, song_len, text, N-1);
        intervalize(snippet, snippet_len, pattern, M-1);


        /* Use fast pattern-matching algorithm to test for match*/
        /*printf("Searching for a match\n");*/
        uint8_t *match = boyer_moore(text, N-1, pattern, M-1);
        if ((match == NULL)||(*match==0)){
            printf("N\n");
        }
        else{
            printf("S\n");
        }

        /* Scan for next input*/
        if ((rc=scanf("%d %d", &N, &M)) != 2){
            return(1);
        }
    }
    return(0);
}