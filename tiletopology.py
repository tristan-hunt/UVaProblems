# 491 - Tile Topology
# Resources: http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
import sys

def get_tilings(n):
	return{
		2: str(1),
		3: str(2),
		4: str(7), 
		5: str(18), 
		6: str(60), 
		7: str(196), 
		8: str(704),
		9: str(2500),
		10: str(9189),
		11: str(33896),
		12: str(126759),
	}.get(n, "1")

def get_input():
	while(1):
		try:
			n = int(next(sys.stdin))
			yield(n)
		except(ValueError):
			break

for n in get_input():
	sys.stdout.write(get_tilings(n)+ "\n")