# Apartment.py

class Apartment:
def __init__(self, rent=0, metersFromUCSB=0, condition="N/A"):
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
return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {""}" \
.format(self.rent, self.metersFromUCSB, self.condition)

def __lt__(self, rhs):
if self.rent < rhs.rent:
return True
elif self.rent == rhs.rent:
if self.metersFromUCSB < rhs.metersFromUCSB:
return True
elif self.metersFromUCSB == rhs.metersFromUCSB:
if (self.condition == "excellent" or self.condition == "average" and rhs.condition == "bad"):
return True
elif (self.condition == "excellent" or rhs.condition == "average"):
return True
else:
return False
else:
return False

def __eq__(self, rhs):
if self.rent == rhs.rent:
if self.metersFromUCSB == rhs.metersFromUCSB:
if self.condition == rhs.condition:
return True
else:
return False

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

Here is lab06.py that I did so far:

# lab06.py
from Apartment import Apartment

def mergesort(apartmentList):
if len(apartmentList) > 1:
mid = len(apartmentList) // 2

lefthalf = apartmentList[:mid]
righthalf = apartmentList[mid:]

mergesort(lefthalf)
mergesort(righthalf)

i = 0
j = 0
k = 0

while i < len(lefthalf) and j < len(righthalf):
if lefthalf[i] <= righthalf[j]:
apartmentList[k] = lefthalf[i]
i = i + 1
else:
apartmentList[k] = righthalf[j]
j = j + 1
k = k + 1

while i < len(lefthalf):
apartmentList[k] = lefthalf[i]
i = i + 1
k = k + 1

while j < len(righthalf):
apartmentList[k] = righthalf[j]
j = j + 1
k = k + 1


def ensureSortedAscending(apartmentList):
for i in apartmentList:
if apartmentList[i + 1] > apartmentList[i]:
return True
else:
return False

def getNthApartment(apartmentList, n):
return str(apartmentList)[n-1]

apartment = 0
for i in range(len(apartmentList):
if apartmentList[i] ==
occur += 1
if len(apartmentList) <
return getApartmentDetails()
else:
return "(Apartment) DNE"


def getTopThreeApartments(apartmentList):
if len(apartmentList) > 1:
mid = len(apartmentList) // 2

lefthalf = apartmentList[:mid]
righthalf = apartmentList[mid:]

mergesort(lefthalf)
mergesort(righthalf)

i = 0
j = 0
k = 0

while i < len(lefthalf) and j < len(righthalf):
if lefthalf[i] <= righthalf[j]:
apartmentList[k] = lefthalf[i]
i = i + 1
else:
apartmentList[k] = righthalf[j]
j = j + 1
k = k + 1

while j < len(righthalf):
apartmentList[k] = righthalf[j]
j = j + 1
k = k + 1

return apartmentList[0:2]
return getApartmentDetails[0:2]