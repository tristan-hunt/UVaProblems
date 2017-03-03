import re
import string
from sys import stdin

first_dict = set()	

lines = stdin.read().splitlines()
for line in lines:	
	# Seperate into words
	words = line.rstrip('\n').split(' ')
	for word in words:
		word = re.split('[^a-zA-Z]', word)
		for token in word:
			token = token.lower()	
			first_dict.add(token)
	
andys_dic = sorted(first_dict)
for word in andys_dic:
	print(word)

