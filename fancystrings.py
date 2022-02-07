# Leetcode 1957.

# removing an character from a string is always a dangerous because we have to manually handle the index. so 

# Similar to the string compression.
def fancystring(s):
    S = []
    for element in s:
        S.append(element)
    i = 0
    counter = 0
    print(S)

    while i < len(s)-1:
        if s[i] == s[i + 1] and counter == 1:
            S.remove(S[i])

        elif s[i] == s[i + 1]:
            counter += 1
            i += 1
        else:
            counter = 0
            i += 1
    print(S)

    return "".join(S)
#print(fancystring("aaabaaaa"))
# Answer does not match.
# Always a risky approach. 

             
# # a a b a a 
# #         i 
  
#   c = 1


# # c = 0

def fancystring(s):
    list = []
    new_set = set()
    for i in range(0, len(s)):
        print(list)
        if i == 0: 
            list.append(s[i])
            new_set.add(s[i])
        
        elif s[i] in new_set: 
            list.append(s[i])
            new_set.remove(s[i])

        elif s[i] not in new_set and s[i] == s[i-1]:
            continue

        elif s[i] not in new_set:
            list.append(s[i])
            new_set.add(s[i])
        

    return "".join(list)
#print(fancystring("aab"))

# Trying to force the solution to what you know previously can be very very dangerous.
# Wrong approach.

def fancy(s):
    result = []
    count = 0
    element = 0
    while element < len(s)-1:
        if s[element] == s[element + 1] and count == 1:
            result.append(s[element])
            element += 1
            count = 0
        elif s[element] == s[element + 1]:
            result.append(s[element])
            count += 1
       
        elif s[element] != s[element + 1]:
            result.append(s[element])
            count = 0
        element += 1
    return "".join(result)

# print(fancy("aaabaaaa"))
# Could have done but yeah could not analyze.Think carefull.y
# a a a b a a a 

#         e 
# c = 1
# a a b a a  


# checking current element and the previous element and if they are same, incrementing the counter, if they are different , just add them 
# and if they are equal and counter is also one,that means it has occureed more than two times and now i do not want to add it such that i will pass it.
def makeFancyString(self, s):

        count = 0
        i = 1
        list = []
        list.append(s[0])
        while i < len(s):
            if s[i] == s[i-1] and count == 1:
                pass
            elif s[i] == s[i-1]:
                list.append(s[i])
                count += 1
            elif s[i] != s[i-1]:
                list.append(s[i])
                count = 0
            i += 1
        return "".join(list)


    
# a a a b a a 
      
#           i
#   c = 0
# list = [a a b a a ]


# l e e e  t c o d 
#          i 
# c = 1
# [l e e t c o d ]

# a a a a a 
#         i 

#   c = 1
# [a, a, ]

        
            


        