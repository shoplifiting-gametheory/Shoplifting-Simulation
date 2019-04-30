from thief import Thief
from retailer import Retailer
from supplier import Supplier

thief = Thief()
retailer = Retailer()
supplier = Supplier()

#Suppose the game starts from low security level and stealing $50
i = 0
while i < 10:
	stolenAmount, nextRound = thief.steal(50, 30)
	security = retailer.strategy(stolenAmount)
	securityLevel, profit = supplier.strategy(security, stolenAmount)
	if stolenAmount < 0:
                print("Thief was caught and paid ${} this round and will steal ${} next round".format(stolenAmount, nextRound))
        else:
                print("Thief stole ${} this round and will steal ${} nextRound".format(stolenAmount, nextRound))
                

	print("Retailer spends ${} on security".format(security))
	print("Security Supplier has profit of ${} and provides {}% level of security".format(profit, securityLevel))
	i += 1
