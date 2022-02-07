def removeduplicates(list):
    count = 0
    new_set = set()
    while count < len(list):
        print(new_set)
        print(count)
        
        if list[count] in new_set:
            list.pop(count)

        
        else:
            new_set.add(list[count])
            count += 1
    return list



def removeddDuplicates(list):
        count = 0
        while count < len(list):
            if list[count] in list[count + 1 :]:
                list.remove(list[count])
            else:
                count += 1
        return list
print(removeddDuplicates([0,0,1,1,1,2,2,3,3,4]))

