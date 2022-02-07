#def integertostring(integer):
# note.
# .join function is only for iterables not for integers. 
# list = [1,2,3,4]
# return .join(list) - error because it is number it should be string instead.

# chr function. '
# chr function takes a integer and gives the chracters.
# eg chr(48) = "0" chr(49) = "1"

# Concept.
# getting a string from integer.
# ord "0" = 48 s0,
# chr(ord("0") + 1) = chr(48+1) = chr(49) = "1"

# Overall, diving the number and getting the remainder, changing it into string and keeping them in list, reversing the list and returning it.

def integertostring(integer):
    is_negative = False
    if integer < 0:
        integer = integer * -1 # we want to make it positive becasue if num is negative taking the remainder will give error.
        is_negative = True
    else:
        is_negative = False
    # getting the remainder.
    list = []
    while integer > 0:
        remainder = integer % 10
        list.append(chr(ord("0") + remainder))
        integer = integer // 10
    
    #reversing the list.
    answer = list[: : -1]
    result = "".join(answer)
    

    if is_negative == True:
        return "-" + result
    return result
   

print(integertostring(-1234))

    
