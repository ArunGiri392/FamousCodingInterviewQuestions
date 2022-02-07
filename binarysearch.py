def binarysearch(list,target):
    value = sorted(list)
    start = 0
    end = len(list)-1
    # count = 0
    count = 0
    while start <= end:
        # print(count)
        middle_value = (start + end)//2
        if value[middle_value] == target:
            return True
        elif value[middle_value] < target:
            start = middle_value + 1
        else:
            end = middle_value - 1
        count += 1
    return False
 
print(binarysearch([1,2,3,4,5,6,7,8],8))



# def most_closest(list,target):
#     value = sorted(list)
#     start = 0
#     end = len(list)-1
#     while start != end:
#         print(value[start])
#         print(value[end])
#         midpoint = (start + end)//2
#         if value[midpoint] < target:
#             start = midpoint
#         else:
#             end = midpoint
#         print(start)
#         print(end)
#     return value[start]
# #print(most_closest([1,0,4,5,6,9],3))

