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

/* A debugging function to print the edges of g*/
void display_edges(struct Graph* graph){
	int V = graph->V;
	int E = graph->E;
	printf("Edges:\n");
	int e, source, destination;
	for (e = 0; e < E; ++e){
		source = graph->edge[e].src;
		destination = graph->edge[e].dest;
		printf("Edge %d from %d to %d\n",e, source, destination);
	}

	
}

/* A debugging function to print the vertices of g*/
void display_vertices(struct Graph* graph){
	int V = graph->V;
	int E = graph->E;

}


/* A debugging function to print the graph */
void display(struct Graph* graph){
	int V = graph->V;
	int E = graph->E;
	printf("Graph: V=%d; E=%d\n", V, E);
	display_edges(graph);
	/*display_vertices(graph);*/
}

/* A utility function to find set of an element ii
 * Uses path compression technique
*/
int find(struct subset subsets[], int i){
	/*find root and make root as parent of i (path compression)*/
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



int findLargest( struct Graph* graph){
	int V = graph->V;
	int E = graph->E;
		
	/*Allocate memory from creating V sets*/
	struct subset *subsets = (struct subset*) malloc(V * sizeof(struct subset));

	/* Need to fix this in case graph given is not 0-indexed*/
	int v;
	for (v=0; v< V; ++v){
		subsets[v].parent = v;
		subsets[v].rank = 0;
	}
	
	display(graph);
	
	/* Iterate thrugh all edges connect them*/
	int e, x, y;
	for (e = 0; e < E; e=e+1){
		x = find(subsets, graph->edge[e].src);
		y = find(subsets, graph->edge[e].dest);
		Union(subsets, x, y);
	}
	
	int rank, parent;
	for (v=0; v< V; ++v){
		rank = subsets[v].rank;
		parent = subsets[v].parent;
		printf("v: %d has rank %d and parent %d ", v, rank, parent);
		printf("and has find value: %d", find(subsets, v));
		printf("\n");
	}


	
	return 0;
}


int main(int argc, char** argv){
	int num_cases, m, n;
	int i, j;
	int rc;
	int largest;
	if ((rc = scanf("%d", &num_cases)) != 1){
		fprintf(stderr, "Error reading input: num cases\n");
	}

	/*Get the rest of the input:*/
	i = 0;
	while (i < num_cases){
		if ((rc = scanf("%d %d", &n, &m)) != 2){
			fprintf(stderr, "Error reading input: m, n\n");
		} 
		/* Create the graph with n=num_citizens vertices and m=num_friendships edges*/
		struct Graph* graph = createGraph(n, m);

		int e, a, b;
		for (e = 0; e < m; ++e){
			if((rc = scanf("%d %d", &a, &b)) != 2){
				fprintf(stderr, "Error reading input: a, b\n");
			}
			graph->edge[e].src = a-1;
			graph->edge[e].dest = b-1;
		}
	
		/* Finding Largest Group*/
		largest = findLargest(graph);
		printf("The largest group of friends in g%d is %d\n", i, largest);
		
		printf("\n");
		i = i + 1;
	}

 
    return 0;
}
