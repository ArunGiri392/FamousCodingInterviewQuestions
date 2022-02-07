# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# nput: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# sort the first string, and i will slice the string equivalaent to the length of first string and sort it and compare the first string and the sliceed one.
# if that matches that is true, else continue the loop.
# nlogn
# 0(1)

# pseudocode
# sorting the first string
# using for loop 
# and slicing the string equivalent to length of first string , sorting it and comparting it.
# " " -- " " -- True
# "" -- "avc" -- False
# ASCII- 128 CHARACTERS.
# case sensitive ??




def stringpermutations(first_string, second_string):
    # if first_string == " " and second_string != " ":
    #     return False
    # if second-string == " " and first_string 1= 
    value = sorted(first_string)
    count = 0
    for element in range(0, len(second_string)):  #m-k+1
        if value == sorted(second_string[element:len(first_string)+ count]):
            return True
        count += 1
    return False
#print(stringpermutations("ab","eidboaoo"))

# { a:1, b:1}
# count = 0
# eidboaoo
# c = 1
# 0

# if count len(firststring)
# return true
#  i create dictionary and put elements in it
#  loop through second string and check every elemnt
#  if present, increase count and check count == len(string) if true return True
#  IF NOT PRESET = COUNT = 0
def stringpermutations(first_string, second_string):
    dictionary = {}
    for element in first_string:
        dictionary[element] = 1
    count = 0
    for element in second_string:
        if element in dictionary:
            count += 1
            if count == len(first_string):
                return True
        else:
            count = 0
    return False
# print(stringpermutations("abcd","dabc"))
# wrong approach - what if the input is "abcd" and "aaaaaaaaa" - will not work.else



#Approach using sliding window.
# 1)Making a dictionary and put all the elements from first string 
# 2) Make a second dictionary from the second string from the subarary equal to the length of first string and we can make add or delete from them later.
# 3) Using sliding window. every time delete left hand element and add right most element to make a new subaray - by deleting or adding in dictionary
# and checking if my current dictionary is equal to the first dictionary , if yes true else continue.

def stringpermtations(first_string,second_string):
    #putting all elements from first string to dictionary.
    dictionary1 = {}
    if len(first_string) > len(second_string):
        return False
    for element in first_string:
        if element in dictionary1:
            dictionary1[element] = dictionary1[element] + 1
        else:
            dictionary1[element] = 1
    print(dictionary1)
    #putting elemenets equal to the length o ffirst string from string2 to dictionary.
    dictionary2 = {}
    for element in range(0,len(first_string)):
        if second_string[element] in dictionary2:
            dictionary2[second_string[element]] =   dictionary2[second_string[element]]   + 1
        else:
             dictionary2[second_string[element]] = 1
    


    print(dictionary2)


    
    #for element in range(0,len(second_string)-len(first_string)):
    for element in range(0,len(second_string)-len(first_string)):
        if dictionary1 == dictionary2:
            return True # if at this point , if dictionary1 is equal to dictioanry2 , return 2.
        # for deleting or adding we need to be aware of many cases.
        # For deleting.
        #we delete if only value of  that element is 1, else if it is 2 or 3 , if we delete , d:3 whole will be deleted. so in taht case we just decrease 
        # it by 1
        if dictionary2[second_string[element]] == 1:
                dictionary2.pop(second_string[element])
        else:
            dictionary2[second_string[element]] -= 1

        # also in adding, if there is no that element we set the value of that element as 1. like d:1 but if there is already that element, we cannot
        # set that to one else we need to increase by 1.
        
        if second_string[element + len(first_string)] in dictionary2:
            dictionary2[second_string[element + len(first_string)]] += 1
        else:
            dictionary2[second_string[element + len(first_string)]] = 1
        print(dictionary2)
      
    return dictionary1 == dictionary2
print(stringpermtations('abc',"ccccbbbbaaaa"))

