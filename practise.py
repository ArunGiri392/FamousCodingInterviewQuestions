# # # str = “1 4 6 34 200” and int = X, find X.

# # # sorted order.
# # #  “1 4 6 34 200” x - 34 --- True
# # #  “1 4 6 34 200” x - 33 -- False
# # #  “ ”            x - 34        --- False
#       "123456   78910 12345"
#       n is the 3 -- no of count of numbers. 

# # # [1,4,6,34,200]
# # # 1) for loops in list and checking whether that there number is there or not. 
# # # 2) binary search - logn ----


# # # “1 4 6 34 200” 
# # # "Google"

 
# # #  1) binary search
# # #  2) and be aware of the empty spaces.range

# # #  def practise(s,target):

# # #      start = 0
# # #      end = len(s) - 1
# # #      mid = (start + end) //2
# # #      while ----:
# # #         mid = (start + end) //2
# # #          if s[mid] == :
# # #              r
# # # list = ["a","z","A","Z","K"]
# # # print(sorted(list))

# # # Input :  arr[] = {"contribute", "geeks", "ide", "practice"}, x = "ide"
# # # Output :  2
# # # The String x is present at index 2.

# # def binary(list,target):
# #     left = 0
# #     right = len(list) - 1
# #     while left <= right:
# #         mid = (left + right) // 2
# #         if list[mid] == target:
# #             return mid
# #         elif list[mid] > target:
# #             right = mid - 1
# #         else:
# #             left = mid + 1
# #     return -1
# # print(binary("","p"))



   






# [1,2,3,4]
# total_sum = 10
# sum of others except the index = 10 - 1 = 9
# 1,  -- 2,3,4      add second element to index and subtract the next index form 9 ie 
# 1,2 --- 3 ,4
# 1,3 - 2,4
# 1,4 - 2,3

# #1,2,3 -- 4
#  1,2,4 - 3


# 2 ---- 1,3,4
# 2,1 --- 3,4
# # 2,3 - -- 1,4
# # 2,4 --- 1,3
# # # 2,1,3 -- 4
# # # 2,1,4 -- 3





# # # 3 -- 1,2,4
# # # 3,1 --- 2,4
# # # 3,2 --- 1,4
# # # 3,4 -- 1,2

# # # 4 -- 1,2,3
# # # 4,1 -- 3,4
# # # 4,2 --- 1,3
# # # 4,3 -- 1,2

# # # total sum = 10
# # # remaining sum = total sum - list[i]
# # # remaining sum = 10 - 1 = 9
# # # remaining sum = 9 - 2 = 7
# # # remaining sum = 7 - 3 = 4
# # # mysum = 2 ie at index 0
# # # then my sum = 1 + 2 = 3 index 1
# # # my sum = 3 + 3 = 6 index 2
# # # my sum = 



# # # reamining sum = 8

# # # remaining sum = 9 - 2 = 7
# # # remaining sum = 7 - 3 = 4
# # # mysum = 1 ie at index 0
# # # then my sum = 1 + 2 = 3 index 1
# # # my sum = 3 + 3 = 6 index 2
# # # my sum = 

# # def two_numbers(list):
# #     total_sum = sum(list)
# #     for element in range(0,len(list)):
# #         my_sum = list[element]
# #         remaining_sum = total_sum - my_sum
# #         if my_sum == remaining_sum:
# #             return True

# #         for value in range(0,len(list)):
# #             if element != value:
# #                 my_sum = my_sum + list[value]
                
# #                 remaining_sum =  total_sum - list[value]
# #                 if my_sum == remaining_sum:
# #                     return True
# #     return False

# # print(two_numbers(1,2,3,4))

# # total_sum = 10
# # my_sum = 1
# # remaining_sum = 9

# # element = 1
# # value = 0


# # my_sum = 2 + 1 = 3 + 3 = 6
# # remaining_sum = 8 - 1 = 7 - 3 = 4

# def checking(message, magazine):
#     # we cannot make a message whose length is greater than the length of the magazine.Because we are making the message from magazine.
#     if len(magazine) < len(message):
#         return False
#     dictionary = {}
#     #converting all the characters from magazine to dictionary and if any characters are repeated, incrementing their value.
#     for element in magazine:
#         if element in dictionary:
#             dictionary[element] += 1
#         else:
#             dictionary[element] = 1
# #     # iterating through the message and checking the condtions and also decreasing the value of the characters by 1 if they are present in dictionary.
# #     for element in message:
# #         if element not in dictionary or dictionary[element] == 0:
# #             return False
# #         if element in dictionary:
# #             dictionary[element] -= 1
# #     return True
# # # Time complexity = O(M+N) where m is the length of the magazine and n is the length of the message.
# # # Space complexity = O(26) - considering we are only dealing with the 26 lower case letters so it is constant time.
# # print(checking("arungiririeiwioaroiwe","aru"))










        

