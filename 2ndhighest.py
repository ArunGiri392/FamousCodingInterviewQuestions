def secondhighest(list):
    count = 2
    #Comparing first two numbers and keeping greater as i and second greated as j
    if list[0] < list[1]:
        i = list[1]
        j = list[0]
    else:
        i = list[0]
        j = list[1]
    print(" i am first highest {}".format(i))
    print()
    print(" i am second highest {}".format(j))
    print()
    #since 1st and 2nd is calculated,we can start comparing from 3rd number so count = 2
    while count < len(list):
        # if the highest num is smaller than the other, make other as i and j as previous i.
        if i < list[count]:
            j = i
            i = list[count]
        #if i is greater than other(but that other number is not i) and j is smaller than other, make that other as j
        elif j < list[count] and list[count] != i:
            j = list[count]
        count += 1
    
    if i == j:
        return "There is no number"
        print(" i am first highest {}".format(i))
        print(" i am second highest {}".format(j))
        print()
        print()
    return j
print(secondhighest([5,5,4,3,2,1]))


#Find the Nth highest element
