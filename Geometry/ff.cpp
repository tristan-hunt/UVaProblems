// A C++ program to find convex hull of a set of points. Refer
// http://www.geeksforgeeks.org/orientation-3-ordered-points/
// for explanation of orientation()
#include <iostream>
#include <stack>
#include <set>
#include <stdlib.h>
#include <math.h>
#include <boost/foreach.hpp>
using namespace std;

#define foreach BOOST_FOREACH

struct Point
{
    int x, y;
    int v, l;
};


// A globle point needed for  sorting points with reference
// to  the first point Used in compare function of qsort()
Point p0;
 
 

// A utility function to find next to top in a stack
Point nextToTop(stack<Point> &S)
{
    Point p = S.top();
    S.pop();
    Point res = S.top();
    S.push(p);
    return res;
}

// A utility function to swap two points
void swap(Point &p1, Point &p2)
{
    Point temp = p1;
    p1 = p2;
    p2 = temp;
}

// A utility function to return square of distance
// between p1 and p2
int distSq(Point p1, Point p2)
{
    return (p1.x - p2.x)*(p1.x - p2.x) +
          (p1.y - p2.y)*(p1.y - p2.y);
}

// To find orientation of ordered triplet (p, q, r).
// The function returns following values
// 0 --> p, q and r are colinear
// 1 --> Clockwise
// 2 --> Counterclockwise
int orientation(Point p, Point q, Point r){
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0;  // colinear
    return (val > 0)? 1: 2; // clock or counterclock wise
}

// A function used by library function qsort() to sort an array of
// points with respect to the first point
int compare(const void *vp1, const void *vp2) {
   Point *p1 = (Point *)vp1;
   Point *p2 = (Point *)vp2;

   // Find orientation
   int o = orientation(p0, *p1, *p2);
   if (o == 0)
     return (distSq(p0, *p2) >= distSq(p0, *p1))? -1 : 1;

   return (o == 2)? -1: 1;
}

// Prints convex hull of a set of n points.
void convexHull(Point points[], int n, stack<Point> *S, int *len_S){
   // Find the bottommost point
   int ymin = points[0].y, min = 0;
   for (int i = 1; i < n; i++)
   {
     int y = points[i].y;

     // Pick the bottom-most or chose the leftmost point in case of tie
     if ((y < ymin) || (ymin == y &&
         points[i].x < points[min].x))
        ymin = points[i].y, min = i;
   }

   // Place the bottom-most point at first position
   swap(points[0], points[min]);

   // Sort n-1 points with respect to the first point.
   // A point p1 comes before p2 in sorted ouput if p2 has larger polar angle (in counterclockwise direction) than p1
   p0 = points[0];
   qsort(&points[1], n-1, sizeof(Point), compare);

   // If two or more points make same angle with p0, Remove all but the one that is farthest from p0
   // Remember that, in above sorting, our criteria was to keep the farthest point at the end when more than
   // one points have same angle.
   int m = 1; // Initialize size of modified array
   for (int i=1; i<n; i++)
   {
       // Keep removing i while angle of i and i+1 is same
       // with respect to p0
       while (i < n-1 && orientation(p0, points[i],
                                    points[i+1]) == 0)
          i++;


       points[m] = points[i];
       m++;  // Update size of modified array
   }

   // If modified array of points has less than 3 points, convex hull is not possible
   if (m < 3) return;

   // Create an empty stack and push first three points to it.
   S->push(points[0]);
   S->push(points[1]);
   S->push(points[2]);
   *len_S = 3;

   // Process remaining n-3 points
   for (int i = 3; i < m; i++)
   {
      // Keep removing top while the angle formed by
      // points next-to-top, top, and points[i] makes
      // a non-left turn
      while (orientation(nextToTop(*S), S->top(), points[i]) != 2)
         S->pop();
      S->push(points[i]);
      *len_S = *len_S + 1;
   }
}

double euclidDist(Point p1, Point p2){
    double d = sqrt(((p2.x - p1.x)*(p2.x - p1.x)) + ((p2.y-p1.y)*(p2.y-p1.y)));
    return d;
}

double perimeter(int n, stack<Point> S){
    double perim = 0;
    stack<Point> P = S;

    Point first = P.top();
    while (n > 1) {
        Point p = P.top();
        perim = perim + (euclidDist(p, nextToTop(P)));
        P.pop();
        n = n - 1;
    }
    Point p = P.top();
    perim = perim + sqrt(distSq(first, p));
    return perim;
}

