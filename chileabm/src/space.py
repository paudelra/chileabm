"""
Tiebout World: A simple model of social dynamics.

Source: Miller JH, Page SE, (2007), A Tale of Two Cities,
In: Complex Adaptive Systems ,An Introduction to Computational Models
of Social Life Princeton University Press, pp. 17-20


Arika Ligmann-Zielinska

Feb 03, 2016

+ define citizens and create six of them
+ create and populate towns
+ select BY MAJORITY chili served and announce the decision
+ check which citizens are happy
+ for every citizen, make a decision on whether to move based on its mobility
+ -> if True - move the agent from town to town
+ optimize some code
+ modify model step (rule of chile selection)

"""

import random
from mode_stats import mode

class Town(object):
	""" Tiebout Town """

	def __init__(self, name, citizens, chili_served='red'):
		""" name (str), citizens (list) [, chili_served='red'] """
		self.name = name
		self.chili_served = chili_served
		self.citizens = self.select_citizens(citizens)

	def select_citizens(self, citizens):
		""" citizens (list of Citizen objects) """
		my_citizens = []
		for citizen in citizens:
			if citizen.town_name == self.name:
				my_citizens.append(citizen)
		return my_citizens

	def __str__(self):
		return "Town {} has {} citizens.".format(self.name, len(self.citizens))

	def coin_flip(self):
		"""randomly select the chili"""
		flip = random.randint(0,1)
		if flip:
			self.chili_served = 'red'
		else:
			self.chili_served = 'green'
		return self.chili_served

	def select_by_majority(self):
		"""select chili served based on the majority rule"""
		# 1st: retrieve agent preferences
		likes = []
		for ag in self.citizens:
			likes.append(ag.chili)
		# 2nd: select preferences by majority
		self.chili_served = mode(likes)
		return self.chili_served
#
	def announce(self):
		print (self.name,"-> this year we'll serve "+self.chili_served.upper())
