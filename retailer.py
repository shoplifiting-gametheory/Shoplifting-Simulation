#Retailer =  Value of items in store - cost of security - the amount stolen by thieves
#Chooses level of security vs profit made off of stuff that was not stolen

class Retailer:
        '''
        Retailer decides the amount to spend on security base on the stolen rate
        parameter: the amount of items that are stolen from thieves
        return: the amount to spend on security, stolen amount * 0.8
        '''
        def strategy(self, stolenAmount, securityLevels, security):
                if stolenAmount > 0:
                        if security == securityLevels.get(30):
                                return securityLevels.get(60)
                        if security == securityLevels.get(60):
                                return securityLevels.get(90)
                return securityLevels.get(30)
