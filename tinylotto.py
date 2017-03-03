# this lotto chooses 3 numbers only.


def read_input():
	line = next(sys.stdin)
	line = [int(x) for x in line.split(" ")]
	while (line[0] != 0):
		yield(line)
		line = next(sys.stdin)
		line = [int(x) for x in line.split(" ")]

for line in read_input():
	k = line[0]
