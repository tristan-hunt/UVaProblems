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