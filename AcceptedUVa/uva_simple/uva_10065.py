# /* UVa problem: 10065 
#  * Useless Tile Packers
#  * Topic: Geometry
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *	Given a shape, find the convex hull, then the ratio of the
#  *      area of the shape to the area of the convex hull 
#  * 
#  * Solution Summary:
#  *	Use of gift-wrapping algorithm to find the convex hull   
#  *
#  * Used Resources:
#  *  https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
#  *   http://www.algorithmist.com/index.php/Gift_Wrapping
#  *    http://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
#  * 
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */



import sys
import math


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "P:({}, {})".format(self.x, self.y)

	def __str__(self):
		return "P:({}, {})".format(self.x, self.y)

def orientation(p, q, r):
	"""
	p, q, r are all Points
	To find orientation of ordered triplet (p, q, r).
	The function returns following values
	0 --> p, q and r are colinear
	1 --> Clockwise
	2 --> Counterclockwise
	"""
	val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
	
	if (val == 0): return 0;  # colinear
	if val > 0:
		return 1
	return 2

 
def convexHull(points, n):
	"""
	points - an array of points
	n - length of points
	Prints convex hull of a set of n points.
	"""
	# There must be at least 3 points
	if (n < 3): return None
 
    # Initialize Result
	hull = list() #list of Points
 
    # Find the leftmost point
	l = 0
	for i in range(1, n):
		if (points[i].x < points[l].x):
			l = i
 
    # Start from leftmost point, keep moving counterclockwise
    # until reach the start point again.  This loop runs O(h)
    # times where h is number of points in result or output.
	p = l
	while(1):
    
        # Add current point to result
		hull.append(points[p]);
 
        # Search for a point 'q' such that orientation(p, x,
        # q) is counterclockwise for all points 'x'. The idea
        # is to keep track of last visited most counterclock-
        # wise point in q. If any point 'i' is more counterclock-
        # wise than q, then update q.
		q = (p+1)%n;
		for i in range(0, n):
           # If i is more counterclockwise than current q, then
           # update q
			if (orientation(points[p], points[i], points[q]) == 2):
				q = i

 
        # Now q is the most counterclockwise with respect to p
        # Set p as q for next iteration, so that q is added to
        # result 'hull'
		p = q;
 
		if (p == l): break  # While we don't come to first point
 
    # Print Result
	#for i in range(0, len(hull)):
	#	sys.stdout.write("({}, {}) ".format(hull[i].x, hull[i].y))
	#sys.stdout.write("\n")
	return hull 




def poly_area(points, n=-1):
    """
    Given a polygon (as a list of points), return the area
    """
    if n == -1:
        n = len(points)

    area = 0
    for i in range(0, n-1):
        x1, y1 = points[i].x, points[i].y
        x2, y2 = points[i+1].x, points[i+1].y
        area = area + (x1*y2-y1*x2)

    xn, yn = points[n-1].x, points[n-1].y
    x1, y1 = points[0].x, points[0].y
    area = area + (xn*y1 - yn*x1)
    area = abs(area)/2
    return(area)


def load():
    n = int(next(sys.stdin))
    while (n!= 0):
        points = list()
        for i in range(0, n):
            point = next(sys.stdin).split()
            point = Point(int(point[0]), int(point[1]))
            points.append(point)
        yield(n, points)
        n = int(next(sys.stdin))


i = 1
for (n, points) in load():
	
	area = poly_area(points, n)
	hull = convexHull(points, n)
	hull_len = len(hull)
	hull_area = poly_area(hull, hull_len)
	wasted = abs((((area - hull_area)/hull_area))*100)
	#print(n, points, wasted)
	sys.stdout.write("Tile #{}\nWasted Space = {:.2f} %\n\n".format(i, wasted))
	i = i + 1




