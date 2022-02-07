def intersect(nums1, nums2):
    list = []
    index = 0
    count = 0
    num1= sorted(nums1)
    num2 = sorted(nums2)
    while index < len(num1) and count < len(num2): # loop will terminate when one of them reaches the end of the list.
        if num1[index] == num2[count]: # checking if the items are equal or not.
            if  index == 0 or num1[index] != num1[index -1]: # checking for repeating. if previously the item has come, again we do not want to write 
                #the same numbers.so due to sorting the numbers are adjacent and if current num is == previous numbers we know it is repeating and
                #we do not want to write that number again but we do not want to check this condition for i = 0 so the condtion is for i = 0.
                list.append(num1[index])
                
            index += 1
            count += 1
            
        elif num1[index ] > num2[count]:
            count += 1
        else:
            index += 1
    return list
print(intersect([1,2,3,3,1], [1,3,3,3,3]))

   
   
    

