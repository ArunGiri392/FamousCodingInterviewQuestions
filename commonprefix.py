# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings
#  [] --- No empty String
#  [" ", " ", " "] -- only a letter
#  upeercase and lowercase - Yes you need to.
#IDEA

# #USE A FOR LOOP AND GO THROUGH EACH ELEMENT AND CHECK THE FIRST, SECOND AND SO ON. WHEN THEY DOES NOT MATCH, WE KNOW THE LONGEST PREFFIX.
def longestcommonprefix(list):
    result = list[0]
    i = 1
    result = ""
    while i < len(list[0]):
        for value in range(1,len(list)):
            if list[0][0:i] != list[value][0:i]:
                if i == 1:
                     return ""
                else:
                    return result
            #print(result)
            print(list[0][0:i] == list[value][0:i])
        i += 1
        result = list[0][0:i]
    return result
#print(longestcommonprefix(["flower","flow","flight"]))



def common(list):
    value = list[0]
    answer = ""
    for element in range(1,len(value)+1):
        #print(element)
        
        result = value[0:element]
        #print(result)
        for reference in range(1, len(list)):
            if result != list[reference][0:element]:
                if element == 1:
                    return ""
                else:
                    return answer
        answer = value[0:element]
    return answer
print(common((["a","a","a"])))
