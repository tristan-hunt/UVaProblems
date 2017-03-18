# /* UVa problem: 12250
#  * Language Detection
#  * Topic: Other (Straightforward)
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *
#  *   Given an input file with strings "HELLO", "CIAO", "HALLO", "BONJOUR" "HOLA" or "ZDRAVSTVUJTE"
#  *    or another string, output the corresponding language
#  * Solution Summary:
#  *  Use a dict to look up which language the string is from.
#  *  
#  * Used Resources:
#  *
#  * 
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import sys

languageLookup = {'HELLO': 'ENGLISH', 'HALLO': 'GERMAN', 'BONJOUR': 'FRENCH', 'CIAO': 'ITALIAN', 'HOLA': 'SPANISH', 'ZDRAVSTVUJTE': 'RUSSIAN'}


def get_input():
	line = next(sys.stdin).split()
	while(line[0] != '#'):
		yield(line[0])
		line = next(sys.stdin).split()

case = 1
for word in get_input():
	language = languageLookup.get(word, 'UNKNOWN')
	sys.stdout.write("Case "+ str(case) +": " + language+"\n")
	case = case + 1