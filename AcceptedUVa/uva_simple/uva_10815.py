# /* UVa problem: 10815
#  * Andy's First Dictionary
#  * Topic: Data Structures
#  *
#  * Level: easy
#  * 
#  * Brief problem description: 
#  *	 Given a string, take all the words present, 
#  *    and sort them (without repetition)
#  *
#  * Solution Summary:
#  *	Use a set to store words to ensure none get repeated
#  *    Then sort.
#  *  
#  *
#  * Used Resources:
#  *	Python docs
#  * 	
#  *
#  * I hereby certify that I have produced the following solution myself
#  * using only the resources listed above in accordance with the CMPUT
#  * 403 collaboration policy.
#  * --------------------- Tristan Hunt
#  */

import re
import string
import sys

first_dict = set()	


lines = sys.stdin.read().splitlines()
for line in lines:	
	# Seperate into words
	words = line.strip('\n').split(' ')
	for word in words:
		word = re.split('[^a-zA-Z]', word)
		for token in word:
			token = token.lower()
			first_dict.add(token)
	
andys_dic = sorted(first_dict)
for word in andys_dic:
	if (len(word)!=0):
		sys.stdout.write("{}\n".format(word))

