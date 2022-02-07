#UMPIRE
# Given a number, return the next smallest prime number
#What if the number is negative?? - make it positive and solve it.
#what if the number is 0 ? -- return 2
# input - 3 --- output -- 5
# input - 7 --- output -- 11
# input - 13 --- output -- 17

#idea.
# 3 ---4,5,6,7,8 and so on
# 1) can iterate towards the right side of the number and check if it is a prime number or not and if it is a prime number, return it else go to the anot
# her number.
# how can i check if 4 is a prime number or not.
#  start from 2 and check the remainder and go up to the that number -1 and 
# 2)for loop'


def nearst_prime_number(number):
    if number == 0:
        return 2
    for element in range(number + 1, 2**32): 
        for value in range(2, element//2): 
            if element % value == 0:
                break
        else:
            return element

print(nearst_prime_number(17))

def nearest_prime_number2(number):
    count = 1
    number = number + count
    print(number)
 
    for element in range(2,number):
        print(number)
        print(element)
        if number % element == 0:
            number = number + count
            break
    else:
        return number
#print(nearest_prime_number2(5))

# number = 6//original
# number = 7
