import math
def primenumber(number):
    for element in range(2, number //2): # instead of going up to n//2 we can just go up to square root + 1 of that number, it is the same.
        if number % element == 0:
            print ("False")
            break
        
    else:
        print(True)
    return ""
#print(primenumber(18))

def primenumber2(number):
    for element in range(2, int(math.sqrt(number))+1):
        print(element)
        if number % element == 0:
            print("False")
            break
        
    else:
        print('True')
    return ""
#print(primenumber2(17))

#ultimate process --
def primenumber3(number):
    if number <= 1:
        return False
    if number <= 3:  # so we have manually checked number between 0 and 3.
        return True
    if number % 2 == 0 and number % 3 == 0: # here we check if that number is divided by 2 or 3 then here we return false statement
        return False
    # if number is divided vy 4,8,-- it is also divided by 2 and if the number is divided by 6,9.-- it is also divided by 3.so we can skip these number
    # as we have already checked by 2 and 3.
    for element in range(5, int(math.sqrt(number))+1, 6):
         # keeping the difference of 6 because between 5 and 11, evertyhing is checked above and 7 is left.
         if number % element == 0 or number % (element + 2) == 0:
             return False
    return True

print(primenumber3(17))
# so we start from 5 and we check if it is divisible by 5, no needed for 6 as 3 has already checked , 7  is obtained by (element + 2), 8 by 2, 9 by 3,10,by 
# 2 and 11 is obtained from loop.
# and 
def prime(list):
    result = []
    result.append(2)
    for element in range(3, list + 1):
        for value in range(2, element//2):
            if element % value == 0:
                break
        else:
            result.append(element)
    return result
#print(prime(25))

