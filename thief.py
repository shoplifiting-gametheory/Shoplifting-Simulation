import random
#Thief: stolen item - cost of being caught
#Percentage of time thief gets caught is based on level of security

class Thief:

	'''
	The thief knows the level of security and decide the amount to steal base on the level.
	If the thief got caught, the thief reduces the amount to steal by 25% for the next round. 
	Otherwise, the thief increases the amount to steal by 25% for the next round.
	Parameter: the item to steal and the level of security
	Return: the profit of the steal and the amount to steal for the next round
	'''
	def steal(self, stolenItem, securityLevel):		
		if random.random() * 100 <= securityLevel: #the thief got caught
			return -3*stolenItem, stolenItem*0.75 
			#stolenItem - 4*stolenItem = -3*stolenItem
		else:
			return stolenItem, stolenItem*1.25
