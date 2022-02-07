def arrayadvancegame(list):
    last_index = len(list)-1 # track the last index in the array
    i = 0 # moves through the entire array
    max_reachest = 0 # calcualte the max index we can reach
    while i <= max_reachest and max_reachest < last_index: # if max _reach is smaller than our current index 
        #it implies that we cannot reach end and if our loop should terminate when max_reach becomes greater
        #than the last index which implies we have reached the last index.
        max_reachest = max(max_reachest, list[i]+i) # changes max_reach each times
        i += 1
    print(max_reachest)
    print(last_index)
    if max_reachest >= last_index: # now we check if our max_reach is greater than the last index we say
        # we have reached to the last point of the arary else we did not.
        return True
    return False
#print(arrayadvancegame([1,0,0,0]))
print(arrayadvancegame([3,3,1,0,2,0,1]))
#print(arrayadvancegame([3,2,0,0,2,0,1]))
    
