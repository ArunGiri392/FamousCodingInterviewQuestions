


def selectionsort(list):
    for element in range(len(list)):
        for value in range(element +1, len(list)):
            if list[element] > list[value]:
                temp = list[element]
                list[element] = list[value]
                list[value] = temp
    return list
#print(selectionsort([5,4,3,2,1]))
# split array in Half 
# call Merge sort on each half to sort them recursively
# combine them

def merge_sort(list):
    if len(list) > 1:
        left = list[0:len(list)//2]
        right = list[len(list)//2 :]
        #recursive
        merge_sort(left)
        merge_sort(right)
    #merge step
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
                k += 1
            else:
                list[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            list[k] = left[i]
            i+=1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j+=1
            k += 1
    return list
#print(merge_sort([4,8,1,2,3,6,0,8,5,3]))
        
# Time complexity = 0(N logn)
# Space complexity = 0(N)

        
def searchinsertposition(list, target):
    start = 0
    end = len(list) - 1
    mid = (start + end) //2
    while start < end:
        # print(start)
        # print(end)
        # print(mid)
        mid = (start + end) //2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid - 1
        elif list[mid] < target:
            start = mid + 1
    
    if target > list[start] :
        return start + 1
    return start
#print(searchinsertposition([1],0))
    


def merge( nums1,nums2):
        i = 0
        j = 0
        list = []
        if len(nums1)  == 0:
            return nums2
        if len(nums2)  == 0:
            return nums1
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                list.append(nums1[i])
                i += 1
            else:
                list.append(nums2[j])
                j += 1
        
        while j < len(nums2):
            list.append(nums2[j])
            j += 1
    
        while i < len(nums1):
            list.append(nums1[i])
            i += 1
        return list
#print(merge([-1,2,3,4],[1,2,3]))
# Time complexity = O(m + N) where m is the length of the first array and n is the length of the second list.



def mergesort(list):
    if len(list) > 1:
        left = list[0:len(list)//2]
        right = list[len(list)//2:]
        mergesort(left)
        mergesort(right)
        # merging 
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
                k += 1
            else:
                list[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            list[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            list[k] = right[j]
            k += 1
            j += 1
        return list
print(mergesort([5,4,3,2,1]))

