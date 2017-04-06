import sys

def load():
    while(1):
        numer = int(next(sys.stdin))
        denom = int(next(sys.stdin))
        yield(numer, denom)

for numer, denom in load():
    sys.stdout.write("{}/{}\n".format(numer, denom))