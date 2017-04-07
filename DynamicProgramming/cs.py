import sys
import time

def cut2(n, coord, memo):
	if (n) in memo:
		return memo[n]

	if n == 0:
		memo[n] = 0
		return 0

	if n == 1:
		memo[n] = 0
		return 0

	#Try cutting at all possible spots, pick the min. 
	cost = 100001
	
	# Calculate cost of cutting stick of length n (as an index into coord): 
	print("Cost of cutting at {}:".format(coord[n]))
	for i in range(0, n-1):
		print("Cutting at {} + cutting at {}".format(coord[i], coord[n]))
		a = cut(i, coord, memo) + (coord[n] - coord[i])
		print("Cutting at {} + cutting at {} is {}".format(coord[i], coord[n], a))

		cost = min(a, cost)
	
	print("Min cost at {} is {}".format(coord[n], cost))
	memo[n] = cost
	return cost



def cut(left, right, coord, memo):
	if (left, right) in memo:
		return memo[(left, right)]

	if left == right:
		memo[(left, right)] = 0
		return 0

	if left+1 == right:
		memo[(left, right)] = 0
		return 0

	cost = 100001
	term = coord[right] - coord[left]
	for i in range(left+1, right):
		if (left, i) not in memo:
			memo[(left, i)] = cut(left, i, coord, memo)
		if (i, right) not in memo:
			memo[(i, right)] = cut(i, right, coord, memo)
		

		a = memo[(left, i)] + memo[(i, right)] + term
		cost = min(cost, a)
	memo[(left, right)]= cost
	#sys.stdout.write("Cost of coord[{}] - coord[{}] = {}\n".format(left, right, cost))
	return cost

def load():
	while(1):
		l = int(next(sys.stdin)) # length of the stick to be cut
		if l == 0:
			break
		else:
			n = int(next(sys.stdin)) # the number of cuts to be made
			coord = next(sys.stdin).split()  # an array representing the places the cuts have to be done 
			coord = [int(c) for c in coord]
			coord.insert(0, 0) #Stick starts at 0
			coord.append(l)
			yield(l, n, coord)

start = time.time()
for (l, n, coord) in load():
    print(coord)
    memo = dict()
    # for i in range(1, n+1):
    # 	memo[(0, i)] = cut(0, i, coord, memo)
    
    cost = cut(0, n+1, coord, memo)
    print(memo)
    sys.stdout.write("The minimum cutting is {}.\n".format(cost))
end = time.time()
print(end - start)