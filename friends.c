/* Compile with: -lm -lcrypt -O2 -pipe -ansi -DONLINE_JUDGE 
 * Concepts Used: Union Find
 * Resources Used: http://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
*/
#include <stdio.h>
#include <stdlib.h>

struct Edge{
	int src, dest;
};

struct Graph{
	int V, E;
	struct Edge* edge;
};

struct subset {
	int parent;
	int rank;
};

/* Creates a graph with V vertices and E edges*/
struct Graph* createGraph(int V, int E){
	struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
	graph->V = V;
	graph->E = E;
	graph->edge = (struct Edge*) malloc( graph->E * sizeof( struct Edge));

	return graph;
}

/* A utility function to find set of an element ii
 * Uses path compression technique
*/
int find(struct subset subsets[], int i){
	/*find rot and make root as parent of i (path compression)*/
	if (subsets[i].parent != i)
		subsets[i].parent = find(subsets, subsets[i].parent);

	return subsets[i].parent;
}

/* A funtion that does union of two sets of x and y
 * Uses union by rank
*/
void Union(struct subset subsets[], int x, int y){
	int xroot = find(subsets, x);
	int yroot = find(subsets, y);

	/* Attach smaller rank tree under root of high rank tree
	 * (Union by rank)
	*/
	if (subsets[xroot].rank < subsets[yroot].rank)
		subsets[xroot].parent = yroot;
	else if (subsets[xroot].rank > subsets[yroot].rank)
		subsets[yroot].parent = xroot;

	/*If ranks are same, then makeone as root and increment its rank*/
	else {
		subsets[yroot].parent = xroot;
		subsets[xroot].rank++;
	}
}

/*The main function to check whether a givre graph contains a cycle or not*/
int isCycle( struct Graph* graph){
	int V = graph->V;
	int E = graph->E;

	/*Allocate memory for creating V sets*/
	struct subset *subsets = (struct subset*) malloc(V * sizeof(struct subset));

	int v;
	for (v=0; v< V; ++v){
		subsets[v].parent = v;
		subsets[v].rank = 0;
	}
	/* Iterate thruogh all edges of graph, find sets of both vertices of every edge, if 
	sets are same, then there is cycle in graph */
	int e, x, y;
	for (e = 0; e < E; ++e){
		x = find(subsets, graph->edge[e].src);
		y = find(subsets, graph->edge[e].dest);
	
		if (x == y){
			return 1;
		}

		Union(subsets, x, y);
	}
	return 0;
}


int main(int argc, char** argv){
	int num_cases, m, n, a, b;
	int i, j;
	int rc;
	if ((rc = scanf("%d", &num_cases)) != 1){
		fprintf(stderr, "Error reading input: num cases\n");
	}


	/*Get the rest of the input:*/
	i = 0;
	while (i < num_cases){
		if ((rc = scanf("%d %d", &m, &n)) != 2){
			fprintf(stderr, "Error reading input: m, n\n");
		} 
		while (j < m){
			if((rc = scanf("%d %d", &a, &b)) != 2){
				fprintf(stderr, "Error reading input: a, b\n");
			}

			j = j + 1;
		} 

		i = i + 1;
	}

}