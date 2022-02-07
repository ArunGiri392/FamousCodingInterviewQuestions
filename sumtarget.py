def sumtarget(list, target):
    dict = {}
    for element, value  in enumerate(list):
        complement = target - value
        if value in dict:
            return [dict[value], element]

        else:
            dict[complement] = element
    # since we iterate through the list n times (if the complement is the last number - we have to iterate the entire list) so the time complexity is O(n) and since we are adding ele
    #elements in the dictionary and again if complement is last in the last we have to add every previous element in the dictionary so space complexity is 0(n)
    # The problem with this method is that the space complexity is O(n) which is bad.
print(sumtarget([3,3],6))
# for understanding.
dict = {}
        for element in range(len(list)):
            complement = target - list[element]
            if list[element] in dict:
                return [dict[list[element]], element]
            else:
                dict[complement] = element
# Assuming the array is sorted, we can do the problem coming from front and back - the start and end process and space complexity becomes o(n).

       
    



 
