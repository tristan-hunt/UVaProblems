# /* UVa problem: 756 
#  * Biorythms
#  * Topic: Number Theory
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *	Given a peak of 23, 28 and 33 day cycles, as well as the current day,
#  * state the next time all three peaks will occur at once
#  *
#  * Solution Summary:
#  *	This is a straightforward application of the chinese remainder theorem,
#  *   with x = a (mod 23)
#  *        x = b (mod 28)
#  *        x = c (mod 33)
#  *  x will give the day on which triple-peak occurs (mod 23*28*33).
#  *   Since so much of the problem is given in advance, it is possible to pre-compute
#  *  many of the steps: M = 23*28*33 = 21252
#  *		z1 = M/m1 = m2*m3 = 924
#  *        z2 = 23 * 33 = 759
#  *        z3 = 23 * 28 = 644
#  *   Next, solving for y1, y2, y3 with yizi = 1 mod mi, we get:
#  *     y1 = 6; y2 = 19; y3 = 2
#  *  x = a1*y1*z1 + a2*y2*z2 + a3*y3*z3 (mod 21252)
#  *    To account for amount of days until next cycle, simply subtract d from # of the day  
#  *    on which the triple peak will occur. 
#  *
#  * Used Resources:
#  *
#  *   Textbook: Competitive Programming 3
#  *   Python docs
#  *   Googled various websites for refresher on Chinese Remainder Theorem:
#  * 			http://www.eclasshome.com/attach/upload3/wh_22138672.pdf
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  *
#  * Tristan Hunt
#  */


import sys

m1 = 23
m2 = 28
m3 = 33
M = 21252
z1 = 924
z2 = 759
z3 = 644
y1 = 6
y2 = 19
y3 = 2


def load():
	while(1):
		line = next(sys.stdin).split()
		[a, b, c, d] = [int(i) for i in line]
		if a == -1:
			break
		yield(a, b, c, d)
i = 1
for (a, b, c, d) in load():
	x = a*y1*z1 + b*y2*z2 + c*y3*z3
	x = x%M
	while (x <= d):
		x = x + M
	x = x - d
	sys.stdout.write("Case {}: the next triple peak occurs in {} days.\n".format(i, x))
	i = i + 1

