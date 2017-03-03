import logging

logging.basicConfig(filename='410_log_file.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('\n\n----------------------------------------------------')
logging.debug('Starting computation\n----------------------------------------------------')

import sys


def load():
	while(1):
		try:
			line = next(sys.stdin).split(" ")
			c = int(line[0])
			s = int(line[1])
			weights = next(sys.stdin)

			weights = [int(x) for x in weights.split(" ")]

			yield(c, s, weights)
		except ValueError:
			break
		except IndexError:
			break

case = 1
for (c, s, weights) in load():


	# Step 1: add 0s to make len(weights) == 2*c
	c2 = c * 2
	while(len(weights) < c2):
		weights.append(0)

	# Step 2: sort weights
	weights.sort() # is sort in-place?

	# Step 3: Print
	sys.stdout.write("Set #{}\n".format(case))
	balance = list()
	for chamber in range(0, c):
		sys.stdout.write(" {}:".format(chamber))

		if weights[chamber] != 0:
			sys.stdout.write(" {}".format(weights[chamber]))
		if weights[-(chamber+1)] != 0:
			sys.stdout.write(" {}".format(weights[-(chamber+1)]))
		sys.stdout.write("\n")

		balance.append(weights[chamber] + weights[-(chamber+1)])

	avg = (sum(balance))/(c)
	imbalance = sum([abs(x-avg) for x in balance])	
	sys.stdout.write("IMBALANCE = {:.5f}\n\n".format(imbalance))	

	case = case+1