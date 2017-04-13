# /* UVa problem: 12577
#  *
#  * Topic: Other
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *	Print one of two strings, depending on input
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

def load():
	line = next(sys.stdin).strip()
	while(line[0] != '*'):
		yield(line)
		line = next(sys.stdin).strip()
case_num = 1
for line in load():
	if line == "Hajj":
		sys.stdout.write("Case {}: Hajj-e-Akbar\n".format(case_num))
	else:
		sys.stdout.write("Case {}: Hajj-e-Asghar\n".format(case_num))
	case_num = case_num + 1
