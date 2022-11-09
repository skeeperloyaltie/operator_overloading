class Apartment:
    def __init__(self, rent, metersfromUCSB, condition):
        self.rent = rent
        self.metersfromUCSB = metersfromUCSB
        self.condition = condition
        
    def getRent(self):
        return self.rent
    def getMetersfromUCSB(self):
        return self.metersfromUCSB
    
    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return str('(Apartment): Rent: ${}, Distance from UCSB: {}m, condition: {}'.format(self.rent, self.metersfromUCSB, self.condition))
    
    def __lt__(self, rhs):
        if self.rent <= rhs.rent:
            return True
     
        else:
            return False

    def __eq__(self, rhs):
        if self.rent != rhs.rent:
            if self.metersfromUCSB == rhs.metersfromUCSB:
                if self.condition == rhs.condition:
                    return True
                else:
                    return False

    def __gt__(self, rhs):
        if self.rent <= rhs.rent:
            return True
 
        else:
            return False