void printStack(int n, stack<Point> S){
    stack<Point> P = S;
    // Now H has the output points, we can print them:
    while (!P.empty()) {
        Point p = P.top();
        //Point n = nextToTop(P);
        printf("(%d, %d) ", p.x, p.y);//" (%d, %d)\n", p.x, p.y, n.x, n.y);
        P.pop();
    }printf("\n");
}


// Driver program to test above functions
int main(){
    int rc, i;
    // Get the points, value, length arrays from stdin

    int N;
    rc = scanf("%d", &N); // The number of points
    Point points[N];
    int x, y, v, l;
    for (i=0; i < N; i++){
        rc = scanf("%d %d %d %d", &x, &y, &v, &l);
        points[i] = {x, y, v, l};
    }

    // Set up variables to hold min values
    double min_val;
    stack<Point> min_cut_trees;
    int min_cut_trees_len;
    double min_fence_length;
    double min_hull_length;   

    // Set to hold a subset of points
    int set_size = N;
    stack<Point> cut_trees;
    int cut_trees_len = 0;
    int remaining_trees_len = 0;
    Point set[N];
    int cut_indexes[N];
    for (i = 0; i < N; i++){
        set[i]= points[i];  
    	
    } 


    /* Generate all subsets*/
    unsigned int pow_set_size = pow(2, set_size);
    int counter, j;
 
    /*Run from counter 000..0 to 111..1*/
    for(counter = 0; counter < pow_set_size; counter++){
		/* Generate the subset*/
		for(j = 0; j < set_size; j++) {
			  /* Check if jth bit in the counter is set. If so, add jth element from set */
			  if(counter & (1<<j)){
	              cut_trees.push(set[j]);
	              cut_trees_len  = cut_trees_len + 1;
			  }
        }
       
        /* Code to process subset goes here:*/
		printf("Cut trees: ");
		printStack(cut_trees_len, cut_trees);
		//printf("Remaining trees: ");
		//stack<Point> rem_trees;
		//foreach(Point t, remaining_trees){
		//	rem_trees.push(t);
		//}
		//int rem_trees_len = remaining_trees_len;
        //printStack(rem_trees_len, rem_trees);
       
       /* Find the hull of the remaining trees*/
       
       
       
       /* Find the length of the hull*/
       
       /* Find the perimeter of the cut trees*/
       
       /* If the cut trees are long enough...*/
       
       /* Find the value of the cut trees*/
       
       /* If the value of the cut trees is minimal
       OR equal and the number of cut trees is minimal...*/
       
       /* Set the new min*/
       /* min_cut_trees; min_cut_trees_len; min_fence_length; min_hull_length*/
       
       /* Empty cut_trees for the next guy*/
       while(!cut_trees.empty()){
       		// Pop from cut_trees
       		cut_trees.pop();
       }
       printf("\n\n");
    }

	/* Print the results:*//*
	double extra_wood = min_fence_length-min_hull_length;
	if (forest_num > 1): 
		printf("\n");
	printf("Forest %d\n", forest_num);
	printf("Cut these trees:")
	for (i=0; i<min_cut_trees_len; i++){
		printf(" %d", min_cut_trees[i].i);
	}
	printf("\nExtra wood : %lf{:.2f}\n", extra_wood);
	forest_num = forest_num + 1;
	*/



    // Find the hull of the remaining points
    //int n = sizeof(points)/sizeof(points[0]);
    //stack<Point> H;
    //int H_len;
    //convexHull(points, N, &H, &H_len);
    
    //if (H.empty()){
    //    printf("H is empty:(\n");
    //}

    //printStack(H_len, H);


    // Find the perimeter of the hull
    //double hull_perim = perimeter(H_len, H);
    //printf("Hull perim: %lf\n", hull_perim);
    //stack<Point> C = H; //REMOVE THIS LATER JESUS DONT FORGET
    //int C_len = H_len;
    //int cut_perim = perimeter(C_len, C);

    // Test if size of perim > size hull perim
    //if (hull_perim <= cut_perim){
        // Find the value of the subset


        // Set the new min if val of subset < min subset val
        // OR if they are equal and the amount of trees being cut is less



    //}


    return 0;
}
