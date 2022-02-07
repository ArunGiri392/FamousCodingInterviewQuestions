

# find the contiguos subarray whose sum is equal to the given sum

# [1,2,3,4,5,6]   -- target = 12
# naive approach is checking the sum for 1 , 1+2, 1+2+ and so on and again starting from 2 and 2 + 3 and so on.in
# complexity = 0(N^2) because we are using two loops.

# optimal is obtained from 
# from o(n^2) reducing the repeated work. 

# 1,2,3,4,5,6
# two pointers
# add 1 and check if this num is greater than target  
# if not, add 2 and check again and when it become greater, it means this particular subarray does not give the sum. so reduce the first number and we get type_check_only
# the sum for next element after subtracting the first element and so on. 
def contiguossubarray(list,target):
    i = 0 
    j  = 0
    sum = list[i]
    result = []
    for i in range(1,len(list)+1):
        # print("arun")
        # print(i)
        if sum == target:
            #print(True)
            result.append(j)
            result.append(i-1)
            return result
        elif sum < target:
            sum += list[i]
        elif sum > target:
            sum = sum - list[j]
            j += 1
        print(sum)
    return sum == target
   
    
print(contiguossubarray([2,3,5],10))
        




