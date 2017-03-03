import sys
import re

count = 0
lines = sys.stdin.read().splitlines()

for line in lines:
	if count%2 == 0:
		line = re.sub('"', "``", line, 1)
	else:
		line = re.sub('"', "''", line, 1)
	count = count + 1
	print(line, end = "")