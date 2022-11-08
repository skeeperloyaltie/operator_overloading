
from Apartment import *


def mergesort(apartmentList):
    for apartment, f in enumerate(apartmentList):
        
        if apartment > 1:
            mid = len(apartmentList) // 2
            lefthalf = apartmentList[:mid]
            righthalf = apartmentList[mid:]

            mergesort(lefthalf)
            mergesort(righthalf)

            i = 0
            j = 0
            k = 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
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
    if mergesort(apartmentList) == True:
        return True
    else:
        return  False
   

def getBestApartment(apartmentList):
    if mergesort(apartmentList) == True:
        


def getWorstApartment(apartmentList):
    pass


def getAffordableApartments(apartmentList):
    pass




a0=Apartment(1115, 215, "bad")
a1=Apartment(950, 215, "average")
a2=Apartment(950, 215, "excellent")
a3=Apartment(950, 190, "excellent")
a4=Apartment(900, 190, "excellent")
a5=Apartment(500, 250, "bad")

apartmentList=[a0, a1, a2, a3, a4, a5]

print('apartmentList is NOT SORTED:')
for apartment in apartmentList:
    print(apartment.getApartmentDetails())

assert ensureSortedAscending(apartmentList) == False

mergesort(apartmentList)
assert ensureSortedAscending(apartmentList) == False
print('\n')
print('apartmentList is SORTED:')

for apartment in apartmentList:
    print(apartment.getApartmentDetails())
