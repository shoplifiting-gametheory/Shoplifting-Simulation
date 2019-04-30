#Supplier = revenue - cost of security
#Security level (% of catching thieves): Low (30%), Medium (60%), High(80%) 

class Supplier:
        
        '''
	Supplier decides how much to spend on security base on the stolen amount and the amount 
	of the retailer paid. 
	Paremeter: how much the retailer paid for security and the amount of thieves stole
	Return: the security level and the profit

	okay- so if more is stolen from retailer security ups security
	which costs money

	alternatively retailer has to buy additional security from firm
	increased stealing means they want more security means they r willing to pay more
	if stolen amount is less than what they are paying for security - lower security
	if stolen amount is greater than what they are paying for security - up security
	if stolen amount is equal to what they are paying for security - leave it
        '''
        
        def strategy(self, stolenAmount):
                
                if stolenAmount > 0:
                        SP = { 30 : (stolenAmount/2),
                               60: ((stolenAmount/3) + (stolenAmount/3)),
                               80: ((5*stolenAmount)/6)}
                else:
                        SP = {30: 30, 60:60, 80:80}
                
                return SP
        


			


	

