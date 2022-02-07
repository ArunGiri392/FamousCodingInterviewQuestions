# #Approach one.
# going through each list and checking in every other list. - 

def Destinationcity(list):
  Flag = True
  for element in range(0,len(list)):
    for value in range(0,len(list)):
      if element != value:
        if list[element][1] not in list[value]:
          Flag = True
        else:
          Flag = False
          break
      #print(list[element][1])
    if Flag == True:
      return list[element][1]
# Time complexity = O(N^2)
# Space complexity = O(1)

# Approach 2.
# Using dictionary 



# Destination city.
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 

# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"

# idea#
# The city that does not start on have a relation with city for going is a destinatiokn.
# if the particular city is not the first city of other list, then it is a destination.

# 0(N2) -- going to the last index of list and checking if that element is present on oterh list[0] or not, if not it is the final destination.
# {london:Newyork,: {london, newyork, lima}
# {b,D,C}

# PSEUDOCODE
# 1) ITERATE AND KEEP THE FIRST ITEM OF LIST IN THE DICTIONARY.hash
# 2) ITERATE ON DICTIONARY AND JUST CHECK IF 2ND ELEMENT IS THERE OR NOT.


def destCity(self, list):
        dictionary = {}
        for element in range(0,len(list)):
            dictionary[list[element][0]] = 1
            
        for element in range(0,len(list)):
            if list[element][1] not in dictionary:
                return list[element][1]
# Time complexity = O(N)
# Space complexity = 0(1)



