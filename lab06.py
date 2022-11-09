


from Apartment import *



def mergesort(arr, l, r):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0    # Initial index of first subarray
        j = 0    # Initial index of second subarray
        k = l   

        while i < n1 and j < n2:
            if L[i].getRent() <= R[j].getRent():
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)



def ensureSortedAscending(apartmentList):
    if mergesort(apartmentList,0,len(apartmentList)-1) != False:
        return True
    else:
        return  False
   

def getBestApartment(apartmentList):
    if mergesort(apartmentList,0,len(apartmentList)-1) != False:
        return apartmentList[0].getApartmentDetails()
            
            
def getWorstApartment(apartmentList):
    if mergesort(apartmentList,0,len(apartmentList)-1) != False:
        return apartmentList[-1].getApartmentDetails()
                    


def getAffordableApartments(apartmentList, r):
    u = []
    for i, d in enumerate(apartmentList):
        if d.getRent() <= r:
            u.append(d)
    mergesort(u, 0, len(u)-1)
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

assert ensureSortedAscending(apartmentList) == True
print('\n')
mergesort(apartmentList,0,len(apartmentList)-1)
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
assert ensureSortedAscending(apartmentList) == True
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
