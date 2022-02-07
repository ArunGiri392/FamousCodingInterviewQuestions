def recursivebinarysearch(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2 
        if list[midpoint] ==target:
            return True
        elif  list[midpoint] < target:
            return recursivebinarysearch(list[midpoint +1 :], target)
        else:
            return recursivebinarysearch(list[ : midpoint], target)

print(recursivebinarysearch([0,1,2,3,4,5,6,7,9],8))











