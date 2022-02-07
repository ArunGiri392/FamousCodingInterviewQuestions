def optimaltaskassignment(list):
    #Each worker should get two tasks.
    
    value = sorted(list) # The idea is to sort the whole array and return the largest and the smallest and so on.
    start = 0
    end = len(list)-1
    while start < end:
        print ("{}     {}".format(value[start], value[end]))
        start += 1
        end -= 1
        
   
print(optimaltaskassignment([2,4,2,6]))