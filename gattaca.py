import sys

def find_longest_substring(line, full_string):
	length = len(line)
	if len(line) == 1:
		return(len(line), line)
	else:
		res1 = find_longest_substring(line[:1], full_string)
		substring = res1[1]
		length = res1[0]
		if substring in full_string:
			return(len(substring), substring)
		else:

num_cases = int(input())
for i in range(0, num_cases):
	line = input()
	length = find_longest_substring(line, line)[0]
	string = find_longest_substring(line, line)[1]
	print(length, string)

		# substring_length = 0
	# substring = ""
	# for char in line:
		
		# if char can be added to substring:
		# else



