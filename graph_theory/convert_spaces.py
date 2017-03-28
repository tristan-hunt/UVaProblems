import sys

def load():
	while(1):
		line = next(sys.stdin)
		yield(line)

for line in load():
	edited = ""
	spaces = "" 
	for char in line:
		if char != ' ':
			edited = edited + spaces + char
			spaces = ""
		else:
			spaces = spaces + char
			if len(spaces) == 4:
				spaces = '\t'
	sys.stdout.write(edited)