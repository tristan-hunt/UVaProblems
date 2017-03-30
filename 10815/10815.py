import re
import string
import sys

first_dict = set()	
sys.stdin = open("sample-input.txt") # REMOVE BEFORE SUBMITTING

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

