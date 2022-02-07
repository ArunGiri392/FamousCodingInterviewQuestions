def removezero(list):
    count = 0
    for element in range(len(list)):
        count = 0
        if list[element] != 0:
            list.insert(count, list[element])
            list.pop(element + 1)
            count += 1
    return list




def removezero(list):
    count = 0
    for element in range(0, len(list)):
        if list[element] != 0:
            temp = list[count]
            list[count] = list[element]
            list[element] = temp
            count += 1
    return list
#print(removezero([0,0,0,9,1]))

#what i thought.My thought was absolutely right but the solution was just opposite of mine.Play with the variable.
# I thought if my list[element] finds 0, then my count will increase until i find the non zero number and i would swap between them.
#But the problem with this method was that i could  only increment the count by 1 and for that i needed another loop.

#In the opposite direction.what my loop would work until the list[element]finds non zero and counts keep track of 0 and when that is found swap and increase 
# value of the count. so count would always keep track of 0 element and list[element] would always keep track of number and traverse through array and so on.
        


def removerzero(list):
    i = 0 # i will always search for non zero.
    j = 0 # j will always search for 0

    while i < len(list):
        if list[i] != 0:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            j += 1
        i += 1
    return list
print(removerzero([1,0,0,2,3]))


# [1,2,3,4,5] -- [1,3,5,2,4]

def oddandeven(list):
    # i will always look for the odd number
    #j will always look for the even number
    # and when list[i] is odd, swap them such that even number goes backword.
    i = 0
    j = 0
    while i < len(list):
        if list[i] % 2 == 1:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            j += 1
        i += 1
    return list
print(oddandeven([1,2,3,4,5]))












