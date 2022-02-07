# LEEDCODE 3 
# Given a string s, find the length of the longest substring without repeating characters.

#  Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Input: s = ""
# Output: 0

# use two loops one for postion and one for checking and dictionary to check the length.
# idea#

# use two loops
# 1st loop for traversing
# 2nd for checking for every element
# set to store the data.

#  Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

#  using a slicing window.


# keep two pointers i and j where i will only move if we find the repeated elements and j moves faster to search. so we use set to store the data
# if s[j] is not in set we add them on set and increment j but if we find the current element in set, we stope it , find the maximum length and deleter
# the element at i and increment i because we find to check the other subsequence.
def longestsubstringwithoutrepeating(s):
    if s == "":
        return 0
    new_set = set()
    greatest_maximum = 0
    a = 0
    b = 0
    while b < len(s):
        if s[b] not in new_set:
           new_set.add(s[b])
           b += 1
           greatest_maximum = max(len(new_set), greatest_maximum)
        else:
        #    # initially i calculated the greatest_maximum here, but it does not work if the single element comes because the else condition does not work
        #    for the single element and max will never be calculated . so it is better to keep the max condtion in the if condition.
            new_set.remove(s[a])
            a += 1
        print(new_set)
    return greatest_maximum
print(longestsubstringwithoutrepeating("p"))
 
# Time complexity = 0(N)
# Space complexity = O(1)




# #print(longest_substring("a"))

















# Works for both the negative and the positive cases.
def maximumsubarray(list):
    i = 0
    j = 0
    greater = 0
    greatest = -2^32
    # Flag = True
    # for element in list:
    #     if element < 0:
    #         if element > greatest:
    #             greatest = element
    #     else: 
    #         Flag = False
    # #print(Flag)
    # if Flag == True:
    #     return greatest

    
    while i < len(list):

        #print(i)
        if j != len(list) - 1:
            greater += list[j]
            greatest = max(greater, greatest)
            #print(greatest)
            j += 1
            
        else:
            greater += list[j]
            greatest = max(greater, greatest)
            i += 1
            j = i
            greater = 0
    return greatest
            
    # return max(greater, greatest)
print(maximumsubarray([]))


           





