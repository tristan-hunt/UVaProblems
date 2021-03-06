import sys
import math
from itertools import chain, combinations

 
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "P:({}, {})".format(self.x, self.y)

	def __str__(self):
		return "P:({}, {})".format(self.x, self.y)
		


#def powerSet(soFar, rest):
#	"""
#	soFar, rest currently strings
#	"""
#	if (rest.empty())
#		cout << soFar << endl;
#		
#	else 
#		RecSubsets(soFar + rest[0], rest.substr(1)); // include first char
#		RecSubsets(soFar, rest.substr(1)); // exclude first char
	


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

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
	if (n < 3): return points
		


	hull = list() #list of Points
	l = 0
	for i in range(1, n):
		if (points[i].x < points[l].x):
			l = i
	p = l
	while(1):
		hull.append(points[p]);
 
		q = (p+1)%n
		for i in range(0, n):
			if (orientation(points[p], points[i], points[q]) == 2):
				q = i
		p = q;
		if (p == l): break  # While we don't come to first point
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

def dist(p1, p2):
	"""
	Returns the distance between two points
	"""
	return math.sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y - p2.y)*(p1.y-p2.y))


def poly_perim(points, n=-1):
	"""
	Given a convex hull, finds the length of the perimeter.
	"""
	if n == -1:
		n = len(points)
	if n == 2: 
		return 2*dist(points[0], points[1])
	if n == 1:
		return 0	

	perimeter = 0
	for i in range(0, n-1):
		perimeter = perimeter + dist(points[i], points[i+1])
	perimeter = perimeter + dist(points[0], points[n-1])
	return perimeter


def find_min_subset(n, points, values, lengths):
	"""
	Returns the indexes of the trees that should be cut, 
	as well as the length of the hull given those trees being cut
	"""
	# Try all possible subsets
	min_val = float('inf')
	min_cuts = list() # hold the indexes of minimum cuts
	min_length = float('inf')
	min_hull_length = float('inf')

	tree_powerset_indexes = powerset([i for i in range(0, n)])
	# print("Points: " + str(points))
	# print("Powerset: " + str(tree_powerset_indexes))
	for cut_indexes in list(tree_powerset_indexes):

		cut_trees = [points[i] for i in list(cut_indexes)]
		remaining = list(set(points) - set(cut_trees))	


		
		# See if the convex hull of the remaining trees can be surrounded
		hull = convexHull(remaining, len(remaining))
		if hull != None and len(hull) > 0:
			# Find the length of the hull


			hull_length = poly_perim(hull)

			# Find the length of the perimeter that can be built
			perim = 0
			for i in cut_indexes:
				perim = perim + lengths[i]
			if (perim >= hull_length):

				# Find the value of the subset - minimize it	
				value = 0 
				for i in cut_indexes:
					value = value + values[i]

				if (value < min_val) or (value == min_val and len(cut_indexes) < min_trees):


					#debugging - print:
					#print("Cut i's:" + str(cut_indexes))
					#print("Lengths: " + str(lengths))
					#print("Values: " + str(values))
					#print("Cut trees: " + str(cut_trees))
					#print("Remaining trees: " + str(remaining))
					#print("Hull" + str(hull))
					#print("Hull length: " + str(hull_length))
					#print("Value: " + str(value))
					#print("Perim: " + str(perim))



					min_val = value
					min_cuts = cut_indexes
					min_hull_length = hull_length
					min_trees = len(cut_indexes)
					min_fence_length = perim
					#print("Value is minimal!")
				#print("")

	return min_cuts, min_hull_length, min_fence_length


def load():
    n = int(next(sys.stdin))
    while (n!= 0):
        points = list()
        values = list()
        lengths = list()
        for i in range(0, n):
            line = next(sys.stdin).split()
            point = Point(int(line[0]), int(line[1]))
            values.append(int(line[2]))
            lengths.append(int(line[3]))
            points.append(point)
        yield(n, points, values, lengths)
        n = int(next(sys.stdin))


forest_num = 1
for (n, points, values, lengths) in load():
	
	area = poly_area(points, n)
	hull = convexHull(points, n)
	hull_len = len(hull)
	hull_area = poly_area(hull, hull_len)
	wasted = abs((((area - hull_area)/hull_area))*100)

	cut_trees, hull_length, fence_length = find_min_subset(n, points, values, lengths)	
	
	extra_wood = fence_length-hull_length
	if forest_num > 1: 
		sys.stdout.write("\n")
	sys.stdout.write("Forest {}\n".format(forest_num))
	sys.stdout.write("Cut these trees:")
	for i in cut_trees:
		sys.stdout.write(" {}".format(i+1))
	sys.stdout.write("\nExtra wood : {:.2f}\n".format(extra_wood))
	forest_num += 1




