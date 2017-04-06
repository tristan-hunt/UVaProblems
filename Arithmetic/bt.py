# /* UVa problem: 11955
#  *  Binomial Theorem
#  * Topic: Arithmetic
#  *
#  * Level: simple
#  * 
#  * Brief problem description: 
#  *    Given an binomial number, print its
#  *      binomial expansion 
#  *   
#  * Solution Summary:
#  *   Print the binomial expanision as per the formula.   
#  *     Use python's built-in factorial functions. 
#  *
#  * Used Resources:
#  *   http://stackoverflow.com/questions/3025162/statistics-combinations-in-python#  
#  *  
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */


import sys
from math import factorial

def load():
    T = int(next(sys.stdin))
    for i in range(0, T):
        line = next(sys.stdin)
        line = line.split("^")
        k = int(line[1])
        coeff = line[0]
        coeff = coeff.split("+")
        a = coeff[0].strip("(")
        b = coeff[1].strip(")")


        yield(i, a, b, k)

def choose(n, k):
    return factorial(n) // factorial(k) // factorial(n-k)

for i, a, b, n in load():
    sys.stdout.write("Case {}: ".format(i+1))
    if n == 1:
        sys.stdout.write("{}+{}\n".format(a, b))
    elif n == 2:
        sys.stdout.write("{}^2+2*{}*{}+{}^2\n".format(a, a, b, b))
    elif n == 3:
        sys.stdout.write("{}^3+3*{}^2*{}+3*{}*{}^2+{}^3\n".format(a, a, b, a, b, b))
    else: # hold on to your hats, kids....
        
        sys.stdout.write("{}^{}".format(a, n))
        for K in range(1, n):
            k = K
            
            # Calculate coefficient
            coeff = choose(n, k)
            coeff = str(coeff) + "*"

            # Convert n-k, k to strings:
            if n-k > 1:
                nk = "^" + str(n-k)
            elif n-k == 1:
                nk = ""
            
            if k > 1:
                k_str = "^" + str(k)
            elif k == 1:
                k_str = ""

            sys.stdout.write("+{}{}{}*{}{}".format(coeff, a, nk, b, k_str))

        sys.stdout.write("+{}^{}".format(b, n))
        sys.stdout.write("\n")
