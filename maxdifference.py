def maxdifferent(list):
    new_list = []
    for element in range(1, len(list)):
        for value in range(0, element):
            if list[element] - list[value] > 0:
                new_list.append(list[element] -list[value])
    
    if new_list == []:
        return -1
    return max(new_list)
print(maxdifferent([5,4,3,2,1]))
