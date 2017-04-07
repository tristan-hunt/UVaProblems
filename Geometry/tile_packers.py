#https://en.wikipedia.org/wiki/Gift_wrapping_algorithm

import sys
import math

def poly_area(points, n=-1):
    """
    Given a polygon (as a list of points), return the area
    """
    if n == -1:
        n = len(points)

    area = 0
    for i in range(0, n-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        area = area + (x1*y2-y1*x2)

    xn, yn = points[n-1]
    x1, y1 = points[0]
    area = area + (xn*y1 - yn*x1)
    area = abs(area)/2
    return(area)

def find_angle(line1, line2, p):
    # use the cosine formula to find angle between two points
    # Then compare position of p1, p2 to see if angle is convex or not. 


def find_lefternmost(points, n=-1):
    """
    Given a list of points, return the index of leftermost point
    """
    if n = -1:
        n = len(points)
    left = +inf
    idx = -1
    i = 0

    while(i<n):
        if points[i][0] < left:
            left = points[i][0]
            idx = i

    return i

def left_of(point, seg1, seg2):
    """
    Given a point, and two more points representing the segment between them, 
    return 1 if the point is on the left of the line from seg1 to seg2
    """
    

def gift_wrap(S):
    """
    Given a list of points, return those that belong to the convex hull. 
    """
    # Step 1: Find leftermost point of S
    left_idx = find_lefternmost(S)
    pointOnHull = S[left_idx] #since the lefternmost point must be on the hull
    P = list()

    # Gift-Wrap
    i = 0
    while(1):
        P.append(pointOnHull) 
        endpoint = S[0] #initial endpoint for candidate edge on the hull
        for j in range(1, len(S)):
            if (endpoint == pointOnHull) or (left_of(S[j], P[-1], endpoint)): #if S[j] is left of line from P[i] to endpoint
                endpoint = S[j]
        i = i + 1
        pointOnHull = endpoint
        if endpoint == P[0]:
            break

    return P

def load():
    n = int(next(sys.stdin))
    while (n!= 0):
        points = list()
        for i in range(0, n):
            point = next(sys.stdin).split()
            point = int(point[0]), int(point[1])
            points.append(point)
        yield(n, points)
        n = int(next(sys.stdin))



for (n, points) in load():
    area = poly_area(points, n)
    hull = convex_hull(points)


