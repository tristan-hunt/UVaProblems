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

    hist = list()
    hist.append(numer)
    if (numer < denom):
        numer = numer*10
        dec = "0."

    while(1):
        q = math.floor(numer/denom)
        dec = dec + str(q)
        bq = denom*q
        
        numer = (numer - bq)*10
        while(numer<denom):
            sys.stdout.write("{} ".format(numer))
            hist.append(numer)
            numer = numer*10
            dec = dec + "0"

        if numer in hist:
            hist.append(numer)
            break
        if numer == 0:
            break
        sys.stdout.write("{} ".format(numer))
        hist.append(numer)


    if numer == 0:
        print("not repeating")
    else:
        print("repeating")