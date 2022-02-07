#from stack import Stack
# def convert(number):
#     s = Stack()
#     while number > 0:
       
#         remainder = number % 2
#         s.push(remainder)
#         number = number // 2
#     result = ""
#     while s.is_empty()  == False:
#         result += str(s.pop())
#     return result


    
def convertToBinary(number):
    # Write your code here
    s =[]
    while number > 0:
        remainder = number % 2
        s.append(remainder)
        number = number // 2
    print(s)
    result = ""
    while len(s) > 0:
        result += str(s.pop())
    print(result)
    return result

