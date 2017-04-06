# /* UVa problem: 332 
#  * Rational Numbers from Repeating Fractions
#  * Topic: Arithmetic
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *       Given a number as a repeating fraction, 
#  *     Convert it to its fractional form. 
#  *   
#  * Solution Summary:
#  *    Use of the formula provided on the question. 
#  *    Manipulate decimal number as a string rather than multiplying
#  *        by powers of 10 (so as not to risk imprecision with
#  *         floating-point arithmetic)
#  *    
#  * Used Resources:
#  *
#  *   Python docs
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  * Tristan Hunt (Your Name)
#  */

import sys
from fractions import Fraction as F

def load():
    i = 1
    while(1):
        line = next(sys.stdin)
        line = line.split()
        j = int(line[0])
        if j == -1:
            break
        dec = line[1]
        yield(i, j, dec)
        i = i + 1

for i, j, dec in load():
    dec = dec[2:]
    k = len(dec) - j 
    sys.stdout.write("Case {}: ".format(i))
    term1 = "1"
    term2 = "1"
    for i in range(k+j):
        term1 = term1 + "0"
    for i in range(k):
        term2 = term2 + "0"
    if j > 0:     
        denom = int(term1) - int(term2)
    else:
        denom = int(term1)

    if denom == 0:
        denom = 1

    

    numer = int(dec)
    if k > 0 and j > 0:
        term2 = int(dec[:k])
    else:
        term2 = 0
    numer = numer - term2

    f = F(numer, denom)
    sys.stdout.write("{}/{}\n".format(f.numerator, f.denominator))
