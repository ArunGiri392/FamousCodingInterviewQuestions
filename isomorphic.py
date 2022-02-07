# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: false

# Input: s = "paper", t = "title"
# Output: true
def isomorphic(s,t):
    if len(s) != len(t):
        return False
    dictionary = {}
    for element in range(0,len(s)):
        dictionary[s[element]] = t[element]
    newset = set()

    for element in dictionary:
        newset.add(dictionary[element])
    print(dictionary)
    print(newset)
    if len(dictionary) != len(newset):
        return False



    for element in range(0,len(s)):
        if dictionary[s[element]] != t[element]:
             return False
    return True


    
#print(isomorphic("badc","baba"))

def isomorphic(s, t):
    for element in range(0, len(s)):
        if len(s) != len(t):
            return False
        value1 = s[element]
        value2 = t[element]
        for value in range(element + 1, len(s)):
            if s[value] == value1:
                if t[value] != value2:
                    return False
            if t[value] == value2:
                if s[value] != value1:
                    return False
    return True
print(isomorphic("paper","title"))
            
                
            
            

