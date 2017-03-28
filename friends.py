# Task: Count how many people are in the largest group of friends

import sys

class Friend:
	def __init__(self, label):
		self.label = label
		self.friends = list()
		self.visited = 0

	def add_friend(self, friend):
		self.friends.append(friend)
		friend.friends.append(self)

def dfs(f):
	for g in f.friends:
		if g.visited == 0:
			g.visited = 1
			dfs(g)

def load():
	num_cases = int(next(sys.stdin))
	for i in range(num_cases):
		N = int(next(sys.stdin))
		M = int(next(sys.stdin))
		friends = list()
		for j in range(M):
			pair = next(sys.stdin)
			A = Friend(int(pair[0]))
			B = Friend(int(pair[1]))
			A.add_friend(B)
			friends.append(A)
			friends.append(B)
		yield(N, M, friends)

for (N, M, friends) in load():
	# Now we can see what the size of the largest component is:
	num_components = 0
	for f in friends:
		if f.visited == 0
			num_components = num_components + 1
			f.visited = 1
			dfs(f)
	sys.stdout.write("{}\n".format(num_components))		















































































































































































