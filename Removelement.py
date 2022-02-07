# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# iterate through the list and whenever i encounter the val, remove it and got through end of the list. 0(N^2)
# if i encounter val, stay there with i and j will go to serach non j
# when j reaches to non j , swap them and i goes to another number.
# def remove(list, val):
#     i = 0
#     j = 0
#     while j < len(list):
#         if list[i] != val:
#             i += 1
        
#         if list[j] != val:
#             if list[i] == val and j > i:
#                 temp = list[i]
#                 list[i] = list[j]
#                 list[j] = temp
#                 i += 1
#             else:
#                 j += 1



def remove(list,val):
    count = 0
    while count < len(list):
        if list[count] == val:
            list.remove(list[count])
        else:
            count += 1
    return list
#print(remove([0,1,2,2,3,0,4,2],2))



#Take all the val into the last and at that point my i will be in the last of non val, which is also the length of non val.so return i at that time.
def remove(list, val):
    i = 0
    j = 0
    while j < len(list):
        if list[i] != val and list[j] != val:
            i += 1
            j += 1
        elif list[i] == val and list[j] == val:
            j += 1
        elif list[i] == val and list[j] != val:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            i += 1
            j += 1
        elif list[i] != val and list[j] == val:
            j += 1
    return list


print(remove([1,3,4,5],2))

#Bring all the 1's at first of the list.

# [2,3,1,1] -- [1,1,2,3]

def bringone(list):
    i = 0
    j = 0
    while i < len(list) and j < len(list):
        if list[i] != 1 and list[j] == 1:
            i += 1
            j += 1
        elif list[i] == 1 and list[j] == 1:
            j += 1
        elif list[i] != 1 and list[j] != 1:
            i += 1
        elif list[i] == 1 and list[j] != 1:
            if i > j:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                i += 1
                j += 1
            else:
                i += 1
    return list
#print(bringone([1,1,2,3,4,5,6,71,1]))
   

def movezerobackonefront(list, val = 0):
    i = 0
    j = 0
    while j < len(list):
        if list[i] != val and list[j] != val:
            i += 1
            j += 1
        elif list[i] == val and list[j] == val:
            j += 1
        elif list[i] == val and list[j] != val:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            i += 1
        elif list[i] != val and list[j] == val:
            j += 1
    

    i = 0
    j = 0
    while i < len(list) and j < len(list):
        if list[i] != 1 and list[j] == 1:
            i += 1
            j += 1
        elif list[i] == 1 and list[j] == 1:
            j += 1
        elif list[i] != 1 and list[j] != 1:
            i += 1
        elif list[i] == 1 and list[j] != 1:
            if i > j:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                i += 1
                j += 1
            else:
                i += 1
    return list

#print(movezerobackonefront([1,9,0,0,1,1,1,1,1,3,4,5]))

























    # value = "[{("
    # 1) put all the opening elements in list until we encounter closing.
    # 2) when we get closing check if that and last element from list are same, if not return false. and if equal pop that element.
    # 3) if at certain case, if the length of array is 0 , it means we do not have opening brackets and closing brackets length is more, so return False.
    # 4)

def checker(opening, closing):
    if opening == "(" and closing == ")":
        return True
    elif opening == "[" and closing == "]":
        return True
    if opening == "{" and closing == "}":
        return True
    else:
        return False
    
def brackets(s):
    
    value = "[{("
    list = []
    for element in s:
        if element in value:
            list.append(element)
        else:
            if len(list) == 0:
                #print(5555)
                return False
                
            elif checker(list[len(list)-1], element) == False:
                # print(len(list)-1)
                # print(element)
                # print(list)
               
                return False
            elif checker(list[len(list)-1], element) == True:
                list.pop()
    

    return len(list) == 0
#print(brackets("([)]"))
            
