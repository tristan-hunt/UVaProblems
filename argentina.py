# Problem #11804
# Maximize abilities of attacking, defending players

import sys

class Player:
	def __init__(self, name, attack, defense):
		self.name = name
		self.attack = attack
		self.defense = defense
	def __lt__(self, other):
		return self.name < other.name

	def __repr__(self):
		return(self.name)

	def __str__(self):
		return(self.name)

def find_defenders(players, attackers):
	defenders = list()
	for player in players:
		if player not in attackers:
			defenders.append(player)
	return(defenders)

def find_positions(players):
	players = sorted(list(players))
	attackers = list()
	defenders = list()

	max_attack = 0
	for i in range(0, 6):
		for j in range(i+1, 7):
			for k in range(j+1, 8):
				for l in range(k+1, 9):
					for m in range(l+1, 10):
						total_attack = players[i].attack + players[j].attack +players[k].attack +players[l].attack +players[m].attack  
						if total_attack > max_attack:
							max_attack = total_attack
							attackers = (players[i],players[j],players[k],players[l],players[m])  
	
	defenders = find_defenders(players, attackers)
	return(attackers, defenders)



def load_input():
	players = set()
	k = int(next(sys.stdin))
	for i in range(0, k):
		for j in range(0, 10):
			player_info = next(sys.stdin).split()
			players.add(Player(player_info[0], int(player_info[1]), int(player_info[2])))
		yield(players)

k = 1
for players in load_input():
	sys.stdout.write("Case " + str(k) + ": \n" )
	(attackers, defenders) = find_positions(players)

	sys.stdout.write("(")
	for i in range(0, 5):
		sys.stdout.write(attackers[i].name)
		if i != 4:
			sys.stdout.write(", ")
	sys.stdout.write(")\n(")

	for i in range(0, 5):
		sys.stdout.write(defenders[i].name)
		if i != 4:
			sys.stdout.write(", ")
	sys.stdout.write(")\n")
	k = k + 1