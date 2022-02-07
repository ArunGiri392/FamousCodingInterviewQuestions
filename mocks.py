[1,1,2,2] k = 7
[1,1], [2] [2]
# all the numbers should be in k lists.
[ 1,2,3,4,5] k = 2  --- False  
# if k > len(list): return false
a = 4,2
b = 3,1
c = 4,5 
[1,1,1,3,1,2] k = 3 [1,1,1] [3] [1,2] --- True condition

# 


1) in between k lists, there should be all the numbers from original list. 
2) sum of each list should be equal to each other.  

[1,2,3]

[] [1,2,3]
[1] [2,3]
[1,2] [3]
[1,3] [2]


[1,2,3]                    

[] [] [1,2,3]
[] [1] [2,3]
[][1,2] [3]
[] [1,3] [2]
[1][2][3]
[1,2][][3]
[]
