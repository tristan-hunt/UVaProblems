# /* UVa problem: 11498
#  * Division of Nlogonia
#  * Topic: Other (Straightforward)
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *
#  *   Given a center coordinate, determine if each following coordinate is
#  *    northwest, northeast, southwest, or southeast from the coordinate.
#  * Solution Summary:
#  *  Use many conditionals to check which quadrant the coordinate is in. 
#  *  
#  * Used Resources:
#  *
#  * 
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */


import sys

def get_input():
	k = int(next(sys.stdin))
	while (k != 0):
		coords = next(sys.stdin).split()
		(n, m) = int(coords[0]), int(coords[1])
		for i in range(0, k):
			res = next(sys.stdin).split()
			(x, y) = int(res[0]), int(res[1])
			yield (n, m, x, y)
		
		k = int(next(sys.stdin))

for (n, m, x, y) in get_input():
	if (x > n) and (y > m):
		sys.stdout.write("NE\n")
	elif (x > n) and (y < m):
		sys.stdout.write("SE\n")
	elif (x < n) and (y > m):
		sys.stdout.write("NO\n")
	elif (x < n) and (y < m):
		sys.stdout.write("SO\n")
	else:
		sys.stdout.write("divisa\n")


