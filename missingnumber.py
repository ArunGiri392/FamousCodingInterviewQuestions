


def missingnumber(list):
    new_set = set()
 

    for element in list:
        new_set.add(element)

    for element in range(0,len(list)+1):
        if element not in new_set:
            return element
#print(missingnumber([0]))

# using a constant space and time complexity - O(Nlogn)
# sorted them and checked if the difference is 1 or not if not there is some missing elements. also if we complete the loop and everything is fine ,
# it means the missing element is 1 plus the last element. special cases for 0 and 1.
def missingnumber(list):
    if list == [0]:
        return 1
    if list == [1]:
        return 0
    
    value = sorted(list)
    for element in range(1,len(value)):
        if value[0] != 0:
            return 0

        if value[element] - value[element-1] == 1:
            continue
        else:
            return value[element] -1
    return value[element] + 1

# finding the sum of n numbers from n (n+1) //2 same for numbers starting with zero. and finding the sum from our aray and subtracting them to find the m
# missing number.

def missingnumber(list):
    real_sum = (len(list) * ((len(list) + 1))) //2
    our_sum = sum(list)
    return real_sum - our_sum
 
#print(missingnumber([0]))

def squares(list):
    j = 0
    
    # for element in range(0,len(list)):
    #     if list[element] < 0:
    #          j += 1
    while j < len(list) and list[j] < 0:
        j += 1
        
 
    i = j -1
    print(j)
    print(i)

    final_list = []
    # print(i)
    # print(j)
    # if i == j:
    #     for element in range(0, len(list)):
    #          final_list.append(list[element]*list[element])
    #     return final_list
        
    
   


    while j < len(list) and i >= 0:
        if (list[i] * list[i]) <= (list[j] * list[j]):
            final_list.append(list[i] * list[i])
            i -= 1
        else:
            final_list.append(list[j] * list[j])
            j += 1
   
    if i < 0:
        while  j < len(list):
            final_list.append(list[j] * list[j])
            j += 1

    if j >= len(list):
         while i >= 0:
              final_list.append(list[i] * list[i])
              i -= 1
    return final_list
# print(squares([-3,-2,-1,0,1,2,3]))
# print(squares([1,2,3,4]))
# print(squares([-1,-2,-3,-4]))

# i = 0
# j = -1
# [1,2,3,4]
# if 
# print(squares([-1,-2,-3,-4]))



def squares(list):
    start = 0
    end = len(list) - 1
    final_list = []
    while start <= end:
        if abs(list[start]) >= abs(list[end]):
            final_list.append(list[start]* list[start])
            start += 1
        else:
            final_list.append(list[end]* list[end])
            end -= 1
    count = 0
    for i in range(len(list)-1,-1,-1):
        list[count] = final_list[i]
        count += 1
    return list
    # return [: : -1]

# [-2,-1,0,1,2]
#        se
        
# [4,4,1,1,0]

# [1,2,3,4,5]
#  s e 
#  [25,16, 9 ,4,1 ]

#  [-1,-2,-3,-4]
#  s          e 
#  [16, 9,4,1 ]
# print(squares([-2,-1,0,1,2]))
# print(squares([1,2,3,4,5]))
# print(squares([-1,-2,-3,-4,-5]))
# print(squares([-6, -3, -1, 2, 4, 5]))
# print(squares([-5,-4,-2,0,1]))

def flip_the_numbers(nums,threshold):
    start = 0
    end = len(nums)-1
    while start <= end:
        if nums[start] < threshold and nums[end] < threshold:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        elif nums[start] >= threshold:
            start += 1
        elif nums[end] >= threshold:
            end -= 1
    return nums
print(flip_the_numbers([5,12,3,10,4],10))