# # kADANE'S ALGORITHM
# def maximumcontiguossubarray(list):
#     biggest = -2**32
#     count = -1
#     for element in list:
#         if element < 0:
#             if element > biggest:
#                 biggest = element
#         else:
#             count = 1 
#     if count == -1:
#         return biggest 

#     max_so_far = list[0]
#     max_ending_here = 0
     
#     for i in range(0, len(list)):
#         max_ending_here = max_ending_here + list[i]
#         if max_ending_here < 0:
#             max_ending_here = 0
         
#         # Do not compare for all elements. Compare only  
#         # when  max_ending_here > 0
#         elif (max_so_far < max_ending_here):
#             max_so_far = max_ending_here
             
#     return max_so_far
# #print(maximumcontiguossubarray( [-1,-2,-3,4]))

# def compressstring(s):
#     if s == "":
#         return ""
#     result = ""
#     count = 1
#     for element in range(0,len(s)-1):
        
#         if s[element] == s[element + 1]:
#             result = result + s[element]
#             count += 1
#         else:
#             result += s[element] +str(count)
#             count = 1
#     result += s[element] + str(count)
#     return result
# print(compressstring(""))

# def stock(list):
#     minimum_price = list[0]
#     maximum = 0
#     for i in range(1, len(list)):
#         if list[i] > minimum_price:
#             profit = list[i] - minimum_price
#             maximum = max(profit, maximum)
#         else:
#             minimum_price = list[i]
#     return maximum

# #print(stock([7,2,3,1,2]))

# # strings = "my name is arun giri"
# # strings = strings.replace ( " ", "")
# # print(strings)

# # value = sorted(strings)
# # print(value)
    
# # strings = "mynameissandesh"
# # value = sorted(strings)
# # print(value)



# #rint(next_number("1311221"))
# def missingnumber(list):
#     new_set = set()
 

#     for element in list:
#         new_set.add(element)

#     for element in range(0,len(list)+1):
#         if element not in new_set:
#             return element
# #print(missingnumber([0]))

# # using a constant space and time complexity - O(Nlogn)
# # sorted them and checked if the difference is 1 or not if not there is some missing elements. also if we complete the loop and everything is fine ,
# # it means the missing element is 1 plus the last element. special cases for 0 and 1.
# def missingnumber(list):
#     if list == [0]:
#         return 1
#     if list == [1]:
#         return 0
    
#     value = sorted(list)
#     for element in range(1,len(value)):
#         if value[0] != 0:
#             return 0

#         if value[element] - value[element-1] == 1:
#             continue
#         else:
#             return value[element] -1
#     return value[element] + 1


# def missingnumber(list):
#     real_sum = (len(list) * ((len(list) + 1))) //2
#     our_sum = sum(list)
#     return real_sum - our_sum
 
# print(missingnumber([0]))

# def twoarray(list):
#     left_diagonal = 0
#     right_diagonal = 0
#     for i in range(0,len(list)):
#         left_diagonal += list[i][i]
#         right_diagonal += list[i][len(list)-1-i]
#     print(left_diagonal)
#     print(right_diagonal)

# print(twoarray([[1,2,12],[4,8,6],[7,8,9]]))
# # 00 01 02
# # 10 11 12 
# # 20 21 22
# def instantiate_matrix(matrix):
    
#     new_list = []
#     for row in range(0, len(matrix)):
#         list = []
#         for col in range(0, len(matrix[row])):
#             list.append(0)
#         new_list.append(list)

#     return new_list
# #print(instantiate_matrix([[1,2,3,4,5],[4,5,6,6,7],[7,8,9,10,11]]))

# new_list = []
#     for row in range(0, len(matrix)):
#         list = []
#         for col in range(0, len(matrix[row])):
#             list.append(0)
#         new_list.append(list)

        
# def one_shift_operation(matrix):
#     new_list = []
#     for row in range(0, len(matrix)):
#         list = []
#         for col in range(0, len(matrix[row])):
#             list.append(0)
#         new_list.append(list)
   
# #
#     for row in range(0, len(matrix)):
#         for col in range(0 , len(matrix[row])):
#             length_row = len(matrix)
#             length_column =  len(matrix[row])
#             if row == length_row -1 and col == length_column - 1:
#                 new_list[0][0] =  matrix[row-1][col-1]

#             elif col == length_column -1 :
#                 new_list[row + 1][0] =  matrix[row][col]

#             else:
#                 new_list[row][col + 1] =  matrix[row][col]
#     return new_list



# def shift_operation(matrix, k):
#     for i in range(0,k):
#        matrix =  one_shift_operation(matrix)

def sorting(list):
    for element in range(0,len(list)):
        for value in range(element, len(list)):
            if list[value] < list[element]:
                temp = list[element]
                list[element] = list[value]
                list[value] = temp
    return list
print(sorting([5,4,3,2,1]))

