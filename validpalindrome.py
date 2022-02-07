def validpalindrome(s):
    result = ""
    for element in s:
        if element.isalnum():
            result += element.lower()
    start = 0
    end = len(result) - 1
    while start < end:
        if result[start] == result[end]:
            start += 1
            end -= 1
        else:
            return False
    return True
    
#print(validpalindrome("A man, a plan, a canal: Panama"))

#palindrome of string.
# The idea is to reverse the integer using the mathematical process ie divide by 10 and add remainder .
# Also if original number is negative, although the number matches after reversing, return False.
def palindromeofinteger(number):
    if int(number) == 0: # This case handels the cases like 00000, 00 - all will be true.
        return True
    if number < 0:
        return False
    original_number = number
    result = 0
    while number > 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10
    
    if original_number== result:
        return True
    return False
    
print(palindromeofinteger(1111111))
#