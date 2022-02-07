def plusone(list):
    value = []
    result = ''
    for element in list:
        result = result + str(element)
    

    result = str((int(result) + 1))
    print(result)

    
    for element in result:
        value.append(int(element))
    return value
#print(plusone([1,4,4]))

#same method but using map and join function.
def plusone2(list2):
   result =  "".join(map(str, list))
   return int(result) + 1
 
  
def plusone3(list):
    list[len(list)-1] = list[len(list)-1] + 1 #adding 1 to the last number
    for element in range((len(list)-1),0,-1): # using loop and coming from back up to 1st postion - not on 0th postion-0 index
        
        if list[element] != 10: # if we add one and the sum on that index does not become 10, no carry over and we can break the loop.   
            break        
        
        
        list[element] = 0 # if adding one result 10 on that postion, now we make that postion as 0
        list[element - 1] = list[element-1] + 1 # and add 1 to the left number of that postion and the loop works continously.
   

    if list[0] == 10: # now special case- if the first elements becomes 10 then we make it one and add 0 to the end of the list.
        list[0] = 1
        list.append(0)
    return list
#print(plusone3([9,9,9]))

    
def addone(list):
    list[len(list)-1] = list[len(list)-1] + 1
    for element in range(len(list)-1, 0,-1):
        if list[element] != 10:
            break
        else:
            list[element] = 0
            list[element - 1] = list[element - 1] + 1
    if list[0] == 10:
        list[0] = 1
        list.append(0)
    return list
print(addone([1,2]))

#  10 0 0 0 
#  e

# 10 0  0 
#    e
# 1 2 3 4 6

# 1 2 3 4 

# 9 9 9 




















# def reduce(number, k):
#     if len(number) <= k:
#         return number
    
#     i = 0
#     while i < len(number):
#         if 








        




