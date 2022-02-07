def anagram(first_string, second_string):
    dict1 = {}
    dict2 = {}
    for element in first_string:
        if element in dict1:
             dict1[element] = dict1[element] + 1

        else:
            dict1[element] = 1
    for element in second_string:
        if element in dict2:
             dict2[element] = dict2[element] + 1

        else:
            dict2[element] = 1
    if dict1 == dict2:
        return True
    return False
print(anagram("arun","nura")) 

# Time complexity = 0(n)
# space complexity = O(1) because there are only 26 letters in alphabet.

def anagram2(first_string, second_string):
    dict = {}
    for element in first_string:
        if element in dict:
             dict[element] = dict[element] + 1

        else:
            dict[element] = 1
    for element in second_string:
        if element in dict:
            dict[element] = dict[element] - 1
        else:
            return False
    for element in dict:
        if dict[element] != 0:
            return False
    return True

        
    
# a:1 r:1 u:1 n:1 

