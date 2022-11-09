
from Apartment import *

def mergeSort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        left = apartmentList[:mid]
        right = apartmentList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              apartmentList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                apartmentList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            apartmentList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            apartmentList[k]=right[j]
            j += 1
            k += 1



def ensureSortedAscending(apartmentList):
    prev = apartmentList[0]
    for cur in apartmentList:
        if cur.getRent() < prev.getRent():
            return False
        prev = cur
    return True

   

def getBestApartment(apartmentList):
    if mergeSort(apartmentList) != False:
        return apartmentList[0].getApartmentDetails()
            
            
def getWorstApartment(apartmentList):
    if mergeSort(apartmentList) != False:
        return apartmentList[-1].getApartmentDetails()
                    


def getAffordableApartments(apartmentList, r):
    u = []
    for i, d in enumerate(apartmentList):
        if d.getRent() <= r:
            u.append(d)
    mergeSort(u)
    return "\n".join([ x.getApartmentDetails() for x in u])
               


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
print('\n')
mergeSort(apartmentList)
assert ensureSortedAscending(apartmentList) == True
print('apartmentList is SORTED:')

for apartment in apartmentList:
    print(apartment.getApartmentDetails())
    
    
a0 = Apartment(1200, 200, "average")
a1 = Apartment(1200, 200, "excellent")
a2 = Apartment(1000, 100, "average")
a3 = Apartment(1000, 215, "excellent")
a4 = Apartment(700, 315, "bad")
a5 = Apartment(800, 250, "excellent")
apartmentList = [a0, a1, a2, a3, a4, a5]
assert ensureSortedAscending(apartmentList) == False
print('\n')
print('Best Apartment in apartmentList:')
print(getBestApartment(apartmentList))
print('Worst Apartment in apartmentList:')
print(getWorstApartment(apartmentList))


a0 = Apartment(1115, 215, "bad")
a1 = Apartment(970, 215, "average")
a2 = Apartment(950, 215, "average")
a3 = Apartment(950, 190, "excellent")
a4 = Apartment(900, 190, "excellent")
a5 = Apartment(500, 250, "bad")
apartmentList = [a0, a1, a2, a3, a4, a5]
print('\n')
print('All apartments whose rent is <= in SORTED order:')
print(getAffordableApartments(apartmentList, 950))