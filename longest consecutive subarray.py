def consecutive(list):
    value = sorted(list)
    print(value)
    count = 1
    largestvalue = 0
    for element in range(len(list)-1):
        if value[element + 1] == value[element]: # whenever we get the repeated element, we just skip over it.
            # continue function instructs a loop to continue to the next iteration and any code executed below continue statement is not executed for once.
            continue

        if value[element + 1] - value[element] == 1: # if the difference of current element and the next element == 1 increment count
            count += 1
        else:
            largestvalue = max(largestvalue, count) # if not, means we know that the next sequence is started and set the max between current and previous
            # and count to 1 becuase count starts from 1 for the next sequence
            count = 1
    return max(largestvalue, count) # what if the loop completes while the last elements is still in sequence then else does not work and we are not
    #able to compare the count and the largest value so to avoid it, we have again calcualted the max in the end too.
    
#print(consecutive([1,2,2,3,4,5,7,8,9,10]))
# Time complexity - 0(n logn) -- sorting the list
# space complexity - 0(n) -- storing the sorted list somewhere.



def consecutive(list):
    value = set()
    for element in list:
        value.add(element)
    
    

    length = 0
    largest_length = 0
    for element in list:
        if (element -1) not in value:# signifies this is the starting of the new sequence.
            while element in value:
                element += 1
                length += 1
                # print(element)
                # print(length)
            #print("while loop is stopped so update the length")
            #length = 0
            
            largest_length = max(largest_length, length)
            length = 0
            # print(largest_length)
            #print(length)
    return max(largest_length, length)

# element = 11
# length =  4
# highest_length = 5
print(consecutive([1,2,3, 4,5,17,18,19,20,21,22,23,23,23,24,25,26]))

            






# # go through each element and if the next element - current element == 1: they are consecutive,increment count
# # else new subsequence is created and count increase until there is difference greater than 1 and compare previous count  and current count.


# [1,2,3,7,8,9,10,11]

# [0,1,7,8,9,10,11,12]

# count = 5
# largestvalue = 
