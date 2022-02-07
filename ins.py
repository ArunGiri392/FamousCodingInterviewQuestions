# def interection(list1, list2): 
#     dictionary = {} 
#     list = [] 
#     for element in list1:
#         if element in dictionary:
#             dictionary[element] += 1

#         else:
#             dictionary[element] = 1 

 
#     for element in list2:
#         if element in dictionary and dictionary[element] !=0 :
            
#             list.append(element)
#             dictionary[element] -= 1 
#     print(list)
   

#     new_set = set()
#     for element in list:
#         if element not in new_set:
#             new_set.add(element)
#     print(new_set)
#     final_list = []

#     for element in new_set:
#         print(element)
#         final_list.append(element)
#     print(final_list)
    
#     return final_list

        
# print(interection([1,2,2,1],[2,2]))


    
def intersection(list1, list2):
    list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j] :
            if list1[i] != list1[i-1] or i == 0:
                list.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return list
print(intersection([1,2,2,1],[2,2]))

        
