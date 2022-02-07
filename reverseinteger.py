def reverseinteger(num):
   
        value = str(num)
        result = ''
        for element in range(len(value)-1,-1,-1):
            if value[element] == "-":
                result = value[element] + result
            else:
                result = result + value[element]
        if int(result) > 2**31 or int(result) < -2**31:
            return 0
        return int(result)

def reverseit(num):
    if num < 0:
        value = num * (-1)
    else:
        value = num
    result = 0

    
    while value > 0:
        remainder = value % 10
        value= value // 10
        result = result * 10 + remainder
    if result > 2**31 or result < -2**31:
            return 0
    if num > 0:
        return result
    if num < 0:
        return result * (-1)
    
print(reverseit(-124))






#Reverse a integer.
# 123 -- 321
# -123 -- -321
# 12900 -- 921
# 000 -- 0
# 0 -- 0

# 1 2 3 -- 3 2 1
# 1 2 3 4 5 -- 5 4 3 2    1

# interger:
# 00992 -- int() -- 992
# list = [1,2,3]

# 1)convert integer to list and reverse them and later again convert them to integer. 

def reverseinteger(integer):
    list = []
    value = str(integer)
    for element in value:
        if element != "-":
            list.append(element)
    
    start = 0
    end = len(list)-1
    while start < end:
        temp = list[start]
        list[start] = list[end]
        list[end] = temp
        start += 1
        end -= 1
    #result = ""
    #print(list)
    result = "".join(list)
    if integer < 0:
        return int(int(result)* -1)
    return int(result)
#print(reverseinteger(0))

  
#reverse a float number.
# 12345.678
# 1)idea is multiply the number by some multiples of 10 unitl it becomes a integer. so here we multiply by 1000 because there are three zeroes after decimal.
# then after having integer, reverse it as usual . now we have 87654321
# 2)and divide it by some number by same 1000. no it will not be correct.
# 3)Divide it by 10^(total length of the decimal exluding point - length of numbers after point) do so math you will see beauty why.

# so we need total length of the decimal exluding point and length of numbers after point we should keep track both of them.

def reversefloat(number):
    # first change the number to decimal.
    s = 0
    while number != int(number):
        number = number * 10
        s += 1 # Here s will keep track of the how many numbers are there after decimal becuase we will multiply that much time by 10.
    # now number is changed to integer and let us reverse it.


    
    # In python float * integer = float so we need to convert it to integer
    integer_number = int(number)
    
    result = 0
    length = 0
    print(integer_number)
    while integer_number > 0:
        remainder = integer_number % 10
        print(remainder)
        result = result * 10 + remainder
        integer_number = integer_number // 10
        length += 1
    print(result)

    return (result/(10**(length-s)))
#print(reversefloat(12345667.89))


def pracitse(s):
    result = ""
    count = 0
    for element in range(0, len(s)):
        if element == len(s) - 1:
            result += s[element]
            return result
        elif s[element] != s[element + 1]:
            result += str(count)
            count = 0
        else:
            result += s[element]
            count += 1
  
# print(pracitse("aaaabbbccccdd"))


    
