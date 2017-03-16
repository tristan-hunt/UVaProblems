import sys

def load():
	num_cases = int(next(sys.stdin))
	for i in range(0, num_cases):
		word = next(sys.stdin).strip()
		yield(word)

for word in load():
	if len(word) == 5:
		sys.stdout.write('3\n')
	

	elif word == 'one' or (word[0] == 'o' and word[1] == 'n') or (word[0] == 'o' and word[2] == 'e') or (word[1] == 'n' and word[2] == 'e'):
		sys.stdout.write("1\n")
	elif word == 'two' or (word[0] == 't' and word[1] == 'w') or (word[0] == 't' and word[2] == 'o') or (word[1] == 'w' and word[2] ==  'o'):
		sys.stdout.write('2\n')
