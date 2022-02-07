# The idea is 
# 123  can be obtained as 1*10**2 + 2*10**1 + 3*10**0 ie 100 + 20 + 3 --- 123
# so similar to school's math put the power of 10 from back starting from 0.

# #ord function.
# Python ord() function returns the Unicode code from a given character. 
# This function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument.
# ord("0") - 48
# ord("1") - 49
# ord("2") - 50
# ord("3") - 51
# ord ("32") - error

def convertstringtointeger(strings):
    is_negative = False
    index = 0
    result = 0
    #handling the negative or postive cases.
    if strings[0] == "-":
        index += 1
        is_negative = True
    else:
        index = 0
        is_negative = False
    # Here, i can do it in my way to. for list[i] == "-": continue and so on.
    for element in range(index, len(strings)):
        place = 10**(len(strings)-(element+1))
        digit = ord(strings[element]) - ord("0") #because ord("1") = 49 and ord("0") = 48 so 49-48 = 1
        result = result + (place * digit)
    print(is_negative)
    if is_negative == True:
        return -1 * result
    return result
print(convertstringtointeger("-1234"))

#print(convertstringtointeger("21474836460"))

        

