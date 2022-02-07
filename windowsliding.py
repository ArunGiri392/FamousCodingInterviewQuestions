#https://www.geeksforgeeks.org/window-sliding-technique/

# Given an array of integers of size ‘n’.
# Our aim is to calculate the maximum sum of ‘k’ 
# consecutive elements in the array.

# Input  : arr[] = {100, 200, 300, 400}
#          k = 2
# Output : 700

# Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
#          k = 4 
# Output : 39
# We get maximum sum by adding subarray {4, 2, 10, 23}
# of size 4.
# General approach;

def slicing_window(list,k):
    highest_sum = 0
    current_sum = 0
    count = 0
    for element in range(0,len(list)-k+1):
        current_sum = sum(list[element:k+count])
        highest_sum = max(highest_sum, current_sum)
        count += 1
    return highest_sum
#print(slicing_window([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
# Time complexity = O(n*k) where n is the length of the list and k is the length of the subarray we achieve every time
# .

#approach using Slicing window.

def slicing_window(list,k):
    current_sum = sum(list[0:k])
    highest_sum = current_sum
    for element in range(0, len(list)-k):
        current_sum = current_sum - list[element] + list[element+k]
        highest_sum = max(current_sum, highest_sum)
    return highest_sum
print(slicing_window([1, 4, 2, 10, 23, 3, 1, 0, 20],4))



