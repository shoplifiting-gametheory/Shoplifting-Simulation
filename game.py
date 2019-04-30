from thief import Thief
from retailer import Retailer
from supplier import Supplier

thief = Thief()
retailer = Retailer()
supplier = Supplier()

nextRound = 50
security = 30
#Suppose the game starts from low security level and stealing $50
i = 0
while i < 10:
        
        stolenAmount, nextRound = thief.steal(nextRound, security)
        securityLevels = supplier.strategy(stolenAmount)
        security = retailer.strategy(stolenAmount, securityLevels, security)
        print(security)
        if stolenAmount < 0:
                print("Thief was caught and paid ${} this round and will steal ${} next round".format(stolenAmount, nextRound))
        else:
                print("Thief stole ${} this round and will steal ${} nextRound".format(stolenAmount, nextRound))
        

        print("Retailer spends ${} on security".format(security))
        print("Security Supplier has profit of (x) and provides {}% level of security".format(security))
        i += 1

'''tpoints = thief.points()
rpoints = retailer.points()
spoints = supplier.points()
print("Thief: ", tpoints)
print("Retailer: ", rpoints)
print("Supplier: ", spoints)'''
