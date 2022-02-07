
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step              1  2 ??? i can them in several ways.
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# input n = 4
#  1 1 1 1
#  1 2 1
#  1 1 2
#  2 1 1
#  2  2                              4  1 , 2
# output = 5 - there will be atleast one steps.

# i can only use numbers 1 and 2 and in how many distinct way i can add them to get n.

# 4
#  1* 4 + 2 * 0    --    T
#  1 * 3 + 2 * 0 -- 3 -- f 
#  1 * 2 + 2 * 0 -- 2 -- F 
#  1 * 1 + 2 * 0 -- 1 -- F
#   1 * 0 + 2 * 0 -- 0 -- F
 
# #  1* 4 + 2 * 1 --  6    F
# #  1 * 3 + 2 * 1 -- 5 -- f 
# #  1 * 2 + 2 * 1 -- 4 -- T
# #  1 * 1 + 2 * 1 -- 3 -- F
#  1 * 0 + 2 * 1 -- 2 --   F


#  1* 4 + 2 * 2 --  6    F
#  1 * 3 + 2 * 2 --7 -- f 
#  1 * 2 + 2 * 2 -- 6 -- F
#  1 * 1 + 2 * 2 -- 5 -- F
#  1 * 0 + 2 * 2 -- 4 -- T
def stairs(number):
    count = 0
    if number == 2:
        return 2

    for element in range(0,(number // 2) + 1):
        for value in range(number,-1,-1 ):
            if 1 * value + 2 * element == number:
                count += 1
            if  2 * value + 1 * element == number:
                count += 1
            print ("1 *" + value + "2 * " + element +  " ==" {}.format()1 * value + 2 * element  )
    return count


print(stairs(4))


    # for element in range(0,(number // 2) + 1):
    #     for value in range(number,-1,-1 ):
    #         if  2 * value + 1 * element == number:
    #             count += 1
    # return count

#  2 * 4 + 1 * 0 -- 6    F
#  2 * 3 + 2 * 0 -- 5 -- f 
#  2 * 2 + 2 * 0 -- 4 -- T
#  2 * 1 + 2 * 0 -- 3 -- F

#  2* 4 + 1 * 1 --  9    F
#  2 * 3 + 1 * 1 -- 7 -- f 
#  2 * 2 + 1 * 1 -- 5 -- F
#  2 * 1 + 1 * 1 -- 3 -- F
#  2 * 0 + 1 * 1 -- 1 -- F
 
#  2* 4 + 1 * 2 --  10    F
#  2 * 3 + 1 * 2 -- 8 -- f 
#  2 * 2 + 1 * 2 -- 4 -- T
#  2 * 1 + 1 * 2 -- 4 -- T
#  2 * 0 + 1 * 2 -- 2 -- f








