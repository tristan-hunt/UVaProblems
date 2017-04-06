# /* UVa problem: 355 
#  * Bases Are Loaded
#  * Topic: Arithmetic
#  *
#  * Level: challenging
#  * 
#  * Brief problem description: 
#  *  Given a number in any base, convert it to any other base  
#  *  
#  * Solution Summary:
#  *   Make use of python's int() function to get input from the given   
#  *        base, then convert it to the desired base by dividing
#  *       that base out and keeping track of each remainder. 
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

def load():
    while(1):
        line = next(sys.stdin).split()
        baseFrom = int(line[0])
        baseTo = int(line[1])
        originalStr = line[2]
        yield(baseFrom, baseTo, originalStr)

for (baseFrom, baseTo, originalStr) in load():
    try:
        value = int(originalStr, baseFrom)
    except ValueError:
        sys.stdout.write("{} is an illegal base {} number\n".format(originalStr, baseFrom))
        continue
    
    # convert value to a string in base 'baseTo'
    a = value
    value = ""
    while(a is not 0):
        a, r = divmod(a, baseTo)
        if baseTo > 10 and r > 9:
            r = chr(r+55)
        value = str(r) + value
    if value == "":
        value = 0
    sys.stdout.write("{} base {} = {} base {}\n".format(originalStr, baseFrom, value, baseTo))