#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define ALPHABET_LEN 256
#define NOT_FOUND patlen

void kmp_table(char* W, int len_w, int* T,int len_t){
    /*  Note that len_t == len_w*/
    printf("kmp table\n");
    int pos = 2;
    int cnd = 0;

    int i;
    T[0] = -1;
    T[1] = 0;

    for(i=0; i < len_t; i++){
        printf("%d ", T[i]);
    }
    printf("\n");
    printf("len_w: %d\n", len_w);
    while (pos < len_w){
        /*# first case - substring continues*/
        if (W[pos-1] == W[cnd]){
            T[pos] = cnd + 1;
            cnd = cnd + 1;
            pos = pos + 1;
        }
        /*# second case: it doesn't, but we can fall back*/
        else if (cnd > 0){
            cnd = T[cnd];
        }
        /*# third case: we have run out of candidates. */
        else {
            T[pos] = 0;
            pos = pos + 1;
        }
    }
    
    for(i=0; i < len_t; i++){
        printf("%d ", T[i]);
    }
    printf("\n");
    return;

}

int kmp_search(char* S, int len_s, char* W, int len_w){
    printf("kmp search\n");
    int m = 0;
    int i = 0;
    int len_t = len_s;
    int T[len_t];
    
    for(i=0; i < len_t; i++){
        T[i] = 0;
    }

    kmp_table(W, len_w, T, len_t);
    printf("S: %s, len_s: %d, W: %s, len_w: %d, len_t: %d\n",S, len_s, W, len_w, len_t);
    i = 0;
    while(m+1 < len_s){
        /*printf("W: %s, i: %d, S:%s, m+1:%d\n", W, i, S, m+1);*/
        if (W[i] == S[m+1]) {
            if (i == (len_w - 1)) {
                return m;
            }
            i = i + 1;
        }
        else{
            if (T[i] > -1){
                /*printf("3: i: %d, T[i] = %d\n", i, T[i]);*/
                m= m+1 - T[i];
                i = T[i];
            }
            else{
                m = m + 1;
                i = 0;
            }
        }
    }
    return len_s;
}

void intervalize(char* notes, int notes_len, char* text,int text_len){
    int i=0;
    /*printf("intervalizing %s. str_len: %d, text_len: %d\n", notes, notes_len, text_len);*/


    /* Convert string of notes to semitones*/
    
    int indexes_len = text_len+1;
    int indexes[indexes_len];
    char space = ' ';
    char *note;
    note = strtok(notes, &space);
    int len;
    
    while(note != NULL){
        len = strlen(note);
        /*printf("LEN:  %d ", len);*/
        int index = note[0];
        /*printf(" FIRST: %d ", index);*/
        index = index - 65; /* 65 - value of A in ASCII*/
        /*printf("INDEX: %d ", index);*/
        switch(index){
            case 0: indexes[i] = 1; break;
            case 1: indexes[i] = 3; break;
            case 2: indexes[i] = 4; break;
            case 3: indexes[i] = 6; break;
            case 4: indexes[i] = 8; break;
            case 5: indexes[i] = 9; break;
            case 6: indexes[i] = 11; break;

        }        

        /*printf("%d ", indexes[i]);*/

        if (len > 1){
            /*printf("%c ", note[1]);*/
            if (note[1] == '#'){
                indexes[i] = indexes[i] + 1;
            }
            if (note[1] == 'b'){
                indexes[i] = indexes[i] - 1;
            }
        }
        /*printf("%d \n", indexes[i]);*/
        i = i + 1;
        note = strtok(NULL, &space);
    }

    /*
    printf("Indexes: %d\n", indexes_len);
    for(i = 0; i < indexes_len; i++){
        printf("%d ", indexes[i]);

    }
    printf("/\n");*/


    /* Now convert semitones to intervals*/
    int intervals_len = indexes_len-1;
    int intervals[intervals_len];
    int dist;
    for (i = 0; i < intervals_len; i++){
        dist = indexes[i+1] - indexes[i];
        if (dist < 0){
            dist = dist + 12;
        }
        intervals[i] = dist; 
    }
    
    /*
    printf("Intervals: %d\n", intervals_len);
    for(i = 0; i < intervals_len; i++){
        printf("%d ", intervals[i]);

    }
    printf("\n");*/

    /* Finally make a string of ascii characters*/
    for (i=0; i < text_len; i++){
        text[i] = (char)(intervals[i] +97);/*Convert to string*/
    }
    text[text_len] = '\0';
    /*
    printf("Text: %d\n", text_len);
    for(i = 0; i < text_len; i++){
        printf("%c ", text[i]);

    }
    printf("\n");*/
    
    return;
}

int main(int argc, char** argv){
    /* Get the input from stdin*/
    int rc, i;
    int N; /* Song length*/
    int M; /* Snippet length*/
    char *song;
    char *snippet;
    size_t bufsize = 400000;
    song = (char *)malloc(bufsize * sizeof(char));
    snippet = (char *)malloc(bufsize * sizeof(char));

    /* Get N, M from stdin by reading and splitting a line*/
    size_t bsize = 20;
    char *buffer = (char *)malloc(bsize *sizeof(char));
    if ((rc =scanf("%d %d", &N, &M))!= 2){
        return(1);
    }
    while(getchar() != '\n')
        ;

    /*printf("Starting while loop\n");*/
    while((N != 0) &&(M != 0)){
        int song_len = getline(&song, &bufsize, stdin);
        int snippet_len = getline(&snippet, &bufsize, stdin);

        /* Process the song, snippet, and check for a match*/
        /*printf("Converting song& snippet to intervals\n");*/
        /* Convert the sequence of notes into a sequence of intervals*/
        char text[N-1];
        char pattern[M-1];

        intervalize(song, song_len, text, N-1);
        intervalize(snippet, snippet_len, pattern, M-1);


        /* Use fast pattern-matching algorithm to test for match*/
        printf("Searching for a match\n");
        printf("%s\n", text);
        printf("%s\n", pattern);
        int match = kmp_search(pattern, M-1, text, N-1);
        /*printf("back!\n");*/
        if (match==0){
            printf("N\n");
        }
        else{
            printf("S\n");
        }

        
        /* Scan for next input*/
        if ((rc=scanf("%d %d", &N, &M)) != 2){
            printf("Scanf failed to read N, M\n");
            printf("rc = %d\n", rc);
            return(1);
        }
        while(getchar() != '\n')
            ;
    }
    return(0);
}