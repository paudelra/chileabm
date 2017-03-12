

import random
from src.agent import Citizen
from src.space import Town
from src.mode_stats import mode


def model_step(town, rule="MAJORITY"):
	"""choose chili, announce, and stir emotions"""
	if rule == "COIN FLIP":
		choice = town.coin_flip()
	elif rule == "MAJORITY":
		choice = town.select_by_majority()
	town.announce()
	for ag in town.citizens:
		ag.stir_emotions(choice)

# NOTE the change in code organization
# [1] DATA
chili_log = ["red","green","green"]*2
town_names = ["Chiletown","Chilegrod"]
town_log = town_names*3
database = zip(chili_log,town_log)
ticks = 30 # TIME!

# [2] MODEL SETUP
# initialize agents and towns
citizens = []
for chili_color, town in database:
	# let's make the mobility random
	mobility = random.uniform(0.7,1)
	citizens.append(Citizen(chili_color,town,mobility))

townA = Town("Chiletown",citizens)
townB = Town("Chilegrod",citizens)

# [3] MODEL EXECUTION
print ("\nOnce upon a time in towns ",townA.name.upper(),"and",townB.name.upper())
# choose chili, announce, and stir emotions (all in one)
moves = []
for tick in range(ticks):
	move = 0
	print ("\n Year",tick+1)
	model_step(townA)
	model_step(townB)

	# move agents
	for ag in townA.citizens:
		if ag.decide_to_move():
			# an agent stops moving when it is happy
			if ag.happy == False:
				ag.move(townA,townB)
				# the total number of moves per time step
				move += 1
	for ag in townB.citizens:
		if ag.decide_to_move():
			# an agent stops moving when it is happy
			if ag.happy == False:
				ag.move(townB,townA)
				# the total number of moves per time step
				move += 1
	print ('move',move)

# after migration: choose chili, announce, and stir emotions (all in one)
	model_step(townA)
	model_step(townB)
	moves.append(move)
	time = range(1,31)
	summarys = zip(time, moves)

filename = 'mobility.txt'

with open(filename, 'a') as file_object:
	file_object.write(str(moves) + '\n')
print ("Migration log:")
for time, moves in summarys:
	if moves > 0:
		print("\n In year " + str(time) + " , " + str(moves) + " citizens migrated between villages.")
print ("\n All remaining years had no migration")
