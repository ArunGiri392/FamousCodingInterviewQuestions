# from typing_extensions import IntVar


# largest to smallest.
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
#  5 - iv 
# 9 - ix

# else:
#     the normal condition applies ie the greater one always comes first.
#     7- vii
#     17- Xvii
#     5 - 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Input: s = "III"
# Output: 3

# Input: s = "IV"
# Output: 4

# Input: s = "IX"
# Output: 9

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

def roman(roman):
    dictionary = {}
    dictionary["I"] = 1
    dictionary["V"] = 5
    dictionary["X"] = 10
    dictionary["L"] = 50
    dictionary["C"] = 100
    dictionary["D"] = 500
    dictionary["M"] = 1000
    dictionary["IX"] = 9
    dictionary["IV"] = 4
    dictionary["XL"] = 40
    dictionary["XC"] = 90
    dictionary["CD"] = 400
    dictionary["CM"] = 900
    result = 0
    element = 0
  
        

    while element <= len(roman)-1:
        if element == len(roman)-1:
            result += dictionary[roman[element]]
            return result
        
        if roman[element] == "I" :
            if roman[element + 1] == "V":
                result += dictionary["IV"]
                element = element + 1
            elif roman[element + 1] == "X":
                result += dictionary["IX"]
                element = element + 1
            else:
                result += dictionary["I"]
            


        elif roman[element] == "X" :
            if roman[element + 1] == "L":
                result += dictionary["XL"]
                element = element + 1
            elif roman[element + 1] == "C":
                result += dictionary["XC"]
                element = element + 1
            else:
                result += dictionary["X"]

        elif roman[element] == "C" :
            if roman[element + 1] == "D":
                    result += dictionary["CD"]
                    element = element + 1
            elif roman[element + 1] == "M":
                    result += dictionary["CM"]
                    element = element + 1
            else:
                result += dictionary["C"]
        else:
             result = result + dictionary[roman[element]]

        element += 1
    return result

#print(roman("MCMXCIV"))
    
# "MCMXCIV" -- 
# result = 1000 + 900 + 90 + 4
def roman(roman):
    #If the current element is greater than the next element, just add them and let the loop go.
    #if the current element is less than the next element, subtract greater from smaller and add them and increase element in total by 2.
    #take care of the edge cases what about the last element, can you compare it with the next element, index error so make sure to check for this case.
    
    dictionary = {}
    dictionary["I"] = 1
    dictionary["V"] = 5
    dictionary["X"] = 10
    dictionary["L"] = 50
    dictionary["C"] = 100
    dictionary["D"] = 500
    dictionary["M"] = 1000

    result = 0
    element = 0
    while element < len(roman):
        if element == len(roman) - 1:
            result += dictionary[roman[element]]
            return result

        if dictionary[roman[element]] >= dictionary[roman[element + 1]] :
            result += dictionary[roman[element]]

        elif dictionary[roman[element]] < dictionary[roman[element + 1]]:
            result = result + (dictionary[roman[element + 1]] - dictionary[roman[element]])
            element += 1
        element += 1
    return result
print(roman("IX"))
        