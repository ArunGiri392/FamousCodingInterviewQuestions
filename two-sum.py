
l = [3,2,1,4]
def two_sum(target):
    i = 0
    my_hash = {}
    for elem in range(0,len(list)):
        #print(i)
        diff = target - l[elem]
       
        #print(diff)
        if l[elem] in my_hash:
            return [my_hash[diff],i]
        my_hash[diff] = i
        i += 1
    print(my_hash)
print(two_sum(6))