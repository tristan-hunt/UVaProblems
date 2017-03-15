import sys


def load():
	while(1):
		next(sys.stdin)
		num_people = int(next(sys.stdin))
		enemies = list()
		for i in range(0, num_people):
			enemies.append(next(sys.stdin).split())
			enemies[i] = [int(x) for x in enemies[i]] 
		yield(num_people, enemies)
	
num_cases = int(next(sys.stdin))
for (n, enem) in load():
	print(n)
	for en in enem:
		print(en)