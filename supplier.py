#Supplier = revenue - cost of security
#Security level (% of catching thieves): Low (30%), Medium (60%), High(80%) 

class Supplier:
        spoints = 0
        '''
	Supplier decides how much to spend on security base on the stolen amount and the amount 
	of the retailer paid. 
	Paremeter: how much the retailer paid for security and the amount of thieves stole
	Return: the security level and the profit 
        '''
        def strategy(self, revenue, stolenAmount):
                if stolenAmount < 0:
                        return 30, revenue
                elif stolenAmount > revenue:
                        return 80, 0
                elif (stolenAmount/revenue) > 0.8:
                        return 80, revenue - stolenAmount
                elif (stolenAmount/revenue) > 0.6:
                        return 60, revenue - stolenAmount
                else:
                        return 30, revenue - stolenAmount

        def points():
                return spoints
			


	

