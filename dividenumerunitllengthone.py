# 12345 --- 15 --- 6
# 1234 --- 10 -- 1

# concept is to use two while loops.
# do first loop until the length becomes one ie number less than 9 has a length 1 so it should be greater than 9.
# second for dividing and adding each time.




def divide(number):
    result = 0
    
   
    

    while result > 9 or result == 0: # for the length to become greater than 1.
    
        result = 0

        while number > 0: # for the quotiend
            remainder = number % 10
            result += remainder
            number = number // 10
        number = result
    return result
#print(divide(1345))
#123456

# Constant time solution.


# 123456

# 9 18 27 36 45 54 81 
# multiples of 9 always add to give 9.

# and for the number ie not divisible by 9.
# eg - 20 = 2 + 0 = 2
#      21 = 2 + 1 = 3
#      22 = 2 + 2 = 22

#      so we also See 
#      20 % 9 = 2
#      21 % 9 = 3
#      22 % 9 = 4
# so if that number is 0, return 0
# if that number is divisble by 9, then answer is 9
# if not, then answer is the remainder of the number % 9.

def divide(number):
    if number == 0:
        return 0
    elif number % 9 == 0:
        return 9
    else:
        return number % 9
print(divide(25))









    
    