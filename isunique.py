def isunique(string):
    dictionary = {}
    if len(string) > 128: # because unique string cannot have more than 128 characters.
        return False
    for element in string:
        if element not in dictionary:
            dictionary[element] = 1
        else: 
            return False
    return True
print(isunique("aruna"))
# Time complexity = o(N)
# space complexity = 0(128) = 0(n) because whatever we store in the dictionary, we will not store more than 129 characters.




    #There are two types of string. 
    # ASCII - which contains 128 characters and each character is assigned to some ASCII ValueError
    # unicode - They have 140,00 characters on them.Contains all the characters from the world.

#Asking if my string contains only the ASCII or the unicode? --- only ASCII.

