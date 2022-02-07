# # Leetcode Merge Intervals -- 56.
# def intervals(list): 
#     final_list = []
#     current_list = list[0]
#     for i in range(1, len(list)):
#         if list[i][0] < current_list[0]:
#             if list[i][1] > current_list[1]:
#                 current_list[1] = list[i][1]
#             current_list[0] = list[i][0]
#         elif list[i][0] >= current_list[0] and list[i][0] <= current_list[1]:
#             if list[i][1] > current_list[1]:
#                 current_list[1] = list[i][1]
    


#         else:
#             final_list.append(current_list)
#             current_list = list[i]
  
#     final_list.append(current_list)
#     return final_list
# print(intervals([[1,3],[2,6],[8,10],[15,18]]))



# merge intervals.


def merge_intervals(list):
    list = sorted(list)
    print(list)
    current_list = list[0]
    i = 1
    end_interval = list[0][1]
    final_list = []
    while i < len(list):
        if list[i][0] <= end_interval:
            end_interval = max(end_interval, list[i][1])
            current_list[1] = end_interval
        else:
            final_list.append(current_list)
            current_list = list[i]
        i += 1
    if current_list != []:
        final_list.append(current_list)
        return final_list
  
    return final_list
print(merge_intervals([[6,7], [2,4], [5,9]]))











# #  0 1 2 3 4 5
# #    *     *
# # *        *
# list = ["my", "name", "is"]
# result = " ".join(list)
# print(result)


# def reversewordsinstring(s):
#     list = []
#     list = s.split()
#     start = 0
#     end = len(list)-1
#     print(list)
#     while start < end:
#         temp = list[start]
#         list[start] = list[end]
#         list[end] = temp
#         start += 1
#         end -= 1
#     print(list)
#     return " ".join(list)
# print(reversewordsinstring("The weather is amazing today!"))



