# Call this program by:
# > cat <old.c> | python3 convert_c_comments.py >| <new_file.c>
# for use on linux, or
#
#> python convert_c_comments.py <old.c> > <new_file.c>
# when using windows.
# where <old.c> represents file with // style comments to be replaced by /* */ comments

# Can we make it change for loops, as well?

import sys

if len(sys.argv) > 1:
	sys.stdin = open(sys.argv[1])

for line in sys.stdin:

	pc = False # indicates potential for beginning of comment
	c_idx = -1 # index of start of the comment
	has_comment = False


	floop = False # indicates potential for a for loop
	for_str = "for(int"
	f_idx = 0 # index into for_str 
	f_start = -1;
	has_for = False
	f_var = ' '

	idx = 0

	line = [x for x in line if x != '\n' and x != '\r']
	for char in line:		
		if char == '/':
			if (pc == True):
				has_comment = True
				c_idx = idx
			else:
				pc = True
		else:
			pc = False
		
		if floop and f_var == ' ':
			f_var = char


		if char == for_str[f_idx]:
			f_idx = f_idx + 1
			if f_start == -1:
				f_start = idx
			if (f_idx == len(for_str)):
				floop=True
				f_idx = 0
		else:
			f_idx = 0

		idx=idx+1;


	if (has_comment == True):
		line[c_idx] = '*'
		line.append('*/')

	if (floop == True):
		# write the spaces:
		for s in range(f_start):
			sys.stdout.write(line[s])
		sys.stdout.write("int {};\n".format(f_var))
		line = "".join(line)
		line = line.replace("int ", "")
		line = [x for x in line]

	line = "".join(line)		

	sys.stdout.write("{}\n".format(line))	
