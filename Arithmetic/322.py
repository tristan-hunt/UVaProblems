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
