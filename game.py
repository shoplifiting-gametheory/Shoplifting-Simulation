from thief import Thief
from retailer import Retailer
from supplier import Supplier

thief = Thief()
retailer = Retailer()
supplier = Supplier()

#Suppose the game starts from low security level and stealing $50
i = 0
while i < 10:
	sotelnAmont, nextRound = thief.steal(50, 30)
	security = retailer.strategy(sotelnAmont)
	securityLevel, profit = supplier.strategy(security, sotelnAmont)

	print("Thief stole ${} this round and will steal ${} nextRound".format(sotelnAmont, nextRound))
	print("Retailer spends ${} on security".format(security))
	print("Security Supplier has profit of ${} and provides {}% level of security".format(profit, securityLevel))
	i += 1