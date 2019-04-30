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
	def steal(self, stolenAmount, securityLevel):		
		if random.random() * 100 <= securityLevel: #the thief got caught
			return -3*stolenAmount, stolenAmount*0.75 
			#stolenAmount - 4*stolenAmount = -3*stolenAmount
		else:
			return stolenAmount, stolenAmount*1.25
