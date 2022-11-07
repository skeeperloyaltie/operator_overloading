class Apartment:
    def __init__(self, rent, metersfromUCSB, condition):
        self.rent = rent
        self.metersfromUCSB = metersfromUCSB
        self.condition = condition
        
    def getRent(self):
        return self.rent
    def getMetersFromUCSB(self):
        return self.metersfromUCSB
    
    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return str('(Apartment): Rent: ${}, Distance from UCSB: {}m, condition: {}'.format(self.rent, self.metersfromUCSB, self.condition))
    
    