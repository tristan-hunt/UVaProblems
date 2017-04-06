# /* UVa problem: 291 
#  * Bases Are Loaded
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