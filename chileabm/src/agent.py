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

class Citizen(object):
	""" Tiebout World Citizen """

	def __init__(self, chili, town, mobility=0.5, happy=True):
		""" preference (str), town (str)[, happy=True] """
		self.chili = chili
		self.happy = happy
		self.town_name = town
		self.mobility = mobility

	def __str__(self):
		message = "Citizen likes {} chili, lives in {}, and is ".format(self.chili, self.town_name)
		if self.happy:
			message += "ecstatic "
		else:
			message += "depressed "
		# Add the mobility info
		if self.mobility >= 0.7:
			message += "(loves to move)."
		elif self.mobility <= 0.3:
			message += "(hates to move)."
		else:
			message += "(OK moving)."
		return  message

	def stir_emotions(self,chili_served):
		"""set citizen's happiness based on chili served"""
		if self.chili == chili_served:
			self.happy = True
		else:
			self.happy = False
		print (self)

	def decide_to_move(self):
		"""decide whether to move to the other town"""
		yes = False
		if random.uniform(0,1) <= self.mobility: # how I modified the code to run the expirments
			yes = True
		return yes

	def move(self,from_city,to_city):
		"""move the agent"""
		print ("Agent is moving to",to_city.name)
		from_city.citizens.remove(self) # ... move out
		to_city.citizens.append(self) # ... move in
		self.town_name = to_city.name # new address
		# set happiness
		self.stir_emotions(to_city.chili_served)


