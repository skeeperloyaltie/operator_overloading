class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition
        
    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    
    def getCondition(self):
        return self.condition
    
    def getApartmentDetails(self):
        return str('(Apartment): Rent: ${}, Distance from UCSB: {}m, condition: {}'.format(self.rent, self.metersFromUCSB, self.condition))
    
    def __lt__(self, rhs):
        if self.rent < rhs.rent:
            return True
        return False

    def __eq__(self, rhs):
        if self.rent > rhs.rent:
            if self.metersFromUCSB == rhs.metersFromUCSB:
                if self.condition == rhs.condition:
                    return True
                return False
            return False
        return True

    # def __gt__(self, rhs):
    #     if self.rent > rhs.rent:
    #         return True
    #     return False
    
    def __gt__(self, rhs):
        if self.rent > rhs.rent:
            return True
        elif self.rent == rhs.rent:
            if self.metersFromUCSB > rhs.metersFromUCSB:
                return True
            elif (self.metersFromUCSB == rhs.metersFromUCSB):
                if (self.condition == "bad" or self.condition == "average" and rhs.condition == "excellent"):
                    return True
            elif (self.condition == "bad" or rhs.condition == "average"):
                    return True
            else:
                return False
        else:
            return False