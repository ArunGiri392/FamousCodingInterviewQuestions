#what if you are said reverse that in the string iteslf.else
def reverstring(string):
    result = ""
    for element in string:
        result = element + result
    return result
# Time complexity = 0(N2) -- for loop and adding the element into the result also caused o(N)
# SPACE COMPLEXITY = 0(N)

#convert the string to array, reverse the array and convert the array to the string.
def reversestring(string):
    value = []
    for element in string: 
        value.append(element)

    start = 0
    end = len(value)-1
    while start < end:
        temp = value[start]
        value[start] = value[end]
        value[end] = temp
        start += 1
        end -= 1
    result = ""
    return (result.join(value))
print(reversestring("arungiri"))
 #time complexity of the join function is o(n) so overall time complexity is also o(n). 
 #space complexity is 0(N)
    


#This is with list .
def reverse_string(list):
    start = 0
    end = len(list)-1
    while start < end:
        temp = list[start]
        list[start] = list[end]
        list[end] = temp
        start += 1
        end -= 1
    return list
#print(reverse_string('arun'))

