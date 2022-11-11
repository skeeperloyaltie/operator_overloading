### Instructions
#### three files:
- Apartment.py - file containing a class definition for an Apartment object
- lab06.py - file containing mergesort and other functions defined in the lab06.py section of this lab.
- testFile.py - file containing pytest functions testing the overall correctness of your class definitions

### Apartment.py class
- The Apartment.py file will contain the definition of an Apartment. We will define the Apartment attributes as follows:
    -rent - integer that represents the rent of the Apartment
    - metersFromUCSB - integer that represents the Apartment’s distance, in meters, from UCSB
    - condition - string that represents the condition of the Apartment. This string will be one of three options: "bad", "average", or "excellent".
- You should write a constructor that allows the user to construct an apartment object by passing in values for all of the fields. You may assume that all attributes of the Apartment object will be defined.
- Therefore, there should be no default values for rent, metersFromUCSB, or condition.
__init__(self, rent, metersFromUCSB, condition)
- In addition to your constructor, your class definition should also support “getter” methods that can receive the state of the Apartment object:
    - getRent(self)
    - getMetersFromUCSB(self)
    - getCondition(self)
You will also implement the method
    - getApartmentDetails(self)
        - that returns a str with all of the Apartment attributes. The string should contain all attributes in the following EXACT format (Note: There is no \n character at the end of this string):

        ``` a0 = Apartment(1204, 200, "bad")```<br>
        ``` print(a0.getApartmentDetails())```<br>
        Output<br>
            ``` (Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad```

#### lab06.py
- This file will contain functions that sort a list of Apartment objects, ensures that the list of Apartment objects are in asending order (best-to-worst), retrives information about the best/worst apartments, and gets the info of every affordable apartment in the list. These function defintions as well as their descriptions are provided below. Note that in order for the autograder to correctly check your implementation, function defintions must match exactly.
    - mergesort(apartmentList) - Performs a mergesort on the apartmentList passed as input. Sorts the Apartment objects based on the specifications in the Introduction section of this lab. Gradescope will test to ensure that your mergesort implementation’s Big-O is O(NlogN).
    - ensureSortedAscending(apartmentList) - method that returns a boolean value. True if the apartmentList is sorted correctly in asending order. False otherwise.
    - getBestApartment(apartmentList) - method that returns a string detailing the best Apartment’s rent, meters from UCSB, and condition. Make use of
    - getApartmentDetails(self) and mergesort(apartmentList). You can assume that apartmentList has at least one apartment.
    - getWorstApartment(apartmentList) - method that returns a string detailing the worst Apartment’s rent, meters from UCSB, and condition. Make use of
    - getApartmentDetails(self) and mergesort(apartmentList). You can assume that apartmentList has at least one apartment.
    - getAffordableApartments(apartmentList, budget) - method that returns a labeled, newline separated string detailing the rent, meters from UCSB, and condition of all theapartments whose rent is less than or equal to budget from the apartmentList in sorted order. Make use of getApartmentDetails(self) and mergesort(apartmentList). You can assume that apartmentList has at least one apart


        a0 = Apartment(1115, 215, "bad")
        a1 = Apartment(950, 215, "average")
        a2 = Apartment(950, 215, "excellent")
        a3 = Apartment(950, 190, "excellent")
        a4 = Apartment(900, 190, "excellent")
        a5 = Apartment(500, 250, "bad")
        apartmentList = [a0, a1, a2, a3, a4, a5]
        print('apartmentList is NOT SORTED:')
        for apartment in apartmentList:
        print(apartment.getApartmentDetails())
        assert ensureSortedAscending(apartmentList) == False
        mergesort(apartmentList)
        assert ensureSortedAscending(apartmentList) == True
        print('apartmentList is SORTED:')
        for apartment in apartmentList:
        print(apartment.getApartmentDetails()) ```