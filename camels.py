import sys
import time

def load():
	num_camels = int(next(sys.stdin))
	jaap = next(sys.stdin).strip().split()
	jan = next(sys.stdin).strip().split()
	thijs = next(sys.stdin).strip().split()
	jaap = [int(i) for i in jaap]
	jan = [int(i) for i in jan]
	thijs = [int(i) for i in thijs]
	yield(num_camels, jaap, jan, thijs)

def main1():
	for (num_camels, jaap, jan, thijs) in load():
		sum_camels = 0
		half_camels = int(num_camels/2)
		for i in range(0, num_camels-1):
			for j in range(i+1, num_camels):
				#sys.stdout.write("i:{} j:{}\n".format(i, j))
				a1 = jaap[i]
				a2 = jaap[j]
				b1 = jan.index(a1)
				b2 = jan.index(a2)

				#sys.stdout.write("{} < {} and {} < {} and {} < {}\n\n".format(a1, a2, b1, b2, c1, c2))
				if b1 < b2:
					c1 = thijs.index(a1)
					c2 = thijs.index(a2)
					if c1 < c2:
						sys.stdout.write("{} < {} and {} < {} and {} < {}\n\n".format(i, j, b1, b2, c1, c2))
						sum_camels = sum_camels + 1

				# elif b1 > b2: 
				# 	c1 = thijs.index(a1)
				# 	c2 = thijs.index(a2)
				# 	if c1 > c2:
				# 		sys.stdout.write("{} > {} and {} > {} and {} > {}\n\n".format(i, j, b1, b2, c1, c2))
				# 		sum_camels = sum_camels + 1

		sys.stdout.write("{}\n".format(sum_camels))

# def main2():
# 	for (num_camels, jaap, jan, thijs) in load():
# 		sum_camels = 0




start_time = time.time()
main1()
print("--- %s seconds ---" % (time.time() - start_time))
