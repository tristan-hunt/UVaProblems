#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* Struct to store information about the entry*/
struct entry{
    int left; /* Stores the right hand edge*/
    int right; /* Stores the left hand edge*/
};


/* Comparison function used by sort() to compare two suffixes*/
/* Compares two pairs - returns 1 if first pair is smaller*/
int cmp(const void * x, const void * y){
    struct entry *i;
    i = (struct entry*)x;
    struct entry *j;
    j = (struct entry*)y;
    struct entry a = *i;
    struct entry b = *j;
    int len_a = a.right - a.left
    int len_b = b.right - b.left
    if (len_a < len_b){
        return 1;
    }
    return 0;
}

int cut(int left, int right, int* coord){
    if (left, right) in memo:
        return memo[(left, right)]

    if left+1 == right:
        memo[(left, right)] = 0
        return 0

    cost = 100001
    term = coord[right] - coord[left]
    for i in range(left+1, right):
        if (left, i) not in memo:
            memo[(left, i)] = cut(left, i, coord)
        if (i, right) not in memo:
            memo[(i, right)] = cut(i, right, coord)
        

        a = memo[(left, i)] + memo[(i, right)] + term
        cost = min(cost, a)
    memo[(left, right)]= cost
    return cost
}

int main(int argc, char** argv){
    int l, n, i;
    while(1){
        scanf("%d", &l); /* length of the stick to be cut*/
        if (l == 0){
            return 0;
        }
        
        scanf("%d", &n); /* the number of cuts to be made*/
        int coord[n];
        for (i=0; i < n; i++){
            scanf("%d", &coord[i]);    
        }

        /* Make the map: std::map <key_type, data_type, [comparison_funtion>*/
        /* Note that by using an entry as a key type, we can use the map like
        an array to access cost. */
        map <(struct entry), int, cmp>
        int cost = cut(0, n+1, coord);
        printf("The minimum cutting is %d.\n",cost)
    }
}