def removeduplicates(list):
    # so two swaps is not needed only one swap is needed for this problem. since it is sorted we know that which element is unique because if the 
    # element just before the element is same it is not the first unique and if the element just before is different , it means that it is the first 
    # unique and we want to take the element at first or at certain postion.
    i = 1
    j = 1
    while j < len(list):
        # it means that i have found the  first unique element
        if list[j] != list[j-1]:
            list[i] = list[j]
            i += 1
            j += 1
        else:
            j += 1
    return list
  



    

print(removeduplicates([4,1,2,2,1,2,0]))
print(removeduplicates([0,1,2,2,2,4,5]))




def same_order(s):
    list = []
    new_set = {'a','e','i','o','u'}
    for character in s:
        list.append(character)

    start = 0
    end = len(s)-1
    while start < end:
        if list[start] not in new_set:
            start += 1
        if list[end] not in new_set:
            end -= 1
        if list[start] in new_set and list[end] in new_set:
            temp = list[start]
            list[start] = list[end]
            list[end] = temp
            start += 1
            end -= 1
    

    return "".join(list)
# print(same_order('arun giri'))
   
def greatest_sum_neighbours(list):
    max_result = 0
    for row in range(len(list)):
       for col in range(len(list[row])):
            result = 0
            if col + 1 < len(list[row]):
                result += list[row][col + 1]
            if col - 1 >= 0:
                result += list[row][col-1]
            if row + 1 < len(list):
                result +=  list[row + 1][col]
            if row - 1 >= 0:
                result += list[row-1][col]
            print(result)
            max_result = max(result, max_result)

    return max(result, max_result)
        
# print(greatest_sum_neighbours([
# [1, 2, 0], 
# [4, 5, 6], 
# [7, 8, 9]]) )
            # increase_right = list[row][col + 1]
            # inrease_left = list[row][col-1]
            # increase_top = list[row-1][col]
            # decrease_top = list[row + 1][col]

            # if col + 1 <= len(list[row]):
            #     result += increase_right
            # if col - 1 >= 0:
            #     result += inrease_left
            # if row + 1 < len(list):
            #     result +=  decrease_top 
            # if row - 1 >= 0:
            #     result += increase_top

def compressstring(list):
    result = ""
    count = 1
    for element in range(0,len(list)-1):
        if list[element] != list[element + 1]:
            result += list[element] + str(count)
            count = 1
        else:
            count += 1
    result += list[element] + str(count)
    return result
#print(compressstring("aaabcd"))


['a','a','a''b','d']
['a','3','b',"1" "d" "1"]
        
def compression(s):
    result = []
    count = 1
    for element in range(0,len(s)-1):
        if s[element] == s[element + 1]:
            count += 1
        else:
            result.append(s[element])
            result.append(str(count))
            count = 1
    result.append(s[len(s)-1])
    result.append(str(count))

    return "".join(result)
#print(compression("aabbccddeeffgghhiikk"))
# Time complexity = O(N)
# Space compelxity = 

def two_pointers(list):
    i = 1
    j = 1
    while j < len(list):
        if list[j] != list[j-1]:
            list[i] = list[j]
            i += 1
            j += 1
        else:
            j += 1
    print(i)
    if i > len(list):
        print(666)
        return list
    
    j = j - 1
    while j >= i:
        list.pop()
        j -= 1

        #print(list)
    print(55)
    return list
#print(two_pointers([1,2,2,4,4,5]))

             
# 1,2,4,4,4
#     i 
#         j  
#  1,2,3,3,3
#        i 
#          j
# 1,2,3,3,3
#       i 
#       j
#  1 2 3 4 5
#    i 
#    j


def noofwords(string):
    is_space = False
    count = 0
    for element in range(len(string)-1, -1,-1):
        if string[element] != " ":
            is_space = True 
        if string[element] == " "  and is_space == True:
            count += 1
            is_space = False
       
    return count + 1
        

   
#print(noofwords("my name ")


# def number(first_number, second_number):
#     count = 0
#     for number in range(first_number, second_number + 1):
#         while number > 0:
#             remainder = number % 10
#             number = number // 10
#             if remainder == 3:
#                 count += 1
#     return count
# print(number(1,10))
# # 333     335 
# difference + 1  n -- difference

# # number = 334

# N * logm 
# where n is the difference and m is the value of each number.

# # remainder = 4
# # numbefr = 33
# # count = 3


# 1000000

# 6
# log10(100000000)

# 1 2 3
# 4 5 6
# 7 8 9

# 4 3 2 1
# # 8 5 7 6
# # 9 1 8 0

# # row = 1
# # col =  1              0 1              


# # temp = 2
# # list[0][1]


# # 1 2 3 4

# # row = 0
# # col = 2                 0 1 2 3'

# # temp = 2


# def change(list):
#     for row in range(0,len(list)):
#         for col in range(0, (len(list[row])//2)):
#             temp = list[row][col]
#             list[row][col] = list[row][len(list[row])-col-1]
#             list[row][len(list[row])-col-1] = temp
#     return list
# print(change([[1,2,3,4],
# [5,6,7,8],
# [9,10,11,12]]))

# 1 2
# 3 4

# 1 2 3 
# 4 5 6  -- 11  no of rows - odd 3 - 11
# 7 8 9

# 1 2 3 4
# 5 6 7 8 
# 1 2 3 4    no of rows even
# 2 1 1 1    1 6 3 1 4 7 2 2 

# 1 2 3 4 5 
# 6 7 1 2 3 
# 1 2 3 4 6  no of rows odd   5 -22
# 6 7 8 9 1    
# 1 1 1 1 1    1 7 3 9 1 5 2 7 1

# 1+5+9+3+7   
#                                7 -33
#                                9 - 44
#                                11 - 55
# if the length of the row is odd, then i need to subtract
# if lenght is even , i do not need to subtract  --- simple  

# 00 11 22 - left diagnonal 
# 02 11 20  

# row - 0 1 2 

def digonal(list):
    left_diagonal = 0
    right_diagonal = 0
    result = 0
    for row in range(0,len(list)):
        left_diagonal += list[row][row]
        right_diagonal += list[row][len(list)-row-1]
    print(left_diagonal)
    print(right_diagonal)

    result = left_diagonal + right_diagonal
    if len(list) % 2 == 1:
        result -= list[len(list)//2][len(list)//2]
    return result
       
  
# print(digonal([[1,2,3,4],[4,5,6,7],[7,8,9,10],[11,12,13,14]]))


def move_zero(list):
    list1 = []
    list2 = []

    for char in list:
        if char == 0:
            list1.append(char)
    print(list1)
    for char in list:
        if char != 0:
            list2.append(char)
    
    return list1.append(list2)

#print(move_zero[1,0,0,1,2])




