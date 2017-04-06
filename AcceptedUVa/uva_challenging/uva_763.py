# /* UVa problem: 763
#  * Fibinary
#  * Topic: Arithmetic
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *    Define Fibinary representation of a number, which is a string of 0s and 1s
#  *        which uses the fibonacci numbers as bases instead of powers of 2
#  *    i.e. '10010' represents 2+8 = 10
#  *    Write a program which adds two fibinary numbers
#  *   
#  *
#  * Solution Summary:
#  *    Convert numbers to fibinary by comparing the string 
#  *   to a list of fibonacci numbers, and adding the corresponding
#  *   fibonacci 'digit' when there is a 1. 
#  *   To convert a value back to Fibinary, go backwards through the
#  *    fibonacci array, and subtract from the running value if possible
#  *     and in so doing, add a 1 to the representation. If that fibonacci number
#  *    is too big (but we have already placed significant figures on our string)
#  *     then add a 0 to the representation.
#  *   
#  * 
#  * Used Resources:
#  *
#  * 
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  *
#  *
#  * Tristan Hunt (Your Name)
#  */


import sys

fib = [1,   2,   3,   5,   8,   13,   21,   34,   55,   89,   144,   233,   377,   610,  987,   1597,   2584,   4181,   6765,   10946,   17711,   28657,   46368,   75025,   121393,   196418,   317811,   514229,   832040,   1346269,   2178309,   3524578,   5702887,   9227465,   14930352,   24157817,   39088169,   63245986,   102334155,   165580141,   267914296,   433494437,   701408733,   1134903170,   1836311903,   2971215073, 4807526976, 7778742049,   12586269025]

class Fib:
    def __init__(self, string):
        if string == "":
            string = "0"
        self.string = string
        self.length = len(string)
        if self.length > len(fib):
            while(self.length+10 > len(fib)):
                fib.append(fib[-1]+fib[-2])


        value = 0
        for i in range(0, self.length):
            if self.string[i] == '1':
                value = value + fib[self.length-i-1]
        self.value = value




def load():
    while(1):
        a = next(sys.stdin).strip()
        b = next(sys.stdin).strip()
        yield(a, b)
        next(sys.stdin)


first = 0 
for a, b in load():
    # for i in range(2, len(fib)):
    #     assert(fib[i] == fib[i-1] + fib[i-2])
    if first == 1:
        sys.stdout.write("\n")
    first = 1

    a = Fib(a)
    b = Fib(b)
    c = a.value + b.value
    
    string = ""
    value = a.value + b.value
    maxFib = len(fib)
    l = [maxFib-1-i for i in range(0, maxFib)]
    sig = False
    for i in l:
        if value < fib[i]:
            if (sig):
                string = string + "0"
        else:
            sig = True
            string = string + "1"
            value = value - fib[i]

    c = Fib(string)

    #sys.stdout.write("a:{} = {}\n b:{} = {}\n".format(a.string, a.value, b.string, b.value))
    sys.stdout.write("{}\n".format(c.string))