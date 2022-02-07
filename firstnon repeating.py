def firstUniqChar(string):
       for element in range(len(string)):
           print(string[0: element])
           if string[element] not in string[element + 1 :] and  string[element] not in string[0: element]:
               return element
complexity 0(n**2)


           
print (firstUniqChar('aarun'))

def firstuniqchars(string):
    dict = {}
    for element in string:
        if element in dict:
            dict[element] = dict[element] + 1
        
        else:
            dict[element] = 1
        print(dict)
    for element in range(len(string)):
        if dict[string[element]] == 1:
            return element
    return -1
        
print(firstuniqchars("aabb"))
0(n) and 0(1)