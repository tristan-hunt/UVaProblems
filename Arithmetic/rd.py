# /* UVa problem: 202
#  *  Repeating Decimals
#  * Topic: Arithmetic
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *    Given an number in its fraction form.
#  *     describe its decimal form in terms of 
#  *    a repeating fraction. 
#  *   
#  * Solution Summary:
#  *  
#  *
#  * Used Resources:
#  *  
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import sys
import math

def load():
    while(1):
        line = next(sys.stdin).split()
        numer = int(line[0])
        denom = int(line[1])
        yield(numer, denom)

for numer, denom in load():
    dec = "" #build our string as we go!
    hist = list() # to keep track of numers we've seen
    isDec = False
    sys.stdout.write("{}/{} = ".format(numer, denom))

    if numer == 0:
        sys.stdout.write("0.(0)\n   1 = number of digits in repeating cycle\n\n")
        continue

    if (numer < denom):
        numer = numer*10
        dec = "0."
        isDec = True

    while(numer<denom):
        numer = numer*10
        dec = dec + "0"

    # Do one step of the calculations:    
    while(1):
        # Make numer > denom
        while(numer < denom):
                hist.append(numer)
                dec = dec + "0"
                numer = numer*10
        
        # Check if we are in a repeating situation, or done
        if numer in hist:
            break
        if numer == 0:
            break
        if isDec:
            hist.append(numer)

        # Calculate new values for q, bq, numer
        q = math.floor(numer/denom)
        dec = dec + str(q)
        bq = denom * q
        numer = (numer - bq)*10

        if (isDec==False):
            dec = dec+"."
            isDec = True
        if numer == 0:
            break
        isDec = True

    dec = [d for d in dec]

    if numer == 0:
        if isDec == True:
            dec.append("(0)")
        else:
            dec.append(".(0)")
        rep = 1
        sys.stdout.write("{}\n".format("".join(dec)))

    else:
        first = hist.index(numer)
        last = len(hist)
        rep = last - first

        if (isDec == True):
            while (dec[-1] == '0') and (dec[-(rep+1)] == '0'):
                dec.pop()


        #insert parantheses around the repeating part of the fraction:
        dec = [d for d in dec]
        dec.insert(-rep, "(")
        if len(dec) > 53:
            while(len(dec)>53):
                dec.pop()
            dec.append("...)")
            sys.stdout.write("{}\n".format("".join(dec)))

        else:
            dec.append(")")
            sys.stdout.write("{}\n".format("".join(dec)))
    
    sys.stdout.write("   {} = number of digits in repeating cycle\n\n".format(rep))
    

    #Go to next decimal
    